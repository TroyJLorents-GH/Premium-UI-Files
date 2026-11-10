# Stack selection

Choose by the job, select the smallest set that expresses the design, and verify before adopting. Status labels (research snapshot November 2026): **Standard** = default today; **Rising** = growing, safe to adopt; **Niche** = right for a specific need; **Legacy** = still works, do not start new work on it. Every version and Baseline claim is dated: confirm with current docs (Context7 or official pages) before writing code.

## Contents

1. The ladder and the rules
2. Choose by the job
3. Native platform features (use before any library)
4. Motion libraries
5. Scroll: smoothing and scroll-linked motion
6. Components: headless, styled, single-purpose
7. Expressive component collections and their caveats
8. 3D, shaders, canvas
9. Designed animation formats
10. Styling systems
11. Frameworks and page transitions
12. What changed 2024–2026 (why older advice is wrong)
13. Adoption rubric

## 1. The ladder and the rules

Platform (CSS, View Transitions, scroll-driven animations, `<dialog>`, `popover`, anchor positioning) → library (GSAP for timelines, scroll choreography, SVG; Motion for React/Vue component state and layout) → engine (Three.js/R3F, OGL, shaders). GSAP and Motion can coexist: Motion owns component state, GSAP owns scroll and timeline choreography. Never install two engines for the same job. Never let two systems write the same property.

## 2. Choose by the job

| Job | Start by evaluating | The decision that matters |
|---|---|---|
| Hover/focus/pressed, small state changes | Native CSS transitions | Cheap, direct, explicit property list (never `transition: all`) |
| Complex sequences, scroll choreography, SVG | GSAP + only the plugins used | Lifecycle cleanup, one ticker, refresh after layout changes |
| App layout, enter/exit, gestures (React/Vue) | Motion | Interruptibility; mount/unmount must allow exit animations (`AnimatePresence`) |
| Physics springs | Motion / react-spring / platform springs | Velocity retargeting over dramatic bounce |
| Shared page/state transitions | View Transition API | Same-document vs cross-document support; keep focus, history, non-animated navigation |
| Scroll progress, simple reveals | CSS `animation-timeline: scroll()/view()` or ScrollTrigger | Static layout must stand on its own |
| Optional smooth scrolling | Lenis (or ScrollSmoother in all-GSAP stacks) | Marketing only; test anchors, focus, touch, reduced motion |
| Interactive 3D | Three.js (WebGPURenderer, TSL) or Babylon.js | Asset budget, DPR cap, fallback poster |
| React 3D | React Three Fiber + selected Drei | Pin stable majors (v10 was alpha at snapshot) |
| Single product preview / AR | `<model-viewer>` | Do not build a scene system for one model |
| Illustrated interactive motion | Rive | Runtime (~100 KB+ WASM) plus asset cost |
| Exported linear animation | dotLottie (preferred runtime) / Lottie / video | State machines only when input changes the story |
| 2D canvas scenes / editors | PixiJS (throughput) / Konva / Fabric.js (editing) | Accessibility is yours to build |
| Shader backgrounds | Paper Shaders, Unicorn Studio embed, small custom shader | Resolution cap, pause off-screen, readable fallback |
| Accessible custom controls | Base UI / Radix / React Aria / Ark UI (one foundation) | Composition, portals, focus in your app |
| Components you customize and own | shadcn/ui (and shadcn-vue, shadcn-svelte, Spartan) | You own the copied source and its updates |
| Broad styled app UI | MUI, Mantine, Ant Design, Fluent, Carbon | Workflow, density, ecosystem |
| Large tables/lists | TanStack Table + TanStack Virtual / Virtuoso / AG Grid | Selection, focus, URL state, scroll restoration |
| Forms | Native semantics + react-hook-form or TanStack Form + Zod/Valibot; Superforms; VeeValidate | Validation timing, server-error recovery |
| Typography | Fontsource / `next/font` + variable font + Utopia | Fallback metrics, zoom, script coverage |
| Tokens | DTCG JSON + Style Dictionary / Tokens Studio | Semantic roles, ownership |
| Verification | DevTools Performance, Playwright + axe, real screen readers | Automation covers a fraction |

## 3. Native platform features (use before any library)

