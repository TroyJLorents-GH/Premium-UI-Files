# Resource routing (Claude Code)

Discover skills from the active catalog first. On Troy's current Windows setup these are fallback locations, not portable guarantees:

- 21st-ui-build: `C:/Users/Troy/.claude/skills/21st-ui-build/SKILL.md`
- refero-design: `C:/Users/Troy/.agents/skills/refero-design/SKILL.md`
- impeccable: `C:/Users/Troy/.claude/skills/impeccable/SKILL.md`
- gsap-core, gsap-scrolltrigger, gsap-react, scroll-world: `C:/Users/Troy/.claude/skills/<name>/SKILL.md`

Read each selected skill before using its workflow. If a path moved, check the current skill catalog and bounded likely locations. Do not silently install or reconfigure integrations. State an unavailable dependency and use the following fallback when possible.

This file mirrors the Codex copy at `C:/Users/Troy/.codex/skills/hero-design/references/integrations.md`. Rules are the same; only tool names differ.

## 21st: saved taste, components, themes, templates

Prefer connected MCP tools (`21st` server: `list_bookmark_lists`, `get_bookmark_list`, `list_bookmarks`, `search`, `get_component`, `get_theme`, `get_usage`); use the installed `21st` CLI as a fallback. The MCP server disconnects often in this environment, so the CLI is the reliable path. Discover tool schemas and CLI help before assuming flags.

1. List bookmark lists (`list_bookmark_lists`, or `21st lists`); choose relevant lists by returned names, then open them with their real IDs (`get_bookmark_list`, or `21st list <listId>`). Inspect relevant saved items, including themes/templates where useful. Use `list_bookmarks` / `21st bookmarks` if there are no relevant lists. Do not invent collection names or modify bookmarks just to research.

   Last seen 2026-09-23, for orientation only (always re-list; IDs can change): Hero (49), Scroll Effect (10), BG-Patterns (10), Marquees (11), Images (5), Carousel (3), Text (2), Menu Bar (3), Lists/Grids (3), portfolio (7).

2. Search the actual section and product need. The user's example CLI searches are:

   ```sh
   21st search "hero section"
   21st search "pricing table" --type component --limit 5
   21st search "dark dashboard" --type theme
   21st search "saas starter" --type template
   ```

   Adapt queries to the brief; do not search pricing or dashboards for an unrelated hero. Add `--context auto` where supported by the installed CLI and 21st-ui-build. `--liked` restricts to items Troy hearted.
3. Search returns metadata. Retrieve chosen component code with `get_component` / `21st get <id>`; themes use `get_theme` / `21st theme <id>`. Templates may provide only a listing URL and price, not downloadable code. Inspect previews and actual source/demo before adoption. A relevant saved item can supply the implementation; catalog search need not displace it.
4. Preserve source provenance and note which structure, motion, or primitive is reused. A library result is a starting point, not authority to override the user's composition rule.
5. Check `get_usage` or `21st usage` before hosted AI generation. Paid component retrieval does not imply hosted AI entitlement, remaining credits, or authority for extra purchases. If AI is disabled or unknown, use search/retrieval and implement locally. Do not repeatedly call an unavailable generation endpoint.

   Last seen 2026-09-23: tier paid, unlimited search and retrieval, **21st AI generation not enabled**. Re-check before assuming it changed.

If list access is unavailable but search works, explain that limit and proceed. If all 21st access fails, use real project primitives and other available references, and say the requested 21st research could not be completed.

## Mobbin: real section and UI examples

In Claude Code, Mobbin is a claude.ai connector: `mcp__claude_ai_Mobbin__search_sections`, `search_screens`, `search_flows`. These are often deferred; load their schemas with ToolSearch (`select:mcp__claude_ai_Mobbin__search_sections,...`) before calling.

For website heroes, prefer section search. Translate broad requests into concrete visible content, for example:

- "Technology company hero with a central product visualization and integrated headline."
- "Business website hero with full-width photography and overlaid navigation."

Use concise task intent consistently across searches and inspect returned images. Cite the stable Mobbin page link. For scroll effects, look for a playable/live source when available: a still image cannot establish animation, scroll behavior, or timing. Report that limit rather than inventing behavior.

## Refero: visual language and pattern evidence

Use the `refero-design` skill even if live MCP is absent, drawing on the bundled references and user-provided sources as directed. Live tools in Claude Code (`refero` server, user scope): `refero_search_styles`, `refero_get_style`, `refero_search_screens`, `refero_get_similar_screens`, `refero_search_flows`, `refero_get_flow`, `refero_get_screen_image`. Route styles to visual direction, screens to concrete UI patterns, and flows to multi-step behavior. Retrieve strong results and preserve source roles; do not combine every reference into a bland average.

## Impeccable: context, execution, evaluation

Use its installed launcher and current playbooks, not remembered subcommands. Load context once in the target project (on Windows without `sh`, use `scripts/impeccable.cmd`). For a new surface follow its new-work routing; for critique or scoped refinement load only the relevant playbook. Read its craft floor immediately before UI edits. Reuse confirmed product information and existing workflow defaults. The `impeccable-*` agents (finish-reviewer, asset-producer, documenter) are available for its finish handoffs.

## Image generation and Superdesign

Discover capabilities at use time. Claude Code options, in order of preference:

- **Higgsfield** (claude.ai connector or local `higgsfield` MCP): `generate_image`, `generate_image_batch`; call `models_explore` with action `recommend` when unsure which model fits. Also `upscale_image`, `outpaint_image`, `remove_background`.
- **ElevenLabs** `creative_generate_image` / `creative_edit_image` (flow-based; poll `creative_get_flow_run_status`).
- **Canva** `generate-image` for marketing-style graphics.
- Logos: `/logo-fetcher` only. Never generate a brand logo.
- Background removal: Troy's own useknockout API (`https://useknockout--api.modal.run`, `POST /remove`, options as form fields) or Higgsfield `remove_background`.

Do not invent image-generation APIs or quietly switch to a separately billed API key. Higgsfield and ElevenLabs spend credits; state the plan before large batches.

Use generation when a comp, illustration, photographic concept, texture, or scene is needed. Art-direct the subject, material, lighting, palette, aspect ratio, focal point, text-safe space, and mobile crop. Actual UI screenshots and factual assets stay authentic. Track the asset's source and whether it is generated.

Use **Superdesign** (Claude Code plugin skill `superdesign`, driven by `npx @superdesign/cli`) for a focused composition or UI exploration grounded in the same direction contract. Load its skill and follow its environment preflight. Inspect its output and adapt it to the real framework and shared tokens; tool output is not automatically production-ready. If no callable Superdesign capability is available, say so and continue with 21st, references, and local implementation. Do not block all design work or claim Superdesign contributed.

## Verification tools

Render with Claude-in-Chrome (real browser session), Playwright MCP (headless, deterministic), or `/browse` (gstack daemon). Chrome DevTools MCP for Lighthouse, LCP, and performance traces when hero asset weight matters.
