---
name: flagship-ui-design
description: Design and build flagship-grade, award-level websites, landing pages, web apps and UI sections with real art direction, physics-based motion, and zero AI-slop. Use this skill whenever the user wants a premium, polished, high-end, "Awwwards", Linear/Vercel/Stripe-quality, or non-generic interface; asks for a hero, bento grid, nav, pricing page, dashboard, scroll experience, page transition, or animated component; mentions GSAP, ScrollTrigger, Lenis, Motion, Framer Motion, Three.js, shaders, View Transitions, 120Hz, or smooth scroll; wants a redesign of something that "looks like AI made it", bland, templated or flat; or needs design references from Refero, Mobbin, 21st.dev or Impeccable. Also use it to review or elevate an existing UI. Trigger even when the user only says "make it look better", "make it feel premium", or "build me a landing page" without naming any tool.
---

# Flagship UI Design

Build interfaces that feel authored, not generated. The difference between a flagship site and a template is almost never the framework: it is **a committed point of view, real content, disciplined motion, and verified craft**. This skill is the operating procedure for getting there, and a router into a large reference library so you load only what the task needs.

## The five commitments

1. **Direction before decoration.** Pick a visual world on purpose (see `references/workflow.md`). Never default to the median look: purple/blue gradient on near-black, Inter everywhere, three identical feature cards, a glowing orb. Those are the tells of slop (`references/anti-slop.md`).
2. **Platform first, library second, custom engine last.** CSS / View Transitions / scroll-driven animation → Motion or GSAP → Three.js / shaders. Every added dependency must earn its bytes.
3. **Motion is information.** Each animation says something: weight, hierarchy, causality, where to look next. One hero effect, one navigation idea, two or three micro-interactions per page. More reads as noise (`references/motion-system.md`).
4. **Real content, real states.** Design with authentic copy and data. Empty, loading, error, long-string, offline and reduced-motion states are part of the design, not afterthoughts.
5. **Verify in a browser.** Nothing is "done" until it has been rendered, looked at on desktop and mobile, and checked against the gates in `references/quality-gates.md`. Report what you actually checked.

## Workflow

Run these phases in order. Skip a phase only when the user already supplied its output (e.g. they brought a brief or a Figma).

### 0. Orient (fast, no questions yet)
- Look at the project: stack, existing tokens, `PRODUCT.md` / `DESIGN.md` (Impeccable context files), fonts, components, content. Don't treat a missing DESIGN.md as "greenfield" automatically.
- Classify the surface by mode: **Persuade** (landing, marketing, pricing: design is the product), **Operate** (app UI, dashboards: scanability and consistency outrank expression), **Read** (docs, articles), **Experience** (portfolio, showcase: artifact leads, UI recedes). The mode sets how bold motion may be.

### 1. Brief
Fill the brief in `references/workflow.md` §Brief. Ask the user only for what would change the architecture (audience, primary action, brand constraints, target devices, delivery stack). For everything else state an assumption and proceed. If the user gave no direction, propose 2–3 distinct directions in one short message and pick the strongest as default rather than blocking.

### 2. Research and references (use the tools, don't guess)
Ground the direction in real examples before writing code. Route per `references/tool-integrations.md`:
- **Refero Styles / Refero MCP**: pull a production DESIGN.md-style system close to the target mood (tokens, type, spacing).
- **Mobbin**: real flows, screens and sections for the component or journey at hand.
- **21st.dev** (`21st search`, `21st get`, `21st add`): component sources to adapt (never paste unreviewed).
- **Impeccable**: the design-direction and critique engine (`shape`, `critique`, `audit`, `polish`, `animate`, `typeset`, `layout`, `harden`, `optimize`).
- **Higgsfield**: generated imagery/video only when real assets are unavailable, and **only after announcing the purpose and estimated credit cost and getting a yes** (protocol in `references/tool-integrations.md`).
Summarize what you borrowed and what you deliberately changed. Borrow structure and principles, never clone a brand's identity.

### 3. Stack decision
Choose the smallest stack that satisfies the brief using `references/stack-selection.md`. Name the primary component system, the single principal motion engine, the scroll strategy, and anything exotic (WebGL, Rive) with its fallback. State one-line reasons.

### 4. Design system first
Define tokens before screens: OKLCH color roles (neutrals tinted toward the brand hue, one accent used sparingly), a type scale (fluid `clamp()`, 2 families max, real optical hierarchy), 4/8pt spacing, radii that nest (`outer = inner + padding`), elevation recipe, motion tokens (durations, easings, springs). Put them in CSS custom properties / `@theme`. Self-host fonts with metric-matched fallbacks.