| Feature | Unlocks | Support note (Nov 2026) |
|---|---|---|
| `transition`, `@keyframes`, `transition-behavior: allow-discrete` | Compositor animation; animating `display` | Baseline |
| `@starting-style` | Entry animations from `display: none` for dialogs, popovers, toasts | Baseline 2024 |
| `interpolate-size: allow-keywords` / `calc-size()` | Animate `height: auto`, accordions, `<details>` | Chrome, Safari 26; verify Firefox |
| View Transitions (same-document) | `document.startViewTransition()`, `view-transition-name`, types | Baseline newly available (Chrome 111, Safari 18, Firefox 144) |
| View Transitions (cross-document) | `@view-transition { navigation: auto }` for MPAs | Chrome, Safari 18.2+; Firefox partial |
| Scroll-driven animations | `animation-timeline: scroll()/view()`, `animation-range`, off main thread | Baseline newly available (Firefox 159, Oct 2026) |
| `linear()` easing | Springs and bounces in CSS | Baseline |
| `@property` | Typed custom properties that interpolate (gradients, angles) | Baseline |
| `popover` + `popovertarget`, `<dialog>` + `showModal()`, invoker commands | Tooltip/menu/modal plumbing without a library | Baseline; invokers Chrome 135+, Safari 26 |
| CSS anchor positioning | Replaces Floating UI for tooltips/dropdowns | Chrome 125+, Safari 26+; Firefox in progress, keep Floating UI fallback |
| `<details name>`, `::details-content`, `hidden="until-found"` | Exclusive accordions, find-in-page friendly collapses | Baseline |
| Container queries (size, style), `:has()`, `@scope`, nesting, `@layer` | Component-level responsiveness | Baseline |
| `text-wrap: balance/pretty`, `text-box-trim`, `field-sizing: content` | Balanced headings, trimmed buttons, autosize textarea | Baseline; verify `text-box-trim` Firefox |
| `color-mix()`, relative color, `oklch()`, `light-dark()`, `contrast-color()` | Theme math in CSS | Baseline 2025; `contrast-color()` partial |
| `scroll-state()` container queries, `scrollend` | Stuck/snapped styling without scroll listeners | Chrome; verify others |
| `corner-shape: superellipse`, `clip-path: shape()`, `display: grid-lanes` (masonry) | Squircles, arbitrary clips, masonry | Partial; verify |
| Navigation API, Speculation Rules (`prerender`) | SPA navigation hooks, near-instant next page | Chrome/Edge; Firefox 147+, Safari 26.4+ for Navigation API |
| `IntersectionObserver`, `ResizeObserver`, `scheduler.yield()`, `content-visibility` | Reveal once, responsive components, INP, skip off-screen rendering | Baseline |

Feature-detect exact capabilities (`@supports`, API presence). Build the usable HTML and stable layout first; enhancements may fail independently.

## 4. Motion libraries

| Library | Use for | Status / note |
|---|---|---|
| GSAP 3.15+ (100% free since Apr 2025 under Webflow; SplitText, MorphSVG, ScrollSmoother, DrawSVG, Flip, Inertia all included) | Timelines, ScrollTrigger pinning/scrubbing/snapping, SVG morph/draw/motion path, Flip, Draggable+Inertia, Observer, `useGSAP()` in React | Standard. Custom no-charge license, not MIT; prohibits bundling into a competing visual animation builder. Core ≈23 KB gz plus plugins |
| Motion 12.x (ex-Framer Motion; React, Vue, vanilla) | Component animation: `layout`/`layoutId`, `AnimatePresence`, gestures, `useScroll`/`useTransform`, springs, `Reorder`; hybrid engine hands simple tweens to WAAPI; `LazyMotion` for bundle | Standard. Some features (Motion+) are paid |
| Anime.js v4 (Apr 2025 rewrite) | Small modular timeline engine, `createScope`, `createDraggable`, `createLayout`, SVG drawable/morph | Standard for lightweight vanilla |
| React Spring v10 | Physics hooks across DOM/Three/RN | Standard, slower cadence |
| Web Animations API | Play/pause/reverse without a library; underlies Motion and Anime | Standard |
| AutoAnimate | One-line list add/remove/reorder | Standard for CRUD lists |
| Theatre.js | Visual keyframe editor for Three/DOM | Niche; studio is AGPL; maintenance slowed |
| NumberFlow, Typed.js/TypeIt, canvas-confetti/tsParticles, `@use-gesture`, Rough Notation, `use-sound` | Single-purpose | Standard per need |
| Popmotion, Velocity, Mo.js, Tween.js, KUTE.js, Hammer.js, AOS/ScrollReveal/WOW, ScrollMagic, Waypoints, Skrollr, Rellax, react-flip-toolkit, react-window | Maintenance only | Legacy |

