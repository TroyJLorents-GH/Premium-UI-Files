# Workflow integrations

Agent skills guide the work; MCP integrations expose tools and data; registries distribute source; runtime libraries ship in the product. Different layers, even when one vendor offers several. Use **one lead design workflow per pass**; stacking several design skills produces contradictory instructions.

## Impeccable (design vocabulary + slop detector)

Open-source (Apache-2.0) skill for coding agents: a design director's judgment, 20+ named commands, a 62-rule deterministic slop detector (no LLM), and PRODUCT.md/DESIGN.md project context. Strongest on interfaces that already exist.

**Sequence that works**

1. `init` once per project → writes `PRODUCT.md` (who it is for, what it must do, constraints). Every later command reads it.
2. `document` → captures the existing visual system as `DESIGN.md` so changes stay on-brand. (`extract` pulls tokens.)
3. `shape` → plan UX/UI before implementation; discovers the task, then enters new-work for visual-world decisions.
4. `critique` → scores UX against usability heuristics and ranks fixes. `audit` → accessibility, performance, theming, responsive; findings P0 (blocking) → P3 (polish).
5. Focused passes: `typeset` (fonts, hierarchy, sizing) · `layout` (spacing, rhythm) · `colorize` · `animate` (transitions, interaction feedback) · `delight` · `overdrive` (shaders, springs, scroll effects; use sparingly) · `bolder` / `quieter` · `distill` (remove what the page does not need) · `clarify` (copy) · `harden` (errors, i18n, overflow, edge cases) · `adapt` (screens and devices) · `optimize` (loading and rendering) · `polish` (final pass).
6. `doctor` reports drift between artifacts; `hooks` manages the auto-detector; `pin <command>` creates a `/command` shortcut.

Modes: **Persuade** (landing/marketing) · **Operate** (apps/dashboards) · **Read** (docs/editorial) · **Experience** (portfolios). This skill uses the same vocabulary.

Rules of engagement: narrow targets beat whole pages; verify rendered results at shipped sizes; batch checks. Read Impeccable's live-copy/hook permissions before enabling them (its README documents a fallback that can launch a local agent with approval-bypass flags). Impeccable's detector and `scripts/flagship_audit.py` overlap on slop tells but differ on motion/3D rules; run both when both are available.

## Refero Styles (DESIGN.md library)

Free (beta) library of 2,000+ design systems extracted from real product sites, each as a DESIGN.md (YAML-ish tokens + prose semantics), with CSS-variable and Tailwind v4 exports and an MCP server. DESIGN.md as a format was open-sourced by Google Stitch; Refero's files lack the official YAML front matter, so convert if a tool expects spec compliance.

**How to use it well**

1. Choose by **density and tone** (landing vs dashboard vs docs vs onboarding), not by brand name.
2. Read the prose first: it carries intent ("acid lime is a functional flashlight, not decoration") that tokens cannot.
3. Map colors by function (canvas, content surface, readable text, selected state, action) onto the project's semantic roles; record which face owns display vs reading text and the paragraph measure.
4. Apply one pass of typography + whitespace to an existing mediocre screen before anything else; it is the highest-return use.
5. **Copy the system, never the website.** Tokens are public data; logos, trademarks, illustrations, and look-alike reproduction are not. The result must be recognizably the user's product.

## Mobbin (real screens and flows; MCP available)

Search real web/iOS screens, full user journeys, and component flows for the *same surface and task* (checkout, onboarding, settings, pricing). Use it to ground information architecture, state coverage (empty, error, loading), and interaction conventions, and to save references into collections with notes. Screenshots are pattern evidence; they do not prove a pattern works for this audience. Cite screens by their Mobbin URL; download `image_url` for docs rather than hot-linking (URLs expire).

## 21st.dev (component marketplace + CLI + review)

- `21st init --design-context` → `.21st/design.json` (framework, Tailwind version, shadcn setup, tokens, primitives, with evidence) + `.21st/DESIGN.md`; edit `constraints.must`, `constraints.avoid`, `decisions`; `--refresh`/`--check` later.
- `21st search "<need>" --context auto` (components, themes, templates; free) → `21st get <id>` (code + demo; metered on free tier) → `21st add <user>/<slug>` (installs through the shadcn registry) or `21st add @<registry>` for a whole registry.
- `21st theme <id>` (free CSS), `21st logo <brand>` (SVG URLs), bookmarks/lists for research.
- `21st review src/ [--fix] [--json]` → local, free, deterministic a11y/interaction/responsive/motion/design-system findings with file:line; suppress only with a reason comment.
- `21st generate "<section>" --context auto --variants 3` requires AI credits; check `21st usage` first.
- `21st skills install` / `21st skills catalog` manage first-party and vetted external skills (external installs are project-local and explicit).

