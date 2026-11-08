# Anti-slop: what makes UI look generated, and what to do instead

"AI slop" is regression to the training-set mean: the Tailwind starter aesthetic, the same hero, the same three cards, the same purple gradient, the same copy. It is detectable, and most of it is deterministic. `scripts/flagship_audit.py` flags the mechanical tells; this file covers judgment.

## The tells (and the replacement)

| Tell | Why it reads as generated | Do instead |
|---|---|---|
| Gradient text on the headline | The single most common 2023–2026 LLM default | Solid ink; earn contrast with size, weight, measure, and a real accent used once |
| Purple/indigo → pink/blue gradients, glow blobs everywhere | Default palette of every starter | One accent in OKLCH with semantic roles; derive states with `color-mix()`; let imagery carry color |
| Glassmorphism as the default surface | Blur with no light logic | Glass only where layering is meaningful (floating nav, overlay); otherwise border + soft tinted shadow, or elevation by lighter surface in dark mode |
| Three identical icon cards ("Fast · Secure · Scalable") | Interchangeable filler; no evidence | Show the feature working (screenshot, live sandbox, bento with real micro-interactions); outcomes, numbers, names |
| Hero: "Welcome to…", "Revolutionize", "Unleash", "Seamless", "Elevate", "Supercharge", "cutting-edge" | Adjective-driven copy | Specific over clever, numbers over adjectives, verbs on buttons ("Start free trial", "Create project"), microcopy beside risk ("No card required") |
| `rounded-2xl shadow-lg` on every element | Uniform elevation flattens hierarchy | Radius tokens with nested-radius math; 2–3 layered shadows only on raised surfaces; borders as `color-mix(currentColor 12%)` |
| Inter / system font and nothing else | No type voice | A deliberate pairing (display + text), variable font, optical sizing, tracking on display, `tabular-nums` on data |
| Everything centered, every section the same rhythm | No composition | Vary density and alignment; asymmetry with purpose; subgrid-aligned cards; section rhythm need → mechanism → proof → objection → action |
| Fade-up on every section, bounce on every button | Motion as decoration | One hero choreography, two or three micro-interactions, consistent `--duration-*`/`--ease-*`; press scale 0.97 at 100 ms; no `bounce`/`elastic` on surfaces |
| Emoji as icons; sparkles ✨ | Avoids an icon system | One icon family (Lucide/Phosphor/Material Symbols) with consistent stroke and optical size; label meaningful icons |
| Side-stripe borders (`border-l-4`) on cards/alerts | Bootstrap-era affordance | Tinted surface + 1 px border + leading icon; or a left rail only in a real status list |
| Pure `#000` on `#fff` dark mode | No surface model | Near-black (`oklch(15% …)`) base, lighter surface = higher elevation, desaturated accents, 1 px alpha borders, glows instead of shadows |
| `lorem ipsum`, `placeholder.com`, `picsum.photos`, `unsplash.com/random` | Not designed with content | Real copy, real product media, or clearly marked assets the user must supply |
| `z-index: 9999`, `!important` sprinkled | No system | Z-index tokens (`--z-dropdown: 100` …) and `@layer` order |
| Skeleton shimmer for everything, fake progress %, infinite spinners | Pretend performance | Skeleton only after ~300 ms and matching final layout; determinate progress only when meaningful; optimistic UI where safe |
| Full-page preloader, scroll-jacking, autoplay hero carousel, custom cursor on touch | Hurt LCP, INP, a11y, conversion | Light intro that never blocks content; native scroll with ScrollTrigger; static hero with one motion focus; cursor effects only under `(hover: hover) and (pointer: fine)` |
| `<div onClick>`, `<a href="#">`, `outline: none` | Inaccessible by construction | `<button>`/`<a href>` with real destinations; `:focus-visible` ring 2 px, 3:1 contrast |
| Generic "Get Started" / "Learn more" / "Submit" / "Click here" | Says nothing | Name the outcome |

## Judgment heuristics (what the script cannot see)

- **The squint test.** Blur your eyes at 25% zoom: is there one unmistakable focal point per screen and per scroll beat?
- **The provenance test.** Could this page belong to any product? If yes, it has no visual world. Name one ("research lab notebook at noon", "midnight hardware gallery") and let it decide type, color, texture, and motion.
- **The evidence test.** Every claim has a demonstration, a number with a source, or a named customer. Remove what cannot be backed.
- **The hierarchy test.** Cover the hero: can you still tell what the product does in five seconds from the next section? Cover the headline: does the visual explain it?
- **The state test.** Open with empty data, a 400-character name, a translated string 35% longer, a failed request, an expired session. Is it still designed?
- **The repeat test.** Click the same button five times fast; open and close the drawer mid-animation; resize during a transition. Does everything land in a valid state?
- **The theft test.** Reference systems (Linear, Vercel, Stripe, Refero DESIGN.md) inform density, tone, and token logic. They are not to be reproduced; the result must be recognizably this product.

## Copy rules that de-slop faster than any CSS

- Lead with what, for whom, and the outcome; one primary CTA, one secondary low-commitment path.
- Buttons are verbs with objects. Links describe destinations.
- Error messages: what happened, what is affected, what to do next.
- Empty states: why empty, what to do, sample or template.
- Numbers get `tabular-nums`, units, and a time frame.
- Remove intensifiers (very, truly, seamlessly, effortlessly) and hedges (maybe, somewhat).

## When the user says "make it look premium"

Translate before building: which **mode** (Persuade/Operate/Read/Experience), which **visual world**, which **type pairing**, which **single signature motion**, which **budgets**, and which **reference DESIGN.md** for density. Then build the boring parts (states, forms, focus, loading) to the same standard as the hero. Premium is the sum of invisible details, not the hero alone.
