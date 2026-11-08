#!/usr/bin/env python3
"""Deterministic motion / performance / accessibility / anti-slop audit for web UI code.

Usage:
    python3 flagship_audit.py <path> [--json] [--min-severity P3] [--ignore RULE,RULE]

Scans .html .htm .vue .svelte .astro .jsx .tsx .js .ts .mjs .css .scss .mdx files.
Exit code 1 when any P0/P1 finding exists (CI-friendly), 0 otherwise.

Rules are regex heuristics with file:line attribution. They flag *tells*, not verdicts:
read each finding in context before changing code. No network, no LLM.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict

EXTS = {".html", ".htm", ".vue", ".svelte", ".astro", ".jsx", ".tsx", ".js", ".ts", ".mjs", ".css", ".scss", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", ".svelte-kit", ".astro", "out", "coverage", ".turbo", "vendor", ".output", "storybook-static"}
MAX_FILE_BYTES = 2_000_000
SEVERITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


@dataclass
class Finding:
    rule: str
    severity: str
    file: str
    line: int
    message: str
    fix: str
    snippet: str


# (rule_id, severity, compiled regex, message, fix, which extensions ('*' = all, 'style' = css-like+markup, 'script' = js-like+markup))
STYLE_EXTS = {".css", ".scss", ".vue", ".svelte", ".astro", ".html", ".htm", ".jsx", ".tsx", ".mdx"}
SCRIPT_EXTS = {".js", ".ts", ".mjs", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".html", ".htm", ".mdx"}
MARKUP_EXTS = {".html", ".htm", ".vue", ".svelte", ".astro", ".jsx", ".tsx", ".mdx"}

LINE_RULES = [
    # ---------------- Motion & rendering pipeline ----------------
    ("M02", "P2", re.compile(r"transition\s*:\s*all\b|transition-property\s*:\s*all\b|\btransition-all\b"), STYLE_EXTS,
     "`transition: all` animates unrelated properties (including layout) and makes interruption unpredictable.",
     "List the properties explicitly: `transition: transform var(--duration-fast) var(--ease-out), opacity ...`."),
    ("M03", "P2", re.compile(r"transition\s*:\s*[^;{}]*\b(width|height|top|left|right|bottom|margin[a-z-]*|padding[a-z-]*|box-shadow|border-width)\b"), {".css", ".scss", ".vue", ".svelte", ".astro", ".html"},
     "Transitioning a layout/paint property (width/height/top/left/margin/box-shadow) runs on the main thread and janks on mid-range phones.",
     "Animate `transform`/`opacity`; use `grid-template-rows: 0fr→1fr` or `interpolate-size` for height; fade a pseudo-element for shadows."),
    ("M03K", "P2", re.compile(r"(?<![\w-])(?:width|height|top|left|margin[a-z-]*|box-shadow)\s*:"), {".css", ".scss"},
     "Layout/paint property inside a @keyframes block (heuristic: only flagged when inside `@keyframes`).",
     "Rewrite keyframes with `transform`/`opacity`/`clip-path`."),
    ("M05", "P1", re.compile(r"setPixelRatio\s*\(\s*(window\.)?devicePixelRatio\s*\)"), SCRIPT_EXTS,
     "Uncapped devicePixelRatio: 3× DPR phones shade 9× the fragments and throttle within seconds.",
     "`renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))` (1.5 during active scroll on mobile)."),
    ("M07", "P2", re.compile(r"""['"](@studio-freight/lenis|framer-motion|aos|scrollmagic|wowjs|wow\.js|scrollreveal|react-beautiful-dnd|react-window|hammerjs|locomotive-scroll@4|tailwindcss-animate|react-transition-group|react-flip-toolkit|popmotion|velocity-animate|jquery)['"]"""), SCRIPT_EXTS | {".json"},
     "Legacy or renamed package imported.",
     "Use the maintained successor: lenis, motion (`motion/react`), native scroll-driven animations/IntersectionObserver, dnd-kit/Pragmatic DnD, TanStack Virtual, Pointer Events/@use-gesture, tw-animate-css."),
    ("M07B", "P3", re.compile(r"\bTweenMax\b|\bTweenLite\b|\bTimelineMax\b"), SCRIPT_EXTS,
     "GSAP 2 API (TweenMax/TweenLite) is dead.",
     "Use GSAP 3 `gsap.to/from/timeline` and register only the plugins used."),
    ("M08", "P2", re.compile(r"<video\b(?![^>]*\bmuted\b)[^>]*\bautoplay\b|<video\b[^>]*\bautoplay\b(?![^>]*\bmuted\b)"), MARKUP_EXTS,
     "Autoplay video without `muted` will be blocked by browsers and is an a11y problem (sound on autoplay).",
     "`<video muted autoplay loop playsinline poster=...>` and pause offscreen / under reduced motion."),
    ("M08B", "P3", re.compile(r"<video\b(?![^>]*\bposter=)[^>]*\bautoplay\b"), MARKUP_EXTS,
     "Autoplay video without a `poster`: nothing meaningful paints before the video decodes (LCP, reduced motion).",
     "Add a `poster` that matches frame 0 (< 50 KB WebP/AVIF)."),
    ("M10", "P0", re.compile(r"maximum-scale\s*=\s*1(\.0)?\b|user-scalable\s*=\s*(no|0)\b"), MARKUP_EXTS | {".ts", ".js"},
     "Viewport blocks pinch-zoom: fails WCAG 1.4.4 Resize Text and is hostile on mobile.",
     "Remove `maximum-scale`/`user-scalable=no` from the viewport meta."),
    ("M11", "P1", re.compile(r"outline\s*:\s*(none|0)\b|\boutline-none\b"), STYLE_EXTS,
     "Focus outline removed. Unless a `:focus-visible` replacement exists nearby, keyboard users lose their position.",
     "Keep `:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }` (3:1 contrast) and remove outlines only for `:focus:not(:focus-visible)`."),
    ("M13", "P1", re.compile(r"\bgsap\.(to|from|fromTo|timeline|set)\s*\("), {".jsx", ".tsx"},
     "GSAP call in a React component without a visible `useGSAP`/`gsap.context` in the file: animations and ScrollTriggers leak across remounts.",
     "Wrap in `useGSAP(() => {...}, { scope })` from `@gsap/react` or `gsap.context()` with `ctx.revert()` on cleanup."),
    ("M14", "P1", re.compile(r"new\s+Lenis\s*\(\s*\{[^}]*autoRaf\s*:\s*true"), SCRIPT_EXTS,
     "Lenis `autoRaf: true` while the project also uses `gsap.ticker` = two animation loops racing (micro-jitter at 120 Hz).",
     "`new Lenis({ autoRaf: false })` and drive `lenis.raf(time * 1000)` from `gsap.ticker.add()`; `gsap.ticker.lagSmoothing(0)`."),
    ("M15", "P2", re.compile(r"addEventListener\s*\(\s*['\"](scroll|touchstart|touchmove|wheel)['\"]\s*,\s*[^,)]+\)"), SCRIPT_EXTS,
     "Scroll/touch/wheel listener without `{ passive: true }` can block scrolling and hurt INP.",
     "Add `{ passive: true }` (or use IntersectionObserver / scroll-driven animations / ScrollTrigger)."),
    ("M16", "P2", re.compile(r"@font-face\s*\{(?![^}]*font-display)[^}]*\}", re.S), {".css", ".scss"},
     "@font-face without `font-display`: invisible text or layout shift during font load.",
     "Add `font-display: swap` (or `optional` for zero CLS) plus `size-adjust`/`ascent-override` metric fallbacks."),
    ("M17", "P3", re.compile(r"fonts\.googleapis\.com"), MARKUP_EXTS | {".css"},
     "Google Fonts via CDN: extra origin, privacy implications, no subsetting control.",
     "Self-host (Fontsource, next/font) with preload and unicode-range subsets."),
    ("M18", "P2", re.compile(r"cursor\s*:\s*none\b"), STYLE_EXTS,
     "Custom cursor (`cursor: none`) without a pointer guard breaks touch devices and reduced-motion users.",
     "Scope to `@media (hover: hover) and (pointer: fine)` and disable under `prefers-reduced-motion`."),
    ("M19", "P2", re.compile(r"\.currentTime\s*=\s*[^;]*(progress|scroll)", re.I), SCRIPT_EXTS,
     "Scrubbing `<video>.currentTime` from scroll is decode-bound and janky.",
     "Use a WebP/AVIF frame sequence on `<canvas>`, or encode all-keyframe video (`ffmpeg -g 1 -keyint_min 1`)."),
    ("M20", "P2", re.compile(r"animation\s*:\s*[^;]*\binfinite\b"), {".css", ".scss", ".vue", ".svelte", ".astro"},
     "Infinite CSS animation: confirm it pauses offscreen, on hover (if a marquee), and under reduced motion (WCAG 2.2.2).",
     "Guard with `@media (prefers-reduced-motion: reduce) { animation: none }`, pause via IntersectionObserver, and provide controls for > 5 s motion."),
    ("M21", "P3", re.compile(r"\bease\s*:\s*['\"](bounce|elastic)[.\w]*['\"]|\bease-(bounce|elastic)\b|\banimate-bounce\b"), SCRIPT_EXTS | STYLE_EXTS,
     "Bounce/elastic easing: cartoonish on surfaces and task UI.",
     "Use `expo.out`/`power4.out` or a spring with `bounce: 0–0.2`; reserve bounce for tiny playful accents."),
    ("M22", "P3", re.compile(r"(?<![-\w])ease-in-out\b|ease\s*:\s*['\"]power1\.inOut['\"]"), STYLE_EXTS | SCRIPT_EXTS,
     "Stock `ease-in-out` on UI motion feels sluggish at start.",
     "Entrances: `cubic-bezier(0.22, 1, 0.36, 1)` or `expo.out`; moves: `cubic-bezier(0.65, 0, 0.35, 1)`; scrubs: `none`."),
    ("M23", "P2", re.compile(r"loading\s*=\s*['\"]lazy['\"]"), MARKUP_EXTS,
     "`loading=\"lazy\"` found. Fine below the fold; harmful on the LCP element or inside/above pinned ScrollTrigger sections (pin drift).",
     "Remove from hero/LCP media and pinned sections; set `fetchpriority=\"high\"` on the LCP image; call `ScrollTrigger.refresh()` after assets load."),
    ("M24", "P2", re.compile(r"<img\b(?![^>]*\b(width|height)\s*=)(?![^>]*\bclass\s*=\s*['\"][^'\"]*\b(aspect-|size-|h-\d|w-\d))[^>]*>"), MARKUP_EXTS,
     "`<img>` without intrinsic `width`/`height` (or an aspect-ratio class): layout shift (CLS).",
     "Add `width`/`height` attributes or `aspect-ratio`; use the framework image component."),
    ("M25", "P3", re.compile(r"will-change\s*:"), STYLE_EXTS,
     "`will-change` present. More than 2–5 promoted layers exhausts mobile GPU memory.",
     "Apply only right before motion and remove after; never on `*` or large lists."),
    ("M26", "P3", re.compile(r"backdrop-filter\s*:(?!\s*none\b)|\bbackdrop-blur"), STYLE_EXTS,
     "Backdrop blur. Expensive on iOS when regions are large or overlap; glass as a default surface is a slop tell.",
     "Limit area and count; solid fallback for `prefers-reduced-transparency`; use glass only where layering is meaningful."),
    ("M27", "P2", re.compile(r"\bsetAnimationLoop\s*\(|requestAnimationFrame\s*\(\s*(function|\w+\s*=>|\w+\s*\))"), SCRIPT_EXTS,
     "A self-scheduling animation loop. If GSAP/Lenis also tick, this is a second loop (dual-ticker jitter).",
     "Drive renderer/lenis/DOM updates from one `gsap.ticker.add()` callback; cancel on teardown."),
    ("M28", "P2", re.compile(r"\bscrub\s*:\s*true\b"), SCRIPT_EXTS,
     "`scrub: true` ties motion 1:1 to raw scroll; no physical weight.",
     "Use `scrub: 0.5–1.2` for a catch-up buffer (keep `ease: 'none'` on scrubbed tweens)."),
    # ---------------- Accessibility ----------------
    ("A01", "P1", re.compile(r"<(div|span)\b[^>]*\bon[Cc]lick\s*=(?![^>]*\brole=)(?![^>]*\btabIndex|[^>]*\btabindex)"), MARKUP_EXTS,
     "Clickable `<div>`/`<span>` without role/tabindex: unreachable by keyboard and nameless to screen readers.",
     "Use `<button>` (actions) or `<a href>` (navigation)."),
    ("A02", "P2", re.compile(r"<a\b[^>]*\bhref\s*=\s*['\"]#['\"]"), MARKUP_EXTS,
     "`<a href=\"#\">` is a button in disguise and scrolls to top.",
     "Use `<button type=\"button\">` or a real destination."),
    ("A03", "P1", re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>"), MARKUP_EXTS,
     "`<img>` without `alt`.",
     "Describe meaningful images; `alt=\"\"` for decorative ones."),
    ("A04", "P3", re.compile(r"z-index\s*:\s*(9{3,}|[1-9]\d{3,})\b|\bz-\[?\s*9{3,}"), STYLE_EXTS,
     "Magic z-index (9999…): no layering system.",
     "Use z-index tokens (`--z-dropdown: 100`, `--z-modal: 300`, `--z-toast: 400`) and `@layer`."),
    ("A05", "P3", re.compile(r"!important"), {".css", ".scss", ".vue", ".svelte", ".astro"},
     "`!important` present.",
     "Fix specificity with `@layer` ordering and scoped selectors."),
    ("A06", "P2", re.compile(r"<(button|a)\b(?![^>]*\b(aria-label|aria-labelledby|title)\s*=)[^>]*>\s*<(svg|i|span|[A-Z]\w*Icon)\b[^>]*/?>(?:\s*</(svg|i|span|[A-Z]\w*Icon)>)?\s*</(button|a)>"), MARKUP_EXTS,
     "Icon-only control without visible text (heuristic). Needs an accessible name.",
     "Add `aria-label`, visually-hidden text, or a tooltip with a keyboard-triggered equivalent."),
    ("A07", "P2", re.compile(r"<input\b(?![^>]*\b(aria-label|aria-labelledby|id)\s*=)[^>]*\btype\s*=\s*['\"](text|email|password|search|tel|url|number)['\"][^>]*>"), MARKUP_EXTS,
     "Text input without `id` (for a `<label for>`) or an aria label.",
     "Pair with a persistent visible `<label>`; placeholders supplement, never replace."),
    ("A08", "P2", re.compile(r"\bplaceholder\s*=\s*['\"][^'\"]+['\"](?![^>]*\baria-label)"), MARKUP_EXTS,
     "Placeholder present (check that a persistent label also exists; placeholder-only labels vanish on typing).",
     "Keep a visible label; use `:placeholder-shown` only for floating-label styling."),
    ("A09", "P1", re.compile(r"\btabindex\s*=\s*['\"]?[1-9]\d*"), MARKUP_EXTS,
     "Positive `tabindex` breaks natural focus order.",
     "Use `tabindex=\"0\"`/`-1` and DOM order."),
    ("A10", "P2", re.compile(r"<(h[1-6])\b[^>]*>\s*(<img|<svg)"), MARKUP_EXTS,
     "Heading containing only an image/icon.",
     "Headings need text (visually hidden if necessary)."),
    # ---------------- Anti-slop (design tells) ----------------
    ("S01", "P3", re.compile(r"\bbg-clip-text\b|background-clip\s*:\s*text|-webkit-background-clip\s*:\s*text"), STYLE_EXTS,
     "Gradient/clipped text: the most recognizable AI-generated headline tell.",
     "Solid ink; earn contrast with size, weight, measure, and one accent used once."),
    ("S02", "P3", re.compile(r"\bfrom-(purple|indigo|violet|fuchsia)-\d+\b.*\bto-(pink|blue|cyan|purple|indigo|fuchsia)-\d+\b|\bvia-purple-|linear-gradient\([^)]*#(8b5cf6|a855f7|7c3aed|6366f1|ec4899|d946ef)"), STYLE_EXTS,
     "Purple/indigo → pink/blue gradient: default starter palette.",
     "One OKLCH accent with semantic roles; let imagery carry color; derive states with `color-mix()`."),
    ("S03", "P1", re.compile(r"lorem ipsum|dolor sit amet", re.I), MARKUP_EXTS | {".ts", ".js", ".json"},
     "Placeholder copy. The page was not designed with content.",
     "Use real copy or clearly mark what the user must supply."),
    ("S04", "P2", re.compile(r"<(h[1-6]|button|a|span|li)\b[^>]*>[^<]*[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\u2728]"), MARKUP_EXTS,
     "Emoji used as an icon or inside headings/controls.",
     "Use one SVG icon family (Lucide/Phosphor/Material Symbols) with consistent stroke and labeling."),
    ("S05", "P3", re.compile(r"font-family\s*:\s*['\"]?(Inter|Roboto|Arial|Helvetica|system-ui|-apple-system)\b"), STYLE_EXTS,
     "Default typeface declared. Fine as the text face; a slop tell if it is the only voice.",
     "Pair a display face with a text workhorse; use variable axes, optical sizing, tracking on display."),
    ("S06", "P3", re.compile(r"background(-color)?\s*:\s*#000(000)?\b|\bbg-black\b|background(-color)?\s*:\s*black\b"), STYLE_EXTS,
     "Pure black background: flat dark mode without a surface model.",
     "Near-black base (`oklch(15% …)` / `#090A0F`), lighter surfaces for elevation, alpha borders, glows instead of shadows."),
    ("S07", "P3", re.compile(r"\brounded-(2xl|3xl)\b[^\"']*\bshadow-(lg|xl|2xl)\b|\bshadow-(lg|xl|2xl)\b[^\"']*\brounded-(2xl|3xl)\b"), MARKUP_EXTS,
     "`rounded-2xl` + `shadow-lg/xl` card recipe (uniform elevation = template look).",
     "Radius tokens with nested-radius math; 2–3 layered tinted shadows only on raised surfaces; borders as alpha `color-mix`."),
    ("S08", "P2", re.compile(r">\s*(Get Started|Learn More|Submit|Click Here|Read More|Sign Up Now|Discover More)\s*<", re.I), MARKUP_EXTS,
     "Generic CTA copy.",
     "Name the outcome: \"Start free trial\", \"Create project\", \"See pricing\"."),
    ("S09", "P2", re.compile(r"\b(Welcome to|Revolutioni[sz]e|Unleash|Supercharge|Elevate your|Seamless(ly)?|cutting[- ]edge|next[- ]level|game[- ]chang(er|ing)|Empower(ing)? your|Unlock the power)\b", re.I), MARKUP_EXTS,
     "Marketing-slop phrase.",
     "Specific over clever; numbers over adjectives; what, for whom, outcome."),
    ("S10", "P3", re.compile(r"\bborder-l-4\b|border-left\s*:\s*[4-8]px\s+solid"), STYLE_EXTS,
     "Side-stripe border (Bootstrap-era alert/card affordance; Impeccable tell).",
     "Tinted surface + 1 px border + leading icon."),
    ("S11", "P2", re.compile(r"(via\.placeholder\.com|placeholder\.com|placehold\.co|picsum\.photos|unsplash\.com/random|loremflickr|dummyimage\.com|placekitten)"), MARKUP_EXTS | {".ts", ".js", ".json", ".css"},
     "Placeholder image service.",
     "Use real product media or mark assets the user must supply."),
    ("S12", "P3", re.compile(r"\banimate-pulse\b"), MARKUP_EXTS,
     "Pulse skeleton/shimmer. Only for loads > ~300 ms and only matching final layout.",
     "Show skeletons after a delay; prefer streaming/optimistic UI; never endless shimmer."),
    ("S13", "P3", re.compile(r"\btext-center\b[^\"']*\bmx-auto\b[^\"']*\bmax-w-"), MARKUP_EXTS,
     "Centered-everything section pattern (heuristic).",
     "Vary alignment and density per section; asymmetry with purpose; subgrid-aligned content."),
    ("S14", "P3", re.compile(r"\bgrid-cols-3\b[^\"']*\bgap-\d+"), MARKUP_EXTS,
     "Three-column grid (check it is not three identical icon cards: 'Fast · Secure · Scalable').",
     "Show the feature working; outcomes with evidence; bento with real micro-interactions."),
]

