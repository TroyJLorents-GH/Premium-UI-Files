# Scroll choreography and 3D

Scroll storytelling, pinning, smooth scroll integration, image-sequence scrubbing, Three.js/R3F budgets, the Blender-to-web pipeline, and the 3D-to-2D callout bridge. For individual GSAP plugin demos, use `gsap-plugin-playbook/PLAYBOOK.md`.

## Contents

1. Decide the medium first
2. Scroll patterns and how they are built
3. Lenis + ScrollTrigger integration
4. Pinned chapters: rules
5. Image-sequence scrubbing
6. Three.js / R3F budgets and setup
7. Blender-to-web pipeline
8. 3D-to-2D projection for callouts
9. 2.5D depth-map hero (the cheap alternative)
10. Lexicon: vague request → precise spec
11. QA protocol for scroll and 3D

## 1. Decide the medium first

| Need | Medium |
|---|---|
| User freely rotates/inspects the object | Live `.glb` in Three.js/R3F (budget ≤3–4 MB compressed) |
| Camera follows one art-directed path on scroll | Pre-rendered WebP/AVIF frame sequence on `<canvas>` (90–150 frames, ≤6 MB) or a baked camera track in the glTF |
| A single product with AR | `<model-viewer>` |
| Depth and parallax from a still render | 2.5D: beauty image + Z-depth map in a tiny fragment shader (§9), ~200 KB total |
| Scene with hundreds of transparent/refractive parts | Pre-render it; live refraction at that scale melts phones |
| Shader ambience only | Paper Shaders / Unicorn Studio / small `ShaderMaterial` |

Ask the user only if the answer changes this table. Otherwise assume: mid-range phone floor, real-time only where interaction needs it, poster first.

## 2. Scroll patterns and how they are built

| Pattern | Build |
|---|---|
| Pinned storytelling chapter | `ScrollTrigger` `pin: true, scrub: 0.6–1` on a paused master timeline, `end: "+=300%"`; or CSS `position: sticky` + `view()` timeline for simple cases |
| Horizontal runway in a vertical page | Pin wrapper and tween `xPercent`, or CSS scroll-snap on x with `scroll-timeline` progress bar |
| Image-sequence scrub | §5 |
| Scroll-scrubbed Lottie/Rive | `goToAndStop()` / Rive number input from ScrollTrigger progress |
| Stacking cards | `position: sticky; top: 4rem` per card; scale 0.92 and `filter: brightness()` on earlier cards from `view()` or ScrollTrigger |
| Text reveal on scroll | SplitText lines + `ScrollTrigger.batch`, or `view()` with `animation-range: entry 0% entry 60%`; once |
| Per-word reading illumination | word spans opacity 0.15→1 as the reading line passes; `view()` timeline or scrub; stays static once read |
| Scroll progress bar | `animation-timeline: scroll(root)` — three lines of CSS |
| Hide-on-scroll-down header | GSAP `Observer` direction callbacks or `scroll-state(stuck)` + class |
| Velocity skew / stretch | Read `lenis.velocity` / `ScrollTrigger.getVelocity()`, damp, `skewY` or `scaleY` ≤14°, return to 0 |
| Infinite marquee | Duplicated track + CSS keyframes or GSAP `horizontalLoop` helper; `pos mod width` |
| Scroll snap sections | `scroll-snap-type: y mandatory` + `scroll-snap-stop: always`; style with `scroll-state(snapped)`; test keyboard and long content; not with Lenis |
| Full-screen slide deck with wheel capture | GSAP `Observer` (`type: "wheel,touch,pointer"`, `tolerance`, `preventDefault`) — must add keyboard navigation, an exit, and a reduced-motion path; the captured demo lacks them |

Scroll hygiene: passive listeners, `overscroll-behavior: contain` on drawers, `scrollbar-gutter: stable`, `scrollend` instead of debounced scroll, scroll restoration on back. Never do layout reads (`getBoundingClientRect`) inside a raw `scroll` handler for many elements; use IntersectionObserver, ScrollTrigger, or CSS timelines.

## 3. Lenis + ScrollTrigger integration

```js
const lenis = new Lenis({ autoRaf: false, lerp: 0.08 });  // or duration/easing
lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((t) => lenis.raf(t * 1000));
gsap.ticker.lagSmoothing(0);
// reduced motion / WebView: do not instantiate Lenis at all
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
```

- `data-lenis-prevent` on nested scrollers (modals, code blocks, tables).
- Keep touch native (`syncTouch: false` default); iOS momentum already feels right.
- Native CSS scroll-snap does not work with Lenis; use its snap addon or drop one of them.
- Anchor links: use `lenis.scrollTo(target, { offset })` and move focus separately.
- `ScrollSmoother` is the alternative in all-GSAP stacks: needs `#smooth-wrapper > #smooth-content`, `effects: true` enables `data-speed`/`data-lag`, `normalizeScroll: true` tames mobile address bars; test fixed elements and anchors.

## 4. Pinned chapters: rules

