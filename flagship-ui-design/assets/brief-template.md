# Design brief (fill before building)

Copy, fill the brackets, and keep it next to the work. Supply references and authentic content wherever available. Sections marked ◆ change the architecture; ask only if they are genuinely ambiguous.

## 1. Surface and mode
- Surface: [landing / pricing / portfolio / SaaS app / dashboard / docs / component] for [audience]
- Mode: [Persuade / Experience / Operate / Read]
- Primary task the visitor must complete: [one sentence]
- Success means: [observable outcomes: comprehension in 5 s, CTA click, task completion, INP, support tickets]

## 2. Constraints and preservation
- Stack and versions: [framework, styling, primitives, package manager; existing PRODUCT.md / DESIGN.md / tokens]
- Preserve these working capabilities and factual claims: [list]
- Avoid these mismatches: [examples of what would be wrong for this brand/audience]
- Hardware floor ◆: [mid-range phone on 4G / desktop only / kiosk] · Budgets: LCP [≤2.5 s], INP [≤200 ms], CLS [≤0.1], JS [≤300 KB], hero media [≤200 KB img / ≤2 MB video / ≤3 MB 3D]

## 3. Visual world
- One-line world: ["midnight hardware gallery", "research notebook at noon"]
- Direction (pick one): [dark glow / Swiss editorial / liquid glass / bento / dither-pixel / neo-brutalist / mono + accent / grain-mesh]
- Reference DESIGN.md (Refero Styles, by density and tone, never by brand): [link] — what we borrow: [token logic, measure, surface rules]; what we must not copy: [brand assets, look-alike layout]
- Type pairing: display [face] · text [face] · mono [face]; fluid scale [Utopia settings]
- Color roles (OKLCH): bg / bg-elevated / fg / fg-muted / border / accent / accent-fg / status
- Materials allowed: [glass only on nav; layered tinted shadows; grain 3%]
- Icon family: [Lucide / Phosphor / Material Symbols]

## 4. Content and evidence
- Real copy source: [doc/CMS]; what the user must supply: [list]
- Proof: [customers, numbers with sources, demos]
- Media: [product screenshots / renders / video; or generation plan with Higgsfield (purpose, model, count, estimated cost, approval)]

## 5. Motion spec
- Signature hero motion (exactly one): [what it communicates]
- Navigation idea (one): [e.g., hide-on-scroll glass bar with layoutId indicator]
- Micro-interactions (two or three): [press 0.97/100 ms; hover lift; inline validation check]
- Primary Actor / Secondary Follower (+delay) / Static Anchor per beat: [list]
- Timing and physics: durations, eases, springs, staggers, scrub buffer: [values from motion-numbers]
- Property ownership and ticker: [CSS vs GSAP vs Motion; single `gsap.ticker` with Lenis `autoRaf: false`]
- Interruption behavior: [rapid repeat, reverse, route change, resize]
- Reduced-motion composition: [what remains: crossfades ≤150 ms, instant states, native flow]

## 6. Delivery medium ◆ (3D/scroll stories only)
- [real-time WebGL/WebGPU · scrubbed canvas sequence · 2.5D depth shader · native CSS/SVG]
- Camera freedom ◆: [free orbit (live .glb) / fixed path (sequence or baked track)]
- Asset starting point ◆: [model/CAD · flat image · procedural bpy]
- Pipeline: Blender passes [Combined, Z, Normal, AO, Cryptomatte, Empties] → gltf-transform / Sharp / FFmpeg → budgets [tris, draw calls, textures, bytes]

## 7. States and accessibility
- States to design: empty · loading (>300 ms) · error · success · offline · long content · permission · stale
- Keyboard path, focus order, names/roles, contrast targets, 24/44 px targets, dragging alternative, live regions
- Localization: [languages, RTL, +35% expansion]

## 8. Verification plan
- Audit: `python3 scripts/flagship_audit.py <path>`; Impeccable `critique` → `audit` (if installed); `21st review` (if installed)
- Browser: sizes [360 / 768 / 1280 / 1920], reduced-motion emulation, keyboard-only, 4× CPU throttle trace, 200% zoom, 320 px reflow, forced colors
- Devices: [mid-range Android, 120 Hz iPhone]
- Field: `web-vitals` attribution wired; rollback threshold

---

## 6-layer prompt for any generated motion/3D component

1. **Context & medium**: [stack + versions]
2. **Spatial & camera spec**: [projection, focal length, start → end, target]
3. **Actor hierarchy**: [Primary / Secondary + delay / Static Anchor]
4. **Timing & physics**: [durations, staggers, eases/springs, scrub]
5. **Performance budget**: [draw calls, DPR cap, texture size, cleanup]
6. **A11y & reduced motion**: [exact fallback behavior, keyboard path, static state]