Framework-native first: Svelte 5 (`transition:`, `animate:flip`, `Spring`/`Tween`, `crossfade`) rarely needs a library; Vue `<Transition>`/`<TransitionGroup>`; Angular 20+ `animate.enter/leave` (deprecated `@angular/animations`); React has nothing built in (`<ViewTransition>` experimental).

## 5. Scroll: smoothing and scroll-linked motion

| Tool | Notes | Status |
|---|---|---|
| Lenis (MIT, ~4 KB) | Keeps native scrollbar; `data-lenis-prevent` for nested scrollers; `autoRaf: false` + `gsap.ticker`; incompatible with native CSS scroll-snap (use its snap addon); keep touch native (`syncTouch` off); disable under reduced motion and in WebViews | Standard for marketing/portfolio |
| Locomotive Scroll v5 | Declarative `data-scroll` wrapper over Lenis | Standard for declarative projects |
| GSAP ScrollSmoother | Deepest ScrollTrigger integration, `data-speed`/`data-lag`; needs wrapper/content structure; test fixed elements, anchors, focus | Standard in all-GSAP stacks |
| Native `scroll-behavior: smooth` + `scrollIntoView` | Apps, docs, dashboards | Standard |
| GSAP ScrollTrigger | Pin, scrub, snap, `batch()`, `normalizeScroll()`, markers | Standard |
| CSS scroll-driven animations | Reveals, progress bars, parallax layers, image sequences off main thread | Standard |
| IntersectionObserver (+ Motion `whileInView`) | One-shot class toggles | Standard |
| Scrollama | Data-journalism stepping | Niche |
| Embla (what shadcn ships), Swiper 11 | Carousels; CSS scroll-snap + `::scroll-button()`/`::scroll-marker` rising | Standard |
| TanStack Virtual, Virtuoso | Long lists | Standard |

Smooth scroll is a marketing-site tool. Never on content-heavy apps.

## 6. Components: headless, styled, single-purpose

Headless (behavior + a11y, no styles): Base UI 1.0 (default under shadcn since July 2026; from the Radix/Floating UI/MUI authors), Radix Primitives (mature; cadence slowed, still supported), React Aria (deepest a11y/i18n), Ark UI/Zag (multi-framework), Headless UI v2, Reka UI (Vue), Bits UI (Svelte), Kobalte (Solid), Angular CDK/Aria. Choose one foundation per product. A default change (Radix → Base UI) is not a reason to rewrite a working system.

Styled / copy-paste: shadcn/ui (Tailwind v4, registry, blocks, Visual Builder), Radix Themes, Park UI, Mantine 8, Chakra v3, MUI v7, HeroUI, Nuxt UI v4, PrimeVue, shadcn-svelte, Spartan (Angular), Web Awesome (web components). Reference systems to study for API and motion tokens: Geist, Primer, Polaris, Carbon, Spectrum 2, Fluent 2, Atlassian, Gestalt, Material 3 Expressive, Apple HIG.

Single-purpose that premium apps reuse: Sonner (toasts), cmdk (⌘K), NumberFlow, react-resizable-panels, input-otp, TanStack Table/Form/Query, react-day-picker, next-themes, nuqs, dnd-kit / Pragmatic drag and drop, react-dropzone/Uppy, Tiptap/Lexical, Streamdown + assistant-ui for AI chat.

Caveats found in the research: **Vaul's README says unmaintained**; keep it in existing projects, evaluate a maintained drawer (Base UI Dialog + drag handling, or a current fork) for new work, while keeping its signature settle curve. **Vercel AI Elements** announced deprecation at end of November 2026 in favor of shadcn/ui AI Elements. **React Bits / Vue Bits** are MIT + Commons Clause (redistribution limits). Embla docs distinguish v9 RC from v8 stable.

