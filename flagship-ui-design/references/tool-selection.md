# Tool selection (snapshot 6 Nov 2026)

Three rules: **platform first** (CSS, View Transitions, scroll-driven animations, `@starting-style`, popover, anchor positioning), **library second** (GSAP, Motion, Anime.js), **custom engine last** (Three.js, shaders). One primary component system, one principal motion strategy. Statuses: **Standard** (default today) · **Rising** (safe to adopt) · **Niche** (specific need) · **Legacy** (do not start new work on it). Evidence: `V` official source inspected, `R` recheck before adopting. For any entry: `python3 scripts/lookup.py "<name>"` prints its catalog row with URL.

## Choose by the job

| Job | Start by evaluating | Key decision |
|---|---|---|
| Hover/focus/pressed states | Native CSS transitions, `:focus-visible`, `@starting-style` | Explicit property lists; never `transition: all` |
| Component enter/exit, layout, gestures (React/Vue) | **Motion** (`motion/react`, `motion/vue`; `layoutId`, `AnimatePresence`, springs) | Interruptible state tied to real UI; lazy-load with `LazyMotion` |
| Scroll choreography, pinned stories, SVG, complex timelines | **GSAP** + only the plugins used (all free since 2025) | Timeline control; cleanup with `gsap.context()`/`useGSAP()` |
| Lightweight timeline without GSAP's size | **Anime.js v4** (modular ESM, `animate`, `createTimeline`, `createScope`) | v4 API only; v3 tutorials are wrong |
| Physics springs in React | Motion springs or **react-spring** | Retargeting continuity over dramatic bounce |
| Lists that add/remove/reorder | **AutoAnimate** (one line) or Motion `layout` | Precision vs zero authoring |
| Shared-element / page transitions | **View Transition API** (same-document Baseline; cross-document Chrome/Safari) → Motion `layoutId` → GSAP Flip; Barba/Swup/Taxi for agency wipes | Verify exact feature support; focus/history correctness |
| Scroll progress, simple reveals, parallax layers | **Native scroll-driven animations** (`animation-timeline: scroll()/view()`, Baseline Oct 2026) or ScrollTrigger | Static layout must remain complete |
| Smooth scroll (optional, marketing only) | **Lenis** (MIT, ~4 KB, native scrollbar) or GSAP ScrollSmoother | Single ticker; reduced motion; never on content apps |
| Carousels | **Embla** (shadcn default) or Swiper; CSS scroll-snap + `::scroll-button()`/`::scroll-marker` rising | Labeled controls, pause, keyboard |
| Interactive 3D | **Three.js** (`WebGPURenderer` + TSL, WebGL2 fallback) · **R3F + Drei** (React; v10 alpha, pin stable v9) · Threlte (Svelte) · TresJS (Vue) · Babylon.js (apps/games) | Asset budget, DPR cap, accessibility, static fallback |
| Simple product 3D/AR preview | `<model-viewer>` | Poster, loading/error, non-AR path |
| No-code 3D/shader hero | **Spline**, **Unicorn Studio**, **Paper Shaders** (`@paper-design/shaders-react`), ShaderGradient | Embed size, DPR, pause offscreen |
| Image distortion planes | Curtains.js / gpu-curtains, OGL | Resize, context loss, static fallback |
| 2D canvas / editors | PixiJS v8 (GPU 2D), Konva, Fabric.js, tldraw SDK | Accessible alternatives for canvas content |
| Designer-authored animation | **Rive** (state machines, data binding, tiny files) · **dotLottie** (preferred Lottie runtime) | Runtime cost vs interactivity |
| Text split/reveal | GSAP **SplitText** (`mask: 'lines'`, aria handling) · Motion `splitText()` (Motion+) | Final text selectable; no char-by-char reading delays |
| Animated numbers | **NumberFlow** | `tabular-nums` |
| Physics | Matter.js (2D), Rapier (WASM 2D/3D, R3F binding) | Fixed step, bounded bodies |
| Gestures | Pointer Events, `@use-gesture` | Keyboard alternative, dragging alternative (WCAG 2.5.7) |
| Headless accessible primitives (React) | **Base UI** (shadcn default since Jul 2026) · Radix (supported, watch cadence) · React Aria (deepest a11y/i18n) · Ark UI/Zag (multi-framework) | One foundation per product |
| Styled + owned components | **shadcn/ui** (+ shadcn-vue, shadcn-svelte, Spartan for Angular) | You own copied source; record provenance |
| Broad styled suites | MUI, Mantine, Chakra v3, Ant Design, PrimeVue/NG, Nuxt UI v4, Vuetify, Web Awesome | Density, ecosystem, license tiers |
| Drawer/sheet, toasts, ⌘K | Vaul (README: unmaintained; evaluate alternatives for new work) · Sonner · cmdk / Base UI Combobox | Persistent UI for critical failures |
| Tables/lists at scale | TanStack Table + TanStack Virtual · AG Grid · Virtuoso · Glide Data Grid (canvas) | Focus, URL state, scroll restoration |
| Forms | React Hook Form / TanStack Form + Zod/Valibot · Conform · Superforms · VeeValidate/FormKit | Server-error recovery, draft preservation |
| Charts | Recharts 3 (shadcn charts), visx, ECharts (large data), Observable Plot, D3 | Text/table alternative; ≤ 800 ms animation |
| Rich text / code | Tiptap, Lexical, Plate, BlockNote · CodeMirror 6, Monaco, Shiki | Schema and migration planning |
| Drag and drop | dnd-kit, Pragmatic drag and drop, Motion `Reorder`, Swapy | Non-drag reorder path |
| Styling | **Tailwind v4** (CSS-first `@theme`, `tw-animate-css`) · CSS Modules + modern CSS · Panda · vanilla-extract · StyleX | Runtime CSS-in-JS is legacy for new work |
| Tokens | DTCG JSON + Style Dictionary v4 / Tokens Studio / Figma Variables / Penpot | Semantic roles, ownership, platform output |
| Typography delivery | Fontsource, `next/font`, Fontaine, Capsize, pyftsubset, Utopia | Subsetting, metric fallbacks, `font-display` |
| Icons | Lucide, Phosphor, Material Symbols (variable), Iconify; animated: pqoqubbw/icons, Hugeicons, Lordicon | One family; label meaningful icons |
| Frameworks | Next.js 16 (apps), Astro 6 (content/marketing), SvelteKit 3/Svelte 5 (motion-heavy, smallest bundles), Nuxt 4, TanStack Start, React Router v7 | Rendering model, View Transitions support, bundle |
| Page transitions in frameworks | Astro `ClientRouter`, Next `<ViewTransition>` (experimental), Nuxt `experimental.viewTransition`, SvelteKit `onNavigate`, Angular `withViewTransitions()` | Exits 150–250 ms, enters 250–400 ms |
| Measurement | Chrome DevTools Performance/Animations/Layers, `web-vitals` attribution, Lighthouse CI, Playwright + axe, react-scan, r3f-perf, Spector.js | Field p75 beats lab scores |
| User understanding | Task tests, first-click, tree tests (Maze, Lyssna), session replay (Clarity, PostHog) | Method answers the actual question |

