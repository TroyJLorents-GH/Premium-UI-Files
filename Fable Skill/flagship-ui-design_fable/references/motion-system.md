# Motion system

Timing, easing, springs, choreography, reduced motion, the physics formulas worth knowing by heart, and the failure modes that make expensive motion look cheap. Numbers are starting hypotheses; tune by travel distance, task frequency, input type, and measured response on the slowest supported device.

## Contents

1. Principles (what the transition is for)
2. Durations and easing
3. Springs vs curves
4. Choreography rules
5. Reduced motion as a composition
6. Physics formulas
7. The single ticker
8. Motion failure modes and fixes
9. Motion tokens

## 1. Principles

In software engineering a state change is instantaneous (`isOpen = true`). In interface motion the transition *is* the information: it says how heavy a thing is, where it came from, how parts relate, and where to look next. Decide that message before picking a duration.

- **Hierarchy of attention.** Each beat has one Primary Actor (the dominant movement), optionally one Secondary Follower (reacts 60–120 ms later: a callout line, a label), and Static Anchors (grid hairlines, pinned header, persistent nav) that give the eye a reference. Without an anchor, camera or parallax movement feels like the whole page sliding.
- **Initiation vs settlement.** Objects overcome static friction quickly and spend most of the duration decelerating. That is why strong ease-out curves read as both responsive and luxurious.
- **Expressive surfaces have a floor, quiet surfaces a cap.** A landing, launch, portfolio, or experiential page needs a hero sequence of several actors, one scroll set piece, and named micro-interactions (`signature-motion.md`); a page that only fades things up is a failed page there. Apps, dashboards, docs, and reading surfaces keep motion quiet: one hero treatment, one nav idea, two or three micro-interactions.
- **Restraint still applies inside the choreography**: lock text once it has entered, keep the UI around a complex subject razor-quiet, alternate pinned spectacle with normal-flow reading so scroll fatigue does not set in. Restraint is about where the eye rests, not about how much the page is allowed to move.
- **Fluid interface rules** (Apple WWDC18): instant response, continuous feedback, interruptible, redirectable, natural mapping. Material 3: informative, focused, expressive. Everything below serves those.

## 2. Durations and easing

| Element | Enter | Exit | Notes |
|---|---|---|---|
| Hover, color, press | 100–150 ms | same | press `scale(0.97)` at ~100 ms |
| Tooltip, toggle, checkbox | 150 ms | 100 ms | translate 4–6 px + fade |
| Dropdown, popover, menu | 150–200 ms | 100–150 ms | scale from 0.95, `transform-origin` at the anchor side |
| Modal, drawer, sheet | 200–300 ms | 150–200 ms | scale 0.96→1 or slide; backdrop fades concurrently |
| List add / remove / reorder | 200–300 ms | 150 ms | stagger 20–40 ms, cap total ≈ 300 ms |
| Page / route / view transition | 250–400 ms | 150–250 ms | crossfade default; shared-element morph for related items |
| Scroll reveal | 500–800 ms | — | translate 24–40 px, trigger 10–20% in view, once, no re-trigger on backscroll |
| Hero sequence (expressive) | 1.2–1.8 s total | — | 3–6 actors on one labeled timeline: figure leads, lines ~350 ms later, CTA last; headline legible by ~0.6 s; CTA interactive from first paint |
| Hero intro (quiet) | ≤800 ms total | — | headline + sub + CTA; CTA last |
| Pinned set piece | 200–300% viewport | — | `scrub: 0.6–1`; linear tweens inside; copy chapters synced to figure states |
| Number counters | 600–1000 ms | — | ease-out, `tabular-nums` |
| Marquee / ambient loop | 20–60 s | — | linear; pause on hover, off-screen, hidden tab |

