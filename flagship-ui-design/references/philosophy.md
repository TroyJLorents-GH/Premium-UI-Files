# Philosophy: taste, physics, and the lexicon

Most bad motion design is not weak code; it is undisciplined creative direction. In software, a state change is instantaneous (`isOpen = true`). In motion design, **the transition is the information**: it tells the user how heavy a thing is, what it is made of, how parts relate in space, and where to look next. The barrier is no longer technical execution. The barrier is taste.

## The three laws

**1. Tactile friction: nothing moves for free.** Objects have mass. They resist, accelerate hard, then settle with micro-damping. Never use stock `ease-in-out` for UI or camera motion. Use aggressive deceleration (`cubic-bezier(0.16, 1, 0.3, 1)`, `expo.out`, `power4.out`) so ~80% of travel happens in the first ~25% of duration and the remainder is spent settling. Use springs (defined by perceptual duration + bounce, carrying input velocity) wherever a gesture or interruption is possible.

**2. Directed attention: choreography over chaos.** At any millisecond there is one **Primary Actor** (the thing that moves), one **Secondary Follower** (reacts 60–120 ms later: a callout line drawing, a label sliding in), and a **Static Anchor** (grid hairlines, pinned headline, persistent nav) that gives the eye a reference. Without an anchor, camera movement feels like the whole page is sliding. Sequence beats as **Move → Settle → Annotate**: complete ~75% of the camera/layout move before the annotation starts.

**3. The frame budget is the luxury.** 16.7 ms at 60 Hz, 8.3 ms at 120 Hz, 4.1 ms at 240 Hz for the *entire* pipeline (input → script → style → layout → paint → composite → GPU). A modest effect locked at the display rate beats a cinematic one that stutters. Fluidity is the premium; measure missed frames, not average FPS.

## The principle of restraint

Restraint wins when:
- **The user is reading or comparing.** Never animate text opacity or position while they read. Once text reveals (≤ 0.8 s), lock it down.
- **The subject is already complex.** A 300-part mechanical breakdown needs razor-sharp, quiet UI. Particles, chromatic aberration, and bouncing buttons cheapen precision.
- **Scroll fatigue sets in.** Not every section should pin the viewport for 4000 px. Alternate "pinned spectacle" chapters with normal-flow reading chapters so the user feels in control.
- **The action is frequent.** Toggles used 100× a day get near-zero motion. Keyboard-triggered actions get faster, simpler motion than pointer-triggered ones.
- **It is an exit.** Users do not watch exits. Fade + slight scale, faster than the entrance.

Pick **one hero effect, one navigation idea, two or three micro-interactions** per page.

## Typography as architecture

In 3D or motion-heavy pages, type is the bridge between the viewport glass and the scene behind it. Either lock display type rigidly to a 2D Swiss grid to ground the scene, or sandwich the subject in Z-space (large background title behind the mesh, crisp technical telemetry in front) for optical depth without shaders. Keep meaningful text as real DOM text: selectable, searchable, translatable, announced correctly.

## Lighting and material contrast

Beginners flood scenes with ambient light so "everything is visible"; that destroys depth. Establish the **rim/back light first** to carve silhouette, then a softer **key light** at 30–45° to reveal surface normals, then a subtle **fill** so shadows keep texture. The same logic applies to 2D: surfaces need a light direction (1 px top highlight, tinted layered shadows, grain) or they read as flat vector.

## The Golden Sequence (scroll-driven product story)

- **0–20% Silhouette & hook**: high-contrast rim light, minimal UI, establish scale.
- **20–50% Deconstruction**: camera dollies in while layers separate along local axes; SVG line-art draws in to bridge art and engineering.
- **50–80% Micro-inspection**: telephoto focal shift (85–135 mm equivalent), material detail, staggered masked data readouts.
- **80–100% Reassembly & resolution**: parts snap back with high-velocity springs; camera settles into a heroic 3/4 or orthographic lockup.

## The lexicon: words that command precision

Vague adjectives produce generic code. Specify in mathematical, optical, and choreographic terms.

| Vague | Specify instead |
|---|---|
| "smooth scroll" | Sub-pixel inertial damping via rAF interpolation (`lerp ≈ 0.08–0.1`), single ticker, native scrollbar preserved |
| "fade in the text" | Overflow-masked line/word split reveal, `yPercent: 110 → 0`, `rotateZ: 2° → 0`, 0.03 s stagger, 0.85 s, `expo.out` |
| "connect it to scroll" | Pin the container for `+=300%`, bind normalized progress 0–1 to a paused master timeline with `scrub: 0.6` catch-up |
| "move pieces apart" | Procedural axial explosion along normalized vectors from the assembly origin, 0.04 s stagger from housing inward |
| "zoom in on the part" | Dolly along local Z while narrowing vertical FOV 50° → 24°, interpolating the controls target to the part's bounding-box center |
| "technical view" | Interpolate projection from perspective (35 mm) to orthographic (`frustumSize: 4`) so callouts align to a 2D grid |
| "cool lighting" | Three-point studio: warm grazing rim at 135° azimuth, cool soft area key at 45°, anisotropic clearcoat with baked contact AO |
| "make it feel premium" | Name the surface mode, the visual world, the type pairing, the one signature motion, and the budgets |
| "modern / clean" | Banned. Replace with a token system, a type scale, and a reference DESIGN.md |

## The 6-layer prompt (for any motion or 3D component)

1. **Context & medium**: stack and versions (e.g., Three.js r18x + GSAP 3.1x ScrollTrigger, or CSS scroll-driven only).
2. **Spatial & camera spec**: projection, focal length, initial → final coordinates, target vector.
3. **Actor hierarchy**: Primary Actor, Secondary Follower (+ delay), Static Anchor.
4. **Timing & physics**: durations, staggers, exact eases or spring params, scrub buffer.
5. **Performance budget**: draw calls, DPR cap, texture size, cleanup via `gsap.context()` / dispose.
6. **A11y & reduced motion**: exact behavior under `prefers-reduced-motion: reduce`, keyboard path, static fallback.

## Seven failure modes to diagnose on sight

1. **Dual-ticker jitter**: vibration during fast scroll at 120 fps → competing rAF loops. Fix: `new Lenis({ autoRaf: false })`, one `gsap.ticker.add()`.
2. **VRAM leaks in SPAs**: tab crashes after 4–5 navigations → orphaned ScrollTriggers, undisposed geometries/textures. Fix: `gsap.context()`/`useGSAP()`, `dispose()` on unmount.
3. **Layout-property animation**: purple layout bars in DevTools → animating `top/left/width/height/blur` on scroll. Fix: transforms, opacity, or Flip.
4. **Kinetic overload**: site looks expensive, users remember nothing → camera + explosion + lines + text all at the same scroll %. Fix: Move → Settle → Annotate.
5. **Uncapped DPR**: phones throttle to 30 fps in 20 s. Fix: `Math.min(devicePixelRatio, 2)` (1.5 during scroll).
6. **Pin drift**: pinned sections overlap the footer → lazy media/fonts changed document height after measurement. Fix: `aspect-ratio` on media, no `loading="lazy"` inside pinned sections, `ScrollTrigger.refresh()` after fonts/assets.
7. **Color mismatch between render and CSS**: the "same" red looks different → AgX/Filmic tone mapping vs sRGB CSS. Fix: Blender view transform Standard, or match `renderer.toneMapping` and render the background inside the canvas.
