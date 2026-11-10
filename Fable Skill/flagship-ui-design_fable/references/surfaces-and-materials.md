# Surfaces and materials

Tokens, color, typography, dark mode, and the CSS recipes for the surface effects that read as premium when the parameters are right and as slop when they are not. Recipes are distilled from the bundled 120 Hz motion lab (`assets/motion-lab-reference.html`; the effect catalog with line references is `signature-motion.md`) and the 2026 research; each carries its cost.

## Contents

1. Token architecture
2. Color
3. Typography
4. Dark mode
5. Shadows and elevation
6. Glass
7. Specular hairline border
8. Cursor spotlight
9. Conic border beam
10. Grain
11. Gooey and displacement filters
12. Cost table

## 1. Token architecture

Author once (DTCG JSON, Figma Variables, or a CSS file), compile to CSS custom properties, Tailwind `@theme`, or Panda tokens. Layers: primitives → semantic roles → component tokens.

- Spacing: 4, 8, 12, 16, 24, 32, 48, 64, 96 px; fluid section padding via `clamp()`.
- Radius: 4 / 8 / 12 / 16 / 24 / full. Nested rule: `inner = outer − padding`. `corner-shape: superellipse(…)` for squircles where supported (verify).
- Z-index as tokens (`--z-dropdown: 100`, `--z-sticky: 200`, `--z-modal: 300`, `--z-toast: 400`) with `@layer` ordering (reset, tokens, base, components, utilities, overrides).
- Motion tokens: see `motion-system.md` §9.
- Logical properties (`margin-inline`, `inset-block`) for RTL. Container queries for components, media queries for page layout.
- Borders: `color-mix(in oklab, currentColor 12%, transparent)` scales across themes better than fixed grays.

`assets/tokens.css` is a starter file for all of this.

## 2. Color

- Define in OKLCH (perceptually uniform lightness): `oklch(L C H)`. Pickers: oklch.com, Huetone, Atmos, Leonardo (contrast-driven), Material Theme Builder (HCT).
- Scales of 10–12 steps per hue with semantic roles (Radix Colors convention): 1–2 app/subtle backgrounds, 3–5 interactive component backgrounds (normal/hover/active), 6–8 borders and separators, 9–10 solid fills (brand, hover), 11–12 low- and high-contrast text.
- Semantic roles over raw hues: `--bg`, `--bg-elevated`, `--fg`, `--fg-muted`, `--border`, `--accent`, `--accent-fg`, and `--success/--warning/--danger` each with `-bg/-fg/-border`.
- Derive states: `color-mix(in oklab, var(--accent) 90%, black)` for hover; relative color syntax `oklch(from var(--accent) calc(l - 0.08) c h)` for pressed.
- Contrast: WCAG 4.5:1 body / 3:1 large text and UI parts for compliance; APCA Lc 60+ body, 75+ small text as the perceptual check. Test every real pair, including text over gradients, video, glass, and images.
- Wide gamut: OKLCH lets you reach Display P3; always check gamut mapping on sRGB screens, and keep a sRGB fallback where the gamut shift would change meaning.
- Theming: `color-scheme: light dark` + `light-dark()` or `[data-theme]`; persist explicit choice (next-themes or a cookie) to avoid theme flash; theme switch as a View Transition circular reveal from the toggle position.

## 3. Typography

| Topic | Do this |
|---|---|
| Families | One or two variable fonts (`wght`, `opsz`, `wdth` axes); `font-optical-sizing: auto`. Free premium-feeling: Inter 4, Geist, Satoshi, General Sans, Switzer, Manrope, Instrument Sans/Serif, Bricolage Grotesque, Fraunces, Newsreader, JetBrains Mono, Monaspace. Paid agency look: Söhne, ABC Diatype, Neue Montreal, PP Editorial New, Suisse Int'l, GT America |
| Loading | Self-host, `preload` the body font, `font-display: swap` (or `optional` for zero CLS), subset by `unicode-range`, metric-matched fallbacks via `size-adjust`/`ascent-override`/`descent-override` (Capsize, Fontaine, `next/font`) |
| Scale | `font-size: clamp(min, preferred, max)` per step (Utopia); fluid space too |
| Measure and rhythm | 45–75 ch body (`max-width: 65ch`), line-height 1.45–1.6 body, 1.0–1.15 display, negative tracking only on large display (−0.01 to −0.03 em), 4/8 px vertical rhythm |
| Wrapping | `text-wrap: balance` on headings up to ~4 lines, `pretty` on body, `hyphens: auto` with `lang`, `overflow-wrap: anywhere` for URLs |
| OpenType | `font-variant-numeric: tabular-nums slashed-zero` on counters, prices, tables; `font-feature-settings` for stylistic sets; `font-kerning: normal` |
| Vertical trim | `text-box-trim: trim-both; text-box-edge: cap alphabetic` removes half-leading in buttons and cards (verify support) |
| Rendering | `font-synthesis: none`; `-webkit-font-smoothing: antialiased` only on dark backgrounds |
| Accessibility | ≥16 px body on mobile, `rem` units, never `maximum-scale=1`, spacing overrides (1.5 line-height, 2× paragraph, 0.12 letter, 0.16 word) must not break layout |
| International | `lang` per element, per-script fallback stacks, `Intl.Segmenter` for grapheme-safe splitting (emoji, Indic), `word-break: keep-all` for CJK |

