# Design brief and motion spec templates

Fill the brackets. Supply references and authentic content where they exist. Keep the brief short enough to read before every pass.

## Brief

```text
Surface: [landing page | experiential site | SaaS app | dashboard | docs | commerce | component]
Surface class: [expressive (motion floor applies) | quiet (motion cap applies)]
Concept (expressive only): [verb → object: what the product does to what; the moment of change; the figure that shows it; the feeling in one word. Reskin test: would this page still work with another product's copy? If yes, no concept yet]
Hero construction (expressive only): [figure-dominant | typographic monument | stage and caption | scroll-opening | editorial masthead | interactive instrument | crossed split; never headline-beside-card]
Audience: [who, expertise, device floor, context]
Primary task: [what the visitor must be able to do within seconds]
Success: [observable outcomes: comprehension, completion, time, recovery]
Stack and constraints: [framework, package manager, installed animation libs, hosting, browsers]
Preserve: [working capabilities, factual claims, existing tokens or brand]
Direction (two sentences): [e.g. Dark, near-black with a single warm accent; editorial left-aligned type on a 12-column grid; glass only on the nav; motion quiet except one pinned product chapter.]
References: [2–3 Refero/Mobbin/URL references and what to take from each]
Avoid: [specific mismatches: e.g. gradient text, icon-card triplets, scroll-jacking, custom cursor]
Content: [real copy and media available? what is placeholder and marked as such?]
Named motion (expressive): [hero sequence: 3–6 actors by catalog name from signature-motion.md, order and offsets; set piece: which figure, how many chapters, pin length; micro-interactions: 3+ by name (CTA, nav, proof section)]
Motion cap (quiet): [one hero treatment, one nav idea, 2–3 micro-interactions, no pin]
Performance budget: [LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1; JS ≤300 KB mobile; hero media limits]
Accessibility: [WCAG 2.2 AA; reduced motion composition; keyboard paths for every effect]
Verification: [browser frames during the hero (0/300/700/1200 ms) and at 0/25/50/75/100% scroll plus set-piece 0/50/100%, at 1440×900 and 390×844; template check on the first viewport; scrollWidth === innerWidth at 390; clipped/colliding text; dead space in cards; then audit script and the perf/a11y protocol]
```

## Motion spec (per animation)

```text
Element: [what moves]
Communicates: [why it moves: origin, relationship, feedback, hierarchy]
Trigger: [load | scroll (range) | hover | press | state change | route]
Primary actor / secondary follower / static anchor: [...]
Timing: [duration + ease] or [spring: visualDuration, bounce] ; stagger [ms, from]
Properties and owner: [transform/opacity only; CSS | GSAP | Motion; nothing else writes them]
Interruption: [retarget from current position/velocity; reverse on cancel; repeated activation]
Cleanup: [revert/kill/dispose on unmount or route change]
Reduced motion: [what remains: fade only / instant state / static frame]
Cost: [layers promoted, blur area, DPR cap, when paused]
```

## Six-layer prompt for a motion or 3D component

```text
1. CONTEXT & MEDIUM: [e.g. Next 16 + GSAP 3.15 ScrollTrigger; or Three r18x WebGPURenderer + R3F; or CSS only]
2. SPATIAL & CAMERA SPEC: [projection, focal length, start → end positions, target]
3. ACTOR HIERARCHY: [primary motion; secondary reaction + delay; static anchors]
4. TIMING & PHYSICS: [durations, stagger, eases or spring params, scrub buffer]
5. PERFORMANCE BUDGET: [draw calls, DPR cap Math.min(dpr, 2), asset sizes, cleanup via gsap.context()/dispose()]
6. A11Y & REDUCED MOTION: [behavior under prefers-reduced-motion; keyboard path; text stays in DOM]
```

## Review output template

```text
Direction check: [does the page have one direction? where does it leak?]
Concept and motion check (expressive): [does the first viewport read as a template? is the figure the product's own? does the page read as static in captured frames? is there a set piece?]
Top findings by user impact:
1. [task completion / recovery] — [finding] — [fix]
2. [accessibility / performance] — [finding] — [fix]
3. [visual craft / motion] — [finding] — [fix]
Anti-slop tells present: [list or none]
Verified: [what was actually tested, on what, with what]
Not verified: [what remains]
```