- Expressive pages need at least one pinned set piece that makes the product's concept physical (the figure changes state as the visitor scrolls; copy chapters annotate each state). Alternate it with normal-flow reading; one pinned chapter per screen-height of reading is the ceiling, because scroll fatigue is real. Quiet surfaces pin nothing.
- Pin length 200–350% viewport; `scrub: 0.5–1` so wheel ticks are smoothed by the damped catch-up (linear tweens inside, the scrub supplies the easing). Worked recipe: `signature-motion.md` §11.
- The stage is sized in `dvh`, never `vh`: `height: 100dvh`, figure `min(60vw, 64dvh)` on desktop and `min(72vw, 44dvh)` on phones with the chapters stacked inside the pinned box. Copy and figure must both be inside the viewport at 390 × 844 and 1440 × 900 at 0, 50, and 100% progress; verify with captured frames.
- Chapter copy never names a layout position ("the panel at right", "below the diagram"): at 390 px the figure is above the copy.
- Header and figure are one group. Lay the stage out as a grid with `grid-template-rows: auto minmax(0, 1fr)` so the figure grows into the remaining height; do not center a fixed-size figure in leftover space, which leaves a dead band under the header.
- The live value rides on the moving marker. Attach the readout to the playhead (same transform owner, or set in the same `onUpdate`), and flip or clamp it near the edges so it stays whole. A readout in a far corner forces the reader to look away from the thing they are scrubbing.
- A chapter label is a range or a title, never a bare time. A label that holds "2:00" while the marker has moved to 3:30 reads as a wrong clock. Show the chapter's span ("2:00–3:15") and switch it when the marker leaves that span, or write it as a beat name with no time format.
- Chapter copy states what the figure shows. Derive times, peaks, and spans from the data array that draws the figure, then check each claim at its progress point.
- Explicit `aspect-ratio` on every image/canvas inside and above the pin; no `loading="lazy"` there; `ScrollTrigger.refresh()` after `document.fonts.ready` and asset loads. Layout shift after measurement is the number-one pin bug.
- 3D stages with `perspective` leak horizontal overflow on phones; `overflow: clip` on the stage, and check `document.documentElement.scrollWidth === innerWidth` at 390 px. Do not hide it with `overflow-x: hidden` on `<body>`.
- Short viewports (phones in landscape, 700 px laptops): test; provide a static fallback layout via `gsap.matchMedia()` conditions.
- Pinned content must be reachable and readable with keyboard; focus must not land in an off-screen pinned stage.
- Reduced motion: `toggleActions: "play none none reverse"` with simple fades, no pin, figure shown in its most informative state. This is the fallback, derived from the full chapter after it is built.

## 5. Image-sequence scrubbing

Apple-style hardware reveal: preload 90–150 frames (1440–1920 px wide, WebP quality ~80, AVIF where decode speed allows; total ≤6 MB with progressive loading), draw the frame for the current progress to a `<canvas>` (DPR-aware, `OffscreenCanvas` in a worker for heavy sequences). Never scrub `<video>.currentTime` (decode-bound and janky) unless encoded with every frame as a keyframe: `ffmpeg -i f_%04d.png -c:v libx264 -crf 20 -pix_fmt yuv420p -g 1 -keyint_min 1 -movflags +faststart out.mp4`. Show frame 0 as a <50 KB poster immediately. Under reduced motion show the final or most informative frame as a static image.

## 6. Three.js / R3F budgets and setup

Budgets (mobile floor): <150k triangles (<500k desktop), <50–60 draw calls, textures ≤2048² as KTX2/Basis, compressed `.glb` ≤3–4 MB, hero scene ≤2–3 MB where possible.

- `renderer.setPixelRatio(Math.min(devicePixelRatio, 2))`, 1.5 during active scroll; `frameloop="demand"` when idle; render only when visible (`IntersectionObserver`, `visibilityState`).
- Prefer baked AO/lightmaps and MatCaps over multiple real-time shadow-casting lights; `InstancedMesh`, LOD.
- WebGPURenderer with automatic WebGL2 fallback; TSL for shaders; check that custom GLSL `ShaderMaterial` code has a fallback path.
- Lazy-load the 3D bundle after LCP; poster image first; static poster under reduced motion or when `navigator.gpu`/WebGL is missing; handle context loss.
- Dispose geometries, materials, textures, render targets, and the renderer on unmount; verify `renderer.info.memory.textures` returns to 0.
- Profile with `r3f-perf`, Spector.js, Chrome Performance; `OffscreenCanvas` + Worker for heavy scenes.
- Drei helpers to reach for: `Environment`, `ContactShadows`, `Float`, `MeshTransmissionMaterial` (expensive), `Text`/`Text3D`, `ScrollControls`, `Html`, `useGLTF`, `CameraControls`, `AdaptiveDpr`, `PerformanceMonitor`.
- Lighting as creative direction: rim/back light first to carve the silhouette, key at 30–45°, soft fill so shadows keep texture; uniform ambient light flattens everything.

## 7. Blender-to-web pipeline

