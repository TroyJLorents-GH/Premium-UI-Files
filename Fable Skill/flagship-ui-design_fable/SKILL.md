---
name: flagship-ui-design
description: "Design and build award-level web UI with a product-specific concept, a written direction contract, brand-chosen typography, and signature motion: landing and launch pages, portfolios, experiential sites, heroes, plus SaaS apps, dashboards, docs, navigation, scroll choreography, micro-interactions, tokens, dark mode, materials, 3D heroes, and page transitions, using GSAP (ScrollTrigger, SplitText, Flip), Motion, Lenis, View Transitions, Three.js/R3F, shadcn, Tailwind, a bundled 120 Hz motion lab, and the GSAP playbook. Use whenever the user asks for a website, page, section, component, redesign, polish pass, better fonts, 'make it premium / Awwwards / less generic / less AI-looking', animation, smooth scroll, or a design review, even without saying 'design'. Also audits UI for performance (LCP/INP/CLS), WCAG 2.2, reduced motion, and AI-slop patterns, with research via Refero, Mobbin, 21st.dev, and Impeccable."
---

# Flagship UI Design

There are two kinds of surface, and almost every rule in this skill branches on which one you are building.

**Expressive surfaces** (landing, marketing, launch, portfolio, experiential): the page *is* the argument for the product. Here a safe page is a failed page. A headline on one side, a mockup on the other, cards that fade up on scroll: that is the standard AI layout, and it ships as "a terrible web page" no matter how clean the tokens are. Expressive surfaces are required to have a concept the product owns, a hero sequence of several coordinated actors, a scroll-driven set piece that makes the concept physical, and signature micro-interactions, all chosen by name before any structure is written.

**Quiet surfaces** (SaaS apps, dashboards, docs, reading, checkout, settings): the craft is in states, speed, and recovery. Motion stays quiet; the old per-page cap (one hero treatment, one navigation idea, two or three micro-interactions) applies here and only here.

Everything else (performance, accessibility, honest states, one ticker, transform-only animation) is non-negotiable on both. Reduced motion is a fallback path derived from the full experience; it is never the reason the default is timid. Research snapshot of the sources: **November 2026**; verify versions and APIs against current docs before adopting anything.

## 1. Concept before layout

Before any structure, find the product's own physical or visual metaphor and let it drive the hero figure and the page's main motion. The test: swap the copy for a different product. If the page still works, there is no concept, only a template.

Reasoning pattern (write the answers down; three lines is enough):

1. **Verb and object.** What does the product do, to what? Not "helps teams collaborate"; "merges three ledgers into one", "cools a room by two degrees", "turns a sketch into a cut file".
2. **The moment of change.** When does the object visibly change state? That instant is the hero's first 1.5 seconds and the set piece's whole arc.
3. **The figure.** What is the simplest honest picture of that object mid-change? Layers separating, a line resolving, a grid reorganizing, a surface settling, a waveform flattening. Real geometry from the domain, not an abstract blob.
4. **The feeling.** Relief, precision, speed, calm, power. One word; it picks the easing, the pace, and the materials.
5. **The motion.** The figure's change *is* the hero animation and the scroll chapter. Type and CTA follow it.

| Product | Verb → object | Figure that could not belong to anything else | Hero motion | Scroll set piece |
|---|---|---|---|---|
| Payments API | reconciles → ledgers | Three columns of entries sliding into one aligned column | Rows converge and lock, totals count to equal | Pinned: a payment travels left to right through each stage, chapters annotate |
| Sleep tracker | dims → a room | A room at dusk; light falling, a heart-rate line slowing | Scene darkens over 1.2 s, line settles | Night progresses with scroll; stages label themselves |
| Logistics routing | resolves → a route | Tangled candidate paths collapsing to one stroke | Strokes draw, losers fade, winner thickens | Route scrubs across a map; stops snap into place |
| Code review tool | reduces → a diff | A wall of red/green lines shrinking to a short, readable list | Noise lines fall away, the signal lines stay | Pinned diff: each scroll step removes a category of noise |
| Coffee roaster | develops → beans | Beans turning from green to brown along a temperature curve | Color ramps with a drawn curve | Roast profile drawn by scroll with crack markers |
| Typeface foundry | tunes → letterforms | One glyph's weight and width breathing across axes | `wght` sweeps 300 → 800 as the word sets | Specimen reflows across axes with scroll |
| Climate sensor | samples → air | A field of particles with a few lighting up as they are measured | Field settles, samples pulse | Readings accumulate into a chart as you scroll |
| Contract tool | redlines → clauses | A dense page with clauses lifting out and simplifying | Clauses lift, shrink, line up | Pinned page: scroll walks clause by clause |
| Audio mastering | flattens → a waveform | Spiky waveform settling into a controlled shape with headroom | Peaks compress in 0.9 s | Scroll scrubs through a track; meters respond |
| Architecture studio | assembles → a building | Structural layers arriving in order: slab, frame, skin | Exploded stack closes | Stack explodes with scroll; each layer named |

