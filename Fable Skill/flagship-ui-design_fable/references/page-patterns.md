# Page patterns

Per-archetype motion floors and caps with acceptance criteria, then the section-by-section playbook: what the signature pattern is, how it is built in 2026, and the trap in each. Expressive archetypes (landing, marketing, launch, portfolio, experiential) have a floor: a hero sequence of several actors, one scroll set piece, three or more named micro-interactions (`signature-motion.md`). Quiet archetypes (apps, dashboards, docs, commerce flows) have a cap: one hero treatment, one navigation idea, two or three micro-interactions, CSS elsewhere.

## Contents

1. Archetypes: composition, motion budget, validation
2. Hero
3. Navigation and menus
4. Sections, bento grids, feature blocks
5. Lists, pagination, data
6. Cards, images, media
7. Overlays, forms, feedback
8. Cursor, background, ambient
9. Footer
10. Mobile-specific rules

## 1. Archetypes

| Archetype | Composition | Motion (floor for expressive, cap for quiet) | Validate first |
|---|---|---|---|
| Landing / marketing / launch (expressive) | A concept figure the product owns; a hero construction from `SKILL.md` §3, never the two-column split; semantic content, authored type and media | Floor: hero sequence of 3–6 actors on one timeline, one pinned scroll set piece that makes the concept physical, 3+ named micro-interactions; secondary content reveals once | First viewport does not read as a template at 1440 and 390; hero and scroll frames show motion; LCP; CTA; no horizontal overflow on phone |
| Portfolio / experiential (expressive) | Strong art direction; GSAP, and a graphics engine where the concept needs it | Floor as above, plus spatial transitions and camera movement; authored scroll chapters alternated with reading | Direct access to content, keyboard, reduced-motion composition, GPU load |
| SaaS app (Linear / Vercel style) | Accessible primitives + tokens + query/state layer; Motion + shadcn/Base UI + cmdk + Sonner | Layout continuity (`layoutId` pills), dialogs, drag feedback, optimistic UI, tabular numerals, 1 px specular borders | Task throughput, forms, focus, error recovery, INP |
| Dashboard | Tables/charts + query cache + virtualization | Filter transitions, selection continuity | Readability, units, large datasets, stale states, export |
| Editorial / docs | Content-first renderer + search + readable type | Anchored navigation, restrained route transitions | Reading, search, deep links, font loading |
| Commerce | Product media + accessible variants + robust checkout | Product transitions, feedback | Pricing truth, stock, cart persistence, payments, device performance |
| Brand / design-system showcase | Rive + scroll-driven CSS + anchor positioning | State-machine illustrations, bento with live sandboxes, glass nav | Interactive value, asset cost |

"Premium" needs no particular framework, kit, or engine on quiet surfaces. On expressive surfaces it needs a concept and choreography; a well-built native control still beats a complicated custom effect inside the product.

## 2. Hero

Acceptance: product, audience, benefit, and next action understood within seconds; the first viewport is unmistakably this product's (see the constructions in `SKILL.md` §3; a headline beside a card, mockup, or image is not an acceptable default on expressive surfaces); real media or an authored scene; one primary CTA and a sensible secondary; LCP content prioritized (`fetchpriority="high"`, preloaded font, no lazy-load); separate mobile art direction (reframed, not stacked); no compulsory intro.

Expressive heroes are a sequence, not a treatment: the concept figure leads, headline lines follow about 350 ms later, CTA and eyebrow land last, nav settles, 1.2–1.8 s on one labeled timeline (`signature-motion.md` §10). The rows below are actors to combine, not alternatives to pick one of.