Checklist when picking any component: keyboard and screen-reader behavior, reduced-motion handling, RTL, bundle size, SSR/RSC compatibility, exit-animation support (`data-[state]` attributes).

## 7. Expressive component collections and their caveats

Most "wow" effects on 2026 landing pages come from a dozen copy-paste collections (Tailwind + Motion, sometimes GSAP/OGL/Three): Magic UI, Aceternity UI, React Bits, Motion Primitives (beta), Animate UI, Cult UI, Kokonut UI, Skiper UI, Fancy Components, Animata, Hover.dev (paid), Tailark/shadcnblocks (marketing sections), Inspira UI/Vue Bits (Vue), Svelte Animations, Uiverse (CSS), Codrops (original creative effects with tutorials). 21st.dev aggregates them with search, CLI, and MCP.

Treat every snippet as owned source: audit `prefers-reduced-motion`, keyboard focus, hydration safety, bundle weight, GPU cost on a phone, and license before shipping. The collections are where slop comes from when pasted whole; they are reference material when adapted to your tokens and budget.

Tutorial authors whose patterns define the current look (study, do not copy): Emil Kowalski (Vaul, Sonner, animations.dev), Rauno Freiberg (rauno.me/craft, easing.dev), Josh Comeau, Sam Selikoff (Build UI), Jhey Tompkins, Adam Argyle, Bramus Van Damme (scroll-driven, view transitions), Olivier Larose (zoom parallax, curved menu, mask cursor), Bruno Simon (Three.js Journey), Codrops.

## 8. 3D, shaders, canvas

Three.js r182+ with `WebGPURenderer` and TSL (compiles to WGSL and GLSL, WebGL 2 fallback) is the default engine; R3F v9.x stable with Drei (`Environment`, `MeshTransmissionMaterial`, `Float`, `ContactShadows`, `ScrollControls`, `useGLTF`); `@react-three/rapier` for physics; `pmndrs/postprocessing` for bloom/DoF/grain/dither. Threlte (Svelte), TresJS (Vue). Babylon.js 8 for apps/configurators/games. OGL for shader-heavy creative sites with a small bundle. PixiJS v8 for 2D. `<model-viewer>` for product/AR. No-code sources: Spline (most common 3D hero), Unicorn Studio (shader embeds), Paper Shaders (`@paper-design/shaders-react`), ShaderGradient. Asset pipeline: Blender → glTF/GLB → `gltf-transform optimize --compress meshopt --texture-compress ktx2`. Details, budgets, and the Blender-to-web workflow: `scroll-and-3d.md`.

## 9. Designed animation formats

CSS for UI transitions; dotLottie (`@lottiefiles/dotlottie-web`, WASM renderer, themes, state machines) as the preferred Lottie runtime; Lottie JSON (`lottie-web` ~60 KB+, masks/mattes hurt) for broad compatibility; Rive (`.riv` 10–15× smaller, state machines, data binding, one C++ renderer, ~100 KB+ runtime, freemium editor) for anything reacting to state or data; animated SVG (CSS/SMIL/`offset-path`) for line art under ~1k nodes; muted looping `<video>` (AV1/HEVC, ≤2 MB, poster, pause off-screen) to replace GIFs. Icon systems: Lucide, Phosphor, Heroicons, Tabler, Hugeicons, Iconify, Material Symbols (variable axes); animate icon state changes by transforming SVG parts, not swapping files. Authoring: After Effects + Bodymovin, Lottie Creator, Rive Editor, Jitter, Cavalry (free for individuals since Apr 2026), SVGator.

## 10. Styling systems

Tailwind CSS v4.x (Oxide, CSS-first `@theme`, container queries, `@property`-backed utilities) is the default; helpers `tailwind-merge`, `clsx`/`cn()`, `cva` or `tailwind-variants`, `tw-animate-css`, `prettier-plugin-tailwindcss`. Alternatives: CSS Modules + modern CSS (systems that outlive frameworks), Panda CSS (typed tokens, Park UI), vanilla-extract, StyleX (very large apps), UnoCSS, Open Props (vanilla tokens). Runtime CSS-in-JS (styled-components, Emotion, Stitches) is legacy and conflicts with RSC. Sass is legacy for new work (nesting, mixins, color functions are native now). Lightning CSS / PostCSS in the pipeline. Conventions that read as premium: tokens first, OKLCH + `color-mix()`, logical properties, `@layer` order, container queries for components, utilities for layout and custom properties for theme, critical CSS inlined (<14 KB), no `!important`.