Not a concept: particles, gradient orbs, floating glass cards, dot grids, 3D blobs, a glowing ring. These are textures; they fit any product, which is exactly the problem.

## 2. Signature motion: the floor on expressive surfaces

Choose the effects by name from `references/signature-motion.md` (the catalog of the bundled 120 Hz motion lab, with line references and corrected code) before you write structure. Lab sections 07–12 are GSAP-native builds of this floor and the first place to look for its parts: a pinned, labeled, snapping set piece (07), a six-actor SplitText hero timeline (08), a horizontal `containerAnimation` gallery with velocity skew (09), a navigation suite with full keyboard paths (10), a DrawSVG, MorphSVG and MotionPath scene (11), and a WebGL2 shader stage with a poster fallback (12), each with a `gsap.matchMedia()` reduced-motion composition and a cleanup path. Then build to this floor:

1. **Hero sequence.** Three to six coordinated actors on one labeled timeline: the concept figure leads, headline lines mask-reveal about 350 ms later, eyebrow and CTA land last, the nav settles. Total 1.2–1.8 s; the headline is legible by about 0.6 s; the CTA is interactive from first paint (opacity and transform only, never `display: none`). Recipe: `signature-motion.md` §10.
2. **One scroll-driven chapter or set piece.** Pinned, scrubbed (`scrub: 0.6–1`, `end: "+=200–300%"`), with copy chapters synchronized to figure states. It makes the product's idea physical; it is not a reveal-on-scroll. The reader's eye is on the moving marker, so any live value rides on or beside that marker, and the section header and figure sit together as one group with no dead band between them. A static label near a moving playhead reads as the clock: give it a visible range or write it as a beat title, not a bare timestamp. Recipe: `signature-motion.md` §11; rules: `references/scroll-and-3d.md` §4.
3. **Signature micro-interactions.** At least three named effects: one on the primary CTA, one in the navigation, one in the proof or feature section, sharing one easing grammar. A hover color change is not one of them.
4. **One playable product instrument** when the page sells a product or tool. The visitor drags, scrubs, types, or toggles, and computed output changes immediately with a live readout. This is what proves the product is real, and it is the part people remember. It runs on labeled sample data, works by touch, and has a keyboard path (a real `<input type="range">` or arrow keys). It can be the hero or its own section. A looping demo or a screenshot does not count.
5. **Named before building.** The motion list (effect name, what it communicates, trigger, duration or spring, owner, reduced-motion equivalent) is written before the first layout decision and reported with the build.

Use GSAP with ScrollTrigger and SplitText freely (Flip, DrawSVG, ScrambleText, Observer as needed; routes in `references/gsap-plugin-playbook/PLAYBOOK.md`). On a single-file page, load from a pinned CDN with exact versions, for example `https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js`, `.../dist/ScrollTrigger.min.js`, `.../dist/SplitText.min.js` (versions here are dated; check the current release). Lenis is allowed on expressive pages, driven from `gsap.ticker`.

The floor is not a license for noise. One owner per property, one ticker, compositor-only properties on continuous paths, Move → Settle → Annotate, text static once it has finished entering, every effect with a cleanup owner, and a reduced-motion composition for each actor. Those rules make the motion read as expensive rather than busy.

## 3. Hero constructions

On an expressive surface the two-column hero (headline on one side, card, mockup, or image on the other) is not an acceptable default, and neither is a centered headline above a floating mockup. The first viewport must be unmistakably this product's. Pick one of these, or invent one that follows the concept:

