# Quality bar

The checklist to review against, condensed from a 140-point audit. Use it as acceptance criteria: pick the rows relevant to the surface, check the rendered, interactive product (not a screenshot), and order findings by user impact. Heuristics guide judgment; only real tasks with real users establish that a design works for its audience.

## Contents

1. Per-surface acceptance criteria
2. Purpose, content, trust
3. Visual system and art direction
4. Typography and reading
5. Navigation and wayfinding
6. Hero and landing sections
7. Controls, forms, overlays, direct manipulation
8. State, resilience, polish
9. Product-specific additions
10. Five rules against fragile "premium"

## 1. Per-surface acceptance criteria

| Surface | Must be true |
|---|---|
| Hero | Clear proposition, authentic visual, obvious action, fast primary content, mobile art direction; on expressive surfaces: a figure the product owns, a construction that is not headline-beside-card, and a multi-actor sequence visible in captured frames |
| Sections | Logical story, useful headings, varied but coherent composition, real evidence, accessible structure |
| Navigation | Current location, descriptive labels, keyboard and touch, deep links, back/forward, focus and scroll restoration |
| Pagination | Current page, sensible range, prev/next, clear disabled state, preserved filters/sort, URL state |
| Typography | Coherent roles, readable measure and leading, thoughtful wrapping, real text, stable fonts, script coverage |
| Forms | Persistent labels, autofill, clear validation, input recovery, loading/success/error, duplicate-submit handling |
| Modal / sheet | Correct label, focus lifecycle, dismissal, scroll handling, keyboard and insets, safe areas |
| Table / chart | Units and headings, meaningful selection and sort, responsive behavior, keyboard and textual alternatives |
| Empty / loading / error | Explain the state and the next action; preserve layout and work; useful retry |
| Motion | Purpose, consistent timing, interruption and reversal, bounded cost, meaningful reduced-motion equivalent; on expressive surfaces the floor is met (hero sequence, one pinned set piece, 3+ named micro-interactions) and fade-up is not the only motion |

## 2. Purpose, content, trust

- Primary task identifiable at a glance; next action obvious.
- Audience fit: expertise, language, device, environment, time pressure.
- Information architecture matches users' mental models; important paths validated.
- One name per object and action across screens and help.
- Progressive disclosure: frequent decisions immediate, specialist options exposed when useful.
- Evidence-based claims: real demonstrations, permissioned testimonials, qualified metrics. Never fabricated proof.
- Honest pricing: renewal, trial, cancellation, limits, required steps stated before commitment.
- Action language names the outcome ("Save changes", "Create project").
- Error language: what happened, what is affected, how to recover.
- Frequently changing copy and imagery have an editable home.
- Help in context without losing work.
- Ethical choice architecture: dismissal, consent, cancellation, deletion understandable.
- Research loop: observe completion and errors; evidence over preference.
- Inclusive imagery, names, examples, alt text, localization.
- Success measures (completion, time, recovery, comprehension, confidence) defined before polishing.

## 3. Visual system and art direction

- One deliberate visual direction tied to product and audience.
- Hierarchy from size, weight, position, space, and contrast establishes reading order.
- A spacing scale with optical corrections; no magic uniform 8 px.
- Optical alignment of icons, letters, controls, illustrations.
- Recompose at small sizes; prioritize content rather than shrinking uniformly.
- Intrinsic layouts: real content sets heights; long names, translations, missing media handled.
- Components respond to their container, not only the viewport.
- Density options for productive audiences without careless hit-target shrinkage.
- Negative space separates meaningful groups without inflating page length.
- Clear surface hierarchy: page, panels, overlays, active, disabled.
- Semantic color roles; contrast tested on real pairs including translucent surfaces and images.
- Complete dark mode (imagery, shadows, borders, chart colors, focus), not an inversion.
- System preference respected initially; explicit choice persisted without flash.
- Material effects (glass, gradients, grain, bevels, shadows) clarify the chosen world rather than decorate.
- Authentic media with rights; focal points and separate mobile crops.
- One icon grammar: stroke, fill style, optical size.
- Data color never relies on hue alone.
- Governed system: tokens centralized; component contracts, variants, states, ownership, versioning, deprecation documented.

## 4. Typography and reading

