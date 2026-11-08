# Quality checklist, surface acceptance criteria, and adoption rubric

Use rows as acceptance criteria; select those relevant to the surface. Heuristics guide judgment; user research establishes whether a design works for an audience. Foundations: NN/g heuristics, W3C APG, WCAG 2.2.

## Surface acceptance criteria

| Surface | Must be true |
|---|---|
| Hero | Clear proposition, authentic visual, obvious action, fast primary content, mobile art direction |
| Sections | Logical story, useful headings, varied but coherent composition, real evidence, accessible structure |
| Navigation | Current location, descriptive labels, keyboard/touch, deep links, back/forward, focus and scroll restoration |
| Pagination | Current page, sensible range, prev/next, clear disabled state, preserved filters/sort, URL state |
| Typography | Coherent roles, readable measure/leading, thoughtful wrapping, real text, stable fonts, script coverage |
| Forms | Persistent labels, autofill, clear validation, input recovery, loading/success/error, duplicate-submit handling |
| Modal / sheet | Correct label, focus lifecycle, dismissal, scroll handling, keyboard/insets, safe areas |
| Table / chart | Units and headings, meaningful selection/sort, responsive behavior, keyboard and textual alternatives |
| Empty / loading / error | Explain state and next action; preserve layout and work; useful retry |
| Motion | Purpose, consistent timing, interruption/reversal, bounded cost, meaningful reduced-motion equivalent |

By surface type: **Landing** → first-screen comprehension, LCP, CTA, phone layout · **Portfolio/experiential** → direct access, reading, keyboard, motion reduction, GPU load · **SaaS app** → task throughput, forms, focus, error recovery, INP · **Dashboard** → readability, units, large datasets, stale states, export · **Editorial/docs** → reading, search, copy/share, deep links, fonts · **Commerce** → pricing truth, stock, cart persistence, payments, device performance · **Desktop/creative tool** → precision input, persistence, large documents, multiwindow.

## The 140 checks (condensed)

**Purpose, content, trust** — Q001 clear primary task · Q002 audience fit · Q003 IA by mental models · Q004 one name per object/action · Q005 progressive disclosure · Q006 evidence-based claims · Q007 honest pricing/commitments · Q008 outcome-named actions · Q009 useful errors (what, affected, next) · Q010 editable home for changing content · Q011 context-preserving help · Q012 ethical choice architecture · Q013 research loop · Q014 inclusive imagery/alt/localization · Q015 task-based success measures defined before polish.

**Visual system** — Q016 deliberate identity · Q017 strong hierarchy · Q018 consistent spacing with optical corrections · Q019 optical alignment · Q020 recompose at small sizes · Q021 intrinsic layouts handle long/missing content · Q022 container-responsive components · Q023 density options without shrinking targets · Q024 purposeful negative space · Q025 clear surface hierarchy · Q026 semantic color roles · Q027 contrast on real pairs incl. translucent · Q028 complete dark mode · Q029 system + persisted theme without flash · Q030 controlled material effects · Q031 authentic media with rights · Q032 focal points and mobile crops · Q033 consistent icon grammar · Q034 data color not hue-only · Q035 governed system (tokens, contracts, versioning).

**Typography** — Q036 purposeful family · Q037 clear roles · Q038 fluid, zoom-safe sizing · Q039 45–75 ch measure as a start · Q040 leading per size/script · Q041 tracking sparingly · Q042 balanced breaks, no brittle manual `<br>` · Q043 tabular numerals, fractions, ligatures · Q044 optical sizing · Q045 font loading stability · Q046 subsetting preserves needed glyphs · Q047 real selectable text · Q048 rich text structure · Q049 RTL/script support · Q050 survives user text overrides.

**Navigation & pagination** — Q051 stable global nav · Q052 visible current location · Q053 links navigate, buttons act · Q054 keyboard sequence and widget keys · Q055 skip link · Q056 no hover-only menus · Q057 mega-menu focus/escape/pointer travel · Q058 mobile reach, safe areas, keyboard · Q059 sticky UI restraint · Q060 refresh/deep link/back/titles · Q061 scroll and focus restoration · Q062 search quality · Q063 command palette with alternatives · Q064 tabs vs links semantics · Q065 numbered pagination completeness · Q066 pagination URL state · Q067 cursor pagination for feeds · Q068 load-more with count · Q069 infinite feed recovery · Q070 filter/sort continuity.