Everything installed is **owned code**: audit motion, focus, reduced motion, dependencies, and license before shipping. Pull from React Bits, Magic UI, Aceternity, Motion Primitives, Cult UI, Kokonut etc. through 21st.dev or their repos with the same discipline.

## Lenis

Optional smooth scroll for marketing/experiential surfaces. Drive it from `gsap.ticker` (`autoRaf: false`), forward `lenis.on('scroll', ScrollTrigger.update)`, set `gsap.ticker.lagSmoothing(0)`. Honors `prefers-reduced-motion` by default (lerp → 1, instant programmatic scroll) while continuing to run for WebGL sync. Options to know: `lerp`, `duration`/`easing`, `anchors`, `autoToggle`, `allowNestedScroll`, `stopInertiaOnNavigate`, `prevent(node)`, `syncTouch` (off unless tested), `data-lenis-prevent`. No native CSS scroll-snap (use the snap plugin). Adapters: `lenis/react`, `lenis/vue`, `lenis/nuxt`, Framer. Package is `lenis` (not `@studio-freight/lenis`). Locomotive Scroll v5 is a declarative wrapper on Lenis. Never on content-heavy apps or inside native webviews with their own overscroll physics.

## GSAP plugin playbook (bundled)

`references/gsap-playbook/INDEX.md` routes to captured demos and prompts for every plugin. Before adapting any captured code read `source-caveats.md` (mislabeled sections, repeated demos, implicit globals, duplicated IDs, accessibility defects in the nested-link SplitText example, mixed version strings). Extract the smallest behavior, scope selectors, own cleanup, verify at real sizes. Captured versions are not recommendations; inspect the project lockfile.

## Higgsfield (image and video generation)

Platform with 50+ image/video models (Soul, Seedance, Kling, Wan, Recraft, Ideogram…), reachable via web, MCP (Claude), CLI, and a separate pay-per-generation API (USD balance, published per-model rates, failed requests refunded). MCP/CLI/API generations **always** spend credits or dollars; only the website has free/unlimited pools.

**Protocol (mandatory)**

1. Prefer the user's authentic assets. Generation is for missing hero media, product scenes, ambient loops, texture plates, or storyboard frames when nothing real exists.
2. Before generating, state in one block: **purpose** (where it will be used), **model** and settings (resolution, duration, aspect), **count** including likely retries (budget 2–4 attempts per usable clip), and **estimated cost** (credits or USD from the model's published rate; e.g., a short 1080p clip has run ~20 credits ≈ $1 on recent checks; verify the current rate on the Generate button or API catalog).
3. Wait for explicit approval. Then generate, review against the brief (lighting direction, silhouette, palette match to tokens, no text artifacts), and optimize for delivery (AVIF/WebP ≤ 200 KB, video ≤ 2 MB with poster, pause offscreen, reduced-motion fallback).
4. Report what was generated, what it cost, and rights (Higgsfield terms grant usage rights to generated content; still avoid brand look-alikes and real-person likenesses).

## Other references the user may supply

- Argon's "Master UI/UX & Motion Engineering" Google Site and the AETHER 120 Hz motion-lab HTML page: technique references only. Reuse the ideas (Houdini `@property` beams, spotlight cards, single-ticker lab), never the brand, palette, or copy.
- Project `PRODUCT.md`, `DESIGN.md`, `.21st/design.json`, Storybook, token files: read before proposing anything; preserve working capabilities and factual claims.

## Galleries for direction (not for copying)

Awwwards, Godly, CSS Design Awards, Minimal Gallery, Siteinspire, Curated Design, Landing.love (award-level motion/layout) · Mobbin, Refero, Page Flows, Nicelydone (real flows) · Land-book, Lapa Ninja, SaaSFrame (landing pages) · Design Spells, Rauno's craft, Linear/Vercel/Raycast changelogs (micro-interaction details) · Codrops, Three.js examples, Shadertoy (creative references). Design-engineering voices: Emil Kowalski, Rauno Freiberg, Josh Comeau, Adam Argyle, Bramus Van Damme, Jhey Tompkins, Olivier Larose, Bruno Simon.
