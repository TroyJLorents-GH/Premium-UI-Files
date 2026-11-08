# Scroll architecture, 3D, shaders, and the Blender → web pipeline

The 2026 stack for scroll-heavy sites: **Lenis** for feel, **GSAP ScrollTrigger** for choreography, **native scroll-driven animations** for simple reveals and progress. For 3D: **Three.js** (`WebGPURenderer` + TSL, WebGL2 fallback), **R3F + Drei** in React, **Spline/Unicorn Studio/Paper Shaders** when hand-written WebGL is not justified. For plugin-level GSAP detail, read the [GSAP playbook](gsap-playbook/INDEX.md).

## Clarify only when it changes the architecture

1. **Delivery medium**: real-time WebGL/WebGPU, pre-rendered scrubbed canvas sequence, 2.5D depth shader, or native CSS/SVG?
2. **Camera freedom vs fidelity**: free orbit/inspect (needs a live `.glb`) or a single art-directed path on scroll (often better as a WebP/AVIF sequence or baked camera track)?
3. **Hardware floor**: mid-range phone on cellular (< 5 MB initial, DPR cap) or controlled desktop/kiosk?
4. **Asset starting point**: existing model/CAD, flat reference image, or procedural via Blender Python?

Otherwise state production assumptions and build.

## The five golden formats

| Format | When | How |
|---|---|---|
| **Raytraced canvas scrub** (`<canvas>` + WebP sequence + ScrollTrigger) | Photoreal reflections, smoke, 500-part exploded assemblies that would melt a phone GPU | Render 90–150 frames in Cycles, transparent WebP q80, ≤ 6 MB total, progressive load; draw frame index from scrub progress (`scrub: 0.5`) |
| **Baked `.glb` + MatCap/baked AO** (live Three.js) | User must drag, inspect, or transition the camera freely | Bake lighting/AO into UV2 textures or use MatCaps; no real-time shadow maps on mobile; compress with gltf-transform |
| **2.5D depth-displaced plane** (beauty + Z-depth + fragment shader) | Hero backgrounds and detail shots where a full model is overkill | ~180 KB beauty + ~45 KB depth; pointer offset `uIntensity` 0.015–0.025; runs at 120–240 fps on integrated GPUs |
| **Orthographic vector projection** (Blender Line Art → SVG → DrawSVG) | Technical overlays, HUD callouts, engineering transitions | Match SVG viewBox to the Blender camera, or project 3D anchors to DOM each tick |
| **GSAP Flip state morph** (DOM ↔ canvas continuity) | Bento → fullscreen inspector, page transitions | `Flip.getState()` → mutate DOM → `Flip.from(state, { absolute: true, nested: true, ease: 'expo.out' })` |

## Single-ticker synchronization (the golden rule)

Never run independent rAF loops for Lenis, GSAP, and Three.js; they desync within one frame and jitter on 120–240 Hz displays.

```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import Lenis from 'lenis';

gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis({ autoRaf: false, lerp: 0.08 });
lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);          // A: damped scroll position (ms)
  syncProjectedAnchors();          // B: 3D → 2D callouts, cursor lerps
  renderer.render(scene, camera);  // C: draw
});
gsap.ticker.lagSmoothing(0);
```

Lenis honors `prefers-reduced-motion` by default (lerp forced to 1, programmatic scrolls instant) and keeps running so WebGL sync stays intact; check `lenis.prefersReducedMotion` for your own branches. Use `lenis/react` (`<ReactLenis root options={{ autoRaf: false }}>`) or `lenis/vue` adapters and remove the ticker callback on unmount. Native CSS scroll-snap is unsupported by Lenis; use its snap plugin. `data-lenis-prevent` for nested scrollers. Keep `syncTouch` off unless tested. Smooth scroll is a marketing-surface tool; never on content-heavy apps. Full template: `assets/single-ticker.js`.

## ScrollTrigger essentials

- Pinned story: `pin: true, start: 'top top', end: '+=300%', scrub: 0.5–1.2`; a paused master timeline with `ease: 'none'` on scrubbed tweens; weight comes from the scrub buffer.
- Wrap everything in `gsap.matchMedia()` with `(prefers-reduced-motion: reduce)` and breakpoint conditions; it returns a context for automatic cleanup (`mm.revert()`).
- Measure after layout settles: explicit `aspect-ratio` on media; no `loading="lazy"` inside or above pinned sections; `ScrollTrigger.refresh()` after fonts (`document.fonts.ready`) and async assets; `invalidateOnRefresh: true` for responsive values.
- `ScrollTrigger.batch()` for staggered reveals; `normalizeScroll()` only when mobile address-bar resizing breaks pins; `markers: true` while authoring, removed before ship.
- `Observer` for hide-on-scroll headers and intent-based sections; always provide a keyboard path and an exit.
- React: `useGSAP()` from `@gsap/react` with `scope`; never create ScrollTriggers during SSR.
- Reduced motion fallback: `scrub: false`, `toggleActions: 'play none none reverse'`, instant states, native flow.

## Three.js / R3F budgets and rules