| Pattern | Build | Trap |
|---|---|---|
| Masked headline lines | SplitText `mask: "lines"` (or Motion `staggerChildren`) → `yPercent: 120→0`, optional `rotate: 1.5→0`, 30–40 ms stagger (80–100 ms for display sizes), `expo.out`; mask padding 0.1–0.15 em with negative margin so ascenders and descenders are not clipped; wait for `document.fonts.ready` | Characters stagger on a sentence; glyphs clipped by a tight mask; headline unreadable for 2 s |
| Concept figure build | The product's own object mid-change (layers separating, a route resolving, a grid reorganizing) as the primary actor; DOM/SVG/canvas per `signature-motion.md` §4–5 | A generic orb, particle cloud, or glass card standing in for a figure |
| 3D object / product | Spline embed or R3F (`Float`, `Environment`, `ContactShadows`); poster first; DPR capped; `frameloop="demand"` idle | 15 MB scene before first paint |
| Shader / mesh gradient background | Paper Shaders, Unicorn Studio, Stripe-style gradient, Three `ShaderMaterial` + simplex noise | Full-res on a 3× phone |
| Video background | `<video muted autoplay loop playsinline poster>` AV1/HEVC, 6–10 s, ≤2 MB, darkening overlay, pause off-screen | Autoplay with sound; no poster |
| Parallax / depth | CSS `perspective` + `translateZ`, `view()` timeline per layer, or mouse parallax via damped pointer; 2.5D depth-map shader for a pre-rendered scene | Large travel under reduced motion |
| Interactive sandbox | Embedded playable micro-app, canvas, or hardware breakdown | Blocking the LCP; no keyboard path |
| Preloader / intro | Only if assets are heavy: counter 0→100 (NumberFlow or GSAP) + `clip-path: inset()` curtain, then hero timeline | Preloader on a light page costs LCP for nothing |
| Magnetic CTA + conic beam | `quickTo` pull at strength 0.3–0.4 on fine pointers; beam on the primary CTA only (`signature-motion.md` §7.1, §8.3) | Beam on every button; pull on touch |
| Scroll cue | Subtle bounce with reduced-motion guard; fade on first scroll | — |

Copy: specific nouns and verbs about what the product does. No "Unlock", "Seamlessly", "Elevate", "Supercharge". Never name a layout position ("the demo at right", "the chart below"): positions change at breakpoints.

## 3. Navigation and menus

Acceptance: current location visible, descriptive labels, keyboard and touch work, deep links, back/forward, focus and scroll restoration, no hover-only access, sticky UI that never hides focused elements.

| Pattern | Build |
|---|---|
| Sticky header that hides on scroll-down, blurs over content, morphs into a floating "dynamic island" pill past ~60 px | `position: sticky` + `backdrop-filter` + direction class from GSAP `Observer` or `scroll-state(stuck)`; morph padding/width/radius with one 400–500 ms ease-out transition on a class toggle, not per-scroll-event style writes |
| Animated active indicator (tabs, nav pill) | Motion `layoutId`, View Transitions `view-transition-name`, or CSS anchor positioning; vanilla: measure target rect once and transition `transform` + `width` on the pill (320 ms, ease-out) |
| Mega menu | Base UI / Radix `NavigationMenu`, cross-fading panels, hover-intent delay 100–150 ms, `AnimatePresence` exit; click opens too |
| Full-screen menu | `<dialog>` or `popover` + `@starting-style`; staggered links 30 ms; burger→X by transforming the lines |
| Command palette ⌘K | cmdk / Base UI Combobox; fuzzy search, recent items, keyboard hints, 150 ms scale/fade; arrow keys, Enter, Escape |
| Dock magnification | `useMotionValue` on pointer x → spring-scaled widths; fine pointer only |
| Magnetic buttons | GSAP `quickTo()` or Motion springs on pointer offset within 20–40 px, strength 0.3–0.4, reset on leave; disable on touch and reduced motion; never move the real hit target far from the pointer |
| Mobile bottom nav / sheet | Fixed bar with `env(safe-area-inset-bottom)`; sheet with snap points and drag-to-dismiss |
| Scrollspy / TOC / breadcrumbs | `IntersectionObserver` with `rootMargin` offset for the sticky header; `aria-current` |

## 4. Sections, bento grids, feature blocks

Acceptance: logical narrative (need → mechanism → evidence → objections → action), varied composition and density within one system, features shown working rather than as interchangeable icon cards, real proof with context, accessible structure (headings in order).