## Creative component collections (inspect source before use)

Magic UI (marquee, dock, beams, globe), Aceternity (aurora, lamp, spotlight, container scroll), **React Bits** (text effects, WebGL backgrounds; MIT + Commons Clause), Motion Primitives (beta; app-grade), Animate UI, Cult UI, Kokonut, Fancy Components (physics text), Animata, Codrops (canonical creative demos with tutorials), Inspira UI / Vue Bits (Vue), Svelte Animations. Aggregated with live previews and MCP on **21st.dev**. Audit each snippet for reduced motion, focus, hydration safety, bundle weight, GPU cost on phones.

## Legacy → replacement (do not start new work on the left)

| Legacy | Replace with |
|---|---|
| jQuery `.animate`, Velocity, Popmotion, Mo.js, Tween.js | GSAP, Motion, Anime.js v4, CSS/WAAPI |
| `framer-motion` package, Motion One | `motion` (`motion/react`, `motion/vue`, vanilla) |
| Anime.js v3 `anime({})` | v4 `animate`, `createTimeline` |
| TweenMax/TweenLite, GSAP Club licenses | GSAP 3.15 free (license is custom, not MIT) |
| AOS, WOW, ScrollReveal, Sal, ScrollOut, ScrollMagic, Waypoints, Skrollr, Rellax, Parallax.js | Native scroll-driven animations, IntersectionObserver, ScrollTrigger |
| `@studio-freight/lenis`, Locomotive v4 | `lenis`, Locomotive v5 (built on Lenis) |
| Slick, Owl, bxSlider, Flexslider, Tiny Slider | Embla, Swiper, CSS scroll-snap |
| react-transition-group, react-motion, react-flip-toolkit, react-beautiful-dnd, react-window | Motion/AutoAnimate, View Transitions, dnd-kit/Pragmatic DnD, TanStack Virtual |
| Hammer.js, Dragula | Pointer Events, `@use-gesture` |
| Floating UI/Popper for simple tooltips, `react-wrap-balancer` | CSS anchor positioning + `popover`, `text-wrap: balance` (check Firefox for anchor positioning) |
| `tailwindcss-animate`, Tailwind v3 config | `tw-animate-css`, Tailwind v4 `@theme` |
| styled-components, Emotion, Stitches, Sass for new work | Tailwind v4, CSS Modules, Panda, vanilla-extract |
| `@angular/animations` | Angular 20.2+ `animate.enter`/`animate.leave` |
| Icon fonts | SVG icons |
| `WebGLRenderer`-only + raw GLSL for new work | `WebGPURenderer` + TSL with WebGL fallback |
| lottie-web with heavy mattes | dotLottie runtime or Rive |
| Animating `height/width/top/left/box-shadow/blur` | `transform`, `opacity`, `grid-template-rows`, `interpolate-size`, pseudo-element fade |
| Full-page preloaders, scroll-jacking, autoplay hero carousels, cursor hijack on touch | Light intros, native scroll, static hero with one motion focus |
| FID, Lighthouse-only reviews | INP + field data (CrUX/RUM) |
| WCAG 2.0/2.1-only checklists, accessibility overlays | WCAG 2.2 AA audits and real fixes |
| Moment.js | Temporal, date-fns, Day.js |