Text effects: line/word masked reveals (SplitText `mask: "lines"`, Motion `splitText`; pad each mask block 0.1–0.15 em with a matching negative margin so ascenders and descenders are not clipped at tight display line-heights), scroll-linked per-word opacity (0.15 → 1 as the reading point passes; `view()` timeline or ScrollTrigger scrub), gradient/shimmer text via `background-clip: text` with an `@property`-typed angle, variable-weight proximity via `font-variation-settings`, knockout text with `mix-blend-mode` or SVG mask, underline animations via `text-decoration-thickness`/`text-underline-offset`. Under reduced motion, show text immediately; keep only opacity.

## 4. Dark mode

- Base is near-black with a hue, never `#000`: `oklch(14–16% 0.01–0.02 H)`; the lab's family `#07090E` (base) → `#0D111A` (surface) → `#131926` (elevated).
- Elevation is a lighter surface, not a bigger shadow. Add a top-edge highlight (`inset 0 1px 0 rgba(255,255,255,0.06–0.12)`) on raised cards.
- Desaturate accents slightly; body text at 85–92% opacity, display at 100%; borders as 6–12% white or `color-mix` of `currentColor`.
- Reconsider imagery, chart colors, focus rings, and shadows; do not invert.
- Test `prefers-contrast: more` and `forced-colors: active` (state must not live only in background images or gradients).

## 5. Shadows and elevation

Two or three layered soft shadows plus a 1 px low-alpha border for UI cards (Josh Comeau palette approach, tinted with the background hue); four to six layers with doubling offsets and blur only for hero or elevated marketing surfaces where the cost is paid once.

```css
/* UI card, light mode */
--shadow-2: 0 1px 2px oklch(from var(--bg) l c h / 0.06),
            0 4px 12px oklch(from var(--bg) l c h / 0.08);
/* Elevated marketing surface, dark mode */
.ambient-shadow {
  box-shadow:
    0 1px 2px rgba(0,0,0,.45), 0 4px 8px rgba(0,0,0,.35),
    0 12px 24px rgba(0,0,0,.35), 0 24px 48px rgba(0,0,0,.45),
    inset 0 1px 0 rgba(255,255,255,.12);
}
```

Hover lift: `translateY(-2px)` and cross-fade a pseudo-element that carries the larger shadow (150–200 ms ease-out). Never animate `box-shadow` directly.

## 6. Glass

```css
.glass {
  background: rgb(13 17 26 / 0.42);               /* 40–70% alpha of the surface color */
  backdrop-filter: blur(20px) saturate(190%);      /* blur 16–20, saturate 180–190 keeps dark glass from going muddy */
  -webkit-backdrop-filter: blur(20px) saturate(190%);
  border: 1px solid rgb(255 255 255 / 0.16);      /* 0.12–0.16 */
  box-shadow: inset 0 1px 0 rgb(255 255 255 / 0.45), 0 20px 40px rgb(0 0 0 / 0.45);
}
@media (prefers-reduced-transparency: reduce) {
  .glass { background: var(--bg-elevated); backdrop-filter: none; }
}
```

Add 2–4% grain inside the glass (§10). Progressive blur under floating headers: stack 2–3 `backdrop-filter` layers masked with `mask-image: linear-gradient(to bottom, black, transparent)` so content dissolves rather than cutting off. Liquid-glass refraction (SVG `feDisplacementMap`) is CPU-heavy: one small element, never a full surface. Limit total blurred area and count, particularly on iOS; verify text contrast against moving content underneath.

