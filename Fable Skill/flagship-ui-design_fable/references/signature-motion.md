# Signature motion: the lab catalog

The bundled motion lab (`assets/motion-lab-reference.html`, 5,415 lines, single file; sections 00–06 are vanilla, sections 07–12 use GSAP 3.15.1 with ScrollTrigger, SplitText, ScrambleText, DrawSVG, MorphSVG and MotionPath from pinned jsDelivr URLs) is this skill's core pattern library for expressive surfaces. It is a working page: every effect below runs in a browser as shipped, and the line ranges point at the exact CSS, markup, and JS. Reach for effects by name, take the actor, correct the listed defect, and compose several into a hero sequence and a scroll set piece. Expressive pages (landing, marketing, launch, portfolio, experiential) are required to use at least a hero sequence of several coordinated actors, one scroll-driven set piece, and three or more signature micro-interactions; this file is where those come from.

Sections of the lab: `hero-section` 628–836, `bento-section` 841–1327, `scroll-section` 1332–1563, `micro-section` 1568–1718, `advanced-section` 1723–2134, `pinned-section` (07) 2139–2252, `splittext-section` (08) 2257–2342, `gallery-section` (09) 2347–2429, `nav-section` (10) 2434–2580, `svg-story-section` (11) 2585–2686, `shader-section` (12) 2691–2756, shared CSS 44–437 (07–12 at 328–436), SVG filter defs 445–490, nav 537–622, command palette 2772–2807, GSAP loader 9–16, sections 07–12 JS 4436–5101 (shared clock, `gsap.matchMedia()` contexts, cleanup registry 4436–4478), master loop 5105–5412 (driven by `gsap.ticker` at 5408–5411; frame hooks 5402–5405).

## Contents

1. How to read the lab (take the actors, not the page)
2. Quick pick by job
3. Catalog: type and text
4. Catalog: hero figures and fields
5. Catalog: scroll set pieces
6. Catalog: navigation and shell
7. Catalog: micro-interactions and feedback
8. Catalog: surfaces, filters, and ambience
9. Catalog: physics and the master loop
10. Recipe: a hero sequence from lab actors
11. Recipe: a pinned set piece from lab actors
12. Defects common to the whole lab

## 1. How to read the lab

Take: the actors (what moves, how it is parameterized, the curves and numbers), the single-ticker architecture, the physics helpers, the material parameters.

Do not take:

- **The hero layout.** Lines 629–833 are a 7/5 two-column split: headline left, canvas card right. That is the default layout this skill forbids on expressive surfaces. The actors inside it (masked line reveal, cipher eyebrow, magnetic beam CTA, vector field) are excellent; the arrangement is not. See `SKILL.md` "Hero constructions".
- **The bento frames.** Every effect sits in an identical card with an eyebrow label, a title, a paragraph, and an "Inspect Code" button. That is lab chrome. A product page shows one feature working in one dominant cell, not a row of equal cards.
- **The palette and voice.** Near-black with cyan/indigo/rose and `// SYS.120HZ` mono eyebrows is one direction. Derive your own from the product's concept.
- **The page plumbing.** Tailwind from a CDN, Google Fonts at runtime, `class="scroll-smooth"` on `<html>` (fights Lenis and ScrollTrigger), `overflow-x: hidden` on `<body>` (hides the horizontal-overflow bug instead of fixing it), inline `onclick`/`onmouseenter` handlers, and `document.execCommand("copy")`.

Line numbers refer to the bundled file. When adapting, read the referenced range rather than trusting the summary here.

## 2. Quick pick by job

| Job | Effects (section numbers below) |
|---|---|
| Headline that arrives with weight | Masked staggered line reveal (3.1); for one word, Cipher decode (3.2); as a complete GSAP hero timeline, SplitText hero choreography (3.5) |
| A figure that proves the product does something | Scroll-scrubbed exploded stack (5.1), Stroke trace (4.3), Vector field (4.1), FLIP projection (7.3), SVG story scene (4.5) |
| The hero should respond to the visitor in under a second | Vector field with shockwave (4.1), Variable-axis tuner (3.3), 3D tilt with glare (4.2), Fragment shader stage (4.6) |
| A scroll chapter that makes the concept physical | Pinned labeled set piece with snap (5.4), Exploded stack (5.1), SVG story scene (4.5), Per-word reading illumination (5.2), Stroke trace scrubbed (4.3) |
| A gallery or sequence of panels that should read as one journey | Horizontal pinned gallery with `containerAnimation` (5.5) |
| Scroll should feel like it has mass | Velocity-reactive marquee (5.3), Velocity skew on the gallery (5.5), Spring puck physics (9.1) |
| Primary CTA that feels alive without glowing | Magnetic pull (7.1) with Conic beam (8.3) on one CTA only |
| Navigation with a signature | Dynamic island morph (6.1), Sliding pill (6.2), Command palette (6.3), Scroll-direction header with section progress (6.5), Morphing mega menu (6.6), Clip-path dialog menu (6.7) |
| Feedback that feels engineered | Button state morph (7.4), Stacked toasts (7.5), Morphing pagination (7.2), Procedural UI sound (7.7, opt-in) |
| Surface that reads as expensive | Specular hairline (8.1), Cursor spotlight (8.2), Glass with grain (8.4), Aurora backdrop (8.5) |
| Liquid, optical, playful accent | Gooey metaballs (8.6), Chromatic lens (8.7), Fragment shader stage (4.6) |
| Mobile sheet with real physics | Sheet depth scale and rubber-band (7.6) |

## 3. Catalog: type and text

### 3.1 Masked staggered line reveal

- **Lab**: CSS 203–220 (`.line-mask`, `.line-inner`), markup 666–689, trigger `replayHeroReveal()` 3681–3687, fired at 5123.
- **Communicates**: the headline is set, not typed; weight and intent. The strongest single hero actor.
- **Fits**: every expressive hero; section headings on scroll (once); quiet surfaces only for the page title, under 600 ms.
- **Parameters that work**: `translateY(110%) → 0`, transform 0.95 s and opacity 0.75 s on `cubic-bezier(0.16, 1, 0.3, 1)`, per-line delay 40 / 140 / 240 ms (about 100 ms apart; 30–40 ms for lines under 40 px).
- **Adapt (GSAP SplitText)**:

```js
document.fonts.ready.then(() => {
  const split = SplitText.create("#hero h1", { type: "lines", mask: "lines", linesClass: "line" });
  // Masks are the line boxes; give them room so ascenders and descenders are not clipped
  (split.masks || []).forEach((m) => { m.style.paddingBlock = "0.12em"; m.style.marginBlock = "-0.12em"; });
  gsap.from(split.lines, { yPercent: 120, rotate: 1.5, duration: 0.95, ease: "expo.out", stagger: 0.09 });
});
```

- **Correct**: the lab's mask has `padding-bottom: 0.08em` and no top padding, so at `line-height: 1.07` descenders of g, y, p and the tops of accented capitals are clipped during and after the reveal; use the padding-block/negative-margin pair above and travel 115–120% so the padding does not leak the glyph before the reveal. The lab fires the reveal from a 120 ms `setTimeout` before fonts are ready, so lines measured in the fallback font re-wrap mid-animation; wait for `document.fonts.ready`. `will-change: transform, opacity` is left on forever (line 215); remove after the reveal or let GSAP manage it. Line 675 uses gradient `bg-clip-text` on the second line: a slop tell, drop it. Reduced motion: lines appear at full opacity with no travel.

### 3.2 Cipher decode (scramble)

