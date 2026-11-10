If you want to build an AI skill—and a personal practice—that produces extraordinary 3D motion design and interactive web experiences, you must start with a hard truth: **most bad motion design is not caused by weak code; it is caused by undisciplined creative direction.**

As an experienced software developer, you already know how to manipulate state, manage event loops, and structure components. Moving into high-craft motion design requires shifting how you think about time and space. In standard software engineering, state transitions are instantaneous (`isOpen = true`). In motion design, **the transition *is* the information**. It tells the user how heavy an object is, what it is made of, how parts relate to one another in space, and where their eyes should look next.

What follows is the complete architectural and creative blueprint for mastering this craft and encoding it into a reusable, production-grade AI skill.

---

## Foundational Principles vs. Advanced Techniques

Before writing a skill definition, you must separate the timeless fundamentals of visual direction from the advanced technical tricks that execute them. An AI agent (or human designer) that skips the foundations will only generate high-frame-rate chaos.

### Part A: Essential Foundations (Creative Direction & Physics)

1. **Hierarchy of Attention (Primary, Secondary, Anchor):**
   The human eye can only track one primary focal vector at a time. At any given frame of an animation, your composition must have:
   * **The Primary Actor:** The single dominant movement (e.g., a 3D mechanical assembly rotating 45 degrees).
   * **The Secondary Follower:** A subordinate element that reacts with a slight temporal offset (`60ms–120ms` delay), such as an SVG callout line drawing out from a bolt.
   * **The Static Anchor:** Unmoving structural elements (grid hairlines, pinned section headers, or persistent navigation) that give the eye a spatial reference point. Without a static anchor, camera movement feels like the entire webpage is sliding around uncomfortably.

2. **Tactile Physics & Easing Discipline:**
   Physical objects possess mass and inertia; they cannot change velocity instantaneously.
   * **Initiation vs. Settlement:** When an element enters or responds to user input, it should overcome static friction quickly and spend most of its duration decelerating into rest. An aggressive out-ease such as `cubic-bezier(0.16, 1, 0.3, 1)` (or GSAP’s `expo.out` / `power4.out`) front-loads 80% of the spatial travel into the first 25% of the duration, creating both responsiveness and luxury.
   * **Linear Motion (`none`):** Use linear interpolation *only* for continuous constant-velocity loops (like a spinning cooling fan) or timelines directly scrubbed by a smooth-scroll container that already applies inertial damping.

3. **Typography as Architecture:**
   In 3D web experiences, typography is the bridge between the viewport glass and the 3D void behind it. High-contrast display typography should either lock rigidly to a 2D Swiss grid to ground the 3D scene, or sandwich the 3D subject in Z-space (large background title behind the 3D mesh, crisp technical telemetry in front of it) to create immediate optical depth without heavy shaders.

4. **Lighting & Material Contrast (Silhouette First):**
   Beginners flood 3D scenes with uniform ambient light so "everything is visible." That destroys depth. Great 3D rendering relies on **chiaroscuro**—the ratio of light to shadow. Always establish a strong **Rim/Back Light** first to carve the object's silhouette out from the background, a softer **Key Light** at a 30–45° angle to reveal surface normal detail, and a subtle **Fill/Bounce Light** so shadow areas retain texture without turning to muddy gray.

5. **The Principle of Restraint (When Less Beats More):**
   Restraint produces a superior result whenever:
   * **The user is trying to read or compare data:** Never animate text opacity or horizontal position while the user is actively trying to read a paragraph. Once text reveals, lock it down.
   * **The 3D subject is already complex:** If you are showcasing a 300-part mechanical assembly, your UI transitions should be razor-sharp, minimal, and quiet. Competing particle effects, chromatic aberration, and bouncing buttons cheapen precision engineering.
   * **Scroll fatigue sets in:** Not every section of a webpage should pin the viewport and hijack scroll for 4,000 pixels. Alternate high-intensity "pinned spectacle" chapters with normal-flow reading chapters so the user feels in control of their journey.

### Part B: Advanced Techniques (Execution & Pipeline Alchemy)

1. **3D-to-2D Spatial Projection Bridging:**
   Instead of rendering text inside WebGL/WebGPU (which looks blurry, breaks screen readers, and cannot be translated by browsers), place invisible `Empty` anchor nodes on your 3D model in Blender. In the browser, project each anchor's 3D world position into 2D Normalized Device Coordinates (`vector.project(camera)`) on every frame, and position crisp HTML/SVG overlays via CSS `transform: translate3d(x, y, 0)`.
2. **Baked Lighting & MatCap Shaders over Real-Time Raytracing:**
   Instead of forcing a mobile GPU to calculate 4 dynamic shadow-casting lights at 60fps, bake cycles ambient occlusion and lightmaps directly into textures in Blender, or use custom **MatCap (Material Capture)** spherical environment lookups in Three.js. You get studio-grade reflections at near-zero GPU cost.
3. **Render-Pass Compositing (Z-Depth, Normals, Cryptomatte):**
   Exporting auxiliary data passes from Blender lets you fake 3D depth on 2D images. A 150KB beauty image paired with a 50KB grayscale Z-Depth map inside a simple fragment shader creates realistic cursor-driven parallax at 240fps without loading a single polygon.