| Construction | Layout | Actors |
|---|---|---|
| **Figure-dominant** | The concept figure occupies 70–100% of the viewport; the headline is set across or into it (large type behind or over the figure, `mix-blend-mode` or a masked band); CTA anchored to a corner of the grid | Figure build, masked lines, magnetic CTA |
| **Typographic monument** | Headline at 10–16 vw fills the width over two or three lines; the figure is small and precise and lives inside the type (a word that is a live counter, a glyph that is the instrument) | Masked lines, variable-axis sweep, cipher on one word |
| **Stage and caption** | Full-bleed stage (canvas, 3D, image sequence) edge to edge; a thin caption rail (eyebrow, one line, CTA) pinned to the bottom-left; nav minimal | Vector field or sequence, cipher eyebrow, beam CTA |
| **Scroll-opening** | The hero is frame 0 of the set piece. The first scroll pins the viewport and begins the concept build; the headline shrinks into a sticky title | Pinned stack or trace, SplitText lines, dynamic-island nav |
| **Editorial masthead** | A top rule, a full-width headline, the figure below spanning the full width, body copy in a narrow measure off-axis | Masked lines, stroke trace, per-word illumination |
| **Interactive instrument** | The hero is a working piece of the product the visitor can touch within a second (a tuner, a slider, a search, a field that reacts) | Tilt, spring puck, variable-axis tuner, vector field |
| **Crossed split** | Two columns are allowed only if the figure breaks the column: it overlaps the headline, bleeds past the gutter, or reacts to the type; never 50/50 or 7/5 with a card | Exploded stack bleeding behind type, magnetic CTA |

Mobile is reframed, not stacked: crop the figure deliberately, keep the first viewport to `100dvh` with the headline, CTA, and at least part of the figure inside it, and never let the figure become a decorative thumbnail above a text block.

### Brief, contract, static first

The hero method comes from the `hero-design` skill (full working method in `references/hero-and-direction.md`):

1. **Read the real brief.** Existing route, adjacent sections, real copy and assets, tokens, PRODUCT.md/DESIGN.md. A hero request does not authorize a site redesign.
2. **Research that ends in decisions.** 21st saved lists and searches, Mobbin sections, Refero styles; inspect previews and source, then keep a short source list saying what each contributes.
3. **Write the direction contract before editing UI**: story and action, construction and why, references and traits taken, typography roles, palette roles, spacing rhythm, image treatment, desktop and mobile composition, motion purpose, things to avoid.
4. **Static before motion.** The desktop view and the mobile recomposition must work with motion off before any timeline is written.
5. **Before and after.** On an existing page, render 1440 × 900 and 390 × 844 before touching it, and render the same views after, judged against the contract.

### Section headlines

The hero is not the only place the layout shows. A section headline stacked in a narrow left column with the right side empty is the same AI layout at a smaller size. On expressive surfaces, a section opens with its headline spread across the top of the section in the display face, on two balanced lines, with the section's content below it. Size it with `clamp()` so it takes two lines at desktop width, and use `text-wrap: balance` rather than manual breaks. Never force one `nowrap` line, which runs off the edge at some width. Phones may wrap to three or four lines. Exceptions need a reason the composition can show, such as a figure that deliberately occupies the space beside the type.

## 4. Direction and tokens

Write the direction in two sentences before coding (dark with a single warm accent; editorial Swiss with big type and air; warm minimal; neo-brutalist; translucent glass; grain-and-mesh), derived from the concept's feeling, then expand it into the direction contract (§3).

Type is chosen, not defaulted. Assign a face per role (display, text, and a data/label face when the page shows numbers), pick from a shortlist matched to the concept's feeling, and check weights or axes, tabular figures, glyph coverage, and license before committing. Instrument Serif + Inter, Inter or Geist alone, Playfair or Fraunces over Inter, and Space Grotesk are the saturated defaults; use them only when the brief gives a reason. A display face with a single weight can only make hierarchy through size. Procedure: `references/hero-and-direction.md` §5.

Encode the direction as tokens: color roles in OKLCH, a 4/8 px spacing scale, radius with the nested rule (inner = outer minus padding), two or three shadow layers, named `--duration-*` and `--ease-*`. `assets/tokens.css` is a starter; one direction per product, applied through tokens.

Ground it in reality: look at two or three production references in the category through Refero or Mobbin, then diverge deliberately (`references/tool-integrations.md`). Never clone a reference's palette, type, and layout together.