## 7. Specular hairline border

A 1 px gradient ring that catches light from one direction, built with a masked pseudo-element so it respects `border-radius`.

```css
.specular { position: relative; }
.specular::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit; padding: 1px;
  background: linear-gradient(135deg, rgb(255 255 255 / .24), rgb(255 255 255 / .06) 45%, rgb(34 211 238 / .14));
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
  pointer-events: none;
}
```

## 8. Cursor spotlight (bento cards)

```css
.card { --x: -500px; --y: -500px; position: relative; overflow: hidden; }
.card::after {                /* soft surface glow */
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: radial-gradient(550px circle at var(--x) var(--y), rgb(34 211 238 / .07), transparent 55%);
}
.card-border {                /* 1px illuminated ring */
  position: absolute; inset: 0; border-radius: inherit; padding: 1px; pointer-events: none;
  background: radial-gradient(360px circle at var(--x) var(--y), rgb(34 211 238 / .75), rgb(99 102 241 / .35) 35%, rgb(255 255 255 / .07) 70%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
}
```

```js
// One listener on the grid, not one per card; rects cached and refreshed on resize/scroll-end.
grid.addEventListener("pointermove", (e) => {
  for (const [card, r] of rects) {
    card.style.setProperty("--x", `${e.clientX - r.left}px`);
    card.style.setProperty("--y", `${e.clientY - r.top}px`);
  }
}, { passive: true });
```

Gate behind `@media (hover: hover) and (pointer: fine)`. Calling `getBoundingClientRect()` per card per move forces layout; cache.

## 9. Conic border beam

```css
@property --beam-angle { syntax: "<angle>"; initial-value: 0deg; inherits: false; }
@keyframes spin-beam { to { --beam-angle: 360deg; } }
.beam { position: relative; isolation: isolate; }
.beam::before {
  content: ""; position: absolute; inset: -1px; border-radius: inherit; padding: 1.5px; pointer-events: none;
  background: conic-gradient(from var(--beam-angle), transparent 60%, var(--accent-2) 82%, var(--accent) 96%, #fff 100%);
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor; mask-composite: exclude;
  animation: spin-beam 3.2s linear infinite;
}
@media (prefers-reduced-motion: reduce) { .beam::before { animation: none; } }
```

One CTA per screen. A rotating beam on every card is the single most recognizable slop tell.

## 10. Grain

```html
<svg class="grain" aria-hidden="true">
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.82" numOctaves="4" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  <rect width="100%" height="100%" filter="url(#grain)"/>
</svg>
```

`.grain { position: fixed; inset: 0; pointer-events: none; opacity: 0.03; mix-blend-mode: overlay; }` — 2–4% over surfaces and gradients (kills banding, adds a matte finish); up to ~6% as a deliberate texture. A live full-viewport SVG filter costs paint on every frame it overlaps; a tiled 256 px noise PNG is cheaper and looks the same. Grainy gradients: `feTurbulence` + gradient with `mix-blend-mode`.

## 11. Gooey and displacement filters

Gooey merge (`feGaussianBlur stdDeviation 10–16` → `feColorMatrix` alpha `0 0 0 24 -10` → `feComposite atop`) melts badges or blobs together; displacement (`feTurbulence baseFrequency 0.02–0.03` → `feDisplacementMap scale 20–40`) gives liquid lenses and chromatic split (pair with two opposing colored `text-shadow`s). Both are CPU filters on the main thread: bound them to small elements, pause off-screen, never put them on scrolling content. For anything larger, move to a WebGL shader (OGL, Paper Shaders, Three `ShaderMaterial`).

## 12. Cost table

| Treatment | Safe use | Constrain |
|---|---|---|
| `backdrop-filter` glass | Nav bar, one floating panel, toasts | Count, area, iOS; solid fallback |
| Large `filter: blur()` ambient blobs | 2–3 blurred gradient divs drifting 20–40 s | `will-change: transform` on those only; pause off-screen |
| SVG filters (goo, displacement, live grain) | Small elements, hero accent | Never on scroll paths or full viewport |
| Shader backgrounds | Hero canvas | Cap DPR at 1.5–2, pause when hidden, poster fallback |
| Multi-layer shadows | Static elevated surfaces | Never animated |
| Spotlight / specular borders | Bento grids on fine-pointer devices | One listener, cached rects, touch disabled |
