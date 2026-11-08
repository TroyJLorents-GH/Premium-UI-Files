# Motion numbers: durations, eases, springs, choreography

Good UI motion responds within 100 ms, lasts 150–400 ms, eases out on entry, exits faster than it enters, and can be interrupted at any frame. These are **starting hypotheses** from Apple fluid-interface guidance, Material 3, and the design-engineering school (Emil Kowalski, Rauno Freiberg, Josh Comeau), not standards. Tune by travel distance, input type, frequency, platform, and measured response. Never add delay to make an effect visible.

## Durations by element

| Element | Enter | Exit | Notes |
|---|---|---|---|
| Hover / color / press | 100–150 ms | same | `ease`; press scale 0.97 at ~100 ms |
| Tooltip, toggle, checkbox | 150 ms | 100 ms | translate 4–6 px + fade |
| Dropdown, popover, menu | 150–200 ms | 100–150 ms | scale from 0.95 at the anchor's `transform-origin` |
| Modal, drawer, sheet | 200–300 ms | 150–200 ms | scale 0.96 → 1 or slide; backdrop fades simultaneously |
| List add/remove/reorder | 200–300 ms | 150 ms | stagger 20–40 ms, cap total ≈ 300 ms |
| Page / route transition | 250–400 ms | 150–250 ms | crossfade or shared-element morph |
| Scroll reveal | 500–800 ms | — | translate 24–40 px, ease-out, trigger 10–20% in view, once |
| Hero intro choreography | 800–1200 ms total | — | the one place long timelines are acceptable; CTA available early |
| Number counters | 600–1000 ms | — | ease-out, tabular figures |
| Marquee / ambient loops | 20–60 s | — | linear; pause on hover, offscreen, and reduced motion |
| Masked text reveal | 0.85–1.1 s | — | `yPercent: 110 → 0`, 0.025–0.04 s stagger per line/word, `expo.out` |
| Scroll-scrubbed timeline | scroll-bound | — | `scrub: 0.5–1.2` for weight; `ease: 'none'` inside the scrubbed timeline |

Quick budgets: small feedback 80–150 ms · compact enter/exit 150–250 ms · larger spatial 200–400 ms. Keyboard-triggered and repeated actions get faster/simpler motion.

## Easing by intent

| Intent | Curve | Why |
|---|---|---|
| Element enters | `cubic-bezier(0.22, 1, 0.36, 1)` (quint-out) · `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out) · GSAP `expo.out` / `power4.out` | Fast start reads as responsive; long settle reads as luxury |
| Element exits | fast ease-out fade ≤ 150 ms (or `ease-in` only if quick) | Avoid sluggish starts |
| Element moves on screen | `cubic-bezier(0.65, 0, 0.35, 1)` | Visible at both ends |
| Color / opacity | `ease` or `linear` when very short | Perceptually flat |
| Progress, marquee, scrub | `linear` / `none` | Constant rate is the point |
| Gesture-driven, interruptible | spring | Carries velocity; never "finishes then restarts" |
| Drawer feel (Vaul signature) | `cubic-bezier(0.32, 0.72, 0, 1)` | Snappy settle |
| Camera / 3D travel | `power2.inOut` for scrubbed orbits; `expo.out` for settles | Weight without robotic stops |
| Never for UI | `ease-in` on long moves, `linear` on movement, `elastic`/`bounce` on surfaces, stock `ease-in-out` on UI | Feels broken or cartoonish |

## Springs

Define by **perceptual duration + bounce**, not raw stiffness/damping: Apple `.spring(duration:bounce:)`, Motion `{ type: 'spring', visualDuration: 0.3, bounce: 0.2 }`. `bounce: 0` for layout and large surfaces; 0.1–0.3 for small playful elements. Carry gesture velocity into the release spring. Spring numbers are engine-specific; the same stiffness/damping differ across libraries. Bake springs into CSS with `linear()` via linear-easing-generator or easing.dev when no runtime physics is needed (fixed playback; no retargeting).

Frame-rate-independent damping for custom loops: `value = lerp(current, target, 1 − e^(−λ·Δt))`. Rubber-band overscroll: `f(x) = 1 − 1 / ((x·c)/d + 1)`, with `c ≈ 0.55`, `d` = dimension; roughly 0.3× travel past the limit.

## Motion tokens (copy into the project)

| Token | Typical values |
|---|---|
| `--duration-instant / fast / base / slow / slower` | 50 / 150 / 250 / 400 / 600 ms |
| `--ease-out` (enter) | `cubic-bezier(0.22, 1, 0.36, 1)` |
| `--ease-out-expo` (hero, masked reveals) | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--ease-in` (quick exits) | `cubic-bezier(0.55, 0, 1, 0.45)` |
| `--ease-in-out` (move) | `cubic-bezier(0.65, 0, 0.35, 1)` |
| `--ease-drawer` | `cubic-bezier(0.32, 0.72, 0, 1)` |
| `--ease-spring` | `linear(…)` generated from a spring |