## 5. Build order

Real brief and before renders → concept statement → research and direction contract (typography roles included) → named motion list → semantic HTML with real content → layout (hero construction chosen) → tokens and type → static desktop and mobile check → every component state (default, hover, focus-visible, pressed, selected, disabled, busy, success, error, empty, loading, long content) → the hero timeline, the set piece, the micro-interactions → materials → verification. Motion is planned first and built after structure; materials are last because they are the cheapest to change and the easiest to overdo.

Standard components (pricing, FAQ, comparison tables, testimonials, footers) are where hand-written pages go flat. Source them instead of improvising: search 21st.dev first (for pricing, `21st search "pricing components" --type component`), compare two or three, then adapt the best one to this page's tokens and concept. If nothing fits, or 21st.dev is unavailable, make Impeccable the lead workflow for that component. Details: `references/page-patterns.md`.

## 6. Stack ladder

Platform first (CSS transitions and keyframes, `@starting-style`, View Transitions, scroll-driven animations, `<dialog>`, `popover`, anchor positioning), a library second (GSAP for timelines, scroll choreography, and SVG; Motion for React/Vue component state and layout animation), a custom engine last (Three.js/R3F, OGL, shaders). Never add a second engine for a job the installed one does; never migrate frameworks unasked. Smooth-scroll layers (Lenis) only on expressive pages. Selection tables: `references/stack-selection.md`.

## 7. Intake

Answer these from the request and the project; ask the user only when the answer changes the architecture, otherwise state the assumption and proceed.

| Question | Why it matters |
|---|---|
| Expressive or quiet surface | Decides whether the motion floor or the motion cap applies |
| Existing stack, framework, package manager, installed animation libs | Use what is installed; add GSAP on expressive pages if nothing covers timelines and scroll |
| Audience device floor | Mid-range Android on 4G is the default floor for public sites |
| Primary task of the visitor | The hero, nav, and CTA exist to make it obvious; motion that delays it is a cost |
| Content reality: real copy, media, or placeholders | Design with real content; placeholders hide long names, missing images, translated strings |
| Interaction freedom vs fixed path (3D/scroll stories) | Free orbit needs live WebGL; a fixed camera path is cheaper as a frame sequence or 2.5D depth map |

### Common requests and the first move

| Request | First move |
|---|---|
| "Make it look premium / less generic / less AI" | Run the anti-slop table; if the hero is a split or a centered-mockup, re-concept it (§1, §3) before touching tokens |
| "Add animations" / "make it feel alive" | Expressive surface: build the floor in §2 from named effects. Quiet surface: one hero treatment, one nav idea, two or three micro-interactions, CSS elsewhere |
| "Add smooth scrolling" | Expressive pages get Lenis on the single ticker with a reduced-motion opt-out; apps, docs, dashboards keep native scroll |
| "Copy this site" / inspiration URL | Extract direction, tokens, one or two patterns; never palette, type, and layout together |
| "Make the hero pop" | Before renders, then re-check the concept, the construction, and the direction contract, then the sequence; a stronger effect on a template hero is still a template |
| "The fonts look generic" | Typography selection in `references/hero-and-direction.md` §5: roles, shortlist, checks, real-size previews |
| "Review / critique this UI" | `references/quality-bar.md` ordered by user impact; findings with fixes, not praise; on expressive surfaces judge the concept and the motion first |
| "Why is it janky" | Single-ticker check, layout-property animation check, DPR cap, scroll-handler layout reads, then a throttled trace |
| "It needs to be accessible" | Exact WCAG 2.2 numbers in `references/performance-a11y.md` §5; reduced-motion composition; keyboard pass |

## Non-negotiables