---

## The Actionable AI Skill Blueprint

### 1. Purpose, Scope, and Activation Triggers

* **Purpose:** To guide an AI engineering/design assistant in architecting, scripting, and auditing production-ready 3D motion graphics, Blender-to-web asset pipelines, and choreographed scroll/interactive web experiences that run at 60–240fps across devices while honoring accessibility standards.
* **Scope:**
  * *In Scope:* Creative direction, storyboard pacing, Blender Python (`bpy`) procedural modeling/animation/rendering scripts, glTF/GLB optimization pipelines, Three.js (WebGL2 & WebGPU/TSL) scene architecture, GSAP choreography (`ScrollTrigger`, `Flip`, `SplitText`, `DrawSVG`), native CSS Scroll-Driven Animations & View Transitions, SVG vector motion, and performance/accessibility QA.
  * *Out of Scope:* Character rigging for long-form narrative film, fluid/smoke vfx caches meant purely for offline cinema servers, or unrequested framework migrations.
* **Activation Triggers:** Activate this skill whenever a prompt requests:
  * "Scroll-driven storytelling," "product breakdown/exploded view," "interactive 3D hero," or "scrollytelling."
  * Integration between **Blender**, **Three.js / React Three Fiber**, **GSAP**, **Lenis**, or **SVG callout animations**.
  * Polishing an existing UI/3D prototype that feels "flat," "janky," "disconnected," or "robotic."

---

### 2. Required Inputs and Clarifying Questions

Before generating code or 3D scripts, the skill must evaluate four variables. **Rule:** *Only ask clarifying questions if missing information would fundamentally change the rendering architecture. Otherwise, state reasonable production assumptions and proceed.*

#### The 4 Material Clarifying Questions (Ask Only When Ambiguous):
1. **Delivery Medium:** Is the final output a **real-time interactive web experience** (DOM/WebGL/Canvas), a **pre-rendered video/motion reel** (MP4/ProRes), or a **hybrid** (pre-rendered image sequence scrubbed on a webpage)?
2. **Interaction Freedom vs. Visual Fidelity:** Does the user need to freely rotate/inspect the 3D object from any angle (requires live `.glb` in Three.js), or does the camera follow a single art-directed path on scroll (often better served by a pre-rendered WebP/AVIF `<canvas>` sequence or baked keyframe track)?
3. **Target Hardware Floor:** Must this run smoothly on mid-range mobile phones over cellular networks (strict `< 5MB` initial asset budget, capped pixel ratio), or is it for a controlled desktop/kiosk environment?
4. **Asset Starting Point:** Do we have an existing 3D model/CAD file, a flat 2D reference image, or are we generating geometry procedurally via Blender Python (`bpy`)?

---

### 3. Tool-Selection Framework (Verified Licensing & Job-Fit)

Choosing the right tool means matching the rendering medium to the physics of the job—and understanding the legal and maintenance realities of your stack.

