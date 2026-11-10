# Quality gates

Run these before calling anything done. Do them as one batched pass: render, capture desktop + mobile, check, fix everything in one batch, confirm once. Report what you did and did not verify.

## Contents
- Creative and choreographic audit
- Performance budgets
- Accessibility
- States and resilience
- Motion engineering audit
- Browser verification recipe
- UX laws as review lenses
- Report template

## Creative and choreographic audit
- [ ] **Squint test:** one unmistakable focal point per viewport.
- [ ] **Swap test:** the design is not interchangeable with a competitor's after swapping logo/copy.
- [ ] **Slop scan:** run `anti-slop.md`; no generic gradient/orb/three-card skeleton, no lorem, no invented proof.
- [ ] **Velocity check:** objects initiate fast and settle softly; nothing stops with a clunk.
- [ ] **Text stability:** body copy is stationary after its entrance (<0.8 s).
- [ ] **Restraint:** ≤1 hero effect, ≤1 navigation idea, 2–3 micro-interactions per page.
- [ ] **Copy:** specific, verb-led CTAs, numbers over adjectives, microcopy beside risk.

## Performance budgets

| Metric | Target | Notes |
|---|---|---|
| LCP | ≤2.5 s (aim 1.5 s) | `fetchpriority="high"` on hero, no lazy-load on LCP element, preload hero font |
| INP | ≤200 ms (aim 100 ms) | `scheduler.yield()`, no heavy handlers, visual feedback on pointer-down |
| CLS | ≤0.1 (aim 0) | `aspect-ratio`, reserved skeletons, metric-matched fallback fonts, `scrollbar-gutter: stable` |
| Frame budget | 16.7 ms @60 Hz, 8.3 ms @120 Hz | Long animation frames >50 ms are INP culprits |
| JS (mobile initial) | ≤~300 KB compressed; motion libs lazy | Dynamic `import()` after idle/interaction |
| Hero media | image ≤~200 KB AVIF; video ≤~2 MB; 3D ≤~3–4 MB | Poster first, then enhance |

Thresholds are measured at the 75th percentile of field data, mobile and desktop separately. Some blogs claim tighter 2026 thresholds; treat as unverified and check web.dev/vitals before quoting.

Checks:
- [ ] Chrome DevTools Performance with **CPU 4× slowdown + Fast 4G**, record a full scroll: no long-task (>50 ms) triangles, no layout-thrash/purple spikes in scroll scrubbing.
- [ ] Rendering panel: paint flashing and layer borders show no layer explosion.
- [ ] Off-screen things paused (canvas, Lottie/Rive, marquees, video).
- [ ] Images AVIF/WebP with `srcset/sizes`, width/height set; fonts subset, preloaded.
- [ ] For WebGL: `renderer.info.render.calls` <60; textures return to 0 after unmount; DPR clamped.
- [ ] Test (or explicitly state not tested) on a mid-range Android and a 120 Hz device.

## Accessibility (WCAG 2.2 AA is the bar)
- [ ] Semantic HTML first; landmarks; skip link; headings in order.
- [ ] Keyboard: everything reachable/operable, visible `:focus-visible` (≥2 px, 3:1), logical order, Escape closes overlays, focus restored to trigger, focus not obscured by sticky UI (2.4.11).
- [ ] No keyboard trap inside pinned/scroll-jacked sections; focus does not enter off-screen animated elements.
- [ ] Contrast 4.5:1 text, 3:1 large text and UI/graphics; verified in light, dark and `forced-colors`.
- [ ] Targets ≥24×24 CSS px (AA minimum), ≥44 px on touch where possible; drag interactions have a non-drag alternative (2.5.7).
- [ ] Text resizes to 200%, reflows at 320 CSS px, survives text-spacing overrides; no `maximum-scale`.
- [ ] `prefers-reduced-motion` emulated (DevTools → Rendering): parallax, pinning, camera moves, looping removed; crossfades remain.
- [ ] Anything moving >5 s can pause (2.2.2); ≤3 flashes/s (2.3.1); autoplaying carousels have a visible pause.
- [ ] Reduced transparency/contrast: solid fallback for glass UI.
- [ ] Split text reads as full sentences to a screen reader; no duplicate tab stops.
- [ ] Forms: persistent labels, associated errors (`aria-describedby`), no cognitive-test-only auth, paste allowed.
- [ ] Live regions (`aria-live="polite"`) for toasts and counters.
- [ ] Automated axe/Lighthouse run (finds only ~30–40% of issues) plus a manual screen-reader smoke test when feasible.

## States and resilience
- [ ] Empty, loading (skeleton only after ~300 ms), error (cause + fix + retry), success (next action), offline/slow.
- [ ] Long strings, 2-line vs 1-line titles, missing images, RTL/localized text expansion where relevant.
- [ ] Rapid repeated input, interrupted animations, route changes and remounts do not leak or double-run.
- [ ] Destructive actions: undo preferred over confirm; type-to-confirm only for catastrophic.
- [ ] No dark patterns (confirmshaming, fake urgency, hidden costs).

## Motion engineering audit
- [ ] Only transform/opacity/clip-path/small filters on hot path.
- [ ] One owner per animated property; no CSS-vs-JS fights.
- [ ] Exactly one master loop (`grep requestAnimationFrame|setAnimationLoop`).
- [ ] All GSAP inside `gsap.context()` / `useGSAP()` / `gsap.matchMedia()`; SplitText reverted; observers killed; `ScrollTrigger.refresh()` after fonts/media.
- [ ] Reversal/interruption works at any frame; replays don't duplicate side effects.
- [ ] `will-change` scoped and removed.

## Browser verification recipe
1. Start the dev server (preview tool). 2. Screenshot desktop (≈1440) and mobile (≈390) at top, mid, and bottom of the page, plus key interactive states (hover/focus/open). 3. Read the console (must be clean). 4. Emulate reduced motion and re-capture. 5. Tab through the page. 6. Run Lighthouse / perf trace if the surface is performance-sensitive. Use `chrome-devtools-mcp` skills (`a11y-debugging`, `debug-optimize-lcp`, `memory-leak-debugging`) when available.

## UX laws as review lenses
Fitts (large near targets), Hick (fewer choices, one primary CTA per section), Jakob (follow conventions), Doherty (<400 ms response, optimistic UI), Miller (chunk), Peak-end (invest in success and exit moments), Von Restorff (one distinct CTA), Tesler (absorb complexity in defaults), Postel (accept messy input). Response-time tiers: <100 ms instant, <1 s flow, >1 s progress indicator, >10 s notify.

## Report template

```
Built: <what, where>
Direction: <world in one sentence> · type <A + B> · palette <roles> · motion <signature>
Borrowed from: <Refero style / Mobbin flow / 21st component / etc.> → <what changed>
Stack: <primary components> · <motion engine> · <scroll> · <exotic + fallback>
Verified: <viewports, states, reduced-motion, keyboard, perf numbers, tools used>
Not verified: <e.g. real-device 120 Hz, screen-reader, Safari>
Generated assets: <Higgsfield items + credits used, or none>
Follow-ups: <only real ones>
```
