# Surfaces, materials, color, and typography

The difference between a template and a flagship interface is light simulation, perceptual color, surface texture, and type set with intent. Encode all of it in tokens, never per-page overrides.

## Tokens first

- **Spacing**: 4, 8, 12, 16, 24, 32, 48, 64, 96 px scale; fluid section padding via `clamp()`; optical corrections allowed (no "8 px everywhere" dogma).
- **Radius**: 4 / 8 / 12 / 16 / 24 / full; **nested radius rule `inner = outer − padding`**; `corner-shape: superellipse()` for squircles where supported.
- **Shadows**: 2–3 layered soft shadows + 1 px border (Josh Comeau palette approach), tinted with the background hue; elevation tokens `--shadow-1..5`. In dark mode swap shadows for lighter surfaces, borders, and glows.
- **Borders**: 1 px `color-mix(in oklab, currentColor 12%, transparent)` scales across themes better than fixed grays.
- **Z-index**: tokens (`--z-dropdown: 100`, `--z-sticky: 200`, `--z-modal: 300`, `--z-toast: 400`) plus `@layer` order `reset, tokens, base, components, utilities, overrides`.
- **Motion**: `--duration-*`, `--ease-*` named by intent (see motion-numbers).
- Pipeline: Figma Variables / Tokens Studio / Penpot → DTCG JSON → Style Dictionary v4 → CSS vars, Tailwind `@theme`, Swift/Kotlin.

## Color

- Work in **OKLCH** (perceptually uniform lightness). Pickers: oklch.com, Atmos, Huetone, Leonardo (contrast-driven).
- 10–12 steps per hue (Radix Colors semantics: 1–2 backgrounds, 3–5 interactive, 6–8 borders, 9–10 solid, 11–12 text).
- **Semantic roles over raw hues**: `--bg`, `--bg-elevated`, `--fg`, `--fg-muted`, `--border`, `--accent`, `--accent-fg`, `--success/--warning/--danger` each with `-bg/-fg/-border`.
- Derive states: `color-mix(in oklab, var(--accent) 90%, black)` and relative color syntax; `light-dark()` + `color-scheme` for theming instead of duplicated selectors; persist explicit choice without theme flash.
- Contrast: WCAG 4.5:1 text / 3:1 UI for compliance; APCA Lc 60+ body, 75+ small as the perceptual check; test on every actual background including translucent surfaces, gradients, images, video. `contrast-color()` where supported.
- **Dark mode done right**: near-black surfaces (`oklch(15% …)`, e.g. `#090A0F`), not `#000`; lighter surface = higher elevation; top-edge specular highlight; desaturate accents slightly; borders as alpha `color-mix`; reconsider imagery, chart colors, focus rings; test `prefers-contrast` and `forced-colors`.
- Data color: never hue alone; labels, shapes, patterns.
- One accent used as a "functional flashlight" (action, selection) reads premium; three accents read as a template.

## Materials

| Material | Recipe | Constrain |
|---|---|---|
| Frosted glass | `backdrop-filter: blur(16–20px) saturate(180%)` over 40–70% alpha surface + `border: 1px solid rgba(255,255,255,0.14)` inner specular highlight + subtle noise | Large overlapping blur regions, iOS GPU cost, contrast loss; solid fallback for `prefers-reduced-transparency` |
| Progressive blur | Stacked `backdrop-filter` planes masked with `mask-image: linear-gradient(transparent, black)` under floating headers/bars | Count and area |
| Specular hairline border | 1 px pseudo-element with directional gradient and `mask-composite: exclude` so edges catch overhead light | Keep to raised surfaces |
| Cursor-tracked spotlight | `--x/--y` from pointer → `radial-gradient(600px circle at var(--x) var(--y), …)` on a card's border/surface pseudo-element | Pointer devices only |
| Conic border beam | Rotating `conic-gradient` inside a masked 1 px border with an `@property`-typed angle | One or two elements |
| Film grain | Inline SVG `<feTurbulence type="fractalNoise">` at 2–4% opacity, `mix-blend-mode: overlay`, fixed pseudo-element (tiled PNG if perf matters) | Kills banding on dark gradients |
| Gooey / liquid | `<feGaussianBlur>` + high-contrast alpha `<feColorMatrix>` | Small elements |
| Liquid-glass refraction / dispersion | SVG `<feDisplacementMap>` or WebGL refraction, RGB split along rounded edges | CPU-heavy; sparingly |
| Aurora / mesh gradient | WebGL simplex noise or animated radial gradients; Paper Shaders | Resolution cap, pause offscreen |
| Dither / ASCII / halftone | Post-processing passes (Bayer, pixelation, ASCII grid) | Readability of content above |
| Layered elevation shadow | 4–6 layers doubling offset and blur (1, 2, 4, 8, 16, 32 px) + 1 px outline | Light mode; swap for surface lift in dark |

