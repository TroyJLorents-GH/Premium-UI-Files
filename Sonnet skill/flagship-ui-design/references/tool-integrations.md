# Tool integrations

These tools sit at different layers. **Skills** guide the agent's work, **MCP servers** expose data and actions, **registries** distribute source code, **runtime libraries** ship in the product. Don't conflate them, and don't use two competing "design lead" skills in one pass.

Availability varies per session. If a tool is not connected or needs auth, say so in one line and fall back (see each section). Never ask the user to paste tokens or OAuth codes; point them to `/mcp`.

## Contents
- Impeccable
- Refero (Styles + MCP)
- Mobbin
- 21st.dev
- Higgsfield (announce-and-confirm protocol)
- Lenis
- Other useful repos and skills
- Combining the tools: a typical research pass

---

## Impeccable (design engine and critique)

Open-source design skill and polish toolkit for coding agents. Invoke the installed `impeccable` skill rather than re-implementing its checks.

- Run its context loader once per session (it reads PRODUCT.md / DESIGN.md and surface briefs).
- Commands: `init`, `shape`, `critique`, `audit`, `polish`, `animate`, `bolder`, `quieter`, `colorize`, `typeset`, `layout`, `distill`, `adapt`, `clarify`, `harden`, `onboard`, `optimize`, `extract`, `document`, `live`. Confirm against the installed version's command table.
- Best use: a concrete brief + authentic content + screenshots + acceptance criteria → focused critique → selected changes → browser/device checks. Ask for reasons behind changes.
- It is a development-time tool. It does not make a shipped page fast or accessible by itself; run `quality-gates.md` anyway.
- Its `live` mode can launch a local agent with elevated flags. Get user approval first.
- Its anti-pattern detector and craft floor are complementary to `anti-slop.md`; when they disagree on a pinned brief, the brief wins.

## Refero (Styles + MCP)

Refero Styles: a curated library of 2,000+ design systems extracted from real production sites, packaged as machine-readable DESIGN.md. Use it to anchor tokens in something real.

Tools (when connected): `refero_search_styles`, `refero_get_style`, `refero_search_sites`, `refero_search_screens`, `refero_get_screen`, `refero_get_screen_image`, `refero_get_similar_screens`, `refero_search_flows`, `refero_get_flow`, `refero_search_apps`. The `refero-design` skill documents the intended flow; use it if installed.

Workflow:
1. Search styles by mood + product category + surface (e.g. "editorial dark fintech dashboard").
2. Fetch 2–3 candidate styles; compare type pairings, spacing scale, radius, shadow, color roles.
3. Extract *principles and token structure*, then translate into this project's tokens. Do not ship another brand's identity (name, logo, signature illustration, exact palette + type combo) as your own.
4. Record which style(s) informed which decisions in the final report.

## Mobbin (flows, screens, sections)

Hundreds of thousands of real app/web screens and complete user journeys. Use it for **structure and interaction patterns** (onboarding, checkout, pricing, settings, empty states, navigation), not for visual style.

Tools (when connected): `search_screens`, `search_flows`, `search_sections`, plus `create_collection` / `save_content` / `get_collection_contents` to curate. The `mobbin:search` and `mobbin:redesign-screen` skills are available if installed.

Workflow:
1. Search flows for the *journey* (e.g. "upgrade plan", "invite teammate"), sections for page blocks (e.g. "pricing table", "feature bento").
2. Note step count, where friction is removed, what states appear (empty/error/success), and microcopy.
3. Save a small collection when the work spans sessions.
4. Adapt the pattern to this product's content; never replicate a company's trademarked visuals.

## 21st.dev (components, themes, templates)

Marketplace of components, themes and templates, with CLI and MCP. Use it to find and *inspect* component source. Treat anything you install as owned code.

CLI (searching is free; `get` is free on paid plans and metered on the free tier):

```bash
21st search "hero section"
21st search "pricing table" --type component --limit 5 --free
21st search "dark dashboard" --type theme
21st search "saas starter" --type template --context auto   # grounds ranking in project Design Context
21st get <id>            # component code + demo
21st theme <id>          # theme CSS
21st add <user>/<slug>            # installs via shadcn registry (npx shadcn@latest add)
21st add <user>/<slug> --print    # show the command only
21st logo "next js" --limit 5     # brand/UI SVG logos (free)
21st bookmark <id> --type component ; 21st lists ; 21st list-new "Dashboard inspo"
```

Every command accepts `--json`. Docs index: `https://help.21st.dev/llms.txt`. Related installed skills: `21st-ui-explore` (compare directions), `21st-ui-build`, `21st-ui-review`, `21st-registry`, `21st-cli-use`, `21st-design-sync`.

Before adopting any component:
- Read its source: dependencies, license, hard-coded colors/sizes, motion, a11y (focus, roles, reduced motion).
- Re-theme to project tokens. Remove unused effects. Check mobile and keyboard.
- Record provenance (id/author) in a comment or notes so updates are deliberate.
- Prefer functionality (a stable table, a recoverable form) over another animated background.