- **Lab**: badge 636–645, hero word 679–688, JS 3689–3712 (`CIPHER_GLYPHS`, `triggerCipherDecode`).
- **Communicates**: computation resolving into meaning; a system coming online. One short string only (an eyebrow, a stat label, the last word of a headline).
- **Parameters**: tick 22 ms, 0.55 characters resolved per tick (about 40 ms per glyph), left-to-right resolve, spaces untouched.
- **Adapt**:

```js
const GLYPHS = "01<>-_/[]{}=+*^?#";
function decode(el, final, { step = 22, perTick = 0.55 } = {}) {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches || el.dataset.busy) { el.textContent = final; return; }
  el.dataset.busy = "1"; el.setAttribute("aria-label", final);        // assistive tech reads the result, not the noise
  let i = 0;
  const id = setInterval(() => {
    el.textContent = [...final].map((ch, idx) => ch === " " ? " " : idx < i ? ch : GLYPHS[(Math.random() * GLYPHS.length) | 0]).join("");
    if ((i += perTick) >= final.length) { el.textContent = final; delete el.dataset.busy; clearInterval(id); }
  }, step);
}
```

- **Correct**: the lab's glyph set includes katakana and em dashes that change the string width every tick on a proportional font; use a monospace or `tabular-nums` face, or reserve width with `min-inline-size: Nch`. The lab rewrites `textContent` for screen readers every 22 ms; set `aria-label` to the final string (above) or wrap the animating span in `aria-hidden` with a visually hidden copy. GSAP's `ScrambleTextPlugin` (playbook) does the same with `tweenLength` and `chars` options.

### 3.3 Variable font axis and tracking tuner

- **Lab**: markup 696–762, JS 3714–3737 (`updateHeroTypography`): `wght` 200–900, tracking −0.06 to 0.08 em, line-height 0.9–1.45 applied live to the `<h1>`.
- **Communicates**: craft and control; type as an instrument.
- **Fits**: a type foundry, design tool, editor, or any product whose concept is precision. As a hero actor, animate `font-variation-settings: "wght"` from 300 to 760 over the reveal (0.9 s, `expo.out`) rather than exposing sliders, or breathe `wght` ±40 on hover of a display word.
- **Correct**: the lab writes `letterSpacing` and `lineHeight` per input event, which reflows the headline (acceptable for a slider the visitor drags; not for a continuous loop). Animate only `font-variation-settings` and `transform` on anything that runs by itself. Requires a variable font with the axis (`Inter` 100..900 in the lab).

### 3.4 Per-word reading illumination

See 5.2; it is a scroll actor.

### 3.5 SplitText hero choreography (six actors, one labeled timeline)

- **Lab**: Section 08, markup 2257–2342 (stage 2280–2306, controls 2308–2340), JS 4545–4619 (`buildSplitHeroTimeline`, `initSplitHero`, `updateSplitHeroControls`, `replaySplitHero`), snippet `splittext-hero` 3247–3282. Actors on one timeline with labels `figure → type → cta`: five bars rise (`scaleY`) with a tabular counter 0 → 23; three headline lines mask-reveal from `yPercent: 120` 350 ms later; a ScrambleText eyebrow decodes; the CTA pair and a hairline land last. Replayable; stagger (0.03–0.22 s) and ease are live controls; total about 1.4–1.6 s, headline legible by about 0.65 s.
- **Communicates**: the page was composed, not assembled; the figure matters more than the type.
- **Fits**: every expressive hero. This is the working form of recipe §10; swap the bars and counter for the product's own figure.
- **Adapt**:

```js
gsap.registerPlugin(SplitText, ScrambleTextPlugin);
document.fonts.ready.then(() => {
  SplitText.create(".hero h1", { type: "lines", mask: "lines", autoSplit: true, onSplit(self) {
    self.masks.forEach((m) => { m.style.paddingBlock = "0.14em"; m.style.marginBlock = "-0.14em"; });   // room for ascenders/descenders
    return build(self);                                                                              // re-split on resize rebuilds it
  } });
});
function build(split) {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) { gsap.set(split.lines, { yPercent: 0, autoAlpha: 1 }); return gsap.timeline(); }
  return gsap.timeline({ defaults: { ease: "expo.out" } })
    .addLabel("figure").from(".figure .bar", { scaleY: 0, duration: 0.9, stagger: 0.07 }, "figure")
    .addLabel("type", "figure+=0.35").from(split.lines, { yPercent: 120, rotate: 1.2, duration: 0.9, stagger: 0.09 }, "type")
    .to(".eyebrow span", { duration: 0.8, scrambleText: { text: "Shipping since 2019", chars: "01<>-_/[]{}=+*^?#", speed: 0.6 } }, "type")
    .addLabel("cta", "type+=0.45").from(".cta", { autoAlpha: 0, y: 12, duration: 0.5 }, "cta");
}
```

- **Correct**: the lab build waits for `document.fonts.ready`, pads the masks, travels 120% so the padding never leaks a glyph, writes only `transform`/`opacity`, and puts spaces around the headline `<br>`s so SplitText's `aria-label` reads as a sentence. When adapting: keep `autoSplit: true` and return the timeline from `onSplit` (manual re-splits on resize leak the old timeline); keep the eyebrow's real text in an `aria-label` on the wrapper because ScrambleText rewrites `textContent` every frame; the `power2.inOut` option in the lab's ease select is there to show the wrong curve for an entrance, do not ship it; `will-change` is set only on the `.st-line` elements, not left on the page. Cleanup: `tl.kill(); split.revert()` (the lab registers both in `LAB_GSAP_CLEANUP`).

## 4. Catalog: hero figures and fields

### 4.1 Cursor-reactive vector / ASCII field (canvas)

