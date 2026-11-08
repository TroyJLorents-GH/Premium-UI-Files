# Source library (verbatim originals)

Large originals kept verbatim for deep lookups with official URLs and evidence flags. **Grep or open by section; do not read whole files.** Snapshot date 6 Nov 2026. Rows marked `R` were not individually verified; recheck versions, licenses, and support before adopting.

| File | Size | What it is | Best for |
|---|---|---|---|
| `cheat-sheet-2026.md` | ~110 KB | 21 sections: motion libs, native platform, scroll, 3D, Lottie/Rive, components, collections, styling, typography, **section playbook**, transitions/frameworks, **performance**, **accessibility**, mobile, **tokens/color**, **motion numbers**, **UX laws**, rich content, tooling, **legacy**, sources | "Which tool / how is X built", version and status checks |
| `field-guide.md` | ~160 KB | Evidence-flagged field guide: 140 quality checks (Q001–Q140), surface recipes, browser-native capabilities, motion/3D catalog (M001–M088), component catalog (C001–C105), platform/perf/a11y catalog (P001–P080), styling/research (W001–W031), rubric, reusable AI brief | Deep dives, adoption rules, acceptance criteria, exact WCAG text |
| `foundation-principles-of-motion.md` | ~35 KB | Creative direction + 3D pipeline: hierarchy of attention, tool licensing table, 5-step workflow, lexicon, 6-layer prompt, **three worked code examples** (GLB + SVG HUD, 2.5D depth hero, Flip bento → inspector), 7 failure modes, QA protocol | Cinematic/3D/scroll work with code |
| `tool-index.csv` | ~100 KB | 341 rows: `id,category,name,function,tradeoff,evidence,url,research_date` | `python3 scripts/lookup.py "<keyword>"` |
| `source-ledger.md` | ~25 KB | What was verified (V) vs reference-only (R), access failures, caveats | Trust calibration |

## Section locator

**cheat-sheet-2026.md** (`grep -n '^## ' cheat-sheet-2026.md`): 1 JS motion libraries · 2 Native web platform · 3 Scroll · 4 3D/WebGL/shaders · 5 Lottie/Rive/SVG/icons · 6 Component libraries & headless · 7 Animated component collections · 8 Styling systems · 9 Typography · 10 Page-section playbook · 11 Transitions/routing/frameworks · 12 Performance · 13 Accessibility · 14 Mobile · 15 Tokens/theming/color · 16 Motion principles & numbers · 17 UX laws & conversion · 18 Rich content · 19 Tooling & workflow · 20 Legacy/deprecated · 21 Sources.

**field-guide.md**: 1 Read first · 2 Fast selection · 3 Qualities to specify (Q-rows) · 4 Surface recipes · 5 Browser-native (B-rows) · 6 Motion/graphics/3D (M-rows, patterns, smoothness checklist) · 7 Components & design workflow (C-rows, Impeccable, watchlist, adoption rules) · 8 Platform/perf/a11y/QA (P-rows, exact WCAG, release checklist) · 9 Styling/prototyping/research (W-rows) · 10 Smooth motion in practice · 11 Rubric · 12 Reusable AI brief · 13 Maintenance.

Examples: `grep -n "Q099\|Q104" field-guide.md` · `grep -n -i "view transition" cheat-sheet-2026.md` · `grep -n "^### " foundation-principles-of-motion.md`.
