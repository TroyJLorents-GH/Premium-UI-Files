# Stack selection

Rule: **platform first, library second, custom engine last.** Choose one primary component system and one principal motion strategy; add a specialist tool only for a concrete requirement. Snapshot date 6 Nov 2026: verify versions, licenses and browser support against official docs before committing.

## Contents
- Job → tool matrix
- Archetype → stack
- Native platform features to try before a library
- Components and tokens
- Typography and color defaults
- Legacy to avoid
- Licensing notes

## Job → tool matrix

| Job | Start with | Notes |
|---|---|---|
| Hover/focus/press, simple enter/exit | CSS transitions, `@starting-style`, `linear()` | Cheapest, compositor-friendly |
| Same-page or cross-page shared element transitions | View Transitions API | Check Firefox cross-document support; give a no-VT fallback |
| Scroll progress, reveals, parallax | CSS scroll-driven animations (`animation-timeline`) | Zero main-thread cost; fall back to IntersectionObserver |
| Complex timelines, pinning, scrubbing, SVG, text | GSAP + ScrollTrigger / SplitText / Flip / DrawSVG / MorphSVG | Free since 2025; see `gsap-playbook/INDEX.md` |
| React app layout, gestures, presence, springs | Motion (`motion/react`, formerly Framer Motion) | `layout`, `layoutId`, `AnimatePresence`, `useSpring` |
| Lightweight landing micro-animations | Anime.js v4 (modular) | Avoid full GSAP if only a few tweens |
| List mutation polish | AutoAnimate | One-line, great for CRUD |
| Smooth scroll | Lenis (or ScrollSmoother in an all-GSAP stack) | Optional; never both; skip for apps/reading UIs |
| Interactive vector illustration/state | Rive; Lottie/dotLottie for AE exports | Verify runtime features; control loops |
| 3D product / scene | Three.js (WebGPURenderer + TSL), R3F + Drei, Spline, model-viewer for simple previews | Budgets in `motion-system.md`; poster fallback |
| Shader backgrounds | Paper Shaders, Unicorn Studio, OGL, custom GLSL | Cap DPR and resolution; keep text readable |
| DOM → WebGL image distortion | Curtains.js / OGL | Awwwards-style; heavy; reduced-motion static fallback |
| 2D canvas scenes | PixiJS, Konva, Fabric.js | Choose throughput vs editing features |
| Physics | Matter.js (2D), Rapier (WASM 2D/3D) | |
| Accessible primitives | Base UI, React Aria, Radix, Ark UI/Zag, Headless UI | One primary foundation |
| Owned styled components | shadcn/ui (Base UI or Radix) + Tailwind v4 | Budget for update ownership |
| Command palette, toasts, drawers, carousels | cmdk, Sonner, Vaul, Embla | Proven; interruptible, accessible |
| Tables / long lists | TanStack Table + Virtual, AG Grid, Virtuoso | Preserve selection, focus, URL state |
| Forms | Native semantics + React Hook Form / TanStack Form + Zod/Valibot | |
| Charts / data viz | Recharts, visx, ECharts, D3, Observable Plot | Tabular numerals, textual alternatives |
| Page-transition routers (MPA) | Swup, Barba.js, or cross-document View Transitions | |
| Mobile native | SwiftUI; Jetpack Compose; React Native + Reanimated + Gesture Handler + Skia; Flutter (Impeller) | Haptics, interruptible gestures, rubber-banding |
| Design tokens | DTCG JSON + Tokens Studio / Style Dictionary | Semantic roles |
| Verification | Playwright + axe, Lighthouse, Chrome DevTools Performance, real assistive tech | Automation covers only ~30–40% of a11y issues |

## Archetype → stack

