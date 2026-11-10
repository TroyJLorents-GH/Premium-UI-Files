# Motion system

Distilled from the cheat sheet (§16), the Foundation Principles of Motion, and the 120Hz lab. Numbers are working heuristics, not standards; tune by input, travel distance, audience and repetition.

## Contents
- Principles
- Durations
- Easing and springs
- Choreography rules
- Property ownership and the render pipeline
- Single-ticker architecture
- Scroll patterns
- Text and masked reveals
- Layout and shared-element transitions
- 3D / WebGL budgets and pipeline
- Reduced motion
- Common failure modes

## Principles

- Respond within 100 ms; last 150–400 ms for UI; ease out on entry; exit faster than entry; be interruptible at any frame.
- Motion carries information: mass, causality, relationship, where to look next. If an animation says nothing, delete it.
- Physical objects cannot change velocity instantly. Initiate fast, spend most of the duration decelerating (`expo.out`, `power4.out`, `cubic-bezier(0.16, 1, 0.3, 1)` front-loads ~80% of travel into the first ~25%).
- Linear only for constant-rate things: marquees, progress, and timelines scrubbed by an already-damped scroll.
- **Restraint wins** when: the user is reading or comparing data; the 3D subject is already complex; scroll fatigue sets in (alternate pinned spectacle chapters with normal-flow reading chapters). Repeated actions (a toggle used 100×/day) get near-zero motion; keyboard-triggered actions are faster/simpler than pointer-triggered.
- Typography is architecture: lock display type to a rigid grid to ground a 3D scene, or sandwich the subject in Z (large title behind, crisp telemetry in front).

## Durations

| Element | Enter | Exit | Notes |
|---|---|---|---|
| Hover / color / press | 100–150 ms | same | press scale 0.97 |
| Tooltip, toggle, checkbox | 150 ms | 100 ms | translate 4–6 px + fade |
| Dropdown, popover, menu | 150–200 ms | 100–150 ms | scale from 0.95 at the anchor's transform-origin |
| Modal, drawer, sheet | 200–300 ms | 150–200 ms | scale 0.96→1 or slide; backdrop in parallel |
| List add/remove/reorder | 200–300 ms | 150 ms | stagger 20–40 ms, cap total ≈ 300 ms |
| Page / route transition | 250–400 ms | 150–250 ms | crossfade or shared-element morph |
| Scroll reveal | 500–800 ms | — | translate 24–40 px, ease-out, trigger 10–20% in view |
| Hero intro | 800–1200 ms total | — | the one place long timelines are OK |
| Counters | 600–1000 ms | — | ease-out, `tabular-nums` |
| Ambient loops | 20–60 s | — | linear; pause on hover and off-screen |

## Easing and springs

| Intent | Curve |
|---|---|
| Enter | `cubic-bezier(0.22, 1, 0.36, 1)` or `(0.16, 1, 0.3, 1)` |
| Move on screen | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Exit | fast ease-out fade (≤150 ms) |
| Progress / scrub / marquee | linear |
| Drawer feel | `cubic-bezier(0.32, 0.72, 0, 1)` |
| Gesture-driven or interruptible | spring (carries velocity) |
| Avoid | ease-in on long moves, linear on movement, elastic/bounce on large surfaces |

Springs: specify by perceptual duration + bounce (Motion `visualDuration: 0.3, bounce: 0.2`); `bounce: 0` for layout/large surfaces, 0.1–0.3 for small playful elements; carry gesture velocity into release; bake into CSS with `linear()` (linear-easing-generator / easing.dev). Rubber-banding past limits: `f(x) = 1 − 1/((x·c/d) + 1)`, c ≈ 0.55.

## Choreography rules

- Transform origin from the trigger. Container moves first, content second. Related things share an axis; unrelated crossfade.
- Exits simpler than entrances (fade + slight scale; optional ≤4 px blur on small elements).
- Stagger from the user's attention point, 20–50 ms apart, never per-item on long lists.
- Scale from 0.95–0.97 (not 0); translate 4–8 px (tooltips), 16–40 px (cards). Scale containers, not text (text blurs). Animate `grid-template-rows` or `interpolate-size`, not `height`.
- Direct manipulation: content follows the finger 1:1, rubber-bands at edges, snaps with velocity thresholds.
- Motion never delays input. If state is instant, show it instantly and animate the consequence.
- Per beat define: primary actor, secondary follower (+60–120 ms), static anchor. Sequence Move → Settle → Annotate.

## Property ownership and the render pipeline

- Hot path: `transform`, `opacity`, `clip-path`, small `filter`. Never animate `top/left/width/height/margin/box-shadow`. Fake shadow motion by fading a pseudo-element.
- One owner per property. Mixing CSS transitions, WAAPI and a JS library on the same `transform` causes jitter and snap-back.
- Batch DOM reads before writes. `will-change` on ≤5 elements right before animating; remove after.
- `backdrop-filter` and big blurs are expensive (iOS especially): limit area and count.
- `content-visibility: auto` + `contain-intrinsic-size` for long pages; pause everything off-screen (IntersectionObserver, `visibilitychange`), including Lottie, Rive, canvas, marquees.
- Frame-rate-independent damping: `value = lerp(current, target, 1 − e^(−λ·Δt))`, not a fixed per-frame factor.
- Budgets: 16.7 ms at 60 Hz, 8.3 ms at 120 Hz. Measure dropped frames, not average FPS.

## Single-ticker architecture

