# Premium UI/UX Field Guide

**A practical reference for websites, landing pages, web applications, mobile applications, desktop software, and individual interface components.**

Research snapshot: **November 6, 2026 · America/Phoenix**. Prepared for Troy.

**Inventory:** 140 quality checks · 341 catalog entries (280 V / 61 R) · 24 motion patterns · 15 promising design repositories.

## Contents

- [1. Read this first](#1-read-this-first)
- [2. Fast selection guide](#2-fast-selection-guide)
- [3. The qualities to specify before selecting tools](#3-the-qualities-to-specify-before-selecting-tools)
- [4. Surface-by-surface build recipes](#4-surface-by-surface-build-recipes)
- [5. Browser-native layout, typography, and interface capabilities](#5-browser-native-layout-typography-and-interface-capabilities)
- [6. Motion, transitions, graphics, and creative rendering](#6-motion-transitions-graphics-and-creative-rendering)
- [7. Components, design systems, and design workflow](#7-components-design-systems-and-design-workflow)
- [8. Platform, architecture, performance, accessibility, and QA reference](#8-platform-architecture-performance-accessibility-and-qa-reference)
- [9. Styling systems, prototyping, and research tools](#9-styling-systems-prototyping-and-research-tools)
- [10. How to achieve smooth motion in practice](#10-how-to-achieve-smooth-motion-in-practice)
- [11. Choosing and maintaining a toolset](#11-choosing-and-maintaining-a-toolset)
- [12. A reusable brief for AI-assisted UI/UX work](#12-a-reusable-brief-for-ai-assisted-uiux-work)
- [13. Keeping this reference useful](#13-keeping-this-reference-useful)

## 1. Read this first

Premium UX combines clear purpose, visual craft, predictable interaction, accessibility, speed, and reliability. GSAP and Three.js are implementation tools within that larger system. A well-built native control can deliver a more polished experience than a complicated custom effect.

No honest document can enumerate every UI technique, package, plugin, or private design system. This guide is a broad, organized inventory of the most useful categories and candidates, with explicit evidence boundaries. It is designed to be extended as the ecosystem changes, not treated as a universal ranking.

**How to use it:** choose the surface and user task; use the quality checklist; select the smallest compatible toolset; prototype the hardest interaction; test it on representative devices; then add expressive details within the performance budget.

### Evidence and relevance legend

- **V — inspected:** an official documentation page or project repository was inspected during this research. This verifies the described capability, not every version, browser, license term, or maintenance metric.
- **R — reference candidate:** linked for discovery; its current documentation or maintenance was not individually verified in this pass. Recheck before selecting it.
- **Emerging / limited / beta / legacy / commercial:** specific cautions, where stated. These are independent of V/R.
- **Recommended fit:** editorial judgment about the stated use case, not a measured head-to-head performance result.
- **Promising repository:** useful direction worth evaluating. It does not mean verified GitHub Trending placement, rapid growth, or guaranteed production quality.

The catalogs include tools, platform APIs, standards, and plugins. Counts describe **catalog entries**, not hundreds of independent packages to install. Subfeatures are identified as such. No packages were installed or benchmarked for this report.

## 2. Fast selection guide

| Need | First candidates to evaluate | What earns the choice |
|---|---|---|
| Buttons, focus, hover, basic disclosure | Semantic HTML, native CSS transitions | Minimal complexity; direct feedback; keyboard support |
| Complex branded sequences and scroll stories | GSAP + selected plugins | Timeline control, orchestration, responsive cleanup |
| Component enter/exit and layout transitions | Motion; framework transitions; native View Transitions where appropriate | Interruptible state changes tied to real UI |
| Spring-based direct manipulation | Motion, react-spring, native platform springs | Velocity continuity and gesture response |
| Marketing 3D / configurators | Three.js or Babylon.js; React Three Fiber for React | Camera/material control and actual interactive 3D value |
| Lightweight object preview | model-viewer | Product viewing without a custom engine architecture |
| 2D animated illustration | Rive; Lottie / dotLottie | Designer-authored assets with a suitable runtime |
| Production app controls | React Aria, Base UI, Radix, Ark UI, or platform-native controls | Focus, keyboard, semantics, composition |
| A substantial app in an established ecosystem | MUI, Mantine, Ant Design, Fluent, or the corresponding native system | Cohesive components, density, documentation, maintainability |
| Branded components you own | shadcn/ui and carefully selected source registries | Editable source and explicit ownership of updates |
| Visual inspiration / experiments | React Bits, Magic UI, Aceternity, 21st.dev | Distinct patterns to adapt and verify |
| AI design discipline | Impeccable and focused design skills | Better briefs, critique, typography, responsiveness, hardening |
| Large collections | Pagination + suitable table/list virtualization | Stable selection, URL state, memory and navigation behavior |
| Mobile-native feel | SwiftUI/UIKit; Compose; or deliberate RN/Flutter implementations | OS navigation, gestures, text scaling, keyboard, haptics |
| Quality verification | Browser profilers + real-user metrics + accessibility/manual tests | Evidence from the rendered, interactive product |

These are starting candidates. Their detailed catalogs below provide primary links and caveats. Avoid installing several animation engines or component systems to solve the same job.

## 3. The qualities to specify before selecting tools

The following is an original product-design checklist. Use its rows as acceptance criteria, selecting those relevant to the product. General foundations include [Nielsen Norman Group's usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), [W3C's ARIA patterns](https://www.w3.org/WAI/ARIA/apg/patterns/), and the accessibility requirements in the performance/accessibility section. Heuristics guide judgment; user research establishes whether a particular design works for a particular audience.

### Purpose, content, trust, and product structure

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q001 | Clear primary task | Can the visitor identify what the product does and what to do next? |
| Q002 | Audience fit | Match expertise, language, device, environment, and time pressure. |
| Q003 | Information architecture | Group content by users' mental models; validate important findability paths. |
| Q004 | Consistent vocabulary | Use one name for each object and action across screens and help. |
| Q005 | Progressive disclosure | Keep frequent decisions immediate; expose specialist options when useful. |
| Q006 | Evidence-based claims | Use real product demonstrations, testimonials with permission, and qualified metrics. |
| Q007 | Honest pricing and commitments | Explain renewal, trial, cancellation, limits, and required steps before commitment. |
| Q008 | Clear action language | Prefer “Save changes” or “Create project” when that is the actual outcome. |
| Q009 | Useful error language | Explain what happened, what is affected, and the next recovery action. |
| Q010 | Content ownership | Give frequently changing copy, cards, ordering, and imagery an editable home. |
| Q011 | Context-preserving help | Provide contextual documentation and assistance without losing user work. |
| Q012 | Ethical choice architecture | Make dismissal, consent, cancellation, and account deletion understandable. |
| Q013 | Research and feedback loop | Observe task completion and errors; prioritize evidence over a designer's preference. |
| Q014 | Inclusive identity and imagery | Use appropriate names, examples, representation, alt text, and localization. |
| Q015 | Task-based success measures | Define completion, time, recovery, comprehension, and user confidence before polishing. |

### Visual system, layout, and art direction

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q016 | Deliberate visual identity | Choose a coherent visual direction tied to the product and audience. |
| Q017 | Strong hierarchy | Size, weight, position, space, and contrast establish a clear reading order. |
| Q018 | Consistent spacing | Use a deliberate spacing scale with optical corrections; no magic requirement to use 8 px everywhere. |
| Q019 | Optical alignment | Align perceived edges of icons, letters, controls, and illustrations. |
| Q020 | Responsive composition | Recompose at small sizes; prioritize content instead of uniformly shrinking it. |
| Q021 | Intrinsic layouts | Let real content determine height; handle long names, translated strings, and missing media. |
| Q022 | Component adaptation | Components respond to their container, not only the viewport. |
| Q023 | Density options | Support productive dense views when the audience needs them, without shrinking hit targets carelessly. |
| Q024 | Negative space with purpose | Separate meaningful groups; preserve scanning and avoid unnecessary page length. |
| Q025 | Clear surface hierarchy | Differentiate page, panels, overlays, active items, and disabled controls. |
| Q026 | Color roles | Define semantic foreground, background, action, warning, error, and success tokens. |
| Q027 | Accessible contrast | Test actual foreground/background pairs, including translucent surfaces and images. |
| Q028 | Complete dark mode | Reconsider imagery, shadows, borders, chart colors, and focus; avoid merely inverting colors. |
| Q029 | System and user theme choice | Respect system preferences initially where appropriate; persist explicit choices without theme flash. |
| Q030 | Controlled material effects | Glass, gradients, grain, bevels, and shadows should clarify the chosen visual world. |
| Q031 | Authentic media | Use product-specific photos, illustrations, renders, or demonstrations with appropriate rights. |
| Q032 | Crop direction | Define focal points and separate mobile crops when composition demands them. |
| Q033 | Consistent icon grammar | Match stroke, filled/outlined treatment, optical size, and recognizability. |
| Q034 | Data-appropriate color | Do not rely on hue alone; use labels, shapes, and patterns where needed. |
| Q035 | Governed design system | Centralize tokens; document component contracts, variants, states, ownership, versioning, and deprecation/migration policy. |

### Typography and reading

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q036 | Purposeful type family | Choose for tone, legibility, script coverage, licensing, and delivery cost. |
| Q037 | Clear type roles | Specify display, headings, body, labels, captions, code, and numeric data. |
| Q038 | Fluid sizing | Use bounded scales; text remains usable with zoom and large accessibility settings. |
| Q039 | Comfortable measure | Tune line length to font, language, device, and reading task; roughly 45–75 characters is a useful prose starting range, not a universal requirement. |
| Q040 | Appropriate leading | Set line-height for size and script; avoid clipping accents and large text. |
| Q041 | Deliberate tracking | Adjust display text sparingly; preserve readability in small labels and body copy. |
| Q042 | Balanced headline breaks | Use text wrapping controls and editorial judgment; avoid brittle desktop-only manual line breaks. |
| Q043 | OpenType features | Use tabular numerals in aligned data, appropriate fractions, and supported ligatures. |
| Q044 | Optical sizing | Use a font's optical-size axis where supported and useful. |
| Q045 | Font loading stability | Match fallback metrics; reserve space; avoid hiding readable content for font downloads. |
| Q046 | Font subsetting | Ship required scripts/weights; preserve glyphs needed by real user content. |
| Q047 | Selectable, searchable text | Keep meaningful text in real text layers rather than baking it into images/canvas. |
| Q048 | Rich text structure | Use real headings, lists, captions, quotes, tables, and meaningful link labels. |
| Q049 | RTL and script support | Test mixed direction text, numerals, line breaking, and culturally suitable fonts. |
| Q050 | User text overrides | Remain usable with text resize, spacing overrides, system fonts, and high contrast. |

### Navigation, wayfinding, and pagination

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q051 | Predictable global navigation | Keep major destinations and labels stable across routes. |
| Q052 | Visible current location | Mark active page/section; provide breadcrumbs where hierarchy warrants them. |
| Q053 | Semantic destination vs action | Links navigate; buttons perform actions; preserve open-in-new-tab behavior. |
| Q054 | Keyboard navigation | Provide visible focus and a meaningful sequence; use widget-specific keys correctly. |
| Q055 | Skip navigation | Let keyboard users reach primary content efficiently. |
| Q056 | Accessible menu behavior | Support click/tap and keyboard; avoid hover-only access and accidental dismissal. |
| Q057 | Mega-menu discipline | Group links clearly; provide sensible focus, escape, and pointer travel behavior. |
| Q058 | Mobile navigation reach | Accommodate thumb reach, safe areas, orientation, foldables, split-screen, and the on-screen keyboard. |
| Q059 | Sticky UI restraint | Keep useful controls available without hiding focused elements or consuming the viewport. |
| Q060 | Route state and history | Support refresh, deep links, browser back/forward, and meaningful document titles. |
| Q061 | Scroll and focus restoration | Restore previous list position; place focus appropriately after route changes. |
| Q062 | Search quality | Handle synonyms, typo tolerance where useful, loading, no results, and query preservation. |
| Q063 | Command palette | Provide discoverable shortcuts, scoped results, and alternatives for essential actions. |
| Q064 | Tabs and segmented controls | Match semantics to behavior; avoid masquerading navigation links as application tabs. |
| Q065 | Numbered pagination | Show current page, nearby pages, previous/next, disabled states, and total information when known. |
| Q066 | Pagination URL state | Preserve page, filters, sorting, and page size in shareable state where appropriate. |
| Q067 | Cursor pagination | Use stable cursor ordering for changing feeds; do not imply reliable arbitrary page jumps. |
| Q068 | Load more | Preserve context and expose count/progress; keep footer and controls reachable. |
| Q069 | Infinite feed recovery | Restore position on return; support keyboard access and avoid inaccessible endless content. |
| Q070 | Filter/sort continuity | Reset page only when appropriate; retain selections predictably and explain scope. |

### Heroes, landing pages, and page sections

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q071 | Hero comprehension | Communicate the product, audience, benefit, and next action promptly. |
| Q072 | Demonstrative hero media | Show the actual product or a relevant authored scene; keep the core message readable. |
| Q073 | Focused conversion path | Establish a clear primary CTA and a sensible secondary path. |
| Q074 | Fast hero delivery | Prioritize the actual LCP content; load decorative 3D/video progressively. |
| Q075 | Responsive art direction | Reframe hero imagery and motion at phone/tablet widths. |
| Q076 | Credible proof | Present real case studies, supported outcomes, customers, and source context. |
| Q077 | Section narrative | Build a logical sequence: need, mechanism, evidence, objections, action as appropriate. |
| Q078 | Varied section rhythm | Vary composition and density while keeping one visual system. |
| Q079 | Feature clarity | Explain user outcomes and show the feature working; avoid interchangeable icon-card filler. |
| Q080 | Comparison integrity | Use meaningful criteria and truthful limitations; make comparison tables readable on mobile. |
| Q081 | Pricing comprehension | Make billing periods, included usage, exclusions, and plan differences clear. |
| Q082 | FAQ discoverability | Answer real objections; use accessible disclosures and readable direct links where useful. |
| Q083 | Functional contact path | Use a real submission path with validation, delivery states, and recovery. |
| Q084 | Useful footer | Include navigation, support, identity, legal/account paths appropriate to the business. |
| Q085 | Nonblocking storytelling | Visitors can reach content and act without waiting through an intro or scroll sequence. |

### Controls, forms, overlays, and direct manipulation

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q086 | Complete control states | Default, hover where available, focus, pressed, selected, disabled, busy, success, and error. |
| Q087 | Obvious hit areas | Make interactive targets easy to acquire; no visual-only hover affordance. |
| Q088 | Immediate acknowledgment | Press/tap gets feedback promptly, even when completion takes longer. |
| Q089 | Persistent field labels | Keep labels available while entering data; placeholders supplement labels. |
| Q090 | Helpful input configuration | Correct input types, autocomplete, inputmode, capitalization, and autofill support. |
| Q091 | Timely validation | Validate at useful moments; explain correction without punishing partially entered values. |
| Q092 | Error summary and association | Link summaries to fields and associate errors programmatically. |
| Q093 | Preserve appropriate user input | Recover suitable drafts after failures; avoid automatically persisting passwords, payment credentials, or sensitive shared-device content. |
| Q094 | Password-manager compatibility | Allow paste/autofill and accessible show-password controls. |
| Q095 | Multi-step orientation | Show meaningful progress, save state, and permit revisiting earlier steps safely. |
| Q096 | Upload usability | Preview, file constraints, progress, cancellation, retries, and specific rejection reasons. |
| Q097 | Date and time clarity | Support keyboard entry and explain timezone, locale, and ambiguous dates. |
| Q098 | Destructive action handling | Match confirmation strength to impact; offer undo when feasible. |
| Q099 | Modal focus lifecycle | Label it, set initial focus appropriately, contain modal interaction, and restore focus on close. |
| Q100 | Popover behavior | Define dismissal and focus deliberately; a popover is not automatically a modal dialog. |
| Q101 | Tooltip limitations | Do not hide essential information behind hover; support keyboard-triggered equivalents. |
| Q102 | Bottom sheet quality | Respect scroll/drag conflicts, snap points, keyboard, safe areas, and explicit dismissal. |
| Q103 | Toast restraint | Use for supplemental feedback; critical failures and required actions remain discoverable. |
| Q104 | Drag alternatives | Provide non-drag controls for reorder, movement, and resizing when required. |
| Q105 | Gesture arbitration | Distinguish scrolling, swiping, long press, zoom, and drag without accidental activation. |
| Q106 | Haptic restraint | Use available platform feedback to confirm meaningful events; respect preferences. |
| Q107 | Bulk action clarity | Make selection scope, count, exceptions, and consequences explicit. |
| Q108 | Resizable workspace | Preserve useful panel minimums and offer keyboard or menu alternatives. |
| Q109 | Editor confidence | Provide undo/redo, selection consistency, autosave status, and recovery. |
| Q110 | Table usability | Clear headers, sorting, filtering, density, column behavior, and accessible alternatives. |

### State, resilience, accessibility, and polish

| ID | Quality | Concrete implementation / review question |
|---|---|---|
| Q111 | Intentional empty states | Explain why the area is empty and the useful next action. |
| Q112 | Proportional loading UI | Choose immediate feedback, skeletons, determinate progress, or background work based on actual delay. |
| Q113 | Accurate progress | Show percentages only when meaningful; distinguish uploading, processing, and completion. |
| Q114 | Optimistic interaction | Apply when safe; reconcile server response, rollback visibly, and preserve retry context. |
| Q115 | Stale-data visibility | Indicate freshness where decisions depend on it; avoid silent data replacement during interaction. |
| Q116 | Offline and reconnect | Explain capabilities, queue states, conflicts, and what is actually saved. |
| Q117 | Duplicate prevention | Protect submissions and payments from repeat activation without stranding users. |
| Q118 | Partial-failure recovery | Keep functioning sections usable; offer retries near failed content. |
| Q119 | Session continuity | Warn about expiry when useful; recover drafts after reauthentication. |
| Q120 | Permission and role states | Explain unavailable actions and request access paths without leaking protected data. |
| Q121 | Screen reader semantics | Names, roles, values, landmarks, headings, and bounded live announcements. |
| Q122 | Reduced motion | Remove nonessential movement while preserving state changes and task feedback. |
| Q123 | Reduced sensory load | Offer control over looping media, sound, flashes, and persistent distractions. |
| Q124 | High contrast support | Test forced colors and visible boundaries; do not encode state only in background images. |
| Q125 | Localization resilience | Handle string expansion, currencies, calendars, plurals, RTL, and language-specific input. |
| Q126 | Chart comprehension | Provide meaningful labels, units, legends, keyboard access where interactive, and text/table alternatives. |
| Q127 | Adaptive-device responsiveness | Test slow CPU, memory pressure, tablets/foldables, window resizing, zoom, external keyboards, mixed touch/pointer input, and screen readers. |
| Q128 | Consistent animation grammar | Share durations, springs, easing, origins, and entry/exit conventions. |
| Q129 | Correct cancellation | Animations and pending actions can be interrupted without jumping or leaving stale states. |
| Q130 | Quiet ongoing operation | Pause unnecessary rendering when hidden/offscreen; avoid battery-draining decoration. |
| Q131 | Accurate completion feedback | A success state means the action actually succeeded, not only that a button was pressed. |
| Q132 | Measured polish | Review visual details alongside task results, field performance, and support evidence. |

### Additional product-specific patterns

| ID | Surface | Qualities beyond the common checklist |
|---|---|---|
| Q133 | Commerce / checkout | Real stock and totals, transparent shipping, guest checkout when suitable, recoverable payment errors, receipt and order status. |
| Q134 | Authentication / onboarding | Explain permissions in context; support passkeys/autofill where appropriate; make first meaningful success easy. |
| Q135 | AI / chat interfaces | Distinguish generated and sourced content; show streaming and stop state; preserve edits; require appropriate review of consequential actions. |
| Q136 | Collaborative tools | Presence with meaning, conflict handling, revision history, permissions, and understandable synchronization. |
| Q137 | Media applications | Captions, transcripts when appropriate, keyboard controls, accessible progress, volume, playback rate, and buffering recovery. |
| Q138 | Maps and geospatial UI | Accessible search/list alternatives, understandable clusters, location permission context, and controllable zoom. |
| Q139 | Notifications / inboxes | Priorities, preferences, read state, batching, useful destinations, and explicit action outcomes. |
| Q140 | Account / settings | Searchable organization, saved-state clarity, theme/language/preferences, data export, cancellation, and deletion workflows. |

## 4. Surface-by-surface build recipes

| Surface | Appropriate composition | Motion worth considering | Highest-priority validation |
|---|---|---|---|
| Landing page | Semantic content + lean renderer + authored typography/media | One distinctive hero treatment; short section transitions | First-screen comprehension, LCP, CTA, phone layout |
| Portfolio / experiential site | Strong art direction + GSAP or graphics engine only where justified | Spatial transitions, camera movement, authored scroll scenes | Direct access, reading, keyboard, motion reduction, GPU load |
| SaaS web app | Accessible primitives + tokens + query/state layer | Layout continuity, dialogs, drag feedback, progress | Task throughput, forms, focus, error recovery, INP |
| Data dashboard | Tables/charts + query cache + virtualization where needed | Filter transitions and selection continuity | Readability, units, large datasets, stale states, export |
| Editorial / docs | Content-first renderer + search + readable type | Anchored navigation; restrained route transitions | Reading, search, copy/share, deep links, font loading |
| Commerce | Product media + accessible variants + robust checkout | Product transitions and feedback | Pricing truth, stock, cart persistence, payments, device performance |
| Native mobile | Platform UI patterns or intentionally adapted cross-platform controls | Interactive navigation, native springs, meaningful haptics | Gesture conflicts, keyboards, back navigation, text scale |
| Desktop / creative tool | Multi-pane layout + shortcuts + undo/history | Panel resizing, spatial continuity, direct manipulation | Precision input, persistence, large documents, multiwindow |

These recipes describe combinations to evaluate. “Premium” does not require a particular programming language, framework, UI kit, or animation engine.


## 5. Browser-native layout, typography, and interface capabilities

These are often the first tools to consider. They work across web frameworks; many need no additional package. **V** means the linked official reference was inspected; **R** means it remains a linked candidate to recheck. Browser support is feature- and subfeature-specific. Use the linked compatibility tables and your audience's device matrix, including embedded webviews. A Baseline label for a parent feature does not establish universal support for every value.

### Layout, structure, and styling

| ID | Tool / capability | Functionality and fit | Tradeoff / current-use guidance | Evidence |
|---|---|---|---|---|
| B001 | [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout) | Two-dimensional layouts, editorial grids, dashboards. | Maintain meaningful DOM order across visual rearrangements. | R |
| B002 | [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout) | One-dimensional alignment and distribution of controls/content. | Handle wrapping and minimum-content sizing deliberately. | R |
| B003 | [Subgrid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Subgrid) | Align nested cards and sections to parent grid tracks. | Excellent for aligned card metadata; nested grid structure still matters. | V |
| B004 | [Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries) | Recompose a reusable component based on its container. | Size, style, scroll-state, and anchored query support are distinct. | V |
| B005 | [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning) | Position tethered UI relative to a trigger, with fallback positions. | Geometry does not supply complete keyboard or popup semantics. | V |
| B006 | [Logical properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values) | Direction-aware padding, margin, sizes, and positioning. | Test actual RTL content; directional icons may need separate treatment. | V |
| B007 | [Cascade layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer) | Define intentional precedence across resets, libraries, themes, utilities. | Learn how unlayered styles and important declarations interact. | V |
| B008 | [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting) | Group related selectors within native CSS. | Avoid excessive nesting and accidental specificity. | V |
| B009 | [CSS scope](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope) | Limit styling to a DOM subtree, optionally with boundaries. | MDN identifies newly available support; account for older clients. | V |
| B010 | [:has()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has) | Style a container based on related descendant/sibling state. | Prefer bounded selectors; do not replace necessary application state management. | V |
| B011 | [Custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) | Runtime theme, density, motion, and component tokens. | Naming, scope, and fallbacks need design-system governance. | R |
| B012 | [@property](https://developer.mozilla.org/en-US/docs/Web/CSS/@property) | Register typed CSS custom properties for interpolation and defaults. | Registration does not make an expensive paint effect free. | R |
| B013 | [clamp(), min(), max()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp) | Bounded fluid type, spacing, and layouts. | Use sensible min/max and zoom-safe units; inspect extreme widths. | R |
| B014 | [Dynamic/small viewport units](https://developer.mozilla.org/en-US/docs/Web/CSS/length) | Fit browser chrome changes and mobile viewport conditions. | Choose dvh/svh/lvh deliberately; test keyboard and address-bar behavior. | R |
| B015 | [Safe-area environment variables](https://developer.mozilla.org/en-US/docs/Web/CSS/env) | Keep controls clear of device cutouts and system areas. | Combine with platform/webview configuration; do not assume one inset everywhere. | R |
| B017 | [Overscroll behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/overscroll-behavior) | Control scroll chaining at nested boundaries. | Preserve useful browser/navigation behavior and touch expectations. | R |
| B018 | [Scroll anchoring](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_anchoring/Overview) | Stabilize reading position as content above changes. | Disable only for a demonstrated conflict; virtual lists need coordination. | V |
| B019 | [Scrollbar gutter](https://developer.mozilla.org/en-US/docs/Web/CSS/scrollbar-gutter) | Reserve scrollbar space and reduce width jumps. | Overlay-scrollbar platforms behave differently. | R |

### Type, color, and font delivery

| ID | Tool / capability | Functionality and fit | Tradeoff / current-use guidance | Evidence |
|---|---|---|---|---|
| B020 | [Variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts) | Multiple weights, widths, or custom axes in a font resource. | One variable font is not always smaller than the few static styles you need. | V |
| B021 | [Optical sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-optical-sizing) | Size-specific letterforms when the font supports an optical axis. | Depends on the chosen font, not just browser support. | V |
| B022 | [Numeric OpenType variants](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric) | Tabular numbers, fractions, ordinals, and other numeric glyph choices. | Font must contain the requested features. | V |
| B023 | [text-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap) | Balanced headings and improved wrapping via supported values. | Balance/pretty/stable differ; test per-value support and layout cost. | V |
| B024 | [font-size-adjust](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust) | Improve apparent size consistency between preferred/fallback fonts. | Does not alone match all ascent, descent, width, and line-gap metrics. | V |
| B025 | [Font metric overrides](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/size-adjust) | Tune fallback size alongside ascent/descent/line-gap descriptors. | Values must be derived for the actual font pair. | R |
| B026 | [Fontsource](https://fontsource.org/docs/getting-started/introduction) | Versioned packages for self-hosting open-source fonts. | Select only required files; verify font-specific licenses and scripts. | V |
| B027 | [Utopia](https://utopia.fyi/type/calculator/) | Generates fluid type and space scales. | Generated values are a starting point; inspect real content and zoom. | V |
| B029 | [Google Fonts](https://fonts.google.com/) | Font discovery and delivery ecosystem. | Review individual font licensing, privacy needs, and delivery strategy. | R |
| B030 | [Adobe Fonts](https://fonts.adobe.com/) | Commercial font discovery and licensed activation/web use. | Subscription and web hosting/embedding rights require project-specific review. | R |
| B031 | [OKLCH](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch) | Perceptually oriented lightness/chroma/hue color specification. | Check gamut mapping and contrast on actual rendered colors. | V |
| B032 | [Relative CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors) | Derive themed color variations from base tokens. | Derived colors still need contrast checks; use fallbacks as necessary. | V |
| B033 | [color-mix()](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix) | Blend colors in a chosen interpolation space. | A convenient blend is not automatically an accessible palette. | R |
| B034 | [Culori](https://culorijs.org/) | Color conversion, interpolation, and gamut-aware calculations in JS. | Use when programmatic color work exceeds native CSS needs. | R |
| B035 | [Color.js](https://colorjs.io/) | Color-space conversion, color manipulation, and contrast-related utilities. | Match chosen contrast algorithms to your actual compliance target. | R |

### Semantics and application behavior

| ID | Tool / capability | Functionality and fit | Tradeoff / current-use guidance | Evidence |
|---|---|---|---|---|
| B036 | [HTML dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog) | Native modal/nonmodal dialog foundation. | Add proper names, initial focus, close behavior, and focus restoration; subfeatures vary. | V |
| B037 | [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API) | Declarative/scripted top-layer popovers and supported dismissal behavior. | Popovers are nonmodal; choose appropriate roles and focus behavior. | V |
| B038 | [Native select](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select) | OS-integrated option selection with established behavior. | New customizable-select features have separate compatibility requirements. | V |
| B039 | [details / summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) | Native disclosure foundation for FAQ and secondary information. | Not a substitute for every tab, menu, or complex tree interaction. | R |
| B040 | [inert](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inert) | Make a subtree unavailable to focus and interaction. | Coordinate visual state and restoration; do not strand focus. | R |
| B041 | [Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) | Locale-aware numbers, dates, plurals, lists, collation, segmentation. | Translation and product terminology need a separate content workflow. | R |
| B042 | [FormatJS](https://formatjs.github.io/) | Internationalized messages and ICU-format tooling. | Plan message extraction and translator context. | R |
| B043 | [i18next](https://www.i18next.com/) | Translation resources, language resolution, framework integrations. | Test plural rules, fallbacks, interpolation, and layout expansion. | R |
| B044 | [Lingui](https://lingui.dev/) | Message catalog and compile-time localization workflow. | Align extraction and build configuration with the app. | R |
| B045 | [DTCG design-token format](https://www.designtokens.org/) | Shared representation for typed design decisions across tooling. | Stable community-group format exists; actual tool interoperability still needs validation. | V |

### Native-first adoption rules

1. Build usable HTML and a stable layout first. Enhanced effects may fail independently.
2. Feature-detect exact capabilities. Use `@supports` for CSS and check APIs before calling them.
3. Keep meaningful text and controls accessible even when the visual layer is canvas/WebGL.
4. For modal UI, test keyboard, screen reader, nested overlays, scrolling, and mobile back behavior.
5. Evaluate production client support, not only the latest browser installed on the developer's machine.


## 6. Motion, transitions, graphics, and creative rendering

Research snapshot: **November 6, 2026 (America/Phoenix)**. `V` means an official documentation page, official repository, or official catalog entry was inspected in this research pass. It does not mean the package was installed, benchmarked, audited, or tested on every browser. `R` means a useful additional reference whose individual documentation was not inspected in this pass; recheck before adoption. `E` flags an evolving or compatibility-sensitive capability separately from evidence. Descriptions of fit and tradeoffs are engineering recommendations, not measured rankings.

### Choose the smallest motion system that expresses the design

| Need | Good starting point | Add complexity when |
|---|---|---|
| Hover, focus, pressed, and small state changes | CSS transitions | You need interruption control, orchestration, or dynamic values. |
| React app panels, shared layouts, and gestures | Motion | A timeline or specialist SVG behavior is central to the experience. |
| Art-directed landing page and scroll storytelling | GSAP + ScrollTrigger | Add only the specific plugins used; smooth scrolling remains optional. |
| Framework-independent animation sequences | GSAP or Anime.js | The project needs specialist integration or a visual timeline. |
| Browser-native page continuity | View Transition API | Required browsers lack a feature or router coordination needs more control. |
| Interactive illustrated character or branded control | Rive | Compare runtime/asset cost with a simpler SVG or video. |
| Mostly linear exported animation | Lottie/dotLottie or video | Choose interactive state machines only when user input actually changes the story. |
| React-based interactive 3D | Three.js + React Three Fiber + selected Drei helpers | Bring physics and postprocessing only when visible benefits justify their cost. |
| Simple product model/AR preview | `<model-viewer>` | A custom scene graph or configurator exceeds its scope. |
| 2D canvas editor | Konva or Fabric.js | Large GPU scenes, specialist text editing, or custom rendering require another approach. |
| Shader-rich visual background | A small custom shader or Paper Shaders | The interaction requires a full scene engine. |

Motion quality comes from continuity, response, consistent timing, interruption handling, and useful feedback. No library guarantees smoothness. Avoid multiple engines writing the same transform, opacity, scroll position, or scene property.

### Browser-native motion and rendering primitives

| ID | Tool/API · evidence | Functionality and strongest fit | Main tradeoff / adoption note |
|---|---|---|---|
| M001 | [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions) · R | Interpolates property changes; ideal for small hover, focus, toggle, and pressed feedback. | Explicitly name properties; `transition: all` can animate unrelated layout changes. |
| M002 | [CSS keyframe animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations) · R | Repeating or staged CSS animation; loaders, short entrances, ambient accents. | Pause unnecessary loops; honor reduced motion and avoid making content depend on animation. |
| M003 | [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API) · V | JavaScript control of keyframes, playback, reversal, cancellation, and animation timing. | Low dependency cost, but you own orchestration, lifecycle cleanup, and feature differences. |
| M004 | [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) · V / E | Browser-managed snapshots and shared visual continuity for state changes and page navigation. | Check same-document and cross-document support separately; retain focus, history, and nonanimated navigation. |
| M005 | [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) · V / E | Drives animation progress from scrolling or element visibility; progress bars and restrained reveals. | Test the exact timeline/range feature on target browsers; preserve the full static layout. |
| M006 | [ScrollTimeline / ViewTimeline](https://developer.mozilla.org/en-US/docs/Web/API/ViewTimeline) · V / E | Uses scroll/view progress as an animation timeline through JavaScript. | Related to M005, not a separate library; older devices still need fallback. |
| M007 | [CSS `linear()` easing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear) · V | Piecewise easing curves, including sampled spring-like curves, without a runtime physics engine. | A sampled curve has fixed playback; use a real spring for velocity-sensitive retargeting. |
| M008 | [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style) · V | Supplies entry styles for newly rendered elements, useful with dialog/popover transitions. | Baseline 2024 in inspected docs; coordinate entry/exit/display/top-layer behavior and verify older targets. |
| M009 | [`transition-behavior: allow-discrete`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior) · V / E | Allows transitions involving discrete properties such as `display`. | MDN marks limited availability in the inspected page; keep a working immediate-state fallback. |
| M010 | [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size) · V / E | Opts into transitions between explicit sizes and supported intrinsic size values. | Experimental/limited availability in inspected docs; size animation can still incur layout work. |
| M011 | [CSS motion paths](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_motion_path) · R | Moves elements along a path through offset properties; useful for diagrams or decorative trajectories. | Essential information should remain understandable without following motion. |
| M012 | [CSS Scroll Snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap) · R | Native alignment of scrolling galleries and stepwise panels. | Aggressive mandatory snapping can impede exploration; test keyboard, touch, and long content. |
| M013 | [`requestAnimationFrame`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame) · R | Schedules custom drawing and animation work around browser frames. | Use elapsed time, not fixed per-frame increments; cancel loops on teardown. |
| M014 | [Pointer Events](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) · R | Common mouse, pen, and touch input model, including capture for dragging. | Pointer handling does not provide keyboard alternatives or accessibility semantics. |
| M015 | [WebGPU](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) · V / E | GPU graphics and compute for demanding rendering and simulation. | Requires secure context and supported browser/device; handle adapter failure/device loss and supply fallback. |
| M016 | [OffscreenCanvas](https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas) · V | Allows canvas rendering away from the DOM and, where supported, in workers. | Worker rendering reduces some main-thread pressure; it does not reduce GPU or asset costs automatically. |

### GSAP and its specialist plugins

These are one ecosystem, not 24 unrelated packages to install. The [official plugin catalog](https://gsap.com/docs/v3/Plugins/) lists included capabilities and optional plugins. GSAP's current [standard no-charge license](https://gsap.com/community/standard-license/) is a custom license with defined permitted/prohibited uses; do not describe it as MIT or assume old paid-plugin instructions still apply.

| ID | Tool/API · evidence | Functionality and strongest fit | Main tradeoff / adoption note |
|---|---|---|---|
| M017 | [GSAP core](https://gsap.com/docs/v3/GSAP/) · V | Tweens JavaScript properties, DOM styles, SVG, and scene values; coordinates timelines and callbacks. | Strong general orchestration; lifecycle cleanup and property ownership remain your responsibility. |
| M018 | [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) · V | Scroll-linked timelines, pinning, scrubbing, snapping, and triggers. | Pinning consumes scroll distance; refresh measurements after relevant layout/font changes. |
| M019 | [ScrollSmoother](https://gsap.com/docs/v3/Plugins/ScrollSmoother/) · V | Adds transformed-content smoothing and parallax on top of native scrolling and ScrollTrigger. | Requires ScrollTrigger and a suitable wrapper; test fixed elements, anchors, keyboard, and touch. |
| M020 | [ScrollToPlugin](https://gsap.com/docs/v3/Plugins/ScrollToPlugin/) · V, catalog | Animates scroll destinations. | Leave user interruption possible; native scrolling is sufficient for many anchor links. |
| M021 | [SplitText](https://gsap.com/docs/v3/Plugins/SplitText/) · V | Splits lines/words/characters for text animation; supports responsive re-splitting and ARIA assistance. | Preserve nested link semantics; split only necessary content and avoid delaying hero comprehension. |
| M022 | [ScrambleTextPlugin](https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/) · V, catalog | Scrambles characters into final text. | Decorative short labels only; retain an accessible stable text equivalent. |
| M023 | [TextPlugin](https://gsap.com/docs/v3/Plugins/TextPlugin/) · V, catalog | Replaces text progressively. | Avoid announcing every intermediate change to screen readers. |
| M024 | [DrawSVGPlugin](https://gsap.com/docs/v3/Plugins/DrawSVGPlugin/) · V | Reveals SVG strokes progressively, including selected segments. | Acts on strokes, not filled shapes; dense paths can be expensive. |
| M025 | [MorphSVGPlugin](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/) · V | Interpolates SVG path shapes. | Choose readable start/end shapes; complex geometry still needs optimization. |
| M026 | [MotionPathPlugin](https://gsap.com/docs/v3/Plugins/MotionPathPlugin/) · V, catalog | Animates along paths with orientation. | A guided path should communicate relationships; looping particles can distract. |
| M027 | [MotionPathHelper](https://gsap.com/docs/v3/Plugins/MotionPathHelper/) · V, catalog | Visually edits motion paths. | Authoring aid; do not unnecessarily ship editing controls to visitors. |
| M028 | [Flip](https://gsap.com/docs/v3/Plugins/Flip/) · V | Animates between measured layout states, including DOM reordering and shared-element changes. | Capture before/after layout at the correct framework lifecycle point; avoid concurrent measurements. |
| M029 | [Draggable](https://gsap.com/docs/v3/Plugins/Draggable/) · V | Dragging, bounds, rotation, and snapping controls. | Supply click/keyboard alternatives and discoverable handles. |
| M030 | [InertiaPlugin](https://gsap.com/docs/v3/Plugins/InertiaPlugin/) · V, catalog | Momentum and settling after release. | Companion to interactions such as Draggable; limit excessive travel and settling time. |
| M031 | [Observer](https://gsap.com/docs/v3/Plugins/Observer/) · V, catalog | Normalizes wheel/touch/pointer gesture observations. | Do not intercept ordinary navigation gestures without a clear interaction purpose. |
| M032 | [CustomEase](https://gsap.com/docs/v3/Eases/CustomEase/) · V, catalog | Custom timing curves. | Establish a small shared vocabulary rather than unique easing on every control. |
| M033 | [CustomWiggle](https://gsap.com/docs/v3/Eases/CustomWiggle/) · V, catalog | Configurable oscillating eases. | Requires CustomEase; limit to intentional character or feedback moments. |
| M034 | [CustomBounce](https://gsap.com/docs/v3/Eases/CustomBounce/) · V, catalog | Configurable bounce eases. | Requires CustomEase; repeated bounce is distracting in task interfaces. |
| M035 | [EasePack](https://gsap.com/docs/v3/Eases/) · V, catalog | Additional RoughEase, SlowMo, and ExpoScaleEase curves. | Specialized expression; only import what the scene uses. |
| M036 | [Physics2DPlugin](https://gsap.com/docs/v3/Plugins/Physics2DPlugin/) · V, catalog | Velocity/acceleration-style 2D motion. | A motion helper, not a complete collision simulation engine. |
| M037 | [PhysicsPropsPlugin](https://gsap.com/docs/v3/Plugins/PhysicsPropsPlugin/) · V, catalog | Physics-like interpolation of properties. | Use a full physics engine only when bodies, contacts, or constraints are required. |
| M038 | [GSDevTools](https://gsap.com/docs/v3/Plugins/GSDevTools/) · V, catalog | Playback and timeline inspection controls. | Development tool; keep it out of the final public interface. |
| M039 | [PixiPlugin](https://gsap.com/docs/v3/Plugins/PixiPlugin/) · V, catalog | GSAP integration for Pixi display properties. | Useful only in a Pixi scene; check supported Pixi major versions. |
| M040 | [`useGSAP`](https://gsap.com/resources/React/) · V | React integration with scoped setup and cleanup via GSAP context. | Ensure callbacks and subsequently created animations are also cleaned up. |

### Other animation, gesture, and page-transition systems

| ID | Tool/API · evidence | Functionality and strongest fit | Main tradeoff / adoption note |
|---|---|---|---|
| M041 | [Motion](https://motion.dev/docs/) · V | Animation, springs, layout transitions, gestures, presence, and scroll tools for React/JS/Vue. | Choose the appropriate platform API; avoid mounting/unmounting that prevents exit animation. |
| M042 | [Anime.js](https://animejs.com/documentation/) · V | Framework-independent tweens, timelines, SVG/text tools, draggable and layout capabilities, WAAPI tooling. | Check current-major APIs; older tutorials may describe a different API surface. |
| M043 | [react-spring](https://www.react-spring.dev/) · V | Spring-driven React animation with several rendering targets. | Tune damping and interruption carefully; long oscillations are rarely helpful for frequent actions. |
| M044 | [AutoAnimate](https://auto-animate.formkit.com/) · V | Automatically animates immediate-child insertions, removals, and reordering. | Convenient for lists; less precise than authored choreography and affects layout context. |
| M045 | [Lenis](https://github.com/darkroomengineering/lenis) · V | Optional scroll smoothing and synchronization for visual experiences. | Native CSS scroll-snap is unsupported per its README; use its snap integration if needed. Test anchors, focus, and reduced motion. |
| M046 | [Locomotive Scroll](https://github.com/locomotivemtl/locomotive-scroll) · V | Scroll-based viewport detection, smooth scrolling, and parallax; the current repository builds on Lenis. | Check the installed major; current documentation and old transform-scroller tutorials differ. |
| M047 | [use-gesture](https://use-gesture.netlify.app/) · V | Drag, pinch, wheel, hover, and related gesture state for custom interactions. | Gesture recognition is separate from rendering and keyboard accessibility. |
| M048 | [Rive](https://rive.app/docs/getting-started/introduction) · V | Authored interactive graphics, timelines, state-driven behavior, data binding, and runtime delivery. | Budget runtime plus assets; provide semantic HTML/native controls around visual interactions. |
| M049 | [Lottie Web](https://github.com/airbnb/lottie-web) · V | Plays exported vector animation, commonly from After Effects workflows. | Exported feature support varies; huge path counts or raster assets undermine lightweight delivery. |
| M050 | [dotLottie runtimes](https://docs.lottiefiles.com/en) · V | Packages and plays Lottie assets across web/mobile integrations. | Format, runtime, state-machine support, and framework wrapper are separate version choices. |
| M051 | [Theatre.js](https://www.theatrejs.com/) · V | Visual keyframe/curve authoring for JavaScript values and 3D sequences. | Strong for art direction; inspect current package compatibility before building a new production pipeline. |
| M052 | [Barba.js](https://barba.js.org/) · V | Coordinates transitions between website pages. | Own focus, analytics, scripts, caching, and back/forward behavior; compare native View Transitions first. |
| M053 | [Swup](https://swup.js.org/) · V | Extensible page transitions for server-rendered sites. | Test progressive enhancement and third-party script lifecycle after content replacement. |
| M054 | [Svelte transitions / animate](https://svelte.dev/docs/svelte/transition) · R | Framework-native entry/exit and movement animation. | Usually the simplest fit for Svelte; avoid adding a second engine for equivalent needs. |
| M055 | [Vue Transition / TransitionGroup](https://vuejs.org/guide/built-ins/transition.html) · R | Framework-native transition lifecycle and list movement. | Supply transition styles and cancellation behavior; visual motion does not supply component semantics. |
| M056 | [Motion Studio / AI Kit / Performance Doctor](https://motion.dev/docs/) · V | Official authoring and agent-oriented tools for creating and diagnosing Motion work. | Tool-assisted diagnosis needs real-browser validation; access/plan terms should be checked. |

### 3D, GPU, canvas, physics, and asset delivery

| ID | Tool/API · evidence | Functionality and strongest fit | Main tradeoff / adoption note |
|---|---|---|---|
| M057 | [Three.js](https://threejs.org/docs/) · V | 3D scenes, cameras, meshes, lighting, materials, loaders, animation, and renderers. | A rendering toolkit: you still design interaction, accessibility, asset budgets, and quality tiers. |
| M058 | [Three.js WebGPURenderer](https://threejs.org/docs/pages/WebGPURenderer.html) · V / E | Renderer selecting WebGPU where available and falling back to WebGL2. | Renderer fallback does not guarantee every custom shader or compute feature has an equivalent fallback. |
| M059 | [Three.js TSL](https://threejs.org/docs/) · V, catalog / E | Node-based shader authoring within the Three ecosystem. | Check renderer/material compatibility; existing GLSL ShaderMaterial code may require migration. |
| M060 | [React Three Fiber](https://r3f.docs.pmnd.rs/getting-started/introduction) · V | Declarative React renderer for Three.js, integrating scene composition and React state. | Pair React and Fiber major versions correctly; inspected docs mark v10 as alpha. |
| M061 | [Drei](https://drei.docs.pmnd.rs/getting-started/introduction) · V | R3F helpers for controls, environment, text, assets, instances, and adaptive rendering. | Helpers can contain expensive effects; evaluate each selected component rather than enabling everything. |
| M062 | [Babylon.js](https://doc.babylonjs.com/) · V | Broad web rendering engine with integrated scene tooling and ecosystem. | Attractive for substantial 3D applications; a simple model preview may need less infrastructure. |
| M063 | [PlayCanvas](https://playcanvas.com/) · V | WebGL/WebGPU engine and collaborative editor for interactive 3D. | Engine and hosted editor are separate product choices; inspect project/export requirements. |
| M064 | [Spline](https://docs.spline.design/) · V | Visual creation and publishing of interactive 3D and 2D scenes; animation, materials, events, and data. | Inspect embed size, loading, ownership/export options, and device performance for the chosen plan. |
| M065 | [Spline Hana](https://docs.spline.design/) · V | Spline's 2D interface/animated-graphics editor sharing its interaction and publishing model. | A visual authoring option; exported canvas does not automatically provide accessible document structure. |
| M066 | [`<model-viewer>`](https://modelviewer.dev/) · V | Web component for interactive model presentation and supported AR modes. | AR capabilities vary by device; provide poster, loading/error states, and non-AR access. |
| M067 | [OGL](https://github.com/oframe/ogl) · V | Minimal WebGL abstraction for custom graphics and shader-driven scenes. | Less built-in infrastructure means more renderer/asset work for the developer. |
| M068 | [Curtains.js](https://www.curtainsjs.com/) · V | Positions WebGL image/video/canvas planes relative to DOM elements. | Useful for image distortions and transitions; handle resize, scroll, context loss, and static fallbacks. |
| M069 | [PixiJS](https://pixijs.com/8.x/guides/getting-started/intro) · V | GPU-based 2D scene graph, textures, text, events, filters, masks, and particles. | Canvas graphics require explicit accessibility treatment; measure GPU overdraw and texture memory. |
| M070 | [Konva](https://konvajs.org/) · V | Canvas scene graph with input, layers, dragging, transforms, filters, and raster export. | Good for editors and diagrams; manage redraws, large scenes, and accessible alternatives. |
| M071 | [Fabric.js](https://www.fabricjs.com/) · V | Interactive canvas objects, rich text editing, serialization, SVG import/export, and custom controls. | Export fidelity, font availability, and migration across major versions need testing. |
| M072 | [p5.js](https://p5js.org/) · V | Creative coding for interactive art, animation, and visual experiments. | Excellent exploration tool; production interfaces still need accessibility and resource budgets. |
| M073 | [Paper.js](http://paperjs.org/) · R | Vector graphics and path operations on canvas; illustration and geometry tools. | Verify current release/maintenance before new adoption; not interchangeable with Paper Shaders. |
| M074 | [Two.js](https://two.js.org/) · R | Common 2D drawing abstraction across SVG, Canvas, and WebGL renderers. | Renderer differences and project maintenance should be checked for required features. |
| M075 | [Rapier](https://rapier.rs/) · V | 2D/3D rigid-body physics, contacts, constraints, and scene queries with web bindings. | Physics consumes CPU/WASM startup; use fixed stepping and limit active bodies. |
| M076 | [React Three Rapier](https://github.com/pmndrs/react-three-rapier) · V | React/R3F integration for Rapier bodies, colliders, and events. | Match dependency versions; avoid React rerenders for every physics-frame update. |
| M077 | [Matter.js](https://brm.io/matter-js/) · V | JavaScript 2D rigid-body simulation with collisions and constraints. | Useful for playful 2D interactions; unnecessary for ordinary button or panel springs. |
| M078 | [pmndrs postprocessing](https://github.com/pmndrs/postprocessing) · V | Three.js image effects and effect composition. | Bloom, depth effects, and additional passes increase GPU cost; inspect renderer compatibility. |
| M079 | [Paper Shaders](https://shaders.paper.design/) · V | Reusable canvas shader effects such as grain gradients, glass, dithering, water, and liquid metal. | Distinctive accents can become visual noise; pause offscreen and cap resolution. |
| M080 | [TypeGPU](https://docs.swmansion.com/TypeGPU/) · V / E | TypeScript-oriented WebGPU toolkit with typed GPU data and shader authoring. | Specialized graphics/compute infrastructure; budget for evolving APIs and device support. |
| M081 | [glTF Transform](https://gltf-transform.dev/) · V | SDK/CLI for optimizing and processing glTF assets, geometry, animation, and textures. | Validate final visual quality and required loader/decoder support after compression. |
| M082 | [Meshoptimizer](https://github.com/zeux/meshoptimizer) · R | Mesh optimization, simplification, and compression for geometry pipelines. | Compression changes transfer/decoding tradeoffs; measure total startup cost. |
| M083 | [Draco](https://github.com/google/draco) · R | Compresses 3D geometry for asset delivery. | Adds decoding work; compare with Meshopt using representative assets. |
| M084 | [KTX / Basis Universal](https://github.com/BinomialLLC/basis_universal) · R | Texture compression/transcoding pipeline for more efficient GPU texture delivery. | Format support, decoding, quality, and color management require validation. |
| M085 | [tsParticles](https://github.com/tsparticles/tsparticles) · R | Configurable particle effects and framework integrations. | Decorative effects should be bounded, optional, and absent from critical content paths. |
| M086 | [Canvas Confetti](https://github.com/catdad/canvas-confetti) · R | Short celebratory particle bursts. | Use for meaningful milestones; respect reduced motion and prevent repeat spam. |
| M087 | [Remotion](https://www.remotion.dev/docs/) · V | Code-authored video composition, rendering, and player integration. | Useful for pre-rendered hero/demo assets; licensing differs by use and is not a generic animation-runtime license. |
| M088 | [Blender](https://www.blender.org/) · R | 3D modeling, materials, animation, lighting, and offline rendering for authentic assets. | Asset creation tool, not the browser runtime; optimize exports before web delivery. |

### Motion patterns that make interfaces feel deliberate

These are design patterns rather than packages. Timing ranges below are **starting hypotheses**, not standards or universal optimum values. Tune by travel distance, task frequency, input type, and measured response. User feedback should start promptly even when the full transition takes longer.

| Pattern | What good execution looks like | Tools / caution |
|---|---|---|
| Press feedback | A control responds immediately with a small visual change; its hit area stays stable. | CSS/Motion; avoid moving the target away from the pointer. |
| Hover and focus | Equivalent state clarity for mouse and keyboard; focus remains visible throughout. | CSS; never use hover as the only disclosure route. |
| Menu/disclosure | Small movement from the trigger plus opacity can clarify origin; repeated activation reverses cleanly. | CSS/Motion; commonly begin testing around 120–220 ms. |
| Dialog and drawer | Backdrop and surface are coordinated; close can interrupt open; focus enters/restores correctly. | CSS/Motion; roughly 180–320 ms is a starting test range. |
| Shared-element transition | The same item visibly moves between list and detail, preserving identity and orientation. | View Transitions/Motion layout/GSAP Flip; manage focus independently. |
| Layout reflow | Surrounding elements move coherently when content expands, filters, or reorders. | FLIP/Motion/AutoAnimate; avoid expensive repeated layout reads. |
| Height expansion | Content reveals without clipping text or shifting unrelated context unexpectedly. | Measured height, layout animation, or supported intrinsic-size animation. |
| Drag and drop | The object tracks input closely; insertion location is visible; drop settles briefly. | Gesture system + animation; include non-drag reordering. |
| Spring retargeting | Mid-flight changes continue from current position and velocity instead of restarting. | Motion/react-spring; restrained damping for frequent product actions. |
| Route transition | A short transition establishes continuity without holding up navigation. | View Transitions/Swup/Barba; back/forward and focus are part of correctness. |
| List stagger | A small ordered offset communicates grouping without postponing access to later items. | GSAP/Motion/Anime.js; cap total duration instead of multiplying indefinitely. |
| Scroll reveal | Content remains accessible before JS and becomes visible once; motion supports reading order. | IntersectionObserver/ScrollTrigger/CSS timelines; avoid repeated surprise on backscroll. |
| Reading progress | Accurately maps relevant content position to progress without taking focus. | Native scroll timeline; allow shorter/longer content and zoom. |
| Pinned story sequence | Each scroll segment reveals an understandable product idea; easy exit and alternate static flow. | ScrollTrigger; use sparingly and test short viewports. |
| Parallax | Modest depth separation supports composition while the reading plane stays stable. | CSS/GSAP/Lenis; disable large travel for reduced motion. |
| Hero choreography | A single purposeful sequence establishes hierarchy; headline and CTA are available quickly. | Timeline tools; no compulsory intro before the visitor can act. |
| Text reveal | Phrases or lines enter coherently; final text remains selectable and semantically intact. | SplitText/Anime.js; avoid character-by-character reading delays. |
| SVG trace or morph | Illustrates a relationship or identity change with simple paths and a clear final state. | DrawSVG/MorphSVG; decorative tracing should not explain essential content alone. |
| Loading transition | Existing content stays stable where possible; skeleton dimensions match incoming layout. | CSS/Motion; no fake progress percentages or endless shimmer by default. |
| Optimistic feedback | UI immediately reflects a reversible action; failure rolls back with an understandable message. | State layer + small motion; animation cannot replace data consistency. |
| Success celebration | Brief reward follows an actual meaningful completion; ordinary repetitive actions remain quiet. | Rive/Lottie/confetti; give text confirmation too. |
| Carousel movement | User chooses movement, position is clear, and reduced-motion controls remain usable. | Native Scroll Snap or accessible carousel library; avoid forced autoplay. |
| 3D product reveal | Useful angles, appropriate lighting, and a poster let users understand the product immediately. | model-viewer/Three/Spline; load only when it adds material value. |
| Shader transition | Image distortion or material change is short, localized, and legible. | OGL/Curtains/Paper/Three; profile fill rate at phone resolution. |

### Smoothness engineering checklist

- **One owner per animated property.** Use nested wrappers if CSS layout, GSAP, and a framework need separate transform responsibilities.
- **Make animation interruptible.** Test rapid clicks, reversals, route changes, unmounts, tab hiding, resize, and breakpoint changes.
- **Design a reduced-motion composition.** Preserve state changes and feedback while removing spatial travel, parallax, looping, and unnecessary zoom; do not merely accelerate everything.
- **Prefer transform/opacity where visually appropriate.** They often avoid layout/paint work, but compositing is implementation- and scene-dependent; inspect browser traces instead of assuming GPU acceleration.
- **Batch reads and writes.** Read geometry together, update styles together, and avoid forced synchronous layout in pointer/scroll handlers.
- **Stop hidden work.** Pause offscreen and background-tab scenes; render 3D on demand when nothing changes; resume without time-step jumps.
- **Use adaptive visual quality.** Cap device-pixel ratio, reduce particle counts, downgrade shadows/postprocessing, and offer a static fallback on weaker devices.
- **Budget textures as well as transfer bytes.** Compressed downloads can still inflate into large GPU allocations. Dispose resources on navigation and replacement.
- **Keep semantic controls outside the canvas when possible.** A visual canvas button alone does not supply a name, role, focus order, or keyboard behavior.
- **Check real devices.** A development desktop with a discrete GPU does not represent a midrange phone under thermal throttling.
- **Measure frame pacing.** 60 Hz provides about 16.7 ms per frame and 120 Hz about 8.3 ms for the entire pipeline, not a safe allowance for JavaScript alone. Check missed frames and long interactions, not only average FPS.
- **Keep the useful page load independent.** Deliver readable headline, navigation, CTA, and poster before optional graphics; reserve asset dimensions to avoid layout shifts.

### What deserves attention now

The following are promising capabilities verified in official sources, **not a measured GitHub trending leaderboard**:

- Native View Transitions and scroll timelines can remove custom orchestration from appropriate cases; support remains feature-specific.
- Motion now documents animation authoring and agent tools alongside its React/JavaScript/Vue APIs.
- Anime.js's current documentation covers layout and draggable workflows in addition to classic timelines.
- Three.js's WebGPU renderer and TSL provide a modern rendering direction; evaluate the exact material/effect migration.
- React Three Fiber's inspected documentation calls out a v10 alpha; pin compatible stable versions for routine delivery.
- Paper Shaders offers reusable visual materials without committing the entire interface to a large 3D scene.
- TypeGPU enables typed WebGPU workflows and TypeScript shader authoring for teams able to own GPU engineering.
- Rive, Spline, and PlayCanvas have expanded authoring/agent workflows; an agent-assisted tool still needs asset, accessibility, and performance review.


## 7. Components, design systems, and design workflow

Research snapshot: **November 6, 2026 (America/Phoenix)**. These entries are a selection guide, not a recommendation to install every dependency. **V** means a publisher's documentation or repository was inspected during this research for the described purpose; **R** means a useful reference whose substantive current documentation could not be inspected. V is not a benchmark, security audit, compatibility guarantee, or confirmation that every release remains maintained. Framework fit and tradeoffs are editorial guidance. A library's accessibility claims still require verification in the finished interface.

### Headless behavior and component foundations

Choose one main foundation per product. Headless components supply behavior and semantics; the visual design, content, and integrated usability still belong to your team.

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C001 | [Base UI](https://base-ui.com/react/overview/quick-start) | Unstyled React controls, menus, dialogs, comboboxes, navigation, and overlays. | Strong custom design-system foundation; check composition, portals, and focus in your app. | V |
| C002 | [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction) | React primitives handling keyboard interaction, ARIA semantics, and focus management. | Mature option for existing products; styling and correct composition remain your responsibility. | V |
| C003 | [React Aria](https://react-aria.adobe.com/) | Accessible React behavior and components with internationalization and adaptive interaction. | Especially useful for complex selection, dates, and multilingual products; requires a visual layer. | V |
| C004 | [Headless UI](https://headlessui.com/) | Unstyled React/Vue menus, dialogs, listboxes, tabs, and related controls. | Good Tailwind fit; verify each framework's API and component availability. | V |
| C005 | [Floating UI](https://floating-ui.com/) | Positions tooltips/popovers using collision detection, flipping, shifting, and sizing. | Positioning alone does not implement a complete accessible menu or dialog. | V |
| C006 | [Ark UI](https://ark-ui.com/) | Headless components across React, Vue, Solid, and Svelte. | Useful when maintaining several frontend stacks; check adapter-specific integration. | V |
| C007 | [Zag.js](https://zagjs.com/) | State-machine behavior for controls such as sliders, menus, and dialogs. | Lower-level than a styled kit; useful for shared behavior across frameworks. | V |
| C008 | [Reka UI](https://reka-ui.com/) | Vue primitives with keyboard support, focus management, and localization facilities. | Use current Reka documentation when encountering older Radix Vue examples. | V |
| C009 | [Bits UI](https://bits-ui.com/) | Unstyled Svelte primitives for an owned component system. | Match the package generation to your Svelte version. | V |
| C010 | [shadcn/ui](https://ui.shadcn.com/docs) | Source-distributed components, blocks, themes, and registries for React products. | You own copied code and updates. Base UI is now the default for new projects; Radix remains supported. | V |
| C011 | [shadcn/vue](https://www.shadcn-vue.com/) | Customizable source components and blocks for Vue. | A framework-specific implementation; React examples cannot be copied unchanged. | V |
| C012 | [shadcn-svelte](https://www.shadcn-svelte.com/) | Customizable Svelte component source with accessible behavior. | Maintain local changes and follow its own upgrade guidance. | V |

Current migration note: shadcn's [July 2026 announcement](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default) explicitly keeps Radix supported. A change in the default is not a reason to rewrite a working production component system.

### Styled component systems and broad UI suites

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C013 | [Material UI](https://mui.com/material-ui/getting-started/) | Comprehensive React controls and theme customization for product interfaces. | A strong visual starting point; advanced MUI X products have separate capabilities and licensing. | V |
| C014 | [Mantine](https://mantine.dev/) | React components, hooks, forms, overlays, and date-oriented UI. | Convenient integrated toolkit; choose deliberately instead of mixing several full suites. | V |
| C015 | [Chakra UI](https://chakra-ui.com/) | React component system with semantic tokens, recipes, and composition. | Fit depends on its styling/runtime architecture and your existing conventions. | V |
| C016 | [Ant Design](https://ant.design/) | Dense React application controls, tables, forms, and enterprise interaction patterns. | Particularly useful for operational tools; customize density and brand intentionally. | V |
| C017 | [HeroUI](https://heroui.com/) | Styled component ecosystem for React web and React Native. | Web and native are distinct targets; premium templates and services are separate products. | V |
| C018 | [Nuxt UI](https://github.com/nuxt/ui) | Vue components built with Reka UI and Tailwind, for Nuxt or plain Vue/Vite. | Verify v4 versus older examples; framework and theme conventions matter. | V |
| C019 | [PrimeVue](https://primevue.dev/) | Broad Vue component suite for forms, navigation, and business data. | Review theme choices and separately sold templates/support. | V |
| C020 | [PrimeNG](https://primeng.dev/) | Broad Angular suite with rich application components. | Coordinate Angular and suite versions; avoid replacing native semantics accidentally. | V |
| C021 | [PrimeReact](https://primereact.dev/) | React controls with styled and more customizable presentation paths. | Select the documented mode deliberately; licensing can differ for additional products. | V |
| C022 | [Vuetify](https://github.com/vuetifyjs/vuetify) | Vue component framework with responsive layouts, themes, and localization. | Good for consistent app UI; inspect version and support window before adoption. | V |
| C023 | [Quasar](https://quasar.dev/) | Vue components plus integrated SPA, SSR, PWA, mobile, and desktop build modes. | A broader application framework commitment, not only a component import. | V |
| C024 | [Carbon Design System](https://www.carbondesignsystem.com/) | IBM design guidance, reusable components, and enterprise patterns. | Useful for rigorous product systems; match the implementation package to your stack. | V |
| C025 | [Fluent 2](https://fluent2.microsoft.design/) | Microsoft's design guidance, UI kits, and platform component implementations. | Particularly relevant to Microsoft-style productivity experiences; platform packages differ. | V |
| C026 | [Web Awesome](https://webawesome.com/) | Framework-neutral web components with styling and component documentation. | Check custom-element SSR, form integration, and free/Pro feature boundaries. | V |
| C027 | [Tailwind Plus](https://tailwindcss.com/plus) | Commercial UI blocks and templates for accelerating page composition. | Current page redirected to login during research; verify account access, license, and framework coverage. | R |
| C028 | [daisyUI](https://daisyui.com/) | Semantic component classes and theme presets on Tailwind CSS. | CSS styling does not automatically supply all interactive behavior and accessibility. | V |
| C029 | [Bootstrap](https://getbootstrap.com/) | Framework-neutral layout, controls, utilities, and JavaScript components. | Still useful when fit is right. Homepage promotes v6 alpha; distinguish prerelease from the v5.3 stable line. | V |

### Forms, validation, and field state

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C030 | [React Hook Form](https://react-hook-form.com/) | React form registration, field state, validation, and submission handling. | Design error timing, focus, and server-error recovery; client validation is not a security boundary. | V |
| C031 | [TanStack Form](https://tanstack.com/form/latest) | Typed form state and validation with framework adapters. | Useful for complex reactive forms; headless logic still needs accessible rendering. | V |
| C032 | [Zod](https://zod.dev/) | Runtime schemas and validation with TypeScript type inference. | Reuse contracts across boundaries; do not expose raw technical validation messages to users. | V |
| C033 | [Valibot](https://valibot.dev/) | Modular runtime validation with type inference and composable schemas. | Consider when validation bundle cost matters; measure the actual selected schema bundle. | V |
| C034 | [VeeValidate](https://vee-validate.logaretm.com/v4/) | Vue value tracking, validation, submissions, arrays, and error state. | Use docs matching the installed version; plan async validation and backend errors. | V |
| C035 | [Superforms](https://superforms.rocks/) | SvelteKit client/server forms, validation, uploads, snapshots, and status messages. | Coordinate server actions and progressive enhancement; choose a supported schema adapter. | V |
| C036 | [Conform](https://conform.guide/) | Form handling around HTML semantics and server validation in React ecosystems. | Distinguish stable APIs from the documentation's explicitly marked Future APIs. | V |
| C037 | [FormKit](https://formkit.com/) | Composable fields, validation, structured form data, and schema-driven forms. | Current site presents React as well as the established Vue ecosystem; verify the exact adapter/version. | V |

### Tables, virtualization, charts, and visual analytics

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C038 | [TanStack Table](https://tanstack.com/table/latest) | Headless table models for sorting, filtering, pagination, selection, and more. | You implement rendering and accessibility; server pagination and stable row identity need explicit design. | V |
| C039 | [AG Grid](https://www.ag-grid.com/) | Full-featured interactive grids for React, Angular, Vue, and JavaScript. | Choose Community/Enterprise features deliberately; heavy data operations may belong on the server. | V |
| C040 | [Handsontable](https://handsontable.com/) | Spreadsheet-like editing, cell selection, and data-grid interactions. | Review commercial terms; spreadsheet UX is different from a read-only data table. | V |
| C041 | [TanStack Virtual](https://tanstack.com/virtual/latest) | Headless list/grid virtualization that renders the visible window. | Preserve keyboard navigation, focus, findability, and screen-reader behavior. | V |
| C042 | [React Virtuoso](https://virtuoso.dev/) | Virtualized lists, grids, tables, and variable-height conversations. | Check licensing for specialized products such as Message List; test scroll anchoring and streaming. | V |
| C043 | [Chart.js](https://www.chartjs.org/) | Canvas charts with modular registration and animation. | Supply accessible summaries/tables; avoid redrawing huge datasets unnecessarily. | V |
| C044 | [Apache ECharts](https://echarts.apache.org/en/index.html) | Configurable charts, transforms, Canvas/SVG rendering, and interactive analytics. | A broad engine; import only required modules and profile large datasets. | V |
| C045 | [D3](https://d3js.org/) | Scales, shapes, layouts, selections, geographic projections, and interaction primitives. | Highest flexibility comes with more engineering; manage DOM ownership when mixing with React. | V |
| C046 | [Recharts](https://recharts.github.io/) | Composable charts expressed as React components. | Convenient for dashboards; consider point count, responsive sizing, tooltips, and accessible alternatives. | V |
| C047 | [visx](https://github.com/airbnb/visx) | Low-level React visualization components using D3 calculations. | Useful for a proprietary chart system; axes, interaction, and accessibility need assembly. | V |
| C048 | [Observable Plot](https://observablehq.github.io/plot/) | Concise charts using layered marks, transforms, scales, and facets. | Excellent exploratory/editorial fit; complex app behavior may need additional integration. | V |
| C049 | [Highcharts](https://www.highcharts.com/) | Broad charting products for interactive business visualization. | Review commercial licensing and the accessibility/export modules required by your product. | V |

### Editors, workflow canvases, drag and drop, and specialist controls

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C050 | [Tiptap](https://tiptap.dev/) | Headless rich-text editing and extensible document workflows. | Core editor and paid extensions/cloud services have different terms; plan content migrations. | V |
| C051 | [Lexical](https://lexical.dev/) | Modular text-editor framework with editor state and extension packages. | You assemble toolbar, editing behaviors, serialization, and application integration. | V |
| C052 | [Plate](https://platejs.org/) | Rich-text editor framework, plugins, and UI components. | Evaluate the exact plugins and document schema before committing stored content. | V |
| C053 | [BlockNote](https://www.blocknotejs.org/) | React block editing with slash menus, drag handles, and collaboration integration. | Check commercial features and model/backend requirements for AI capabilities. | V |
| C054 | [ProseMirror](https://github.com/ProseMirror/prosemirror) | Schema-based rich document editing and collaborative-editing foundations. | Low-level architecture; GitHub repository has moved to the linked maintainer forge, not simply disappeared. | V |
| C055 | [CodeMirror](https://github.com/codemirror/dev) | Modular in-browser code editing with composable language/editor packages. | Its development repository moved to the maintainer forge; use package docs, not old repo activity alone. | V |
| C056 | [Monaco Editor](https://github.com/microsoft/monaco-editor) | VS Code-derived code editor with models, language services, and editor APIs. | More substantial integration and worker loading; AMD builds are deprecated. | V |
| C057 | [React Flow](https://reactflow.dev/) | React node/edge canvases for workflow builders, diagrams, and visual tools. | A canvas does not supply your execution engine; add layout, persistence, keyboard access, and undo. | V |
| C058 | [Svelte Flow](https://svelteflow.dev/) | Node-based visual interfaces using Svelte. | Use its own API; layout and business behavior remain application responsibilities. | V |
| C059 | [dnd kit](https://dndkit.com/) | Drag, drop, sortable layouts, sensors, modifiers, and framework adapters. | Current docs cover TypeScript, React, Vue, Svelte, and Solid; distinguish new APIs from older tutorials. | V |
| C060 | [Pragmatic drag and drop](https://github.com/atlassian/pragmatic-drag-and-drop) | Framework-neutral drag/drop core with optional rendering and accessibility helpers. | Assistive alternatives need explicit implementation; a pointer drag alone is incomplete. | V |
| C061 | [FullCalendar](https://fullcalendar.io/) | Event calendars, time grids, scheduling interactions, and framework integrations. | Resource/specialized capabilities may be Premium; correctly model time zones and recurrence. | V |
| C062 | [React DayPicker](https://daypicker.dev/) | Date inputs/calendars with single, multi-date, and range selection. | Use current package/version guidance; validate locale, time zone, disabled dates, and keyboard flow. | V |
| C063 | [Uppy](https://uppy.io/) | Modular upload UI with resumable transport and external-source integrations. | Requires an upload backend; configure limits, retry, cancellation, validation, and privacy. | V |
| C064 | [cmdk](https://github.com/dip/cmdk) | Unstyled React command-menu foundation. | Define useful ranking, shortcuts, discoverability, and recovery from zero results. | V |
| C065 | [Sonner](https://sonner.emilkowal.ski/) | React toast notifications with action and promise states. | Critical failures and required decisions need persistent UI; do not rely only on disappearing toasts. | V |

### Maps, galleries, carousels, panels, and onboarding

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C066 | [MapLibre GL JS](https://maplibre.org/) | GPU-rendered vector maps and customizable map styles. | Renderer is separate from map data, tile hosting, geocoding, and their licenses/costs. | V |
| C067 | [Leaflet](https://leafletjs.com/) | Interactive maps with tile layers, markers, and a plugin ecosystem. | Website announces 2.0 beta; check plugin compatibility and choose a release deliberately. | V |
| C068 | [Mapbox GL JS](https://docs.mapbox.com/mapbox-gl-js/guides/) | Styled vector maps, layers, camera controls, and Mapbox service integrations. | Account, token, service pricing, attribution, and offline use need review. | V |
| C069 | [OpenLayers](https://openlayers.org/) | Rich geospatial maps supporting varied data formats and mapping services. | Strong GIS fit; more concepts and configuration than a basic store locator. | V |
| C070 | [Embla Carousel](https://www.embla-carousel.com/) | Flexible carousel behavior with framework adapters and optional plugins. | Main docs distinguish v9 RC and v8 stable. Add labeled controls, pause, and keyboard behavior. | V |
| C071 | [Swiper](https://swiperjs.com/) | Touch-oriented sliders with modules and web/framework integrations. | Disable unnecessary modules and effects; autoplay must remain controllable. | V |
| C072 | [PhotoSwipe](https://photoswipe.com/) | Responsive lightboxes and image galleries. | Preserve captions, image dimensions, keyboard exit, and focus restoration. | V |
| C073 | [Vaul](https://github.com/emilkowalski/vaul) | React drawer interaction component found in many existing projects. | **README says unmaintained.** For new work, evaluate a maintained drawer/dialog primitive. | V |
| C074 | [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) | Resizable layouts for editor panes and productivity tools. | Persist layouts carefully; preserve minimum usable sizes and keyboard resizing. | V |
| C075 | [Driver.js](https://driverjs.com/) | Guided tours, highlights, and contextual feature hints. | Prefer useful empty states first; tours should be dismissible, replayable, and resilient to layout changes. | V |

### Design systems, handoff, icons, and component verification

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C076 | [Figma Design / Dev Mode](https://www.figma.com/dev-mode/) | Interface design, prototypes, component libraries, and developer handoff. | A prototype is not production behavior; map design components and tokens to real implementation. | V |
| C077 | [Penpot](https://penpot.app/) | Open-source collaborative design, prototyping, and design/developer workflows. | Assess self-hosting operations and ecosystem fit; confirm export fidelity with the target implementation. | V |
| C078 | [Tokens Studio](https://tokens.studio/) | Token authoring, themes, synchronization, and design-to-code workflows. | Establish ownership and review changes; plugin/platform tiers have different capabilities. | V |
| C079 | [Style Dictionary](https://styledictionary.com/) | Transforms shared design tokens into CSS, JavaScript, iOS, Android, and other outputs. | Build tooling, not a runtime UI library; transformations need platform-aware validation. | V |
| C081 | [Storybook](https://storybook.js.org/) | Isolated component development, documentation, examples, and test integration. | Include loading, error, long-content, keyboard, and responsive states, not only happy-path demos. | V |
| C082 | [Chromatic](https://www.chromatic.com/) | Hosted visual review and UI regression workflows around component/browser tests. | Screenshot baselines need human review; subscription usage depends on test volume. | V |
| C086 | [Lucide](https://lucide.dev/) | Consistent SVG icons with framework packages and configurable strokes. | Import individual icons; label meaningful icons and hide purely decorative ones from assistive technology. | V |
| C087 | [Phosphor Icons](https://github.com/phosphor-icons/core) | SVG icon assets and framework implementations with a coherent visual vocabulary. | Maintain consistent weight and optical sizing; icon meaning still needs text where ambiguous. | V |
| C089 | [Iconify](https://github.com/iconify/iconify) | Unified access to many icon sets through web/framework components and design plugins. | Each source set has its own license and visual language; avoid mixing incompatible styles. | V |
| C090 | [Polypane](https://polypane.app/) | Development browser for synchronized responsive views, accessibility inspection, and quality checks. | Useful paid workflow tool; still validate target browsers and actual touch devices. | V |

### AI design skills, component discovery, and expressive UI collections

Agent skills guide an AI's work. MCP integrations expose tools and data. Component registries distribute source. Runtime libraries execute in the shipped product. These are different layers, even when one vendor offers several.

| ID | Tool / official source | What it does and where it fits | Main decision / limitation | Evidence |
|---|---|---|---|---|
| C091 | [Impeccable](https://github.com/pbakaus/impeccable) | Agent design vocabulary and workflows for critique, auditing, refinement, motion, and context. | Development-time skill/tooling; it does not make a shipped page accessible or fast automatically. | V |
| C092 | [21st MCP / component discovery](https://github.com/21st-dev/magic-mcp) | Searches/retrieves UI components and connects coding agents to 21st workflows. | Old Magic MCP is a compatibility proxy; current unified MCP, access, and generation entitlements differ. | V |
| C093 | [Superdesign skill](https://github.com/superdesigndev/superdesign-skill) | Design exploration and iteration through an agent skill linked to the Superdesign product. | Hosted generation may require account/credits. The original IDE-extension repository is historical and unmaintained. | V |
| C094 | [Magic UI](https://github.com/magicuidesign/magicui) | Copyable animated React components and visual effects. | Treat effects as adaptable source; audit motion, contrast, interaction, and added dependencies. | V |
| C095 | [Aceternity UI](https://ui.aceternity.com/) | React/Tailwind/Motion landing-page components, blocks, templates, and interactions. | Free/commercial products differ; elaborate effects need mobile and reduced-motion treatment. | V |
| C096 | [React Bits](https://github.com/DavidHDev/react-bits) | Animated and interactive React components for distinctive presentation. | MIT + Commons Clause terms; check component redistribution restrictions. Profile GPU cost and reduced-motion behavior. | V |
| C097 | [Vue Bits](https://github.com/DavidHDev/vue-bits) | Animated and interactive Vue components. | MIT + Commons Clause terms; verify redistribution restrictions and Vue-specific component coverage. | V |
| C098 | [Kokonut UI](https://github.com/kokonut-labs/kokonutui) | React source components using Tailwind, shadcn/ui, and Motion. | Customize tokens and interaction semantics; source ownership includes upgrade responsibility. | V |
| C099 | [Cult UI](https://github.com/nolly-studio/cult-ui) | Animated shadcn registry components, cards, illustrations, and product UI. | Check each item's dependencies and adapt its visual style to the product. | V |
| C100 | [Motion Primitives](https://github.com/ibelick/motion-primitives) | Composable animated UI patterns built with Motion and Tailwind. | README calls it beta; expect API/component changes and review imported code. | V |
| C101 | [UI UX Pro Max skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent-oriented design knowledge and guidance spanning platforms and frameworks. | Preset/style suggestions need user research and product context; no guaranteed design-quality ranking. | V |
| C102 | [tweakcn](https://github.com/jnsahaj/tweakcn) | Visual theme editing for Tailwind and shadcn/ui. | A theme editor changes tokens; it does not solve information architecture or task flow. | V |
| C103 | [coss ui, formerly Origin UI](https://github.com/cosscom/ui) | Cal.com's design-system components and associated product UI source. | Old Origin repository redirects here; distinguish current packages from legacy examples. | V |
| C104 | [assistant-ui](https://github.com/assistant-ui/assistant-ui) | React/TypeScript components and integration patterns for AI chat experiences. | Plan streaming, cancellation, persistence, errors, permissions, and model/backend boundaries. | V |
| C105 | [AI Elements](https://github.com/vercel/ai-elements) | UI patterns for AI conversations, messages, code blocks, sources, and tool displays. | **Migration underway:** repo announces deprecation at end of November 2026 in favor of shadcn/ui AI Elements. | V |

### Impeccable: useful commands and how to apply the idea

[Impeccable](https://github.com/pbakaus/impeccable) provides design-oriented agent instructions and tooling. It belongs in the development workflow. Commands worth understanding include `init` for product context; `shape` for planning; `critique` for design review; `audit` for technical checks; `polish` for finish; `clarify` for copy; `typeset` for typography; `layout` for spacing; `animate` for motion; `adapt` for devices; `harden` for edge cases; and `optimize` for performance. Confirm names against the installed version.

Use it with a concrete brief, authentic content, screenshots, and success criteria. Ask for reasons behind changes and verify the rendered result. A useful sequence is context → focused critique → selected changes → browser/device checks. Multiple competing design skills can create contradictory instructions; choose one lead workflow for a given pass.

### Observed GitHub Trending snapshot

The retrieved [GitHub Trending “Today” page](https://github.com/trending), checked for this November 6, 2026 report, included [Angular](https://github.com/angular/angular), [Zed](https://github.com/zed-industries/zed), and [Google skills](https://github.com/google/skills). Angular is directly relevant to UI implementation; Zed and the skills collection are development-workflow context. This is a changing, general-purpose listing, not a UI-quality leaderboard. The targeted design repositories below are selected for their capabilities; their inclusion does not assert daily Trending placement or measured growth.

### Promising repositories to examine first

This is a **capability-based watchlist**, not a verified GitHub Trending leaderboard. No star counts, daily ranks, or growth rates are used as proof of quality. All repositories below were inspected during this research; production suitability remains component- and version-specific.

| Repository | Why it is worth examining | Evaluation focus |
|---|---|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Makes design critique and refinement explicit in coding-agent workflows. | Whether it preserves the product brief and improves actual rendered results. |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Broad searchable design guidance for agent-assisted work. | Quality of recommendations for your users, content, and constraints. |
| [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | Branchable visual exploration integrated with coding agents. | Current hosted-service costs and integration with your existing design system. |
| [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) | Documents the move to unified 21st MCP and component discovery. | Use current setup; the historical package is a compatibility bridge. |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Source ownership, registry distribution, and adaptable component foundations. | Existing primitive choice, update strategy, and local modifications. |
| [mui/base-ui](https://github.com/mui/base-ui) | Accessible unstyled foundation with growing ecosystem integration. | Complex focus, touch, overlays, and custom composition. |
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | Distinctive interactive component ideas for expressive sites. | Mobile GPU/CPU load, readability, and reduced motion. |
| [DavidHDev/vue-bits](https://github.com/DavidHDev/vue-bits) | Comparable creative component exploration for Vue. | Current component coverage and framework compatibility. |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | Approachable source-based motion and presentation patterns. | Whether each effect supports the message and earns its bytes. |
| [nolly-studio/cult-ui](https://github.com/nolly-studio/cult-ui) | Broad expressive component registry with accessible source ownership. | Theme integration and behavior across input methods. |
| [kokonut-labs/kokonutui](https://github.com/kokonut-labs/kokonutui) | Small interaction ideas and reusable product-facing components. | State completeness, token alignment, and dependency cost. |
| [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) | Focused building blocks for animated UI. | Beta status and interruptibility of composed transitions. |
| [jnsahaj/tweakcn](https://github.com/jnsahaj/tweakcn) | Fast exploration of a coherent shadcn token palette. | Contrast, theme persistence, and avoiding purely cosmetic redesigns. |
| [cosscom/ui](https://github.com/cosscom/ui) | Product-oriented system evolving from Origin UI. | Current library versus legacy Origin code. |
| [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) | Purpose-built conversational UI foundations. | Streaming/stop/retry behavior, focus, citations, and tool approvals. |

### Adoption rules that prevent an impressive demo becoming a fragile product

1. Choose a primary component system and one principal motion strategy. Add specialist libraries only for a demonstrated requirement.
2. Inspect the actual component source, package versions, license, transitive dependencies, and recent maintenance signals before adopting it.
3. Test real states: empty, loading, long content, validation errors, network failures, permission restrictions, localization, and stale data.
4. Check keyboard, focus restoration, screen reader output, touch, zoom, dark mode, forced colors, and reduced motion after integration.
5. Profile the final page on representative devices. Component-gallery speed and package-size marketing claims do not predict your application.
6. Treat copied registry source as owned code. Record provenance and a deliberate update strategy so fixes do not silently overwrite customization.
7. Prefer meaningful functionality over a novelty checklist: a usable paginator, stable table, and recoverable form often improve perceived quality more than another animated background.
8. Read agent-plugin and live-editing permissions before activating them. For example, Impeccable's current README documents a live-copy fallback that can launch a local agent with approval/sandbox bypass flags; it also documents chat-only and disabled modes. This catalog does not activate those workflows.

## 8. Platform, architecture, performance, accessibility, and QA reference

Research date: **November 6, 2026, America/Phoenix**. This section contains **79 named entries** (P044 is consolidated into C041): **60 V and 19 R**. It is a selection reference, not a ranking, installation prescription, or claim that every project needs these tools.

**Evidence:** **V** means a substantive official page or maintainer documentation was retrieved and inspected during this research. **R** means a reference candidate whose individual documentation was not successfully inspected; treat its description as a starting point and recheck before adoption. V verifies the documented capability at the linked source, not compatibility with your codebase, full maintenance health, benchmark performance, licensing suitability, or the latest release. Fit and tradeoffs below are engineering judgments. No tools were installed or benchmarked.

### Native Apple and Android

| ID | Tool / official source | What it does and best fit | Main tradeoff / adoption check | Evidence |
|---|---|---|---|---|
| P001 | [SwiftUI](https://developer.apple.com/swiftui/) | Declarative UI, state-driven transitions, previews, and integration with UIKit/AppKit; strong fit for polished Apple products. | Deployment-target availability and complex interactions can require UIKit/AppKit bridges; device profiling still matters. | V |
| P002 | [UIKit](https://developer.apple.com/documentation/uikit) | Apple's imperative iOS/iPadOS UI framework; useful for mature apps, custom presentation, and precise view/controller behavior. | More explicit lifecycle and state coordination than declarative UI; individual docs returned a JavaScript shell. | R |
| P003 | [Core Animation](https://developer.apple.com/documentation/quartzcore) | Layer animation and compositing APIs for native Apple motion, masks, transforms, and timing. | Layer/rendering expertise and accessibility semantics must accompany visual work; docs could not be read. | R |
| P004 | [UIViewPropertyAnimator](https://developer.apple.com/documentation/uikit/uiviewpropertyanimator) | Interruptible, reversible, gesture-controlled UIKit animations; useful for sheets, panels, and direct manipulation. | UIKit-specific implementation and interaction-state complexity; recheck API availability. | R |
| P005 | [AppKit](https://developer.apple.com/documentation/appkit) | Native macOS windows, menus, document workflows, keyboard behavior, and desktop controls. | Apple desktop scope and a different interaction model from touch-first apps. | R |
| P006 | [Jetpack Compose](https://developer.android.com/develop/ui/compose/animation/introduction) | Android's declarative UI approach; state-aware layout and interaction with integrated animation APIs. | Recomposition, state ownership, and layout phases affect responsiveness; native does not mean automatically smooth. | V |
| P007 | [MotionLayout](https://developer.android.com/develop/ui/views/animations/motionlayout) | Constraint-based, seekable Android layout transitions and keyframes; good for coordinated, touch-driven View layouts. | Direct children only; does not itself handle nested hierarchies or activity transitions. | V |
| P008 | [Compose Animation](https://developer.android.com/develop/ui/compose/animation/introduction) | AnimatedVisibility, AnimatedContent, value animation, transitions, springs, and animation testing; everyday native interaction motion. | Choose the simplest API that expresses state; animation-driven layout work can still cost frame time. | V |
| P009 | [Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview) | Guides Android ahead-of-time compilation for important startup and interaction paths; improves first-use experience. | Requires representative journeys and release integration; vendor percentage examples are not your app's forecast. | V |
| P010 | [Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) | Measures startup, scrolling, and large UI operations; emits measurements and traces and can generate Baseline Profiles. | Reliable comparison requires controlled hardware, builds, compilation state, and repeatable scenarios. | V |
| P011 | [Android Studio Profiler](https://developer.android.com/studio/profile) | CPU, memory, graphics, and power investigation; useful for jank, freezes, leaks, and battery problems. | Debuggable builds add overhead; choose profileable release builds for representative performance work. | V |

### Cross-platform mobile and desktop

| ID | Tool / official source | What it does and best fit | Main tradeoff / adoption check | Evidence |
|---|---|---|---|---|
| P012 | [Flutter](https://docs.flutter.dev/) | Shared Dart UI for mobile, desktop, and web, with animation and custom painting; useful for a consistent branded interaction system. | Platform conventions, semantics, text input, startup, and renderer behavior need per-platform validation. | V |
| P013 | [Impeller](https://docs.flutter.dev/perf/impeller) | Flutter rendering runtime with engine-build-time shader preparation; reduces one source of unpredictable rendering work. | Backend availability differs by platform. Inspected docs say iOS has no Skia switch; Android API 29+ defaults with fallback; web remains Skia. | V |
| P014 | [Flutter and Dart DevTools](https://docs.flutter.dev/tools/devtools) | Inspector, performance timeline, memory and CPU investigation for Flutter/Dart apps. | Use an appropriate profile/release workflow and real devices; a fast development preview proves little about delivery performance. | V |
| P015 | [React Native](https://reactnative.dev/docs/performance) | React-based native app UI; good when a React team needs native navigation, controls, and platform access. | JavaScript and UI thread work can bottleneck independently; verify release performance and native dependency compatibility. | V |
| P016 | [React Native Reanimated](https://docs.swmansion.com/react-native-reanimated/) | Runs animations on the UI thread by default, including layout, sensors, and keyboard-related motion. | Worklet/runtime and architecture compatibility require attention; advertised frame rates are capability claims, not app guarantees. | V |
| P017 | [React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/) | Native gesture recognizers and gesture composition; strong for drags, swipes, pans, and pinch interactions. | Coordinate navigation and nested scrolling, and provide accessible alternatives to gesture-only actions. | V |
| P018 | [React Native Skia](https://wcandillon.github.io/react-native-skia/) | Custom 2D drawing within React Native; useful for charts, effects, and distinctive interactive surfaces. | Drawing does not supply native semantic controls; budget GPU, memory, text, and accessibility work. Official former Shopify docs now redirect here. | V |
| P019 | [Expo](https://docs.expo.dev/) | React Native development tooling, SDK modules, development builds, preview distribution, and release services. | Native module support, build configuration, update policy, and paid service limits need project-specific checks. | V |
| P020 | [Expo Router](https://docs.expo.dev/router/introduction/) | File-based routing for Expo apps; useful for universal routes, deep links, and consistent navigation structure. | Routing conventions and platform-specific navigation behavior still need design decisions; overview verified via Expo documentation. | V |
| P021 | [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html) | Shares Kotlin logic across platforms while allowing native UI; useful when preserving separate native interaction quality. | Shared logic is not automatically shared UI; source page yielded no readable body in this pass. | R |
| P022 | [Compose Multiplatform](https://kotlinlang.org/compose-multiplatform/) | Shared declarative Kotlin UI and familiar Compose state/layout/animation APIs across mobile, desktop, and web. | Validate support and interoperability for each target; do not infer identical maturity from one platform to another. | V |
| P023 | [Tauri](https://v2.tauri.app/) | Web UI with Rust/system integration using the operating system's web renderer; desktop plus mobile targets. | System WebView differences require cross-OS testing; permissions/plugins and native integration remain engineering work. | V |
| P024 | [Electron](https://www.electronjs.org/docs/latest/) | Desktop applications with bundled Chromium and Node.js; good for substantial web-based tools and consistent browser behavior. | Bundled runtime, process architecture, resource use, security updates, and desktop conventions need deliberate management. | V |
| P025 | [Qt Quick](https://doc.qt.io/qt-6/qtquick-index.html) | QML/C++ UI with animation, input, models, and delayed object creation; useful for desktop, embedded, and device interfaces. | QML/C++ expertise, platform accessibility, deployment, and relevant Qt license terms require review. | V |
| P026 | [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui) | C#/XAML app UI shared across Android, iOS, macOS, and Windows with native access. | Platform-specific behavior and handlers may be necessary; verify exact target support and toolchain requirements. | V |
| P027 | [Avalonia](https://docs.avaloniaui.net/docs/welcome) | .NET/XAML UI using its own rendering, supporting desktop and other targets; useful for a consistent desktop product. | Drawn controls require explicit platform-fit and assistive-technology testing; platform support varies. | V |
| P028 | [Uno Platform](https://platform.uno/docs/articles/intro.html) | C#/XAML cross-platform application development; relevant for teams invested in the Windows/.NET UI model. | Validate target-specific rendering, ecosystem integration, and deployment support before selection. | R |
| P029 | [WinUI 3](https://learn.microsoft.com/en-us/windows/apps/winui/winui3/) | Native Windows UI for applications with strong Windows integration and conventions. | Windows-specific rather than a cross-platform strategy; verify Windows App SDK requirements. | R |

### Web application delivery and state architecture

Frameworks shape loading, navigation, failure recovery, and how much code a device executes. Choose these against the product's interaction model, hosting constraints, team skills, and existing code. None produces premium design automatically.

| ID | Tool / official source | What it does and best fit | Main tradeoff / adoption check | Evidence |
|---|---|---|---|---|
| P030 | [Next.js](https://nextjs.org/docs) | React full-stack framework with server/client composition, routing, data handling, and image/font optimization. | Cache, streaming, server/client boundaries, and deployment behavior need explicit understanding; framework adoption alone does not fix UX. | V |
| P031 | [React Router Framework Mode](https://reactrouter.com/start/framework/rendering) | Client rendering, server rendering, and static prerendering with route-based data and pending/error UI. | Choose rendering strategy per product; navigation, focus restoration, and pending behavior remain application responsibilities. | V |
| P032 | [Astro](https://docs.astro.build/en/concepts/islands/) | Static HTML with independently hydrated client islands and separately rendered server islands; strong for content-heavy sites. | Highly interconnected app state may need additional coordination across islands. | V |
| P033 | [SvelteKit](https://svelte.dev/docs/kit/introduction) | Svelte app framework with routes, loading, form actions, rendering choices, and deployment adapters. | Adapter/runtime behavior and server/client state boundaries matter; design validation remains separate from compilation. | V |
| P034 | [Nuxt](https://nuxt.com/docs/4.x/guide/concepts/rendering) | Vue full-stack framework with rendering choices and route-level delivery options. | Recheck version-specific caching/rendering semantics and deployment constraints; source retrieval failed in this pass. | R |
| P035 | [Qwik](https://qwik.dev/docs/) | Resumability-oriented web framework designed to defer browser execution; relevant where initial JavaScript execution is a constraint. | Different serialization and event-loading model; confirm current tooling and integration fit with a real prototype. | V |
| P036 | [Vite](https://vite.dev/guide/) | Development/build tooling for web frontends and framework integrations; useful for fast iteration and controlled output. | A build tool is not a routing, data-loading, or server-rendering architecture on its own. | V |
| P037 | [TanStack Start](https://tanstack.com/start/latest) | Full-stack React/Solid framework built around typed routes, SSR, streaming, and server functions. | Validate deployment adapters and dependency compatibility; more framework surface than a router alone. | V |
| P038 | [TanStack Router](https://tanstack.com/router/latest) | Typed route trees, parameters, URL search state, loaders, and navigation boundaries; useful for complex application navigation. | Schema design and route conventions add setup; keep shareable product state in URLs deliberately. | V |
| P039 | [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) | Server-state fetching, caching, synchronization, and mutation handling; good for responsive data-heavy apps. | Invalidation, stale data, retry, cancellation, and optimistic rollback need product decisions; it does not replace all client state. | V |
| P040 | [SWR](https://swr.vercel.app/) | React data-fetching/cache library using stale-while-revalidate behavior; useful for incremental data refresh. | Avoid confusing stale display with confirmed current data; source retrieval returned unsupported content type. | R |
| P041 | [Redux Toolkit](https://redux.js.org/toolkit/introduction/getting-started) | Structured Redux state management; includes optional RTK Query for data fetching/caching. | Useful for shared complex state, but globalizing local UI state adds needless coordination. | V |
| P042 | [Zustand](https://github.com/pmndrs/zustand) | Small React-oriented state store; useful for bounded shared client interaction state. | Store ownership, selectors, persistence, and SSR isolation require discipline; docs URL had moved or failed. | R |
| P043 | [XState](https://stately.ai/docs/xstate) | State machines, actors, and workflow orchestration; valuable for onboarding, editors, and failure-rich interactions. | Modeling cost is justified by state complexity; current docs include a v6 beta label, so confirm the intended stable version. | V |
| P045 | [Partytown](https://partytown.builder.io/) | Moves compatible third-party script work into a worker; relevant when analytics/marketing scripts dominate main-thread work. | DOM proxying and script compatibility add constraints; documentation timed out and current package status needs rechecking. | R |
| P046 | [Workbox](https://developer.chrome.com/docs/workbox) | Service-worker tooling for precaching and runtime caching; useful for resilient/offline web experiences. | Cache invalidation, authenticated data, update UX, and stale content become product responsibilities. | V |

### Image and font delivery

| ID | Tool / official source | What it does and best fit | Main tradeoff / adoption check | Evidence |
|---|---|---|---|---|
| P047 | [sharp](https://sharp.pixelplumbing.com/) | Node image processing for resizing, conversion, compositing, and optimized variants; useful in build/server media pipelines. | Native runtime/deployment requirements and CPU/memory costs need validation. | V |
| P048 | [Squoosh](https://squoosh.app/) | Local browser image compression with visual comparison; useful for hand-tuning a small number of important assets. | Manual workflow does not replace automated responsive delivery; inspect artifacts at intended display size. | V |
| P049 | [Cloudinary](https://cloudinary.com/documentation/image_optimization) | Hosted media transformations and optimization/delivery; useful for large, changing media inventories. | Transformation policy, CDN caching, costs, data handling, and vendor dependence need explicit decisions. | V |
| P050 | [imgix](https://docs.imgix.com/en-US) | Image rendering APIs, URL transformations, and responsive image integrations. | Request variants, source security, usage costs, and art direction still need management. | V |
| P051 | [fontTools / pyftsubset](https://fonttools.readthedocs.io/en/latest/) | Font inspection, transformation, and subsetting; useful for reducing font bytes while preserving needed writing systems. | Incorrect subsets break glyphs, language coverage, shaping, or features; respect font licensing. | V |
| P052 | [next/font](https://nextjs.org/docs/app/getting-started/fonts) | Next.js font loading and self-hosting support; reduces external font requests and helps stable text rendering. | Framework-specific; verify chosen fallback metrics, actual layout stability, font rights, and language coverage. | V |
| P053 | [Unpic](https://unpic.pics/) | Cross-framework image utilities/components, CDN URL handling, and placeholders. | Optimization depends on the underlying source/CDN and correct sizes; placeholder aesthetics do not prove faster meaningful loading. | V |
| P054 | [Fontaine](https://github.com/unjs/fontaine) | Font metric fallback tooling intended to reduce shifts during webfont replacement. | Recheck active integrations and fallback measurements; this individual source was not inspected. | R |

### Profiling, accessibility, testing, and production observation

| ID | Tool / official source | What it does and best fit | Main tradeoff / adoption check | Evidence |
|---|---|---|---|---|
| P055 | [Chrome DevTools Performance](https://developer.chrome.com/docs/devtools/performance) | Records runtime work to diagnose interaction latency, animation jank, scripting, rendering, and main-thread bottlenecks. | A local trace reflects its device/build/network state; use repeatable scenarios and real-user data too. | V |
| P056 | [Safari Web Inspector](https://webkit.org/web-inspector/) | WebKit inspection of layout, layers, timelines, networking, memory, and accessibility; necessary for Apple-browser issues. | Platform-specific tooling and remote-device setup; desktop emulation does not replace iPhone testing. | V |
| P057 | [Firefox Profiler](https://firefox-source-docs.mozilla.org/tools/profiler/) | Thread samples, native/JavaScript stacks, markers, and Firefox profiling; useful for browser-specific bottlenecks. | Capture/interpretation differs from Chromium, so compare user outcomes rather than expecting identical trace models. | V |
| P058 | [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) | Automated lab audits for performance, accessibility, SEO, and other page quality; useful for repeatable regression detection. | A high score is not proof of field performance, accessible journeys, or sound product design. | V |
| P059 | [PageSpeed Insights](https://pagespeed.web.dev/) | Public performance inspection combining eligible field data with a lab analysis. | Field coverage and aggregation differ from a single lab run; individual page was not inspected here. | R |
| P060 | [WebPageTest](https://www.webpagetest.org/) | Synthetic page-load testing, waterfalls, filmstrips, and configurable network/device locations. | Public site returned 403 and docs 502 in this pass; confirm current access, features, and limits. | R |
| P061 | [web-vitals](https://github.com/GoogleChrome/web-vitals) | JavaScript measurement of LCP, INP, and CLS, including attribution tooling; useful for first-party real-user monitoring. | Requires a reporting backend, privacy-aware attributes, sampling, and lifecycle handling; avoid duplicate observer registration. | V |
| P062 | [Chrome UX Report / CrUX](https://developer.chrome.com/docs/crux) | Aggregated experiences of eligible real-world Chrome users; useful for independent field context. | Not every origin/page qualifies, and Chrome users are not the entire audience. | V |
| P063 | [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility rules for DOM/UI auditing, including WCAG rules; useful in component and journey tests. | Incomplete findings need review, and passing automation cannot establish full conformance. | V |
| P064 | [Pa11y](https://pa11y.org/) | Accessibility CLI, CI, dashboard, and service options for repeatable page checks. | Ensure flows, authentication, engine configuration, and WCAG coverage match the product; combine with manual evaluation. | V |
| P065 | [Playwright](https://playwright.dev/docs/accessibility-testing) | Browser journey automation, visual comparisons, tracing, and integration with axe-based accessibility checks. | Simulated input, browser builds, and screenshots do not cover actual assistive technology or device feel. | V |
| P066 | [Cypress](https://docs.cypress.io/app/get-started/why-cypress) | End-to-end and component testing with interactive debugging; useful for browser product regression checks. | Distinguish the open-source app from paid cloud/accessibility products, and validate relevant browser/workflow constraints. | V |
| P067 | [Testing Library](https://testing-library.com/docs/) | UI queries and interactions aligned with what users perceive; useful for labels, roles, and state behavior. | Simulated DOM tests do not verify layout, rendering performance, or full browser/assistive-technology behavior. | V |
| P068 | [Sentry](https://docs.sentry.io/platforms/javascript/) | Application error/performance observation and relevant frontend diagnostics; useful for connecting failures to affected journeys. | Recheck current SDK/features/pricing; redact sensitive data, manage sampling, and measure instrumentation overhead. Source retrieval failed. | R |
| P069 | [OpenTelemetry JavaScript](https://opentelemetry.io/docs/languages/js/) | Vendor-neutral telemetry APIs/SDKs for traces, metrics, and logs; connects user actions to backend work. | Official docs explicitly label browser client instrumentation experimental; do not infer browser maturity from stable tracing/metrics APIs. | V |
| P070 | [Firebase Performance Monitoring](https://firebase.google.com/docs/perf-mon) | Apple/Android/web/Flutter performance data, network traces, native startup/rendering, custom traces, and alerts. | Validate automatic coverage and privacy/data settings per platform; custom product task measurements still need instrumentation. | V |
| P071 | [MetricKit](https://developer.apple.com/documentation/metrickit) | Apple-device performance and diagnostic reports; useful for real-world native startup, resource, and responsiveness investigation. | Aggregation/delivery and platform availability limit immediate debugging; individual docs were not inspected. | R |
| P072 | [Instruments](https://developer.apple.com/tutorials/instruments) | Apple profiling suite for runtime performance, allocations, energy, and related traces. | Device/build selection and trace interpretation matter; no native app was profiled for this research. | R |
| P073 | [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector) | Inspects Apple accessibility properties and supports auditing native interface accessibility. | Inspector output complements actual VoiceOver, switch/keyboard, text-scaling, and user testing. | R |
| P074 | [Android Accessibility Scanner](https://support.google.com/accessibility/android/answer/6006564?hl=en) | Google accessibility review aid that suggests improvements to Android apps. | A scan is advisory and cannot validate complete user journeys; source overview confirmed the tool, not every rule. | V |
| P075 | [NVDA](https://www.nvaccess.org/about-nvda/) | Windows screen reader with browser/application support; useful for testing semantics, focus, announcements, and task completion. | Requires practiced testing and representative browser combinations; one screen reader cannot represent every user. | V |
| P076 | [VoiceOver](https://support.apple.com/guide/voiceover/welcome/mac) | Built-in Apple screen reader; essential for checking Apple native/web interaction semantics. | macOS and iOS behavior differ; source returned 429, so current instructions were not verified. | R |
| P077 | [TalkBack](https://support.google.com/accessibility/android/answer/6283677?hl=en) | Android screen reader and gesture-based accessible navigation; useful for native/mobile web journey evaluation. | Device manufacturer, Android, and TalkBack versions can change behavior; test the supported device set. | V |
| P078 | [Accessibility Insights](https://accessibilityinsights.io/) | Guided web/Windows assessment, FastPass, inspection, and contrast helpers. | Inspected site explicitly advertises WCAG 2.1 AA assessment; separately cover the additional WCAG 2.2 requirements. | V |
| P079 | [Appium](https://appium.io/docs/en/latest/) | Driver-based UI automation across native/mobile/browser/desktop and other platforms. | Driver/toolchain compatibility, test IDs, device setup, and execution time add maintenance cost. | V |
| P080 | [Maestro](https://docs.maestro.dev/) | YAML-based mobile/web UI automation with CLI, desktop tooling, and cloud options; good for readable critical-journey smoke flows. | Confirm platform support and cloud terms; a deterministic flow is not a performance or accessibility audit. | V |

### Practical platform selection

| Product situation | Sensible starting shortlist | What the prototype must prove |
|---|---|---|
| Apple-only product where system behavior is central | SwiftUI plus targeted UIKit/AppKit integration | Text input, accessibility, navigation, window behavior, interruptible motion, deployment targets. |
| Android-first product | Compose, Compose Animation; MotionLayout for appropriate existing View screens | Back navigation, keyboard/insets, large-screen adaptation, TalkBack, frame-time distribution. |
| React team building mobile apps | React Native + Expo; add Reanimated/Gesture Handler only as interactions require | Native dependency fit, release startup, keyboard transitions, nested scrolling, deep links, accessible gesture alternatives. |
| Shared bespoke mobile UI | Flutter or Compose Multiplatform | Actual target-device performance, platform integration, native text/input conventions, accessibility tree. |
| Shared logic with distinct native experiences | Kotlin Multiplatform + native platform UI | Interoperability, shared-state boundaries, debugging, and whether duplicated UI effort is acceptable. |
| Web-skilled team delivering a desktop tool | Electron or Tauri | OS integration, memory/startup, update flow, accessibility, actual WebView/browser differences. |
| .NET desktop/cross-platform product | Avalonia, MAUI, Uno; WinUI 3 for Windows-specific scope | Required target support, control semantics, deployment, platform-specific interactions, license requirements. |
| Content-led website with a few interactive sections | Astro or suitable static/prerender mode in an existing framework | Essential content before JS, small interactive islands, image delivery, navigation/focus behavior. |
| Stateful web application | Existing supported stack, or Next.js / React Router / SvelteKit / Nuxt / TanStack Start | Pending/error/empty states, URL state, cache correctness, realistic interaction latency, server costs. |

### Performance and motion acceptance criteria

**Verified Core Web Vitals targets:** a good result requires **LCP ≤2.5 seconds, INP ≤200 milliseconds, and CLS ≤0.1 at the 75th percentile**; assess mobile and desktop separately. These are field targets. A laboratory score, average, or one favorable trace does not establish that users meet them. [Official Web Vitals guidance](https://web.dev/articles/vitals).

**Project budgets below are proposed engineering starting points, not WCAG requirements or universal thresholds.** Set them against actual users/devices and retain a baseline before adding animation or dependencies.

| Measure | Practical acceptance approach |
|---|---|
| Frame pacing | At 60 Hz, one display interval is about 16.67 ms; at 120 Hz about 8.33 ms. This interval includes the whole rendering pipeline. Track missed deadlines and p95/p99 frame time during representative interactions instead of quoting average FPS alone. [React Native frame guidance](https://reactnative.dev/docs/performance). |
| Response acknowledgement | Target visible acknowledgement within roughly 100 ms for direct input; keep it independent of network completion. Treat this as a product budget. Validate on the slow supported device, including queued work and touch feedback. |
| Interaction completion | Specify separate p75/p95 budgets for navigation, search, save, upload, and AI/remote work. Record time to useful output and successful completion; a spinner appearing quickly does not mean a task is quick. |
| Motion duration | Start with roughly 80–150 ms for small feedback, 150–250 ms for compact enter/exit changes, and 200–400 ms for larger spatial transitions; tune by travel distance, input, context, and platform. These are suggested design ranges, not standards. Let repeated and expert flows move faster. |
| Motion interruption | Test rapid reversal, repeated tapping, navigation during animation, gesture cancellation, resize, and state updates mid-transition. Content and focus must end in the correct state. |
| Reduced motion | Replace vestibularly heavy travel, parallax, zoom, and endless decoration with quiet state changes while preserving feedback and meaning. Test both initial system preference and runtime changes; provide product control when justified. |
| Main-thread work | Record traces during typing, scrolling, drag, open/close, and route transitions. Reduce expensive work before adding layers or memoization. Track long tasks alongside the interaction they delay. |
| Payload | Set route-specific transfer and parse/execute budgets from a measured baseline. Reserve image dimensions, serve correct responsive sizes, defer nonessential media/scripts, and inspect delivered font subsets. Avoid arbitrary one-size-fits-all KB limits. |
| Native resources | Compare cold/warm startup, p95 frame time, memory after repeated navigation, and energy/thermal behavior under a sustained workload. Use release/profileable builds and target hardware. |
| Reliability | Monitor task success, error/retry rate, abandoned flows, crashes, and app unresponsiveness alongside speed. Use privacy-aware segmentation by route, release, device class, and connection class. |

Do not ship multiple large animation/rendering systems merely because each is capable. Preserve a clear owner for every animated property and gesture, isolate expensive surfaces, and profile a representative page or screen before committing to the stack.

### Exact accessibility requirements that often affect polished interfaces

This is a focused design/testing reference, **not a complete WCAG conformance checklist**. WCAG 2.2 AA conformance includes applicable Level A requirements as well as AA requirements. The linked Understanding pages explain criteria; the [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/) is the normative source. Native applications additionally need their platform accessibility APIs and applicable product requirements.

| Criterion | Verified requirement and design implication |
|---|---|
| 1.4.3 Contrast (Minimum), AA | At least **4.5:1** for ordinary text and images of text; **3:1** for large text. Large text is at least **18 pt**, or **14 pt bold** (24 CSS px or approximately 18.67 CSS px respectively at the standard CSS conversion). Exceptions include incidental text, inactive controls, pure decoration, and logos/brand text as specified. Assess every actual background and state. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). |
| 1.4.11 Non-text Contrast, AA | **3:1** against adjacent colors for visual information necessary to identify controls/states and meaningful graphic parts, with specified inactive, unmodified user-agent, and essential-presentation exceptions. This is not a blanket requirement for every decorative border. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). |
| 1.4.4 Resize Text, AA | Text must support enlargement to **200%** without lost content/functionality and without requiring assistive technology, except captions and images of text. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html). |
| 1.4.10 Reflow, AA | Preserve information/functionality without two-dimensional scrolling at **320 CSS px width** for vertically scrolling content, or **256 CSS px height** for horizontally scrolling content. Parts genuinely requiring two-dimensional layout are excepted; the exception is not permission to make the entire page overflow. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html). |
| 1.4.12 Text Spacing, AA | With no other style changes, tolerate user overrides of line height **1.5× font size**, paragraph spacing **2×**, letter spacing **0.12×**, and word spacing **0.16×** without lost content/functionality. These are override-test values, not mandatory authored typography. Language/script exceptions apply for properties not used. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html). |
| 2.2.2 Pause, Stop, Hide, A | Automatically starting moving/blinking/scrolling information lasting **more than five seconds** alongside other content needs pause, stop, or hide unless essential. Automatically updating information alongside other content needs pause/stop/hide or frequency control unless essential; that branch has no five-second exemption. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html). |
| 2.3.1 Three Flashes or Below Threshold, A | No content flashing **more than three times in any one-second period**, unless below the defined general-flash and red-flash thresholds. Avoid flashing effects rather than assuming a tiny graphic or reduced-motion toggle makes them safe. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html). |
| 2.4.11 Focus Not Obscured (Minimum), AA | A component receiving keyboard focus must not be **entirely hidden** by author-created content. Fully unobscured focus is the stronger AAA criterion; design for that better experience where practical. Check sticky headers, banners, drawers, and overlays. User-positioned content and user-opened content have qualifying notes. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum). |
| 2.5.7 Dragging Movements, AA | A dragging function must also work with a **single pointer without dragging**, unless dragging is essential or the unmodified user agent provides the function. Keyboard support alone does not satisfy this requirement; clickable move controls or a selectable destination can. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements). |
| 2.5.8 Target Size (Minimum), AA | Pointer-target minimum: **24×24 CSS px**, subject to the five exceptions below. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum). |

**Authentication and repeated information:** [3.3.8 Accessible Authentication (Minimum), AA](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) limits required cognitive tests during authentication, with alternatives, assisting mechanisms, object-recognition, and personal-content provisions. Support password managers and paste rather than forcing memory or transcription. [3.3.7 Redundant Entry, A](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html) requires information needed again within the same process to be populated or selectable, except where re-entry is essential, needed for security, or the earlier information is invalid.

**The five 2.5.8 exceptions, precisely summarized:**

1. **Spacing:** center a **24 CSS px diameter circle on each undersized target's bounding box**. It must intersect neither another target nor another undersized target's circle.
2. **Equivalent:** a compliant control on the **same page** supplies the same function.
3. **Inline:** a sentence target, or size constrained by non-target text line-height.
4. **User agent control:** unmodified size set by the user agent.
5. **Essential:** essential or legally required presentation of the information.

The size test requires a contained, axis-aligned 24×24 CSS px square. A 24px-diameter circle may instead pass through sufficient spacing. [W3C details](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum).

**Avoid two frequent standards errors:** **44×44 CSS px** belongs to 2.5.5 Target Size (Enhanced), **AAA**. The focus-indicator area equivalent to a **2 CSS px thick perimeter** plus **3:1** change between focused/unfocused pixels belongs to 2.4.13 Focus Appearance, **AAA**; do not describe it as a new AA rule. AA still requires visible focus and applicable contrast. [Target-size comparison](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), [Focus Appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html).

### Release review checklist

- **Journeys and content:** test the main task, interrupted task, undo/retry, expired session, network timeout/offline, validation errors, empty/loading/partial states, and real long content. Verify content order makes sense without animation.
- **Layout:** inspect narrow phones, large phones/tablets, desktop resizing, landscape, safe areas, virtual keyboard, 200% text scaling, 320 CSS px reflow, translated/RTL content where supported, and user text-spacing overrides.
- **Input:** use keyboard only, visible focus, Escape/back behavior, pointer/touch/stylus where relevant, and a single-pointer alternative for dragging. Check nested scroll regions and prevent accidental gesture capture.
- **Assistive technology:** inspect roles/names/states; run actual NVDA, VoiceOver, or TalkBack journeys appropriate to supported platforms. Check focus after modals/navigation, error announcements, live regions, and data updates.
- **Motion:** test reduced motion, autoplay controls, fast repeated actions, cancellation, slow network, low-power devices, and background/resume. Keep controls and labels usable while animations run.
- **Visual quality:** inspect real media and delivered fonts, dark/light/high-contrast settings where supported, selected/disabled/error/focus states, contrast over gradients/video/glass, and screenshot differences at representative sizes.
- **Performance:** record production/profileable builds on a realistic slower device; capture startup plus repeated navigation, typing, scrolling, and heavy scenes. Compare lab regressions with field p75 and segmented p95 product timings.
- **Automation:** automate a small set of critical behavior/visual/accessibility flows; do not generate tests that merely repeat implementation details. Review false positives and untested states rather than treating a green badge as approval.
- **Production:** correlate release, route/screen, device class, and failing task with errors/performance; redact personal content and measure telemetry overhead. Assign ownership and a rollback threshold for material regressions.

### Source and status limitations

- V rows are document-verified capabilities. No stack was installed, integrated, load-tested, or accessibility-certified.
- R rows are explicitly less verified. In particular, Apple API documentation returned JavaScript-only bodies or an unsupported Markdown content type; VoiceOver returned rate limiting; WebPageTest blocked/failed; Nuxt, SWR, and Sentry returned unsupported content types; Partytown timed out; Kotlin docs returned no readable body; Zustand's attempted docs URL returned 404.
- Platform targets, stable/beta status, service limits, pricing, and license obligations can change. Inspect the linked project version/support matrix before procurement or implementation. Avoid using footer dates, popularity, or a successful documentation fetch as proof of active maintenance.
- Rendering-engine availability is target-specific. Impeller is not a blanket statement about every Flutter target, and React Native Skia is custom drawing rather than a replacement for accessible native UI.
- The accompanying [source ledger](SOURCE-LEDGER.md) records inspected primary sources and verification caveats for this section.

## 9. Styling systems, prototyping, and research tools

These complement the component, rendering, and platform catalogs. They solve different jobs: styling code, authoring interactive ideas, studying user behavior, or collecting references. Access to a paid plan or a plugin does not automatically include every hosted generation or export feature.

| ID | Tool / official source | Functionality and fit | Tradeoff / adoption note | Evidence |
|---|---|---|---|---|
| W001 | [Tailwind CSS](https://tailwindcss.com/docs/styling-with-utility-classes) | Utility styling, variants, responsive rules, themes, and composition. | A styling system, not a ready-made art direction or complete interaction layer. | V |
| W002 | [vanilla-extract](https://vanilla-extract.style/) | Typed styles/themes compiled to static CSS. | Requires build integration; dynamic runtime values need intentional design. | V |
| W003 | [Panda CSS](https://panda-css.com/) | Build-time styles, tokens, recipes, and typed variants. | Check extraction rules and framework/build compatibility. | V |
| W004 | [StyleX](https://stylexjs.com/) | Typed, composable, predictable styling system. | Evaluate its compiler and constraints against your existing build. | V |
| W005 | [Open Props](https://open-props.style/) | Framework-neutral CSS custom-property tokens for spacing, color, easing, and more. | Map primitives into your own semantic roles; avoid blindly inheriting a whole preset. | V |
| W006 | [UnoCSS](https://unocss.dev/) | On-demand atomic CSS engine with presets and integrations. | Extraction, safelisting, and preset choice affect generated output. | V |
| W007 | [CSS Modules](https://github.com/css-modules/css-modules) | Locally scoped styles with familiar CSS authoring. | Theme and variant architecture are your responsibility. | R |
| W008 | [Sass](https://sass-lang.com/) | Stylesheet preprocessing, reusable functions, mixins, and modules. | Native CSS now solves many older preprocessing needs; adopt for actual project value. | R |
| W009 | [Lightning CSS](https://lightningcss.dev/) | CSS transformation, bundling, optimization, and compatibility tooling. | Transpilation cannot fully polyfill every runtime browser feature. | R |
| W010 | [ProtoPie](https://www.protopie.io/) | High-fidelity interaction logic, device/system integration, and prototype handoff. | Validate the production implementation separately; check authoring/player platform requirements. | V |
| W011 | [Origami Studio](https://origami.design/) | Visual interaction and motion prototyping with reusable patches/patterns. | macOS-oriented authoring; validate current OS availability before choosing it on Windows. | V |
| W012 | [Framer](https://www.framer.com/) | Visual website creation, responsive composition, CMS, and publishing. | Distinct product from the Motion animation library; assess hosting, export, and app-logic constraints. | V |
| W013 | [Webflow](https://webflow.com/) | Visual website building, content management, and managed publishing. | Assess plan, custom-code, localization, CMS, and portability constraints. | V |
| W014 | [Stark](https://www.getstark.co/) | Accessibility tooling integrated into design/development workflows. | Automated/design checks do not establish complete accessibility conformance. | V |
| W015 | [Maze](https://maze.co/) | Prototype/live-site testing, interviews, surveys, and research synthesis. | Match recruitment and study method to the target audience; inspect participant-data handling. | V |
| W016 | [Lyssna](https://www.lyssna.com/) | First-click tests, card sorting, tree testing, preference tests, and interviews. | Preference is not task success; choose the correct question and representative participants. | V |
| W017 | [Dovetail](https://dovetail.com/) | Organize and analyze customer feedback and research evidence. | Validate AI summaries against original evidence; synthetic respondents do not replace observed users. | V |
| W018 | [Mobbin](https://mobbin.com/) | Research real web/mobile interface screens and flows. | Useful pattern evidence and inspiration; screenshots do not prove the pattern works for your users. | V |
| W019 | [Refero](https://refero.design/) | Interface-reference discovery for visual and product research. | Current site returned no readable content in this pass; verify current scope/access. | R |

### UI rendering and server-driven interaction alternatives

These are architectural alternatives, not appearance presets. They complement the delivery frameworks listed elsewhere.

| ID | Tool / official source | Functionality and fit | Tradeoff / adoption note | Evidence |
|---|---|---|---|---|
| W020 | [React](https://react.dev/) | Component-based interactive UI with a large web/native ecosystem. | Plan state boundaries, rendering cost, and framework-specific delivery; ecosystem size is not a quality guarantee. | V |
| W021 | [Vue](https://vuejs.org/guide/introduction.html) | Reactive component UI for incremental adoption and full applications. | Keep framework/plugin versions aligned and choose an explicit routing/data architecture. | V |
| W022 | [Svelte](https://svelte.dev/docs/svelte/overview) | Compiler-based components with state and built-in interaction primitives. | Understand the current reactivity model and distinguish Svelte components from SvelteKit application architecture. | V |
| W023 | [Angular](https://angular.dev/overview) | Integrated application framework with components, routing, forms, and tooling. | Suits teams wanting broad conventions; evaluate complexity and upgrade requirements. | V |
| W024 | [Solid](https://docs.solidjs.com/) | Fine-grained reactive UI with JSX and composable primitives. | JSX resemblance does not make React libraries drop-in compatible. | V |
| W025 | [Preact](https://preactjs.com/guide/v10/getting-started/) | Compact component rendering and a React-compatibility path. | Test exact ecosystem dependencies; compatibility does not mean identical implementation. | V |
| W026 | [Lit](https://lit.dev/) | Reactive templates and components built on Web Components standards. | Shadow DOM, SSR, forms, and accessibility integration need deliberate architecture. | V |
| W027 | [Alpine.js](https://alpinejs.dev/) | Small interactive behaviors expressed in HTML attributes. | Appropriate for bounded interactions; complex shared state may need a different architecture. | V |
| W028 | [htmx](https://htmx.org/docs/) | HTML-driven requests and partial-page swaps backed by server endpoints. | Design latency, history, focus, validation, and response trust carefully. | V |
| W029 | [Hotwire](https://hotwired.dev/) | HTML-over-the-wire approach with Turbo/Stimulus-related tooling. | Server rendering reduces some client work; network-dependent interactions still need responsive feedback. | V |
| W030 | [Phoenix LiveView](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html) | Stateful Elixir/Phoenix UI updates transmitted as rendered diffs. | Connection lifecycle and server-side state shape offline behavior and scaling. | V |
| W031 | [Laravel Livewire](https://livewire.laravel.com/) | Reactive interfaces built within Laravel/PHP workflows. | Coordinate server round trips, local interaction, loading states, and connection failures. | V |

### Research and design skills worth practicing

| Skill | What to do | Evidence of a good result |
|---|---|---|
| Problem framing | Define user, task, context, constraints, and success. | The team can explain why the interface exists. |
| Interviews / contextual inquiry | Study real needs and the environment in which work happens. | The proposed workflow addresses observed constraints, not only stated preferences. |
| Task analysis | Map the steps and decisions needed to achieve the goal. | Unnecessary steps and dangerous assumptions are visible. |
| Content modeling | Define objects, relationships, labels, and ownership. | Navigation and screens use coherent concepts. |
| Card sorting / tree testing | Study how people group and locate content. | Important destinations are findable without visual hints. |
| Flow design | Map happy paths, alternate paths, failure, and recovery. | The UI supports more than a successful demo. |
| Wireframing | Explore hierarchy and task sequence cheaply. | Structure works before visual embellishment. |
| Visual exploration | Compare distinct compositions using the same real content. | A direction wins for explicit reasons, not novelty alone. |
| Interaction prototyping | Build the uncertain gesture/state/transition at useful fidelity. | Users understand it; implementation constraints become visible. |
| Usability testing | Give realistic tasks without coaching answers. | Observe completion, mistakes, confusion, and recovery. |
| Accessibility review | Combine standards checks, assistive technology, and user testing. | Essential tasks work across relevant input and perception needs. |
| Performance investigation | Reproduce a bottleneck and measure before/after. | A change improves actual user-visible behavior. |
| Experiment design | State hypothesis, primary outcome, guardrails, and stopping criteria. | You can distinguish an improvement from random variation. |
| Design-system governance | Version tokens/components and clarify ownership. | Product evolution remains coherent and upgrades remain manageable. |


## 10. How to achieve smooth motion in practice

Smoothness depends on the whole rendering and interaction path: event handling, state updates, layout, paint, compositing, asset decoding, GPU work, and display refresh. Choosing a library is only one part of that path. The motion catalog provides techniques and tools; use these acceptance tests for the integrated result.

| Property | What to design | How to evaluate it |
|---|---|---|
| Response | Acknowledge an action promptly; separate acknowledgment from request completion. | Record the interaction on a representative slower device. |
| Continuity | Preserve position, scale, identity, and direction across states. | Repeatedly open/close, reverse, navigate back, and resize during transitions. |
| Interruptibility | Retarget from current state and velocity where appropriate. | Tap repeatedly and change direction mid-gesture. |
| Timing | Use a small coherent family of durations/springs. | Confirm feedback never makes routine work feel delayed. |
| Spatial logic | Enter/exit from meaningful origins; maintain hierarchy. | A user can explain where an object came from and where it went. |
| Stable layout | Reserve media and loading space; avoid incidental reflow. | Observe first load, fonts, validation, and asynchronous content. |
| Frame pacing | Avoid isolated long frames, not just a misleading average FPS. | Inspect traces, missed frames, and GPU/CPU bottlenecks during the actual sequence. |
| Resilience | Finish in a valid state after cancellation, error, route change, or tab hiding. | Run those interruptions explicitly. |
| Accessibility | Provide reduced motion and equivalent controls/feedback. | Complete the same task with motion reduction, keyboard, and assistive tech. |

### Timing starting points, not standards

Try roughly **80–150 ms** for small control feedback, **150–250 ms** for compact enter/exit changes, and **200–400 ms** for larger spatial transitions. These are authoring heuristics, not WCAG requirements or guarantees of user preference. Long-distance movements, gestures, large screens, and platform conventions may need different timing. Spring parameters are engine-specific: the same stiffness/damping numbers do not necessarily produce the same motion in different libraries. Do not add a delay merely to make an effect visible.

### Common expensive or disruptive treatments

| Treatment | Appropriate use | What to constrain |
|---|---|---|
| Blur / glass / backdrop filters | Layer separation in a deliberate material system | Large overlapping blur regions, contrast loss, GPU cost |
| Parallax / scroll pinning | Spatial storytelling and product demonstrations | Motion sickness, keyboard access, trapped scroll, phone usability |
| Magnetic buttons / custom cursors | Optional fine-pointer expression | Do not move the real hit target unpredictably; preserve native affordances |
| Text splitting / scramble / typewriter | Short branded moments | Immediate comprehension, selectable text, nested links, screen reader duplication |
| Marquees / looping carousels | Secondary visual rhythm | Pause controls when applicable, readability, battery, distraction |
| Large shader backgrounds | A specific authored visual experience | Resolution, frame time, context loss, motion preferences, readable fallback |
| 3D product scenes | Interaction reveals useful product information | Download size, textures, draw calls, accessibility, low-end fallback |
| View/page transitions | Preserve context between destinations | Focus/history correctness, interruption, browser fallback, navigation delay |
| Skeleton shimmer | Brief anticipation of known content structure | Layout stability, repeated animations, delayed error disclosure |
| Celebratory particles / sound | Occasional meaningful completion | Motion/audio control, repetition, task interruption |

## 11. Choosing and maintaining a toolset

### A practical evaluation rubric

Score candidates 0–3 for each criterion: 0 unusable/unproven, 1 substantial work, 2 adequate, 3 strong fit. **Treat accessibility, licensing, and essential platform support as gates**; do not average a blocking failure away with visual scores. This rubric is an organizational aid, not a scientific quality ranking.

| Criterion | Question |
|---|---|
| Task fit | Does it directly solve a real interaction or production problem? |
| Accessibility | Can the integrated result satisfy required semantics, focus, input, and perception needs? |
| Visual control | Can it express the brand without brittle overrides? |
| Performance | What happens with your assets, content volume, network, and weakest supported device? |
| Platform fit | Does it support your framework versions, SSR/hydration approach, native targets, and browsers? |
| State completeness | Does it handle errors, cancellation, empty states, async updates, and interruptions? |
| Maintenance | Are releases, migration instructions, issue responses, and ownership credible for your use case? |
| License and cost | Are your actual use, redistribution, templates, editor features, and asset rights permitted? |
| Ownership | Can you maintain or replace it, export your assets/data, and debug the result? |
| Integration cost | How much glue, testing, build configuration, and skill does the team need? |

### What to check before adopting a repository

1. Verify the canonical project and documentation; old names, forks, archived mirrors, and transferred repos are common.
2. Check the release channel. Main-branch demos may use alpha, beta, or release-candidate APIs.
3. Inspect releases, substantive commits, maintainer responses, unresolved regressions, and migration guides. A low commit rate alone does not prove abandonment.
4. Read the exact license and relevant asset/plugin terms. “Free,” source available, open source, and permitted commercial redistribution are different claims.
5. Build one representative difficult interaction with realistic content. Measure the compiled asset cost and actual runtime behavior.
6. Check keyboard/touch/assistive technology, reduced motion, localization, and your slowest supported device.
7. Record the chosen version, why it won, known limitations, and how to replace or upgrade it.

### Useful combinations without unnecessary duplication

- **Lean branded landing page:** semantic HTML + CSS tokens + responsive media + one motion strategy; add GSAP when its timeline, scroll, SVG, or interaction capabilities solve a concrete requirement.
- **React application:** one accessible primitive/component system + a chosen styling layer + query/state/form tools only as needed + Motion or a focused native animation approach.
- **Expressive 3D React experience:** Three.js + React Three Fiber + selected Drei utilities, with one intentional animation owner and a useful static fallback.
- **Content-heavy site:** a content-oriented renderer + search + stable typography + selective islands of interactivity.
- **Native iOS/Android product:** platform UI and animation foundations, with accessibility, gesture, keyboard, and lifecycle behavior designed alongside visuals.
- **Cross-platform mobile:** React Native or Flutter with the platform-specific adaptation budget treated as part of the project.

Use these combinations as hypotheses. Keep an established architecture when it already serves the product well.

## 12. A reusable brief for AI-assisted UI/UX work

Copy this into a coding/design assistant and fill in the brackets. Supply references and authentic product content where available.

```text
Design or improve [surface] for [audience], helping them complete [primary task].
Success means [observable outcomes]. Existing stack and constraints: [details].
Preserve these working capabilities and factual claims: [list].
Use this visual direction, authentic assets, and references: [links/files].
Avoid these specific mismatches: [examples].

Use the Premium UI/UX Field Guide as a reference, selecting only relevant tools.
Recommend the smallest suitable stack and explain material tradeoffs.
Verify the current official docs, versions, licenses, and platform support for
anything you propose adopting. Treat R-marked catalog entries as unverified.

Specify layout, typography, tokens, responsive behavior, navigation, and all
important states. Include keyboard/focus behavior, text scaling, localization,
empty/loading/error/success/offline states as applicable.

For motion, explain what each animation communicates, its timing/physics,
interruption behavior, property ownership, and reduced-motion alternative.
Set performance budgets appropriate to the surface and target devices.

Build and review with real content. Verify the primary tasks and rendered UI
on relevant desktop/mobile platforms, including slower hardware and adverse
network states. Report what was tested and any remaining limitations.
Keep local previews, committed work, deployment, and user approval distinct.
```

## 13. Keeping this reference useful

Recheck selected dependencies when starting a project and before major upgrades. Revisit fast-moving skills, registries, hosted tools, and browser-sensitive APIs more frequently. Record discoveries in a project-local decision log using: **tool/version · official URL · checked date · purpose · license · target support · measured cost · decision · known risks**.

The source ledger accompanies this guide. Inspection establishes what the retrieved source said at research time; it does not replace installation tests, a security review, a legal assessment of a license, or user research.