| Tool / Technology | License Category & Verified Status | What It Excels At (When to Use) | When NOT to Use It |
| :--- | :--- | :--- | :--- |
| **Blender (5.2 LTS / 4.5 LTS)** | **Free & Open Source (FOSS)**<br>GNU GPL v2/v3 (Cycles engine is Apache 2.0). Outputs (renders, `.glb` files) are 100% yours for commercial use. *Note:* Distributed Python add-ons using `bpy` must be GPL-compatible. | Modeling, procedural Geometry Nodes, PBR/anisotropic shading, baking lightmaps, freestyle SVG line-art exports, and rendering raytraced image sequences. | Do not export raw, un-decimated Blender meshes with procedural node trees directly to Three.js (procedural shader nodes do not translate to glTF without baking). |
| **Three.js (r186+)** | **Free & Open Source (FOSS)**<br>MIT License. Actively maintained monthly. Includes `WebGPURenderer` with automatic WebGL 2 fallback and **TSL** (Three.js Shading Language). | Real-time interactive 3D in the browser, dynamic camera projections, custom post-processing, and cursor-reactive shaders. | Do not use for static 2D layouts or scenes with 500+ transparent refractive glass parts that can be pre-rendered as a scrubbed 2D `<canvas>` sequence at 1/10th the GPU cost. |
| **GSAP (v3.13+)** | **Proprietary, 100% Free to Use (Commercial Included)**<br>Acquired by Webflow (Oct 2024); made 100% free in April 2025—including all former Club plugins (`SplitText`, `Flip`, `ScrollTrigger`, `DrawSVG`, `MorphSVG`). *Caveat:* Standard GreenSock License is **not** OSI open-source (not GPL-compatible) and prohibits bundling GSAP into a competing visual no-code animation builder. | Complex multi-element timeline choreography, scroll pinning/scrubbing (`ScrollTrigger`), seamless DOM layout morphing (`Flip`), and accessible text splitting (`SplitText`). | Do not use for simple hover states or single-property scroll progress bars where native CSS transitions or CSS `animation-timeline: scroll()` suffice. |
| **Lenis (Darkroom Eng.)** | **Free & Open Source (FOSS)**<br>MIT License. Actively maintained (~4KB zero-dependency). | Normalizing trackpad and mouse-wheel scroll deltas into damped inertia while keeping native `position: sticky`, anchor links, and screen-reader scrolling intact. | Do not use inside native mobile WebViews that already enforce custom overscroll physics, or when `prefers-reduced-motion: reduce` is active. |
| **glTF-Transform** | **Free & Open Source (FOSS)**<br>MIT License (by Don McCurdy). Actively maintained CLI & JS SDK. | Compressing `.glb` files via **Meshopt/Draco**, converting textures to GPU-ready **KTX2**, welding vertices, and joining meshes to reduce draw calls. | Always use it before shipping any `.glb` to production; never skip this step. |
| **CSS Scroll-Driven Animations & View Transitions** | **Open Web Standards (W3C)**<br>Free native browser APIs. Supported across Chrome 115+, Edge 115+, Safari 26+, and recent Firefox (~85–88% global baseline support). | Off-main-thread (compositor) scroll progress bars, parallax reveals (`animation-timeline: scroll()` / `view()`), and zero-JS cross-document page morphs. | Do not use when you need complex sequential timeline scrubbing synchronized with WebGL/Three.js camera math or physics-based velocity callbacks. |
| **Theatre.js** | **Open Source (Mixed License)**<br>`@theatre/core` (runtime) is Apache-2.0; `@theatre/studio` (editor) is AGPL-3.0. *Maintenance Warning:* Public GitHub commits slowed significantly after 2024 while v1.0 development moved private. | Visual curve-editor keyframing of Three.js camera paths in the browser during development. | Avoid locking mission-critical enterprise architecture to it if long-term dependency freshness against monthly Three.js releases is required; exporting camera animations directly inside the `.glb` from Blender is more durable. |
| **FFmpeg & Sharp** | **Free & Open Source (FOSS)**<br>FFmpeg (LGPLv2.1+ / GPLv2+); Sharp (Apache-2.0). | Converting Blender PNG passes into `.webp`/`.avif` sequences or scrubbable intra-frame (`-g 1`) MP4/WebM videos. | N/A (Build-step pipeline tools). |

---

### 4. Step-by-Step Production Workflow

A world-class motion piece succeeds because every stage of the pipeline feeds clean data to the next:

```
[1. Storyboard & Budget] ──► [2. Blender Scene & Passes] ──► [3. CLI Compression Alchemy]
                                                                       │
[5. QA, A11y & Perf Audit] ◄── [4. Single-Ticker Web Sync (Lenis + GSAP + Three.js/Canvas)]
```

#### Step 1: Storyboard & Motion Budgeting
* Define the **Narrative Arc** (Hook $\rightarrow$ Deconstruction $\rightarrow$ Macro Inspection $\rightarrow$ Resolution).
* Set hard performance budgets before modeling:
  * **Real-Time WebGL Budget:** `< 150,000` triangles total on mobile (`< 500,000` desktop), `< 50` draw calls per frame, max texture resolution `2048x2048` compressed to KTX2, total compressed `.glb` payload `< 4MB`.
  * **Canvas Sequence Budget:** `90–150` frames at `1920x1080` (or `1440x1080`), encoded as `.webp` (`quality: 80`), total sequence payload `< 6MB` with progressive loading.

#### Step 2: Asset Creation, Lighting & Pass Export in Blender
* **Clean Hierarchy & Pivots:** Name every object semantically (`diffuser_strake_L`, `anchor_callout_exhaust`). Set each component's origin (`Object > Set Origin > Origin to Geometry`) along the exact axis it will slide or rotate along.
* **Empty Anchors for Web UI:** Place `Empty` objects (`Plain Axes`) at exact surface points where HTML/SVG callouts will attach.
* **Bake or Render Passes:**
  * *For Real-Time `.glb`:* Bake cycles lighting and Ambient Occlusion into UV Channel 2 textures so real-time shaders look grounded without expensive shadow maps.
  * *For Pre-Rendered Sequences / 2.5D:* Enable Render Passes in Blender (`View Layer Properties > Passes > Data`): **Combined (Beauty)**, **Z (Normalized via Map Range node in Compositor)**, **Normal**, **Ambient Occlusion**, and **Cryptomatte (Object/Material)** for instant isolation masks.
  * *For Vector Overlays:* Use a **Grease Pencil Line Art Modifier** on the collection and export camera-projected strokes as SVG, or dynamically project 3D anchors in Three.js.

#### Step 3: Asset Compression & Pipeline Alchemy (CLI)
Never load raw Blender outputs into a browser. Run automated CLI transforms:
* **For 3D Models (`.glb`):**
  ```bash
  # Weld vertices, simplify geometry, compress meshes with Meshopt, and convert textures to KTX2
  npx @gltf-transform/cli optimize raw_model.glb public/model_opt.glb --compress meshopt --texture-compress ktx2 --texture-size 2048
  ```