Platform references: Material 3 durations short1–extraLong4 (50–1000 ms) with emphasized/standard easings; Apple presets `smooth`, `snappy`, `bouncy`; Carbon productive vs expressive. See `assets/motion-tokens.css`.

## Choreography rules

- **Transform origin from the trigger**: popovers scale from their anchor side, dialogs from center, FAB sheets from the button, theme toggles reveal from the click point.
- **Container first, content second**: the surface moves, then children fade/stagger in (Material container transform).
- **Shared axis**: related things move along one axis; unrelated things crossfade.
- **Stagger from the attention point** (first item, hovered card, click position), 20–50 ms apart; cap total duration; never per-item on long lists (batch with `ScrollTrigger.batch` or cap at ~8 items).
- **Scale from 0.95–0.97, not 0**; translate 4–8 px for tooltips, 16–40 px for cards; blur 2–4 px max and only on small elements.
- **Animate `grid-template-rows: 0fr → 1fr` or `interpolate-size` instead of `height`**; `clip-path: inset()` for reveals.
- **Direct manipulation**: content follows the finger 1:1, rubber-bands at edges, snaps with velocity thresholds, haptic tick on snap (native).
- **Motion never delays input**: if a state change is instant, show it instantly and animate the consequence. Visible acknowledgement within ~100 ms independent of network.
- **Interruptible by construction**: rapid repeat, reverse mid-flight, route change, unmount, tab hide, resize, breakpoint change all land in a valid state. Use `overwrite: 'auto'`, `AnimatePresence`, springs, and `gsap.context()` reverts.
- **One owner per property**: nested wrappers when CSS layout, GSAP, and a framework each need a transform.

## Patterns and what good looks like

| Pattern | Good execution | Tools / caution |
|---|---|---|
| Press feedback | Immediate small change; hit area stable | CSS/Motion; never move the target away from the pointer |
| Hover & focus | Equivalent clarity for mouse and keyboard | Never hover-only disclosure |
| Menu/disclosure | Small movement from the trigger + opacity; repeated activation reverses cleanly | 120–220 ms |
| Dialog/drawer | Backdrop and surface coordinated; close interrupts open; focus enters/restores | 180–320 ms |
| Shared-element | Same item visibly moves between list and detail, preserving identity | View Transitions / `layoutId` / Flip; manage focus separately |
| Height expansion | No clipped text, no unrelated shift | `grid-template-rows`, `interpolate-size`, measured height |
| Drag and drop | Tracks input closely; insertion visible; drop settles briefly | Include non-drag reorder |
| Spring retargeting | Mid-flight change continues from current position/velocity | Motion/react-spring; restrained damping |
| Route transition | Short continuity that never holds up navigation | Back/forward and focus are correctness |
| List stagger | Ordered offset communicates grouping without delaying later items | Cap total duration |
| Scroll reveal | Content accessible before JS; becomes visible once; supports reading order | No surprise on backscroll |
| Pinned story | Each segment reveals an understandable idea; easy exit and static alternative | Sparingly; test short viewports |
| Parallax | Modest depth; reading plane stable | Disable large travel for reduced motion |
| Text reveal | Lines/words enter coherently; final text selectable and semantic | No char-by-char reading delay |
| Loading | Existing content stable; skeleton matches incoming layout | No fake percentages |
| Success | Brief reward after a real completion; routine actions stay quiet | Text confirmation too |
| 3D reveal | Useful angles, poster first, loads only when it adds value | model-viewer / Three / Spline |
| Shader transition | Short, localized, legible | Profile fill rate at phone resolution |

## Reduced motion composition

Under `prefers-reduced-motion: reduce`: show text immediately (opacity only); remove parallax, pinning, auto-scroll, loops, zoom, camera orbits, axial explosions; replace with calm crossfades ≤ 150 ms and native document flow; keep state changes and feedback; keep `scrub: false` with `toggleActions` or an instant state. Test the initial preference and a live change. App-like products add a persisted motion toggle. Vestibular safety: no full-viewport zoom, spin, or parallax by default.

## Tuning tools

easings.net, easing.dev, cubic-bezier.com, GSAP Ease Visualizer, linear-easing-generator, Josh Comeau's spring playground, Chrome DevTools Animations panel (slow to 10% to inspect), `document.getAnimations()`.
