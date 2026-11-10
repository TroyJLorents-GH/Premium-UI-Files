# AETHER // 120Hz UI/UX & Motion Engineering Lab — Section-by-Section Guide

This guide breaks down every section, interactive sandbox, and global system inside the **AETHER Motion Engineering Lab** (`index.html`). For each component, you will find:
1. **UX & Visual Goal:** Why the pattern feels premium.
2. **What We Used (Vanilla / Native Stack):** The exact HTML, CSS, SVG, and JavaScript APIs powering the live demo.
3. **Core Mechanics & Math:** The underlying formulas, easing curves, or compositor properties.
4. **Production Framework Equivalents:** What libraries to reach for when building this in React, Next.js, Vue, or native mobile apps.

---

## Table of Contents

1. [Global Foundation: Surface Optics, Lighting & The Master RAF Loop](#1-global-foundation-surface-optics-lighting--the-master-raf-loop)
2. [Global HUD & Tooling: 120Hz Telemetry Pill, Cmd+K Palette & Code Inspector](#2-global-hud--tooling-120hz-telemetry-pill-cmdk-palette--code-inspector)
3. [Header: Morphing Dynamic Island Navbar & Shared-Layout Sliding Pill](#3-header-morphing-dynamic-island-navbar--shared-layout-sliding-pill)
4. [Section 00 (Hero Lab): Kinetic Typography, Variable Fonts, Magnetic CTAs & Vector/ASCII Field](#4-section-00-hero-lab-kinetic-typography-variable-fonts-magnetic-ctas--vectorascii-field)
5. [Section 01 (Bento Workbench): Spotlight Borders, Specular Glass, 3D Tilt, Springs & SVG Goo](#5-section-01-bento-workbench-spotlight-borders-specular-glass-3d-tilt-springs--svg-goo)
6. [Sections 02–04 (Scroll Lab): 3D Exploded Stack, Opacity Reading & Velocity Marquee](#6-sections-0204-scroll-lab-3d-exploded-stack-opacity-reading--velocity-marquee)
7. [Section 05 (Micro-Interactions): Morphing Pagination & Optimistic UI + Sonner Toasts](#7-section-05-micro-interactions-morphing-pagination--optimistic-ui--sonner-toasts)
8. [Section 06 (Advanced Spatial & Acoustic Lab): FLIP Engine, Chromatic Lens, iOS Sheet & Web Audio](#8-section-06-advanced-spatial--acoustic-lab-flip-engine-chromatic-lens-ios-sheet--web-audio)
9. [Section 07 (GSAP Pinned Set Piece): Labeled Scrub Timeline, Snap & Live Readout](#9-section-07-gsap-pinned-set-piece-labeled-scrub-timeline-snap--live-readout)
10. [Section 08 (SplitText Hero Choreography): Masked Lines, ScrambleText Eyebrow & Tunable Timeline](#10-section-08-splittext-hero-choreography-masked-lines-scrambletext-eyebrow--tunable-timeline)
11. [Section 09 (Horizontal Pinned Gallery): containerAnimation Triggers & Velocity Skew](#11-section-09-horizontal-pinned-gallery-containeranimation-triggers--velocity-skew)
12. [Section 10 (Navigation Suite): Direction-Aware Header, Section Progress, Morphing Mega Menu & Clip-Path Dialog](#12-section-10-navigation-suite-direction-aware-header-section-progress-morphing-mega-menu--clip-path-dialog)
13. [Section 11 (SVG Storytelling): DrawSVG Route, MotionPath Courier & MorphSVG Parcel](#13-section-11-svg-storytelling-drawsvg-route-motionpath-courier--morphsvg-parcel)
14. [Section 12 (WebGL2 Fragment Shader Hero): One Triangle, Capped DPR, Off-Screen Pause & Poster Fallback](#14-section-12-webgl2-fragment-shader-hero-one-triangle-capped-dpr-off-screen-pause--poster-fallback)
15. [Summary Cheat Sheet: Section-to-Technology Matrix](#15-summary-cheat-sheet-section-to-technology-matrix)
16. [Copy-Paste Prompts for Your Custom UI/UX Skill](#16-copy-paste-prompts-for-your-custom-uiux-skill)

---

## 1. Global Foundation: Surface Optics, Lighting & The Master RAF Loop

Before any individual component renders, the entire page establishes a high-craft dark-mode environment (`#07090E` Obsidian base and `#0D111A` elevated surfaces) using four global techniques:

### A. Inline SVG Fractal Noise Grain Overlay
* **UX & Visual Goal:** Eliminates 8-bit gradient color banding on dark backgrounds and gives frosted glass a physical, anodized texture.
* **What We Used:**
  * A fixed, full-viewport inline `<svg>` with `pointer-events: none` and `opacity: 0.032` ($3.2\%$).
  * `<feTurbulence type="fractalNoise" baseFrequency="0.82" numOctaves="4" stitchTiles="stitch" />` paired with `<feColorMatrix type="saturate" values="0" />` for monochrome grain.

### B. Specular $1\text{ px}$ Hairline Borders (`.specular-border`)
* **UX & Visual Goal:** Standard `border: 1px solid rgba(255,255,255,0.1)` looks flat. A directional gradient border simulates overhead light catching the top-left bevel of cut glass.
* **What We Used:**
  * A `::before` pseudo-element with `padding: 1px` and `background: linear-gradient(135deg, rgba(255,255,255,0.24) 0%, rgba(255,255,255,0.06) 45%, rgba(34,211,238,0.14) 100%)`.
  * Masked strictly to the $1\text{ px}$ perimeter using `-webkit-mask-composite: xor` and `mask-composite: exclude`.

### C. Multi-Layered Ambient Elevation Shadows (`.ambient-shadow`)
* **UX & Visual Goal:** Replaces harsh single drop shadows with photorealistic ambient occlusion and a top-edge inner highlight.
* **What We Used:**
  * Five stacked `box-shadow` declarations with expanding vertical offsets and blur radii (`1px 2px`, `4px 8px`, `12px 24px`, `24px 48px`) plus `inset 0 1px 0 0 rgba(255, 255, 255, 0.12)`.

### D. Master Frame-Rate Independent `requestAnimationFrame` Loop
* **UX & Visual Goal:** Ensures all physics, canvas vectors, and scroll marquees run at the exact same physical speed whether the user is on a $60\text{ Hz}$ laptop, a $120\text{ Hz}$ ProMotion MacBook/iPhone, or a $240\text{ Hz}$ desktop monitor.
* **Core Mechanics & Math:**
  Every frame measures delta time $\Delta t = \min\left(\frac{t_{\text{now}} - t_{\text{last}}}{1000}, 0.064\right)$ and uses exponential decay damping:
  $$\text{damp}(x, target, \lambda, \Delta t) = x + (target - x) \cdot \left(1 - e^{-\lambda \Delta t}\right)$$
* **Since Sections 07–12 were added:** the page has exactly one clock. When GSAP is present, `gsap.ticker.add()` drives this same `animateLoop`, so ScrollTrigger, every tween and the lab's own physics share a single `requestAnimationFrame`; the loop also steps a small `LAB_FRAME_HOOKS` array (the WebGL shader renders from it). Without GSAP the loop falls back to its own `requestAnimationFrame`. GSAP 3.15.1 and six plugins (ScrollTrigger, SplitText, ScrambleText, DrawSVG, MorphSVG, MotionPath) load once from pinned jsDelivr URLs in `<head>`.

### E. Reduced Motion and Cleanup Infrastructure (Sections 07–12)
* **UX & Visual Goal:** Every new section ships a complete composition for `prefers-reduced-motion: reduce`, derived from the full one rather than a kill switch: pinned stages become static boxes with all chapters readable, the gallery becomes a wrapped grid, the hero jumps to its end state, the shader draws one frame.
* **What We Used:**
  * `gsap.matchMedia()` with two contexts per section (`(prefers-reduced-motion: no-preference)` and `reduce`); each context returns a cleanup function, so toggling the OS setting at runtime rebuilds the section.
  * A `LAB_GSAP_CLEANUP` registry and `destroyGsapLabSections()` that revert every matchMedia context, SplitText instance, listener (`AbortController`) and the WebGL context, the equivalent of a route-change teardown.
  * `html.st-snapping { scroll-behavior: auto !important }`, toggled from ScrollTrigger's snap callbacks, so the page's `scroll-smooth` cannot fight the snap tween.

---

## 2. Global HUD & Tooling: 120Hz Telemetry Pill, Cmd+K Palette & Code Inspector

### A. Real-Time Telemetry HUD Pill (`#telemetry-hud`)
* **What It Does:** Floating bottom-left status bar displaying live smoothed **FPS**, frame time ($\Delta t$ in $\text{ms}$), scroll velocity ($\text{px/s}$), and cursor coordinates ($X, Y$).
* **What We Used:**
  * Driven by the master `requestAnimationFrame` loop (`fps = 1 / dt`).
  * Uses `font-variant-numeric: tabular-nums` (`JetBrains Mono`) so rapidly changing digits occupy identical horizontal widths and never cause layout jitter.

### B. `Cmd + K` / `Ctrl + K` Command Palette (`#cmdk-backdrop`)
* **What It Does:** Keyboard-first modal launcher that fuzzy-filters all 22 UI patterns in real time (16 from Sections 00–06, 6 from Sections 07–12), allowing instant navigation (`Enter`) or direct code inspection.
* **What We Used:**
  * Global `window.addEventListener('keydown')` listening for `(e.metaKey || e.ctrlKey) && e.key === 'k'`, plus `ArrowUp`, `ArrowDown`, `Enter`, and `Escape`.
  * **Production Equivalents:** `cmdk` (Paco Coursey), Radix UI Dialog, or KBar.

### C. Slide-Over Live Code Inspector Drawer (`#code-drawer-backdrop`)
* **What It Does:** Clicking any `</>` button slides out a glassmorphic drawer containing the exact, copy-ready CSS/JS snippet for that specific pattern.
* **What We Used:**
  * A centralized `CODE_SNIPPETS` lookup dictionary mapped to each section's key, paired with clipboard copy feedback that triggers a Sonner toast.

---

## 3. Header: Morphing Dynamic Island Navbar & Shared-Layout Sliding Pill

### A. Dynamic Island Scroll-Detaching Header (`#dynamic-navbar`)
* **UX & Visual Goal:** Maximizes screen real estate while scrolling by detaching the full-width top header (`max-w-7xl`) and shrinking it into a floating glassmorphic pill (`max-w-4xl mt-3 rounded-full`).
* **What We Used:**
  * Passive scroll listener checking `window.scrollY > 60` (plus a manual state-machine override button: `Morph: Auto | Pill | Full`).
  * Smooth CSS interpolation using `transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)]` and `backdrop-blur-xl`.
  * **Production Equivalents:** Motion (`useScroll` + `useTransform`) or GSAP `ScrollTrigger`.

### B. Shared-Layout Sliding Pill Indicator (`#nav-sliding-pill`)
* **UX & Visual Goal:** Instead of abruptly toggling background colors when hovering navigation links, a single physical highlight pill glides smoothly from tab to tab.
* **What We Used:**
  * Measures the hovered link's `getBoundingClientRect()` relative to `#nav-pill-container` and dynamically updates `width` and `transform: translateX()` with a spring-like bezier (`cubic-bezier(0.22, 1, 0.36, 1)`).
  * **Production Equivalents:** Motion `layoutId="nav-pill"` or Native CSS Anchor Positioning (`anchor-name`).

---

## 4. Section 00 (Hero Lab): Kinetic Typography, Variable Fonts, Magnetic CTAs & Vector/ASCII Field

### A. Cipher / Scramble Text Decode (`#cipher-badge` & Headline)
* **UX & Visual Goal:** Creates a technical, high-craft reveal by rapidly cycling Katakana, binary, and mathematical glyphs before locking into the target string from left to right.
* **What We Used:**
  * Custom JS interval (`22ms` tick) iterating over `targetText.split('')` and substituting unrevealed indices with random characters from `01アイウエオカキクケコ!<>-_\/[]{}—=+*^?#`.
  * **Production Equivalents:** GSAP `ScrambleTextPlugin` or custom React hook.

### B. Masked Staggered Line Reveal (`#hero-headline`)
* **UX & Visual Goal:** Headlines rise cleanly out of invisible horizontal baselines rather than fading in all at once.
* **What We Used:**
  * Each line is wrapped in `<span class="line-mask">` (`overflow: hidden; display: block`) containing `<span class="line-inner">`.
  * `.line-inner` transitions from `transform: translateY(110%); opacity: 0` to `translateY(0%); opacity: 1` using an exponential out curve (`cubic-bezier(0.16, 1, 0.3, 1)`) with staggered `transition-delay` values (`40ms`, `140ms`, `240ms`).
  * **Production Equivalents:** GSAP `SplitText` + timeline stagger, or Motion `variants` with `staggerChildren`.

### C. Live Variable Font Axis & Optical Tracking Scrubber
* **UX & Visual Goal:** Demonstrates how modern Variable Fonts (`Inter` `100..900`) interpolate weight and optical tracking smoothly without loading multiple static `.woff2` files.
* **What We Used:**
  * Three range sliders bound to `fontWeight` (`200` to `900`), `letterSpacing` (`-0.060em` to `+0.080em`), and `lineHeight` (`0.90` to `1.45`).

### D. Magnetic CTA Buttons & Rotating Conic Border Beam
* **UX & Visual Goal:** The primary button features an orbiting laser border beam and physically pulls toward the user's cursor within a $35\text{ px}$ radius.
* **What We Used:**
  * **CSS Houdini `@property --beam-angle`:** Registers a typed `<angle>` custom property so `@keyframes spinBeam` can natively animate `conic-gradient(from var(--beam-angle), ...)` from $0^\circ$ to $360^\circ$ inside a $1.5\text{ px}$ masked border.
  * **Magnetic Pull:** Calculates pointer offset from the button's center:
    $$\Delta x = (x_{\text{pointer}} - x_{\text{center}}) \cdot 0.38, \quad \Delta y = (y_{\text{pointer}} - y_{\text{center}}) \cdot 0.38$$
    and applies `translate3d(dx, dy, 0)`, snapping back to $(0,0,0)$ on `mouseleave`.

### E. Interactive Hero HTML5 Canvas (`#hero-vector-canvas`)
* **UX & Visual Goal:** Replaces a static hero image with a $120\text{ fps}$ interactive vector and ASCII shader field that reacts to pointer proximity and click shockwaves.
* **What We Used:**
  * High-DPI HTML5 `<canvas>` scaled by `window.devicePixelRatio`.
  * Computes a $26\text{ px}$ grid of nodes. Nodes within $145\text{ px}$ of the damped cursor rotate toward the pointer via $\theta = \text{atan2}(\Delta y, \Delta x)$ and dynamically swap from vector needles into glowing ASCII glyphs (`+`, `×`, `◈`, `0`, `1`, `∆`). Clicking launches an expanding radial shockwave ring ($r += 340 \cdot \Delta t$).

---

## 5. Section 01 (Bento Workbench): Spotlight Borders, Specular Glass, 3D Tilt, Springs & SVG Goo

### A. Bento Grid Cursor-Tracked Radial Border Spotlight (`#bento-grid`)
* **UX & Visual Goal:** As your cursor moves anywhere across the Bento grid, nearby card borders illuminate like metallic edges catching a flashlight, even before the cursor enters a card.
* **What We Used:**
  * A single `mousemove` listener on `#bento-grid` calculates each card's relative coordinates (`e.clientX - rect.left`, `e.clientY - rect.top`) and sets `--mouse-x` and `--mouse-y` CSS variables on every `.bento-card`.
  * `.bento-card-border` renders `radial-gradient(360px circle at var(--mouse-x) var(--mouse-y), rgba(34,211,238,0.75), ...)` masked to a $1\text{ px}$ border via `mask-composite: exclude`.

### B. Card A — Specular Glassmorphism & Acrylic Tuner (`#glass-specimen`)
* **UX & Visual Goal:** Shows why basic `backdrop-filter: blur()` looks dull on dark UIs unless paired with color saturation boosting (`saturate(190%)`), a specular top-edge highlight, and frost grain.
* **What We Used:**
  * Floating aurora background orbs animated via CSS keyframes (`auroraFloat1`, `auroraFloat2`).
  * Four live sliders dynamically updating `backdrop-filter: blur(Xpx) saturate(Y%)`, `box-shadow: inset 0 1px 0 0 rgba(255,255,255,Z)`, and internal radial grain opacity.

### C. Card B — 3D Perspective Tilt & Multi-Depth Z Parallax (`#tilt-card`)
* **UX & Visual Goal:** Gives cards physical mass and depth by tilting them toward the pointer in 3D space while internal badges float at different $Z$ elevations.
* **What We Used:**
  * Stage wrapper with `perspective: 1000px` and card with `transform-style: preserve-3d`.
  * Normalizes pointer position to $[-0.5, 0.5]$ and maps to $\text{rotateY} = n_x \cdot 26^\circ$ and $\text{rotateX} = -n_y \cdot 26^\circ$.
  * Inner layers use `transform: translateZ(28px)` and `translateZ(52px)` so they shift with true 3D parallax, paired with a dynamic radial glare overlay.
  * **Production Equivalents:** `vanilla-tilt.js`, Aceternity 3D Card, or React Spring.

### D. Card C — Hooke's Law Spring Physics Solver vs. Fixed CSS Easing
* **UX & Visual Goal:** Proves why modern UI frameworks use spring physics instead of fixed CSS durations (`0.65s ease-in-out`). Clicking target nodes rapidly mid-flight shows how the spring puck preserves momentum and arcs naturally into the new target, whereas CSS easing abruptly resets its velocity curve.
* **Core Mechanics & Math:**
  Uses semi-implicit Euler integration inside the master RAF loop:
  $$F_{\text{spring}} = -k \cdot (x - x_{\text{target}}), \quad F_{\text{damp}} = -c \cdot v$$
  $$a = \frac{F_{\text{spring}} + F_{\text{damp}}}{m}, \quad v_{t+1} = v_t + a \cdot \Delta t, \quad x_{t+1} = x_t + v_{t+1} \cdot \Delta t$$
* **What We Used:**
  * Custom JS spring solver driving `#spring-puck` via `translate3d()`, compared against `#css-puck` (`transition: transform 650ms ease-in-out`), plus a live HTML5 `<canvas>` plotting the 140-frame rolling displacement wave $x(t)$.
  * **Production Equivalents:** Motion (`type: "spring", stiffness, damping, mass`), `react-spring`, or SwiftUI `.spring()`.

### E. Card D — SVG Motion: Liquid Gooey Metaballs & Stroke-Dashoffset Blueprint
* **UX & Visual Goal:** Demonstrates two distinct SVG capabilities: organic liquid mercury fusion and geometric blueprint line drawing.
* **What We Used:**
  * **Tab 1 (Liquid Gooey Metaballs):** Applies `filter: url(#liquid-goo-filter)` to a parent container. The SVG filter blurs the children (`<feGaussianBlur stdDeviation="13">`) and passes the result through a high-contrast alpha `<feColorMatrix values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 24 -10">`. That `24 -10` alpha multiplier sharpens the blurred edges back into a crisp boundary, causing nearby circles to bridge and melt together like liquid mercury.
  * **Tab 2 (Stroke-Dashoffset Blueprint):** Sets `stroke-dasharray` to each `<path>`'s total length ($520$, $460$, $145$) and scrubs `stroke-dashoffset = totalLength * (1 - progress)`.
  * **Production Equivalents:** GSAP `DrawSVGPlugin`, GSAP `MorphSVGPlugin`, or Rive.

---

## 6. Sections 02–04 (Scroll Lab): 3D Exploded Stack, Opacity Reading & Velocity Marquee

### A. Section 02 — Scroll-Scrubbed 3D Exploded Hardware & UI Stack
* **UX & Visual Goal:** Replicates Apple and Linear hardware/architecture teardowns where scrolling separates a component into stacked 3D isometric layers.
* **What We Used:**
  * Isometric container using `perspective: 1200px`, `transform-style: preserve-3d`, and `transform: rotateX(56deg) rotateZ(-34deg)`.
  * Scroll listener calculates normalized viewport progress $p \in [0, 1]$ (with a manual range slider override) and translates the four planes along the $Z$-axis:
    $$Z_1 = -90p\text{ px}, \quad Z_2 = 0\text{ px}, \quad Z_3 = +90p\text{ px}, \quad Z_4 = +180p\text{ px}$$
  * **Production Equivalents:** GSAP `ScrollTrigger` (`scrub: true`), Three.js / React Three Fiber, or Native CSS `animation-timeline: view()`.

### B. Section 03 — Scroll-Scrubbed Per-Word Opacity Reading
* **UX & Visual Goal:** Guides the reader's eye down long-form manifesto or editorial copy by illuminating words from dim grey (`0.15` opacity) to crisp white (`1.0` opacity) as they scroll.
* **What We Used:**
  * Splits the paragraph into individual `<span>` word nodes on load.
  * On scroll (or slider scrub), computes each word's normalized index threshold $w_i = i / N$ and clamps opacity:
    $$\alpha_i = \text{clamp}\Big(0.15, \; 1.0, \; 0.15 + (p - w_i) \cdot 5.5 \cdot 0.85\Big)$$

### C. Section 04 — Velocity-Reactive Kinetic Marquee
* **UX & Visual Goal:** An infinite horizontal text ticker that senses how fast the user flicks their scroll wheel—accelerating up to $7\times$ speed and dynamically skewing (`skewX`) into the motion before settling smoothly back to $0^\circ$ at rest.
* **What We Used:**
  * Computes instantaneous scroll velocity $v_{\text{scroll}} = \frac{\Delta\text{scrollY}}{\Delta t}$ inside the master RAF loop and smooths it via exponential damping.
  * Translates a duplicated flex track modulo half its scroll width ($\text{offset} \bmod \frac{W}{2}$) and applies `transform: translate3d(offset, 0, 0) skewX(skewDeg)`.

---

## 7. Section 05 (Micro-Interactions): Morphing Pagination & Optimistic UI + Sonner Toasts

### A. Pattern 01 — Morphing Pagination Pill Carousel
* **UX & Visual Goal:** Instead of static carousel dots, the active indicator stretches horizontally from a $10\text{ px}$ circle (`w-2.5`) into a $40\text{ px}$ pill track (`w-10`) while a gradient progress bar fills inside it in real time.
* **What We Used:**
  * Width morphing via `transition-all duration-300 ease-[cubic-bezier(0.22,1,0.36,1)]`.
  * Autoplay fill driven by the master RAF loop (`slideProgress += dt * 24`), pausing automatically on `mouseenter`.
  * **Production Equivalents:** Embla Carousel + Motion layout animations.

### B. Pattern 02 — Inline Button State Morphing & 3D Stacked Sonner Toasts
* **UX & Visual Goal:** Eliminates jarring layout shifts when submitting forms or deploying builds, and stacks notifications cleanly in 3D space.
* **What We Used:**
  * **Inline Width Morphing:** Animates explicit button widths (`215px` Idle $\rightarrow$ `148px` Compiling Spinner $\rightarrow$ `195px` Emerald Success Badge) with `cubic-bezier(0.22, 1, 0.36, 1)` and **Optimistic UI** state updates ($0\text{ ms}$ perceived latency).
  * **Sonner Stacked Toasts (`#toast-viewport`):** Manages an array of toast DOM nodes in the bottom-right corner. By default, older toasts tuck behind the newest toast using:
    $$\text{translateY} = -11i\text{ px}, \quad \text{scale} = 1 - 0.055i$$
    Hovering the stack flips `toastStackExpanded = true`, fanning all toasts vertically (`translateY = -76i px`, `scale = 1`).
  * **Production Equivalents:** `sonner` (Emil Kowalski) + Motion `AnimatePresence`.

---

## 8. Section 06 (Advanced Spatial & Acoustic Lab): FLIP Engine, Chromatic Lens, iOS Sheet & Web Audio

### A. Lab 06A — FLIP Shared-Element Layout Projection Engine (`performFlipAnimation`)
* **UX & Visual Goal:** CSS cannot natively animate `grid-template-columns`, flex order, or DOM node re-parenting. The **FLIP** (*First, Last, Invert, Play*) technique makes arbitrary layout changes and list shuffles glide seamlessly at $120\text{ fps}$.
* **What We Used & How It Works:**
  1. **First:** Measures every card's initial bounding box via `el.getBoundingClientRect()` before changing classes or DOM order.
  2. **Last:** Applies the new layout class (`2x2 Bento Grid`, `Linear Stack`, `Spotlight Split`, or random array shuffle) and immediately measures the new `getBoundingClientRect()`.
  3. **Invert:** Calculates the position and scale deltas:
     $$\Delta x = x_{\text{first}} - x_{\text{last}}, \quad \Delta y = y_{\text{first}} - y_{\text{last}}, \quad s_w = \frac{w_{\text{first}}}{w_{\text{last}}}, \quad s_h = \frac{h_{\text{first}}}{h_{\text{last}}}$$
     and applies `translate3d(dx, dy, 0) scale(sw, sh)` with `transition: none` so the cards appear to have not moved yet.
  4. **Play:** Forces a synchronous browser reflow (`void stage.offsetHeight`) and on the next `requestAnimationFrame` transitions every card back to `translate3d(0, 0, 0) scale(1, 1)` over `0.55s cubic-bezier(0.22, 1, 0.36, 1)`.
  * **Production Equivalents:** GSAP `Flip` plugin, Motion `layout` / `layoutId` prop, or the Native Browser **View Transitions API** (`document.startViewTransition()`).

### B. Lab 06B — Chromatic Dispersion & Liquid Glass Refraction Lens
* **UX & Visual Goal:** Simulates thick optical glass that bends background pixels and splits red/cyan color channels (chromatic aberration) near the edges.
* **What We Used:**
  * Inline SVG filter `#chromatic-liquid-lens` chaining `<feTurbulence type="fractalNoise" baseFrequency="0.025">` into `<feDisplacementMap in="SourceGraphic" in2="noise" scale="28" xChannelSelector="R" yChannelSelector="G" />`.
  * Moving the cursor updates the lens puck's `translate3d` position and dynamically modulates the turbulence `baseFrequency`, while dual opposing `text-shadow` offsets (`-3px 0 rgba(244,63,94,0.85), 3px 0 rgba(34,211,238,0.85)`) simulate RGB dispersion.
  * **Production Equivalents:** Three.js / React Three Fiber `MeshTransmissionMaterial` (`@react-three/drei`) or custom GLSL fragment shaders.

### C. Lab 06C — iOS / `Vaul` Gesture Bottom Sheet & Logarithmic Rubber-Banding
* **UX & Visual Goal:** Replicates native iOS modal sheet physics where the background app scales back into depth (`scale(0.92)` + `20px` rounded corners) and pulling the sheet past its limit applies diminishing rubber-band resistance.
* **Core Mechanics & Math:**
  Implements Apple's logarithmic rubber-banding formula:
  $$f(x) = \left(1 - \frac{1}{\frac{x \cdot c}{d} + 1}\right) \cdot d$$
  where $x$ is raw pull distance, $d = 176\text{ px}$ is the sheet height, and $c = 0.55$ is the resistance constant.
* **What We Used:**
  * Transitions use Apple's signature iOS spring-approximating curve: `cubic-bezier(0.32, 0.72, 0, 1)`.
  * **Production Equivalents:** `vaul` (for React web apps) or `SwiftUI` `.presentationDetents()`.

### D. Lab 06D — Procedural Web Audio UI Synthesizer & Single-File Exporter
* **UX & Visual Goal:** High-craft interfaces pair visual micro-interactions with subtle, sub-$20\text{ ms}$ acoustic feedback without downloading external `.mp3` or `.wav` files.
* **What We Used:**
  * Native Browser **Web Audio API** (`window.AudioContext`).
  * Synthesizes four distinct sounds in real time using `OscillatorNode` (`sine` and `triangle` waves) and `GainNode` with exponential frequency and volume envelopes (`exponentialRampToValueAtTime`):
    * **01 // TICK:** $1850\text{ Hz} \rightarrow 140\text{ Hz}$ sine impulse over $16\text{ ms}$.
    * **02 // SNAP:** $220\text{ Hz} \rightarrow 640\text{ Hz}$ upward pitch-envelope triangle pop over $65\text{ ms}$.
    * **03 // CHIME:** Harmonic fifth glass interval ($587.33\text{ Hz}$ $\text{D}_5$ + $880\text{ Hz}$ $\text{A}_5$).
    * **04 // DEPLOY:** Ascending major triad arpeggio ($\text{C}_4 \rightarrow \text{E}_4 \rightarrow \text{G}_4 \rightarrow \text{C}_5$).

---

## 9. Section 07 (GSAP Pinned Set Piece): Labeled Scrub Timeline, Snap & Live Readout

### A. Pinned Stage That Fits the Viewport (`#pin-stage`)
* **UX & Visual Goal:** The scroll set piece every expressive page needs: the stage holds still for 300% of viewport travel while one request travels through four stages and the copy changes chapter by chapter. The reader controls the pace; the figure makes the product's idea physical.
* **What We Used:**
  * `ScrollTrigger` with `pin: true`, `start: "top 80px"` (under the fixed header), `end: "+=300%"`, `scrub: 0.8`, `anticipatePin: 1`, `invalidateOnRefresh: true`.
  * Stage CSS `height: calc(100dvh - 6.5rem); overflow: clip` (`dvh`, never `vh`); on phones a `grid-rows-[minmax(0,1fr)_auto]` grid puts the figure above the stacked chapters, with `pb-16` so the fixed telemetry HUD never covers the last line.
  * **Production Equivalents:** GSAP ScrollTrigger (as built), Motion `useScroll` + `useTransform` with a sticky stage, or native CSS `animation-timeline: view()` for the non-pinned parts.

### B. One Labeled Timeline, Four Actors
* **What We Used:**
  * A single `gsap.timeline({ defaults: { ease: "none" } })`: tweens inside are linear and the scrub supplies the easing. Actors: the packet (`x` 0 → 480 over 3 s), the lit track (`stroke-dashoffset` 1 → 0 with `pathLength="1"`), node rings and cores (`scale`, `stroke`, `fill` at each label), chapter copy (`autoAlpha`, `y`), the progress rail (`scaleX`) and the grid (`y` parallax).
  * Labels `ingress`, `auth`, `compute`, `egress` at 0, 1, 2, 3 s and `settled` at 4 s.
* **Core Mechanics & Math:**
  * Chapter $i$ finishes entering **at** its label: fade-in from $i - 0.27$, previous chapter out at $i - 0.5$. Snap rests exactly on labels, so a `fromTo` that *starts* at the label would leave the rest position with no copy.
  * Readout label $= \text{previousLabel}(p \cdot D + 0.001)$ where $p$ is ScrollTrigger progress and $D$ the timeline duration; `currentLabel()` would lag by the scrub duration.

### C. Snap to Labels Without Fighting Smooth Scroll
* **What We Used:** `snap: { snapTo: "labels", inertia: false, duration: { min: 0.2, max: 0.6 }, delay: 0.1, ease: "power1.inOut" }`. `inertia: false` makes the snap go to the nearest label; with inertia a fast flick projects to the end. The snap's `onStart`/`onInterrupt`/`onComplete` toggle `html.st-snapping` because the page's `scroll-behavior: smooth` would otherwise smooth every `scrollTo` the snap tween writes.
* **Reduced Motion:** `.is-static` on the stage (height auto, chapters `position: static`), figure at its end state, readout reads `static / 100%`, no pin.

---

## 10. Section 08 (SplitText Hero Choreography): Masked Lines, ScrambleText Eyebrow & Tunable Timeline

### A. Six Actors on One Labeled Timeline (`#st-stage`)
* **UX & Visual Goal:** The working form of the hero recipe: the figure leads, type follows 350 ms later, the CTA lands last, everything on one timeline that can be replayed, retimed and reversed.
* **What We Used:**
  * `SplitText.create("#st-headline", { type: "lines", mask: "lines", autoSplit: true, onSplit })`; the returned timeline is reverted and rebuilt by SplitText on every re-split (resize).
  * Masks padded from JS: `padding-block: 0.14em; margin-block: -0.14em`, so ascenders and descenders survive the reveal; lines travel `yPercent: 120` so the padding never leaks a glyph before its cue.
  * `ScrambleTextPlugin` on the eyebrow (`chars: "01<>-_/[]{}=+*^?#"`, `speed: 0.6`, `revealDelay: 0.1`) with the real text in an `aria-label` on the wrapper; a tabular counter tweened 0 → 23; five bars `scaleY` from 0; CTA pair and hairline last.
  * Labels: `figure` at 0, `type` at `figure+=0.35`, `cta` at `type+=0.45`. Total about 1.43 s; headline legible by about 0.65 s.
  * **Production Equivalents:** GSAP SplitText (as built), Motion `variants` with `staggerChildren` and a masked line component, or CSS `@starting-style` for a one-shot version.

### B. Live Controls
* **What We Used:** A stagger slider (0.03–0.22 s) and an ease select (`expo.out`, `power4.out`, `back.out(1.4)`, and `power2.inOut` as the deliberately wrong curve for comparison). Changing either rebuilds the timeline and plays it from 0; the total and the legibility time are recomputed from `tl.duration()` and the `type` label.
* **Reduced Motion:** lines set to `yPercent: 0, autoAlpha: 1`, eyebrow written directly, counter at 23, and a 150 ms stage fade acknowledges a replay.

---

## 11. Section 09 (Horizontal Pinned Gallery): containerAnimation Triggers & Velocity Skew

### A. Vertical Scroll Drives a Horizontal Track (`#hg-stage`, `#hg-track`)
* **UX & Visual Goal:** Five panels read left to right as one journey while the visitor scrolls normally; the stage pins, the track slides.
* **What We Used:**
  * `gsap.to(track, { x: () => -(track.scrollWidth - stage.clientWidth), ease: "none", scrollTrigger: { pin: true, scrub: 1, end: () => "+=" + Math.max(distance, innerHeight), invalidateOnRefresh: true } })`.
  * The pinned stage has `overflow: clip`, so the 2,700 px track never leaks into `document.documentElement.scrollWidth` (the 390 px overflow check passes).
  * **Production Equivalents:** GSAP ScrollTrigger `containerAnimation` (as built); Motion `useScroll` with a sticky container and `useTransform` for `x`; Lenis + ScrollTrigger for a smoothed version.

### B. Nested Triggers Inside the Moving Track
* **What We Used:** Each panel's shape (`rotate -14 → 0`, `scale 0.82 → 1`) and caption (`y 28 → 0`, `autoAlpha 0 → 1`) have their own `ScrollTrigger` with `containerAnimation: scroll` and `start: "left 85–90%", end: "left 35–45%"`, measured against the horizontal tween instead of the window. The container tween must be linear and horizontal-only; nested triggers must not pin.

### C. Velocity Skew Without a Second Loop
* **Core Mechanics & Math:** On the pin's `onUpdate`, $\text{skew} = \text{clamp}(-10, 10, v / -250)$ from `self.getVelocity()`. If $|\text{skew}|$ exceeds the current proxy value, the proxy is set and a 0.7 s `power3` tween decays it back to 0, writing `skewX` through a `quickSetter` on the media boxes only, so the captions stay legible.
* **Reduced Motion:** `.is-static` turns the track into a wrapped grid (`repeat(auto-fit, minmax(240px, 1fr))`), captions and shapes at their end state, no pin, no skew.

---

## 12. Section 10 (Navigation Suite): Direction-Aware Header, Section Progress, Morphing Mega Menu & Clip-Path Dialog

### A. Hide on Scroll Down, Reveal on Scroll Up (`#ns-mini-header`)
* **UX & Visual Goal:** The chrome leaves while the reader moves forward and returns on any backward intent; the rule is direction, not distance, so a pause never loses the navigation.
* **What We Used:**
  * `ScrollTrigger.create({ scroller: "#ns-scroller", start: 0, end: "max", onUpdate })`: `self.direction === 1 && self.scroll() > 48` hides (`yPercent: -100`, 380 ms `power3.out`, `overwrite: true`), anything else reveals. The demo lives in a 360 px scroller so it can coexist with the lab's own fixed header; on a real page omit `scroller`.
  * `focusin` on the header reveals it immediately: a hidden header must never hold keyboard focus (WCAG 2.4.11). Two buttons scroll the panel ±260 px for keyboard and assistive users; a polite live region reports the state.

### B. Page Progress Bar and Section Rail (`#ns-progress`, `#ns-rail`)
* **What We Used:** The page bar is `scaleX(self.progress)`. One `ScrollTrigger` per section (`start: "top 55%", end: "bottom 55%"`) sets the matching rail button's `aria-current` in `onToggle` and its 1 px fill `scaleX` in `onUpdate`; the buttons scroll to their section (`behavior: "auto"` under reduced motion).

### C. Morphing Mega Menu (`#ns-mega`)
* **UX & Visual Goal:** One panel that reshapes itself between Product, Solutions and Company, with a caret that slides under the active trigger.
* **Core Mechanics:** Open or switch measures the target content once (`width/height: auto`, one `offsetWidth`/`offsetHeight` read), then a single 320 ms `power3.out` tween morphs `width` and `height`, the content crossfades (`autoAlpha`, 6 px `y`) and the caret tweens `x` to the trigger's centre. A one-shot size morph on a state change is the acceptable exception to transform-only animation.
* **Keyboard & Focus:** Tab to a trigger, Enter/Space toggles, ← → move between triggers and switch the open panel, ↓ moves focus into the panel's first link, Esc closes and refocuses the trigger, `focusout` outside the nav closes, hover opens only when `(hover: hover) and (pointer: fine)`. Content visibility is toggled with inline `display` because the `hidden` attribute loses to Tailwind's `grid`/`flex` utilities.
* **Production Equivalents:** Radix / Base UI NavigationMenu with Motion `layout`, or GSAP `Flip` for the size morph.

### D. Full-Screen Clip-Path Menu From the Click Point (`#ns-overlay-menu`)
* **What We Used:**
  * A native `<dialog>` opened with `showModal()`: top layer, focus trap, inert page, Esc, and focus restored to the opener on close. CSS resets the UA sizing (`position: fixed; inset: 0; width: 100vw; height: 100dvh; max-width: none; max-height: none; margin: 0`).
  * `clip-path: circle(0 at X Y) → circle(R at X Y)` over 0.7 s `expo.out`, where $(X, Y)$ is the pointer for a click and the button's centre for keyboard activation (`event.detail === 0`), and $R = \sqrt{\max(X, W - X)^2 + \max(Y, H - Y)^2} + 24$. Links stagger in 60 ms apart from 0.18 s.
  * Esc is routed through the dialog's `cancel` event (`preventDefault`, animated close, then `dialog.close()`), and the exit reads the circle origin back from the computed `clip-path`.
* **Reduced Motion:** 120–150 ms fades, no size morph, `clip-path: none`.

---

## 13. Section 11 (SVG Storytelling): DrawSVG Route, MotionPath Courier & MorphSVG Parcel

### A. One Scroll-Driven Scene, Three Plugins (`#story-stage`, `#story-svg`)
* **UX & Visual Goal:** A small story rather than a demo: a route is drawn from the depot, a courier follows it, the parcel changes shape at the hub and again at the door, and only then do the place names appear. Nothing here repeats the Card D dashoffset blueprint: lengths are measured, the courier moves along the geometry, and the shape itself changes.
* **What We Used:**
  * `DrawSVGPlugin`: `fromTo("#story-route", { drawSVG: "0%" }, { drawSVG: "100%" })` over 0–5 s of an 8.4 s timeline; `vector-effect: non-scaling-stroke` keeps the stroke 3 px.
  * `MotionPathPlugin`: the courier (`autoRotate: true`) and the parcel wrapper follow `#story-route` with `align` and `alignOrigin: [0.5, 0.5]` from 0.6 s, so they trail the pen; both sample by distance, as DrawSVG does by length, so they never overtake it.
  * `MorphSVGPlugin`: `#story-parcel` morphs box → rounded parcel at 2.9 s and parcel → hexagonal seal at 5.3 s, with a `scale` pulse (`yoyo`) on arrival. The target shapes are hidden `<path>`s with similar point counts.
  * Pinned with `end: "+=260%"`, `scrub: 0.8`; labels `drawing`, `in-transit`, `delivered` feed the scene readout; stops light as the courier passes; labels fade in at 6.2 s (Move → Settle → Annotate); a 1 s hold keeps the final frame.
  * **Production Equivalents:** GSAP plugins (as built), Rive for a designer-authored state machine, Lottie for a baked sequence.
* **Reduced Motion:** unpinned stage, route fully drawn, courier and parcel placed at the end via a paused `motionPath` tween at `progress(1)`, seal shape set with `morphSVG`, labels and all three chapters visible.

---

## 14. Section 12 (WebGL2 Fragment Shader Hero): One Triangle, Capped DPR, Off-Screen Pause & Poster Fallback

### A. Raw WebGL2 Stage With a Caption Rail (`#shader-stage`, `#shader-canvas`)
* **UX & Visual Goal:** The "stage and caption" hero construction: a full-bleed living material with the headline, copy and CTA in the DOM over it. Light leans toward the pointer; two uniforms are exposed as controls.
* **What We Used:**
  * `canvas.getContext("webgl2", { antialias: false, alpha: false, powerPreference: "low-power", preserveDrawingBuffer: false })`; one fullscreen triangle (`[-1,-1, 3,-1, -1,3]`); a GLSL ES 3.00 fragment shader with uniforms `u_res`, `u_time`, `u_mouse`, `u_speed`, `u_warp`.
  * Domain-warped fbm: $q = \text{fbm}(p + t)$, $r = \text{fbm}(p + w\,q)$, $f = \text{fbm}(p + w\,r)$ with five octaves and a 2×2 rotation-scale matrix per octave; a pointer glow $e^{-9 d^2}$ in cyan with a rose core; a one-line hash dither against banding.
  * `ResizeObserver` sizes the backing store at $\text{DPR} = \min(\text{devicePixelRatio}, 1.5)$; `IntersectionObserver` (threshold 0.05), `visibilitychange` and a Pause button gate rendering; `webglcontextlost` and a null context swap in a CSS-gradient poster in the same palette.
  * Rendering is stepped by the page's single clock (`LAB_FRAME_HOOKS` inside the master loop); the pointer is damped at $\lambda = 10$ on the shared $\Delta t$; `u_mouse` is in device pixels with the y axis flipped to match `gl_FragCoord`.
  * **Production Equivalents:** Three.js `ShaderMaterial` on a full-screen quad, OGL, or React Three Fiber with `@react-three/drei` `shaderMaterial`.
* **Reduced Motion:** exactly one frame is drawn with `u_time` frozen and the pointer ignored; the media-query `change` event re-evaluates at runtime.
* **Cleanup:** disconnect both observers, remove listeners, delete the buffer and program, and call `WEBGL_lose_context.loseContext()`.

---

## 15. Summary Cheat Sheet: Section-to-Technology Matrix

| Lab Section / Feature | Core CSS / SVG / Web API Used | Mathematical / Easing Model | Production Library Equivalent |
| :--- | :--- | :--- | :--- |
| **Global Surface & Grain** | SVG `<feTurbulence>`, `mask-composite: exclude`, multi-layer `box-shadow` | $3.2\%$ fractal noise + $135^\circ$ linear gradient border | Tailwind CSS + Custom Utilities |
| **120Hz Telemetry & RAF Loop** | `requestAnimationFrame`, `performance.now()`, `tabular-nums` | $x + (target - x)(1 - e^{-\lambda \Delta t})$ | GSAP Ticker / Motion `useAnimationFrame` |
| **Dynamic Island & Sliding Pill** | `backdrop-filter`, `getBoundingClientRect()`, `translateX()` | `cubic-bezier(0.16, 1, 0.3, 1)` & `(0.22, 1, 0.36, 1)` | Motion `layoutId` / CSS Anchor Positioning |
| **Hero Typography & Scrubber** | `.line-mask` (`overflow: hidden`), Variable Font `wght`, JS glyph loop | Staggered `40ms / 140ms / 240ms` exponential out | GSAP `SplitText` + `ScrambleTextPlugin` |
| **Conic Beam & Magnetic CTA** | CSS Houdini `@property --beam-angle`, `conic-gradient`, `translate3d` | Pointer proximity pull: $\Delta x \cdot 0.38, \Delta y \cdot 0.38$ | Magic UI / Aceternity Border Beam |
| **Hero Vector / ASCII Canvas** | HTML5 2D `<canvas>`, `devicePixelRatio` scaling | $\theta = \text{atan2}(\Delta y, \Delta x)$ + radial shockwave | Three.js / PixiJS / Custom GLSL Shader |
| **Bento Cursor Spotlights** | CSS Custom Properties `--mouse-x`, `--mouse-y` + `radial-gradient` | $360\text{ px}$ masked border circle + $550\text{ px}$ glow | Radix / Tailwind Spotlight Pattern |
| **Card A: Specular Glass Tuner** | `backdrop-filter: blur() saturate()`, `inset` top highlight | Variable blur ($0\text{--}40\text{ px}$) & saturation ($100\text{--}300\%$) | Apple macOS / visionOS Acrylic Spec |
| **Card B: 3D Perspective Tilt** | `perspective: 1000px`, `preserve-3d`, `rotateX/Y`, `translateZ` | Normalized pointer $[-0.5, 0.5] \times 26^\circ$ | `vanilla-tilt.js` / React Spring 3D |
| **Card C: Spring Physics Engine** | Semi-implicit Euler solver + live 2D `<canvas>` oscillation graph | Hooke's Law: $F = -kx - cv, \; a = F/m$ | Motion (`Framer Motion`) / `react-spring` |
| **Card D: SVG Goo & Blueprint** | `<feGaussianBlur>` + `<feColorMatrix>`, `stroke-dashoffset` | Alpha threshold `24 -10`; offset $L \cdot (1 - p)$ | GSAP `DrawSVG` / `MorphSVG` / Rive |
| **3D Exploded Scroll Stack** | Isometric `rotateX(56deg) rotateZ(-34deg)` + `translateZ` | Scroll progress $p \in [0, 1] \rightarrow [-90\text{ px}, +180\text{ px}]$ | GSAP `ScrollTrigger` (`scrub: true`) |
| **Scroll Opacity & Marquee** | Per-word `<span>` opacity + `translate3d` + `skewX()` | Velocity $v = \Delta y / \Delta t \rightarrow \text{skewX}(\pm 14^\circ)$ | Lenis Smooth Scroll + GSAP ScrollTrigger |
| **Morphing Dots & Sonner Toasts** | Pill width interpolation + 3D stacked toast transforms | Stack depth: $Y = -11i\text{ px}, \; \text{scale} = 1 - 0.055i$ | `sonner` + Embla Carousel |
| **Lab 06A: FLIP Layout Engine** | `getBoundingClientRect()` pre/post DOM mutation + reflow | $\Delta x, \Delta y, s_w, s_h$ inverted matrix playback | GSAP `Flip` / Browser View Transitions API |
| **Lab 06B: Chromatic Lens** | SVG `<feDisplacementMap>` + RGB split `text-shadow` | Dynamic turbulence frequency + $\pm 3\text{ px}$ RGB offset | Three.js `MeshTransmissionMaterial` |
| **Lab 06C: iOS Bottom Sheet** | Background `scale(0.92)` + `cubic-bezier(0.32, 0.72, 0, 1)` | Rubber-band: $\left(1 - \frac{1}{(x \cdot c / d) + 1}\right) \cdot d$ | `vaul` / SwiftUI Sheet Detents |
| **Lab 06D: Web Audio Synth** | Native `AudioContext`, `OscillatorNode`, `GainNode` | Exponential frequency & gain envelopes ($16\text{--}450\text{ ms}$) | Web Audio API / Howler.js |
| **Section 07: Pinned Set Piece** | GSAP ScrollTrigger `pin`, `scrub: 0.8`, `snap: "labels"`, `gsap.matchMedia()` | Chapter $i$ enters at $i - 0.27$; label $= \text{previousLabel}(p \cdot D)$ | GSAP ScrollTrigger / Motion `useScroll` |
| **Section 08: SplitText Hero** | `SplitText` (`mask: "lines"`, `autoSplit`), `ScrambleTextPlugin`, labeled timeline | Mask pad $0.14\text{ em}$, travel $120\%$; `type` at $+0.35\text{ s}$, `cta` at $+0.45\text{ s}$ | GSAP SplitText / Motion `staggerChildren` |
| **Section 09: Horizontal Gallery** | ScrollTrigger `containerAnimation`, `quickSetter`, `overflow: clip` | $\text{skew} = \text{clamp}(\pm 10^\circ, v / -250)$ decaying over $0.7\text{ s}$ | GSAP ScrollTrigger / Motion `useTransform` |
| **Section 10: Navigation Suite** | ScrollTrigger `direction`, `<dialog>`, `clip-path: circle()`, one-shot size morph | $R = \sqrt{\max(X, W{-}X)^2 + \max(Y, H{-}Y)^2} + 24$ from the press point | Radix / Base UI NavigationMenu + Motion `layout` |
| **Section 11: SVG Storytelling** | `DrawSVGPlugin`, `MotionPathPlugin` (`autoRotate`), `MorphSVGPlugin` | Draw $0\text{--}5\text{ s}$, courier from $0.6\text{ s}$, morphs at $2.9\text{ s}$ and $5.3\text{ s}$, annotate at $6.2\text{ s}$ | GSAP plugins / Rive / Lottie |
| **Section 12: WebGL2 Shader Hero** | Raw WebGL2, one triangle, GLSL ES 3.00, `ResizeObserver`, `IntersectionObserver` | Domain-warped fbm (5 octaves), $\text{DPR} \le 1.5$, pointer damped at $\lambda = 10$ | Three.js `ShaderMaterial` / OGL / R3F |

---

## 16. Copy-Paste Prompts for Your Custom UI/UX Skill

When you drop **both** `index.html` (the live web app) and `aether_lab_section_guide.md` (this breakdown file) into your custom UI/UX skill, you can copy and paste either of the prompts below depending on how detailed you want its response to be:

### Option A: Short & Direct Wording (Polished Version of Your Phrasing)
> "I am attaching two files: `index.html` is our live interactive UI/UX & 120Hz Motion Engineering Lab web app, and `aether_lab_section_guide.md` breaks down what each section feature is along with the exact languages, APIs, math formulas, and motion skills used to build it. Based on everything already covered in the `.md` guide and HTML file, what new high-craft UI/UX sections, interactive sandboxes, or motion engineering features should we add next without duplicating what we already have?"

### Option B: Deep-Dive Engineering Prompt (For Specific Code-Ready Ideas)
> "Attached are `index.html` (our single-file interactive 120Hz UI/UX & Motion Engineering Lab) and `aether_lab_section_guide.md` (the architectural guide listing every section feature and the exact CSS, SVG, Canvas, Web Audio, and JS physics skills used for each).
>
> Please audit the 24 patterns we have already built in the `.md` file (Sections 00–12) and propose **4 to 6 brand-new interactive lab sections** we can add next (`Section 13+`). Focus on cutting-edge UI/UX and motion skills we haven't showcased yet—such as Rive-style interactive state machines, CSS View Transitions API morphs, 2D rigid-body gravity/collision badges, image-sequence scroll scrubbing, scroll-driven CSS `animation-timeline`, or skeletons with optimistic data streaming—and specify the exact HTML/CSS/JS implementation for each (vanilla or GSAP 3.15.1, which is already loaded) so we can add them directly into `index.html`."