Never run separate `requestAnimationFrame` loops for Lenis, GSAP and Three.js; they desynchronize inside a frame and produce micro-stutter on 120/240 Hz. Drive everything from `gsap.ticker` in a fixed order: Lenis raf → camera/projection updates → render. Wiring example is in `tool-integrations.md` §Lenis. Search the codebase for `requestAnimationFrame` and `setAnimationLoop` and confirm only one master loop remains.

## Scroll patterns

Prefer native: CSS scroll-driven animations (`animation-timeline: scroll()/view()`, compositor-thread, no jank), `position: sticky`, scroll-snap, `IntersectionObserver`. Use ScrollTrigger when you need pinning, scrubbing with callbacks, snapping, or sync with WebGL/camera math.

- Pinned scrollytelling: pin `100dvh`, `end: '+=300%'`, bind progress to a paused timeline with `scrub: 0.6`.
- Horizontal runway: pin a section, translate a wide track by vertical distance.
- Canvas image-sequence scrub: 90–150 frames WebP/AVIF, total ≤ ~6 MB, progressive loading, poster frame (<50 KB) for first paint.
- Stacking cards: sticky cards that scale down/dim as the next arrives.
- Velocity skew: read scroll velocity, `skewY` proportional, spring back.
- Layout shift breaks pin math: give media `aspect-ratio`, no `loading="lazy"` inside pinned areas, `ScrollTrigger.refresh()` after fonts/media.
- Always provide the unpinned, readable fallback (reduced motion, small screens if pinning hurts).

## Text and masked reveals

GSAP SplitText (free since 2025): `SplitText.create(el, { type: 'lines,words', mask: 'lines' })`; animate `yPercent: 110→0` (optionally `rotate 2deg→0`), ~0.85–1.1 s `expo.out`, stagger 0.025–0.04 s. Wait for `document.fonts.ready`; re-split on resize via `autoSplit`; revert on teardown. Keep one accessible reading path (SplitText adds aria labels; do not leave focusable controls inside an aria-hidden visual duplicate). See `gsap-playbook/accessible-split-text.md` for the known defects of the captured demo. Use `font-variant-numeric: tabular-nums` on live numbers; `text-wrap: balance` on headings.

## Layout and shared-element transitions

Order of preference: View Transitions API (`document.startViewTransition`, `@view-transition { navigation: auto }`, `view-transition-name`) → Motion `layout`/`layoutId` (React) → GSAP Flip (vanilla/any DOM reparenting). Flip: `Flip.getState` before the DOM change, mutate, then `Flip.from(state, { duration: 0.85, ease: 'expo.out', absolute: true })`. Preserve focus identity across reorders. Circular theme reveal: animate `clip-path: circle()` from the click point on the View Transition `ready` promise.

## 3D / WebGL budgets and pipeline

Use 3D only when it earns its cost and a poster fallback exists.
- Budgets: mobile ≤150k triangles (desktop ≤500k), <50 draw calls, textures ≤2048² KTX2, `.glb` ≤ ~4 MB. Cap `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))` (1.5 during scroll).
- Compress: `npx @gltf-transform/cli optimize in.glb out.glb --compress meshopt --texture-compress ktx2 --texture-size 2048`.
- Scrubbable video needs all-intra frames: `ffmpeg -i f_%04d.png -c:v libx264 -crf 20 -pix_fmt yuv420p -g 1 -keyint_min 1 -movflags +faststart scrub.mp4`.
- HTML/SVG labels over 3D: place empties in the model, `vector.project(camera)` each tick, position with `translate3d`. Never render UI text as WebGL textures.
- Prefer baked AO/lightmaps and MatCaps over many real-time shadow lights. Match Blender color management (Standard vs AgX) to the Three.js tone mapping when blending into CSS colors.
- 2.5D hero alternative: beauty render (~180 KB) + grayscale depth map (~45 KB), fragment shader offsets UV by damped pointer × (depth − 0.5) × 0.015–0.025.
- Dispose geometries, materials, textures and the renderer on unmount; verify `renderer.info.memory.textures` returns to 0.
- Prefer `WebGPURenderer` + TSL (WebGL fallback) for new Three.js work; check support.

## Reduced motion

Implement with `gsap.matchMedia()` (or CSS `@media (prefers-reduced-motion: reduce)`, Motion `useReducedMotion`). Under reduce: remove parallax, auto-scroll, pinning, camera orbits, looping and large spatial moves; keep opacity fades and ≤150 ms transforms; swap scrubbed sequences for static states. Pause anything moving >5 s (WCAG 2.2.2); no more than 3 flashes/s. Never let focus travel into an off-screen animated element. For app-like products add a persistent in-app motion toggle.

## Common failure modes (diagnose fast)

| Symptom | Cause | Fix |
|---|---|---|
| Jitter on 120/240 Hz while FPS looks fine | Multiple rAF loops | Single `gsap.ticker` |
| Tab crashes after several route changes | Orphan ScrollTriggers, undisposed GPU resources | `gsap.context`/`useGSAP`, dispose Three.js assets |
| Purple layout/paint bars while scrolling | Animating layout props or big blurs | Transforms only; Flip for layout |
| Busy but unmemorable | Camera + text + SVG all move at once | Move → Settle → Annotate |
| Phones overheat, drop to 30 fps | Uncapped DPR | Clamp DPR |
| Pins fire early / overlap footer | Layout shift after trigger math | aspect-ratio, no lazy in pins, `refresh()` |
| 3D red looks muted vs CSS red | Tone mapping mismatch | Match view transform / tone mapping |
| Animation snaps back at end | Two owners on a property or CSS vs JS conflict | Single owner; clear inline styles on revert |