- Type family chosen for tone, legibility, script coverage, license, delivery cost.
- Roles specified: display, headings, body, labels, captions, code, numeric.
- Bounded fluid scale usable at zoom and large accessibility settings.
- Measure 45–75 ch as a starting range; leading set per size and script; tracking adjusted sparingly.
- Balanced headline breaks via wrapping controls, not brittle manual breaks.
- Tabular numerals in aligned data; fractions and ligatures where supported; optical sizing where the font has it.
- Fallback metrics matched; space reserved; readable content never hidden waiting for fonts.
- Subsets ship required scripts and weights only, preserving glyphs real content needs.
- Meaningful text stays as real text, selectable and searchable; never baked into images or canvas.
- Real headings, lists, captions, quotes, tables, meaningful link labels.
- RTL and mixed-script tests; user text overrides (resize, spacing, system fonts, high contrast) survive.

## 5. Navigation and wayfinding

- Global navigation stable across routes; current location marked; breadcrumbs where hierarchy warrants.
- Links navigate, buttons act; open-in-new-tab preserved.
- Visible focus and a meaningful sequence; widget-specific keys correct; skip link.
- Menus work by click/tap and keyboard; no hover-only access; no accidental dismissal; mega-menus with sensible focus, escape, pointer travel.
- Mobile reach: thumb zone, safe areas, orientation, foldables, split-screen, on-screen keyboard.
- Sticky UI never hides focused elements or consumes the viewport.
- Refresh, deep links, back/forward, document titles work; scroll and focus restored after route changes.
- Search handles synonyms, typos where useful, loading, no results, query preservation.
- Command palette: discoverable shortcuts, scoped results, non-palette alternatives for essential actions.
- Tabs vs navigation semantics match behavior.
- Numbered pagination shows current, nearby, prev/next, disabled, totals when known; URL state preserved; cursor pagination does not imply arbitrary jumps; "load more" preserves context and footer reach; infinite feeds restore position and remain keyboard-accessible; filter/sort continuity explicit.

## 6. Hero and landing sections

- Product, audience, benefit, next action communicated promptly; demonstrative media keeps the message readable.
- The first viewport could not be reskinned for another product by swapping copy; the hero figure is derived from what the product does (`SKILL.md` §1), and the construction is not the two-column headline-beside-card default (`SKILL.md` §3).
- Captured frames during the hero and at several scroll depths show the figure, type, and CTA changing state; a page that reads as static fails on expressive surfaces.
- No card with large dead space; no clipped or colliding text; no horizontal overflow at 390 px; copy never names a layout position.
- Section headlines span the top of their section on two balanced lines at desktop width; none sit in a narrow column beside empty space.
- Pinned stages keep header and figure together; live readouts stay on or beside the moving marker; labels near a marker read clearly as a range, title, or current value.
- Every time, quantity, and span in copy agrees with the figure's data. Charts reach the end of their axis with first and last labels fully visible.
- Product pages include a playable instrument with computed output, touch support, and a keyboard path.
- Standard components such as pricing were sourced from 21st.dev or shaped with Impeccable, then adapted to the page; a plain three-card table fails.
- Focused conversion path: one primary CTA, a sensible secondary.
- Actual LCP content prioritized; decorative 3D and video progressive.
- Hero reframed at phone and tablet widths.
- Credible proof: real case studies, supported outcomes, customers, source context.
- Section narrative: need, mechanism, evidence, objections, action; varied rhythm in one system.
- Features explain outcomes and show the feature working; no interchangeable icon-card filler.
- Comparison tables truthful and readable on mobile; pricing comprehensible; FAQ answers real objections with accessible disclosures.
- Contact path real with validation, delivery states, recovery; footer useful.
- Non-blocking storytelling: visitors reach content and act without waiting through an intro or scroll sequence.

## 7. Controls, forms, overlays, direct manipulation