- Bento: CSS Grid `grid-template-areas`, one dominant cell (at least 2× the others) showing the feature working, supporting cells asymmetric in size and density, Subgrid for cross-card alignment, nested radii (`R_outer = R_inner + padding`), each card hosting a live, self-contained micro-animation of a real feature; cursor spotlight on fine pointers only. A row of identical cards (icon, title, sentence) fails the anti-slop check; so does a card whose content fills well under half its area.
- Section rhythm: alternate density and width (full-bleed set piece → single large statement in a narrow measure → dense bento → wide figure). Section padding via `clamp(3rem, 8vw, 8rem)`. On expressive pages one section is the pinned set piece (`scroll-and-3d.md` §4).
- Animated beams / connectors: SVG paths with `stroke-dashoffset` + gradient; one per diagram.
- Logo cloud / marquee: duplicated track, CSS `translateX(-50%)` keyframes, `mask-image` fade edges, pause on hover and off-screen; respects 2.2.2 (pause control if >5 s and informative).
- Section headline: on expressive pages, spread across the top of the section in the display face on two balanced lines, with content below (`clamp()` size, `text-wrap: balance`, no forced `nowrap`). A narrow left column with empty space beside it fails the anti-slop check.
- Playable instrument: a piece of the product the visitor operates, with drag, scrub, or input driving computed output and a live readout on labeled sample data. Use a real range input or arrow keys for the keyboard path, and make it work by touch. This is the standard for proof on a product page; a looping demo is not a substitute.
- Pricing: do not hand-roll a plain table. Run `21st search "pricing components" --type component --limit 5`, compare two or three, `21st get <id>` the best (metered on the free tier), then rebuild it on this page's tokens, type, and easing so it looks native. If nothing fits or 21st.dev is unavailable, run Impeccable as the lead workflow on the pricing section. Keep monthly/yearly toggle with `layoutId` pill, NumberFlow prices, and "save 20%" badge where they apply; billing periods, limits, and exclusions stated. The same sourcing applies to other standard components (FAQ, comparison, testimonials, footer).
- FAQ: `<details name>` + `interpolate-size` or `grid-template-rows: 0fr→1fr`; chevron rotates; answers real objections.
- Comparison tables readable on mobile (stacked or scrollable with sticky first column).

## 5. Lists, pagination, data

| Pattern | Build |
|---|---|
| Infinite scroll | `IntersectionObserver` sentinel + `useInfiniteQuery`; keep a "Load more" button for keyboard/SEO; restore position on return; keep footer reachable |
| Virtualized lists | TanStack Virtual / Virtuoso; preserve focus, selection, find-in-page alternatives |
| Classic pagination | Current page, nearby pages, prev/next, disabled states, total when known; page/filters/sort/size in URL (nuqs); prefetch next page on hover/viewport |
| Skeleton → content | Skeleton matches final layout; show only if load >~300 ms; crossfade with `AnimatePresence`; no endless shimmer |
| Optimistic updates | React 19 `useOptimistic` / TanStack mutations with visible rollback and retry context |
| Reorder / drag-drop | dnd-kit, Pragmatic drag and drop, Motion `Reorder`; non-drag alternative required (WCAG 2.5.7) |
| Filters with animated layout | Motion `layout` + `AnimatePresence mode="popLayout"`, or View Transitions on DOM update |
| Tables | TanStack Table, sticky header, `tabular-nums`, row hover, column resize with keyboard alternative; virtualize over ~200 rows |
| Empty / error / zero states | Illustration (SVG/Lottie), one-line explanation, primary action; never bare "No results"; retries near the failed content |

## 6. Cards, images, media

| Pattern | Build |
|---|---|
| Hover lift | `translateY(-2px)` + shadow pseudo-element cross-fade, 150–200 ms ease-out |
| 3D tilt | pointer offset → `rotateX/Y` max ~12°, `perspective(1000px)`, `transform-style: preserve-3d`, glare via radial gradient at the pointer; spring back on leave; fine pointer only |
| Spotlight / border glow | `surfaces-and-materials.md` §8 |
| Image reveal on scroll | `clip-path: inset()` or scale 1.15→1 inside `overflow: hidden`, `view()` timeline, once |
| Image hover distortion / ripple | WebGL displacement (OGL, curtains.js, Codrops hover-effect); poster fallback |
| Expand card → detail | View Transitions, Motion `layoutId`, or GSAP Flip (`absolute: true`, `nested: true`); enable heavy content after the transition settles |
| Before / after | `<input type="range">` + `clip-path` |
| Gallery / lightbox | PhotoSwipe or `<dialog>` + View Transition; preserve captions, dimensions, keyboard exit, focus restore |
| Glass / liquid glass | `surfaces-and-materials.md` §6; refraction sparingly |
| Flip card | `rotateY(180deg)` + `backface-visibility: hidden` |