1. **Animate only `transform`, `opacity`, and sparingly `clip-path`/`filter` on any continuous path** (scroll, pointer, loops). `top/left/width/height/margin/box-shadow/border-width` trigger layout or paint every frame. Cross-fade a pseudo-element for shadow motion; animate `grid-template-rows: 0fr → 1fr` or `interpolate-size` instead of `height`; use FLIP (View Transitions, Motion `layout`, GSAP Flip) for layout changes. A one-shot width morph on a state change is acceptable; per-frame is not.
2. **One owner per animated property, one ticker per page.** CSS, GSAP, Motion, and a framework transition never write the same transform. Lenis, GSAP, and Three.js share one loop (`gsap.ticker`, Lenis `autoRaf: false`). Competing loops cause micro-jitter that FPS counters miss.
3. **Reduced motion is a composition derived from the full one, not a kill switch and not a design constraint on the default.** Under `prefers-reduced-motion: reduce`, remove parallax, pinning, large travel, auto-play loops, and camera moves; keep opacity fades and transforms under about 150 ms; keep every state change and feedback. `gsap.matchMedia()`, Motion `useReducedMotion()`, a global CSS block.
4. **Motion never delays input or comprehension.** Presses acknowledged within 100 ms. Headline, nav, and CTA are readable and operable before any intro finishes; no compulsory preloader. Text that has finished entering stays still while people read it.
5. **The useful page loads independently of the decoration.** Poster before 3D or video; no `loading="lazy"` on the LCP element or inside a pinned section; dimensions reserved for all media; metric-matched font fallbacks. Decorative scripts load after LCP or on first interaction.
6. **Keyboard, focus, and semantics survive the effect.** Real `<button>`, `<nav>`, `<dialog>`, `<details>`, headings in order, visible `:focus-visible`. Pinned and Observer-driven sections keep a keyboard path and an exit. Split text keeps a coherent reading order; canvas and WebGL content keeps its text and controls in the DOM.
7. **Every effect has a cleanup owner.** Revert SplitText, kill ScrollTriggers, dispose Three.js resources, remove listeners, cancel rAF on unmount or route change.
8. **Honest states.** Success means the action succeeded. No fake progress, no endless shimmer, no toast as the only record of a critical failure.

## The numbers

Starting points, tuned by travel distance, frequency, and platform. Repeated actions get near-zero motion; keyboard-triggered actions get faster, simpler motion than pointer-triggered ones.

| Element | Enter | Exit | Notes |
|---|---|---|---|
| Hover, color, press | 100–150 ms | same | press scale 0.97 |
| Tooltip, toggle, checkbox | 150 ms | 100 ms | translate 4–6 px plus fade |
| Dropdown, popover, menu | 150–200 ms | 100–150 ms | scale from 0.95 at the anchor's origin |
| Modal, drawer, sheet | 200–300 ms | 150–200 ms | scale 0.96 → 1 or slide; backdrop in step |
| List add/remove/reorder | 200–300 ms | 150 ms | stagger 20–40 ms, total near 300 ms |
| Route or view transition | 250–400 ms | 150–250 ms | crossfade or shared-element morph |
| Scroll reveal (secondary content) | 500–800 ms | — | translate 24–40 px, trigger at 10–20% in view, once |
| Hero sequence (expressive) | 1.2–1.8 s total | — | several actors, labeled timeline; headline legible by ~0.6 s |
| Hero intro (quiet) | ≤ 800 ms | — | headline, sub, CTA |
| Pinned set piece | 200–300% viewport travel | — | `scrub: 0.6–1`; linear tweens inside, the scrub supplies easing |
| Number counters | 600–1000 ms | — | `tabular-nums` |
| Marquee, ambient loops | 20–60 s | — | linear; pause on hover, off-screen, hidden tab |

Easing by intent: enter with a strong ease-out (`cubic-bezier(0.16, 1, 0.3, 1)`, `expo.out`, `power4.out`); exit with a quick fade (≤150 ms); move on-screen elements with ease-in-out; `linear` only for progress, marquees, and anything scrubbed by a damped scroller; a spring (defined by perceptual duration and bounce, carrying gesture velocity, `bounce: 0` for large surfaces) wherever a gesture or interruption is possible. Never `ease-in` on long moves, `linear` on movement, or `elastic`/`bounce` on large surfaces. Sheet settle: `cubic-bezier(0.32, 0.72, 0, 1)`.

Choreography: primary actor first, followers 60–120 ms later, static anchors (grid hairlines, pinned header) so movement has a reference; scale from 0.95–0.97, never from 0; stagger 20–50 ms from the attention point and cap the total; transform-origin from the trigger; exits simpler than entrances; scale containers, not text; blur 2–4 px max on small elements; for 3D and scroll stories, Move → Settle → Annotate (about 75% of the travel before callouts appear). Full tables, springs, physics formulas, single-ticker setup, and failure modes: `references/motion-system.md`.

