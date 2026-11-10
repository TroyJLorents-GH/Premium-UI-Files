# Hero, direction contract, and typography

Adapted from the installed `hero-design` skill (`~/.claude/skills/hero-design/`). That skill is unchanged and can still be invoked on its own; this file carries its working method into flagship builds. When the task is hero-only, invoking `hero-design` directly is equally valid. Read its `references/integrations.md` for live tool routing (21st saved lists, Mobbin, Refero, Impeccable, image generation, Superdesign).

## 1. Establish the real brief

Before any design decision, inspect what already exists: the route, adjacent sections, screenshots, real copy and assets, project instructions, framework, tokens, and any PRODUCT.md, DESIGN.md, or `.21st` context. Determine the audience, primary action, product evidence, and whether the request is a new design, a refinement, or an evaluation.

Ask only for information that changes the work. A hero-only request does not authorize a whole-site redesign; preserve working navigation, content, analytics, and interactions outside scope.

## 2. Research must lead to decisions

Use the resources in one pass, against one brief:

- **21st**: the user's saved lists first (list them, open the relevant ones by real ID), then targeted catalog searches for the actual section. Search returns metadata; fetch and read the source before adopting anything.
- **Mobbin** website sections for comparable compositions; screens for UI details; flows only when a journey matters.
- **Refero** for visual language: one dominant direction, secondary sources with narrow jobs.
- **Impeccable** for the build or critique playbook and its craft floor.
- **Image generation / Superdesign** only when imagery or a comp materially improves the result (Higgsfield disclosure rule applies).

Inspect previews and real source or demos; metadata alone is not visual inspection. Stop once composition, type, media, and interactions have usable evidence. Report a short source list: link or ID, and the exact trait each one contributes. If a service is unavailable, name it once and continue; never imply it was used.

## 3. The direction contract

Write this before editing UI. It is short, specific, and checked against the render at the end.

| Field | Content |
|---|---|
| Story and action | What the product does, for whom, and the one primary action |
| Composition | The hero construction (SKILL.md §3) and the specific reason it fits this product |
| References | Links or IDs, and the traits taken from each |
| Typography roles | Display, text, and data/label faces; weights and axes used; scale; why these faces fit (§5 below) |
| Palette roles | Background steps, text levels, one accent and where it is allowed |
| Spacing rhythm | Section padding, the grid, where density changes |
| Image / scene treatment | Real, generated, or drawn; crop; focal point |
| Desktop and mobile | The desktop composition and the mobile recomposition (crop, reading order, what stays in the first `100dvh`) |
| Motion purpose | What motion clarifies; not a list of effects |
| Avoid | The specific defaults this page must not fall into |

Mark whether the direction was chosen internally or approved by the user.

## 4. Static first, then motion

Establish the static desktop view and the mobile recomposition before animating. Hierarchy, crop, and type must work with motion off; motion is added only after that, and the reduced-motion path must reveal the complete content. A written concept or a generated screenshot is never presented as an implemented interface.

## 5. Typography selection

Fonts carry most of the first impression, and models reach for the same few pairings. Choose faces for this brand, not for "premium".

**Roles.** Assign a face per role: display (headlines, hero, big numbers), text (body, UI), and, when the page shows data, a data/label face (tabular figures, chart labels, readouts, eyebrows). Two families can cover three roles if one has the range; one family covering everything needs real axis range (width, weight, optical size), not just 400 and 700.

**Saturated defaults: do not pick these without a reason the brief states.**

- Instrument Serif + Inter (the stock AI landing-page pairing)
- Inter, Geist, or DM Sans alone at default weights
- Playfair Display or Fraunces headings over Inter body
- Space Grotesk as the "techy" display face
- Geist + Geist Mono as an automatic dev-tool pair

These are not bad fonts; they are the ones a reader has already seen on a hundred generated pages, so they read as template.

**Selection procedure.**

1. Take the concept's feeling word (SKILL.md §1) and the domain. Write what the type has to say: measured and instrumental, warm and editorial, blunt and industrial, and so on.
2. Shortlist three to five candidates from Google Fonts, Fontshare, or the project's licensed set (Adobe Fonts tools can recommend and preview when connected). Prefer variable fonts.
3. Check each: weights or axes available (a display face with one weight can only make hierarchy through size and italic), tabular and lining figures if numbers appear, glyph coverage for the copy's languages, and license for web use.
4. Preview the real headline, a real paragraph, and a real number at their real sizes. Reject faces that only look good in a specimen.
5. Record the choice and reason in the direction contract. Self-host or load with exact families and axes, `font-display: swap` plus metric-matched fallbacks, and preload the display face if it is the LCP text.

**Craft.** `clamp()` scale with clear steps; negative tracking only at display sizes; `text-wrap: balance` on headings and `pretty` on paragraphs; measure 60–75 characters for body; `tabular-nums` on anything live; small caps or tracked uppercase only from a face that has the weights for it.

## 6. Coherence

Every section uses the same font roles, color roles, spacing rhythm, image treatment, and motion grammar; layout and pacing can vary. Adapt retrieved components to the page's tokens rather than pasting demo styling. Keep headings, navigation, buttons, and essential labels as live accessible UI; never bake copy into images. Carousels, marquees, glass, gradients, and 3D appear only with a role. Generated media never fabricates proof (customers, premises, staff, testimonials, capabilities).

## 7. Before/after on an existing page

When redesigning or testing on a page that already exists:

1. Render the real route at 1440 × 900 and 390 × 844 and keep those captures as the before state. Read the source, motion, fonts, assets, tokens, and primary action.
2. Identify the largest gap between the current page and a product-specific direction. Write the contract and the exact elements in scope.
3. Implement the strongest coherent revision in the real page. Do not rebuild working adjacent sections to show off.
4. Add motion after the static composition works on both viewports.
5. Render the same views after, compare against the contract, exercise the primary action and new motion, and report the comparison.

## 8. Review cadence

One batched inspection of desktop and mobile together, one batch of fixes, at most one confirmation pass unless a functional failure appears. Do not claim visual QA from a build result. Hand off with: direction achieved, actual sources and reused components, files changed, checks run, remaining limitations.