## Before adopting any dependency

- [ ] Canonical repo and docs (old names, forks, moved repos are common); release channel (alpha/beta/RC vs stable)
- [ ] Last release within ~6 months and issues being answered; migration guides exist
- [ ] Bundle size and weekly downloads fit the budget; tree-shakes or lazy-loads
- [ ] Works with the rendering model (RSC, SSR, islands, React Compiler, hydration)
- [ ] Exposes reduced-motion handling, keyboard/focus behavior, and exit animations (`data-[state]`)
- [ ] License fits actual use (MIT vs Commons Clause vs custom vs Pro tiers); asset/plugin terms
- [ ] Browser support matches the audience (webstatus.dev, caniuse), including embedded webviews
- [ ] Prototype the hardest interaction with real content on the slowest supported device; measure
- [ ] Record: tool/version · URL · checked date · purpose · license · support · measured cost · decision · risks

## Licensing notes that bite

- **GSAP**: free for commercial use since Apr 2025 including all former Club plugins; the Standard license is custom (not OSI, not GPL-compatible) and prohibits bundling into competing no-code animation builders.
- **Theatre.js**: `@theatre/core` Apache-2.0, `@theatre/studio` AGPL-3.0; public commits slowed after 2024. Prefer baking camera animation into the `.glb` for durability.
- **React Bits / Vue Bits**: MIT + Commons Clause; check redistribution.
- **Blender**: GPL; outputs are yours. Distributed `bpy` add-ons must be GPL-compatible.
- **Motion+**, Magic UI Pro, Aceternity Pro, Tailwind Plus: paid tiers may hold the feature you need.
- **Fonts**: check web embedding rights per family; Fontshare/Google are free; agency faces (Söhne, ABC Diatype, Neue Montreal, PP Editorial New, Suisse) are licensed per domain/pageviews.