| Intent | Curve | Why |
|---|---|---|
| Element enters | `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out family), `cubic-bezier(0.22, 1, 0.36, 1)` (quint-out), GSAP `expo.out` / `power4.out` | Fast start reads as responsive; ~80% of travel in the first 25% of time |
| Element exits | quick fade ≤150 ms; `ease-in` only if very short | Users do not watch exits; sluggish starts feel broken |
| Element moves on screen | `cubic-bezier(0.65, 0, 0.35, 1)` (ease-in-out) | Visible at both ends |
| Color / opacity | `ease` or `linear` for very short | Perceptually flat |
| Progress, marquee, scrub | `linear` | Constant rate is the point; also for timelines scrubbed by a damped scroller |
| Gesture-driven, interruptible | spring | Carries velocity; never "finishes then restarts" |
| Drawer / sheet settle | `cubic-bezier(0.32, 0.72, 0, 1)` | The snappy iOS-sheet feel popularized by Vaul |
| Never for UI | `ease-in` on long moves; `linear` on movement; `elastic`/`bounce` on large surfaces | Feels broken or cartoonish |

Keyboard-triggered actions get faster and simpler motion than pointer-triggered ones. Repeated actions (toggles used 100× a day) get near-zero motion. Do not add a delay merely to make an effect visible.

## 3. Springs vs curves

- Define springs by perceptual **duration + bounce** (Apple `.spring(duration:bounce:)`, Motion `type: "spring", visualDuration: 0.3, bounce: 0.2`) rather than raw stiffness/damping; the same k/c/m numbers produce different motion in different libraries.
- `bounce: 0` for layout and large surfaces; 0.1–0.3 for small playful elements.
- Carry gesture velocity into the release spring (Motion and react-spring do this; GSAP Inertia tracks it; custom code: see §6).
- A CSS `linear()` easing sampled from a spring (easing.dev, linear-easing-generator) is right for **non-interruptible entrances** (toasts, menus). It has fixed playback, so use a real spring wherever a mid-flight retarget is possible (drag release, rapid toggles, dock magnification).
- Interrupted animation must retarget from its current position and velocity, not restart from the origin. Test by clicking rapidly and reversing mid-flight.

## 4. Choreography rules

- Transform origin comes from the trigger: popovers scale from their anchor side, dialogs from center, FAB sheets from the button, theme toggles reveal from the click point.
- Container first, content second: the surface moves, then children fade/stagger in (Material "container transform").
- Shared axis: related things move along one axis; unrelated things crossfade.
- Exits are simpler than entrances: fade plus slight scale, optional `filter: blur(4px)` on small elements only.
- Stagger from the user's attention point (first item, hovered card, click position), 20–50 ms apart; cap total stagger duration instead of multiplying per item; never stagger a long list item by item.
- Scale from 0.95–0.97, not from 0. Translate 4–8 px for tooltips, 16–40 px for cards. Blur 2–4 px max.
- Scale containers, not text (text under `transform: scale` blurs mid-animation). Animate `grid-template-rows` or `interpolate-size`, not `height`.
- Direct manipulation: content follows the finger 1:1, rubber-bands at edges (≈0.3× past the limit, or the logarithmic formula in §6), snaps with velocity thresholds, haptic tick on snap (native) or a short procedural sound only when the user opted in.
- Move → Settle → Annotate for 3D and scroll stories: complete ~75% of the camera move before SVG callouts and text reveal.
- Text reveal: split by **lines or words** with an overflow mask (`yPercent: 115–120 → 0`, optional `rotate: 1.5–2deg → 0`, 25–40 ms stagger, `expo.out`, ≤0.95 s). The mask box must leave room for ascenders and descenders: pad it 0.1–0.15 em block-wise and counter with a negative margin, or glyphs like g, y, and accented capitals are clipped. Characters only for one short display word. Once revealed, text is static.
- Motion must never delay input: if a state change is instant, show it instantly and animate the consequence.

## 5. Reduced motion as a composition

`prefers-reduced-motion: reduce` is not "set duration to 0", and it is a fallback path: design the full experience first at full strength, then derive the reduced composition from it. The existence of the fallback is never a reason to make the default timid. Design the reduced composition explicitly:

- Remove: parallax, pinning/scroll-jacking, camera travel and orbits, axial explosions, large translations, auto-playing loops (marquees, ambient blobs, video backgrounds), zoom/spin reveals, cursor followers, magnetic pull.
- Keep: opacity crossfades, transforms ≤150 ms and ≤8 px, every state change, every feedback signal, focus movement.
- Also honor `prefers-reduced-transparency` (solid fallback for glass), `prefers-contrast`, and `forced-colors`.
- Mechanics: CSS global block; `gsap.matchMedia()` with a `reduceMotion` condition (and `gsap.context()` cleanup); Motion `useReducedMotion()` / `MotionConfig reducedMotion="user"`; Svelte `prefersReducedMotion`; View Transitions `::view-transition-group(*) { animation: none }`.
- App-like products add a persisted motion toggle in settings.
- WCAG: 2.3.3 (animation from interaction can be disabled), 2.2.2 (pause/stop/hide for anything moving longer than 5 s), 2.3.1 (no more than three flashes per second).

Test both the initial preference and a runtime change.

## 6. Physics formulas

Frame-rate-independent damping (identical feel at 60, 120, 240 Hz). `lambda` ≈ 8–14 for pointer followers, 10–20 for scroll velocity smoothing. Clamp `dt` to ~0.064 s so a background tab does not teleport.

```js
const damp = (current, target, lambda, dt) =>
  current + (target - current) * (1 - Math.exp(-lambda * dt));