* **For Scrubbable Video (If using `<video>` instead of `<canvas>`):**
  Standard MP4s place keyframes every 2–5 seconds, causing severe lag when scrubbing backward on scroll. Encode with **every frame as an intra-frame keyframe (`-g 1`)**:
  ```bash
  ffmpeg -i render_%04d.png -c:v libx264 -crf 20 -pix_fmt yuv420p -g 1 -keyint_min 1 -movflags +faststart scrub_ready.mp4
  ```

#### Step 4: Web Integration & Single-Ticker Synchronization
* **The Golden Rule of Frame Pacing:** Never run independent `requestAnimationFrame` loops for Lenis, GSAP, and Three.js. When multiple loops fire asynchronously within a single 4.1ms (240Hz) or 16.6ms (60Hz) window, scroll positions and 3D camera matrices desynchronize, producing visual jitter.
* **Bind Everything to `gsap.ticker`:**
  ```javascript
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import Lenis from 'lenis';

  gsap.registerPlugin(ScrollTrigger);

  // 1. Initialize Lenis without its internal RAF loop
  const lenis = new Lenis({ autoRaf: false, lerp: 0.08 });
  lenis.on('scroll', ScrollTrigger.update);

  // 2. Drive Lenis, GSAP, and Three.js in strict deterministic order on one ticker
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000); // Step A: Update damped scroll position
    update3DCameraAndProjections(); // Step B: Sync 3D camera & 2D SVG callout anchors
    renderer.render(scene, camera); // Step C: Render WebGL/WebGPU frame
  });
  gsap.ticker.lagSmoothing(0);
  ```

#### Step 5: Accessibility, Mobile Fallbacks & QA
* Wrap all motion initialization inside `gsap.matchMedia()` so desktop vs. mobile viewports—and `prefers-reduced-motion`—are handled declaratively with automatic memory cleanup (`gsap.context`).

---

### 5. Precise Motion Vocabulary & Reusable Prompt Patterns

When prompting an AI or writing technical specifications, vague adjectives ("make it smooth," "add a cool 3D effect," "pop in the text") trigger generic, amateur code. Use exact mathematical, optical, and choreographic terminology.

#### The Lexicon Translation Table

| Domain | Amateur / Vague Phrase | Master Creative-Technologist Specification |
| :--- | :--- | :--- |
| **Camera & Optics** | "Zoom in on the part" | "Dolly camera along its local Z-axis while narrowing vertical FOV from `50°` to `24°` (telephoto compression), interpolating `controls.target` to the component's world-space bounding box center." |
| **Camera & Optics** | "Show a technical view" | "Cross-dissolve or interpolate camera projection matrix from Perspective (`35mm` focal length) to Orthographic projection (`frustumSize: 4`) to flatten perspective lines for 2D CAD callout alignment." |
| **Lighting & Shaders** | "Make the lighting dramatic" | "High-contrast 3-point studio setup: high-intensity warm grazing rim light (`135°` azimuth) to carve silhouette, cool soft area key light (`45°`), and anisotropic carbon-fiber clearcoat with baked contact AO." |
| **Choreography** | "Move the pieces apart" | "Procedural axial explosion: translate sub-meshes outward along their normalized vector from the assembly origin, staggered by `0.04s` from exterior housing inward to the core." |
| **Timing & Easing** | "Fade in the text smoothly" | "Overflow-masked line/character split reveal (`yPercent: 110` to `0`, `rotateZ: 2deg` to `0`), `0.025s` stagger, `0.85s` duration using `cubic-bezier(0.16, 1, 0.3, 1)` (`expo.out`)." |
| **Scroll Sync** | "Animate as the user scrolls" | "Pin the viewport container for `300vh` (`end: '+=300%'`) and bind normalized scroll progress (`0.0–1.0`) to a paused master timeline with a `0.6s` catch-up scrub buffer (`scrub: 0.6`)." |

#### Reusable Prompt Pattern (The 6-Layer Prompt Architecture)
Whenever prompting an AI to generate a motion component or Blender script, structure the prompt using these six explicit blocks:
```markdown
1. [CONTEXT & MEDIUM]: (e.g., Three.js r186 + GSAP 3.13 ScrollTrigger OR Blender 5.2 LTS Python bpy script)
2. [SPATIAL & CAMERA SPEC]: (Projection type, focal length, initial -> final coordinates, target vector)
3. [ACTOR HIERARCHY]: (Primary Actor motion, Secondary Follower motion + delay, Static Anchor elements)
4. [TIMING & PHYSICS]: (Exact durations in seconds, stagger intervals, cubic-bezier / GSAP ease curves, scrub buffer)
5. [PERFORMANCE BUDGET]: (Max draw calls, DPR cap `Math.min(window.devicePixelRatio, 2)`, cleanup via `gsap.context()`)
6. [A11Y & REDUCED MOTION]: (Behavior under `(prefers-reduced-motion: reduce)`—e.g., cross-fade static states instead of spatial camera travel)
```

---

### 6. Three Distinct Worked Examples