## Materials

Full CSS in `references/surfaces-and-materials.md`; the parameters matter more than the technique. Glass: `backdrop-filter: blur(16–20px) saturate(180–190%)` over a 40–70% alpha surface, 1 px border at 12–16% white, inset top highlight, 2–4% grain, solid fallback under `prefers-reduced-transparency`, limited count and area. Shadows: 2–3 layered soft shadows plus a 1 px low-alpha border for cards, 4–6 doubling layers only on hero surfaces, tinted with the background hue, never animated. Dark mode: near-black with a hue, elevation through lighter surfaces, body text at 85–92%, borders as `color-mix(in oklab, currentColor 12%, transparent)`. Specular hairline, cursor spotlight (one listener, cached rects, fine pointers only), conic beam (one CTA per screen), grain (tiled PNG beats a live full-viewport filter). Color in OKLCH with 10–12 step scales and semantic roles. Type: one or two variable fonts, self-hosted and subset, `clamp()` scale, `text-wrap: balance` on headings, negative tracking only on large display, `tabular-nums` on anything live; never `maximum-scale=1`.

## Anti-slop: the tells and the fixes

A model produces these by default. Check your own output against them before showing it.

| Tell | Fix |
|---|---|
| Two-column hero: headline on one side, card, mockup, or image on the other | Not an acceptable default on expressive surfaces. Choose a construction from §3 driven by the concept; if two columns survive, the figure must break the column |
| Centered headline over a floating product shot or glass card | Same: figure-dominant, typographic monument, stage-and-caption, or scroll-opening instead |
| A row of identical bento cards (icon, title, sentence) | One dominant cell showing the feature working (live component, short loop, real screenshot), supporting cells asymmetric in size and density |
| Fade-up on scroll as the only motion; every element fading up | A hero sequence, one pinned set piece, named micro-interactions; reveal secondary content once per group with a 20–50 ms stagger |
| Purple-to-blue gradient, gradient text, glow on every border | One accent on one or two elements per screen; gradients only as a direction choice with grain |
| Section headline stacked in a narrow left column with the right side empty | Spread it across the top of the section in the display face on two balanced lines, content below (§3, Section headlines) |
| Three equal pricing cards with a checkmark list | Source a pricing component from 21st.dev or run Impeccable on it, then adapt it to the page's tokens and concept (§5); keep prices, limits, and exclusions truthful |
| Everything centered, every section the same width and rhythm | Asymmetric composition that varies density and width within one system: a full-bleed stage, a narrow measure, a wide figure; alignment chosen per section, not one axis everywhere |
| `hover:scale-105` everywhere, bounce easing, elastic on large surfaces | Hover lift of 2 px plus shadow cross-fade; ease-out; springs with `bounce: 0` on big things |
| Copy like "Unlock the power of", "Seamlessly", "Elevate"; copy that names layout positions ("at right", "below") | Specific verbs and nouns about what the product does; never reference a position that changes at a breakpoint |
| Copy that disagrees with the figure beside it (a label says one time, the curve peaks at another) | Generate labels, spans, and totals from the same data that draws the figure, so they cannot drift apart |
| Rounded-2xl on everything, inconsistent radii, 1 px gray borders on all cards | Radius tokens with the nested rule; surface hierarchy through background steps |
| Dark gray `#111` page with `#1a1a1a` cards and 100% white text | Near-black with a hue, elevation through lighter surfaces, body text at 85–92% |
| Stock photos, lorem ipsum, placeholder logos, fake testimonials, fake metrics | Real content or honest placeholders marked as such; never fabricate proof |
| Generic sans at default weight with no scale | A deliberate pair, a `clamp()` scale, optical tracking, tabular numerals |
| The stock pairing (Instrument Serif + Inter, Playfair over Inter, Inter or Geist alone) or a one-weight display face | Faces chosen per role from a shortlist matched to the concept, with weights or axes for real hierarchy and a data face where numbers appear (`references/hero-and-direction.md` §5) |
| Full-viewport preloader, scroll-jacked everything, custom cursor on an app | Load the hero fast; one pinned set piece on expressive pages, none on quiet ones; custom cursors only on fine-pointer experiential sites |
| Toast for every action, skeletons that shimmer forever, spinners without timeout | Skeletons only after ~300 ms, progress for anything over 1 s, toasts for supplemental feedback only |
| Modal built from divs, hover-only menus, `outline: none` | `<dialog>`, click-and-keyboard menus, `:focus-visible` ring |
| The lab's own 7/5 split, bento frames, and cyan/indigo palette copied wholesale | Take the actors from `signature-motion.md`, never the lab's layout or direction |