- **Real-time budget**: < 150k triangles mobile (< 500k desktop), < 50–60 draw calls/frame, textures ≤ 2048² as KTX2, total compressed `.glb` < 3–4 MB. Log `renderer.info.render.calls` and `renderer.info.memory.textures`.
- **DPR**: `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`, 1.5 during active scroll/motion on phones.
- **Render on demand**: `frameloop="demand"` when idle; pause offscreen and on `visibilitychange`; resume without time-step jumps.
- **Lighting**: baked AO/lightmaps or MatCaps over real-time shadows; `InstancedMesh`, LOD; `Environment` + `ContactShadows` in Drei for product shots.
- **Postprocessing** (bloom, DoF, chromatic aberration, grain, dither, ASCII) costs fill rate; one or two passes, profiled at phone resolution.
- **Loading**: poster (< 50 KB WebP matching frame 0) first; lazy-load the 3D bundle after LCP; static fallback when `navigator.gpu`/WebGL is missing or reduced motion is on.
- **Disposal**: on unmount traverse the scene and call `geometry.dispose()`, `material.dispose()`, `texture.dispose()`, `renderer.dispose()`; revert `gsap.context()`.
- **Accessibility**: semantic controls live outside the canvas; hotspots are real buttons; keyboard reaches every interaction; meaningful text is never rendered as a texture.
- **Color management**: match Blender view transform (Standard vs AgX/Filmic) to `renderer.toneMapping` when a scene must blend into a CSS background; or render the background inside the canvas.
- R3F: pin stable v9.x (v10 is alpha); `@react-three/postprocessing`, `@react-three/rapier` only when visibly justified; avoid React re-renders per physics frame; `r3f-perf` and Spector.js for profiling; `OffscreenCanvas` + Worker for heavy scenes.
- Shaders: GLSL (WebGL), WGSL (WebGPU), TSL (write once); learn with The Book of Shaders, reuse lygia; signature effects: hover displacement, liquid ripple, fluid sim, image trails, noise spheres, refraction (`MeshTransmissionMaterial`), holographic foil, particle text, Gaussian splats.

## 3D-to-2D spatial bridge (callouts that stay pinned to bolts)

Place `Empty` anchors in Blender at exact surface points. Each tick: `anchor.getWorldPosition(v); v.project(camera); x = (v.x*0.5+0.5)*innerWidth; y = (-(v.y*0.5)+0.5)*innerHeight;` then `wrapper.style.transform = translate3d(x, y, 0)`. HTML/SVG callouts stay crisp, selectable, and accessible. Secondary followers (DrawSVG callout lines, telemetry labels) start only after ~75% of the camera move.

## Blender → web pipeline

1. **Storyboard & budget**: narrative arc (hook → deconstruction → macro inspection → resolution); set triangle/draw-call/texture/payload budgets before modeling.
2. **Scene hygiene**: semantic object names (`diffuser_strake_L`, `anchor_callout_exhaust`); origins set to the axis each part slides/rotates on; Empties at callout points; Geometry Nodes for procedural exploded views; Boolean cutters with emissive edges for live cutaways; `Separate XYZ → ColorRamp → Mix Shader` for wireframe → clay → photoreal wipes.
3. **Passes**: for real-time, bake lighting/AO to UV2; for sequences/2.5D, render Combined, Z (normalized via Map Range), Normal, AO, Cryptomatte; transparent film for layering; Grease Pencil Line Art or Freestyle SVG for vector overlays; orthographic camera when overlays must align to a CSS grid.
4. **Compression (never skip)**: `npx @gltf-transform/cli optimize in.glb out.glb --compress meshopt --texture-compress ktx2 --texture-size 2048`. Sequences via Sharp/FFmpeg to WebP/AVIF. Scrubbable video must be all-keyframe: `ffmpeg -i f_%04d.png -c:v libx264 -crf 20 -pix_fmt yuv420p -g 1 -keyint_min 1 -movflags +faststart out.mp4`.
5. **Integrate on one ticker**, then run the QA protocol in performance-accessibility.

Data passes worth knowing: Z-depth (parallax, displacement), tangent-space normal (detail without geometry), curvature/cavity (edges), MatCap/clay + wireframe (topology reels), AO (grounding), Cryptomatte/material ID (click-to-isolate hover states).

## Worked example skeleton (pinned product breakdown)

```js
mm.add({ reduce: '(prefers-reduced-motion: reduce)' }, ({ conditions }) => {
  const tl = gsap.timeline({ scrollTrigger: {
    trigger: '#stage', start: 'top top', end: '+=300%', pin: true,
    scrub: conditions.reduce ? false : 0.6,
    toggleActions: conditions.reduce ? 'play none none reverse' : undefined } });
  if (conditions.reduce) return tl.to('.callout', { autoAlpha: 1, duration: 0.3 });
  tl.to(camera.position, { x: 2.4, y: 1.6, z: 3.2, ease: 'power2.inOut', duration: 1 }, 0)      // primary actor
    .to(strakeL.position, { x: -0.65, ease: 'expo.out', duration: 0.8 }, 0.25)                 // deconstruction
    .fromTo('#callout-path', { drawSVG: '0%' }, { drawSVG: '100%', duration: 0.35 }, 0.65)      // follower, after settle
    .fromTo('.telemetry', { yPercent: 100, autoAlpha: 0 }, { yPercent: 0, autoAlpha: 1, stagger: 0.05 }, 0.75);
});
```

See `references/library/foundation-principles-of-motion.md` for the full three worked examples (GLB + SVG HUD, 2.5D depth hero with accessible SplitText, Flip bento → inspector).