#### Example 1: Hybrid 3D Mechanical Deconstruction (Real-Time `.glb` + Projected SVG HUD)
* **Creative Brief:** An interactive engineering breakdown of a Formula 1 rear carbon diffuser and exhaust assembly. As the user scrolls through a pinned `350vh` section, the camera orbits from a low rear silhouette to an isometric 3/4 view, the outer carbon strakes slide outward to expose the internal titanium heat-shield, and crisp SVG vector callout lines draw out from specific bolts to display live material specifications.
* **Why This Approach:** Using a compressed `.glb` (`< 3MB`) allows dynamic 3D-to-2D coordinate projection so the HTML/SVG callouts remain razor-sharp at any screen resolution and accessible to screen readers.
* **Implementation Blueprint:**
  ```javascript
  // Core 3D-to-2D Projection & Scroll Choreography Pattern
  import * as THREE from 'three';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  import { DrawSVGPlugin } from 'gsap/DrawSVGPlugin';

  gsap.registerPlugin(ScrollTrigger, DrawSVGPlugin);

  export function initDiffuserBreakdown({ scene, camera, renderer, model, calloutDOMNodes }) {
    const mm = gsap.matchMedia();
    const tempVec = new THREE.Vector3();

    // Extract named sub-meshes and Empty anchor nodes authored in Blender
    const outerStrakeL = model.getObjectByName('diffuser_strake_L');
    const heatShield = model.getObjectByName('titanium_heat_shield');
    const anchorBolt = model.getObjectByName('anchor_exhaust_mount');

    // Project 3D Empty to 2D CSS coordinates every frame
    function syncCallouts() {
      if (!anchorBolt) return;
      anchorBolt.getWorldPosition(tempVec);
      tempVec.project(camera); // Converts to NDC (-1 to +1)

      const x = (tempVec.x * 0.5 + 0.5) * window.innerWidth;
      const y = (-(tempVec.y * 0.5) + 0.5) * window.innerHeight;

      // Move HTML/SVG callout wrapper via GPU-accelerated translate3d
      calloutDOMNodes.exhaustWrapper.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0)`;
    }

    mm.add(
      {
        isDesktop: '(min-width: 768px)',
        reduceMotion: '(prefers-reduced-motion: reduce)'
      },
      (context) => {
        const { reduceMotion } = context.conditions;

        const tl = gsap.timeline({
          scrollTrigger: {
            trigger: '#engineering-stage',
            start: 'top top',
            end: '+=300%',
            pin: true,
            scrub: reduceMotion ? false : 0.6,
            toggleActions: reduceMotion ? 'play none none reverse' : undefined
          }
        });

        if (reduceMotion) {
          // Accessible Fallback: Instant state toggle without dizzying camera orbit or axial slide
          tl.to('.callout-panel', { autoAlpha: 1, duration: 0.3 });
          return;
        }

        // Stage 1 (0% -> 45%): Camera orbit + focal shift
        tl.to(camera.position, { x: 2.4, y: 1.6, z: 3.2, ease: 'power2.inOut', duration: 1 }, 0)
          // Stage 2 (25% -> 75%): Axial explosion along local normals
          .to(outerStrakeL.position, { x: -0.65, ease: 'expo.out', duration: 0.8 }, 0.25)
          .to(heatShield.position, { y: 0.4, ease: 'expo.out', duration: 0.8 }, 0.32)
          // Stage 3 (65% -> 100%): Secondary SVG callout draw + telemetry reveal (Restraint: waits until camera slows!)
          .fromTo('#callout-line-path', { drawSVG: '0%' }, { drawSVG: '100%', ease: 'power3.out', duration: 0.35 }, 0.65)
          .fromTo('.telemetry-label', { yPercent: 100, autoAlpha: 0 }, { yPercent: 0, autoAlpha: 1, stagger: 0.05, ease: 'expo.out', duration: 0.3 }, 0.75);
      }
    );

    return { syncCallouts, cleanup: () => mm.revert() };
  }
  ```

---

#### Example 2: Editorial Typography & 2.5D Depth-Map Hero (Ultra-Light Mobile-First Performance)
* **Creative Brief:** A luxury industrial design studio landing page. Instead of forcing mobile users to download a 15MB 3D scene before seeing the hero section, use a 180KB studio beauty render exported from Blender alongside a 45KB grayscale Z-Depth pass. Combine subtle cursor/gyroscope depth parallax with architectural Swiss typography using GSAP `SplitText` (which includes built-in screen-reader accessibility and automatic overflow masking).
* **Why This Approach:** Loads in `< 0.4s` on 4G connections, runs at 120–240fps on integrated laptops and budget phones, and looks indistinguishable from a raytraced 3D viewport for restricted viewing angles.
* **Implementation Blueprint:**
  * **Fragment Shader Core (GLSL / TSL concept):**
    ```glsl
    // Sample depth map (white = near, black = far) and offset UV coordinates by damped mouse vector
    uniform sampler2D uBeautyMap;
    uniform sampler2D uDepthMap;
    uniform vec2 uPointer; // Damped (-1 to 1) via gsap.quickTo()
    uniform float uIntensity; // Keep subtle: 0.015 to 0.025 (Restraint prevents edge tearing!)
    varying vec2 vUv;

    void main() {
      float depth = texture2D(uDepthMap, vUv).r;
      // Shift foreground pixels opposite to background pixels around focal plane (0.5)
      vec2 parallaxOffset = uPointer * (depth - 0.5) * uIntensity;
      gl_FragColor = texture2D(uBeautyMap, vUv + parallaxOffset);
    }
    ```
  * **Accessible Masked Typography Choreography (GSAP 3.13+ `SplitText`):**
    ```javascript
    import gsap from 'gsap';
    import { SplitText } from 'gsap/SplitText';

    gsap.registerPlugin(SplitText);

    // SplitText v3.13+ automatically adds aria-label attributes for screen readers and supports native line masking
    const split = SplitText.create('.hero-headline', {
      type: 'lines,words',
      mask: 'lines', // Automatically wraps each line in an overflow: clip container
      linesClass: 'split-line'
    });

    gsap.from(split.words, {
      yPercent: 115,
      rotateZ: 1.5,
      duration: 1.1,
      stagger: 0.035,
      ease: 'expo.out',
      delay: 0.15
    });
    ```

---

#### Example 3: Tactile State-Driven Bento Grid to Fullscreen 3D Inspector (`GSAP Flip`)
* **Creative Brief:** A product specification grid where clicking any technical card seamlessly morphs the card’s DOM container into a full-screen interactive 3D viewport without a jarring page reload or layout jump, while surrounding bento cards smoothly reflow out of the way.
* **Why This Approach:** Standard CSS transitions cannot animate changes in DOM parent hierarchy or CSS Grid cell spans (`grid-column: span 1` $\rightarrow$ `position: fixed; inset: 0`). `GSAP Flip` (First, Last, Invert, Play) records the exact screen-space bounding boxes before and after the DOM state change and applies inverse hardware-accelerated transforms.
* **Implementation Blueprint:**
  ```javascript
  import gsap from 'gsap';
  import { Flip } from 'gsap/Flip';

  gsap.registerPlugin(Flip);

  function expandCardToInspector(selectedCard, allCards, inspectorContainer) {
    // 1. FIRST: Capture exact geometry of the card and surrounding grid siblings
    const state = Flip.getState([selectedCard, ...allCards], {
      props: 'borderRadius,backgroundColor'
    });

    // 2. LAST: Mutate the DOM immediately (move card into fixed fullscreen container)
    const isExpanding = !selectedCard.classList.contains('is-expanded');
    selectedCard.classList.toggle('is-expanded', isExpanding);
    inspectorContainer.appendChild(selectedCard);

    // 3. INVERT & PLAY: Let Flip calculate matrix deltas and animate with tactile deceleration
    Flip.from(state, {
      duration: 0.85,
      ease: 'expo.out',
      absolute: true, // Prevents layout thrashing during transition
      nested: true,
      stagger: 0.02,
      onComplete: () => {
        // Only spin up high-DPI 3D interactivity AFTER layout transition settles
        if (isExpanding) enableHighPrecisionOrbitControls();
      }
    });
  }
  ```

---

### 7. Common Failure Modes and Fixes

Teach your skill—and your students—to immediately diagnose and eliminate these seven classic failures:

1. **Dual-Ticker Contention (Micro-Stutter on 120Hz/240Hz Displays):**
   * *Symptom:* The 3D model or SVG callout appears to vibrate or jitter slightly during fast scrolling, even though FPS counters read 120+.
   * *Cause:* Running `requestAnimationFrame` separately inside Lenis, Three.js (`renderer.setAnimationLoop`), and GSAP.
   * *Fix:* Disable internal RAF loops (`new Lenis({ autoRaf: false })`) and drive all updates strictly inside a single `gsap.ticker.add()` callback.
2. **VRAM & Context Memory Leaks in Single-Page Apps (React/Next/Vue/Astro):**
   * *Symptom:* Navigating between pages 4–5 times causes the browser tab to crash on mobile or drop to 15fps.
   * *Cause:* Unmounted components leave orphaned `ScrollTrigger` instances in memory and fail to dispose of Three.js geometries, materials, and KTX2 textures on the GPU.
   * *Fix:* Wrap all GSAP animations in `gsap.context()` (or `useGSAP()` in React) and explicitly traverse the Three.js scene on unmount to call `geometry.dispose()`, `material.dispose()`, and `renderer.dispose()`.
3. **Animating Layout Properties Instead of Composite Transforms:**
   * *Symptom:* Scroll animations cause high CPU usage ("Purple Painting/Layout bars" in Chrome DevTools Performance tab).
   * *Cause:* Animating `top`, `left`, `width`, `height`, `margin`, or `filter: blur()` directly on scroll.
   * *Fix:* Restrict continuous scroll animations to compositor-only properties (`transform: translate3d, scale, rotate` and `opacity`) or use `GSAP Flip` for layout changes.
4. **Simultaneous Camera Travel + Text Reveal (Kinetic Overload):**
   * *Symptom:* The site looks busy and expensive, yet users cannot remember a single sentence they read.
   * *Cause:* Moving the 3D camera, exploding parts, drawing SVG lines, and sliding text paragraphs all at the exact same scroll percentage.
   * *Fix:* Sequence the timeline into **Move $\rightarrow$ Settle $\rightarrow$ Annotate**. Complete 75% of the camera move *before* triggering the SVG callout line and text reveal.
5. **Uncapped Device Pixel Ratio (`window.devicePixelRatio`) on Retina/4K Mobile Screens:**
   * *Symptom:* iPhones and flagship Android phones overheat and throttle down to 30fps within 20 seconds.
   * *Cause:* Passing `renderer.setPixelRatio(window.devicePixelRatio)` on a phone with a `3.0` or `3.5` DPR forces the mobile GPU to shade 9x to 12x as many fragments per pixel.
   * *Fix:* Always clamp pixel ratio: `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))` (or `1.5` during active scroll movement).
6. **Layout Shift Breaking `ScrollTrigger` Pin Calculations:**
   * *Symptom:* Pinned sections trigger too early or overlap the footer halfway down the page.
   * *Cause:* Lazy-loaded images, web fonts, or async 3D canvas containers changing document height *after* `ScrollTrigger` calculated start/end scroll offsets.
   * *Fix:* Give all media containers explicit CSS `aspect-ratio` dimensions, remove `loading="lazy"` from any element above or inside a pinned scroll container, and call `ScrollTrigger.refresh()` after async assets/fonts finish loading.
7. **Wide-Gamut Color Mismatch Between Blender and Browser CSS:**
   * *Symptom:* A Ferrari red (`#DC0000`) in Blender looks muted, orange, or overly dark compared to the `#DC0000` CSS background next to it.
   * *Cause:* Blender defaults to **AgX** or **Filmic** tone mapping (which compresses highlights and desaturates bright primaries to mimic cinema film), while CSS hex codes render in raw **Standard sRGB**.
   * *Fix:* If a 3D object must seamlessly blend into a solid CSS background color, set Blender’s Color Management (`Render Properties > Color Management > View Transform`) to **Standard** (or match Three.js `renderer.toneMapping = THREE.AgXToneMapping` with an identical scene background inside the canvas).