# Project-level rules (need whole-corpus knowledge)
PROJECT_RULES_DOC = {
    "P01": ("P1", "Animations/transitions exist but no `prefers-reduced-motion` handling was found anywhere.",
            "Add a global `@media (prefers-reduced-motion: reduce)` block and `gsap.matchMedia()` / `useReducedMotion()` branches."),
    "P02": ("P1", "Multiple self-scheduling animation loops detected across the project (rAF loops, `setAnimationLoop`, Lenis `autoRaf`, plus GSAP ticker).",
            "Consolidate into one `gsap.ticker.add()` callback: `lenis.raf(time*1000)` → DOM/3D sync → `renderer.render()`."),
    "P03": ("P2", "`will-change` declared on many selectors.",
            "Keep to 2–5 elements, applied just-in-time."),
    "P04": ("P2", "Many `backdrop-filter`/`backdrop-blur` usages: glass is being used as the default surface.",
            "Reserve glass for floating nav/overlays; borders + tinted shadows or surface lift elsewhere."),
    "P05": ("P3", "No `:focus-visible` style found while `outline: none` is used.",
            "Add a visible focus ring (2 px, 3:1) on `:focus-visible`."),
    "P06": ("P3", "No `text-wrap: balance`/`pretty` and no `tabular-nums` found.",
            "Set `text-wrap: balance` on headings, `pretty` on body, `font-variant-numeric: tabular-nums` on numeric data."),
    "P07": ("P3", "No `@layer` and no CSS custom properties for tokens found in stylesheets.",
            "Define `--space-*`, `--radius-*`, `--shadow-*`, `--duration-*`, `--ease-*`, semantic color roles; order `@layer reset, tokens, base, components, utilities`."),
}