### 5. Build
- Semantic HTML first; ARIA only to fill gaps. Mobile-first, container queries for components.
- Compose sections from `references/section-playbook.md` (hero, nav, bento, cards, overlays, forms, footer). Pick patterns that serve the story, not every pattern available.
- Implement motion from `references/motion-system.md`. For GSAP specifics (ScrollTrigger, SplitText, Flip, DrawSVG, MorphSVG, Observer, etc.) read `references/gsap-playbook/INDEX.md` and open only the plugin reference you need. Read `references/gsap-playbook/source-caveats.md` before adapting any captured demo code: several have known defects.
- Smooth scroll (Lenis) only when it improves this experience; wire it to a single ticker (see motion-system.md) and keep a static/native fallback.
- Use `assets/motion-lab-reference.html` as a working reference for 120Hz-grade patterns (Houdini `@property` beams, spotlight borders, etc.). Read it for technique; do not copy its brand ("AETHER") or palette into user work.

### 6. Verify (one batched pass, not an open-ended loop)
Render it. Capture desktop and mobile together. Run the gates in `references/quality-gates.md` (squint test, reduced-motion emulation, keyboard tab-through, CPU-throttled performance trace, CLS/LCP/INP sanity, console clean). Fix everything found in one batch, confirm once, stop.

### 7. Report
Say what was built, which references informed it, what was verified and how, and what was not verified (e.g. no real-device 120Hz test). Distinguish "adapted from reference", "written new", and "runtime-verified".

## Non-negotiables (and why)

- **Animate only `transform`, `opacity`, `clip-path`, and small `filter`s on the hot path.** Layout-triggering properties drop frames on mid-range phones; budget is 8.3 ms/frame at 120Hz.
- **Every effect respects `prefers-reduced-motion`** with a meaningful alternative (crossfade or instant state), via CSS media query or `gsap.matchMedia()`. Premium that fails accessibility is a liability.
- **One owner per animated property.** Two systems fighting over `transform` is the most common source of jitter and "mystery" bugs.
- **One animation clock.** If Lenis + GSAP + WebGL are present, drive them from `gsap.ticker`, not three `requestAnimationFrame` loops.
- **Clean up.** Use `gsap.context()` / `useGSAP()`, revert SplitText, kill observers, dispose Three.js geometries/materials/textures on unmount.
- **No fake content in shipped work.** No lorem ipsum, invented testimonials, invented metrics or logos of real companies as endorsements. Use clearly marked placeholders when real data is missing and tell the user.
- **Never exceed the user's brief on cost.** Paid generation (Higgsfield) and hosted services require an announced estimate and confirmation first.
- **Respect licenses.** GSAP is free but not OSI-open-source (no use in a competing visual animation builder). React Bits / Vue Bits are MIT + Commons Clause. Theatre.js studio is AGPL. Check before bundling copied component source.

## Choosing how deep to go

| Request | Do |
|---|---|
| "Make this look more premium" (existing UI) | Phases 0, 2 (light), then Impeccable `critique` → targeted fixes → verify. Preserve working behavior and copy. |
| One component (button, card, nav, modal) | Phases 0, 4 (tokens only), 5, 6. Check states + keyboard + reduced motion. |
| Full landing page / site | All phases. Direction and design system are mandatory. |
| Scroll-driven / 3D / cinematic piece | All phases + read the 3D budgets and failure modes in `references/motion-system.md` and `references/sources/foundation-principles-of-motion.md`. |
| Review/audit only | Impeccable `audit` + `critique`, `references/quality-gates.md`, report findings ordered by severity. Don't rewrite unasked. |

## Reference map (load on demand)

| Need | Open |
|---|---|
| What counts as slop and its replacements | `references/anti-slop.md` |
| Brief template, direction picking, Impeccable command sequence | `references/workflow.md` |
| Refero / Mobbin / 21st / Impeccable / Higgsfield / Lenis usage and protocols | `references/tool-integrations.md` |
| Timing numbers, easings, springs, choreography, single-ticker, Lenis, reduced motion, 3D budgets | `references/motion-system.md` |
| Which library for which job; legacy to avoid | `references/stack-selection.md` |
| Pattern-by-pattern build recipes for every page section | `references/section-playbook.md` |
| Performance, accessibility, verification checklists | `references/quality-gates.md` |
| Any GSAP plugin or demo | `references/gsap-playbook/INDEX.md` |
| Deep source material (large; grep, don't read whole) | `references/sources/` — see `references/sources/README.md` for a section index |
| 341-row tool catalog with verification status | `references/sources/tool-index.csv` (grep by name or category) |

When a recommendation depends on a library's current API or version, check the official docs (Context7 or the library site) before writing code. The sources here are a dated snapshot (6 Nov 2026) and rows marked `R` in the catalog were not individually verified.