## 11. Frameworks and page transitions

Transitions: cross-document View Transitions + Speculation Rules for MPAs (Astro, Eleventy, Rails, WordPress); same-document View Transitions in every framework (Astro `ClientRouter`, Next `experimental.viewTransition` + React `<ViewTransition>`, Nuxt, SvelteKit `onNavigate`, React Router/TanStack `viewTransition`, Angular `withViewTransitions()`); Motion `AnimatePresence` + `layoutId` for component-level; Barba.js / Swup / Taxi.js for GSAP-choreographed agency sites (own focus, analytics, scripts, back/forward). Recipes: crossfade default, slide by route depth with transition `types`, shared image morph via `view-transition-name`, curtain/wipe with `clip-path`, circular reveal from click point, persistent header/player. Exits 150–250 ms, enters 250–400 ms; reduced motion → `::view-transition-group(*) { animation: none }`.

Frameworks (Nov 2026): Next.js 16 + React 19 (heaviest baseline, best product-app tooling), React Router v7 / TanStack Start + Router (lighter React full-stack), Astro 6 (default for content and marketing), SvelteKit / Svelte 5 (smallest bundles, best built-in motion), Nuxt 4 / Vue 3.6, SolidStart, Qwik 2, Angular 21, HTMX 2 / Alpine / Hotwire for server-rendered stacks, Eleventy/Hugo for static. Routing hygiene for feel: prefetch on hover/viewport, restore scroll on back, top progress bar for navigations over ~300 ms, persistent shells (header, player, sidebar), no full-page spinners.

## 12. What changed 2024–2026 (why older advice is wrong)

- GSAP became 100% free (Apr 2025) after Webflow acquired GreenSock; all former Club plugins ship free. Advice to avoid SplitText/MorphSVG for licensing is obsolete.
- Framer Motion was renamed Motion and runs in React, Vue, and vanilla JS with a hybrid WAAPI engine.
- Anime.js v4 is a full rewrite; v3 tutorials describe a different API.
- View Transitions, scroll-driven animations, `@starting-style`, anchor positioning, `popover`, `linear()` reached Baseline or near it, replacing whole libraries (AOS, Popper/Floating UI for simple cases, react-wrap-balancer, autosize scripts).
- Lenis is the de-facto smooth-scroll layer; Locomotive v5 was rebuilt on it.
- Tailwind v4 moved to CSS-first config; shadcn defaults to Base UI (Radix still supported).
- INP replaced FID (Mar 2024), target ≤200 ms. Claims of a March 2026 tightening (INP 150, LCP 2.0) were unverified at snapshot; check web.dev/vitals before quoting.
- WCAG 2.2 is current; EAA applies since June 2025; US ADA Title II deadlines moved to April 2027.
- Apple Liquid Glass (iOS 26) and Material 3 Expressive pushed platform motion toward springs, morphing shapes, layered translucency.
- Rive is the interactive state-machine default; dotLottie the compact Lottie runtime.
- WebGPU is production-ready in all major browsers; Three.js WebGPURenderer + TSL is the forward path.

## 13. Adoption rubric

Score 0–3 on task fit, accessibility, visual control, performance on the weakest supported device, platform fit (framework versions, SSR/hydration, browsers), state completeness (errors, cancellation, empty, async), maintenance (releases, migration guides, responsiveness), license and cost (actual use, redistribution, templates), ownership (can you maintain, replace, debug, export), integration cost. Treat accessibility, license, and essential platform support as gates, not averages.

Before adopting a repository: verify the canonical project (names, forks, archived mirrors, transfers are common), check the release channel (main-branch demos may use alphas), read the exact license and asset terms, build one representative hard interaction with real content and measure it, check keyboard/touch/AT/reduced motion/localization on the slowest device, and record tool · version · URL · checked date · purpose · license · target support · measured cost · decision · known risks in a project decision log.