Visual directions 2026: dark Linear/Vercel glow; Swiss editorial type + whitespace; Liquid-Glass translucency; bento; dither/pixel/ASCII textures; 3D product renders; neo-brutalism; monochrome + one accent; grain and mesh gradients. **Pick one per product.**

## Typography

Premium typography in 2026: one or two variable fonts, self-hosted and subset, sized with `clamp()`, `text-wrap: balance` on headings, `tabular-nums` on numbers. Text effects use masked line reveals and scroll-driven weight/opacity, never animated `font-size`.

| Topic | Do this | Tools |
|---|---|---|
| Fluid scale | `font-size: clamp(min, preferred vw + rem, max)` for every step; fluid space too | Utopia, Typescale, fluid-tailwind |
| Variable fonts | One WOFF2 per family with `wght`/`opsz`/`wdth`; `font-optical-sizing: auto`; animate `font-variation-settings` for hover/scroll weight | Inter 4, Roboto Flex, Fraunces, Recursive, Geist, Manrope, Bricolage Grotesque |
| Loading | Self-host; `preload` the body font; `font-display: swap` (or `optional` for zero CLS); subset with `unicode-range`; metric-matched fallbacks via `size-adjust`/`ascent-override`/`descent-override` | `next/font`, Fontaine, Capsize, Fontsource, pyftsubset, Wakamai Fondue |
| OpenType | `font-variant-numeric: tabular-nums slashed-zero`; `font-feature-settings: "ss01", "cv11", "case"`; ligatures where appropriate | Inspect axes with Wakamai Fondue |
| Measure & rhythm | 45–75 ch body (`max-width: 65ch`); line-height 1.45–1.6 body, 1.0–1.15 display; display tracking −0.01 to −0.03 em; 4/8 px vertical rhythm | — |
| Wrapping | `text-wrap: balance` (headings ≤ 4 lines), `pretty` (body), `hyphens: auto` with `lang`, `overflow-wrap: anywhere` for URLs, `hanging-punctuation` | Native; no balancer scripts |
| Vertical alignment | `text-box-trim: trim-both; text-box-edge: cap alphabetic` in buttons/cards | Verify Firefox |
| Rendering | `font-synthesis: none`; `-webkit-font-smoothing: antialiased` only on dark backgrounds; `font-size-adjust` for fallback parity | — |
| Accessibility | ≥ 16 px body on mobile; `rem` units; never `maximum-scale=1`; survive WCAG 1.4.12 spacing overrides and 200% zoom | — |
| International | `lang` per element; per-script fallbacks; `Intl.Segmenter` for grapheme-safe splitting; `word-break: keep-all` for CJK; logical properties for RTL | — |

**Fonts people reach for (2026)**. Free, premium-feeling: Inter 4, Geist/Geist Mono, Satoshi, General Sans, Cabinet Grotesk, Switzer (Fontshare); Instrument Sans/Serif, Manrope, Onest, Figtree, Bricolage Grotesque, Hanken Grotesk, Plus Jakarta Sans, DM Sans/Serif, Newsreader, Fraunces, Source Serif 4, Lora, IBM Plex, JetBrains Mono, Monaspace, Commit Mono. Paid agency look: Söhne, ABC Diatype, ABC Favorit, Neue Montreal, PP Editorial New, PP Neue Machina, Suisse Int'l, GT America, Untitled Sans, Founders Grotesk, Aeonik, Matter, Maison Neue, Basel Grotesk, Berkeley Mono. Inspiration: Typewolf, Fonts In Use. Pair a display voice with a text workhorse; let one carry personality and the other carry reading.

## Icons

One family, consistent stroke and optical size: Lucide, Phosphor (6 weights), Heroicons, Tabler, Material Symbols (variable fill/weight/grade), Iconify for breadth. Animate state changes (hamburger ↔ close, play ↔ pause, heart fill) by transforming SVG parts, not swapping files. Label meaningful icons; `aria-hidden` decorative ones. Never emoji as icons.

## Browser-native capabilities to reach for first

Container queries (size, style, scroll-state), subgrid, `:has()`, `@scope`, nesting, `@layer`, `@property`, `clamp()`, `dvh/svh`, `env(safe-area-inset-*)`, `overscroll-behavior`, scroll anchoring, `scrollbar-gutter`, `popover` + `popovertarget`, `<dialog>` + `showModal()`, invoker commands, anchor positioning (`anchor()`, `position-area`, `position-try-fallbacks`), `<details name>` exclusive accordions, `hidden="until-found"`, customizable `<select>`, `text-wrap`, `text-box-trim`, `field-sizing: content`, `color-mix()`, relative color, `light-dark()`, `contrast-color()`, `display: grid-lanes` (masonry, Safari first), `random()`, `sibling-index()`, JPEG XL. Feature-detect exact subfeatures (`@supports`); Baseline for a parent feature does not establish support for every value.