## Verification: judge motion and composition, then everything else

Static screenshots pass motionless pages. Verify in a browser (Playwright, Chrome DevTools MCP, or the built-in browser) at **1440 × 900** and **390 × 844**, and report what you saw.

1. **Hero frames.** Capture at about 0, 300, 700, and 1200 ms after load (and again with `prefers-reduced-motion: reduce`). Between frames the figure, type, and CTA must visibly change state. Identical frames mean the page reads as static: fail.
2. **Scroll frames.** Capture at 0, 25, 50, 75, and 100% of document height, and at three progress points inside the set piece (0, 50, 100%). The set piece must show the figure in different states with its copy in view each time.
3. **Template check.** Look at the first viewport at both sizes as a stranger would. If it reads as a common template (split hero with a card, centered headline over a mockup, three equal cards) the page fails regardless of polish.
4. **Composition checks.** No card with large dead space (content occupies well under half the card's area): resize the card or fill it with the feature working. No clipped or colliding text: headings fit their containers, no overlapping rectangles between text nodes, masked line reveals leave room for ascenders and descenders (pad the mask block 0.1–0.15 em, counter with negative margin). Pinned stages fit copy and figure inside the viewport at both sizes using `dvh`, not `vh`, with the header directly above the figure and no empty band between them. Live readouts stay beside their moving marker at every progress point and flip or clamp at the edges instead of clipping. Charts run to the end of their axis, and first and last axis labels are fully visible. Adjacent full-bleed sections meet with no sliver of page background between them. Section headlines span the top of the section on two lines at 1440 px, with no narrow column beside empty space.
5. **Overflow.** On the 390 px viewport, `document.documentElement.scrollWidth` must equal `window.innerWidth`. If it does not, find the element (3D transforms with `perspective`, marquees, bleeding figures are usual) and fix it; `overflow-x: hidden` on `<body>` is not a fix.
6. **Copy.** No sentence names a layout position ("the panel at right", "the chart below") because the layout changes at breakpoints. Every time, quantity, or span stated in copy is checked against the figure's data, and every label near a moving marker makes clear whether it is a range, a title, or the current value.
7. **Contract and before/after.** Compare the final render against every field of the direction contract. On an existing page, show the before and after captures at both viewports side by side; if the after still reads like the before with new effects, the revision failed.
8. **Static scan.** `node scripts/audit-ui.mjs <dir>` for anti-patterns (it never flags intentional motion; it flags the ways motion goes wrong).
9. **Performance and accessibility.** The DevTools protocol in `references/performance-a11y.md` §8: 4× CPU throttled scroll trace with no long tasks, reduced-motion emulation, keyboard-only pass, 320 px reflow, color modes, cleanup after repeated navigation.

Fail the page when any of 1–7 fails. Inspect desktop and mobile together, fix in one batch, confirm once; do not loop on polish. Report distinguishing what was built, what was adapted from the lab or a reference, and what was verified at runtime on which viewport. Do not claim smoothness from a library choice.

## Tool integrations

Details and commands in `references/tool-integrations.md`.

- **Refero Styles**: machine-readable DESIGN.md extractions of 2,000+ production design systems. Ground a direction in two or three same-category references, derive token values, answer "what do good products do here". Never clone one reference.
- **Mobbin**: real app and web screens, flows, and component patterns. Use for UX structure (onboarding, checkout, settings, empty states), not visual style alone.
- **21st.dev**: `21st search "<need>" --type component|theme|template` is free; `21st get <id>` fetches code (metered on the free tier); `21st theme <id>` is free; `21st add <user>/<slug>` installs through the shadcn registry; `21st logo <brand>` returns SVG logos. Treat fetched components as owned source: audit motion, reduced motion, contrast, dependencies, license. First stop for standard components such as pricing (§5).
- **Impeccable**: one lead design workflow per pass (`critique`, `audit`, `polish`, `typeset`, `layout`, `animate`, `adapt`, `harden`, `optimize`). Supply a brief, real content, and acceptance criteria. Do not run competing design skills in the same pass. Read its permission notes before live mode.
- **Higgsfield (image/video generation)**: before any call, tell the user what it will be used for, what will be generated, and the estimated token/credit cost, then wait for approval. Default to real assets; generate only when the design genuinely needs media that does not exist.
- **Lenis**: `new Lenis({ autoRaf: false })`, drive from `gsap.ticker`, `lenis.on('scroll', ScrollTrigger.update)`, `gsap.ticker.lagSmoothing(0)`. Off under reduced motion and inside native WebViews. Incompatible with native CSS scroll-snap. Expressive pages only.
- **Context7 / official docs**: verify GSAP, Motion, Lenis, Three.js, R3F, shadcn, and Tailwind APIs against current docs before writing code. Version strings in this skill and in captured demos are dated.
- **Bundled 120 Hz motion lab**: `assets/motion-lab-reference.html`, cataloged in `references/signature-motion.md`. Open it in a browser to see any effect running; read the cited line ranges before adapting.
- **Bundled GSAP playbook**: `references/gsap-plugin-playbook/PLAYBOOK.md` routes to captured plugin demos (ScrollTrigger, ScrollSmoother, SplitText, Flip, Draggable, Inertia, Observer, DrawSVG, MorphSVG, MotionPath, Physics2D, Pixi, ScrambleText, utilities, React). Read `source-caveats.md` first; several demos are mislabeled or carry accessibility defects the notes identify.

## Reference map

Read the file that matches the task; do not load all of them.

| When | Read |
|---|---|
| Starting any hero or page: real brief, research-to-decisions, direction contract, typography selection, static-first, before/after | `references/hero-and-direction.md` (from the `hero-design` skill, which can also be invoked directly) |
| Choosing named effects for a hero sequence, set piece, or micro-interactions; adapting anything from the lab | `references/signature-motion.md`, then the cited lines of `assets/motion-lab-reference.html` |
| Understanding how a lab section is built (stack, math, framework equivalents) before adapting or extending it, or extending the lab with a new section | `references/aether-lab-guide.md` |
| Writing or reviewing any animation; springs; physics formulas; single-ticker setup; motion failure modes | `references/motion-system.md` |
| Building a hero, nav, section, list, card, overlay, form, footer; per-archetype motion floor or cap | `references/page-patterns.md` |
| Scroll storytelling, pinning, Lenis, image sequences, Three.js/R3F, Blender-to-web, 3D-to-2D callouts | `references/scroll-and-3d.md` |
| Tokens, color, type, dark mode, glass/grain/shadow/spotlight/beam CSS | `references/surfaces-and-materials.md` |
| Choosing libraries, components, 3D stack; status and license caveats | `references/stack-selection.md` |
| Performance budgets, rendering rules, loading, exact WCAG 2.2 numbers, the DevTools protocol, release checklist | `references/performance-a11y.md` |
| The quality checklist and per-surface acceptance criteria for a review or audit | `references/quality-bar.md` |
| Refero, Mobbin, 21st CLI, Impeccable, Higgsfield rule, Lenis setup | `references/tool-integrations.md` |
| A specific GSAP plugin or captured demo | `references/gsap-plugin-playbook/PLAYBOOK.md` |
| Starting a brief, a concept statement, or a motion spec | `assets/design-brief.md`, `assets/tokens.css` |
| Static scan of a codebase for motion/a11y anti-patterns | `scripts/audit-ui.mjs` |

## Output expectations

For a build on an expressive surface: the concept statement (verb, object, moment of change, figure, feeling), the direction contract with its source list and typography choice, the chosen hero construction, the named motion list (effect, what it communicates, trigger, timing or spring, owner, reduced-motion equivalent), the direction and tokens, the implemented surface with all states, and a verification note listing the hero and scroll frames captured at both viewports, the overflow and composition checks, and remaining limitations. For a quiet surface: the same minus the concept and set piece, with the motion kept inside the cap.

For a review: findings ordered by user impact (task completion and recovery, then accessibility and performance, then concept, composition, and motion craft), each with the concrete fix. On expressive surfaces, a template first viewport or a motionless page is a top finding, not a polish note. Do not pad a review with praise.

For research: two or three grounded references with what to take from each, what to avoid, and how the chosen direction differs.
