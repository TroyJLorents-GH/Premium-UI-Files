# Premium UI/UX & Motion Cheat Sheet (2026)

Nov 6, 2026 · @Troy Lorents

## How to use this sheet

This is a research map of every technique, library, standard and tool that separates premium UI/UX from average in late 2026, grouped by layer so you can pick one and go deeper. Each entry says what it is, when to use it, and its status. Statuses: **Standard** = the default choice today; **Rising** = growing fast and safe to adopt; **Niche** = right for a specific need; **Legacy** = still works, but don't start new projects on it.

Three rules hold the whole sheet together:

1. Reach for the platform first (CSS, View Transitions, scroll-driven animations), a library second (GSAP, Motion), a custom engine last (Three.js, shaders).
2. Animate only `transform`, `opacity`, `clip-path` and `filter` on the hot path; anything that triggers layout will stutter on mid-range phones.
3. Every effect must respect `prefers-reduced-motion`, keyboard focus and Core Web Vitals, or it is not premium.

**State of play, 2024–2026 (what changed):**

- GSAP became 100% free in April 2025 after Webflow acquired GreenSock (Oct 2024); every former paid plugin (SplitText, MorphSVG, ScrollSmoother, DrawSVG, Flip, etc.) now ships free.
- Framer Motion was renamed **Motion** (motion.dev) in late 2024 and now runs in React, Vue and vanilla JS with a hybrid engine that hands off to native browser animations when it can.
- Anime.js v4 (April 2025) is a full modular rewrite: timers, timelines, scope, draggable, scroll observer.
- The web platform caught up: View Transitions, scroll-driven animations, `@starting-style`, `interpolate-size`, anchor positioning, the `popover` attribute and `linear()` easing replace whole libraries from 2022.
- Lenis is the de-facto smooth-scroll layer; Locomotive Scroll v5 was rebuilt on top of it.
- Tailwind CSS v4 (Jan 2025) moved to CSS-first config; shadcn/ui on headless primitives (Radix, Base UI, React Aria, Ark) is the dominant React starting point.
- INP replaced FID as a Core Web Vital in March 2024; the target is under 200 ms.
- Apple's Liquid Glass (June 2025) and Google's Material 3 Expressive (May 2025) pushed platform motion toward physics springs, morphing shapes and layered translucency.
- WCAG 2.2 is the current accessibility standard; the European Accessibility Act applies to new digital products since 28 June 2025.
- Rive became the choice for interactive, state-machine animation; Lottie stays the After-Effects export standard, with dotLottie as its compact format.
- Spline, Unicorn Studio and shader tools made 3D and shader heroes mainstream without hand-written Three.js.
- Mainstream stacks: Vite (Rolldown), React 19, Next.js 16, Svelte 5, Nuxt 4, Astro 6, SolidStart, TanStack Start.

## 1. JavaScript motion & animation libraries

Three engines cover almost every premium site in 2026: GSAP for timelines and scroll choreography, Motion for React/Vue component animation, Anime.js for a tiny modular engine. Everything else below is either framework-native or single-purpose.

**General-purpose engines**

