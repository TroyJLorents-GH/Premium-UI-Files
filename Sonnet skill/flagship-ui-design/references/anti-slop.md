# Anti-slop rules

Slop is what you get when the model reproduces the statistical median of every landing page it has seen. Each item below is a tell, why it reads as generated, and what to do instead. Run this list as a pre-flight on direction and again on the rendered result.

The brief wins: if the user explicitly pins a look (a purple gradient, Inter, glass cards), honor it and execute it with craft. Redirecting a clear brief toward your taste is a failure. These rules govern *defaults*.

## Visual tells

| Tell | Why it reads as AI | Instead |
|---|---|---|
| Purple→blue/indigo gradient on near-black, glowing blurred orbs | The single most common generated palette | Derive color from the product's world (material, era, industry). Tint neutrals toward the brand hue in OKLCH; one accent, used for action only. |
| Inter / system sans for everything, one weight, no hierarchy | No typographic decision was made | Pair a distinctive display face with a quiet text face (2 families max). Use contrast in size, weight, and tracking. Set optical sizing, `text-wrap: balance` on headings, `pretty` on body. |
| Three identical rounded feature cards with icon + title + 2 lines | Template skeleton | Vary scale and composition: asymmetric bento, one dominant card, a live mini-demo inside a card, editorial two-column with real imagery. |
| Everything centered, symmetric, same padding | Safe layout with no tension | Establish a grid, then break it once on purpose. Use scale contrast, off-axis anchors, deliberate whitespace. |
| Emoji or generic icon-in-circle as illustration | Placeholder energy | Real product UI, photography, bespoke SVG, or a consistent icon set (Lucide/Phosphor) at one stroke weight. |
| Glassmorphism on every surface | Effect used as decoration | One or two glass layers max, over varied content, with a 1px specular border and a solid fallback for reduced-transparency. |
| Gradient text on every headline | Reflex | Reserve for at most one phrase, or drop. |
| Uniform 16px radius everywhere | No system | Nest radii (`R_outer = R_inner + padding`); match radius to the brand's character. |
| Flat single `box-shadow: 0 4px 6px` | No light model | Layered ambient shadows (4–6 layers, doubling offset/blur) plus a 1px hairline; on dark UIs elevate with lighter surface tints and top-edge highlights instead. |
| Stock-photo handshake / floating 3D blob / abstract mesh as "hero image" | Says nothing about the product | Show the real product, a real dataset, or a purpose-made visual tied to the claim. |
| Pure `#000` background and `#fff` text | Harsh, unconsidered | Obsidian-style base (e.g. `#07090E`) and off-white; check contrast, not vibes. |
| Fake dashboards with meaningless charts | Decorative data | Use plausible, labeled, internally consistent sample data, marked as sample. |

## Copy tells

- "Revolutionize / Supercharge / Unlock / Seamless / Elevate your workflow." Replace with a specific noun, number, or outcome.
- Headline stacked with a three-word fragment cadence ("Fast. Simple. Powerful.").
- Generic CTAs ("Get Started", "Learn More", "Submit"). Use verb + object + (risk reducer): "Start free trial · no card".
- Invented testimonials, metrics, customer logos. Never ship these; mark placeholders loudly.
- Lorem ipsum anywhere visible.

## Motion tells

- Everything fades up 20px on scroll with the same delay. Vary by role; reveal only what matters; lock text once revealed.
- Bounce/elastic on large surfaces; linear easing on UI movement.
- Parallax on everything, scroll-jacking, auto-rotating hero carousels, custom cursors on touch, full-page preloaders that delay LCP.
- Looping ambient animation with no pause off-screen or under reduced-motion.
- Hover effects with no keyboard-focus equivalent.

## Structural tells

- Hero → logos → 3 features → testimonial → pricing → CTA with no argument connecting them. Write the page's *story* first (problem → insight → proof → action) and let sections serve it.
- Only the happy path designed. No empty/loading/error/long-content/offline state.
- `div` soup with click handlers; missing focus styles; tiny tap targets.
- Components copied from a registry without reading them (unused deps, no reduced-motion, hard-coded colors).

## The squint and swap tests

- **Squint test:** blur your eyes (or view at 25%). Is there one unmistakable focal point per viewport? If three things compete, cut two.
- **Swap test:** replace the logo and copy with a competitor's. If nothing else needs to change, the design carries no identity. Fix by tying visual decisions to product truth.
- **Screenshot test:** would a stranger guess the product category from a blurred screenshot? If it could be any SaaS, it is slop.

## When a design feels flat or generic: escalate in this order

1. Typography (scale contrast, a real display face, tighter tracking on large type).
2. Composition (asymmetry, overlap, cropped imagery, one oversized element).
3. Color discipline (reduce, tint neutrals, one accent).
4. Material and light (grain, layered shadow, specular borders, one spotlight).
5. Motion (one signature interaction, then stop).
6. Only then: 3D / shaders, with a poster fallback and a performance budget.
