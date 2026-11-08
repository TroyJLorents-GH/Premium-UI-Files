# Source library index

Large originals supplied by the user, kept verbatim. **Grep or open by section; do not read whole files.** Snapshot date 6 Nov 2026. Catalog rows marked `R` were not individually verified; recheck versions, licenses and support before adopting.

| File | Size | What it is | Best for |
|---|---|---|---|
| `cheat-sheet-2026.md` | ~110 KB | 21 sections: motion libs, native platform, scroll, 3D, Lottie/Rive, components, typography, section patterns, performance, a11y, mobile, tokens, motion numbers, UX laws, legacy | First stop for any "which tool / how is X built" |
| `field-guide.md` | ~160 KB | Evidence-flagged field guide: qualities to specify, surface recipes, platform/perf/a11y reference, evaluation rubric, reusable AI brief | Deep dives, adoption rules, acceptance criteria |
| `quick-reference.md` | ~6 KB | One-page job → tool table and rules | Fast routing |
| `engineering-reference.md` | ~25 KB | Motion architecture, WebGL/shaders, scroll mechanics, view transitions, materials, component patterns, 120Hz budgets | Technical specifics |
| `master-motion-reference.md` | ~15 KB | Checklist of engines, shaders, CSS APIs, micro-interactions, formulas (lerp, rubber-band) | Quick technique lookup |
| `foundation-principles-of-motion.md` | ~35 KB | Creative direction + 3D pipeline: hierarchy of attention, Blender→glTF→Three.js, single ticker, failure modes, QA protocol | Cinematic/3D/scroll work |
| `source-ledger.md` | ~25 KB | What was verified (V) vs reference-only (R) and access caveats | Trust calibration |
| `tool-index.csv` | ~100 KB | 341 rows: id, category, name, function, tradeoff, evidence, url, date | `grep -i "name" tool-index.csv` |
| `../gsap-playbook/` | — | GSAP plugin demos/prompts + `INDEX.md` router + `source-caveats.md` | Any GSAP implementation |
| `../../assets/motion-lab-reference.html` | ~175 KB | Working "AETHER" 120Hz lab page (Tailwind CDN, Houdini `@property`, spotlight cards, beams) | Technique reference only; do not reuse brand/palette |

## Section locator

### cheat-sheet-2026.md
1 JS motion libraries · 2 Native web platform · 3 Scroll (smooth, triggered, carousels) · 4 3D/WebGL/shaders · 5 Lottie/Rive/SVG/icons · 6 Component libraries & headless · 7 Animated component collections · 8 Styling systems · 9 Typography · **10 Page-section playbook** · 11 Transitions/routing/frameworks · **12 Performance** · **13 Accessibility** · 14 Mobile · **15 Tokens/theming/color** · **16 Motion principles & numbers** · **17 UX laws & conversion** · 18 Rich content (charts, tables, editors, maps, forms) · 19 Tooling & workflow · **20 Legacy/deprecated** · 21 Sources.

Find a heading line: `grep -n '^## ' cheat-sheet-2026.md`.

### field-guide.md (headings by number)
1 Read first · 2 Fast selection · 3 Qualities to specify (purpose, visual system, typography, navigation, hero/landing, controls, state/resilience) · 4 Surface recipes · 5 Browser-native capabilities · 6 Motion/graphics/3D (patterns, smoothness checklist) · 7 Components & design workflow (AI design skills, Impeccable, watchlist repos, adoption rules) · 8 Platform/perf/a11y/QA (exact WCAG requirements, release checklist) · 9 Styling/prototyping/research · 10 Smooth motion in practice · 11 Choosing a toolset (rubric) · **12 Reusable AI brief** · 13 Maintenance.

### foundation-principles-of-motion.md
Part A foundations (hierarchy, easing, typography as architecture, lighting, restraint) · Part B advanced techniques · tool-selection table with licenses · 5-step workflow · motion vocabulary + 6-layer prompt · three worked examples (GLB + SVG HUD, 2.5D depth hero, Flip bento→inspector) · 7 failure modes · QA checklist · copy-ready SKILL draft.

## Using the CSV

Columns: `id,category,name,function,tradeoff,evidence,url,research_date`. Evidence `V` = official docs/repo inspected; `R` = reference candidate needing a fresh check. Example: `grep -i "lenis\|scrollsmoother" tool-index.csv`.
