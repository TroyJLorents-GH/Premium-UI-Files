# Tool integrations

How and when to use the research, component, generation, and smooth-scroll tools this skill assumes are available. Agent skills guide the work; MCP servers expose tools and data; registries distribute source; runtime libraries ship in the product. Keep those layers distinct.

## Contents

1. Research: Refero Styles and Mobbin
2. Components: 21st.dev CLI and MCP, registries
3. Design workflow: Impeccable and other design skills
4. Generated media: Higgsfield disclosure rule
5. Smooth scroll: Lenis
6. Documentation: Context7 and official sources
7. Argon site

## 1. Research: Refero Styles and Mobbin

**Refero Styles** is a curated library of 2,000+ design systems extracted from production websites into machine-readable `DESIGN.md` files (colors, type, spacing, radius, shadows, component conventions). Use it to:

- Ground a direction: pull two or three DESIGN.md files from products in the same category and tone as the brief; note what they share (that is the category convention) and where one diverges (that is a direction choice).
- Derive concrete token values when the user has no brand: start from a reference's scale, then change hue, type pairing, and radius so the result is not a clone.
- Answer "what do good products do here" with evidence rather than memory.
- Validate: Refero also indexes real screens and flows for visual pattern research.

Never reproduce one reference's palette, type, and layout together. One source becomes a copy; three sources become a direction.

**Mobbin** holds hundreds of thousands of real app and web screens with full user journeys and component flows. Use it for UX structure: onboarding, checkout, settings, empty states, permission prompts, pagination, filters. Search by flow, not by style. A screenshot proves the pattern exists at a shipped product, not that it works for this audience; pair with the quality checklist. When a design review needs a comparison, pull two flows and name what each does better.

## 2. Components: 21st.dev CLI and MCP, registries

21st.dev aggregates 60+ expressive component collections (Magic UI, Aceternity, React Bits, Motion Primitives, Cult UI, Kokonut, and others) with search, code fetch, a shadcn-compatible registry, logos, and an MCP server.

```bash
21st search "hero section"                          # free; components, themes, templates
21st search "pricing table" --type component --limit 5
21st search "dark dashboard" --type theme
21st search "saas starter" --type template --free
21st search "bento grid" --context auto             # rank against the project's Design Context
21st get <id>                                       # component code + demo; free on paid plans, metered on free tier
21st theme <id>                                     # theme CSS; free
21st add <user>/<slug>                              # installs via npx shadcn add against /r/<user>/<slug>
21st add <user>/<slug> --print                      # print the command instead of running it
21st add @<registry>                                # install a whole shadcn registry (no 21st fetch, no login)
21st logo discord                                   # brand/UI SVG logos, free
21st bookmarks | lists | teams                      # saved items, named lists, team libraries
```

Every command accepts `--json`. Flags: `--type c|component|theme|template|all`, `--tag`, `--color`, `--sort`, `--free/--paid`, `--author`, `--mine`, `--liked`. Full docs index: `https://help.21st.dev/llms.txt`.

Rules when pulling components:

- Search before `get`; `get` is metered on the free tier, so fetch only what you will adapt.
- Prefer `--print` before `add` in an unfamiliar project so the shadcn command and its dependencies are visible before anything is installed.
- Treat fetched code as owned source: rename to the project's tokens, remove hard-coded colors and gradients, add `prefers-reduced-motion`, verify keyboard and focus, check bundle impact and GPU cost on a phone, check the license (React Bits/Vue Bits are MIT + Commons Clause; Aceternity and Magic UI have free and pro tiers).
- Record provenance (collection, id, date) in a comment or decision log so later updates do not silently overwrite customization.
- The old Magic MCP package is a compatibility proxy; the unified 21st MCP is current. Entitlements for generation differ by plan.

Other registries and sources: shadcn/ui blocks and Visual Builder, Tailark/shadcnblocks (marketing sections), Codrops (original effects with tutorials), Uiverse (CSS snippets), Lucide/Phosphor/Iconify (icons), Fontsource/Google Fonts/Fontshare (type).

## 3. Design workflow: Impeccable and other design skills

Impeccable is a design vocabulary and command set for coding agents: `init` (product context), `shape` (plan), `critique` (design review), `audit` (technical checks), `polish` (finish), `clarify` (copy), `typeset` (typography), `layout` (spacing), `animate` (motion), `adapt` (devices), `harden` (edge cases), `optimize` (performance). Confirm names against the installed version.

- Run one lead workflow per pass with a concrete brief, authentic content, screenshots, and acceptance criteria. Ask for reasons behind each change and verify the rendered result.
- Useful sequence: context → focused critique → selected changes → browser/device checks.
- Do not stack competing design skills (Impeccable, UI UX Pro Max, Superdesign, frontend-design) in the same pass; they issue contradictory instructions. Pick the one whose scope matches the pass and let this skill supply the acceptance bar.
- Read its permission notes: the README documents a live-copy fallback that can launch a local agent with approval/sandbox bypass flags, plus chat-only and disabled modes. Do not activate live modes without the user's explicit go-ahead.
- Superdesign's original IDE extension repository is historical and unmaintained; the current product and skill are different and may require an account or credits.

## 4. Generated media: Higgsfield disclosure rule

Higgsfield (images, video, 3D, audio) spends credits. The user's standing rule:

> Before using Higgsfield, tell the user what it will be used for and the estimated token/credit cost.

Procedure:

1. Decide whether generated media is needed at all. Default to real product assets, the user's own files, or a documented placeholder that is clearly marked. Generate only when the design genuinely needs media that does not exist (a hero visual for a product with no photography, a texture, a short ambient loop).
2. Before any generation call, state in one short message: the purpose (which section/element), what will be generated (count, format, dimensions, model), and the estimated cost (query `balance` and the model's pricing via `models_get`/`show_plans_and_credits` when available; otherwise give a stated estimate and say it is an estimate).
3. Wait for approval. Do not batch-generate variations beyond what was approved.
4. After generation, report actual spend and where the assets were saved; optimize them (AVIF/WebP, dimensions, poster frames) before use.
5. Apply the same disclosure to any other paid generator the user connects.

## 5. Smooth scroll: Lenis

Marketing and experiential pages only. Setup and the single-ticker rule are in `motion-system.md` §7 and `scroll-and-3d.md` §3. Checklist: `autoRaf: false` with `gsap.ticker`; `lenis.on("scroll", ScrollTrigger.update)`; `lagSmoothing(0)`; `data-lenis-prevent` on nested scrollers; touch stays native; not instantiated under reduced motion or inside native WebViews; incompatible with native CSS scroll-snap (use its snap addon); anchors via `lenis.scrollTo` plus manual focus management; `lenis/react` or Vue/Nuxt wrappers in frameworks; Locomotive Scroll v5 if declarative `data-scroll` attributes are preferred.

## 6. Documentation: Context7 and official sources

Library APIs move faster than any skill. Before writing code against GSAP, Motion, Lenis, Three.js/R3F/Drei, shadcn/Base UI/Radix, Tailwind, Next/Astro/SvelteKit, resolve the library in Context7 (`resolve-library-id` → `query-docs` with the full question) or read the official page. Captured demos in the bundled GSAP playbook mix GSAP 3.14–3.15, React 17, Pixi 5, and jQuery; those strings are provenance, not recommendations. Register only the GSAP plugins actually used, and keep core and plugins on one compatible version.

## 7. Argon site

The user's Google Site generated from the Master UI/UX reference requires Google sign-in and could not be read while this skill was authored. If a session has browser access with the user signed in, it can be used as a shared reference and extended with results from this skill; otherwise treat the three Markdown references bundled here as the source of truth.