def iter_files(root: str):
    if os.path.isfile(root):
        yield root
        return
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext in EXTS or (ext == ".json" and fn == "package.json"):
                p = os.path.join(dirpath, fn)
                try:
                    if os.path.getsize(p) <= MAX_FILE_BYTES:
                        yield p
                except OSError:
                    continue


def line_of(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def snippet_at(text: str, idx: int) -> str:
    start = text.rfind("\n", 0, idx) + 1
    end = text.find("\n", idx)
    if end == -1:
        end = len(text)
    s = text[start:end].strip()
    return (s[:140] + "…") if len(s) > 140 else s


def block_spans(text: str, opener: str):
    """Return (start, end) spans of CSS blocks whose at-rule prelude matches `opener`."""
    spans = []
    for m in re.finditer(opener + r"[^{]*\{", text):
        depth, i = 1, m.end()
        while i < len(text) and depth:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        spans.append((m.start(), i))
    return spans


def audit(root: str, ignore: set[str]) -> tuple[list[Finding], dict]:
    findings: list[Finding] = []
    stats = Counter()
    corpus_flags = defaultdict(int)
    files_scanned = 0

    for path in iter_files(root):
        ext = os.path.splitext(path)[1].lower()
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            continue
        files_scanned += 1
        rel = os.path.relpath(path, root if os.path.isdir(root) else os.path.dirname(root) or ".")
        kf_spans = block_spans(text, r"@keyframes\b") if ext in {".css", ".scss"} else []
        rm_spans = block_spans(text, r"@media\b[^{]*prefers-reduced-motion") if ext in STYLE_EXTS else []
        seen: set[tuple[str, int]] = set()

        # corpus-level signals
        if re.search(r"prefers-reduced-motion|useReducedMotion|matchMedia\s*\(\s*['\"]\(prefers-reduced-motion|prefersReducedMotion|reducedMotion", text):
            corpus_flags["reduced_motion"] += 1
        if re.search(r"\btransition\s*:|@keyframes|\bgsap\.|\banimate\(|motion\.|<motion\.|animation-timeline|animate=", text):
            corpus_flags["has_motion"] += 1
        if re.search(r"gsap\.ticker\.add", text):
            corpus_flags["gsap_ticker"] += 1
        corpus_flags["raf_loops"] += len(re.findall(r"\bsetAnimationLoop\s*\(|requestAnimationFrame\s*\(\s*(function|\w+\s*=>|\w+\s*\))", text))
        corpus_flags["lenis_autoraf"] += len(re.findall(r"new\s+Lenis\s*\(\s*\{[^}]*autoRaf\s*:\s*true", text))
        corpus_flags["will_change"] += len(re.findall(r"will-change\s*:", text))
        corpus_flags["backdrop"] += len(re.findall(r"backdrop-filter\s*:(?!\s*none\b)|\bbackdrop-blur", text))
        if re.search(r":focus-visible", text):
            corpus_flags["focus_visible"] += 1
        if re.search(r"outline\s*:\s*(none|0)\b|\boutline-none\b", text):
            corpus_flags["outline_none"] += 1
        if re.search(r"text-wrap\s*:\s*(balance|pretty)|\btext-(balance|pretty)\b", text):
            corpus_flags["text_wrap"] += 1
        if re.search(r"tabular-nums", text):
            corpus_flags["tabular"] += 1
        if ext in {".css", ".scss"}:
            if re.search(r"@layer\b", text):
                corpus_flags["layer"] += 1
            if re.search(r"--(space|radius|shadow|duration|ease|color|bg|fg)[\w-]*\s*:", text):
                corpus_flags["tokens"] += 1
        has_gsap_react_cleanup = bool(re.search(r"useGSAP\s*\(|gsap\.context\s*\(", text))

        for rule, sev, rx, exts, msg, fix in LINE_RULES:
            if rule in ignore or ext not in exts:
                continue
            if rule == "M13" and has_gsap_react_cleanup:
                continue
            if rule == "M14" and corpus_flags["gsap_ticker"] == 0 and "gsap" not in text:
                continue  # only a dual-loop problem when GSAP is also present
            for m in rx.finditer(text):
                idx = m.start()
                if rule == "M03K":
                    if not any(a <= idx < b for a, b in kf_spans):
                        continue
                if rule == "M11":
                    # skip if a :focus-visible rule exists in the same file
                    if re.search(r":focus-visible", text):
                        continue
                if rule in ("A05", "M20") and any(a <= idx < b for a, b in rm_spans):
                    continue  # `!important` / animation overrides inside a reduced-motion block are the right pattern
                ln = line_of(text, idx)
                if (rule, ln) in seen:
                    continue  # one finding per rule per line
                seen.add((rule, ln))
                findings.append(Finding(rule, sev, rel, ln, msg, fix, snippet_at(text, idx)))
                stats[rule] += 1

    # project-level findings
    proj: list[Finding] = []

    def add_proj(rule):
        if rule in ignore:
            return
        sev, msg, fix = PROJECT_RULES_DOC[rule]
        proj.append(Finding(rule, sev, "(project)", 0, msg, fix, ""))

    if corpus_flags["has_motion"] and not corpus_flags["reduced_motion"]:
        add_proj("P01")
    loops = corpus_flags["raf_loops"] + corpus_flags["lenis_autoraf"] + (1 if corpus_flags["gsap_ticker"] else 0)
    if loops >= 2:
        add_proj("P02")
    if corpus_flags["will_change"] > 5:
        add_proj("P03")
    if corpus_flags["backdrop"] > 4:
        add_proj("P04")
    if corpus_flags["outline_none"] and not corpus_flags["focus_visible"]:
        add_proj("P05")
    if files_scanned and not corpus_flags["text_wrap"] and not corpus_flags["tabular"] and corpus_flags["has_motion"]:
        add_proj("P06")
    if any(os.path.splitext(p)[1].lower() in {".css", ".scss"} for p in iter_files(root)) and not corpus_flags["layer"] and not corpus_flags["tokens"]:
        add_proj("P07")

    findings = proj + findings
    summary = {
        "files_scanned": files_scanned,
        "by_severity": dict(Counter(f.severity for f in findings)),
        "by_rule": dict(Counter(f.rule for f in findings)),
        "signals": dict(corpus_flags),
    }
    return findings, summary


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--min-severity", default="P3", choices=["P0", "P1", "P2", "P3"], help="hide findings below this severity")
    ap.add_argument("--ignore", default="", help="comma-separated rule ids to skip")
    ap.add_argument("--max-per-rule", type=int, default=25, help="cap listed findings per rule in text output")
    args = ap.parse_args()

    if not os.path.exists(args.path):
        print(f"error: path not found: {args.path}", file=sys.stderr)
        sys.exit(2)

    ignore = {r.strip().upper() for r in args.ignore.split(",") if r.strip()}
    findings, summary = audit(args.path, ignore)
    maxsev = SEVERITY_ORDER[args.min_severity]
    findings = [f for f in findings if SEVERITY_ORDER[f.severity] <= maxsev]
    findings.sort(key=lambda f: (SEVERITY_ORDER[f.severity], f.rule, f.file, f.line))

    if args.json:
        print(json.dumps({"summary": summary, "findings": [asdict(f) for f in findings]}, indent=2))
    else:
        sev_line = " ".join(f"{k}:{v}" for k, v in sorted(summary["by_severity"].items())) or "no findings"
        print(f"flagship_audit · {summary['files_scanned']} files · {sev_line}")
        print()
        shown = Counter()
        current = None
        for f in findings:
            if f.rule != current:
                current = f.rule
                print(f"[{f.severity}] {f.rule}  {f.message}")
                print(f"      fix: {f.fix}")
            if shown[f.rule] < args.max_per_rule:
                loc = f"{f.file}:{f.line}" if f.line else f.file
                print(f"      - {loc}" + (f"  · {f.snippet}" if f.snippet else ""))
            elif shown[f.rule] == args.max_per_rule:
                print(f"      - … {summary['by_rule'][f.rule] - args.max_per_rule} more")
            shown[f.rule] += 1
        print()
        print("Severity: P0 blocking · P1 fix before shipping · P2 fix before polish · P3 judgment call / tell.")
        print("Heuristics, not verdicts: read each finding in context. See references/anti-slop.md and references/performance-accessibility.md.")

    sys.exit(1 if any(f.severity in ("P0", "P1") for f in findings) else 0)


if __name__ == "__main__":
    main()
