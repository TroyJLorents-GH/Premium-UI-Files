#!/usr/bin/env node
/**
 * audit-ui.mjs — static scan for motion, performance, and accessibility anti-patterns
 * in CSS/HTML/JS/TS/JSX/TSX/Vue/Svelte/Astro files.
 *
 * Usage:  node scripts/audit-ui.mjs <dir-or-file> [--json] [--all]
 *   --json  machine-readable output
 *   --all   include "info" findings (default prints warn + error)
 *
 * It is a heuristic net, not a verdict: every finding points at a line to look at.
 * Exit code 1 when any "error" finding exists, else 0.
 */
import { promises as fs } from "node:fs";
import path from "node:path";

const EXTS = new Set([".css", ".scss", ".html", ".htm", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".astro", ".mdx"]);
const IGNORE_DIRS = new Set(["node_modules", ".git", "dist", "build", ".next", ".nuxt", ".svelte-kit", ".astro", "out", "coverage", ".turbo", ".vercel", "public"]);

const RULES = [
  // ---- motion / rendering ----
  { id: "transition-all", level: "warn", re: /transition\s*:\s*all\b|transition-property\s*:\s*all\b|\btransition-all\b/g,
    why: "`transition: all` animates layout properties you did not intend and hides what owns each property. List the properties." },
  { id: "layout-prop-transition", level: "error", re: /transition(?:-property)?\s*:[^;{}]*\b(width|height|top|left|right|bottom|margin[a-z-]*|padding[a-z-]*|box-shadow|border-width)\b/g,
    why: "Transitioning a layout/paint property runs layout or paint every frame. Use transform/opacity, grid-template-rows 0fr→1fr, interpolate-size, or FLIP; cross-fade a pseudo-element for shadows." },
  { id: "keyframe-layout-prop", level: "warn", re: /@keyframes[\s\S]{0,400}?\b(width|height|top|left|margin[a-z-]*|box-shadow)\s*:/g,
    why: "Keyframes that change layout/paint properties jank on mid-range phones. Prefer transform/opacity." },
  { id: "animate-height-js", level: "warn", re: /\.(height|width|top|left)\s*=\s*[`'"]?\$?\{?[^;]*px/g,
    why: "Writing width/height/top/left per frame in JS forces layout. Use transform (translate/scale) or FLIP." },
  { id: "scroll-listener-layout-read", level: "warn", re: /addEventListener\(\s*['"]scroll['"][\s\S]{0,600}?getBoundingClientRect/g,
    why: "Layout reads inside a scroll handler force synchronous layout on every tick. Use IntersectionObserver, ScrollTrigger, or CSS scroll-driven animations." },
  { id: "multiple-raf-loops", level: "info", re: /requestAnimationFrame\(|setAnimationLoop\(/g, aggregate: true, threshold: 2,
    why: "More than one animation loop in a codebase is a dual-ticker risk (Lenis + GSAP + Three). Drive everything from one gsap.ticker or one rAF." },
  { id: "lenis-autoraf", level: "warn", re: /new\s+Lenis\s*\((?![\s\S]{0,200}autoRaf\s*:\s*false)/g,
    why: "Lenis with its own rAF loop desyncs from GSAP/Three. Use `new Lenis({ autoRaf: false })` and call lenis.raf from gsap.ticker." },
  { id: "video-currenttime-scrub", level: "warn", re: /\.currentTime\s*=\s*[^;]*(?:progress|scroll)/gi,
    why: "Scrubbing <video>.currentTime from scroll is decode-bound and janky unless the file is all-keyframes (-g 1). Prefer a canvas image sequence." },
  { id: "uncapped-dpr", level: "warn", re: /setPixelRatio\(\s*(?:window\.)?devicePixelRatio\s*\)/g,
    why: "Uncapped devicePixelRatio renders 9–12x fragments on 3x phones. Use Math.min(devicePixelRatio, 2)." },
  { id: "bounce-elastic-ease", level: "info", re: /\b(elastic|bounce)\.(in|out|inOut)\b|ease:\s*['"](elastic|bounce)/g,
    why: "Elastic/bounce eases read as cartoonish on large surfaces; reserve for tiny playful elements." },
  { id: "ease-in-enter", level: "info", re: /\.(from|fromTo)\([\s\S]{0,300}?ease\s*:\s*['"][a-z0-9]+\.in['"]/g,
    why: "Entering with ease-in feels sluggish. Enter with ease-out (expo.out / power4.out)." },
  { id: "hover-scale-105", level: "info", re: /hover:scale-10[5-9]|hover:scale-11\d/g, aggregate: true, threshold: 4,
    why: "`hover:scale-105` on many elements is a slop tell. Use a 2px lift and a shadow cross-fade, and reserve scale for one or two elements." },
  { id: "will-change-global", level: "warn", re: /^\s*(\*|body|html|div|\.[a-z-]*card[a-z-]*)\s*\{[^}]*will-change\s*:/gm,
    why: "Broad will-change promotes many layers and exhausts mobile GPU memory. Apply to 2–5 elements right before they animate." },
  { id: "backdrop-filter-count", level: "info", re: /backdrop-filter\s*:\s*blur|backdrop-blur-/g, aggregate: true, threshold: 6,
    why: "Many backdrop-filter surfaces are expensive, especially on iOS. Limit count and area; provide a solid prefers-reduced-transparency fallback." },
  { id: "svg-filter-on-large", level: "info", re: /filter\s*:\s*url\(#/g,
    why: "SVG filters (goo, displacement, grain) run on the CPU. Keep them on small elements and off scroll paths." },

  // ---- reduced motion / a11y ----
  // (reduced-motion coverage is checked repo-wide after the scan; see below)
  { id: "outline-none", level: "error", re: /outline\s*:\s*(none|0)\b(?![^}]*focus-visible)|\boutline-none\b(?![^"']*focus-visible)/g,
    why: "Removing outlines without a :focus-visible replacement hides keyboard focus. Add a visible focus ring." },
  { id: "maximum-scale", level: "error", re: /maximum-scale\s*=\s*1(\.0)?|user-scalable\s*=\s*(no|0)/g,
    why: "Blocking zoom fails WCAG 1.4.4. Remove maximum-scale/user-scalable." },
  { id: "div-button", level: "warn", re: /<div[^>]*\bonClick=|<div[^>]*\bonclick=|<span[^>]*\bonClick=/g,
    why: "Clickable div/span has no keyboard or role semantics. Use <button> or <a>." },
  { id: "autoplay-unmuted", level: "error", re: /<video(?![^>]*\bmuted)[^>]*\bautoplay/gi,
    why: "Autoplaying video with sound is blocked by browsers and violates expectations. Add muted (and playsinline, poster)." },
  { id: "marquee-no-pause", level: "info", re: /animation\s*:[^;]*infinite(?![\s\S]{0,400}(hover|paused|animation-play-state))/g,
    why: "Infinite loops (marquees, beams) need pause on hover/off-screen and a reduced-motion stop (WCAG 2.2.2 if longer than 5 s)." },
  { id: "aria-hidden-focusable", level: "warn", re: /aria-hidden=["']true["'][^>]*>[\s\S]{0,300}?<(a|button|input|select|textarea)\b/g,
    why: "A focusable element inside aria-hidden creates an invisible tab stop (common in SplitText duplicates). Keep one coherent reading and keyboard path." },
  { id: "img-no-dimensions", level: "info", re: /<img(?![^>]*\b(width|height|aspect-ratio|fill)\b)[^>]*>/g,
    why: "Images without dimensions cause CLS. Set width/height or aspect-ratio." },
  { id: "lazy-lcp-risk", level: "info", re: /<img[^>]*\b(loading=["']lazy["'])[^>]*(hero|banner|lcp|poster)/gi,
    why: "A lazy-loaded hero image delays LCP. Use fetchpriority=\"high\" and no loading=\"lazy\" on the LCP element." },

  // ---- slop tells ----
  { id: "gradient-text", level: "info", re: /bg-clip-text|background-clip\s*:\s*text/g, aggregate: true, threshold: 2,
    why: "Gradient text on multiple headings is a recognizable AI default. One accent, used once." },
  { id: "purple-blue-gradient", level: "info", re: /from-(purple|violet|indigo)-\d+\s+(via-[a-z]+-\d+\s+)?to-(blue|cyan|pink|fuchsia)-\d+/g,
    why: "The purple→blue gradient is the single most recognized slop palette. Choose a direction and encode it in tokens." },
  { id: "lorem-ipsum", level: "warn", re: /lorem ipsum/gi,
    why: "Placeholder copy hides layout problems and ships by accident. Use real content or marked placeholders." },
  { id: "marketing-cliche", level: "info", re: /\b(Unlock the power|Seamlessly|Elevate your|Supercharge|Take .{1,30} to the next level|Revolutionize)\b/gi,
    why: "Generic marketing cliché. Say specifically what the product does." },
  { id: "emoji-icons", level: "info", re: /<(h\d|span|div|p)[^>]*>\s*[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/gu, aggregate: true, threshold: 3,
    why: "Emoji as icons render differently per platform and read as unfinished. Use one icon set." },
  { id: "body-overflow-x-hidden", level: "warn", re: /(?:^|[}\s,])(?:html|body)\s*(?:,\s*(?:html|body)\s*)?\{[^}]*overflow(?:-x)?\s*:\s*(?:hidden|clip)/gm,
    why: "overflow-x: hidden on html/body hides horizontal overflow instead of fixing it (3D stages, marquees, bleeding figures). Find the element; verify document.documentElement.scrollWidth === innerWidth at 390 px." },
  { id: "copy-names-position", level: "info", re: />[^<{}]*\b(?:at|on|to) the (?:left|right)\b[^<]*<|>[^<{}]*\b(?:at|on) (?:left|right)\b[^<]*<|>[^<{}]*\b(?:shown|chart|panel|demo|diagram|figure) (?:below|above)\b[^<]*</gi,
    exts: new Set([".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro", ".mdx"]),
    why: "Copy that names a layout position breaks when the layout reflows at a breakpoint. Describe the thing, not where it sits." },
];

async function walk(p, out) {
  const st = await fs.stat(p);
  if (st.isFile()) { if (EXTS.has(path.extname(p).toLowerCase())) out.push(p); return; }
  for (const e of await fs.readdir(p, { withFileTypes: true })) {
    if (e.isDirectory()) { if (!IGNORE_DIRS.has(e.name)) await walk(path.join(p, e.name), out); }
    else if (EXTS.has(path.extname(e.name).toLowerCase())) out.push(path.join(p, e.name));
  }
}

function lineOf(src, idx) { let n = 1; for (let i = 0; i < idx && i < src.length; i++) if (src.charCodeAt(i) === 10) n++; return n; }

async function main() {
  const args = process.argv.slice(2);
  const json = args.includes("--json"), all = args.includes("--all");
  const target = args.find((a) => !a.startsWith("--")) || ".";
  const files = []; await walk(path.resolve(target), files);
  const findings = []; const aggregates = new Map();
  const ANIMATES = /@keyframes|transition\s*:|\.animate\(|gsap\.|useGSAP|<motion\.|animate=\{|ScrollTrigger|new Lenis/;
  const HANDLES_RM = /prefers-reduced-motion|useReducedMotion|reducedMotion|matchMedia\(\s*\{|MotionConfig/;
  // Signals that the page has choreography beyond fade-up: a timeline, scroll scrubbing/pinning, split text, or scroll-driven CSS.
  const CHOREOGRAPHY = /gsap\.timeline|ScrollTrigger|scrub\s*:|pin\s*:\s*true|SplitText|animation-timeline\s*:|view\(\)|scroll\(\)|useScroll|whileInView|Flip\.|DrawSVG|requestAnimationFrame\(|translateZ\(|stroke-dashoffset|@property\s/;
  const HAS_MARKUP = /<(main|section|header|h1)\b/;
  let animatingFiles = 0, reducedMotionHandled = false, markupFiles = 0, choreographyFound = false;

  for (const f of files) {
    let src; try { src = await fs.readFile(f, "utf8"); } catch { continue; }
    if (ANIMATES.test(src)) animatingFiles++;
    if (HANDLES_RM.test(src)) reducedMotionHandled = true;
    if (HAS_MARKUP.test(src)) markupFiles++;
    if (CHOREOGRAPHY.test(src)) choreographyFound = true;
    const ext = path.extname(f).toLowerCase();
    for (const r of RULES) {
      if (r.exts && !r.exts.has(ext)) continue;
      r.re.lastIndex = 0; let m; let count = 0;
      while ((m = r.re.exec(src))) {
        count++;
        if (!r.aggregate) findings.push({ id: r.id, level: r.level, file: f, line: lineOf(src, m.index), why: r.why, match: m[0].slice(0, 80) });
        if (m.index === r.re.lastIndex) r.re.lastIndex++;
      }
      if (r.aggregate && count) { const a = aggregates.get(r.id) || { rule: r, count: 0, files: new Set() }; a.count += count; a.files.add(f); aggregates.set(r.id, a); }
    }
  }
  for (const [, a] of aggregates) if (a.count >= a.rule.threshold)
    findings.push({ id: a.rule.id, level: a.rule.level, file: `${a.files.size} file(s)`, line: 0, why: `${a.rule.why} (${a.count} occurrences)` });
  if (animatingFiles > 0 && !reducedMotionHandled)
    findings.push({ id: "no-reduced-motion", level: "error", file: `${animatingFiles} animating file(s)`, line: 0,
      why: "Nothing in the scanned tree checks prefers-reduced-motion (CSS media query, gsap.matchMedia, useReducedMotion, MotionConfig). Design the reduced composition as a fallback derived from the full experience: fades only, no parallax, pinning, loops, or large travel." });
  if (markupFiles > 0 && !choreographyFound)
    findings.push({ id: "no-choreography", level: "info", file: `${markupFiles} page file(s)`, line: 0,
      why: "No timeline, scroll-scrubbed/pinned chapter, split-text reveal, or scroll-driven CSS found. On a landing, marketing, launch, portfolio, or experiential page that fails the motion floor (hero sequence, one set piece, named micro-interactions; see references/signature-motion.md). Expected on apps, dashboards, and docs." });

  const order = { error: 0, warn: 1, info: 2 };
  const shown = findings.filter((x) => all || x.level !== "info").sort((a, b) => order[a.level] - order[b.level] || a.file.localeCompare(b.file) || a.line - b.line);

  if (json) { console.log(JSON.stringify({ scanned: files.length, findings: shown }, null, 2)); }
  else {
    console.log(`audit-ui: scanned ${files.length} files, ${shown.length} findings${all ? "" : " (use --all to include info)"}\n`);
    for (const x of shown) console.log(`[${x.level.toUpperCase()}] ${x.id}  ${x.file}${x.line ? ":" + x.line : ""}\n    ${x.why}${x.match ? `\n    > ${x.match}` : ""}\n`);
    const hidden = findings.length - shown.length; if (hidden) console.log(`(${hidden} info findings hidden)`);
    console.log("Static checks only: this never judges whether motion is good, only how it goes wrong. Capture browser frames (hero over time, several scroll depths, 1440x900 and 390x844) per references/performance-a11y.md §8 before claiming the page moves, is smooth, or is accessible.");
  }
  process.exit(shown.some((x) => x.level === "error") ? 1 : 0);
}
main().catch((e) => { console.error(e); process.exit(2); });