Images: AVIF default (WebP fallback), `srcset`/`sizes`, `<picture>` art direction, `loading="lazy"` below the fold only, `decoding="async"`, width/height set, LQIP/ThumbHash placeholders.

## 7. Overlays, forms, feedback

| Pattern | Build |
|---|---|
| Modal | `<dialog>` + `@starting-style`; scale 0.96→1 + fade; 200 ms enter / 150 ms exit; `inert` background (automatic with `showModal()`); focus restored to trigger on close; label it |
| Drawer / bottom sheet | Snap points, drag-to-dismiss with velocity threshold, background `scale(0.92–0.96)` + radius increase, `cubic-bezier(0.32, 0.72, 0, 1)`; logarithmic rubber-band past limits; explicit dismiss control; safe areas and keyboard |
| Toasts | Sonner pattern: stacked with scale 1 − 0.05·i and 10–11 px offsets, fan out to ~70 px on hover, swipe to dismiss, promise states, `aria-live="polite"`, max 3–4 visible; never the only record of a critical failure |
| Tooltips / popovers | Base UI / Radix with delay, `@starting-style` fade + 4 px slide; or `popover` + anchor positioning; keyboard-triggered equivalent; no essential info hover-only |
| Inline validation | Validate on blur, re-validate on input after first error; 300 ms shake only for hard errors; success check animates in; errors linked via `aria-describedby`; summary links to fields |
| Inputs | Persistent labels, correct `type`/`inputmode`/`autocomplete`, paste and password managers allowed, show-password control |
| Multi-step forms | Progress with `layout` transitions, directional slide, state persisted in URL/localStorage, earlier steps revisitable |
| Buttons | Press `scale(0.97)` 100 ms; loading spinner replaces label **without changing width** (reserve width, swap content with opacity); success morphs into a check; width morph via measured `width` is acceptable once per click, not per frame |
| Toggles / checkboxes | Spring thumb (`linear()` easing), SVG check path draw |
| Destructive actions | Confirmation proportional to impact; undo when feasible |
| Copy / share / celebrate | Clipboard API + "Copied" morph; confetti only for meaningful milestones, once, reduced-motion aware |
| Cookie / consent | Slide from bottom with `@starting-style`; never blocks LCP; privacy-preserving default |

## 8. Cursor, background, ambient

- Custom cursor: `cursor: none` + damped follower (`damp()` λ≈14 or `quickTo`), invert/text modes on link hover; experiential sites only; disabled on touch and reduced motion; never on apps.
- Grain overlay: 2–4% fixed pseudo-element or tiled PNG.
- Dot/grid backgrounds with radial `mask-image` fade.
- Ambient blobs: 2–3 blurred gradients drifting on 20–40 s keyframes; `will-change: transform` on those only.
- Theme switch: `light-dark()` tokens + View Transition circular reveal from the toggle.
- Procedural UI sounds (Web Audio oscillators, 8–20 ms ticks): opt-in only, muted by default, never on hover for the whole page.

## 9. Footer

Big type or marquee, sticky-reveal footer (`position: sticky; bottom: 0` under content with higher z-index), local time, link hover underlines, back-to-top with smooth scroll, and the real navigation/support/legal/identity paths the business needs.

## 10. Mobile-specific rules

Touch targets ≥44×44 pt (iOS) / 48×48 dp (Android) for primary controls (WCAG AA minimum is 24×24 CSS px; see `performance-a11y.md`), thumb-zone navigation (bottom tabs, sheets), `env(safe-area-inset-*)`, `100dvh`, `interactive-widget=resizes-content`, `touch-action: manipulation`, `overscroll-behavior: contain` on drawers, `-webkit-tap-highlight-color: transparent`, gestures interruptible and velocity-aware, skeletons and optimistic UI matter more on mobile networks, separate hero crop. For native apps (SwiftUI, Compose, Reanimated 4 + Gesture Handler, Flutter/Impeller): UI-thread animation, interruptible springs, shared-element transitions, haptics on snap points, Reduce Motion and Dynamic Type respected, predictive back on Android.