- Complete control states: default, hover (where available), focus, pressed, selected, disabled, busy, success, error.
- Obvious hit areas; no visual-only hover affordance; immediate acknowledgment of press.
- Persistent labels; correct input types, `autocomplete`, `inputmode`, capitalization, autofill.
- Validation at useful moments; partially entered values not punished; error summary linked to fields and associated programmatically.
- Appropriate input preserved after failure; passwords and payment data never auto-persisted; password managers and paste allowed; show-password control.
- Multi-step: meaningful progress, saved state, safe revisiting.
- Uploads: preview, constraints, progress, cancel, retry, specific rejection reasons.
- Dates: keyboard entry, timezone and locale explained.
- Destructive actions: confirmation proportional to impact; undo when feasible.
- Modals: labeled, initial focus appropriate, interaction contained, focus restored on close. Popovers are not modals; dismissal and focus deliberate. Tooltips never hide essential information; keyboard equivalents exist.
- Bottom sheets: scroll/drag conflicts resolved, snap points, keyboard, safe areas, explicit dismissal.
- Toasts supplemental; critical failures and required actions remain discoverable.
- Drag alternatives for reorder, move, resize; gesture arbitration (scroll vs swipe vs long-press vs drag) without accidental activation; haptics restrained and preference-aware.
- Bulk actions: scope, count, exceptions, consequences explicit. Resizable workspaces keep minimums and keyboard alternatives. Editors: undo/redo, selection consistency, autosave status, recovery. Tables: headers, sorting, filtering, density, column behavior, accessible alternatives.

## 8. State, resilience, polish

- Intentional empty states with the useful next action.
- Loading UI proportional to actual delay: immediate feedback, skeletons, determinate progress, or background work.
- Progress percentages only when meaningful; uploading, processing, completion distinguished.
- Optimistic interaction only when safe; server response reconciled; rollback visible; retry context preserved.
- Stale data visible where decisions depend on freshness; no silent replacement mid-interaction.
- Offline/reconnect: capabilities, queue states, conflicts, what is actually saved.
- Duplicate submissions and payments prevented without stranding users.
- Partial failures keep working sections usable; retries near the failed content.
- Session expiry warned when useful; drafts recovered after re-authentication.
- Permission and role states explain unavailable actions without leaking protected data.
- Screen-reader semantics: names, roles, values, landmarks, headings, bounded live announcements.
- Reduced motion removes nonessential movement while preserving state changes and feedback; looping media, sound, flashes, persistent distractions controllable.
- High contrast / forced colors tested; state never encoded only in background images.
- Localization: string expansion, currencies, calendars, plurals, RTL, language-specific input.
- Charts: labels, units, legends, keyboard access when interactive, text/table alternatives.
- Adaptive devices: slow CPU, memory pressure, tablets/foldables, window resizing, zoom, external keyboards, mixed input, screen readers.
- Consistent animation grammar: shared durations, springs, easing, origins, entry/exit conventions.
- Correct cancellation: animations and pending actions interruptible without jumps or stale state.
- Quiet operation: rendering paused when hidden/off-screen; no battery-draining decoration.
- Accurate completion feedback: success means the action succeeded.
- Polish measured alongside task results, field performance, and support evidence.

## 9. Product-specific additions

- Commerce: real stock and totals, transparent shipping, guest checkout where suitable, recoverable payment errors, receipts and order status.
- Auth / onboarding: permissions explained in context, passkeys/autofill, first meaningful success easy.
- AI / chat: generated vs sourced content distinguished, streaming and stop state, edits preserved, review of consequential actions, token-by-token rendering that does not jitter (fixed-width placeholders, `tabular-nums`, `use-stick-to-bottom`).
- Collaboration: meaningful presence, conflict handling, revision history, permissions, understandable sync.
- Media: captions, transcripts, keyboard controls, accessible progress, volume, rate, buffering recovery.
- Maps: accessible search/list alternatives, understandable clusters, permission context, controllable zoom.
- Notifications: priorities, preferences, read state, batching, useful destinations, explicit outcomes.
- Account / settings: searchable organization, saved-state clarity, theme/language, data export, cancellation and deletion workflows.

## 10. Five rules against fragile "premium"

1. One primary component system and one principal motion strategy; specialists only for concrete requirements.
2. Real content and real tasks before decoration.
3. Keyboard, touch, screen reader, reduced motion, failure, and recovery are part of the design, not a pass at the end.
4. Current docs, release channel, license, maintenance, and platform support reviewed before adoption.
5. The delivered experience is judged by task completion and measured runtime behavior alongside visual quality.
