# Workflow detail

## Contents
- Brief template
- Picking a direction
- Impeccable command sequence
- Hierarchy of attention (per viewport)
- 6-layer motion prompt (for specifying motion precisely)
- Iteration discipline

## Brief

Fill this (state assumptions for blanks; do not interrogate the user):

```
Surface: [landing | marketing site | app UI | dashboard | docs | portfolio | component]
Mode: [Persuade | Operate | Read | Experience]
Audience & primary task: [who, and the one action that defines success]
Success looks like: [observable outcomes, e.g. "visitor reaches pricing in <10s"]
Product truth: [what it actually does; claims that are factual and must be preserved]
Brand / constraints: [fonts, colors, tone, legal, existing design system]
Stack & delivery: [framework, hosting, browsers, min device]
References: [links, screenshots, Refero/Mobbin pulls, 21st components]
Anti-references: [what it must not look like]
Motion budget: [none | subtle | signature-moment | cinematic] and device floor
Content: [real copy/assets available vs placeholders needed]
Accessibility & perf bar: [WCAG 2.2 AA; LCP/INP/CLS targets]
```

## Picking a direction

Name the *world* the interface lives in, in one sentence, before choosing any visual. Good worlds have material and constraint: "a printed engineering manual from 1974 rendered on a CRT", "a quiet jewelry counter at night", "a race-engineer's telemetry wall". Bad worlds are adjectives: "modern, clean, sleek".

Then derive: palette (from the material), type (from the era/voice), layout grid (from the artifact), motion character (heavy/precise/airy) and imagery (what would exist in that world).

If the user gave nothing, offer 2–3 directions as one-liners with a tiny palette + type pairing each, recommend one, and proceed with it unless they redirect.

## Impeccable command sequence

Impeccable is the development-time design engine. Names should be confirmed against the installed version (`impeccable` skill's command table). Typical flow:

1. `init` — capture durable product context into PRODUCT.md (once per project).
2. `shape [feature]` — plan UX/UI before code (new surfaces).
3. Build (this skill's phases 3–5).
4. `critique [target]` — heuristic design review; `audit [target]` — a11y/perf/responsive.
5. Targeted refinements as findings dictate: `typeset`, `layout`, `colorize`, `animate`, `bolder` / `quieter`, `distill`, `adapt`, `clarify`, `harden`, `optimize`.
6. `polish [target]` — final pass. `document` — record DESIGN.md from the shipped build.

Rules: use **one lead design workflow per pass**. Competing design skills (Impeccable, ui-ux-pro-max, superdesign, frontend-design) can contradict each other; pick one as lead and use others for reference only. Impeccable's live mode can launch local agents with elevated flags; read its permission notes and ask the user before enabling live editing.

## Hierarchy of attention (define for every key viewport and animation beat)

- **Primary actor:** the single dominant element or movement.
- **Secondary follower:** subordinate reaction, delayed 60–120 ms, starting as the primary begins to decelerate.
- **Static anchor:** unmoving structure (grid hairlines, pinned headers, nav) that gives the eye a reference.

The eye tracks one focal vector at a time. If a beat has two primary actors, sequence them: **Move → Settle → Annotate**. Complete ~75% of a camera/scroll move before drawing callouts or revealing copy. Once body text has revealed (<0.8 s), keep it perfectly still while it is being read.

## 6-layer motion spec (use when describing or prompting for motion)

1. Context & medium (library + versions, DOM/WebGL/canvas sequence)
2. Spatial & camera (projection, FOV change, start→end, target)
3. Actor hierarchy (primary, secondary + delay, static anchors)
4. Timing & physics (seconds, stagger, easing/spring, scrub buffer)
5. Performance budget (draw calls, DPR cap `min(dpr, 2)`, cleanup)
6. A11y & reduced motion (what replaces spatial motion)

Replace vague words with measurable ones:

| Vague | Precise |
|---|---|
| "fade in smoothly" | masked line reveal: `yPercent 110→0`, 0.85 s, `expo.out`, 0.025 s stagger |
| "zoom in" | dolly along Z while narrowing FOV 50°→24°, target lerps to bbox center |
| "animate on scroll" | pin 300vh, `scrub: 0.6` bound to a paused timeline |
| "dramatic lighting" | warm rim light for silhouette, cool soft key at 45°, low fill, baked AO |
| "move pieces apart" | axial explosion along normalized vectors from origin, 0.04 s stagger outside→in |

## Iteration discipline

Verification is a bounded pass: build fully, inspect once with a batched round (desktop + mobile), fix everything found in one batch, confirm with at most one more round, stop. Open-ended self-QA burns time and cost and is done better by a final review pass. Ask the user for taste decisions rather than looping on them.
