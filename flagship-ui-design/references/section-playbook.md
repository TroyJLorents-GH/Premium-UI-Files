# Section playbook: signature patterns and how they are built

Pick one hero effect, one navigation idea, and two or three micro-interactions per page. Each row is the standard 2026 build. Audit every snippet you adapt for reduced motion, keyboard focus, hydration safety, and bundle weight.

## Landing-page anatomy that converts

Above the fold: one clear value proposition (what, for whom, outcome), one primary CTA, a secondary low-commitment CTA, a social-proof strip (logos, rating, user count), and a product visual that shows the real thing. Then: problem → solution → how it works (3 steps) → features as benefits (bento/alternating) → proof (faces, case numbers) → pricing (toggle, highlighted plan, FAQ) → final CTA → footer. Trust signals near forms; transparent pricing; privacy note under inputs. F-pattern for text-heavy, Z-pattern for sparse. Visitors must be able to reach content and act without waiting through an intro.

## Hero

| Pattern | Build |
|---|---|
| Staggered headline + sub-copy + CTA | SplitText lines with `mask: 'lines'` → GSAP timeline or Motion `staggerChildren`; CTA scales in last; total < 1.2 s; headline and CTA usable almost immediately |
| 3D object / product | Spline embed, or R3F with `Float`, `Environment`, `ContactShadows`; poster image until loaded; lazy after LCP |
| Shader / mesh-gradient background | Paper Shaders, Unicorn Studio, Stripe-style gradient, Three `ShaderMaterial` with simplex noise; clamp DPR; pause offscreen |
| Video background | `<video muted autoplay loop playsinline poster>` AV1/H.265, 6–10 s loop, < 2 MB, darken overlay, pause offscreen and under reduced motion |
| Parallax / depth | CSS `perspective` + `translateZ`, or `view()` timeline per layer; mouse parallax via `useMotionValue` + spring or `gsap.quickTo` |
| 2.5D depth-map hero | Beauty render + Z-depth pass in a small fragment shader; pointer offset `uIntensity` 0.015–0.025 |
| Bento grid | CSS Grid `grid-template-areas` + subgrid for aligned metadata; pointer-tracked `--x/--y` radial spotlight; each card holds a real micro-interaction |
| Animated beams / connectors | SVG paths with `stroke-dashoffset` + gradient (Magic UI Animated Beam) |
| Logo cloud / marquee | Duplicated track + CSS `translateX(-50%)` keyframes, `mask-image` fade edges, pause on hover; GSAP `horizontalLoop` for interactive speed |
| Aurora / spotlight / lamp | Blurred radial gradients with `@property` angle animation; limit area and count |
| Preloader / intro | Only if assets are heavy: counter 0→100 (NumberFlow/GSAP), `clip-path: inset()` curtain, then hero timeline; preloaders cost LCP |
| Scroll cue | Arrow/mouse bounce with reduced-motion guard; fade out on first scroll |

## Navigation & menus

| Pattern | Build |
|---|---|
| Sticky header that hides on scroll down, blurs over content | `position: sticky` + `backdrop-filter` + direction class from GSAP `Observer` or `@container scroll-state(stuck)`; shrink padding/logo with a transition |
| Animated active indicator | Motion `layoutId` pill, View Transitions `view-transition-name`, or CSS anchor positioning |
| Mega menu | Base UI/Radix `NavigationMenu` with cross-fading panels; hover-intent delay 100–150 ms; `AnimatePresence` exits; click/tap and keyboard |
| Full-screen menu (burger → X) | `<dialog>`/popover + `@starting-style`; staggered links; burger lines morph via `transform` |
| Command palette ⌘K | cmdk; fuzzy search; recent items; keyboard hints; 150 ms scale/fade |
| Dock magnification | `useMotionValue` on pointer x → spring-scaled widths |
| Magnetic buttons | `gsap.quickTo()` or Motion springs on pointer offset within 20–40 px; reset on leave; disabled on touch; never move the real hit target unpredictably |
| Mobile bottom nav / sheet | Fixed bar with `env(safe-area-inset-bottom)`; drawer with snap points, drag-to-dismiss, background scale 0.96 |
| Breadcrumbs, scrollspy, TOC | `IntersectionObserver` with `rootMargin` tuned to the sticky header; `aria-current` |
| Curved/skewed menu panel | SVG path morph on open (Olivier Larose curved menu) |

## Scroll patterns