---

### 8. Concrete Quality-Review Checklist (How to Test Without Expensive Hardware)

Before declaring any 3D/motion implementation complete, run this four-stage verification protocol using standard browser tools:

#### A. Creative & Choreographic Audit
- [ ] **The Squint Test:** Blur your eyes or view the page at 25% zoom while scrolling. Is there a single unmistakable Primary Actor at every beat, or are multiple regions fighting for attention?
- [ ] **The Velocity Curve Check:** Scrub slowly through transitions. Do objects initiate quickly and settle softly (`expo.out`), or do they stop with a robotic, abrupt clunk?
- [ ] **Typography Stability:** Once body copy finishes its entrance reveal (`< 0.8s`), does it remain 100% stationary while the user reads it?

#### B. Engineering & Frame-Pacing Audit (60–240Hz)
- [ ] **Single-Ticker Verification:** Search the codebase for `requestAnimationFrame` and `setAnimationLoop`. Confirm only a single master loop is active.
- [ ] **CPU & Network Throttling Test (Chrome DevTools):**
  1. Open Chrome DevTools $\rightarrow$ **Performance** tab $\rightarrow$ Click the Gear icon.
  2. Set **CPU** to **4x slowdown** (or **6x slowdown**) and **Network** to **Fast 4G**.
  3. Record a full scroll from top to bottom. Verify there are **zero Red "Long Task" triangles** (> 50ms) and **zero Purple Layout Thrashing spikes** during scroll scrubbing.