```

Interruptible spring (semi-implicit Euler). Retargeting is just changing `target`; velocity is preserved. Typical UI: k 150–300, c 14–26, m 1. Stop when |x−target| < 0.01 and |v| < 0.01.

```js
function stepSpring(s, target, k, c, m, dt) {
  const a = (-k * (s.x - target) - c * s.v) / m;
  s.v += a * dt;
  s.x += s.v * dt;
  return s;
}
```

Logarithmic rubber-band (iOS overscroll). `x` overscroll distance, `d` the dimension being dragged (sheet height, list height), `c` ≈ 0.55.

```js
const rubberBand = (x, d, c = 0.55) => (1 - 1 / ((x * c) / d + 1)) * d;
```

Scroll-velocity skew (kinetic marquee / image stretch): `skew = clamp(velocity * 0.008, -14deg, 14deg)`, smoothed with `damp(…, 10, dt)`, returns to 0 at rest. Read velocity from Lenis (`lenis.velocity`) or ScrollTrigger (`getVelocity()`), not from your own scroll listener.

## 7. The single ticker

Independent `requestAnimationFrame` loops in Lenis, GSAP, and Three.js (`renderer.setAnimationLoop`) fire at different points inside the same frame window; scroll position and camera matrices desynchronize and the result vibrates even at 120 fps.

```js
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis({ autoRaf: false, lerp: 0.08 });
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);      // 1. damped scroll position
  updateCameraAndCallouts();   // 2. 3D camera + projected 2D anchors (if any)
  renderer.render(scene, camera); // 3. draw
});
gsap.ticker.lagSmoothing(0);
```

Search the codebase for `requestAnimationFrame` and `setAnimationLoop` before shipping; there should be one master loop. In React, create it inside `useGSAP`/`useEffect` and remove it on cleanup. Render 3D on demand (`frameloop="demand"`) when nothing changes.

## 8. Motion failure modes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Micro-stutter during fast scroll with a high FPS reading | Dual tickers (Lenis + GSAP + Three) | Single `gsap.ticker` loop (§7) |
| Tab crashes or drops to 15 fps after a few SPA navigations | Orphaned ScrollTriggers, undisposed Three geometries/materials/textures, leaked listeners | `gsap.context()` / `useGSAP()` revert; traverse scene and `dispose()`; `renderer.dispose()`; verify `renderer.info.memory.textures` returns to 0 |
| Purple layout/paint bars in the Performance panel during scroll | Animating `top/left/width/height/margin/filter: blur()` on scroll | Compositor-only properties; FLIP for layout |
| Site looks busy and expensive, users recall nothing | Camera move, explosion, SVG draw, and text reveal at the same scroll percentage | Move → Settle → Annotate |
| Phones overheat and throttle to 30 fps within 20 s | Uncapped `devicePixelRatio` (3.0–3.5 DPR = 9–12× fragments) | `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`, 1.5 during active scroll |
| Pinned sections fire early or overlap the footer | Lazy images, fonts, or async canvases changed document height after ScrollTrigger measured | Explicit `aspect-ratio` on media, no `loading="lazy"` above/inside pinned areas, `ScrollTrigger.refresh()` after fonts/assets load |
| 3D object color does not match the CSS background it should blend into | Blender AgX/Filmic tone mapping vs sRGB hex in CSS | Match Blender view transform to Standard, or set `renderer.toneMapping` and render the background inside the canvas |
| Animation "pops" when interrupted | Fixed-duration CSS transition restarts from the current value with a fresh curve | Spring, or GSAP `overwrite: "auto"` with the same ease and `quickTo()` |
| Hover effect sticks on touch devices | `mouseenter`-driven state with no pointer check | `@media (hover: hover) and (pointer: fine)`; pointer events |
| Text split blurs or shifts on resize | SplitText measured once | `autoSplit: true` with `onSplit` returning the animation, or re-split after `document.fonts.ready` and on resize |
| Scroll reveal re-fires on every backscroll | IntersectionObserver without `once` / ScrollTrigger `toggleActions` replaying | Reveal once; `toggleActions: "play none none none"` |

## 9. Motion tokens

```css
:root {
  --duration-instant: 50ms;
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;
  --duration-slower: 600ms;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-soft: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in: cubic-bezier(0.55, 0, 1, 0.45);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-sheet: cubic-bezier(0.32, 0.72, 0, 1);
  /* --ease-spring: linear(...) generated from a spring for non-interruptible entrances */
}
@media (prefers-reduced-motion: reduce) {
  :root { --duration-base: 120ms; --duration-slow: 150ms; --duration-slower: 150ms; }
}
```

Platform references for calibration: Material 3 durations short1–extraLong4 (50–1000 ms) with standard/emphasized easings; Apple spring presets `smooth`, `snappy`, `bouncy`; Carbon productive vs expressive; Atlassian, Spectrum, Fluent motion tokens. Tools: easing.dev, easings.net, cubic-bezier.com, GSAP Ease Visualizer, Chrome DevTools Animations panel (set playback to 10% to inspect), `document.getAnimations()`.
