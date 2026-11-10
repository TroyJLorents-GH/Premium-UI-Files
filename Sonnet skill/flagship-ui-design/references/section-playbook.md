# Section playbook

Condensed build recipes per page section and component. Pick one hero effect, one navigation idea and two or three micro-interactions per page. The full tables are in `sources/cheat-sheet-2026.md` §10; component-level mechanics in `sources/engineering-reference.md` §6.

## Contents
- Hero
- Navigation and menus
- Bento, cards, media
- Lists, pagination, data
- Overlays, forms, feedback
- Cursor, background, ambient
- Surfaces and materials
- Footer
- Landing-page story arc

## Hero

| Pattern | Build |
|---|---|
| Headline reveal + sub + CTA | SplitText lines in masks → one timeline; CTA last; total <1.2 s |
| 3D product | Spline embed or R3F (`Float`, `Environment`, `ContactShadows`); poster until loaded |
| Shader / mesh gradient | Paper Shaders, Unicorn Studio, Three `ShaderMaterial`; clamp DPR; keep text contrast |
| Video background | `<video muted autoplay loop playsinline poster>`, 6–10 s, <2 MB, dark overlay, pause off-screen |
| Parallax depth | CSS `perspective`/`translateZ`, or `view()` timeline per layer; pointer parallax via spring |
| 2.5D depth hero | Beauty render + depth map shader, offset 0.015–0.025 |
| Animated beams / connectors | SVG `stroke-dashoffset` + gradient |
| Aurora / spotlight | `@property` angle animation on blurred radials (2–3 elements max) |
| Preloader | Usually skip (costs LCP). If used: counter + `clip-path: inset()` wipe, then hero timeline |
| Scroll cue | Bounce with reduced-motion guard; fade on first scroll |

The hero must state *what, for whom, outcome*, one primary CTA, a lower-commitment secondary, proof, and show the real product.

## Navigation and menus

| Pattern | Build |
|---|---|
| Floating glass island nav | `position: sticky` + `backdrop-filter`; hide on scroll-down / reveal on up via `Observer` or `scroll-state(stuck)`; shrink padding |
| Sliding active pill | Motion `layoutId`, or View Transition names, or anchor positioning |
| Mega menu | Base UI/Radix `NavigationMenu`; hover-intent 100–150 ms; cross-fade panels |
| Full-screen menu | `<dialog>`/popover + `@starting-style`; staggered links |
| Command palette ⌘K | cmdk; fuzzy search; recents; key hints; 150 ms scale/fade |
| Magnetic buttons | GSAP `quickTo` or springs within 20–40 px radius; off on touch/reduced motion |
| Dock magnification | Pointer x → spring-scaled widths |
| Mobile bottom nav / sheet | `env(safe-area-inset-bottom)`; Vaul snap points |
| Scrollspy / TOC | `IntersectionObserver` with `rootMargin`; `aria-current` |

## Bento, cards, media

| Pattern | Build |
|---|---|
| Bento grid | CSS Grid `grid-template-areas`, asymmetric spans, Subgrid for aligned metadata, nested radii; each card holds a live micro-demo, not an icon |
| Spotlight / border glow | Pointer `--x/--y` radial gradient in a pseudo-element + masked 1px border |
| Hover lift | `translateY(-2px)` + layered shadow, 150–200 ms ease-out |
| 3D tilt | `rotateX/Y` from pointer with spring, `preserve-3d`, shifting glare |
| Image reveal | `clip-path: inset()` or scale 1.15→1 in overflow-hidden, `view()` timeline |
| Distortion on hover/scroll | WebGL displacement (OGL, Curtains); static fallback |
| Expand card → detail | View Transitions, Motion `layoutId`, or GSAP Flip |
| Before/after | `<input type=range>` + `clip-path` |
| Stacking cards | sticky + scale/brightness on prior cards |
| Marquee / logo cloud | duplicated track, mask edges, pause on hover/off-screen/reduced-motion |

## Lists, pagination, data

| Pattern | Build |
|---|---|
| Infinite scroll | IntersectionObserver + `useInfiniteQuery`, plus a "Load more" button for a11y/SEO |
| Virtual lists/tables | TanStack Virtual/Virtuoso; virtualize >~200 rows |
| Pagination | Cursor API, URL state (nuqs), prefetch next on hover/viewport; show current page, range, previous/next, disabled state, preserved filters |
| Skeleton → content | Layout-matched skeleton only after ~300 ms; crossfade |
| Optimistic updates | `useOptimistic` / mutation rollback |
| Reorder / drag | dnd-kit, Pragmatic DnD, Motion `Reorder`; AutoAnimate for diffs; keyboard + non-drag alternative |
| Empty / zero / error | Illustration + one-line explanation + primary action; never bare "No results" |
| Tables | Sticky header, `tabular-nums`, resizable columns, hover row |

## Overlays, forms, feedback

| Pattern | Build |
|---|---|
| Modal | `<dialog>` + `@starting-style`; scale 0.96→1 + fade; 200 ms in / 150 ms out |
| Drawer / sheet | Vaul: snap points, drag to dismiss, background scale |
| Toasts | Sonner (stack, swipe, promise states, `aria-live`) |
| Tooltips / popovers | Base UI/Radix with delay, or `popover` + anchor positioning |
| Inline validation | On blur, re-validate on input after first error, 300 ms shake only for hard errors, animate success check |
| Buttons | Press 0.97 @100 ms; spinner replaces label without width change; success morphs to check |
| Toggles | Spring thumb (`linear()`), SVG check path draw |
| Pricing toggle | `layoutId` pill + NumberFlow prices |
| FAQ | `<details name>` + `interpolate-size` or `grid-template-rows 0fr→1fr` |
| Multi-step forms | Progress bar, directional slide, persist state in URL/storage |
| Cookie/consent | Bottom slide; never blocks LCP; decline non-essential by default |

## Cursor, background, ambient

Custom cursor only on fine-pointer devices and off under reduced motion. Grain via SVG `feTurbulence` at 2–4% (up to 8% on very dark surfaces), `mix-blend-mode: overlay`. Dot/grid backgrounds with radial mask fade. Ambient blobs 20–40 s drift, 2–3 elements. Theme switch: `light-dark()` tokens + View Transition circular reveal from the toggle.

## Surfaces and materials

- Glass: `backdrop-filter: blur(16–20px) saturate(180%)`, translucent OKLCH fill (40–70% alpha), 1px inner highlight border, optional noise; solid fallback for reduced transparency.
- Progressive blur under floating bars: stacked backdrop-filter planes with gradient `mask-image`.
- Specular hairline borders: 1px pseudo-element with directional gradient using `mask-composite: exclude`.
- Conic border beam: rotating `conic-gradient` in a masked 1px layer, `@property --beam-angle`.
- Elevation: 4–6 layered shadows (1/2/4/8/16/32 px) + hairline; dark UIs elevate with lighter surfaces and top-edge highlights.
- Gooey/liquid: SVG `feGaussianBlur` + alpha `feColorMatrix`; refraction via `feDisplacementMap` is CPU-heavy, use sparingly.

## Footer

Big type or marquee, sticky-reveal footer, local time, link underline hovers, back-to-top. Keep it quiet; it is the exit moment (peak-end rule), so make the final CTA clear.

## Landing-page story arc

Hook (value proposition + real product) → problem → solution → how it works (3 steps) → features as benefits (bento/alternating) → proof (named testimonials with faces, real numbers) → pricing (toggle, highlighted plan, FAQ) → final CTA → footer. Write this arc as one sentence per section before designing; every section must advance the argument.