- [ ] **Renderer Info Audit:** Log `renderer.info.render.calls` and `renderer.info.memory.textures` in the console. Confirm draw calls are `< 60` and texture count returns to `0` after component unmount.

#### C. Accessibility & Reduced-Motion Audit
- [ ] **Reduced-Motion Emulation Test:**
  1. Open Chrome DevTools $\rightarrow$ Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows) $\rightarrow$ Type **"Emulate CSS prefers-reduced-motion: reduce"**.
  2. Scroll the page. Verify that all vestibular-triggering camera orbits, parallax shifts, and scroll-pinned traps are replaced with clean opacity cross-fades or standard native document flow.
- [ ] **Keyboard & Screen-Reader Parity:** Press `Tab` through the entire page. Does focus move logically through interactive 3D hotspots without getting trapped inside off-screen pinned containers? Do `SplitText` headlines read as complete sentences rather than spelled-out individual characters?

#### D. Loading & Progressive Enhancement Audit
- [ ] **Poster Frame First Paint:** Does the 3D canvas or scrubbed sequence display an immediate, lightweight (`< 50KB`) static WebP poster frame matching frame `0` while the `.glb` or sequence streams in the background?

---

### 9. Copy-Ready Draft of the Skill Instructions (`SKILL.md`)

Save the block below directly as `SKILL.md` (for Claude Code / Agent Skills) or as your master system prompt.