- **Lab**: markup 794–833, mode toggle 3763–3770, setup 5192–5216, render 5334–5406. Grid of 26 px cells; each draws a 6–13 px stroke angled by a slow sine field, re-aimed at the pointer within 145 px; a click emits a shockwave ring expanding at 340 px/s that lifts cells within 36 px of the ring; ASCII mode swaps high-influence cells for glyphs `+ × ◈ 0 1 ∆`. Pointer damped with `damp(…, 14, dt)`.
- **Communicates**: a live field that notices you; sensors, data, signal, computation.
- **Fits**: a full-bleed hero stage (construction "Stage and caption" or "Figure-dominant") for infrastructure, analytics, AI, networking, hardware. Adapt the glyph set and the field function to the concept (arrows for routing, bars for levels, dots for sampling).
- **Correct**: canvas backing store uses raw `devicePixelRatio` (5198–5200): cap at `Math.min(devicePixelRatio, 2)`. The loop runs forever: pause via `IntersectionObserver` and `document.visibilityState`. `fillText` per cell is paint-heavy at 3× DPR; keep the cell count under about 600 on phones or drop to vectors only. Mark the canvas `aria-hidden="true"`, keep the headline and CTA in the DOM. Reduced motion: draw the static field once, no pointer reaction. Touch: the pointer field needs a tap-to-shockwave path (the lab's `click` listener already gives one).

### 4.2 3D perspective tilt with glare and Z-layers

- **Lab**: markup 1000–1056, JS 3799–3823. `perspective: 1000px`, rotation ±13°, children at `translateZ(28 / 52 / 20px)`, glare as a radial gradient at the pointer.
- **Communicates**: a physical card or device in the visitor's hand.
- **Fits**: product cards, a hardware or card-shaped product in the hero, pricing tiers (one tilts, not all).
- **Adapt**:

```js
const rx = gsap.quickTo(card, "rotationX", { duration: 0.5, ease: "power3.out" });
const ry = gsap.quickTo(card, "rotationY", { duration: 0.5, ease: "power3.out" });
card.addEventListener("pointermove", (e) => {
  const r = card.getBoundingClientRect(), nx = (e.clientX - r.left) / r.width - 0.5, ny = (e.clientY - r.top) / r.height - 0.5;
  rx(-ny * 20); ry(nx * 20);
  card.style.setProperty("--gx", `${(nx + 0.5) * 100}%`); card.style.setProperty("--gy", `${(ny + 0.5) * 100}%`);
});
card.addEventListener("pointerleave", () => { rx(0); ry(0); });
```

```css
.card { transform-style: preserve-3d; } .card > * { transform: translateZ(var(--z, 24px)); }
.glare { background: radial-gradient(circle at var(--gx, 50%) var(--gy, 50%), rgb(255 255 255 / .25), transparent 65%); }
```

- **Correct**: the lab sets a 150 ms CSS transition on `transform` and then writes `transform` on every move, so the card lags and judders; use `quickTo` (above) or remove the transition. It rebuilds the glare `background` string per move (paint); drive it with two CSS variables. ±13° is over the 12° ceiling; use ±10°. Gate on `(hover: hover) and (pointer: fine)`.

### 4.3 Stroke trace (`stroke-dashoffset` blueprint)

- **Lab**: markup 1257–1321, JS 3896–3902 (`scrubSvgCircuit`). Three paths with hard-coded `stroke-dasharray` 520 / 460 / 145, gradient stroke, drawn by a slider.
- **Communicates**: a system being wired, a route resolving, a plan being drawn.
- **Fits**: diagrams of how the product works; the hero figure for anything with flow (payments, logistics, pipelines, circuits); scrubbed by scroll as a set piece.
- **Adapt**:

```js
const paths = gsap.utils.toArray("svg.diagram path, svg.diagram circle");
paths.forEach((p) => { const L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = L; });
gsap.to(paths, { strokeDashoffset: 0, ease: "none", stagger: 0.15,
  scrollTrigger: { trigger: "svg.diagram", start: "top 75%", end: "bottom 40%", scrub: 0.6 } });
```

  Or `DrawSVGPlugin` with `drawSVG: "0% 100%"` (playbook). Reveal labels after about 75% of the draw (Move → Settle → Annotate).
- **Correct**: compute lengths with `getTotalLength()` instead of constants (the lab's constants break the moment the path changes). Circles need `pathLength` or `getTotalLength()` too. Keep `vector-effect: non-scaling-stroke` so the stroke stays 3 px when the SVG scales.

### 4.4 FLIP shared-element layout projection

See 7.3; it works as a hero figure when the hero is an arrangement that reorganizes itself.

### 4.5 SVG story scene (DrawSVG route, MotionPath courier, MorphSVG parcel)

- **Lab**: Section 11, markup 2585–2686 (SVG 2617–2664: route, three stops, parcel shapes, courier, labels; chapters 2668–2683), JS 4853–4904 (`initSvgStory`), snippet `svg-story` 3363–3395. One pinned, scrubbed timeline (`end: "+=260%"`, `scrub: 0.8`): `drawSVG` draws the route by true length over 0–5; the courier (`autoRotate`) and the parcel follow the same path from 0.6 so they trail the pen; `morphSVG` turns the box into a parcel at the hub (2.9) and into a seal at the door (5.3); stops light as the courier passes; labels fade in after about 75% (6.2); the final frame holds. Labels `drawing`, `in-transit`, `delivered` feed the scene readout.
- **Communicates**: a plan, then execution, then proof; anything that travels and changes state (deliveries, payments, approvals, build pipelines).
- **Fits**: the scroll set piece for a flow product; as a hero figure, play the first two seconds on load and let scroll take over. Not a repeat of 4.3: this is three plugins telling one story, with the route length measured, not hard-coded.
- **Adapt**: the snippet is complete. Keep all three shapes as `<path>` with similar point counts (`MorphSVGPlugin.convertToPath` for primitives), keep `vector-effect: non-scaling-stroke` on the route, and give the courier and parcel the same `align`/`alignOrigin` so they stay registered.
- **Correct**: in the lab the parcel rides in its own group so the courier can `autoRotate` without rotating the parcel; the first chapter is set visible at time 0 (a `fromTo` at 0 leaves the stage empty before the first scroll); the scene readout is derived from scroll progress (`tl.previousLabel(progress × duration)`), not from `tl.currentLabel()`, which lags by the scrub duration. Reduced motion (`gsap.matchMedia()`): unpinned stage, route fully drawn, courier and parcel placed at the end with a paused `motionPath` tween at `progress(1)`, seal shape, labels and all three chapters visible. On phones the SVG label text is enlarged with a media query because SVG type scales with the viewBox.

### 4.6 WebGL2 fragment shader stage (raw, no library)

- **Lab**: Section 12, markup 2691–2756 (stage 2715–2730 with canvas, poster, caption rail; controls 2733–2754), JS 4906–5101 (`shaderLab`, `SHADER_VERT`, `SHADER_FRAG`, `initShaderHero`, `renderShaderFrame`), snippet `webgl-shader` 3396–3433. One fullscreen triangle; a domain-warped fbm fragment shader with uniforms `u_res`, `u_time`, `u_mouse`, `u_speed`, `u_warp`; pointer damped at λ 10 on the page's shared `dt`; DPR capped at 1.5; `ResizeObserver` sizes the backing store; `IntersectionObserver`, `visibilitychange` and a pause button stop rendering; a CSS-gradient poster replaces the canvas when `getContext("webgl2")` fails or the context is lost; the headline, copy and CTA stay in the DOM over the canvas.
- **Communicates**: light, atmosphere, a material that responds; the "stage and caption" hero construction.
- **Fits**: experiential and launch pages where the product is visual or ambient; never behind body text; one per page.
- **Adapt**: the snippet is complete. Step the render from the single ticker (`gsap.ticker.add` or the master loop's frame hooks, as the lab does at 5402–5405); never start a second `requestAnimationFrame`.
- **Correct**: the render function returns early unless the stage is visible, the tab is shown and the user has not paused, and under reduced motion it draws exactly one frame (`u_time` frozen) and ignores the pointer; `alpha: false`, `antialias: false`, `powerPreference: "low-power"`, `preserveDrawingBuffer: false` keep the cost down; the dither line in the shader kills banding in the dark gradient. Cleanup disconnects both observers, removes listeners, deletes the buffer and program and calls `WEBGL_lose_context.loseContext()`. Watch for: the fbm is five octaves evaluated three times per pixel, so keep the DPR cap and the stage under about 60% of the viewport on phones; `u_mouse` is in device pixels with the y axis flipped to match `gl_FragCoord`.

## 5. Catalog: scroll set pieces

### 5.1 Scroll-scrubbed exploded layer stack

- **Lab**: CSS 244–259, markup 1335–1471, JS 3907–3928 (`updateExplodedStack`), scroll binding 5159–5169. Four planes in an isometric stage (`rotateX(56deg) rotateZ(-34deg)`, `perspective: 1200px`), separating along Z to −90 / 0 / 90 / 180 px as progress goes 0 → 1, with a legend whose readouts track the Z values and a manual scrubber.
- **Communicates**: anatomy; what the product is made of; layers that fit together. The single most reusable set piece in the lab.
- **Fits**: platforms, stacks, hardware, documents with layers, anything with architecture. Swap the plane contents for the product's real layers (a request, a policy, a render pass, a garment's layers).
- **Adapt (pinned, scrubbed, with text chapters)**: see recipe §11.
- **Correct**: the lab drives this from a raw `scroll` listener with `getBoundingClientRect()` per event (layout read per scroll tick) and never pins, so the figure scrolls away while it is still separating; pin with ScrollTrigger (`pin: true, scrub: 0.6, end: "+=250%"`). It sets `transition: transform 0.2s ease-out` on the stack (line 251) which fights scrub; remove. Layer 4 carries `backdrop-blur-md` inside a 3D-transformed subtree (line 1454): expensive and often flattened by the browser; use a translucent fill instead. The legend writes text per scroll event; throttle to `onUpdate` or drop it. On phones the stage must fit copy and figure inside `100dvh`: size the figure with `min(72vw, 48dvh)` and stack chapters below it inside the pinned box.

### 5.2 Per-word reading illumination

- **Lab**: markup 1474–1505, JS 3930–3957 (`initOpacityReadingParagraph`, `updateOpacityReading`), scroll binding 5171–5178. Words at opacity 0.15 rise to 1 as a reading line passes (`delta = (progress − index/total) × 5.5`), and flip color from slate to white above 0.85.
- **Communicates**: being read to; one statement that matters, delivered at reading pace.
- **Fits**: the manifesto sentence between hero and features; the single claim before pricing. One per page.
- **Adapt**:

```js
const split = SplitText.create(".statement", { type: "words" });
gsap.fromTo(split.words, { opacity: 0.15 }, { opacity: 1, ease: "none", stagger: 0.05,
  scrollTrigger: { trigger: ".statement", start: "top 80%", end: "bottom 45%", scrub: true } });
```

- **Correct**: the lab splits with `innerHTML` on a plain string, which destroys inline markup and links; use SplitText or `Intl.Segmenter`. The color flip at 0.85 makes words flicker as the threshold crosses; animate opacity only and keep one color. It runs from a scroll listener with a rect read; ScrollTrigger above. Once fully read the text stays static; never re-dim on backscroll past the end (`scrub` keeps it reversible while in range, which is fine). Reduced motion: opacity 1.

### 5.3 Velocity-reactive kinetic marquee

- **Lab**: markup 1508–1561, loop 5244–5264, impulse 5113–5115. Duplicated track (`aria-hidden` on the copy), base speed 68 px/s, speed boost up to 7× with scroll velocity, `skewX` clamped ±14° from `velocity × 0.008`, damped with λ 10; velocity itself damped λ 14 then λ 10.
- **Communicates**: the page has mass; scrolling is pushing something.
- **Fits**: a proof strip (customers, formats, integrations) or a statement band on expressive pages. Never on quiet surfaces.
- **Adapt**:

```js
let x = 0, skew = 0, half = track.scrollWidth / 2;
addEventListener("resize", () => { half = track.scrollWidth / 2; });
gsap.ticker.add((t, dtMs) => {
  const dt = Math.min(dtMs / 1000, 0.064), v = ScrollTrigger.getVelocity();
  x = (x - (68 + Math.min(400, Math.abs(v) * 0.08)) * dt) % half;
  skew += (gsap.utils.clamp(-14, 14, v * 0.008) - skew) * (1 - Math.exp(-10 * dt));
  track.style.transform = `translate3d(${x.toFixed(1)}px,0,0) skewX(${skew.toFixed(2)}deg)`;
});
```

- **Correct**: the lab reads `track.scrollWidth` every frame (layout read): cache it and refresh on resize (above). It never pauses off-screen or in a hidden tab: toggle the ticker callback from a ScrollTrigger `onToggle` and on `visibilitychange`. Loops longer than 5 s that carry information need a pause control (WCAG 2.2.2); a decorative strip needs pause-on-hover at minimum. Reduced motion: static strip or a slow CSS keyframe with no skew. Read velocity from `ScrollTrigger.getVelocity()` or `lenis.velocity`, never a second scroll listener.

### 5.4 Pinned set piece with a labeled timeline and snap (GSAP)

- **Lab**: Section 07, markup 2139–2252 (stage 2163–2250: readouts, progress rail, SVG figure 2183–2224, four chapters 2227–2249), CSS `.pin-stage`/`.pin-chapter`/`.is-static` 340–383, JS 4480–4543 (`initPinnedSetPiece`), snippet `gsap-pin` 3205–3246. `ScrollTrigger` pins the stage for `end: "+=300%"` with `scrub: 0.8`; one timeline moves four actors (packet `x`, track `strokeDashoffset`, node rings and cores, chapter copy, progress rail `scaleX`, grid `y` parallax); labels `ingress`, `auth`, `compute`, `egress`, `settled` at 0–4 s; `snap: { snapTo: "labels", inertia: false }`; `onUpdate` writes a progress percentage and the current label.
- **Communicates**: a process with stages; the product's idea made physical, one chapter at a time.
- **Fits**: the one scroll set piece every expressive page needs (recipe §11). Replace the packet-and-nodes figure with the concept figure; keep the structure.
- **Adapt**: the snippet is complete; the stage CSS is `height: calc(100dvh - 6.5rem); overflow: clip` with `start: "top 80px"` so the pinned box sits under a fixed header, and on phones the figure row takes `minmax(0, 1fr)` with the chapters stacked below (`grid-rows-[minmax(0,1fr)_auto]`).
- **Correct**: five things the lab build gets right that adaptations usually miss. (1) Chapter *i* finishes entering **at** its label (`fromTo` at `i − 0.27`, previous chapter out at `i − 0.5`), because snapping rests exactly on labels and a `fromTo` that starts at the label leaves the rest position with no copy. (2) The first chapter is `set` visible at 0 so the stage reads before any scroll. (3) The label readout is `tl.previousLabel(self.progress × tl.duration() + 0.001)`, not `tl.currentLabel()`, which lags by the scrub duration. (4) `inertia: false` on the snap: with inertia, a fast flick projects past the next label to the end; nearest-label is what chapters want. (5) The page's `scroll-behavior: smooth` would smooth every `scrollTo` the snap tween writes, so `html.st-snapping { scroll-behavior: auto !important }` is toggled from the snap's `onStart`/`onComplete`/`onInterrupt` (4449–4453); on your own page simply do not ship `scroll-smooth`. Reduced motion: `.is-static` (height auto, chapters `position: static` and visible), figure at the end state, no pin. On phones the bottom padding is `pb-16` so the lab's fixed HUD never covers the last line of copy. Cleanup: `mm.revert()`.

### 5.5 Horizontal pinned gallery with `containerAnimation` and velocity skew

- **Lab**: Section 09, markup 2347–2429 (stage 2371–2427, five panels), CSS `.hg-track`/`.hg-panel`/`.is-static` 389–404, JS 4620–4680 (`initHorizontalGallery`), snippet `horizontal-gallery` 3283–3316. Vertical scroll drives `x: -(track.scrollWidth − stage.clientWidth)` on the track (`scrub: 1`, `end` equals the distance or one viewport, whichever is larger); each panel's shape (`rotate −14 → 0`, `scale 0.82 → 1`) and caption (`y 28 → 0`, `autoAlpha`) have their own triggers with `containerAnimation: scroll` and `start: "left 85–90%"`; scroll velocity skews the media (`skewX` clamped ±10°) through a proxy that decays back to 0 in a 0.7 s `power3` tween, so there is no second frame loop.
- **Communicates**: a journey through stages; a portfolio or product line read left to right.
- **Fits**: feature walks, case-study strips, product line-ups on expressive pages. Quiet surfaces scroll vertically.
- **Adapt**: the snippet is complete. `containerAnimation` requires the container tween to be linear (`ease: "none"`) and horizontal-only, and nested triggers must not pin.
- **Correct**: clip with `overflow: clip` on the pinned stage so the track never leaks into `document.documentElement.scrollWidth` (the lab passes the 390 px overflow check with the track 2,700 px wide); skew the media, not the captions, so text stays legible while it moves; the first panel's triggers are already complete at progress 0 (its left edge is inside the stage), which is correct, not a bug. Reduced motion: `.is-static` turns the track into a wrapped grid (`repeat(auto-fit, minmax(240px, 1fr))`) with captions and shapes at their end state, no pin, no skew. Cleanup: `mm.revert()` kills the container tween and every nested trigger.

## 6. Catalog: navigation and shell

### 6.1 Dynamic island navbar morph

- **Lab**: markup 537–622, JS 3616–3632 (`applyNavbarMorphState`), bound to scroll at 5160. Past 60 px the full-width bar becomes a centered `max-w-4xl` pill with the specular border and ambient shadow; subtitle hides; 500 ms `cubic-bezier(0.16,1,0.3,1)`.
- **Communicates**: the chrome gets out of the way; the product is the page.
- **Fits**: expressive pages and marketing shells. Apps keep a stable header.
- **Correct**: the lab toggles classes on every scroll event; toggle once at a threshold with hysteresis (compact above 80 px, expand below 40 px) from ScrollTrigger `onUpdate` or `scroll-state(stuck)`. The morph animates `max-width`, `padding`, and `border-radius` (layout and paint), acceptable as a one-shot class toggle, not per frame; for compositor-only, morph with `clip-path: inset(… round 999px)` and `transform: scale`. Keep the nav links reachable while compact and never let the pill cover a focused element (WCAG 2.4.11).

### 6.2 Shared-layout sliding pill indicator

- **Lab**: markup 559–588, JS 3654–3676 (`initNavSlidingPill`, `movePillTo`): measures the target rect and writes `width` and `translateX` with a 300 ms `cubic-bezier(0.22,1,0.36,1)` transition.
- **Communicates**: continuity; one object moving between states.
- **Correct**: the pill follows `mouseenter` and never returns on leave, so hovering past the nav leaves it stranded; track the active item separately, move on hover and `focus-visible`, return to active on `pointerleave`/`focusout`. Set `aria-current="page"` on the active link. `transition-all` on the pill: list `transform, width`. Better still: Motion `layoutId`, a View Transition, or CSS anchor positioning (see `page-patterns.md` §3).

### 6.3 Command palette (⌘K)

- **Lab**: markup 2772–2807, JS 3439–3570 (`COMMAND_ITEMS`, filter, arrow keys, Enter, Escape, `⌘/Ctrl+K`).
- **Communicates**: an operator's tool; power under the surface.
- **Fits**: apps, docs, and expressive pages for developer products; as a hero instrument when the product is search or control.
- **Correct**: the lab builds the modal from `div`s with `hidden`/`flex` toggles (no `<dialog>`, no focus trap or restore, no enter/exit animation) and re-renders the list `innerHTML` on every `mouseenter`, which churns focus. Use `<dialog>` + `@starting-style` (150 ms scale 0.97 → 1 and fade) or cmdk / Base UI Combobox; rows are `<button>`s; restore focus to the trigger on close.

### 6.4 Code inspector slide-over

- **Lab**: markup 2812–2852, JS 3575–3609. Lab chrome; reusable only as a drawer skeleton. Same corrections as 6.3; slide from the right over 250 ms with the backdrop fading in step.

### 6.5 Scroll-direction header (hide down, reveal up) with section progress

- **Lab**: Section 10A/10B, markup 2456–2508 (mini header and rail of four `.ns-dot` buttons 2469–2480, scoped scroller 2481–2500, scroll buttons and state readout 2502–2506), JS 4689–4733 in `initNavSuite` (header 4695–4721, rail 4723–4733), snippet `nav-suite` 3317–3362. One `ScrollTrigger.create({ scroller, start: 0, end: "max" })` reports `direction` and `progress`: the header tweens `yPercent` to −100 when scrolling down past 48 px and back to 0 on any upward scroll (380 ms `power3.out`, `overwrite: true`); the progress bar is `scaleX`; one trigger per section drives each dot's `aria-current` (`onToggle`) and its fill (`scaleX` of `progress`). The demo runs inside a 360 px scroller so it can coexist with the lab's own fixed header; on a real page omit `scroller`.
- **Communicates**: the chrome respects the reader; the page knows where you are.
- **Fits**: long-form, docs, marketing pages with a tall nav. Apps keep a stable header.
- **Correct**: the rule is direction, not distance, so a reader who pauses never loses the nav; the header returns on `focusin` (a hidden header must never hold keyboard focus, WCAG 2.4.11) and the rail dots are real `<button>`s with `aria-current`; `scrollTo` uses `behavior: "auto"` under reduced motion and the hide/reveal shrinks to 120 ms. Do not add your own scroll listener for direction; ScrollTrigger already has it. Cleanup: kill the triggers and abort the listeners (the lab uses one `AbortController` for the whole suite).

### 6.6 Morphing mega menu

- **Lab**: Section 10C, markup 2522–2551 (`#ns-mega` with three `aria-expanded` triggers, caret, panel with three contents), JS 4735–4807 (`measure`, `openMega`, `closeMega`, key handling). Opening a panel measures the target content once (`width/height: auto`, one `offsetWidth`/`offsetHeight` read), then tweens the panel's `width` and `height` in a single 320 ms `power3.out` tween per switch while the content crossfades in (`autoAlpha`, 6 px `y`) and the caret slides (`x`) under the active trigger.
- **Communicates**: one surface that reshapes itself; continuity between sections of a product.
- **Fits**: marketing and docs navigation with three to five top-level groups.
- **Correct**: a one-shot size morph on a state change is the acceptable exception to "transform only"; never animate the panel size per frame. Keyboard path in the lab: Tab to a trigger, Enter/Space toggles, ← → move between triggers and switch the open panel, ↓ moves focus into the panel, Esc closes and refocuses the trigger, `focusout` outside the nav closes, hover opens only when `(hover: hover) and (pointer: fine)`. The panel's content visibility is toggled with inline `display`, because the `hidden` attribute loses to Tailwind's `grid`/`flex` utilities (the lab had both panels showing until this was fixed); the whole nav is one relative box tall enough to hold the panel so `pointerleave` does not fire in the gap between bar and panel. Reduced motion: 120 ms fades, no scale or travel.

### 6.7 Full-screen clip-path menu from the click point (`<dialog>`)

- **Lab**: Section 10D, markup 2561–2579 (`<dialog id="ns-overlay-menu">` with four display links and a footer), CSS 409–422, JS 4809–4849 (`openOverlay`, `closeOverlay`), opener `#ns-overlay-open` at 2528. `dialog.showModal()` first (top layer, focus trap, page `inert`, Esc), then `clip-path: circle(0 at X Y) → circle(R at X Y)` over 0.7 s `expo.out`, where `X Y` is the pointer for a click and the button's centre for a keyboard activation (`e.detail === 0`) and `R` is the distance to the farthest viewport corner plus 24 px; links stagger in (`y 36 → 0`, 60 ms apart) from 0.18 s; closing reverses the circle to the same origin (read back from the computed `clip-path`) in 0.45 s and then calls `dialog.close()`, which restores focus to the opener.
- **Communicates**: the menu comes from your hand; a confident, whole-screen gesture.
- **Fits**: expressive pages with few destinations; mobile primary navigation.
- **Correct**: route Esc through the `cancel` event (`preventDefault`, then the animated close) or the dialog closes with no exit; animate `clip-path` only (never `width/height` of a full-screen surface); `autofocus` on the close button so focus is visibly placed; the dialog needs `position: fixed; inset: 0; width: 100vw; height: 100dvh; max-width: none; max-height: none; margin: 0` because UA dialog styles centre and cap it. Reduced motion: `clip-path: none` and a 150 ms fade; links appear in place. Cleanup: kill the timeline and `dialog.close()` if open.

## 7. Catalog: micro-interactions and feedback

### 7.1 Magnetic CTA

- **Lab**: markup 766–791 (`.magnetic-wrap`, `data-magnetic-strength` 0.38 / 0.32), JS 3740–3758: offset from the wrap center × strength, 250 ms transition, reset on leave.
- **Communicates**: the button wants to be pressed; tactile pull.
- **Fits**: the primary CTA and at most one secondary. Fine pointers only.
- **Adapt**:

```js
if (matchMedia("(hover: hover) and (pointer: fine)").matches && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
  document.querySelectorAll("[data-magnetic]").forEach((wrap) => {
    const el = wrap.firstElementChild, s = parseFloat(wrap.dataset.magnetic) || 0.35;
    const x = gsap.quickTo(el, "x", { duration: 0.4, ease: "power3.out" }), y = gsap.quickTo(el, "y", { duration: 0.4, ease: "power3.out" });
    wrap.addEventListener("pointermove", (e) => { const r = wrap.getBoundingClientRect(); x((e.clientX - r.left - r.width / 2) * s); y((e.clientY - r.top - r.height / 2) * s); });
    wrap.addEventListener("pointerleave", () => { x(0); y(0); });
  });
}
```

  Give the wrap `padding: 24–40px` (negative margin to keep layout) so the pull zone extends past the button; the lab's copy promises 35 px of pull but its wrap is the button's own box.
- **Correct**: CSS transition plus per-move writes makes the pull lag the pointer; `quickTo` replaces both. No touch or reduced-motion gate in the lab. Never move the hit target more than about 12 px; the visitor must still land on it.

### 7.2 Morphing pagination pill with autoplay fill

- **Lab**: markup 1583–1655, JS 3962–4035, fill at 5320–5331. Active dot grows 10 → 40 px over 300 ms `cubic-bezier(0.22,1,0.36,1)` and fills left-to-right over about 4.1 s; hover pauses.
- **Communicates**: where you are and how long until the next thing.
- **Adapt**:

```css
.dot { position: relative; height: 10px; width: 10px; border-radius: 999px; overflow: hidden; transition: width .3s var(--ease-out-soft); }
.dot[aria-current="true"] { width: 40px; }
.dot > i { position: absolute; inset: 0; transform-origin: left; transform: scaleX(var(--p, 0)); background: var(--accent); }
```

  Set `--p` from the ticker; one-shot `width` morph on state change is acceptable.
- **Correct**: the lab animates the fill by writing `width` per frame (layout every frame); use `scaleX` above. It re-renders the dots' `innerHTML` on every slide, which drops focus from the dot the visitor just pressed; update attributes instead. Autoplay pauses on hover only: also on `focus-within`, off-screen, hidden tab, and reduced motion, with a visible pause button (WCAG 2.2.2).

### 7.3 FLIP shared-element layout projection

- **Lab**: markup 1743–1862, JS 4175–4248 (`performFlipAnimation`, `switchFlipLayout`, `shuffleFlipCards`, `promoteFlipCard`). First-Last-Invert-Play with `translate3d` + `scale`, 550 ms `cubic-bezier(0.22,1,0.36,1)`, forced reflow via `void stage.offsetHeight`.
- **Communicates**: the same objects, reorganized; nothing appears from nowhere.
- **Fits**: feature grids that reconfigure as the story advances, filtering, promoting a card to a spotlight, a hero that rearranges itself when the visitor picks a use case.
- **Correct**: the lab scales cards non-uniformly (`scale(sw, sh)`), which squashes the text inside during flight; with GSAP `Flip.from(state, { absolute: true, nested: true, scale: false })` the size is animated with width/height once (acceptable for a one-shot layout change) or counter-scale children. `promoteFlipCard` calls `switchFlipLayout` through a synthetic `.click()` after its own FLIP, running two FLIPs on one gesture; do one. Keep focus on the promoted card. Reduced motion: switch instantly.

### 7.4 Inline button state morph (Idle → Working → Done)

- **Lab**: markup 1687–1699, JS 4041–4090. Width 215 → 148 → 195 → 215 px with content swaps, 300 ms `cubic-bezier(0.22,1,0.36,1)`, color change to success, 1.6 s hold, reset.
- **Communicates**: the action is happening here, in the control you pressed.
- **Correct**: the width morph is acceptable once per click (measure the target label, set `width`, swap content with a 120 ms opacity crossfade); never mid-interaction per frame. The lab shows "Deployed in 0ms" on a timer: success must reflect the real result (Non-negotiable 8); show a failure state and keep the label width reserved so the layout does not jump. Disable while busy (the lab does, via `morphBtnBusy`).

### 7.5 Sonner-style stacked toasts

- **Lab**: CSS 291–310, viewport 2762–2767 (`aria-live="polite"`), JS 4092–4170. Newest on top; collapsed stack offsets 11 px × index, scale `1 − 0.055 × index`, opacity `1 − 0.14 × index`, third and beyond hidden; hover fans to 76 px per toast; max 4; auto-dismiss 5.2 s; exit 300 ms scale 0.9 + fade.
- **Fits**: supplemental confirmation on any surface.
- **Correct**: expand on `:focus-within` as well as hover; add swipe-to-dismiss on touch; pause the auto-dismiss timer while hovered or focused; never make a toast the only record of a failure.

### 7.6 Sheet depth scale and logarithmic rubber-band

- **Lab**: markup 1950–2042, JS 4289–4330. Opening the sheet scales the background to 0.92, lifts it 6 px, raises its radius 12 → 20 px, drops opacity to 0.65, on `cubic-bezier(0.32, 0.72, 0, 1)` 500 ms; overscroll uses `(1 − 1 / ((x·c)/d + 1))·d` with c 0.55 and a 0.45 multiplier; release snaps back in 500 ms.
- **Fits**: mobile sheets, filters, and any drag-to-dismiss surface.
- **Correct**: the lab simulates the drag with a slider; implement with pointer events (or Draggable/Observer from the playbook) tracking velocity for the dismiss threshold; make the sheet a `<dialog>` so the background is `inert`; read `d` from the sheet's measured height instead of the constant 176. The background's `border-radius` and `opacity` morph are one-shot and fine.

### 7.7 Procedural UI sound (Web Audio synthesizer)

- **Lab**: Lab 06D, markup 2047–2131 (four trigger buttons, mute toggle, single-file export), JS 4333–4416 (`playProceduralSound`, `toggleGlobalAcousticFeedback`), snippet `audio-synth` 3184–3204; the global hover-tick hook is at 5136–5140. Four sounds are synthesized on demand from `OscillatorNode` + `GainNode` with exponential envelopes, no audio files: **tick** 1850 → 140 Hz sine over 16–18 ms; **snap** 220 → 640 Hz triangle pop over 65 ms; **chime** a D5 + A5 fifth (587.33 + 880 Hz); **confirm** a C4 → E4 → G4 → C5 arpeggio. The `AudioContext` is created lazily on the first user gesture; everything is muted until the visitor opts in.
- **Communicates**: tactility; a physical mechanism under the interface. Paired with a visual micro-interaction it makes feedback feel engineered.
- **Fits**: opt-in only, on experiential sites and instruments (synths, games, configurators); never on hover for a whole page; never autoplay; never the only feedback channel. Keep gains ≤ 0.2 and durations under about 450 ms.
- **Adapt**:

```js
let ctx;
const ac = () => (ctx ??= new (window.AudioContext || window.webkitAudioContext)());   // lazily, inside a user gesture
function tick({ from = 1850, to = 140, ms = 16, gain = 0.12, type = "sine" } = {}) {
  if (!soundEnabled || matchMedia("(prefers-reduced-motion: reduce)").matches) return;   // treat sound like motion: respect the preference
  const t0 = ac().currentTime, osc = ac().createOscillator(), g = ac().createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(from, t0);
  osc.frequency.exponentialRampToValueAtTime(to, t0 + ms / 1000);
  g.gain.setValueAtTime(gain, t0);
  g.gain.exponentialRampToValueAtTime(0.001, t0 + ms / 1000);
  osc.connect(g).connect(ac().destination);
  osc.start(t0); osc.stop(t0 + ms / 1000 + 0.01);
}
```

- **Correct**: the lab attaches a hover tick to every `button` and `a` on the page once enabled (5136–5140): limit sound to the controls that carry meaning (primary actions, toggles, drag thresholds) and never to hover. Create the context lazily and `resume()` it on the first gesture (autoplay policy); the lab creates it on first play, which is right. Expose a visible mute that persists (`localStorage`); default muted. `exponentialRampToValueAtTime` cannot reach 0, hence the 0.001 floor. Treat `prefers-reduced-motion` as the signal to stay silent unless the visitor explicitly enables sound.

## 8. Catalog: surfaces, filters, and ambience

### 8.1 Specular hairline border

- **Lab**: CSS 97–118. Full recipe and parameters in `surfaces-and-materials.md` §7. Use on the nav pill, one hero panel, and toasts; not on every card.

### 8.2 Cursor-tracked radial border spotlight

- **Lab**: CSS 123–165 (`.bento-card::after` glow 550 px radius at 7% alpha; `.bento-card-border` 360 px ring 75% → 35% → 7%), binding 5143–5151. Recipe in `surfaces-and-materials.md` §8.
- **Correct**: the lab calls `getBoundingClientRect()` for every card on every `mousemove` (forced layout × cards); cache rects on resize and `scrollend`, use `pointermove` with `passive: true`, gate on `(hover: hover) and (pointer: fine)`.

### 8.3 Rotating conic border beam

- **Lab**: `@property` 48–52, CSS 170–198: `padding: 1.5px`, `transparent 60% → indigo 82% → cyan 96% → white 100%`, 3.2 s linear. Recipe in `surfaces-and-materials.md` §9. One CTA per screen; pause under reduced motion.

### 8.4 Specular glass with grain (tunable)

- **Lab**: specimen 903–937 (`blur(20px) saturate(190%)`, 42% alpha surface, inset top highlight 45%, 16% border, 4% grain), JS 3775–3794. Recipe in `surfaces-and-materials.md` §6.
- **Correct**: `transition-all duration-75` on the specimen; list properties or remove. Solid fallback under `prefers-reduced-transparency`.

### 8.5 Aurora backdrop orbs

- **Lab**: CSS 225–239 (two orbs, 9 s and 11 s `ease-in-out` infinite, translate ±55 px and scale 0.92–1.22), markup 894–900 (orbs at `blur-2xl`, opacity 0.7–0.75, over a 16 px dot grid).
- **Communicates**: depth and atmosphere behind glass or type.
- **Fits**: behind a hero panel or a pricing card; never full-viewport on phones.
- **Correct**: two or three orbs only, `will-change: transform` on those alone, pause when the section is off-screen (toggle `animation-play-state` from an IntersectionObserver), stop under reduced motion. Add 2–4% grain to kill banding (`surfaces-and-materials.md` §10).

### 8.6 Gooey liquid metaballs

- **Lab**: filter 456–468 (`feGaussianBlur stdDeviation 13` → `feColorMatrix` alpha `24 −10` → `feComposite atop`), stage 1210–1254, orbit loop 5311–5318, pointer blob 5181–5189, viscosity 3890–3894 (6–22).
- **Communicates**: merging, fluidity, things becoming one.
- **Fits**: a small accent figure (merging accounts, blending, unifying sources) inside a card or a 300 px hero inset. CPU filter: never on scroll paths or large areas.
- **Correct**: `transition-transform duration-75` on the pointer blob fights per-move writes; drive with `quickTo` or remove. Remove the filter (swap a class) when off-screen. Bound the stage to about 300 × 300 px.

### 8.7 Chromatic liquid lens

- **Lab**: filter 471–488 (`feTurbulence baseFrequency 0.025` → `feDisplacementMap scale 28`), stage 1867–1945, JS 4251–4286. A `backdrop-blur-[3px]` puck follows the pointer; the text under the filter carries opposing red/cyan `text-shadow` for aberration.
- **Communicates**: optics; looking through something.
- **Fits**: one display word or logo in an experiential hero; a hover accent. Never body text (illegible) and never larger than about 400 px.
- **Correct**: the lab rewrites `baseFrequency` on every `mousemove` (4280–4284), recomputing the whole filter per event: never animate turbulence frequency from the pointer; animate the displacement `scale` attribute only, at most once per frame via `gsap.to(node, { attr: { scale } })`. `cursor-none` on the stage hides the pointer without a substitute: keep the cursor or provide a real custom cursor. Reduced motion and touch: static lens or none.

### 8.8 Fractal grain overlay

- **Lab**: 445–451, fixed full-viewport SVG `feTurbulence baseFrequency 0.82, numOctaves 4` at 3.2% opacity, `z-50`.
- **Correct**: a live full-viewport SVG filter repaints with everything beneath it; use a tiled 256 px noise PNG or confine the SVG filter to the hero (`surfaces-and-materials.md` §10). The lab's `z-50` layer also sits over modals; keep grain below overlays or give overlays their own.

### 8.9 Multi-layer ambient shadow and ambient top glow

- **Lab**: `.ambient-shadow` 88–95 (four doubling layers plus an inset top highlight); the fixed 950 × 420 px `blur-[110px]` glow at 493. Static, so cheap enough once; never animate either. Recipe in `surfaces-and-materials.md` §5.

## 9. Catalog: physics and the master loop

### 9.1 Interruptible spring (Hooke's law puck)

- **Lab**: markup 1062–1163, state 3828–3836, params 3838–3846, retarget 3848–3866, integration and graph 5266–5309. Defaults k 220, c 16, m 1.0 (slider ranges k 60–500, c 4–45, m 0.5–3.0), semi-implicit Euler per frame, side-by-side with a 650 ms CSS `ease-in-out` puck that restarts its curve on retarget.
- **Communicates**: the interface has momentum; interrupting it is safe.
- **Use**: any value the visitor can retarget mid-flight (toggles, dock items, drag release, a hero figure that follows the pointer). The lab's k 220 / c 16 / m 1 is a good default "snappy with one soft overshoot"; c 24 at the same k is critically damped. Formula and stop condition in `motion-system.md` §6.
- **Correct**: the lab integrates forever; stop the loop (or skip the step) when `|x − target| < 0.01` and `|v| < 0.01`. Motion's `type: "spring"` or GSAP `InertiaPlugin` are the library forms.

### 9.2 Frame-rate-independent damping and the single rAF loop

- **Lab**: `damp()` 5117–5119; loop 5234–5411 with `dt` clamped to 0.064 s; telemetry HUD 498–532 and 5238–5242; every subsystem (marquee, spring, metaballs, carousel fill, canvas field) steps inside this one loop.
- **Use**: the architecture is right: one loop, one `dt`, every actor stepped from it. With GSAP present, that loop is `gsap.ticker` (`motion-system.md` §7); with Lenis, `lenis.raf` is called from it.
- **Correct**: the lab writes HUD text and reads `scrollWidth` every frame; keep per-frame work to transforms. Gate each subsystem on visibility. The HUD is a development tool: ship it behind a flag or not at all.

### 9.3 Logarithmic rubber-band

See 7.6 and `motion-system.md` §6.

## 10. Recipe: a hero sequence from lab actors

A hero sequence is several actors on one timeline with labels, not one effect. Choose the actors from the concept (see `SKILL.md` "Concept before layout"), then score them. Example for a figure-dominant hero whose figure is an exploded stack (5.1) with a stroke-traced diagram (4.3) over it:

```js
gsap.registerPlugin(ScrollTrigger, SplitText);
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

document.fonts.ready.then(() => {
  const split = SplitText.create(".hero h1", { type: "lines", mask: "lines" });
  (split.masks || []).forEach((m) => { m.style.paddingBlock = "0.12em"; m.style.marginBlock = "-0.12em"; });

  if (reduce) { gsap.set([".hero .eyebrow", ".hero .cta", ".hero .figure", ".nav"], { autoAlpha: 1 }); return; }

  const tl = gsap.timeline({ defaults: { ease: "expo.out" } });
  tl.addLabel("figure")
    .from(".hero .figure .layer", { z: -40, autoAlpha: 0, stagger: 0.07, duration: 1.0 }, "figure")   // primary actor: the concept
    .from(".hero .figure .trace", { strokeDashoffset: (i, el) => el.getTotalLength(), duration: 0.9, ease: "power2.inOut" }, "figure+=0.25")
    .addLabel("type", "figure+=0.35")
    .from(split.lines, { yPercent: 120, rotate: 1.5, duration: 0.9, stagger: 0.09 }, "type")          // headline legible by ~0.6 s after start
    .from(".hero .eyebrow", { autoAlpha: 0, y: 8, duration: 0.4, onStart: () => decode(document.querySelector(".hero .eyebrow"), "Shipping since 2019") }, "type")
    .from(".hero .cta", { autoAlpha: 0, y: 12, duration: 0.5 }, "type+=0.45")                        // CTA last, but it was clickable from first paint (only opacity/transform)
    .from(".nav", { yPercent: -100, duration: 0.6 }, "type+=0.2")                                     // nav settles with the type
    .add(() => initMagnetic(), "type+=0.6");                                                          // micro-interactions arm after the sequence
});
```

Rules the recipe obeys: the figure (concept) leads, type follows 350 ms later, the CTA lands last but was never `display: none`; total 1.4–1.6 s; nothing animates a layout property; the whole thing is one timeline with labels so it can be replayed, scrubbed in GSDevTools, and reversed; reduced motion jumps to the end state. A working build of this recipe, with live stagger and ease controls, is lab Section 08 (3.5).

## 11. Recipe: a pinned set piece from lab actors

The exploded stack (5.1) as a pinned chapter with synchronized copy. Stage is `height: 100dvh`; figure sized `min(60vw, 64dvh)` on desktop, `min(72vw, 44dvh)` on phones with the chapters stacked below it inside the pinned box.

```js
gsap.matchMedia().add({ full: "(prefers-reduced-motion: no-preference)", reduce: "(prefers-reduced-motion: reduce)" }, (ctx) => {
  const layers = gsap.utils.toArray(".stage .layer"), chapters = gsap.utils.toArray(".stage .chapter");
  if (ctx.conditions.reduce) { gsap.set(layers, { z: (i) => (i - 1) * 60 }); gsap.set(chapters, { autoAlpha: 1 }); return; }

  const tl = gsap.timeline({ scrollTrigger: { trigger: ".stage", start: "top top", end: "+=250%", pin: true, scrub: 0.6, anticipatePin: 1 } });
  tl.to(layers, { z: (i) => (i - 1) * 90, ease: "none", duration: 1, stagger: 0.06 }, 0);          // Move
  chapters.forEach((c, i) => {                                                                          // Settle, then Annotate
    const at = 0.2 + i * (0.7 / chapters.length);
    tl.fromTo(c, { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.12, ease: "power2.out" }, at)
      .to(c, { autoAlpha: 0, y: -12, duration: 0.1 }, at + 0.7 / chapters.length - 0.08);
  });
});
```

A working build of this recipe with labels, snap and a live readout is lab Section 07 (5.4); read its "Correct" notes on chapter timing against snap labels before adapting. When adapting, move the readout onto the traveling actor rather than keeping it in the corner, and follow the header, marker, and label rules in `scroll-and-3d.md` §4. Checks before calling it done: every chapter's copy and the figure are inside the viewport at 390 × 844 and 1440 × 900 at 0%, 50%, and 100% progress; `ScrollTrigger.refresh()` runs after fonts and images load; the copy does not say "on the right" or "below", because at 390 px the figure is above the copy; keyboard users can tab past the stage; `document.documentElement.scrollWidth === innerWidth` at 390 px (3D transforms with `perspective` often leak horizontal overflow; fix with `overflow: clip` on the stage, not `overflow-x: hidden` on `<body>`).

## 12. Defects common to the whole lab

Correct these wherever you adapt from it:

1. `mousemove` instead of `pointermove`; no `(hover: hover) and (pointer: fine)` gating; no touch equivalents except the canvas click.
2. No `prefers-reduced-motion` handling anywhere in sections 00–06 (the first 2,134 lines of markup and their JS). The default experience is right; the reduced composition must be added (fades, static end states), never used as the reason to weaken the default. Sections 07–12 show the pattern: every section is built inside `gsap.matchMedia()` with a `reduce` branch that produces a complete static composition (unpinned stage, all chapters visible, figure at its end state, one shader frame) and a cleanup function; the shader section listens for the media-query `change` event as well.
   The same sections also fix items 1, 3–7 and 9 for themselves (pointer events gated on `(hover: hover) and (pointer: fine)`, no CSS transition on a GSAP-driven property, `IntersectionObserver` and `visibilitychange` on the shader, a native `<dialog>` for the overlay, an `AbortController` and a `LAB_GSAP_CLEANUP` registry); items 8 and 10 still apply to the page as a whole.
3. CSS transitions on properties that JS also writes per frame (tilt, magnetic, goo blob, glass specimen), producing lag and fights. One owner per property.
4. Layout reads (`getBoundingClientRect`, `scrollWidth`) inside scroll and pointer handlers and inside the frame loop; cache and refresh on resize/`scrollend`.
5. Per-frame writes to `width`, `innerHTML`, and text nodes; write transforms and CSS variables instead.
6. Nothing pauses off-screen or in a hidden tab; add IntersectionObserver and `visibilitychange` gating per subsystem.
7. Modal surfaces built from `div`s without `<dialog>`, focus management, or `inert`.
8. `overflow-x: hidden` on `<body>` and `scroll-smooth` on `<html>`; remove both (find the overflow; let Lenis or native scrolling own smoothness).
9. Inline `on*` attributes and a global function namespace; module-scope your adaptation and own cleanup (`gsap.context()`, `split.revert()`, listener removal).
10. Dated dependencies: Tailwind via CDN and runtime Google Fonts. Self-host and subset fonts; compile Tailwind.