| Pattern | Build |
|---|---|
| Pinned storytelling section | `ScrollTrigger` `pin: true, scrub: 0.5–1.2` on a timeline, or `position: sticky` + `view()` timeline |
| Horizontal runway inside vertical page | Pin a wrapper, tween `xPercent` of the track; or x-axis scroll-snap with `scroll-timeline` progress bar |
| Image-sequence scrub (Apple style) | Preload 60–150 WebP/AVIF frames, draw to `<canvas>` by progress; never scrub `<video>.currentTime` unless encoded with every frame a keyframe (`-g 1`) |
| Scroll-scrubbed Lottie/Rive | `goToAndStop()` or a Rive number input from ScrollTrigger progress |
| Stacking cards | `position: sticky` per card; scale 0.92 and dim via `view()` or ScrollTrigger |
| Text reveal on scroll | SplitText lines + `ScrollTrigger.batch`, or `view()` timeline `animation-range: entry 0% entry 60%` |
| Paragraph lights up as you scroll | word opacity 0.2 → 1 via `view()` timelines or scrubbed stagger |
| Scroll progress bar | `animation-timeline: scroll(root)`, three lines of CSS |
| Velocity skew | read `ScrollTrigger.getVelocity()`/Lenis velocity → `skewY` on images, spring back to 0 |
| Scroll snap sections | `scroll-snap-type: y mandatory` + `scroll-snap-stop: always`; style active with `scroll-state(snapped)`; avoid for long reading content |

Scroll hygiene: passive listeners, `overscroll-behavior: contain` on drawers, `scrollbar-gutter: stable`, `scrollend` instead of debounced scroll, restore position on back navigation.

## Lists, pagination & data

| Pattern | Build |
|---|---|
| Infinite scroll with sentinel | `IntersectionObserver` + `useInfiniteQuery`; keep a "Load more" button for a11y/SEO; restore position on return |
| Virtualized lists | TanStack Virtual / Virtuoso; preserve keyboard and focus |
| Classic pagination | Current page, nearby range, prev/next, disabled states, URL state (nuqs), prefetch next on hover/viewport |
| Skeleton → content | Matches final layout; crossfade; show only if load > ~300 ms |
| Optimistic updates | React 19 `useOptimistic`, TanStack Query mutations with visible rollback |
| Reordering | dnd-kit, Pragmatic DnD, Motion `Reorder`; AutoAnimate for diffs; non-drag alternative |
| Filters with animated layout | Motion `layout` + `AnimatePresence` (`popLayout`), or View Transitions on DOM update |
| Tables | TanStack Table + sticky header, `tabular-nums`, row hover, column resize; virtualize over ~200 rows |
| Empty / error / zero | Illustration (SVG/Lottie), one-line explanation, primary action; never bare "No results" |

## Cards, images & media