**Heroes & sections** — Q071 hero comprehension · Q072 demonstrative media · Q073 one primary CTA · Q074 real LCP first · Q075 responsive art direction · Q076 credible proof · Q077 section narrative · Q078 varied rhythm, one system · Q079 feature clarity, no icon-card filler · Q080 honest comparisons · Q081 pricing comprehension · Q082 FAQ as real objections, accessible disclosures · Q083 working contact path · Q084 useful footer · Q085 nonblocking storytelling.

**Controls, forms, overlays** — Q086 complete control states · Q087 obvious hit areas · Q088 immediate acknowledgment · Q089 persistent labels · Q090 input types/autocomplete/inputmode · Q091 timely validation · Q092 error summary association · Q093 preserve appropriate input (not secrets) · Q094 password-manager friendly · Q095 multi-step orientation · Q096 upload usability · Q097 date/time clarity · Q098 destructive handling with undo · Q099 modal focus lifecycle · Q100 popover ≠ modal · Q101 no essential info in tooltips · Q102 bottom-sheet quality · Q103 toast restraint · Q104 drag alternatives · Q105 gesture arbitration · Q106 haptic restraint · Q107 bulk-action clarity · Q108 resizable workspace minimums · Q109 editor confidence (undo, autosave) · Q110 table usability.

**State, resilience, polish** — Q111 intentional empty states · Q112 proportional loading UI · Q113 accurate progress · Q114 optimistic with rollback · Q115 stale-data visibility · Q116 offline/reconnect · Q117 duplicate prevention · Q118 partial-failure recovery · Q119 session continuity · Q120 permission states · Q121 screen-reader semantics · Q122 reduced motion · Q123 reduced sensory load (loops, sound) · Q124 high contrast/forced colors · Q125 localization resilience · Q126 chart comprehension · Q127 adaptive-device testing · Q128 consistent animation grammar · Q129 correct cancellation · Q130 quiet when hidden · Q131 success means success · Q132 measured polish.

**Product-specific** — Q133 commerce/checkout (stock, totals, shipping, guest, recoverable payment, receipts) · Q134 auth/onboarding (passkeys, first success) · Q135 AI/chat (generated vs sourced, stop, edits, review) · Q136 collaboration (presence, conflicts, history) · Q137 media (captions, keyboard, buffering) · Q138 maps (list alternative, clusters, permission context) · Q139 notifications (priority, preferences, outcomes) · Q140 account/settings (search, saved state, export, deletion).

Full text with implementation questions: `grep -n "^| Q0" references/library/field-guide.md`.

## Adoption rubric (0–3 each; a11y, license, platform support are gates)

Task fit · Accessibility · Visual control without brittle overrides · Performance with real assets on the weakest device · Platform fit (framework versions, SSR/hydration, browsers) · State completeness (errors, cancellation, empty, async) · Maintenance credibility · License and cost for actual use · Ownership (maintain, replace, export, debug) · Integration cost. Do not average a blocking failure away with visual scores.

## Five rules against fragile "premium"

1. One primary component system, one principal motion strategy; specialists only for concrete requirements.
2. Real content and real tasks before decoration.
3. Keyboard, touch, screen reader, reduced motion, failure, and recovery are part of the design.
4. Review docs, release channel, license, maintenance, and platform support before adoption.
5. Judge by task completion and measured runtime behavior alongside visual quality.

## UX laws that decide conversion

Fitts (big, close targets; sticky CTAs) · Hick (fewer choices; one primary CTA per section) · Jakob (platform conventions; novelty only where it delights) · Doherty (< 400 ms response) · Miller (chunk 5–7) · Aesthetic-usability (polish buys forgiveness, not for broken flows) · Peak-end (invest in the success moment and the exit) · Zeigarnik/goal-gradient (progress indicators) · Von Restorff (one distinct element = the CTA) · Tesler (absorb complexity in defaults) · Postel (accept messy input, strict output) · Gestalt (space and containers over lines). Response: < 100 ms instant · < 1 s keeps flow · > 1 s progress · > 10 s notify.