| Library | What it does | Reach for it when | Status |
| --- | --- | --- | --- |
| [GSAP](https://gsap.com) 3.15 (Apr 2026) | Timelines, 100% free plugins: ScrollTrigger, ScrollSmoother, SplitText, MorphSVG, DrawSVG, MotionPath, Flip, Draggable + Inertia, Observer, ScrambleText, Physics2D, CustomEase/Bounce/Wiggle, Pixi/Easel; `@gsap/react` `useGSAP()` hook | Scroll-driven storytelling, complex sequenced timelines, SVG morphing, Awwwards-style sites, Webflow (its owner) | Standard |
| [Motion](https://motion.dev) 12.x (ex-Framer Motion) | React, Vue and vanilla APIs; hybrid engine hands simple tweens to native WAAPI; `layout`/`layoutId` shared-element animations, `AnimatePresence` exit animations, gestures (`whileHover/Tap/Drag/InView`), `useScroll`/`useTransform`, springs, `Reorder`; 2026 additions: ViewTimeline scroll (12.35), axis-locked `layout="x"`, OKLCH color support, `layoutAnchor`; `animateView()` View-Transitions wrapper (alpha, Motion+ only); Motion UI (Jul 2026: 26 sections, 35 components) and paid Motion+ vault | Component-level UI animation in React/Vue: modals, lists, tabs, drawers, page transitions, micro-interactions | Standard |
| [Anime.js](https://animejs.com) v4 (Apr 2025) | Modular ESM (\~24.5 KB full, \~5 KB timer): `animate`, `createTimeline`, `createTimer`, `createAnimatable`, `createDraggable`, `createLayout` (FLIP), `createScope` (React cleanup), `onScroll`, `createSpring`, SVG `createDrawable`/`morphTo`/`motionPath`, optional WAAPI module | Lightweight vanilla or React projects that want a timeline engine without GSAP's size | Standard |
| [React Spring](https://react-spring.dev) v10 | Physics-based hooks: `useSpring`, `useTrail`, `useTransition`, `useChain`; works on DOM, Three.js, React Native | Interruptible spring motion in React where you don't want a timeline mental model | Standard (slower cadence) |
| [Web Animations API](https://developer.mozilla.org/docs/Web/API/Web_Animations_API) (native) | `el.animate(keyframes, options)`, `Animation` objects, `getAnimations()`, composite modes, scroll/view timelines | Any animation that needs play/pause/reverse without a library; Motion and Anime.js use it under the hood | Standard |
| [Theatre.js](https://www.theatrejs.com) | Visual sequence editor in the browser for DOM and React Three Fiber timelines, keyframe UI for designers | Cinematic 3D scenes, animated storytelling with hand-tuned keyframes | Niche |
| [AutoAnimate](https://auto-animate.formkit.com) (`@formkit/auto-animate`) | One line adds add/remove/reorder transitions to any parent; React, Vue, Svelte, Solid, Angular, vanilla | Lists, grids, todo-style UIs where you want motion with zero authoring | Standard |
| [Popmotion](https://popmotion.io), [Velocity.js](http://velocityjs.org), Mo.js, Tween.js, KUTE.js, Rebound, Dynamics.js | Earlier-generation tween/physics engines | Maintaining old code only; Motion and Anime.js replaced them | Legacy |

**Framework-native motion (use before adding a library)**

| Framework | Built-in | Notes |
| --- | --- | --- |
| React 19 | None built in; use Motion, React Spring, AutoAnimate, or CSS + View Transitions; `<ViewTransition>` component is experimental in React Canary/Next.js | React Compiler (1.0, Oct 2025) removes manual memo work that used to break animations |
| Vue 3.5 | `<Transition>`, `<TransitionGroup>` (FLIP built in), `@vueuse/motion`, Motion for Vue | Nuxt adds page/layout transitions and View Transitions via config |
| Svelte 5 | `transition:`, `in:`/`out:`, `animate:flip`, `svelte/motion` `Spring` and `Tween` classes, `crossfade` | The best built-in motion story of any framework; no library needed for most UI |
| Solid | `solid-transition-group`, `@solid-primitives`, Motion vanilla API | Fine-grained reactivity keeps per-frame updates cheap |
| Angular 20+ | `animate.enter` / `animate.leave` bindings on native CSS; `@angular/animations` deprecated since 20.2 | Migrate old `trigger()` code to CSS classes |
| Astro / HTMX / Rails Turbo | View Transitions (Astro `ClientRouter`), CSS transitions, `hx-swap` transitions | Multi-page apps get native page transitions for free |

**Single-purpose motion libraries**

| Need | Current best | Alternatives |
| --- | --- | --- |
| Animated numbers, counters, prices | [NumberFlow](https://number-flow.barvian.me) (React/Vue/Svelte/vanilla, digit rolling, accessible) | CountUp.js, react-countup, Odometer (legacy) |
| Split text into chars/words/lines | GSAP SplitText (free, handles emoji, `aria-label`) | SplitType, Splitting.js, Motion `splitText()` (Motion+) |
| Typewriter / text cycling | Typed.js, TypeIt, react-type-animation | CSS `steps()` keyframes for short strings |
| Scramble / decode text | GSAP ScrambleText, custom `requestAnimationFrame` | `use-scramble` (React) |
| Confetti, particles, celebrations | canvas-confetti, tsParticles (confetti + presets), party.js | js-confetti, react-rewards |
| Physics (2D/3D) | Matter.js (2D), Rapier (WASM, 2D/3D, R3F binding), cannon-es, Planck.js | Motion/Anime springs for UI-scale physics |
| Gestures (drag, pinch, wheel) | `@use-gesture/react` (pairs with React Spring/Motion), native Pointer Events | interact.js, Hammer.js (dead, avoid) |
| FLIP / shared-element | View Transitions API, Motion `layoutId`, GSAP Flip, Anime `createLayout`, Svelte `crossfade` | react-flip-toolkit (legacy) |
| Sketchy annotations | [Rough Notation](https://roughnotation.com) (underline, circle, highlight) | Rough.js for shapes |
| Sound on interaction | `use-sound` (Howler-based), Web Audio API | Tone.js for synthesis |
| Programmatic video (not UI) | Remotion (React), Motion Canvas, Revideo | Lottie/Rive exports for short loops |
| Tweak panels while tuning | Leva (R3F), Tweakpane, lil-gui | stats.js / r3f-perf for FPS |

Rules of thumb: GSAP and Motion can coexist; use Motion for component state and GSAP for scroll/timeline choreography. For scroll scrubbing and pinning, GSAP ScrollTrigger or native scroll-driven animations beat Motion. Bundle budget: Motion can be lazy-loaded (`LazyMotion` + `domAnimation`), Anime.js tree-shakes to a few KB, GSAP core is about 23 KB gzipped plus plugins.

## 2. Native web platform for motion & layout (use before any library)

As of October 2026 the three big motion APIs are all Baseline: same-document View Transitions (Oct 2025), scroll-driven animations (Firefox 159, Oct 2026) and `@starting-style`. Check [caniuse.com](https://caniuse.com) and [webstatus.dev](https://webstatus.dev) for anything marked "partial".

**Motion primitives in CSS**

| Feature | What it unlocks | Support (Nov 2026) |
| --- | --- | --- |
| `transition` + `@keyframes` | 60–120 fps compositor animation of `transform`, `opacity`, `clip-path`, `filter`; `transition-behavior: allow-discrete` animates `display`/`content-visibility` | Baseline |
| [`@starting-style`](https://developer.mozilla.org/docs/Web/CSS/@starting-style) | Entry animations from `display: none` (dialogs, popovers, toasts) with no JS timing hacks | Baseline |
| `interpolate-size: allow-keywords` / `calc-size()` | Animate `height: auto`, accordions and `<details>` natively | Chrome 129+, Safari 26+; check Firefox |
| [View Transitions](https://developer.mozilla.org/docs/Web/API/View_Transition_API) (same-document) | `document.startViewTransition()`, `view-transition-name`, `view-transition-class`, `match-element`, transition `types`, `::view-transition-old/new` pseudo-elements; browser-level FLIP | Baseline Newly available (Chrome 111, Safari 18, Firefox 144) |
| View Transitions (cross-document) | `@view-transition { navigation: auto }` gives MPAs app-like page transitions in 3 lines | Chrome 126+, Safari 18.2+; Firefox partial/flagged, Interop 2026 focus |
| [Scroll-driven animations](https://scroll-driven-animations.style) | `animation-timeline: scroll()` / `view()`, `animation-range`, `scroll-timeline`, `view-timeline`, `timeline-scope`; progress bars, reveals, parallax, image sequences with zero JS and off-main-thread | Baseline Newly available (Chrome 115, Safari 26, Firefox 159) |
| `linear()` easing | Spring and bounce curves in pure CSS (generate with [linear-easing-generator](https://linear-easing-generator.netlify.app)) | Baseline |
| `@property` | Typed custom properties so gradients, angles and numbers interpolate | Baseline |
| `random()`, `sibling-index()`, `sibling-count()` | Stagger delays and playful variation without JS | Chrome 156 / Safari 26.2 (`random()`); Chrome 138+ (sibling functions) |
| Scroll snap + `scroll-state()` queries | `scroll-snap-type/align/stop`, `scrollend` event, `scroll-snap-change` events, \`@container scroll-state(stuck | snapped |
| `backdrop-filter`, `mask`, `clip-path: shape()`, `corner-shape: superellipse` | Glass, image reveals, arbitrary clip paths, Apple-style squircles (Chrome 139+, Safari 26) | Mostly Baseline; verify `shape()`/`corner-shape` |
| `content-visibility: auto`, `contain`, `will-change` | Skip off-screen rendering; isolate layout; promote layers sparingly | Baseline |

**UI primitives that used to need a JS library**

| Feature | Replaces | Support |
| --- | --- | --- |
| `popover` attribute + `popovertarget`, light dismiss, `::backdrop` | Tooltip/menu/toast libraries' open-close logic | Baseline 2024 |
| `<dialog>` + `showModal()`, `closedby`, invoker `command`/`commandfor` | Modal focus-trap and scroll-lock plumbing | Baseline; invokers Chrome 135+, Safari 26 |
| [CSS anchor positioning](https://developer.chrome.com/blog/anchor-positioning-api) (`anchor()`, `position-area`, `position-try-fallbacks`, `position-visibility`) | Floating UI / Popper for tooltips and dropdowns | Chrome 125+, Safari 26+; Firefox in progress |
| `<details name>` exclusive accordions, `::details-content`, `hidden="until-found"` | Accordion components, find-in-page friendly collapses | Baseline |
| Customizable `<select>` (`appearance: base-select`, `<selectedcontent>`) | Custom dropdown components | Chrome 135+; others in progress |
| Container queries (size + style), `:has()`, `@scope`, nesting, `@layer`, `@mixin`/`@function` | Responsive component logic in JS, Sass | Baseline (functions/mixins Chrome 139+/146+) |
| `text-wrap: balance` / `pretty`, `text-box-trim`, `field-sizing: content` | Balancer scripts, textarea autosize | Baseline (verify `text-box-trim` in Firefox) |
| `color-mix()`, relative color syntax, `oklch()`, `light-dark()`, `contrast-color()` | Sass color functions, JS theme math | Baseline 2025 (`contrast-color()` partial) |
| `display: grid-lanes` (masonry) | Masonry.js, column hacks | Safari 26.4+; Chrome/Firefox in progress |
| `margin-trim`, `reading-flow`, CSS typed arithmetic | `:first-child` overrides, tab-order fixes for grid | Chrome 155 / Safari 16.4; Baseline Oct 2026 (typed arithmetic) |
| JPEG XL | Smaller images than AVIF at high quality | Chrome 155, Firefox 158, Safari 17 (Oct 2026) |

**User preference & capability queries (every premium UI honors these)**

- `prefers-reduced-motion`, `prefers-reduced-transparency`, `prefers-contrast`, `prefers-color-scheme`, `forced-colors`, `dynamic-range`, `hover`/`pointer`/`any-pointer`, `update`, `scripting`.
- `env(safe-area-inset-*)`, `100dvh`/`svh`/`lvh`, `viewport-fit=cover`, `interactive-widget` for keyboards on mobile.

**JavaScript APIs worth knowing**

| API | Use |
| --- | --- |
| `IntersectionObserver`, `ResizeObserver`, `MutationObserver` | Reveal-on-scroll, responsive components, DOM reactions without polling |
| `requestAnimationFrame`, `requestIdleCallback`, `scheduler.yield()`, `scheduler.postTask()` | Frame-aligned work, yielding to keep INP under 200 ms |
| [Navigation API](https://developer.mozilla.org/docs/Web/API/Navigation_API) | SPA routing with built-in transitions and scroll restoration (Chrome 102+, Firefox 147+, Safari 26.4+) |
| [Speculation Rules](https://developer.chrome.com/docs/web-platform/prerender-pages) (`prerender`/`prefetch`) | Near-instant navigations; pair with cross-document view transitions (Chrome/Edge) |
| bfcache, Service Workers, `Cache` API | Instant back/forward, offline, PWA |
| `ScrollTimeline` / `ViewTimeline` (WAAPI) | JS-controlled scroll-linked animations off the main thread |
| `Highlight` API, `CSS.registerProperty`, `CSS.paintWorklet` (Chrome) | Custom text highlights, typed properties from JS, Houdini paint |
| WebGPU (Chrome 113, Safari 26, Firefox 141), `OffscreenCanvas`, Workers | Heavy graphics off the main thread |
| Pointer Events, `touch-action`, `getCoalescedEvents()`, Visual Viewport, Vibration API | Gesture-driven UI, haptics on Android, keyboard-aware layouts |
| Web Share, Clipboard, Screen Wake Lock, `<install>` / `navigator.install()` (Chrome 158 beta) | App-like affordances on the web |

## 3. Scroll: smooth scroll, scroll-triggered motion, carousels

The 2026 stack for scroll-heavy sites is Lenis for feel, GSAP ScrollTrigger for choreography, and native scroll-driven animations for simple reveals and progress bars. Scroll listeners and AOS-style libraries are now the slow path.

**Smooth-scroll engines**

| Tool | Notes | Status |
| --- | --- | --- |
| [Lenis](https://lenis.darkroom.engineering) (`lenis`, `lenis/react`, Vue/Nuxt wrappers) | MIT, keeps the native scrollbar, lerp/duration/easing, `data-lenis-prevent` for nested scrollers, hooks into GSAP's ticker; the Awwwards default | Standard |
| [Locomotive Scroll v5](https://scroll.locomotive.ca) (5.0.1, Jan 2026) | 9.4 kB wrapper on Lenis: `data-scroll` attributes for in-view classes, parallax speed, progress and direction | Standard (declarative projects) |
| GSAP ScrollSmoother (free since 2025) | Deepest ScrollTrigger integration, per-element `data-speed`/`data-lag`, needs wrapper/content structure | Standard with GSAP |
| Native `scroll-behavior: smooth` + `scrollIntoView()` | Zero JS for anchor links; the right answer for apps, docs and dashboards | Standard |

Smooth scroll is a marketing-site tool; disable it under `prefers-reduced-motion`, keep touch native (Lenis `syncTouch` off), and never use it on content-heavy apps.

**Scroll-triggered and scroll-linked tools**

| Tool | Best for | Status |
| --- | --- | --- |
| GSAP ScrollTrigger | Pinning, scrubbing, snapping, horizontal sections, `batch()` staggers, `normalizeScroll()` for mobile address bars, markers for debugging | Standard |
| Native scroll-driven animations (`view()`, `scroll()`) | Reveal on enter, progress bars, parallax layers, image sequences; runs off-main-thread | Standard (Baseline Oct 2026) |
| `IntersectionObserver` (+ `react-intersection-observer`, Motion `whileInView`/`useInView`, Svelte actions) | Toggle a class or trigger a one-shot animation when visible | Standard |
| Motion `useScroll` + `useTransform`, `scroll()` vanilla | Scroll-linked values in React/Vue components, progress indicators | Standard |
| [Scrollama](https://github.com/russellsamora/scrollama) | Data-journalism scrollytelling steps (sticky graphic + stepping text) | Niche |
| [simpleParallax](https://simpleparallax.com), `react-scroll-parallax` | Image-only parallax with little code | Niche |
| AOS, ScrollReveal, Sal.js, WOW.js, ScrollOut | Attribute-driven fade-ins; still common, but replace with `view()` timelines | Legacy |
| ScrollMagic, Waypoints, Skrollr, Rellax, Parallax.js | Unmaintained | Legacy |

**Signature scroll patterns and how they're built**

- Pinned storytelling section: `ScrollTrigger` `pin: true, scrub: 1` on a timeline, or CSS `position: sticky` + `view()` timeline.
- Horizontal scroll inside vertical page: pin a wrapper and tween `xPercent`, or CSS scroll-snap on the x-axis with `scroll-timeline` for the progress bar.
- Image-sequence scrub (Apple product pages): preload 60–150 WebP/AVIF frames, draw to `<canvas>` from scroll progress; never scrub `<video>.currentTime` (janky, decode-bound) unless using a frame-indexed tool.
- Scroll-scrubbed Lottie/Rive: drive `goToAndStop()` or a Rive number input from ScrollTrigger progress.
- Stacking cards: `position: sticky` on each card with scale/opacity from `view()` or ScrollTrigger.
- Text reveal on scroll: SplitText lines + `ScrollTrigger.batch`, or `view()` timeline with `animation-range: entry 0% entry 60%`.
- Scroll progress bar: three lines of CSS with `animation-timeline: scroll(root)`.
- Hide-on-scroll-down header: `Observer` plugin or `scroll-state(stuck)` + a direction class.
- Infinite marquee/logo wall: duplicated track + CSS `translateX(-50%)` keyframes, pause on hover; GSAP `horizontalLoop` helper for interactive speed; `react-fast-marquee`.
- Scrollspy/table of contents: `IntersectionObserver` with `rootMargin` tuned to the sticky header height.
- Scroll snap sections: `scroll-snap-type: y mandatory` + `scroll-snap-stop: always`; style active section with `scroll-state(snapped)`.

**Sliders & carousels**

| Tool | Notes | Status |
| --- | --- | --- |
| [Embla Carousel](https://www.embla-carousel.com) | Tiny, framework bindings, plugins (autoplay, wheel, fade, class names); what shadcn/ui ships | Standard |
| [Swiper](https://swiperjs.com) 11+ | Everything built in (effects: cube, coverflow, cards, creative; thumbs; virtual slides; Web Component) at a larger size | Standard |
| [Keen Slider](https://keen-slider.io), [Splide](https://splidejs.com), Glide.js | Lightweight alternatives; Splide has strong a11y defaults | Niche |
| CSS-only carousels: scroll-snap + `::scroll-button()` + `::scroll-marker` | Native buttons and dots with no JS (Chrome 135+; progressive enhancement elsewhere) | Rising |
| Flickity (commercial), Slick, Owl, Tiny Slider | jQuery era | Legacy |

**Long lists**: TanStack Virtual, `react-virtuoso`, `@tanstack/react-virtual` for Vue/Svelte/Solid; `content-visibility: auto` for static long pages; `react-window` is legacy.

**Scroll hygiene**: passive listeners, `overscroll-behavior: contain` on drawers, `scrollbar-gutter: stable` to stop layout shift, `scrollbar-width`/`scrollbar-color` for styled bars, `scrollend` event instead of debounced scroll, restore scroll position on back navigation (Navigation API or framework router).

## 4. 3D, WebGL/WebGPU, shaders, canvas & generative

WebGPU is production-ready in every major browser (Chrome 113, Firefox 141+, Safari 26), so 2026's premium 3D stack is Three.js r182+ with `WebGPURenderer` and TSL shaders, falling back to WebGL 2 automatically. React Three Fiber v9.6 is stable; v10 (alpha, 2026) adds first-class WebGPU with `useUniforms`, `useNodes` and `usePostProcessing`.

**Engines & framework bindings**

| Tool | Role | Status |
| --- | --- | --- |
| [Three.js](https://threejs.org) (r182, Dec 2025) | The default 3D engine; `three/webgpu` entry, TSL (Three Shading Language) compiles to WGSL and GLSL, compute shaders for particles/physics | Standard |
| [React Three Fiber](https://r3f.docs.pmnd.rs) + [Drei](https://drei.docs.pmnd.rs) (v11 alpha) | Declarative Three in React; Drei helpers: `Environment`, `MeshTransmissionMaterial`, `Text`/`Text3D`, `ScrollControls`, `Html`, `Float`, `ContactShadows`, `useGLTF`, `CameraControls`; `@react-three/postprocessing`, `@react-three/rapier`, `@react-three/xr`, `gltfjsx` | Standard |
| [Threlte](https://threlte.xyz) (Svelte), [TresJS](https://tresjs.org) (Vue), Angular Three | Same idea for other frameworks | Standard per framework |
| [Babylon.js](https://www.babylonjs.com) 8 | Full engine with editor, Havok physics, GUI, WebGPU; stronger for games/configurators than marketing sites | Standard (apps/games) |
| [OGL](https://github.com/oframe/ogl) | Minimal WebGL for shader-heavy creative sites; small bundle | Niche |
| [PixiJS](https://pixijs.com) v8 (WebGPU) | Fast 2D sprites, filters, particles, interactive canvas | Standard (2D) |
| PlayCanvas, Needle Engine, Unity/Unreal/Godot web export, Phaser 4, Kaplay, Excalibur | Game-engine routes; heavy bundles, use for games/configurators | Niche |
| [`<model-viewer>`](https://modelviewer.dev) | Google web component for product 3D + AR (USDZ/Quick Look, Scene Viewer) with zero code | Standard (e-commerce) |
| Curtains.js / gpu-curtains | WebGL/WebGPU planes synced to DOM elements for image distortion effects | Niche |

**No-code / low-code 3D and shader tools**

| Tool | What it gives you |
| --- | --- |
| [Spline](https://spline.design) | 3D design tool with interactive exports (`@splinetool/react-spline`, web component), physics, AI generation; the most common 3D hero source |
| [Unicorn Studio](https://unicorn.studio) | WebGL effects editor (noise, ripple, text distortion, cursor effects) exported as an embed |
| [Paper Design shaders](https://shaders.paper.design) (`@paper-design/shaders-react`) | Mesh gradients, dithering, grain, god rays, water as React components |
| [ShaderGradient](https://shadergradient.co), [Vanta.js](https://www.vantajs.com) | Animated gradient/background scenes with a few props (Vanta is aging) |
| Blender, Womp, Meshy/Tripo (AI 3D), Polycam/Luma (scans, splats) | Asset creation; export glTF/GLB with Draco or meshopt compression |
| [Cables.gl](https://cables.gl), Hydra, Shadertoy | Node-based and live-coded shader experiments |

**Shaders & effects vocabulary**

- Languages: GLSL (WebGL), WGSL (WebGPU), TSL (write once); learn with [The Book of Shaders](https://thebookofshaders.com); reuse [lygia](https://lygia.xyz) shader functions.
- Post-processing: `pmndrs/postprocessing` or TSL effect nodes: bloom, depth of field, chromatic aberration, vignette, SSAO, god rays, film grain, dithering (Bayer), ASCII, pixelation, halftone, datamosh/glitch.
- Signature effects: image hover distortion (displacement maps), liquid/ripple on cursor, fluid simulation (WebGL Fluid), image trails, grainy and mesh gradients, noise-displaced spheres, refraction/glass (`MeshTransmissionMaterial`), holographic foil, particle text, morphing point clouds, 3D Gaussian splatting (Spark, gsplat.js, Luma web).
- Physics: Rapier (WASM, 2D/3D, default with R3F), cannon-es, Matter.js (2D DOM-ish scenes), Havok (Babylon), Jolt.
- Particles: tsParticles (DOM backgrounds), `InstancedMesh`/`Points` + GPGPU, WebGPU compute for 1M+ particles.

**2D canvas & creative coding**: PixiJS, Konva (scene graph + React binding), Fabric.js (editors), p5.js 2.x, Two.js, Paper.js, Rough.js (hand-drawn look), Zdog (pseudo-3D), `canvas-sketch`, simplex-noise for flow fields and generative art.

**Performance rules for 3D on marketing sites**

- Clamp `devicePixelRatio` to 2 (1.5 on mobile); use `frameloop="demand"` when idle.
- Compress assets: Draco or meshopt geometry, KTX2/Basis textures, `gltf-transform` pipeline; keep hero scenes under \~2–3 MB.
- Lazy-load the 3D bundle after LCP; show a poster image first and under `prefers-reduced-motion` or when `navigator.gpu`/WebGL is missing.
- Prefer `InstancedMesh`, LOD and baked lighting; profile with `r3f-perf`, Spector.js and Chrome's Performance panel.
- Keep the 3D canvas off the main thread's hot path: `OffscreenCanvas` + Worker for heavy scenes.

## 5. Designed animation formats: Lottie, Rive, SVG, animated icons

Rule in 2026: CSS for UI transitions, Lottie/dotLottie for designer-authored illustrations and icons, Rive for anything that must react to state or data. Both formats now have state machines, so the choice is mostly runtime size and pipeline.

| Format / runtime | Strengths | Watch-outs | Status |
| --- | --- | --- | --- |
| [Lottie](https://lottiefiles.com) JSON (`lottie-web`, `lottie-react`, `lottie-ios/android`, `lottie-react-native`, Skottie) | After Effects export via Bodymovin, 4.2M weekly downloads across runtimes, huge free library, plays everywhere without a special runtime | JSON can bloat; masks, mattes and effects hurt performance; `lottie-web` is \~60 KB+ | Standard |
| [dotLottie](https://dotlottie.io) `.lottie` (`@lottiefiles/dotlottie-web`, `dotlottie-react`, `dotlottie-wc`) | Zipped bundle with multiple animations, themes (`setTheme('dark')`), and (2026) state machines authored in Lottie Creator; WASM renderer is smaller and faster than `lottie-web` | Newer; verify feature parity for exotic AE features | Standard (preferred Lottie runtime) |
| [Rive](https://rive.app) `.riv` (`@rive-app/canvas`, `@rive-app/webgl2`, `@rive-app/react-canvas`, iOS, Android, Flutter, RN, Unity, Unreal) | Binary files 10–15× smaller than Lottie, state machines with inputs/triggers/events, data binding (live text, colors, images, lists), bones and mesh deformation, responsive layouts, audio, scripting; one C++ renderer everywhere | Needs the Rive runtime (\~100 KB+ WASM); editor is freemium (Cadet $9/mo, Voyager $32/mo); smaller community | Standard for interactive animation |
| Animated SVG (CSS/SMIL/JS) | Crisp at any size, stylable with CSS variables, tiny for line art; `offset-path` motion paths are Baseline | SMIL has no timeline tooling; complex SVG DOM is slow (keep nodes under \~1k) | Standard |
| Animated WebP/AVIF, `<video muted autoplay loop playsinline>` | Replace GIFs; AV1/HEVC loops for photographic heroes | Video can't be styled; add poster + reduced-motion fallback | Standard |

**Authoring tools**

| Tool | Output | Note |
| --- | --- | --- |
| After Effects + Bodymovin / LottieFiles plugin | Lottie, dotLottie | Still the pro pipeline |
| [Lottie Creator](https://lottiefiles.com/lottie-creator) | dotLottie with themes + state machines | Browser-based; free tier has 5 exports |
| [Rive Editor](https://rive.app) | `.riv` | Design + animate + logic in one tool, live preview of runtime |
| [Jitter](https://jitter.video) | Lottie, MP4, GIF | Figma-like motion design for marketing |
| [Cavalry](https://cavalry.scenegroup.co) | Lottie, MP4 | Procedural/data-driven motion; free for individuals since Apr 2026 |
| [SVGator](https://www.svgator.com), [Lottielab](https://www.lottielab.com), Linearity Move, Keyshape | SVG + CSS/JS, Lottie | Code-free SVG and Lottie animation |
| Figma (LottieFiles, Aninix, Motion plugins) | Lottie, GIF | Prototype first, export motion second |

**SVG techniques worth knowing**

- Line drawing: `stroke-dasharray`/`stroke-dashoffset` (GSAP DrawSVG, Vivus.js, Anime `createDrawable`).
- Shape morphing: GSAP MorphSVG (uneven point counts), Flubber, KUTE.js; CSS `clip-path: path()`/`shape()` morphs with same point counts.
- Filters as effects: `feTurbulence` noise/grain, `feDisplacementMap` liquid and "Liquid Glass" refraction, `feGaussianBlur` + `feColorMatrix` gooey blobs, `feMorphology` outlines.
- Motion along a path: CSS `offset-path`/`offset-distance` (Baseline), `<animateMotion>`, GSAP MotionPath.
- Optimize with SVGO/SVGOMG, `vector-effect: non-scaling-stroke`, `shape-rendering`, inline critical icons and sprite the rest.
- Generators: Haikei (blobs, waves, layered shapes), fffuel (gradients, noise, textures), Blobmaker, Get Waves.

**Icon systems**: Lucide (and `pqoqubbw/icons`, Lucide animated with Motion), Phosphor (6 weights), Heroicons, Tabler (5,900+), Radix Icons, Hugeicons (incl. animated), Iconify (200k+ icons, one API), Font Awesome 7, Material Symbols (variable axes: fill, weight, grade); animated icon sources: Lordicon, Rive community, LottieFiles icons, Icons8 animated. Animate icon state changes (hamburger ↔ close, play ↔ pause, heart fill) with transforms on SVG parts rather than swapping files.

## 6. Component libraries & headless primitives

The 2026 model is layered: a headless primitive library handles accessibility and behavior, a copy-paste layer (shadcn/ui and its ports) handles styling, and single-purpose components fill the gaps. shadcn/ui passed 75k stars, added a Visual Builder (Feb 2026), and `npx shadcn init` now defaults to Base UI primitives (July 2026) with Radix still supported.

**Headless primitives (behavior + a11y, no styles)**

| Library | Frameworks | Notes | Status |
| --- | --- | --- | --- |
| [Base UI](https://base-ui.com) 1.0 (2026) | React | From the Radix/Floating UI/MUI creators; `render` prop composition; the new default under shadcn/ui | Standard |
| [Radix Primitives](https://www.radix-ui.com/primitives) | React | 130M monthly downloads, `asChild`; release cadence slowed and ownership is a concern | Standard (watch) |
| [React Aria](https://react-spectrum.adobe.com/react-aria) (Adobe) | React | Deepest accessibility and internationalization; React Aria Components for less boilerplate | Standard (a11y-critical apps) |
| [Ark UI](https://ark-ui.com) / [Zag.js](https://zagjs.com) | React, Vue, Solid, Svelte | State-machine driven, one API across frameworks; powers Chakra v3 and Park UI | Standard (multi-framework) |
| [Headless UI](https://headlessui.com) v2 | React, Vue | Tailwind Labs; small set, pairs with Tailwind Plus | Standard (small) |
| Ariakit, Downshift, [Floating UI](https://floating-ui.com) | React / vanilla | Ariakit for composable a11y; Downshift for combobox; Floating UI for positioning until CSS anchor positioning is Baseline | Niche |
| [Angular Aria](https://angular.dev) + Angular CDK | Angular | Headless primitives from the Angular team (2025+), CDK overlay/drag-drop/virtual scroll | Standard (Angular) |
| [Kobalte](https://kobalte.dev), Corvu | Solid | Headless Solid primitives | Standard (Solid) |
| [Bits UI](https://bits-ui.com), Melt | Svelte 5 | Headless Svelte; under shadcn-svelte | Standard (Svelte) |
| [Reka UI](https://reka-ui.com) (ex-Radix Vue) | Vue | Under shadcn-vue and Nuxt UI | Standard (Vue) |

**Styled & copy-paste layers**

| Framework | Default pick | Also strong |
| --- | --- | --- |
| React | [shadcn/ui](https://ui.shadcn.com) (Tailwind v4, registry, blocks, themes, Visual Builder) | Radix Themes, Park UI (Ark + Panda), Mantine 8, Chakra UI v3, MUI v7, HeroUI (ex-NextUI, Motion-based), Untitled UI React, Origin UI, Kibo UI, Tremor (dashboards), daisyUI v5, Flowbite, Preline, Tailwind Plus (paid) |
| Vue / Nuxt | [Nuxt UI](https://ui.nuxt.com) v4 (Reka + Tailwind v4) or shadcn-vue | PrimeVue v4 (styled + unstyled modes), Vuetify 3, Quasar, Naive UI, Element Plus, Inspira UI (animated) |
| Svelte | [shadcn-svelte](https://www.shadcn-svelte.com) (Bits UI) | Skeleton v4, Flowbite Svelte, Melt builders, Superforms + Formsnap, Paneforge, LayerChart |
| Solid | shadcn-solid (Kobalte) | Ark UI Solid, Solid UI |
| Angular | [Spartan](https://www.spartan.ng) (shadcn for Angular on CDK) or Angular Material (M3) | PrimeNG, Taiga UI, NG-ZORRO |
| Web components / any stack | [Web Awesome](https://webawesome.com) (ex-Shoelace, Font Awesome team), Lit | Spectrum Web Components, Carbon Web Components, Vaadin, Ionic, Wired Elements (sketchy) |
| Design-system reference implementations | Geist (Vercel), Primer (GitHub), Polaris (Shopify), Carbon (IBM), Spectrum (Adobe), Fluent 2 (Microsoft), Atlassian DS, Gestalt (Pinterest) | Study these for API design and motion tokens |

**Single-purpose components that premium apps keep reusing**

| Need | Library |
| --- | --- |
| Drawer / bottom sheet | [Vaul](https://vaul.emilkowal.ski) (React), vaul-vue, vaul-svelte |
| Toasts | [Sonner](https://sonner.emilkowal.ski) (stacked, swipe, promise state); react-hot-toast older |
| Command palette ⌘K | [cmdk](https://cmdk.paco.me), Base UI Combobox, kbar |
| Animated numbers | NumberFlow |
| Resizable panels | react-resizable-panels, Paneforge |
| OTP / masked input | input-otp, maskito |
| Forms + validation | react-hook-form or TanStack Form + Zod/Valibot; Conform for server actions; Superforms (Svelte); VeeValidate (Vue) |
| Tables / data grids | TanStack Table (headless), AG Grid, Glide Data Grid, MUI X |
| Date pickers | react-day-picker, Cally (web component), Flatpickr (legacy), Temporal API for logic |
| Theming | next-themes, CSS `light-dark()` + `color-scheme`, `@media (prefers-color-scheme)` |
| URL/app state | nuqs, Zustand, Jotai, TanStack Query (server state) |
| Hooks | usehooks-ts, @uidotdev/usehooks, VueUse, Svelte runes-based utilities |
| AI chat UIs (2025–26 trend) | Vercel AI Elements, assistant-ui, CopilotKit, Streamdown (streaming markdown), use-stick-to-bottom |
| File upload | react-dropzone, Uppy, FilePond |
| Emoji, mentions, rich input | emoji-mart, Tiptap/Lexical with mention extensions |

What to check when picking any of these: keyboard and screen-reader behavior, `prefers-reduced-motion` handling, RTL, bundle size, SSR/RSC compatibility, and whether exit animations are supported (Base UI and Radix expose `data-[state]` attributes for CSS exit transitions).

## 7. Premium animated component collections & effect sources

Most "wow" effects on 2026 landing pages come from a dozen copy-paste collections built on Tailwind + Motion (sometimes GSAP, OGL or Three). [21st.dev](https://21st.dev) aggregates 60+ of them with live previews and an MCP server so you can pull components into Cursor or Claude Code; [Codrops](https://tympanus.net/codrops) remains the canonical source for original creative effects with tutorials.

| Collection | Stack | Known for | Pricing |
| --- | --- | --- | --- |
| [Magic UI](https://magicui.design) | React, Tailwind, Motion | 150+ pieces: marquee, dock, animated beam, number ticker, orbiting circles, border/shine beam, blur fade, globe (Cobe), meteors, bento grid; Magic MCP | Free + Pro templates |
| [Aceternity UI](https://ui.aceternity.com) | React, Tailwind, Motion, some Three | Aurora/wavy/vortex backgrounds, sparkles, 3D card, lamp, spotlight, background beams, tracing beam, container scroll, MacBook scroll, floating navbar, infinite moving cards, canvas reveal, moving border, lens | Free + Pro |
| [React Bits](https://reactbits.dev) | React (JS/TS, Tailwind or CSS), GSAP, Motion, OGL, Three | #2 JS Rising Star 2025; text effects (split, blur, decrypt, scramble, shiny, variable proximity, ASCII), WebGL backgrounds (Silk, Iridescence, Liquid Chrome, Hyperspeed, Dither, Threads, Galaxy), Dock, Stack, Tilted/Spotlight/Pixel cards, Magnet, Glass surface | Free (MIT) |
| [Motion Primitives](https://motion-primitives.com) | React, Tailwind, Motion | Tasteful app-grade primitives: text effect/loop/morph, animated group, in-view, sliding number, morphing dialog, cursor, dock, progressive blur, border trail, glow, transition panel, magnetic | Free + Pro |
| [Animate UI](https://animate-ui.com) | React, shadcn-style, Motion (Radix and Base variants) | Animated versions of shadcn components, animated icons, counting/sliding numbers, highlight/typing/rolling/splitting text, bubble/stars/hexagon backgrounds, cursor | Free |
| [Cult UI](https://cult-ui.com) | React, Tailwind, Motion | Dynamic island, texture cards, 3D carousel, sortable list, family-style dock, popovers | Free + Pro |
| [Kokonut UI](https://kokonutui.com), [Skiper UI](https://skiper-ui.com), [Smoothui](https://smoothui.dev), [Luxe](https://luxe.guhrodrigues.com), [UI Layouts](https://ui-layouts.com), Eldora UI, Indie UI, Syntax UI, Berlix UI, Hyperiux Vault | React, Tailwind, Motion/GSAP | Cards, buttons, inputs, AI prompt boxes, scroll-lerp galleries, 3D carousels, text effects | Mostly free, some Pro |
| [Fancy Components](https://fancycomponents.dev) | React, Motion, Matter.js | Physics text (gravity, elastic line), pixel/image trail cursors, letter swap, scramble hover, vertical cut reveal, marquee along SVG path, breathing text, screensaver | Free |
| [Animata](https://animata.design) | React, Tailwind | 90+ small effects: bento grids, hover cards, skeletons, text, widgets | Free |
| [Hover.dev](https://www.hover.dev) | React, Tailwind, Motion | Polished recipes: navs, hero text, cards, buttons; good for learning Motion patterns | Paid |
| [Tailark](https://tailark.com), [shadcnblocks](https://www.shadcnblocks.com), Page UI, Launch UI, Once UI | React, shadcn | Marketing sections (hero, pricing, features, testimonials, footer) that drop into shadcn projects | Free / paid |
| [Inspira UI](https://inspira-ui.com), [Vue Bits](https://vue-bits.dev) | Vue / Nuxt | Ports of Aceternity/Magic and React Bits | Free |
| [Svelte Animations](https://animation-svelte.vercel.app), shadcn-svelte-extras | Svelte 5 | Magic UI / Aceternity ports for Svelte | Free |
| [Uiverse](https://uiverse.io) | CSS/Tailwind, community | 6,000+ open-source buttons, loaders, toggles, cards | Free |
| [Codrops](https://tympanus.net/codrops) Playground & Demos | Vanilla, GSAP, Three, OGL | The original source for grid-to-fullscreen, image trails, text effects, WebGL transitions, menu reveals; each demo has a tutorial | Free |

**CSS-only utilities and generators**

- Tailwind: `tw-animate-css` (successor to `tailwindcss-animate`), [Tailwind Motion](https://rombo.co/tailwind) (`motion-preset-*`, `motion-translate-x-in-*`), `@midudev/tailwind-animations`.
- Vanilla: Animate.css (aging but fine), [Animista](https://animista.net) generator, Hover.css, CSShake, Magic.css, [Open Props](https://open-props.style) animations/easings, Keyframes.app, cssfx, AnimXYZ.
- Loaders: [ldrs](https://uiball.com/ldrs) (uiball), [css-loaders.com](https://css-loaders.com) (600+ single-element loaders), SpinKit, Loading.io.
- Backgrounds: [bg.ibelick.com](https://bg.ibelick.com) Tailwind snippets, Stripe-style mesh gradient (Gradient.js / "whatamesh"), [MeshGradient](https://meshgradient.in), Haikei, fffuel, Cobe/globe.gl globes, tsParticles, grainy gradients (SVG `feTurbulence`), Vanta.

**Tutorial authors whose patterns define the current look**

- [Emil Kowalski](https://emilkowal.ski) (Vaul, Sonner; [Animations on the Web](https://animations.dev) course), [Rauno Freiberg](https://rauno.me/craft) (craft, [easing.dev](https://easing.dev), Invisible Details of Interaction Design), Josh Comeau (CSS for JS, Whimsical Animations), Sam Selikoff ([Build UI](https://buildui.com) recipes), Jhey Tompkins (CSS experiments), Adam Argyle (GUI Challenges), Bramus Van Damme (scroll-driven & view transitions), Olivier Larose (blog.olivierlarose.com: zoom parallax, curved menu, mask cursor, perspective transitions, floating gallery, sticky footer), Bruno Simon (Three.js Journey), Yuri Artiukh (WebGL streams), Awwwards Academy courses, Manu Arora, Dillion Verma, Julian Garnier (Anime.js).

Use these as references, not final code: audit each snippet for `prefers-reduced-motion`, keyboard focus, hydration safety and bundle weight before shipping.

## 8. Styling systems & CSS tooling

Tailwind CSS v4.3 (May 2026) is the default styling layer for premium work; the serious alternatives are CSS Modules with modern CSS, or zero-runtime CSS-in-JS (Panda, vanilla-extract, StyleX). Runtime CSS-in-JS (styled-components, Emotion) is in maintenance and conflicts with React Server Components.

| Tool | What it is | When | Status |
| --- | --- | --- | --- |
| [Tailwind CSS](https://tailwindcss.com) v4.3 | Oxide engine (Rust), CSS-first `@theme` config, native cascade layers, `@property`-backed utilities, container queries (`@container`, `@container-size`), 3D transforms, text shadows, masks, scrollbar utilities, new palettes (mauve, olive, mist, taupe), `@apply` inside mixins, Vite 8 + webpack plugins | Nearly every new project; pairs with shadcn/ui and every collection in §7 | Standard |
| Tailwind helpers | `tailwind-merge`, `clsx`/`cn()`, `cva` (class-variance-authority) or `tailwind-variants`, `prettier-plugin-tailwindcss`, `tw-animate-css`, `@tailwindcss/typography`, `@tailwindcss/forms`, `tailwindcss-motion` | Variant-driven component APIs | Standard |
| [Tailwind Plus](https://tailwindcss.com/plus) | Paid UI blocks, templates, Catalyst kit, vanilla JS support (2025) | Fast marketing and app shells | Standard (paid) |
| CSS Modules + modern CSS | Scoped classes with nesting, `@layer`, custom properties, container queries; no runtime | Design systems that outlive frameworks; Astro/Vite/Next all support it | Standard |
| [Panda CSS](https://panda-css.com) | Build-time CSS-in-JS with tokens, recipes, patterns; powers Park UI | Typed design-token systems | Standard |
| [vanilla-extract](https://vanilla-extract.style) | Zero-runtime, TypeScript-typed stylesheets, Sprinkles atomic layer | Typed tokens without Tailwind syntax | Standard |
| [StyleX](https://stylexjs.com) (Meta) | Compile-time atomic CSS, predictable overrides, used across Meta | Very large apps | Niche |
| [UnoCSS](https://unocss.dev) | Instant on-demand atomic engine, presets (Wind, Icons, Attributify) | Vite/Vue projects wanting Tailwind-style with extras | Niche |
| [Open Props](https://open-props.style) | Design tokens as CSS variables (sizes, easings, animations, shadows, gradients) | Vanilla CSS projects | Niche |
| Sass / SCSS | Still common in agencies and legacy design systems; most features now native (nesting, `@mixin`/`@function`, color functions) | Maintaining existing systems | Legacy for new work |
| styled-components, Emotion, Stitches | Runtime CSS-in-JS; Stitches archived, styled-components in maintenance | Existing codebases only | Legacy |
| Lightning CSS, PostCSS | Transpile, minify, prefix; Lightning CSS is the fast default inside Vite/Parcel/Tailwind | Build pipeline | Standard |

**Conventions that read as premium**

- Tokens first: `--space-*` on a 4/8 px scale, `--radius-*` with nested-radius math (inner = outer − padding), `--shadow-*` layered (2–3 soft shadows + 1 px border), `--ease-*` and `--duration-*` named by intent.
- Color in OKLCH with `color-mix()` and relative color syntax for hover/active states; `light-dark()` for theming instead of duplicated selectors.
- Logical properties (`margin-inline`, `inset-block`) for RTL; `@layer` ordering (reset, tokens, base, components, utilities, overrides).
- Container queries for components, media queries only for page layout; `clamp()` for fluid space and type.
- Utility classes for layout, custom properties for theme, one component file per interactive piece; avoid `!important` and deep selectors.
- Lint with Stylelint + `stylelint-config-standard`, format with Prettier; sort Tailwind classes automatically.
- Critical CSS inlined (<14 KB), the rest loaded async; `content-visibility: auto` for long pages; no CSS frameworks with unused resets (Bootstrap only if the team already lives in it).

## 9. Typography

Premium typography in 2026 is one or two variable fonts, self-hosted and subset, sized with `clamp()`, with `text-wrap: balance` on headings and `tabular-nums` on anything numeric. Text effects are built with SplitText-style line masks and scroll-driven weight or opacity, never by animating `font-size`.

**Setup checklist**

| Topic | Do this | Tools |
| --- | --- | --- |
| Fluid scale | `font-size: clamp(min, preferred vw + rem, max)` for every step; fluid space too | [Utopia](https://utopia.fyi), [Typescale](https://typescale.com), `fluid-tailwind` |
| Variable fonts | One WOFF2 per family with `wght`/`opsz`/`wdth` axes; `font-optical-sizing: auto`; animate `font-variation-settings` for hover/scroll weight | Inter 4, Roboto Flex, Fraunces, Recursive, Geist, Manrope, Bricolage Grotesque |
| Loading | Self-host, `preload` the body font, `font-display: swap` (or `optional` for zero CLS), subset with `unicode-range`, metric-matched fallbacks via `size-adjust`/`ascent-override`/`descent-override` | `next/font`, Fontaine (Vite/Nuxt), Capsize, Fontsource, glyphhanger/pyftsubset, Wakamai Fondue |
| OpenType features | `font-variant-numeric: tabular-nums slashed-zero`, `font-feature-settings: "ss01", "cv11", "case"`, `font-kerning: normal`, `font-variant-ligatures` | Inspect axes/features with Wakamai Fondue |
| Measure & rhythm | 45–75 ch body (`max-width: 65ch`), line-height 1.45–1.6 body, 1.0–1.15 display, negative tracking on large display (−0.01 to −0.03 em), 4/8 px vertical rhythm | — |
| Wrapping | `text-wrap: balance` (headings, ≤ 4 lines), `text-wrap: pretty` (body), `hyphens: auto` with `lang`, `overflow-wrap: anywhere` for URLs, `hanging-punctuation` | Native; `react-wrap-balancer` is now unnecessary |
| Vertical alignment | `text-box-trim: trim-both; text-box-edge: cap alphabetic` to kill the half-leading gap in buttons and cards | Verify Firefox support |
| Rendering | `font-synthesis: none`, avoid `-webkit-font-smoothing` hacks except on dark backgrounds, `font-size-adjust` for fallback parity | — |
| Accessibility | ≥ 16 px body on mobile, `rem` units, never `maximum-scale=1`, WCAG 1.4.12 spacing must not break layout, contrast ≥ 4.5:1 (or APCA Lc 60+) | — |
| International text | `lang` attribute per element, per-script fallback stacks, `Intl.Segmenter` for grapheme-safe splitting (emoji, Indic), `word-break: keep-all` for CJK, logical properties for RTL | — |

**Fonts people reach for in 2026**

| Tier | Examples |
| --- | --- |
| Free, premium-feeling | Inter 4, Geist / Geist Mono, Satoshi, General Sans, Cabinet Grotesk, Switzer (Fontshare); Instrument Sans/Serif, Manrope, Onest, Figtree, Bricolage Grotesque, Hanken Grotesk, Plus Jakarta Sans, DM Sans/Serif, Newsreader, Fraunces, Source Serif 4, Lora, IBM Plex, JetBrains Mono, Monaspace, Commit Mono (Google Fonts / Fontshare / GitHub) |
| Paid, agency look | Söhne, ABC Diatype, ABC Favorit, Neue Montreal, PP Editorial New, PP Neue Machina (Pangram Pangram), Suisse Int'l, GT America, Untitled Sans, Founders Grotesk (Klim), Aeonik, Matter, Maison Neue, Basel Grotesk, Berkeley Mono |
| Foundries & catalogs | Google Fonts, Fontshare, Adobe Fonts, Pangram Pangram, Klim, Grilli Type, Dinamo, Colophon, Commercial Type, Atipo, Velvetyne (libre), Collletttivo; inspiration at Typewolf and Fonts In Use |

**Text effects and how they're built**

- Line/word/char reveal: GSAP SplitText (free, `aria-label`-safe) or Motion `splitText()` + stagger inside `overflow: hidden` or `clip-path` masks; `yPercent: 100 → 0` with `power3.out`.
- Scroll-linked text: opacity/weight per word via `view()` timelines or ScrollTrigger scrub (the "paragraph lights up as you scroll" effect).
- Gradient / shimmer text: `background-clip: text` + animated `background-position` or `@property`-typed angle.
- Knockout text over video/image: `mix-blend-mode` or SVG `<mask>`.
- Outlined/stroked text: `-webkit-text-stroke` or `paint-order` on SVG text.
- Variable-weight proximity (text gets bolder near the cursor): `font-variation-settings` driven by pointer distance (React Bits "Variable Proximity").
- Scramble/decrypt, typewriter, text loop/morph: §1 single-purpose libraries; Motion Primitives Text Morph.
- Underline animations: `text-decoration-thickness` + `text-underline-offset` transitions, or `background-size` grow-from-left; `text-decoration-skip-ink` for descenders.
- Kinetic/experimental: text on `<textPath>`, 3D text with Drei `Text3D`, letter physics with Fancy Components or Matter.js.
- Streaming text (AI UIs): token-by-token fade with `animation: fade 150ms` per span, `Streamdown` for markdown.

Under `prefers-reduced-motion`, show text immediately and keep only opacity fades.

## 10. Page-section playbook: signature effects and how they're built

Each row is a pattern you'll see on award-winning sites and polished apps in 2026, with the standard way to build it. Pick one hero effect, one navigation idea and two or three micro-interactions per page; more than that reads as noise.

**Hero**

| Pattern | Build |
| --- | --- |
| Staggered headline reveal + sub-copy + CTA | SplitText lines (mask) → GSAP timeline or Motion `staggerChildren`; CTA scales in last; total under 1.2 s |
| 3D object / product | Spline embed, or R3F with `Float`, `Environment`, `ContactShadows`; poster image until loaded |
| Shader / mesh-gradient background | Paper Shaders, Unicorn Studio, Stripe-style gradient, Three `ShaderMaterial` with simplex noise; clamp DPR |
| Video background | `<video muted autoplay loop playsinline poster>` AV1/H.265, 6–10 s loop, under 2 MB, darken overlay, pause when off-screen |
| Parallax layers / depth | CSS `perspective` + `translateZ`, or `view()` timeline per layer; mouse parallax with `useMotionValue` + spring |
| Bento grid | CSS Grid `grid-template-areas`, hover spotlight using pointer-tracked `--x/--y` radial gradient, `backdrop-filter` glass cards |
| Animated beams / connectors | SVG paths with `stroke-dashoffset` + gradient (Magic UI Animated Beam) |
| Logo cloud / marquee | Duplicated track + CSS translate keyframes, `mask-image` fade edges, pause on hover |
| Aurora / spotlight / lamp | Blurred radial gradients with `@property` angle animation; Aceternity Lamp/Spotlight |
| Preloader / intro | Counter 0→100 with NumberFlow or GSAP, curtain wipe with `clip-path: inset()`, then hero timeline; skip if assets are light (preloaders cost LCP) |
| Scroll cue | Mouse/arrow bounce with `prefers-reduced-motion` guard; fade out on first scroll |

**Navigation & menus**

| Pattern | Build |
| --- | --- |
| Sticky header that hides on scroll down, blurs over content | `position: sticky` + `backdrop-filter` + direction class from `Observer`/`scroll-state(stuck)`; shrink padding and logo with a transition |
| Animated active indicator (tabs, nav) | Motion `layoutId` pill, or View Transitions `view-transition-name`, or CSS anchor positioning |
| Mega menu | Base UI/Radix `NavigationMenu` with cross-fading panels; hover-intent delay 100–150 ms; `AnimatePresence` for exit |
| Full-screen menu (burger → X) | `<dialog>`/popover + `@starting-style`; staggered links; burger lines morph via `transform` |
| Command palette ⌘K | cmdk; fuzzy search; recent items; keyboard hints; 150 ms scale/fade |
| macOS dock magnification | Motion `useMotionValue` on mouse x → spring-scaled widths (Magic UI/Motion Primitives Dock) |
| Magnetic buttons / links | GSAP `quickTo()` or Motion springs on pointer offset; reset on leave; disable on touch |
| Mobile bottom nav / bottom sheet | Fixed bottom bar with `env(safe-area-inset-bottom)`; Vaul drawer with snap points |
| Breadcrumbs, scrollspy, TOC | `IntersectionObserver` with `rootMargin` offset; `aria-current` |
| Curved/skewed menu panels | SVG path morph on open (Olivier Larose curved menu) |

**Lists, pagination & data**

| Pattern | Build |
| --- | --- |
| Infinite scroll with sentinel | `IntersectionObserver` + TanStack Query `useInfiniteQuery`; keep a "Load more" button for a11y and SEO |
| Virtualized long lists | TanStack Virtual / Virtuoso; fixed heights or measured rows |
| Classic pagination | Cursor-based API, `rel=prev/next`, URL state via nuqs, prefetch next page on hover/viewport |
| Skeleton → content | Skeleton that matches final layout; crossfade with `AnimatePresence`; show skeletons only if load > \~300 ms |
| Optimistic updates | React 19 `useOptimistic`, TanStack Query mutations with rollback |
| Reordering / drag-drop | dnd-kit, Pragmatic drag and drop (Atlassian), Motion `Reorder`, Swapy; AutoAnimate for list diffs |
| Filters with animated layout | Motion `layout` on items + `AnimatePresence` (`popLayout`), or View Transitions on DOM update |
| Tables | TanStack Table + sticky header, `tabular-nums`, row hover, column resize; virtualize over \~200 rows |
| Empty / error / zero states | Illustration (Lottie/SVG), one-line explanation, primary action; never a bare "No results" |

**Cards, images & media**

| Pattern | Build |
| --- | --- |
| Hover lift + shadow | `translateY(-2px)` + layered shadow transition 150–200 ms `ease-out` |
| 3D tilt | `react-parallax-tilt`, `vanilla-tilt`, or `rotateX/Y` from pointer with spring; `transform-style: preserve-3d` |
| Spotlight / border glow | Pointer-tracked radial gradient in a pseudo-element, masked border (Aceternity/Magic UI) |
| Image reveal on scroll | `clip-path: inset()` or scale 1.15→1 inside overflow-hidden, `view()` timeline |
| Image hover distortion / ripple | WebGL displacement (Codrops hover-effect, OGL, curtains) |
| Expand card → detail (shared element) | View Transitions or Motion `layoutId` morph; GSAP Flip for vanilla |
| Before/after comparison | `<input type=range>` + `clip-path`; `img-comparison-slider` web component |
| Gallery / lightbox | PhotoSwipe, yet-another-react-lightbox; `<dialog>` + View Transition |
| Glassmorphism / Liquid Glass | `backdrop-filter: blur(20px) saturate(180%)` + 1 px light border + inner highlight; refraction via SVG `feDisplacementMap` (CPU-heavy, use sparingly) |
| Flip card | `rotateY(180deg)` with `backface-visibility: hidden` |

**Overlays, forms & feedback**

| Pattern | Build |
| --- | --- |
| Modal | `<dialog>` + `@starting-style`, scale 0.96→1 + fade, 200 ms enter / 150 ms exit; focus trap and restore built in; Base UI Dialog |
| Drawer / bottom sheet | Vaul (snap points, drag to close, background scale) |
| Toasts | Sonner (stacked, swipe, promise states, `aria-live`) |
| Tooltips / popovers | Base UI/Radix with `delayDuration`, `@starting-style` fade + 4 px slide; or `popover` + anchor positioning |
| Inline validation | Validate on blur, re-validate on input after first error, shake 300 ms for hard errors, success check mark animates in |
| Floating labels, OTP, masks | CSS `:placeholder-shown`/`:has(:focus)`, input-otp, maskito |
| Multi-step forms | Progress bar with `layout` transitions, directional slide, persist state in URL/localStorage |
| Buttons | Press scale 0.97, 100 ms; loading spinner replaces label without changing width; success morphs into check |
| Toggles / checkboxes | Spring thumb (`linear()` easing), SVG check path draw |
| Pricing toggle (monthly/yearly) | `layoutId` pill + NumberFlow prices + "save 20%" badge |
| FAQ accordion | `<details name>` + `interpolate-size` or grid `0fr→1fr`; chevron rotate; `::details-content` |
| Cookie/consent, banners | Slide from bottom with `@starting-style`; never block LCP |
| Copy / share / confetti | Clipboard API + "Copied" morph; canvas-confetti for celebrations; haptics on supported devices |

**Cursor, background & ambient**

- Custom cursor: `cursor: none` + follower with `quickTo`/spring lerp; text-size/invert mode on hover of links; mask-reveal cursor (Olivier Larose); disable on touch and reduced-motion.
- Grain/noise overlay: SVG `feTurbulence` as a fixed pseudo-element at 4–8% opacity (or a tiled PNG for perf).
- Dot/grid backgrounds with radial fade: `background-image` radial dots + `mask-image`.
- Ambient blobs: blurred gradients drifting with 20–40 s keyframes; `will-change: transform` on 2–3 elements max.
- Theme switch: `light-dark()` tokens + View Transition circular reveal from the toggle position.

**Footer**: big type or marquee, sticky-reveal footer (`position: sticky; bottom: 0` under content with higher z-index), live clock/local time, link hover underlines, back-to-top with smooth scroll.

## 11. Page transitions, routing & app frameworks

Page transitions are now a platform feature: cross-document View Transitions plus Speculation Rules give multi-page sites app-like navigation with no router, and every major framework exposes same-document View Transitions. Barba/Swup-style libraries remain for GSAP-choreographed agency sites.

**Transition approaches**

| Approach | How | Use when | Status |
| --- | --- | --- | --- |
| Cross-document View Transitions | `@view-transition { navigation: auto }` on both pages + `view-transition-name` on shared elements; prerender next page with Speculation Rules | Astro, Eleventy, Rails, WordPress, any MPA | Standard (Chrome/Safari; Firefox pending) |
| Same-document View Transitions in frameworks | Astro `ClientRouter` (`transition:name`, `transition:animate`), Next.js `experimental.viewTransition` + React `<ViewTransition>`, Nuxt `experimental.viewTransition`, SvelteKit `onNavigate` + `startViewTransition`, React Router/TanStack `viewTransition` option, Angular `withViewTransitions()` | SPA routing with shared-element morphs | Standard |
| Motion `AnimatePresence` + `layoutId` | Mount/unmount choreography and shared layouts in React/Vue | Component-level and tab transitions | Standard |
| [Barba.js](https://barba.js.org), [Swup](https://swup.js.org), [Taxi.js](https://taxi.js.org) | Intercept links, fetch next page, run GSAP in/out hooks | Agency/portfolio sites with custom wipes, curtains, image morphs | Standard (creative sites) |
| Highway.js, Turbolinks-era hacks | Superseded | — | Legacy |
| Navigation API | Native SPA navigation interception, scroll restoration, transition hooks | Vanilla or custom routers | Rising |

**Transition recipes**: crossfade (default), slide by route depth using transition `types`, shared image/card morph via `view-transition-name`, curtain/wipe with `clip-path`, circular reveal from click point (`::view-transition-new(root)` + `clip-path: circle()`), persistent header/player via `view-transition-name: header`. Keep exits 150–250 ms and enters 250–400 ms; respect reduced motion by setting `::view-transition-group(*) { animation: none }`.

**Frameworks (Nov 2026)**

| Framework | Current | Motion-relevant features |
| --- | --- | --- |
| [Next.js](https://nextjs.org) 16.4 (Oct 2026) + React 19.3 | Turbopack default, Cache Components (default in 17), PPR, `loading.js` streaming, `useOptimistic`, `<ViewTransition>` experimental, React Compiler stable | Best for product apps; heaviest baseline bundle |
| [React Router](https://reactrouter.com) v7, [TanStack Start](https://tanstack.com/start) 1.0, [TanStack Router](https://tanstack.com/router) | Loaders/actions, type-safe routes, Vite Environment API, `viewTransition` on links | Lighter React full-stack without RSC complexity |
| [Astro](https://astro.build) 6 (2026) | Islands, Server Islands, Content Layer, built-in View Transitions, Vite Environment API; team joined Cloudflare | Default for content and marketing sites |
| [SvelteKit](https://svelte.dev) 3 / Svelte 5 runes | Built-in transitions, `onNavigate`, smallest bundles | Best DX for motion-heavy sites |
| [Nuxt](https://nuxt.com) 4.6 (Oct 2026), Nuxt 5 upcoming (Nitro v3) / Vue 3.6 Vapor | `<NuxtPage>` transitions, View Transitions, Nuxt UI | Vue teams |
| SolidStart (Solid 2), Qwik 2 (resumability), Angular 21 (signals, zoneless) | Fine-grained reactivity keeps interactions under 200 ms INP | Niche but strong perf |
| HTMX 2, Alpine.js, Hotwire Turbo 8 | Server-rendered apps with CSS/View Transitions; `hx-swap` transitions | Rails/Laravel/Django/Phoenix stacks |
| Eleventy 3, Hugo | Static output + cross-document View Transitions | Blogs, docs |
| Build tools | Vite 8 (Rolldown), Turbopack, Rspack, esbuild, Bun; Parcel for zero-config | Fast HMR keeps motion tuning loops short |
| Hosting / edge | Vercel, Netlify, Cloudflare Workers/Pages, Fly.io, Railway, Coolify | Edge rendering + CDN cuts TTFB for transitions |
| Content | Sanity, Payload (Figma-owned), Contentful, Storyblok, Keystatic, MDX | Structured content feeding sections in §10 |
| Site builders | Framer (ships Motion), Webflow (ships GSAP), Figma Sites/Make, Wix Studio | No-code premium motion with GSAP/Motion underneath |

Routing hygiene for feel: prefetch on hover/viewport (`<Link prefetch>`, Speculation Rules), restore scroll on back, show a top progress bar for navigations over \~300 ms, keep layout shells persistent (header, player, sidebar) across routes, and avoid full-page spinners.

## 12. Performance

The three Core Web Vitals are still LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1 at the 75th percentile of real users; INP is the one most sites fail (about 43% in early 2026). Some SEO blogs claim Google tightened thresholds in March 2026 (INP 150 ms, LCP 2.0 s); treat that as unverified and check [web.dev/vitals](https://web.dev/vitals) before quoting numbers.

**Budgets that premium teams actually hold**

| Metric | Target | Notes |
| --- | --- | --- |
| LCP | ≤ 2.5 s (aim 1.5 s) | Hero image/text; `fetchpriority="high"`, no lazy-load on LCP element, preload hero font |
| INP | ≤ 200 ms (aim 100 ms) | Every click/tap/keypress; break long tasks with `scheduler.yield()`, avoid heavy handlers |
| CLS | ≤ 0.1 (aim 0) | Reserve space (`aspect-ratio`, `min-height`), `font-display: optional` or metric-matched fallbacks, `scrollbar-gutter: stable` |
| TTFB / FCP | ≤ 0.8 s / ≤ 1.8 s | Edge rendering, caching, 103 Early Hints |
| Frame budget | 16.7 ms @60 Hz, 8.3 ms @120 Hz | Long Animation Frames (> 50 ms) are the INP culprits |
| JS shipped (mobile) | ≤ 300 KB compressed initial, motion libs lazy | Measure with bundle analyzers; RSC/islands cut this fastest |
| Hero media | image ≤ 200 KB AVIF, video ≤ 2 MB, 3D ≤ 3 MB | Poster first, then enhance |

**Rendering pipeline rules (the ones that make motion smooth)**

- Animate only `transform`, `opacity`, and where needed `clip-path`/`filter`; never `top/left/width/height/margin/box-shadow`. Fake shadow motion by fading a pseudo-element.
- Batch DOM reads before writes; forced synchronous layout (reading `offsetWidth` after a style write) is the classic jank source.
- `will-change` on 2–5 elements right before they animate, removed after; too many layers exhaust mobile GPU memory.
- `backdrop-filter` and large `filter: blur()` are expensive; limit area and count, especially on iOS.
- `content-visibility: auto` + `contain-intrinsic-size` on long pages; `contain: layout paint` on independent widgets.
- Prefer CSS/WAAPI/scroll-driven animations (compositor thread) over JS-per-frame; GSAP/Motion are fine when they only touch transforms.
- Pause everything off-screen (`IntersectionObserver`, `document.visibilityState`), including Lottie, Rive, canvas and marquees.
- Workers for heavy compute (`OffscreenCanvas`, Comlink, WASM); Partytown for third-party scripts.
- Test on a mid-range Android with 4× CPU throttling and on a 120 Hz iPhone; both expose different jank.

**Loading & network**

| Area | Techniques |
| --- | --- |
| Images | AVIF default (WebP fallback; JPEG XL now in Chrome 155/Firefox 158/Safari), `srcset`/`sizes`, `<picture>` art direction, `loading="lazy"` below the fold, `decoding="async"`, width/height set, LQIP/BlurHash/ThumbHash placeholders; `next/image`, Astro `<Image>`, Nuxt Image, Cloudinary/imgix/Cloudflare Images/Bunny, Sharp/Squoosh |
| Video | `preload="metadata"`, poster, AV1/HEVC, adaptive HLS via Mux/Cloudflare Stream/Bunny for anything over 10 s |
| Fonts | See §9: self-host, preload, subset, variable, `size-adjust` fallbacks |
| JavaScript | Route-level code splitting, `import()` motion libs after idle/first interaction, `LazyMotion`, Anime.js modular imports, islands/partial hydration (`client:visible`, `client:idle`), React Server Components, React Compiler, avoid barrel imports, `modulepreload`, `useTransition`/`useDeferredValue` for heavy state |
| Network | HTTP/3, Brotli/Zstd, immutable hashed assets with long cache, `preconnect` to critical origins, Speculation Rules `prerender` for likely next pages, bfcache-safe pages (no `unload`), streaming SSR / PPR, Server-Timing headers, no redirect chains |
| Third parties | Load after consent/idle, self-host where licenses allow, `requestIdleCallback`, facade pattern for embeds (YouTube lite, chat widgets) |
| Adaptive loading | `prefers-reduced-data`, `Save-Data`, `navigator.connection.effectiveType`, `navigator.hardwareConcurrency`, `deviceMemory`: serve lighter media/3D to constrained devices |

**Measurement & monitoring**

| Tool | Use |
| --- | --- |
| Chrome DevTools Performance panel (with field data overlay), Rendering → paint flashing/layer borders, Layers, Animations panel | Find long tasks, layout thrash, layer explosions |
| Lighthouse, PageSpeed Insights, [webstatus.dev](https://webstatus.dev) | Lab audits + CrUX field data |
| CrUX dashboard/API, Search Console CWV report | Real-user pass rates by origin |
| WebPageTest | Filmstrips, waterfalls, connection emulation |
| [`web-vitals`](https://github.com/GoogleChrome/web-vitals) attribution build + RUM (Vercel Speed Insights, Cloudflare Web Analytics with LCP/INP sub-parts since Oct 2026, SpeedCurve, Calibre, DebugBear, RUMvision, Sentry, Datadog) | Production monitoring and INP attribution via Long Animation Frames API |
| Lighthouse CI, Unlighthouse, `size-limit`/bundlesize, bundle analyzers | Regression budgets in CI |
| React Profiler, react-scan, Svelte/Vue devtools, `r3f-perf`, Spector.js | Framework- and GPU-level profiling |

**Perceived performance**: respond to input within 100 ms (press states, optimistic UI), show skeletons only after \~300 ms, progress for anything over 1 s, prefetch on hover/viewport, stale-while-revalidate data, keep shells persistent during navigation, and never let an animation exceed the latency it is masking.

## 13. Accessibility & inclusive motion

WCAG 2.2 AA is the standard to build to; WCAG 3.0 is still a Working Draft (updated March and September 2026, final not expected before 2028). The European Accessibility Act has applied since 28 June 2025; the US DOJ extended ADA Title II deadlines by a year on 20 April 2026 (large public entities now 26 April 2027). Premium motion that fails these is a liability, not a feature.

**Standards & law**

| Item | What to know |
| --- | --- |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) AA | Baseline for procurement; adds focus-not-obscured, target size 24×24 px, dragging alternatives, consistent help, accessible authentication |
| WCAG 3.0 (draft) | Outcome-based scoring replaces pass/fail; watch, don't build to it yet |
| EAA (EU, since 2025-06-28), EN 301 549 | Applies to e-commerce, banking, transport, e-books, apps sold in the EU |
| ADA Title II (US public sector) | WCAG 2.1 AA; deadlines moved to Apr 2027 (≥ 50k population) and 2028 (smaller) |
| ADA Title III (US private) | Court-enforced; web suits keep rising, so treat WCAG 2.2 AA as the bar |
| [ARIA Authoring Practices (APG)](https://www.w3.org/WAI/ARIA/apg/) | Keyboard and role patterns for every widget; first rule of ARIA: use native HTML first |

**Motion-specific requirements**

- Honor `prefers-reduced-motion: reduce`: remove parallax, auto-scroll, large movement and looping; keep opacity fades and short (≤ 150 ms) transforms. Motion `useReducedMotion()`, GSAP `gsap.matchMedia()`, Svelte `prefersReducedMotion`, a global `@media` block for CSS.
- WCAG 2.3.3 (animation from interactions can be disabled), 2.2.2 (pause/stop/hide anything moving over 5 s: marquees, carousels, video), 2.3.1 (no more than 3 flashes per second).
- Autoplaying carousels must have visible pause and keyboard focus that doesn't rotate away.
- Transitions must not hide or trap focus: manage focus on open/close (`<dialog>` does it), restore focus to the trigger, never animate the focused element off-screen.
- Provide a motion toggle in settings for app-like products; persist it.
- Vestibular safety: avoid full-viewport zoom, spin and parallax; keep scroll-jacking off or reversible.

**Core checklist for any premium UI**

- Semantic HTML first (`<button>`, `<nav>`, `<dialog>`, `<details>`, headings in order), ARIA only to fill gaps, landmarks, skip link.
- Keyboard: every interactive element reachable and operable, visible `:focus-visible` ring (2 px, 3:1 contrast), logical order, `inert` on background during modals, Escape closes overlays, arrow-key patterns per APG.
- Contrast: 4.5:1 text, 3:1 large text/UI; use APCA (Lc 60+ body) as the forward-looking check; test light, dark and `forced-colors`.
- Target size ≥ 24 px (44 px on touch), spacing between targets, `touch-action: manipulation`.
- Text: resizable to 200%, no `maximum-scale`, spacing overrides survive, `lang` set.
- Media: captions, transcripts, audio description; no autoplay with sound.
- Forms: labels, error identification, `aria-describedby` hints, no CAPTCHA-only auth.
- Live regions (`aria-live="polite"`) for toasts, counters and streaming text; `role="status"` for loaders.
- Reduced transparency / contrast preferences: solid fallbacks for glass UI.
- Screen readers to test with: VoiceOver (macOS/iOS), NVDA + Firefox, JAWS + Chrome, TalkBack.

**Tooling**

| Tool | Use |
| --- | --- |
| axe DevTools / `axe-core`, Lighthouse a11y, Accessibility Insights, WAVE | Automated audits (catch \~30–40% of issues) |
| `eslint-plugin-jsx-a11y`, `vue-a11y`, Svelte compiler a11y warnings | Lint at write time |
| Storybook a11y addon, Playwright + `@axe-core/playwright`, Pa11y CI | Component and CI testing |
| Polypane, Chrome DevTools Rendering → emulate vision deficiencies / reduced motion / forced colors | Manual checks |
| Stark, Figma contrast/A11y plugins, Able | Design-time contrast and annotations |
| [Inclusive Components](https://inclusive-components.design), [a11y-style-guide](https://a11y-style-guide.com), Deque University, WebAIM | Patterns and learning |

## 14. Mobile apps

On mobile, premium feel comes from running animation on the UI thread (Reanimated worklets, SwiftUI, Compose), physics springs that follow the finger, and native platform idioms: Apple's Liquid Glass (iOS 26, 2025) and Google's Material 3 Expressive (2025). Cross-platform in 2026 means React Native 0.84 + Expo SDK 55+ (New Architecture only) or Flutter with Impeller.

**React Native / Expo**

| Tool | Role | Status |
| --- | --- | --- |
| [Expo SDK 55+](https://expo.dev) (RN 0.83–0.84, React 19.2) | New Architecture only, Hermes V1, Expo Router with native tabs, Apple Zoom transitions, `Stack.Toolbar`, Material 3 Colors API, Expo UI (beta: SwiftUI/Compose from JS), `expo-glass-effect` for Liquid Glass, brownfield packages | Standard |
| [Reanimated 4](https://docs.swmansion.com/react-native-reanimated/) | Worklets on the UI thread, `withSpring`/`withTiming`/`withDecay`, layout animations (`entering`/`exiting`/`layout`), shared element transitions, plus CSS-style `animation`/`transition` props | Standard |
| [Gesture Handler 2](https://docs.swmansion.com/react-native-gesture-handler/) | Pan, pinch, fling, long-press composed with Reanimated | Standard |
| [React Native Skia](https://shopify.github.io/react-native-skia/) | GPU drawing, SkSL shaders, blur/glow, charts, image filters | Standard (custom visuals) |
| Moti | Motion-like declarative API over Reanimated | Niche |
| [Rive](https://rive.app) RN, lottie-react-native | Designer animations and interactive icons | Standard |
| `@gorhom/bottom-sheet`, `react-native-screens`, FlashList v2 / Legend List, `expo-image`, `react-native-mmkv`, `react-native-haptic-feedback`/`expo-haptics` | Sheets, native stacks, 60 fps lists, fast images, storage, haptics | Standard |
| UI kits: gluestack-ui v4 (shadcn-style, Reanimated), Tamagui, NativeWind v4 (Tailwind), React Native Paper (M3), Unistyles, HeroUI Native | Styling and component systems | Standard |
| Skia-based charts (Victory Native XL), `react-native-reanimated-carousel`, `react-native-draggable-flatlist` | Charts, carousels, reorder | Standard |

**Flutter**: Impeller renderer default, implicit animations (`AnimatedContainer`, `AnimatedSwitcher`), `Hero` shared elements, `flutter_animate`, Rive and Lottie packages, custom `Curves` and spring simulations, `CustomPainter` + fragment shaders (`FragmentProgram`), Material 3 Expressive widgets and Cupertino Liquid Glass styling as they land.

**SwiftUI (iOS 26, Liquid Glass)**: `.glassEffect()`, `GlassEffectContainer`, morphing glass with `glassEffectID`, `.spring()` and `.bouncy`/`.snappy`/`.smooth` presets, `matchedGeometryEffect` and `matchedTransitionSource` zoom transitions, `PhaseAnimator`, `KeyframeAnimator`, `.sensoryFeedback()` haptics, SF Symbols 7 animated effects (`.symbolEffect`), `ScrollView` `scrollTransition` and `visualEffect`, `TipKit`, Metal shaders via `.layerEffect`/`.distortionEffect`, `.contentTransition(.numericText())`.

**Jetpack Compose (Material 3 Expressive)**: `MaterialExpressiveTheme`, motion schemes (`MotionScheme.expressive()`), spring-based `animateFloatAsState`/`Animatable`, `AnimatedVisibility`, `animateContentSize`, `AnimatedContent`, shared element transitions (`SharedTransitionLayout`), `Modifier.graphicsLayer`, `AGSL` shaders, predictive back, loading indicators with shape morphing, `MotionLayout` (legacy), Lottie Compose, Rive Android.

**Platform guidelines to read**: [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) (Liquid Glass, motion, haptics), [Material 3 Expressive](https://m3.material.io) (motion physics, shape morph, color roles), Fluent 2 (Windows), plus WWDC 2018 "Designing Fluid Interfaces" and WWDC 2025 Liquid Glass sessions.

**Cross-cutting rules**

- Touch targets ≥ 44×44 pt (iOS) / 48×48 dp (Android); thumb-zone navigation (bottom tabs, bottom sheets, FABs).
- Gestures must be interruptible and velocity-aware (springs with initial velocity), with rubber-banding at edges and haptics on snap points.
- 120 Hz displays expose jank: keep animation on the UI thread, avoid JS-thread `setState` per frame, batch layout.
- Respect system settings: Reduce Motion (iOS `UIAccessibility.isReduceMotionEnabled`, RN `AccessibilityInfo.isReduceMotionEnabled`), Dynamic Type, dark mode, RTL.
- Skeletons and optimistic UI matter more on mobile networks; cache images (`expo-image`), prefetch next screens.
- App-store feel: launch screen that matches first frame, no blank flash, predictive back on Android, safe areas and keyboard avoidance.

**Web on mobile / PWA**: `viewport-fit=cover`, `env(safe-area-inset-*)`, `100dvh`, `interactive-widget=resizes-content`, `touch-action`, `overscroll-behavior`, `-webkit-tap-highlight-color: transparent`, Vibration API (Android), `<install>` element / `navigator.install()` (Chrome 158 beta), Web App Manifest, service worker offline, Capacitor or Tauri 2 for store packaging.

## 15. Design systems, tokens, theming & color

Premium UIs are token-driven: color in OKLCH, a 4/8 px spacing scale, nested radii, layered shadows and named motion tokens, authored once (DTCG JSON or Figma Variables) and compiled to CSS variables. The W3C Design Tokens (DTCG) format reached a stable release in late 2025 and Style Dictionary v4, Tokens Studio, Penpot and Figma all speak it.

**Token pipeline**

| Layer | Tools |
| --- | --- |
| Author | Figma Variables (modes for light/dark/density), Tokens Studio plugin, Penpot (native DTCG tokens), Supernova |
| Format | [DTCG](https://www.designtokens.org) JSON (`$value`, `$type`, aliases) |
| Build | [Style Dictionary](https://styledictionary.com) v4, Theo, Cobalt; output CSS vars, Tailwind `@theme`, Swift/Kotlin, Panda tokens |
| Document | Storybook 9 (+ a11y, interactions, visual tests), Chromatic, Ladle, Histoire, zeroheight, Supernova |
| Design ↔ code | Figma Dev Mode, Code Connect, Figma MCP server, Figma Make/Sites, v0, Builder.io, Anima, Onlook, Subframe, Paper |

**Color**

- Work in OKLCH (perceptually uniform lightness); pickers: [oklch.com](https://oklch.com), Atmos, Huetone, Leonardo (Adobe, contrast-driven), Material Theme Builder (HCT), Realtime Colors for previews.
- Palettes with 10–12 steps per hue: [Radix Colors](https://www.radix-ui.com/colors) (12 steps with semantic roles: backgrounds 1–2, interactive 3–5, borders 6–8, solid 9–10, text 11–12), Tailwind v4 palette (OKLCH), Open Props.
- Semantic roles over raw hues: `--bg`, `--bg-elevated`, `--fg`, `--fg-muted`, `--border`, `--accent`, `--accent-fg`, `--success/warning/danger` each with `-bg/-fg/-border`.
- Derive states with `color-mix(in oklab, var(--accent) 90%, black)` and relative color syntax instead of hand-picked hexes.
- Contrast: WCAG 4.5:1 for compliance, APCA (Lc 60+ body, 75+ small) for perceptual accuracy; `contrast-color()` where supported.
- Dark mode done right: near-black surfaces (`oklch(15% …)` not pure black), lighter surface = higher elevation, desaturate accents slightly, borders as `color-mix(currentColor 12%)`, swap shadows for borders/glows, test `prefers-contrast` and `forced-colors`. Implement with `color-scheme` + `light-dark()` or `[data-theme]`, `next-themes` for persistence, View Transition for the switch.

**Shape, space, depth**

- Spacing scale 4, 8, 12, 16, 24, 32, 48, 64, 96 px; fluid section padding via `clamp()`.
- Radius: tokens 4/8/12/16/24/full; nested radius rule `inner = outer − padding`; `corner-shape: superellipse(…)` for Apple-style squircles where supported.
- Shadows: 2–3 layered soft shadows plus a 1 px border (Josh Comeau's shadow palette approach); tint shadows with the background hue; elevation tokens `--shadow-1..5`.
- Surfaces: glass = `backdrop-filter` + 1 px inner highlight + subtle noise; cards = border + very soft shadow in light mode, lighter surface in dark mode.
- Borders: 1 px `color-mix` alpha borders scale across themes better than fixed grays.
- Z-index scale as tokens (`--z-dropdown: 100`, `--z-modal: 300`, …) and `@layer` ordering.

**Motion tokens**

| Token | Typical values |
| --- | --- |
| `--duration-instant/fast/base/slow/slower` | 50 / 150 / 250 / 400 / 600 ms |
| `--ease-out` (enter) | `cubic-bezier(0.22, 1, 0.36, 1)` |
| `--ease-in` (exit) | `cubic-bezier(0.55, 0, 1, 0.45)` |
| `--ease-in-out` (move) | `cubic-bezier(0.65, 0, 0.35, 1)` |
| `--ease-spring` | `linear(…)` generated from a spring (see §16) |
| Platform references | Material 3: duration short1–extraLong4 (50–1000 ms), emphasized/standard easings; Apple: spring presets (`smooth`, `snappy`, `bouncy`); Carbon: productive vs expressive; Atlassian, Spectrum, Fluent motion tokens |

**Systems worth studying**: Vercel Geist, Linear, Raycast, Stripe, Shopify Polaris, GitHub Primer, Atlassian DS, Adobe Spectrum 2, IBM Carbon 11, Microsoft Fluent 2, Material 3 Expressive, Apple HIG, Uber Base, Pinterest Gestalt, GOV.UK/USWDS (accessibility), Untitled UI (Figma kit), Porsche DS, Wise.

**Visual directions in 2026**: dark "Linear/Vercel" SaaS with glow accents; editorial Swiss typography with big type and whitespace; Liquid-Glass-inspired translucency; bento layouts; dithering/pixel/ASCII textures; 3D product renders; neo-brutalism for indie brands; monochrome plus one accent; grain and mesh gradients. Pick one direction per product and encode it in tokens, not per-page overrides.

## 16. Motion design principles & the numbers

Good UI motion responds within 100 ms, lasts 150–400 ms, eases out on entry, exits faster than it enters, and can be interrupted at any frame. Springs replace fixed curves wherever a gesture or interruption is possible. Everything below is the working consensus of Apple's fluid-interface guidance, Material 3, and the design-engineering school (Emil Kowalski, Rauno Freiberg, Josh Comeau).

**Durations by element**

| Element | Enter | Exit | Notes |
| --- | --- | --- | --- |
| Hover / color / press | 100–150 ms | same | `ease`; press scale 0.97 at 100 ms |
| Tooltip, toggle, checkbox | 150 ms | 100 ms | translate 4–6 px + fade |
| Dropdown, popover, menu | 150–200 ms | 100–150 ms | scale from 0.95 at the anchor's `transform-origin` |
| Modal, drawer, sheet | 200–300 ms | 150–200 ms | scale 0.96 → 1 or slide; backdrop fades at same time |
| List add/remove/reorder | 200–300 ms | 150 ms | stagger 20–40 ms, cap total ≈ 300 ms |
| Page / route transition | 250–400 ms | 150–250 ms | crossfade or shared-element morph |
| Scroll reveal | 500–800 ms | — | translate 24–40 px, `ease-out`, trigger 10–20% in view |
| Hero intro choreography | 800–1200 ms total | — | the one place long timelines are acceptable |
| Number counters | 600–1000 ms | — | `ease-out`, tabular figures |
| Marquee / ambient loops | 20–60 s | — | linear, pause on hover and off-screen |

**Easing by intent**

| Intent | Curve | Why |
| --- | --- | --- |
| Element enters | `ease-out` (`cubic-bezier(0.22, 1, 0.36, 1)`, quart/quint) | Fast start reads as responsive |
| Element exits | `ease-in` only if quick (≤ 150 ms); many teams use a fast `ease-out` fade | Avoid sluggish starts |
| Element moves on screen | `ease-in-out` (`cubic-bezier(0.65, 0, 0.35, 1)`) | Visible at both ends |
| Color / opacity | `ease` or `linear` for very short | Perceptually flat |
| Progress, marquee, scrub | `linear` | Constant rate is the point |
| Gesture-driven, interruptible | Spring | Carries velocity, never "finishes then restarts" |
| Drawer feel (Vaul) | `cubic-bezier(0.32, 0.72, 0, 1)` | Signature snappy settle |
| Never for UI | `ease-in` on long moves, `linear` on movement, `elastic`/`bounce` on large surfaces | Feels broken or cartoonish |

**Springs**: define by perceptual duration + bounce (Apple `.spring(duration:bounce:)`, Motion `type: "spring", visualDuration: 0.3, bounce: 0.2`) rather than raw stiffness/damping; use `bounce: 0` for layout and large surfaces, 0.1–0.3 for small playful elements; carry gesture velocity into the release spring; bake springs into CSS with `linear()` via [linear-easing-generator](https://linear-easing-generator.netlify.app) or [easing.dev](https://easing.dev).

**Choreography rules**

- Transform origin from the trigger: popovers scale from their anchor side, dialogs from center, FAB sheets from the button.
- Container first, content second: the surface moves, then children fade/stagger in (Material "container transform").
- Shared axis: things that are related move along one axis; unrelated things crossfade.
- Exits are simpler than entrances (fade + slight scale; optional `filter: blur(4px)`); users don't watch exits.
- Stagger from the user's attention point (first item, hovered card, click position), 20–50 ms apart, never per-item on long lists.
- Scale from 0.95–0.97, not 0; translate 4–8 px for tooltips, 16–40 px for cards; blur 2–4 px max and only on small elements.
- Scale containers, not text (text under `transform: scale` blurs); animate `grid-template-rows` or `interpolate-size` instead of `height`.
- Keyboard-triggered actions get faster/simpler motion than pointer-triggered ones; repeated actions (toggles used 100× a day) get near-zero motion.
- Direct manipulation: content follows the finger 1:1, rubber-bands at edges (≈ 0.3× past the limit), snaps with velocity thresholds, haptic tick on snap.
- Motion must never delay input; if a state change is instant, show it instantly and animate the consequence.

**Principles to internalize**: Apple WWDC18 "Designing Fluid Interfaces" (instant response, continuous feedback, interruptible, redirectable, natural mapping); WWDC23 "Animate with springs"; Material 3 motion (informative, focused, expressive; physics-based 2025 update); the 12 principles of UX in motion (Willenskomer); Disney's 12 applied sparingly (anticipation, follow-through, secondary action, arcs); micro-interaction anatomy (trigger → rules → feedback → loops/modes, Saffer).

**Easing & tuning tools**

| Tool | Use |
| --- | --- |
| [easings.net](https://easings.net), [easing.dev](https://easing.dev), [cubic-bezier.com](https://cubic-bezier.com) | Browse and tune curves |
| GSAP Ease Visualizer, Anime.js easing editor, Motion Studio (VS Code, Motion+) | Library-specific curves and springs |
| Josh Comeau's spring playground, react-spring visualizer | Feel stiffness/damping/mass |
| Figma Smart Animate (spring presets), Jitter, Principle, ProtoPie, Rive | Prototype motion before code |
| Chrome DevTools Animations panel, `document.getAnimations()` | Scrub and slow down live animations (set playback 10% to inspect) |

**Learn from**: [Animations on the Web](https://animations.dev) (Emil Kowalski), Whimsical Animations (Josh Comeau), [Rauno's craft](https://rauno.me/craft) and "Invisible Details of Interaction Design", Val Head's "Designing Interface Animation", Rachel Nabors' "Animation at Work", Sarah Drasner's "SVG Animations", Apple HIG Motion, Material 3 motion guidelines, Awwwards Academy, Codrops.

## 17. UX laws, heuristics & conversion patterns

Motion and polish only pay off on top of sound UX: clear hierarchy, fast feedback, obvious next action, and forgiving errors. These are the rules that decide whether a premium-looking page also converts.

**Laws & heuristics (lawsofux.com, NN/g)**

| Law | Design consequence |
| --- | --- |
| Fitts's law | Big, close targets; sticky CTAs; edge/corner menus; 44 px touch targets |
| Hick's law | Fewer choices per screen; progressive disclosure; one primary CTA per section |
| Jakob's law | Follow platform conventions (cart top-right, logo home, hamburger on mobile); novelty only where it adds delight |
| Doherty threshold | Keep system response under 400 ms; mask latency with optimistic UI and skeletons |
| Miller's law / chunking | Group into 5–7 items; chunk forms into steps; chunk numbers |
| Aesthetic-usability effect | Polish buys forgiveness, but not for broken flows |
| Peak-end rule | Invest in the moment of success (confetti, summary, next step) and the exit |
| Zeigarnik / goal-gradient | Progress indicators, "2 of 3 steps", partially filled profiles |
| Von Restorff | One element visually distinct = the CTA |
| Tesler's law | Complexity goes somewhere; absorb it in defaults and smart inputs |
| Postel's law | Accept messy input (paste, formats), be strict in output |
| Gestalt (proximity, similarity, common region, continuity) | Spacing and containers over lines and boxes |
| Nielsen's 10 heuristics | Visibility of status, match real world, user control (undo), consistency, error prevention, recognition over recall, flexibility, minimalist design, error recovery, help |

**Response-time rules**: < 100 ms feels instant (press states, hover); < 1 s keeps flow (no spinner, maybe a subtle progress); > 1 s needs a progress indicator; > 10 s loses attention (notify when done). RAIL model: Response 100 ms, Animation 16 ms, Idle 50 ms chunks, Load 1 s.

**Landing-page anatomy that converts**

- Above the fold: one clear value proposition (what, for whom, outcome), one primary CTA, a secondary low-commitment CTA, social proof strip (logos, rating, user count), and a product visual that shows the real thing.
- Then: problem → solution → how it works (3 steps) → features as benefits (bento/alternating) → proof (testimonials with faces, case numbers) → pricing (toggle, highlighted plan, FAQ) → final CTA → footer.
- Copy: specific over clever, numbers over adjectives, verbs on buttons ("Start free trial" not "Submit"), microcopy next to risk ("No card required").
- Reading patterns: F-pattern for text-heavy, Z-pattern for sparse; 5-second test for the hero.
- Trust signals: security badges near forms, transparent pricing, real photos, live chat, privacy note under inputs.
- Research: Baymard Institute (e-commerce UX), NN/g, CXL, GoodUI patterns, Julian Shapiro's landing-page handbook, "Refactoring UI" (Wathan/Schoger), "Practical UI" (Dannaway).

**App-side patterns**

| Pattern | Do |
| --- | --- |
| Onboarding | Show value in the first session; progressive profiling; checklists; product tours only when contextual (Driver.js, Shepherd, React Joyride, Intro.js; Appcues/Userpilot/Pendo for SaaS) |
| Empty states | Explain + illustrate + single action; sample data or templates |
| Loading states | Skeletons matching layout, optimistic updates, streaming content; no layout shift when data lands |
| Error states | Human message, cause, fix, retry; inline validation; never lose typed data; undo instead of confirm dialogs |
| Success states | Confirmation with next action; subtle celebration for milestones |
| Destructive actions | Confirm only for irreversible/high-cost; type-to-confirm for catastrophic; undo toast (Sonner) for the rest |
| Notifications | Right channel for the urgency; batch; let users control |
| Search | Instant results, recent/suggested, keyboard-first (⌘K), typo tolerance |
| Settings | Save automatically with a saved indicator, or explicit save with dirty-state warning |
| Dark patterns to avoid | Confirmshaming, hidden costs, roach-motel cancellation, fake urgency; EU DSA and FTC treat these as violations |

**Research & testing**: 5-user usability tests per round, first-click tests, tree tests (Maze, UserTesting, Lyssna), session replay and heatmaps (Microsoft Clarity free, Hotjar, PostHog, FullStory), funnels and A/B tests (PostHog, Statsig, GrowthBook, Optimizely, VWO), surveys (NPS/CSAT in-app), analytics (PostHog, Plausible, Fathom, Amplitude, Mixpanel, GA4). Ship, measure, then decide which motion stays.

## 18. Rich content: charts, tables, editors, drag & drop, canvas, media, maps, forms

These are the heavyweight components where "premium" means smooth at scale: animated chart transitions, 60 fps drag, virtualized tables, and editors that feel native. Pick the headless or canvas-based option when data is large.

| Category | Current best | Alternatives / notes |
| --- | --- | --- |
| Charts (React) | [Recharts](https://recharts.org) 3 (what shadcn charts wrap), [Visx](https://airbnb.io/visx) (D3 primitives), Nivo (animated, themed) | Chart.js 4 (canvas, any framework), Apache ECharts (huge datasets, canvas/WebGPU), Observable Plot, Unovis (multi-framework), Tremor (dashboards), Highcharts/AG Charts (commercial), LightningChart (realtime), TradingView Lightweight Charts (finance), Vega-Lite |
| Charts (other) | LayerChart (Svelte), Vue ECharts, ngx-charts | D3 7 for anything custom; animate with D3 transitions or Motion on SVG paths |
| Chart motion | Enter by drawing lines (`stroke-dashoffset`), grow bars from baseline, morph between datasets with `d3-interpolate`/Flubber, crossfade tooltips; respect reduced motion | Keep chart animation ≤ 800 ms, no bounce |
| Tables / grids | [TanStack Table](https://tanstack.com/table) (headless) + TanStack Virtual | AG Grid (enterprise features), Glide Data Grid (canvas, 1M rows), MUI X Data Grid, Handsontable (spreadsheet), RevoGrid |
| Rich-text editors | [Tiptap](https://tiptap.dev) (ProseMirror; collaboration, AI extensions), [Lexical](https://lexical.dev) (Meta), Plate (shadcn-style on Slate), BlockNote (Notion-style blocks), Novel | ProseMirror/Slate raw; Quill 2 (simpler); Milkdown (markdown) |
| Code editors | CodeMirror 6, Monaco; syntax highlighting with Shiki (build-time or Shiki Magic Move for animated code diffs) | Prism/Highlight.js older |
| Drag & drop | [dnd-kit](https://dndkit.com), [Pragmatic drag and drop](https://atlassian.design/components/pragmatic-drag-and-drop) (Atlassian, native DnD), Motion `Reorder`, Swapy (any framework) | SortableJS (vanilla), react-beautiful-dnd (deprecated) |
| Panels & layout | react-resizable-panels, Dockview (IDE-style docking), Allotment, Gridstack (dashboards) | — |
| Node graphs / flows | [React Flow / Svelte Flow](https://xyflow.com), Rete.js | — |
| Whiteboards & canvas | [tldraw](https://tldraw.dev) SDK, Excalidraw, Konva (React/Vue), Fabric.js, PixiJS, Perfect Freehand (pen strokes) | Collaboration via Yjs/Liveblocks/PartyKit |
| Collaboration | Yjs, Liveblocks, PartyKit/Cloudflare Durable Objects, Automerge; presence cursors (Liveblocks) | Cursor chat, live avatars, comments |
| Video players | Mux Player, Vidstack, Plyr, Video.js, HLS.js/dash.js, YouTube/Vimeo lite embeds | Scroll-scrub with frame sequences, not `currentTime` |
| Video creation | Remotion, Motion Canvas, Revideo, FFmpeg.wasm (client-side transcode) | — |
| Audio | Howler.js, Tone.js, Wavesurfer.js (waveforms), Web Audio API, `use-sound` | Visualizers via AnalyserNode + canvas |
| Maps | MapLibre GL (open), Mapbox GL, Google Maps (vector), Leaflet (simple), deck.gl (big data layers), Cobe/globe.gl (globes), terrae.dev components | Animate camera with `flyTo`, cluster markers |
| Forms | react-hook-form or TanStack Form + Zod/Valibot; Conform (server actions); Superforms (Svelte); VeeValidate/FormKit (Vue); Angular Signal Forms | Autosave, multi-step with URL state, inline validation timing from §10 |
| File handling | Uppy (uploads, resumable tus), FilePond, react-dropzone, UploadThing | Show progress per file, previews, drag-over states |
| Dates & i18n | Temporal API (shipping), date-fns, Day.js, Luxon; `Intl.*` for formats; next-intl, i18next, Paraglide, Lingui, Vue I18n | Tabular numerals in all date/number displays |
| PDFs & documents | PDF.js, react-pdf (render), @react-pdf/renderer (generate), Nutrient/PSPDFKit | — |
| Markdown rendering | react-markdown + remark/rehype, MDX, Streamdown (streaming), Shiki for code | — |
| Search | Algolia, Meilisearch, Typesense, Pagefind (static), Orama (client-side), Fuse.js | Instant results with keyboard nav |
| Calendars & scheduling | FullCalendar, Schedule-X, react-big-calendar; Cal.com embeds | — |
| Charts of motion itself | Use Chrome DevTools Performance to profile chart redraws; canvas/WebGL beyond \~5k points | — |

## 19. Tooling & workflow

In 2026 the design-to-code gap is closing from both sides: Figma now has a native animation timeline (Figma Motion, open beta since Config, June 2026), Code Layers and Make-to-codebase editing, while AI coding agents pull components straight from registries via MCP. The craft still lives in the review loop: prototype → ship → profile → tune.

**Design & prototyping**

| Tool | What it's for in a motion workflow |
| --- | --- |
| [Figma](https://www.figma.com) (Design, Dev Mode, Variables, Smart Animate, Figma Motion, Code Layers, Make, Sites, Draw, Buzz, Weave tools, Figma MCP server, Agent + Skills) | Source of truth for tokens and layouts; Motion for timeline animation on canvas; Make for prompt-to-prototype and editing real code; MCP to hand context to coding agents |
| [Framer](https://www.framer.com) | Production marketing sites with Motion built in, CMS, effects, AI |
| [Webflow](https://webflow.com) | Visual sites with GSAP (now owned by Webflow) interactions, Lenis via code |
| [Rive](https://rive.app), [Spline](https://spline.design), [Jitter](https://jitter.video), [Cavalry](https://cavalry.scenegroup.co), After Effects, Blender | Interactive/vector animation, 3D, motion graphics, assets |
| ProtoPie, Principle, Play (iOS), Origami Studio | High-fidelity gesture prototypes with sensors and springs |
| [Penpot](https://penpot.app) 2.x, Sketch | Open-source / Mac-native alternatives; Penpot has native DTCG tokens |
| Lottie Creator, SVGator, Lottielab | Code-free Lottie/SVG |

**AI-assisted building (2026)**

| Tool | Role |
| --- | --- |
| Cursor, Claude Code, GitHub Copilot, Windsurf, Codex | Agentic coding; load skills for GSAP/Motion/Anime.js/View Transitions so generated motion follows library best practices |
| [v0](https://v0.app), Lovable, Bolt, Replit, Figma Make, Google Stitch, Subframe, Onlook | Prompt-to-UI; use for first drafts, then refactor onto your tokens and primitives |
| MCP servers: Figma MCP, 21st.dev Magic MCP, shadcn MCP/registry, Motion AI Kit, Storybook MCP | Give agents real components and design context instead of guesses |
| Agent skills (skills.sh, Expo skills, Vercel/Callstack guidance) | Encoded rules for performance, a11y and motion that agents apply automatically |
| Review rule | AI output needs the same audit as §7 snippets: reduced motion, focus, hydration, bundle size, INP |

**Dev tooling**

| Need | Tools |
| --- | --- |
| Build / dev server | Vite 8 (Rolldown), Turbopack (Next), Rspack, esbuild, Bun; Lightning CSS |
| Lint / format | Biome or ESLint 9 + oxlint, Prettier (with Tailwind class sorting), Stylelint, `eslint-plugin-jsx-a11y` |
| Types | TypeScript (native Go-based compiler rolling out), Zod/Valibot for runtime schemas |
| Testing | Vitest 4, Playwright (+ axe, visual snapshots), Testing Library; motion-safe tests by disabling animations under test |
| Visual regression | Chromatic, Percy, Lost Pixel, Argos |
| Component workshop | Storybook 9 (interactions, a11y, visual tests), Ladle, Histoire |
| Profiling | Chrome DevTools (Performance, Animations, Layers), React Profiler, react-scan, r3f-perf, Spector.js, Xcode Instruments, Android Studio Profiler, Flashlight (RN) |
| Monorepo / release | Turborepo, Nx, pnpm workspaces, Changesets |

**Inspiration & reference galleries**

| Gallery | Focus |
| --- | --- |
| [Awwwards](https://www.awwwards.com), [Godly](https://godly.website), [CSS Design Awards](https://www.cssdesignawards.com), FWA, [Minimal Gallery](https://minimal.gallery), [Siteinspire](https://www.siteinspire.com), httpster, Dark Mode Design, [Curated Design](https://www.curated.design), [Landing.love](https://www.landing.love) | Award-level motion and layout |
| [Mobbin](https://mobbin.com), ScreensDesign, Page Flows, Nicelydone, Refero, UI Sources | Real app flows and screens (web + mobile) |
| [Land-book](https://land-book.com), Lapa Ninja, SaaSFrame, One Page Love, Dead Simple Sites | Landing pages |
| [Design Spells](https://www.designspells.com), [Rauno's craft](https://rauno.me/craft), Linear/Vercel/Raycast changelogs, Apple Design Awards | Micro-interaction details |
| Codrops, Tympanus demos, Three.js examples, Shadertoy, Are.na, Savee, Cosmos, Dribbble, Behance, Layers | Creative references and moodboards |
| Component directories: 21st.dev, shadcn registry directory, Uiverse, Hover.dev | Copy-paste starting points |

**Research, analytics & monitoring**: see §17 (usability testing, session replay, A/B) and §12 (RUM, CrUX, Lighthouse CI). Wire `web-vitals` and error tracking (Sentry) into every launch so motion regressions show up as INP/CLS changes, not complaints.

## 20. Legacy & deprecated: avoid or migrate in 2026

These still appear in tutorials and templates but have a better replacement today. Keep them only in codebases you are not rewriting.

| Legacy | Replace with | Why |
| --- | --- | --- |
| jQuery animations, `.animate()`, Velocity.js, Popmotion, Mo.js, Bounce.js, Dynamics.js, Rebound | GSAP, Motion, Anime.js v4, CSS/WAAPI | Unmaintained or superseded |
| `framer-motion` package name, `Motion One` | `motion` (`motion/react`, `motion/vue`, vanilla) | Merged into Motion; legacy package only for migration |
| Anime.js v3 API (`anime({...})`) | v4 modular (`animate`, `createTimeline`) | Breaking rewrite; v3 is frozen |
| GSAP Club/Business licenses, `TweenMax`/`TweenLite` (GSAP 2) | GSAP 3.15 free | Everything is free since 2025; GSAP 2 syntax is dead |
| AOS, WOW.js, ScrollReveal, Sal.js, ScrollOut, ScrollMagic, Waypoints, Skrollr, Rellax, Parallax.js | Native scroll-driven animations, `IntersectionObserver`, GSAP ScrollTrigger | Baseline platform features cover them with no JS |
| Locomotive Scroll v4 and earlier, `@studio-freight/lenis` package name | Lenis (`lenis` package), Locomotive v5 | v5 is a rewrite on Lenis |
| Slick, Owl Carousel, bxSlider, Flexslider, Tiny Slider | Embla, Swiper, CSS scroll-snap carousels | jQuery era, poor touch/a11y |
| react-transition-group, react-motion, react-flip-toolkit, react-beautiful-dnd, react-window | Motion/AutoAnimate, View Transitions, dnd-kit/Pragmatic DnD, TanStack Virtual | Archived or stale |
| Hammer.js, Dragula, interact.js (for simple cases) | Pointer Events, `@use-gesture`, Gesture Handler (RN) | Dead or heavy |
| Floating UI / Popper for simple tooltips, `react-wrap-balancer` | CSS anchor positioning + `popover`, `text-wrap: balance` | Platform now does it (check Firefox for anchor positioning) |
| `tailwindcss-animate`, Tailwind v3 config files, Tailwind UI naming | `tw-animate-css`, Tailwind v4 CSS-first `@theme`, Tailwind Plus | v4 migration |
| styled-components, Emotion, Stitches, Sass for new projects | Tailwind v4, CSS Modules, Panda, vanilla-extract | Runtime cost, RSC conflicts |
| Radix-only assumption in shadcn/ui | Radix or Base UI (default since Jul 2026) | Pick per project; Base UI is actively developed |
| `@angular/animations` | Angular 20.2+ `animate.enter`/`animate.leave` with CSS | Deprecated |
| Google Material Web (web components), Material Design 2 | Material 3 Expressive, M3 Compose, Material Web is in maintenance | Design language moved on |
| Bootstrap/Foundation for premium marketing work | Tailwind + headless primitives | Generic look, heavy resets |
| Image formats: GIF, PNG photos, JPEG without AVIF/WebP fallbacks | AVIF/WebP (JPEG XL arriving), animated WebP/AV1 video | Size and quality |
| Icon fonts (Font Awesome webfont, Material Icons font) | SVG icons (Lucide, Phosphor, Material Symbols SVG) | Flash of unstyled icons, a11y |
| Three.js `WebGLRenderer`-only code with raw GLSL for new work | `WebGPURenderer` + TSL (WebGL fallback) | WebGPU is Baseline across browsers |
| Lottie JSON with heavy mattes/effects, `lottie-web` for new projects | dotLottie runtime or Rive | Size and performance |
| Animating `height`, `width`, `top/left`, `box-shadow`, `filter: blur` on large areas | `transform`, `opacity`, `grid-template-rows`, `interpolate-size`, pseudo-element shadow fade | Layout thrash, jank |
| Full-page preloaders, scroll-jacking, auto-rotating hero carousels, cursor hijacking on touch, parallax without reduced-motion guards | Lighter intros, native scroll, static heroes with one motion focus | Hurt LCP, INP, accessibility, conversion |
| FID as a metric, Lighthouse-only perf reviews | INP + field data (CrUX/RUM) | FID retired March 2024 |
| WCAG 2.0/2.1-only checklists, overlay "accessibility widgets" | WCAG 2.2 AA audits, real fixes | Overlays don't satisfy EAA/ADA and attract suits |
| React Native Legacy Architecture, Expo SDK < 53, `react-native-reanimated` v2, FlatList for large lists | New Architecture, Expo SDK 55+, Reanimated 4, FlashList v2/Legend List | Dropped support |
| Moment.js, `Date` math by hand | Temporal API, date-fns, Day.js | Size and correctness |

## 21. Sources checked (6 Nov 2026) and how to keep this sheet current

Version numbers, dates and support claims in this sheet were checked against the pages below on 6 November 2026; everything else is working knowledge current to mid-2026. Treat anything marked "verify" or "check" as a prompt to open caniuse or the library's changelog.

**Pages consulted**

| Topic | Source |
| --- | --- |
| Platform features, Oct 2026 (scroll-driven animations Baseline, JPEG XL, `random()`, `margin-trim`, grid-lanes, `<install>`) | [web.dev: New to the web platform in October](https://web.dev/blog/web-platform-10-2026) (read in full) · [scroll-driven-animations.style Baseline timeline](https://scroll-driven-animations.style/demos/baseline-newly-available/css/) |
| View Transitions support | [web.dev: same-document view transitions Baseline](https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available) · [corewebvitals.io on View Transitions](https://www.corewebvitals.io/pagespeed/view-transition-web-performance) |
| GSAP 3.15, free licensing, usage share | [GSAP 3.15.0 on VersionEye](https://www.versioneye.com/NodeJS/gsap/3.15.0) · [W3Techs GSAP usage](https://w3techs.com/technologies/details/js-gsap) |
| Motion 12.x, Motion UI, `animateView()` | [motion.dev changelog](https://motion.dev/changelog) · [Introducing Motion](https://motion.dev/magazine/framer-motion-is-now-independent-introducing-motion) |
| Anime.js v4 modules | [animejs.com documentation](https://animejs.com/documentation/getting-started) |
| Lenis / Locomotive v5 | [Locomotive Scroll docs](https://scroll.locomotive.ca/docs/) · [Locomotive releases](https://github.com/locomotivemtl/locomotive-scroll/releases) |
| Three.js r182, WebGPU support, R3F v10 alpha | [Utsubo: WebGPU migration guide](https://www.utsubo.com/blog/webgpu-threejs-migration-guide) · [Utsubo: Three.js 2026](https://www.utsubo.com/blog/threejs-2026-what-changed) · [R3F v10.0.0-alpha.4](https://github.com/pmndrs/react-three-fiber/releases/tag/v10.0.0-alpha.4) |
| Lottie vs Rive, dotLottie state machines, Cavalry free tier | [LottieFiles: LottieFiles or Rive](https://lottiefiles.com/blog/lottie-animations/lottiefiles-or-rive) · [LottieFiles: motion tools by use case](https://lottiefiles.com/blog/design-guides-and-tips/best-motion-design-tools-ranked-by-use-case) · [Rive vs Lottie](https://framer.rive.app/blog/rive-as-a-lottie-alternative) |
| shadcn/ui, Base UI 1.0, Radix status | [PkgPulse: shadcn vs Base UI vs Radix](https://www.pkgpulse.com/guides/shadcn-ui-vs-base-ui-vs-radix-components-2026) · [GreatFrontEnd headless libraries 2026](https://www.greatfrontend.com/blog/top-headless-ui-libraries-for-react-in-2026) · [assistant-ui on Base UI default](https://www.assistant-ui.com/docs/base-ui) |
| Animated component collections | [21st.dev Magic UI](https://21st.dev/magicui) · [21st.dev Aceternity](https://21st.dev/aceternity) · [PkgPulse animation guides](https://www.pkgpulse.com/guides/tag/animation) |
| Tailwind v4.3 | [Tailwind releases](https://releases.sh/tailwind-css/tailwind-css.md) · [Tailwind v4.3 blog](https://tailwindcss.com/blog/tailwindcss-v4-3) |
| Frameworks (Next 16.4, Astro 6, Nuxt 4.6, SvelteKit 3, TanStack Start 1.0) | [FocusReactive headless front-ends 2026](https://focusreactive.com/blog/headless-front-ends-guide-2026/) · [Next.js 16.4 coverage](https://javascript.developpez.com/actu/387966/Next-js-16-4-est-disponible-avec-des-performances-ameliorees-grace-a-Turbopack-et-React-19-3-et-une-reduction-de-20-a-25-pourcent-du-stockage-du-cache-disque/) |
| Core Web Vitals thresholds and tooling | [studiomeyer: Core Web Vitals 2026](https://studiomeyer.io/en/blog/core-web-vitals-2026) · [seojuice: auditing CWV 2026](https://seojuice.com/blog/core-web-vitals-2026-audit-changes/) · [Cloudflare: LCP/INP sub-parts](https://developers.cloudflare.com/changelog/post/2026-10-13-core-web-vital-subparts/) |
| WCAG 3.0 drafts, ADA Title II extension | [WCAG 3.0 Working Draft note](https://a11ybot.pages.dev/news/wcag-3-working-draft-2026/) · [Mitsue-Links: WCAG 3.0 Sept 2026 update](https://www.mitsue.co.jp/knowledge/blog/a11y/202609/14_1608.html) · [Seyfarth via Mondaq: DOJ extends Title II deadlines](https://www.mondaq.com/unitedstates/government-contracts-procurement-ppp/1776328/doj-extends-ada-title-ii-website-accessibility-deadlines-for-governmental-entitiesbut-litigation-and-compliance-risks-remain) |
| Expo SDK 55, RN 0.84, Liquid Glass in RN | [Expo SDK 54 changelog](https://expo.dev/changelog/sdk-54.md) · [expo-glass-effect docs](https://docs.expo.dev/versions/unversioned/sdk/glass-effect.md) · [Cheesecake Labs: State of Mobile 2026](https://cheesecakelabs.com/blog/?p=13707) · [gluestack-ui v4](https://gluestack.io/ui/docs/changelog/v4-alpha-release) |
| Figma Config 2026 (Motion, Code Layers, Weave) | [CMSWire on Config 2026](https://www.cmswire.com/digital-experience/figma-launches-code-layers-motion-at-config-2026/) · [Classmethod recap](https://dev.classmethod.jp/en/articles/figma-config-2026-recap/) · [Figma forum: everything announced](https://forum.figma.com/product-updates-3/everything-announced-at-config-2026-55221) |

**Before adopting any library from this sheet**

- [ ] Last release within 6 months and open issues being answered
- [ ] Weekly downloads and bundle size (Bundlephobia / pkg-size) fit your budget
- [ ] Works with your rendering model (RSC, SSR, islands, React Compiler)
- [ ] Exposes reduced-motion handling and keyboard/focus behavior
- [ ] License fits (MIT vs Motion+/Pro/commercial), and the paid tier isn't hiding the feature you need
- [ ] Browser support matches your audience (caniuse, webstatus.dev)

**Keep it current (what to read, and when)**

| Cadence | Source |
| --- | --- |
| Monthly | web.dev "New to the web platform", Chrome/Firefox/Safari release notes, [webstatus.dev](https://webstatus.dev) Baseline, Interop dashboard |
| Weekly | This Week In React, Bytes, Frontend Focus, CSS Weekly, Codrops Collective, Smashing Magazine, Awwwards site of the day |
| Per release | GSAP release notes, motion.dev changelog, Anime.js releases, Lenis releases, shadcn/ui changelog, Tailwind blog, Expo blog, React Native blog, Three.js releases |
| Yearly | State of CSS / State of JS (autumn), JS Rising Stars (January), Google I/O (May), WWDC (June), Figma Config (June), Next.js Conf (October), Core Web Vitals threshold review on web.dev/vitals, WCAG draft status |
| Design engineering voices | Emil Kowalski, Rauno Freiberg, Josh Comeau, Adam Argyle, Bramus Van Damme, Jhey Tompkins, Val Head's UI Animation newsletter |