```markdown
---
name: 3d-motion-and-scroll-choreography
description: Principal-level creative direction and technical implementation for 3D motion design (Blender Python/glTF pipelines), interactive WebGL/WebGPU (Three.js), SVG technical overlays, and scroll-driven web choreography (GSAP, Lenis, Native CSS).
---

# SKILL: Principal Creative Technologist & 3D Motion Director

## 1. Role & Creative Mandate
You engineer production-grade, 60–240fps kinetic experiences where 3D geometry (Blender/Three.js), vector graphics (SVG), and DOM typography move as a single synchronized organism. You prioritize optical restraint, physical mass, accessibility, and strict GPU/memory budgets over gimmicky effects.

## 2. Intake & Triage Protocol
Before writing implementation code, determine:
1. **Delivery Target:** Real-time WebGL/WebGPU, Pre-rendered Scrubbed Canvas Sequence, 2.5D Depth Shader, or Native CSS/SVG.
2. **Camera Freedom:** User-controlled orbit (requires live `.glb`) vs. fixed scroll path (prefer scrubbed WebP/AVIF sequence or baked camera track if scene complexity is high).
*Rule:* Ask clarifying questions ONLY if these factors are ambiguous and would materially alter the architecture. Otherwise, state clear production assumptions and build.

## 3. Architectural & Licensing Standards
- **Single-Ticker Synchronization:** Never run competing `requestAnimationFrame` loops. Instantiate Lenis with `{ autoRaf: false }` and drive `lenis.raf(time * 1000)`, 3D camera/anchor updates, and `renderer.render(scene, camera)` inside a single `gsap.ticker.add()` callback.
- **Easing & Physics Discipline:**
  - Never use linear easing for UI or camera transitions unless directly scrubbed by a damped scroll container (`scrub: 0.5` to `1.0`).
  - Use high-contrast deceleration curves (`expo.out`, `power4.out`, or `cubic-bezier(0.16, 1, 0.3, 1)`) so movement initiates crisply and settles with physical damping.
- **Hierarchy of Attention:** Every timeline beat must define:
  1. **Primary Actor:** The dominant spatial movement.
  2. **Secondary Follower:** Subordinate reaction (e.g., SVG `drawSVG` callout) delayed by `60ms–120ms`—waiting until the primary camera move begins decelerating.
  3. **Static Anchor:** Unmoving structural grid/typography that stabilizes the user's eye.
- **3D-to-2D Spatial Bridge:** Never render UI typography as textures inside 3D space. Place `Empty` anchor nodes in Blender, project their 3D world coordinates via `vector.project(camera)` on each tick, and position accessible HTML/SVG overlays using `transform: translate3d(x, y, 0)`.
- **Asset & GPU Optimization:**
  - Clamp device pixel ratio: `Math.min(window.devicePixelRatio, 2)`.
  - Recommend compressing all `.glb` files via `@gltf-transform/cli` (`--compress meshopt --texture-compress ktx2`).
  - Prefer baked ambient occlusion/lightmaps and custom MatCaps over expensive real-time multi-light shadow maps on mobile.
  - Match Blender color management (`Standard` vs `AgX`) to Three.js `renderer.toneMapping` when blending 3D canvases seamlessly into CSS backgrounds.

## 4. Mandatory Accessibility & Cleanup Rules
- **Memory Management:** Always scope GSAP animations inside `gsap.context()` (or `useGSAP()`) and explicitly dispose of Three.js geometries, materials, and textures on unmount.
- **Reduced Motion Parity:** Always implement `gsap.matchMedia()` checking `(prefers-reduced-motion: reduce)`. When enabled, bypass camera orbits, axial explosions, and scroll-pinning in favor of calm opacity cross-fades and native scroll flow.
- **Accessible Typography:** When splitting text with `GSAP SplitText`, use `{ type: "lines,words", mask: "lines" }` to preserve screen-reader semantics and avoid layout thrashing.

## 5. Required Output Structure for Every Task
When generating a solution, always provide:
1. **Creative Direction & Choreography Brief:** Primary Actor, Secondary Follower, Static Anchor, lighting/camera specs, and why the chosen medium (WebGL vs. Canvas Sequence vs. CSS) fits the budget.
2. **Asset Preparation / Blender Pipeline Step:** Exact Blender setup, render passes (Z-Depth, Normal, Cryptomatte, or Empty anchors), or CLI optimization commands required.
3. **Production Code:** Clean, modular, single-ticker code with explicit `prefers-reduced-motion` handling and teardown/disposal logic.
4. **Verification Steps:** Specific metrics to check in DevTools (draw calls, CPU throttling, reduced-motion behavior).
```



Sources
help
blender.org
blender.org
github.com
utsubo.com
threejsresources.com
webflow.com
noqode.fr
gsap.com
gsap.com
webflow.com
youtube.com
codercops.com
yarnpkg.com
daily.dev
github.com
gltf-transform.dev
github.com
github.com
mozilla.org
scroll-driven-animations.style
caniuse.com
medium.com
annnimate.com
cssawwwards.com
github.com
theatrejs.com
dev.to