| Archetype | Stack | Signatures |
|---|---|---|
| Awwwards-style marketing/product launch | GSAP + ScrollTrigger + SplitText (+ Lenis) + Three.js/R3F or canvas sequence | Scroll-scrubbed 3D/canvas, masked kinetic type, cursor spotlights, pinned/horizontal chapters |
| High-craft SaaS web app (Linear/Vercel/Raycast feel) | Motion + Base UI/Radix + shadcn + cmdk + Sonner + View Transitions | Springs, 1px specular borders, ⌘K, optimistic UI, sliding pills, tabular numerals |
| Brand / design-system showcase | Rive + CSS scroll-driven animation + anchor positioning + Vaul | State-machine illustrations, bento with live demos, floating glass nav |
| Editorial / portfolio (Experience mode) | CSS + GSAP (SplitText, Flip) + View Transitions | Big type, restraint, one signature interaction |
| Docs / content (Read mode) | Native CSS, minimal motion | Comprehension first |
| Mobile app | Platform-native or RN Reanimated + Skia | Gesture-driven sheets, shared-element hero, haptics |

## Native platform features to try before a library

View Transitions, scroll-driven animations, `@starting-style`, `interpolate-size`, `popover`, `<dialog>`, anchor positioning, `<details name>`, container queries, `:has()`, `text-wrap: balance|pretty`, `field-sizing`, `color-mix()`, `oklch()`, `light-dark()`, `@property`, Speculation Rules, `content-visibility`. Always check current support (caniuse / webstatus.dev) and ship a graceful fallback.

## Components and tokens

- Layering: headless primitive (behavior, a11y) → copy-paste styled layer (shadcn/ui) → single-purpose components.
- Tokens as CSS variables: semantic color roles (`--bg`, `--bg-elevated`, `--fg`, `--fg-muted`, `--border`, `--accent`), 4/8 spacing, radius 4/8/12/16/24/full with nesting, shadows `--shadow-1..5`, z-index scale, motion tokens (`--duration-fast/base/slow` = 150/250/400 ms; `--ease-out`, `--ease-in-out`, `--ease-spring` via `linear()`).
- Dark mode: near-black (not pure black), lighter surface = higher elevation, slightly desaturated accents, border-based depth, test `prefers-contrast` and `forced-colors`.

## Typography and color defaults

- 1–2 variable fonts, self-hosted WOFF2, subset, preload body font, `font-display: swap|optional`, metric-matched fallbacks (`size-adjust`, `ascent-override`).
- `clamp()` fluid scale (Utopia), body 45–75ch, line-height 1.45–1.6 body / 1.0–1.15 display, negative tracking on large display, `text-wrap: balance` headings, `tabular-nums` on numbers.
- Work in OKLCH; derive states with `color-mix()`; contrast ≥4.5:1 text, 3:1 UI (consider APCA).
- Distinctive free options: Geist, Satoshi, General Sans, Cabinet Grotesk, Switzer, Instrument Sans/Serif, Bricolage Grotesque, Fraunces, Manrope, Hanken Grotesk. Paid-agency feel: Söhne, ABC Diatype, Neue Montreal, PP Editorial New, Suisse. Pick for the world, not for popularity.

## Legacy to avoid for new work

jQuery animation, Velocity, Popmotion, Anime.js v3 API, `TweenMax` (GSAP 2), AOS/WOW/ScrollReveal/ScrollMagic/Waypoints/Skrollr, Locomotive Scroll ≤4, `@studio-freight/lenis` name, Slick/Owl carousels, react-transition-group/react-motion/react-beautiful-dnd/react-window, Hammer.js, styled-components/Emotion/Stitches for new builds, `tailwindcss-animate` (use `tw-animate-css`), icon fonts, raw-GLSL `WebGLRenderer`-only Three.js for new work, heavy Lottie mattes, accessibility "overlay widgets". Full table: `sources/cheat-sheet-2026.md` §20.

UX anti-patterns that hurt LCP/INP/conversion: full-page preloaders, scroll-jacking, auto-rotating hero carousels, cursor hijacking on touch, parallax without reduced-motion guards, animating `height/top/left/box-shadow`.

## Licensing notes

- GSAP: free (including former Club plugins) under a custom license; not OSI-open-source; do not bundle into a competing visual animation builder.
- Lenis, Three.js, glTF-Transform: MIT. Theatre.js: `@theatre/core` Apache-2.0, `@theatre/studio` AGPL-3.0, and slower public maintenance.
- React Bits / Vue Bits: MIT + Commons Clause (redistribution limits). Aceternity/Magic UI: free vs commercial items differ. Tailwind Plus: paid.
- Blender is GPL (outputs are yours); Blender `bpy` add-ons you distribute must be GPL-compatible.