1. Storyboard and budget: narrative arc (hook → deconstruction → inspection → resolution), budgets above.
2. Scene: semantic object names (`diffuser_strake_L`), origins set on the axis each part slides/rotates along, `Empty` anchors where callouts attach, baked lighting/AO into a second UV set for real-time; render passes (Combined, Z normalized via Map Range, Normal, AO, Cryptomatte) for pre-rendered or 2.5D work; Grease Pencil Line Art for SVG overlays.
3. Compress: `npx @gltf-transform/cli optimize in.glb out.glb --compress meshopt --texture-compress ktx2 --texture-size 2048`. Never ship raw exports; procedural shader nodes do not survive glTF without baking.
4. Integrate on the single ticker (`motion-system.md` §7).
5. Color: Blender's AgX/Filmic view transform desaturates and compresses highlights; CSS hex is raw sRGB. Match by setting Blender to Standard or by tone-mapping in Three and rendering the background inside the canvas.

Licensing notes (snapshot): Blender GPL (outputs are yours), Three.js MIT, GSAP free custom license (not OSI), Lenis MIT, glTF-Transform MIT, Theatre.js core Apache-2 / studio AGPL.

## 8. 3D-to-2D projection for callouts

Do not render UI text inside WebGL (blurry, inaccessible, untranslatable). Project the anchor's world position each tick and position a DOM/SVG overlay with `translate3d`:

```js
const v = new THREE.Vector3();
function syncCallout(anchor, el) {
  anchor.getWorldPosition(v).project(camera);          // NDC −1..1
  const x = (v.x * 0.5 + 0.5) * innerWidth;
  const y = (-v.y * 0.5 + 0.5) * innerHeight;
  el.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0)`;
  el.hidden = v.z > 1;                                  // behind camera
}
```

Draw the callout line (`DrawSVGPlugin` or `stroke-dashoffset`) and reveal the label only after ~75% of the camera move (Move → Settle → Annotate).

## 9. 2.5D depth-map hero (the cheap alternative)

A ~180 KB beauty render plus a ~45 KB grayscale Z-depth pass gives cursor/gyro parallax at any frame rate for a fixed viewing angle:

```glsl
uniform sampler2D uBeauty, uDepth; uniform vec2 uPointer; uniform float uIntensity; // 0.015–0.025
varying vec2 vUv;
void main() {
  float depth = texture2D(uDepth, vUv).r;
  vec2 offset = uPointer * (depth - 0.5) * uIntensity;  // foreground and background move opposite ways
  gl_FragColor = texture2D(uBeauty, vUv + offset);
}
```

Damp `uPointer` with `gsap.quickTo` or `damp()`. Keep intensity small to avoid edge tearing. Pair with Swiss typography sandwiching the scene (large title behind, crisp telemetry in front) for depth without shaders.

## 10. Lexicon: vague request → precise spec

| Vague | Specify |
|---|---|
| "Zoom in on the part" | Dolly camera along local Z while narrowing FOV 50°→24°, interpolate `controls.target` to the part's bounding-box center |
| "Technical view" | Interpolate projection from perspective (35 mm) to orthographic (`frustumSize` 4) for CAD-style callout alignment |
| "Dramatic lighting" | Warm grazing rim at 135° azimuth, cool soft area key at 45°, baked contact AO, clearcoat where material warrants |
| "Move the pieces apart" | Axial explosion: translate sub-meshes along their normalized vector from assembly origin, staggered 0.04 s from housing inward |
| "Fade in the text smoothly" | Masked line reveal `yPercent 110→0`, `rotate 2→0`, 0.025–0.035 s stagger, 0.85–1.1 s, `expo.out` |
| "Animate as the user scrolls" | Pin container `end: "+=300%"`, bind normalized progress to a paused master timeline with `scrub: 0.6` |

Six-layer motion prompt for components (also in `assets/design-brief.md`): context and medium → spatial/camera spec → actor hierarchy (primary, secondary, anchor) → timing and physics → performance budget (draw calls, DPR cap, cleanup) → reduced-motion behavior.

## 11. QA protocol for scroll and 3D

- Frames, not screenshots: capture the set piece at 0, 50, and 100% progress and the page at 0/25/50/75/100% depth, at 1440 × 900 and 390 × 844. The figure must be in a different state in each set-piece frame with its copy in view; identical frames mean the chapter reads as static.
- `document.documentElement.scrollWidth === innerWidth` at 390 px; copy and figure inside the `dvh` stage at both sizes; no text clipped by a mask or overlapping another text node.
- Squint test (25% zoom, scroll): one unmistakable primary actor per beat.
- Velocity curve: scrub slowly; objects initiate fast and settle soft, no robotic stops.
- Typography stability: body copy still within 0.8 s and stationary while reading.
- Single ticker: search for `requestAnimationFrame` / `setAnimationLoop`; one master loop.
- DevTools Performance with 4× (or 6×) CPU slowdown and Fast 4G: record a full scroll; zero long tasks >50 ms, no purple layout spikes during scrub.
- `renderer.info.render.calls` < 60; `renderer.info.memory.textures` → 0 after unmount.
- Emulate `prefers-reduced-motion: reduce`: orbits, parallax, pins replaced by fades or static flow.
- Tab through: focus never trapped in an off-screen pinned stage; SplitText headlines read as sentences.
- Poster frame (<50 KB) visible immediately while the scene or sequence streams.
