---
name: hero-design
description: Design, build, test, or redesign distinctive premium website heroes and coordinated landing-page sections using 21st saved lists, visual references, deliberate art direction, and purposeful GSAP or scroll motion when appropriate. Use for Hero Design requests, generic or AI-looking heroes, newly designed pages that need a visual test, and related carousels, marquees, imagery, or sections that need the same visual identity. Not for backend work or unrelated UI maintenance.
---

# Hero Design

Create a hero that belongs to this product or business. Premium means a clear visual idea, excellent composition, useful content, authentic assets, and precise execution; it does not automatically mean dark, minimal, expensive fonts, or more effects.

## Composition rule

Never default to the familiar two-column hero with headline/subheadline/buttons on one side and an image, mockup, or card on the other. Reversing the columns or adding gradients does not make it a new concept. Use that composition only when the user explicitly requests it, supplies it as the target, or requires preserving an incumbent layout. Explain the exception briefly.

Choose the composition from the story and references. Possibilities include an immersive full-bleed scene with integrated live type, a central artifact with surrounding narrative, an editorial typographic composition, a layered product stage, or a purposeful spatial sequence. These are possibilities, not templates to rotate through. Do not replace one default with a permanently centered headline or the same floating dashboard for every industry.

## 1. Establish the real brief

Inspect the requested route, adjacent sections, existing screenshots, real copy/assets, project instructions, framework, and design tokens. Read existing PRODUCT.md, DESIGN.md, and .21st context when present. Determine the audience, primary action, product evidence, and whether the request is a new design, refinement, or evaluation.

Ask only for missing information that materially changes the work. Do not ask the user to repeat confirmed choices. A hero-only request does not authorize a whole-site redesign. Preserve working navigation, content, analytics, and interactions outside the requested changes.

## 2. Use the design resources deliberately

Read [references/integrations.md](references/integrations.md) before research. Discover current tools instead of assuming names, connectivity, or entitlements.

- Use **21st-ui-build** for implementation. Browse the user's relevant 21st saved lists and run targeted catalog searches before selecting components. Paid access is a resource to use, not a reason to add irrelevant components.
- Use **Mobbin** website sections for comparable heroes and section composition when connected. Use screens for UI details; flows only when a journey matters.
- Use **refero-design** for style research and synthesis when available, including its appropriate references. Keep one dominant direction and give secondary sources narrow jobs.
- Use **impeccable** for the applicable design/build or critique workflow and craft evaluation. Run its context loader once per session in the actual project, then follow the relevant playbook. Do not initialize this skill's folder as a product.
- Use an **image generation tool** (see integrations for the Claude Code options) for assets or visual comps when imagery materially improves the result. Use **Superdesign** for UI exploration or visuals when its capabilities are connected and appropriate.
- Use **gsap-core** for coordinated interface animation and **gsap-scrolltrigger** for scroll-linked behavior. Use **scroll-world** only for a true continuous fly-through, diorama, or pre-rendered scroll-cinematic concept; it is not the default animation layer for an ordinary hero.

These resources serve one brief. Do not run overlapping interviews or collect conflicting full design systems. Carry the user's decisions and the chosen direction between skills. Their concrete workflows still apply; resolve competing aesthetic suggestions against the user's brief and existing visual authority.

Research must lead to decisions. Inspect the strongest previews and actual source/demo where available, then report a short source list with what each contributes. Metadata alone is not visual inspection. Stop when composition, type, media, and needed interactions have usable evidence. If a service is unavailable, name it once and continue with available references; never imply it was used.

## 3. Commit to one direction

Before editing UI, state a compact direction contract:

- Product story and primary action.
- Dominant composition and the specific reason it fits this product.
- Reference links/IDs and the exact traits being adapted.
- Typography roles, palette roles, spacing rhythm, and image/scene treatment.
- Desktop composition and mobile recomposition/crop.
- Required assets, motion purpose, and things the design must avoid.

Use the project's existing design authority for durable choices rather than creating competing token documents. Distinguish an internally chosen direction from one the user approved. Follow explicit requests for options or approval; otherwise make well-supported decisions within the authorized build. Respect any required decision step in an invoked workflow without asking again for an answer already given.

Use a static desktop view and mobile crop/recomposition to establish an ambitious animated scene before investing in full animation. Do not sell a written concept or generated screenshot as an implemented interface.

### Testing a newly designed page

When the user wants to test this skill on an existing page, preserve the page as evidence and run a before/after refinement workflow:

1. Launch the real route and capture desktop plus mobile before-state renders. Inspect the source, existing motion, fonts, assets, tokens, primary action, and any working interactions.
2. Research enough references to identify the largest gap between the current hero and a premium, product-specific direction. State the direction contract and the exact elements in scope.
3. Implement the strongest coherent revision in the actual page. Do not rebuild adjacent working sections merely to demonstrate the skill.
4. Add motion only after the static hierarchy, composition, and mobile layout work. Read [references/motion.md](references/motion.md) before introducing GSAP, ScrollTrigger, or scroll-world.
5. Render the same desktop and mobile views after the change and compare them against the contract. Exercise the primary action and any new motion before handoff.

## 4. Build a coherent site, not a collection of demos

Use the project's framework and existing primitives. Adapt retrieved components to the chosen design language; do not paste incompatible demo styling across sections. Inspect dependencies and code before installation, and use returned install instructions rather than inventing package names.

Keep a shared type system: consistent font families and role assignments, purposeful weights and scale, readable body copy, and deliberate line breaks. Choose fonts for the brand and verify availability/licensing; premium does not require buying fonts. Maintain coherent color roles, lighting, materials, contrast, borders, and motion across the requested sections. Consistency allows variation in layout and pacing.

Make the hero's dominant visual specific to the product, service, process, location, or outcome. Prefer authentic supplied assets and actual product captures when they establish credibility. Generated assets can establish atmosphere or explain a concept, but cannot fabricate customer proof, real premises, staff, testimonials, or product capabilities.

Keep headings, navigation, buttons, and essential labels as live accessible UI. For generated artwork, request appropriate negative space, crop tolerance, and a clean composition; avoid baking essential copy or controls into the image. Check generated media for artifacts and brand mismatch before using it.

Only add carousels, marquees, scroll sequences, gradients, glass, or 3D when they have a clear role. Do not use these as automatic signals of quality. Carousels need usable controls and access to their content; repeated marquee items must not duplicate announcements for assistive technology. Support reduced motion and preserve ordinary scrolling and keyboard access.

Recompose for mobile instead of shrinking the desktop scene. Preserve the focal point, reading order, action visibility, and legibility. Reserve media dimensions, avoid unnecessary heavy libraries, and optimize hero asset loading for the actual implementation.

## 5. Review before calling it complete

Read [references/review.md](references/review.md). Inspect the rendered desktop and mobile result together, fix the meaningful defects in one batch, and confirm once. Avoid an endless polish loop. Run relevant project checks and the applicable 21st/Impeccable review, using findings as evidence rather than blindly chasing a score.

If rendering or a dependency is blocked, complete unaffected work and state the exact verification limit. Do not claim visual QA from a build result.

Handoff concisely: direction achieved, actual reference sources and reused components, files changed, checks performed, and remaining limitations. Distinguish local implementation from any separately authorized deployment. Include a screenshot or preview when available.