## Higgsfield (image and video generation) — announce-and-confirm protocol

Generation costs credits and the output is public-facing content. **Never call a generation tool silently.** Before any generation call:

1. **State the purpose** in one or two sentences: what asset, where it will be used in the design, why a generated asset is needed (no real photography/footage available), and the intended model/settings (type, aspect ratio, duration, resolution).
2. **Give an estimated cost.** Look it up rather than guess: check the balance and model/plan info with the connector's read-only tools (e.g. `balance`, `models_explore`, `show_plans_and_credits`, or the `models_get` of the Higgsfield connector) and present "about N credits (balance M)". If you cannot determine a price, say that plainly and give a range or state it is unknown.
3. **Wait for an explicit yes** from the user in chat. A yes covers that specific asset (or batch), not later ones.
4. After generation, show the result, note any visible flaws (text artifacts, hands, brand-likeness, logos), and ask before regenerating (another charge).

Rules of use:
- Real assets first. Generate only for backgrounds, atmosphere, product-world imagery, or loops that cannot be sourced. Don't generate fake people as testimonials, fake logos, or fake screenshots of the product.
- Keep prompts specific to the chosen world (material, lighting, lens, palette tokens). Match aspect ratio to the layout; plan poster frames and file sizes (hero image ≤ ~200 KB AVIF, video ≤ ~2 MB loop).
- Convert deliverables: AVIF/WebP for stills; muted, `playsinline`, poster, AV1/H.265 for video.
- If the Higgsfield connector requires auth in this session, tell the user to authorize it via `/mcp` and proceed with non-generated assets or placeholders meanwhile.

## Lenis (smooth scroll)

Lightweight (~4 KB) smooth-scroll normalization that keeps native `position: sticky`, anchors and accessibility intact. Package: `lenis` (older `@studio-freight/lenis` is legacy). Locomotive Scroll v5 is built on it. GSAP's ScrollSmoother is the all-GSAP alternative; do not use both.

Adopt only if smooth scroll improves *this* experience. Skip or disable for: dense apps/dashboards, content the user reads and scans, native WebViews with custom overscroll, and when `prefers-reduced-motion: reduce` is active. Known limit: native CSS scroll-snap is not compatible with Lenis smoothing; choose one.

Canonical wiring with GSAP (single clock, deterministic order):

```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import Lenis from 'lenis';
gsap.registerPlugin(ScrollTrigger);

const mm = gsap.matchMedia();
mm.add('(prefers-reduced-motion: no-preference)', () => {
  const lenis = new Lenis({ autoRaf: false, lerp: 0.08 });
  lenis.on('scroll', ScrollTrigger.update);
  const tick = (t) => lenis.raf(t * 1000);
  gsap.ticker.add(tick);
  gsap.ticker.lagSmoothing(0);
  return () => { gsap.ticker.remove(tick); lenis.destroy(); };
});
```

If WebGL is present, render inside the same ticker callback after Lenis updates. Call `ScrollTrigger.refresh()` after fonts and async media settle. Anchor links and in-page jumps: use `lenis.scrollTo()`; handle focus separately. In React, create/destroy inside `useGSAP`/`useEffect` with cleanup so route changes do not leak instances.

## Other useful repos and skills (evaluate, don't bulk-install)

From the field guide watchlist: shadcn/ui (source ownership, registries), Base UI (accessible unstyled primitives; shadcn default since Jul 2026), Radix, React Aria, Magic UI, Aceternity UI, Cult UI, Kokonut UI, Motion Primitives, tweakcn (theme editor), coss ui, UI UX Pro Max skill, Superdesign skill, React Bits (MIT + Commons Clause), Paper Shaders, Rive, Spline, Unicorn Studio. Details and status flags: `references/sources/field-guide.md` §7 and `tool-index.csv`.

Installed helper skills worth knowing: `frontend-design`, `design-review`, `design-html`, `design-consultation`, `design-dna`, `animatedwebs:*`, `gsap-*` (core, timeline, scrolltrigger, plugins, react, performance, utils), `hyperframes*` (HTML video), `figma:*`, `chrome-devtools-mcp:*` (perf/a11y/LCP debugging), `modern-web-guidance`. Use the GSAP skills for API correctness and this skill for taste and routing.

## A typical research pass (≈ 10 minutes)

1. Impeccable `init`/context → know the product.
2. Refero: 2–3 style systems near the target mood → token structure.
3. Mobbin: 1 flow + 1–2 section patterns for the hardest screen.
4. 21st: `search` for 2–3 candidate components (hero, pricing, nav) → `get` and read source.
5. Write a 6–10 line "design intent" note: world, palette, type pair, grid, signature motion, what was borrowed from where, what is deliberately different. Show it to the user if the direction is new; otherwise proceed.