| Pattern | Build |
|---|---|
| Hover lift | `translateY(-2px)` + layered shadow transition 150–200 ms ease-out (fade a pseudo-element shadow, don't animate `box-shadow`) |
| 3D tilt | `rotateX/Y` from pointer with spring; `transform-style: preserve-3d`; `(hover: hover)` only |
| Spotlight / border glow | Pointer-tracked radial gradient in a pseudo-element, masked 1 px border |
| Image reveal on scroll | `clip-path: inset()` or scale 1.15 → 1 inside overflow-hidden, `view()` timeline |
| Hover distortion / ripple | WebGL displacement (OGL, Curtains, Codrops); static fallback |
| Expand card → detail | View Transitions or Motion `layoutId`; GSAP Flip for vanilla (`absolute: true, nested: true`) |
| Before/after | `<input type=range>` + `clip-path` |
| Gallery / lightbox | PhotoSwipe, yet-another-react-lightbox; `<dialog>` + View Transition; preserve captions, keyboard exit, focus restoration |
| Glass / Liquid Glass | `backdrop-filter: blur(20px) saturate(180%)` + 1 px light border + inner highlight; refraction via SVG `feDisplacementMap` is CPU-heavy, use sparingly |
| Flip card | `rotateY(180deg)` with `backface-visibility: hidden` |

## Overlays, forms & feedback

| Pattern | Build |
|---|---|
| Modal | `<dialog>` + `@starting-style`, scale 0.96 → 1 + fade, 200 ms enter / 150 ms exit; label, initial focus, Escape, focus restore; `inert` background |
| Drawer / bottom sheet | Snap points, drag-to-close with velocity threshold, background scale; `overscroll-behavior: contain`; safe areas; explicit close |
| Toasts | Sonner (stacked, swipe, promise state, `aria-live`); critical failures stay persistent |
| Tooltips / popovers | Base UI/Radix with `delayDuration`, `@starting-style` fade + 4 px slide; or `popover` + anchor positioning; keyboard-triggered equivalent |
| Inline validation | Validate on blur, re-validate on input after first error; shake 300 ms for hard errors; success check draws in; error summary linked to fields |
| Floating labels, OTP, masks | `:placeholder-shown` / `:has(:focus)`, input-otp, maskito; labels stay visible |
| Multi-step forms | Progress with `layout` transitions, directional slide, state in URL/localStorage, revisit earlier steps safely |
| Buttons | Press scale 0.97 at 100 ms; loading spinner replaces label without width change; success morphs into check; duplicate-submit protection |
| Toggles / checkboxes | Spring thumb (`linear()`), SVG check path draw |
| Pricing toggle | `layoutId` pill + NumberFlow prices + "save 20%" badge |
| FAQ accordion | `<details name>` + `interpolate-size` or grid `0fr → 1fr`; chevron rotate; `::details-content` |
| Consent / banners | Slide from bottom with `@starting-style`; never block LCP |
| Copy / share / celebrate | Clipboard API + "Copied" morph; canvas-confetti once for real milestones; haptics where supported |
| Destructive actions | Confirm only for irreversible/high-cost; type-to-confirm for catastrophic; undo toast for the rest |

## Cursor, background & ambient

- Custom cursor: `cursor: none` + follower with `quickTo`/spring; invert/scale on link hover; mask-reveal cursor; **only** under `(hover: hover) and (pointer: fine)` and not under reduced motion; native affordances preserved.
- Grain/noise: SVG `feTurbulence` fixed pseudo-element at 2–8% opacity (or a tiled PNG for perf), `mix-blend-mode: overlay` on dark surfaces to kill banding.
- Dot/grid backgrounds with radial `mask-image` fade.
- Ambient blobs: blurred gradients drifting on 20–40 s keyframes; `will-change: transform` on 2–3 elements max; paused offscreen.
- Theme switch: `light-dark()` tokens + View Transition circular reveal from the toggle position (`clip-path: circle()` on `::view-transition-new(root)`).

## Footer

Big type or marquee; sticky-reveal footer (`position: sticky; bottom: 0` under content with higher z-index); live local time; link hover underlines (`text-decoration-thickness` + `text-underline-offset` transitions); back-to-top with smooth scroll; navigation, support, identity, legal paths.

## Page transitions

| Approach | How | Use when |
|---|---|---|
| Cross-document View Transitions | `@view-transition { navigation: auto }` on both pages + `view-transition-name` on shared elements; Speculation Rules `prerender` | Astro, Eleventy, Rails, WordPress, any MPA (Chrome/Safari; Firefox pending) |
| Same-document in frameworks | Astro `ClientRouter`, Next `<ViewTransition>` (experimental), Nuxt, SvelteKit `onNavigate` + `startViewTransition`, React Router/TanStack `viewTransition`, Angular `withViewTransitions()` | SPA routing with shared-element morphs |
| Motion `AnimatePresence` + `layoutId` | Mount/unmount choreography | Component-level and tab transitions |
| Barba / Swup / Taxi | Intercept links, fetch next page, run GSAP in/out hooks | Agency/portfolio sites with custom wipes, curtains, image morphs; own focus, scripts, back/forward |

Recipes: crossfade (default), slide by route depth using transition `types`, shared image/card morph, curtain/wipe with `clip-path`, circular reveal from click point, persistent header/player via `view-transition-name: header`. Exits 150–250 ms, enters 250–400 ms. Reduced motion: `::view-transition-group(*) { animation: none }`. Routing hygiene: prefetch on hover/viewport, restore scroll on back, top progress bar for navigations > ~300 ms, persistent shells, no full-page spinners.

## Text effects

- Line/word/char reveal: SplitText (`type: 'lines,words', mask: 'lines'`) or Motion `splitText()` inside `overflow: clip` masks; `yPercent: 100 → 0` with `power3/expo.out`.
- Scroll-linked weight/opacity per word via `view()` or ScrollTrigger scrub.
- Gradient/shimmer text (`background-clip: text` + animated `background-position`) only as a deliberate accent, never the headline default.
- Knockout text over media: `mix-blend-mode` or SVG `<mask>`. Outlined: `-webkit-text-stroke`.
- Variable-weight proximity: `font-variation-settings` by pointer distance.
- Scramble/decrypt, typewriter, loop/morph: GSAP ScrambleText, Motion Primitives Text Morph; short labels only; stable accessible text.
- Streaming text (AI UIs): token fade 150 ms per span; Streamdown for markdown; `aria-live="polite"` with bounded announcements.
- Never animate `font-size`; scale containers. Under reduced motion: show text immediately, opacity only.

## App-side patterns

| Pattern | Do |
|---|---|
| Onboarding | Value in the first session; progressive profiling; checklists; contextual tours only (Driver.js) |
| Loading | Skeletons matching layout, optimistic updates, streaming; no layout shift when data lands |
| Error | Human message, cause, fix, retry; never lose typed data; undo instead of confirm |
| Settings | Autosave with saved indicator, or explicit save with dirty-state warning |
| Search | Instant results, recents, keyboard-first, typo tolerance, zero-result recovery |
| AI chat | Distinguish generated vs sourced; streaming + stop; preserve edits; review consequential actions |
| Dark patterns | None: no confirmshaming, hidden costs, roach-motel cancellation, fake urgency |
