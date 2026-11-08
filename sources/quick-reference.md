# Premium UI/UX quick reference

**Research snapshot: November 6, 2026.** Read the [full field guide](PREMIUM-UI-UX-FIELD-GUIDE.md) for capabilities, official links, compatibility/maintenance caveats, and evidence flags. Use the [CSV index](UI-UX-TOOL-INDEX.csv) to sort or filter the 341 catalog entries. The [source ledger](SOURCE-LEDGER.md) records the research boundaries.

## What makes an interface feel premium

**Clear purpose + distinctive visual direction + precise interaction + accessible behavior + fast response + reliable recovery.**

Check the actual user journey, not only a screenshot. A beautiful hero cannot compensate for unclear navigation, lost form data, inaccessible controls, or a stalled save action.

## Choose by the job

| Job | Start by evaluating | Key decision |
|---|---|---|
| Small hover/focus/pressed states | Native CSS | Keep feedback direct and inexpensive. |
| Complex sequences, scroll choreography, SVG | GSAP + selected plugins | Use timeline/scroll/SVG/interaction capabilities you actually need. |
| App layout, enter/exit, gestures | Motion; framework/native transitions | Preserve continuity and interruption behavior. |
| Physics-driven UI springs | Motion / react-spring / platform springs | Smooth retargeting matters more than dramatic bounce. |
| Shared page/state transitions | View Transition API | Confirm exact browser feature support and route/focus behavior. |
| Scroll progress | Native scroll timelines or ScrollTrigger | Retain useful ordinary scrolling and a static fallback. |
| Optional smooth scrolling | Lenis or ScrollSmoother | Add only if it improves this experience; check navigation, touch, and scroll-snap interaction. |
| Interactive 3D | Three.js or Babylon.js | Plan assets, GPU budget, accessibility, and fallback. |
| React 3D | React Three Fiber + selected Drei | Match stable versions and keep frame updates efficient. |
| Simple 3D product viewing | model-viewer | Avoid building an entire scene system for a single preview. |
| Illustrated interactive motion | Rive | Verify runtime features and asset cost on every target. |
| Exported vector animation | Lottie / dotLottie | Check actual export compatibility and control looping. |
| 2D scenes/editors | PixiJS / Konva / Fabric.js | Choose rendering throughput versus editing features deliberately. |
| Shader art | Paper Shaders / custom shaders / TypeGPU | Bound resolution, work, and motion; preserve readable content. |
| Custom accessible controls | React Aria / Base UI / Radix / Ark UI | Choose one primary behavior foundation. |
| Components you customize and own | shadcn/ui or corresponding Vue/Svelte implementation | Budget for source ownership and updates. |
| Broad styled app UI | MUI / Mantine / Ant Design / Fluent / platform systems | Choose for the product's workflow, density, and ecosystem. |
| Large tables/lists | TanStack Table/Virtual / AG Grid / Virtuoso | Preserve selection, focus, URL state, and scroll restoration. |
| Forms | Native semantics + framework-appropriate form/schema tools | Validate clearly; preserve suitable input; recover from server errors. |
| Workflow diagrams | React Flow / Svelte Flow | Add persistence, keyboard access, undo, and domain behavior. |
| Typography | Appropriate font + Fontsource + variable-font features + Utopia | Test readability, loading, fallback metrics, languages, and zoom. |
| Design tokens | DTCG format + Tokens Studio / Style Dictionary | Establish semantic roles, ownership, and platform output. |
| AI design workflow | Impeccable; focused current skills | Provide a brief, authentic content, references, and acceptance criteria. |
| Creative component discovery | 21st.dev / React Bits / Magic UI / Cult UI / Kokonut | Inspect each component's source, license, dependencies, and real-device behavior. |
| Native iOS/macOS | SwiftUI + targeted UIKit/AppKit | Follow platform input, accessibility, navigation, and window conventions. |
| Native Android | Compose + appropriate animation APIs | Test back behavior, text scale, insets, gestures, and frame pacing. |
| Cross-platform mobile | React Native/Expo or Flutter; consider Compose Multiplatform | Prove the hardest interaction on each target. |
| Desktop | Electron / Tauri / Qt / appropriate .NET stack | Evaluate native integration, resource use, and platform differences. |
| Verification | Browser profilers + Playwright + axe + real assistive tech | Automation and snapshots cover only part of quality. |
| User understanding | Task tests, interviews, tree tests; Maze / Lyssna as appropriate | Choose a method that answers the actual design question. |

These are shortlists to evaluate, not benchmark winners or a combined installation list. See the full guide for V/R verification status for each item.

## Page and component essentials

| Surface | Acceptance criteria |
|---|---|
| Hero | Clear proposition, authentic visual, obvious action, fast primary content, mobile art direction. |
| Sections | Logical story, useful headings, varied but coherent composition, real evidence, accessible structure. |
| Navigation | Current location, descriptive labels, working keyboard/touch, deep links, back/forward, focus/scroll restoration. |
| Pagination | Current page, sensible range, previous/next, clear disabled state, preserved filters/sort, appropriate URL state. |
| Typography | Coherent roles, readable measure/leading, thoughtful wrapping, real text, stable fonts, script coverage. |
| Forms | Persistent labels, autofill, clear validation, input recovery, loading/success/error, duplicate-submit handling. |
| Modal / sheet | Correct label, focus lifecycle, dismissal, scroll handling, keyboard/insets, safe areas. |
| Table / chart | Clear units and headings, meaningful selection/sort, responsive behavior, keyboard and textual alternatives. |
| Empty / loading / error | Explain state and next action; preserve layout and work; offer useful retry. |
| Motion | Purpose, consistent timing, interruption/reversal, bounded cost, meaningful reduced-motion equivalent. |

## Performance and accessibility checkpoints

- **Core Web Vitals:** good field results are LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 at the 75th percentile; assess mobile and desktop separately. [Official guidance](https://web.dev/articles/vitals).
- **Frame pacing:** approximately 16.67 ms per display interval at 60 Hz and 8.33 ms at 120 Hz; the full pipeline shares that interval. Measure missed deadlines, not only average FPS.
- **Animation:** keep one owner per animated property. Avoid repeated layout read/write cycles; pause unnecessary loops; limit layers, textures, postprocessing, and large blur regions.
- **Loading:** prioritize the real hero/LCP asset, reserve image dimensions, deliver suitable image/font variants, and defer nonessential work.
- **Accessibility:** keyboard and visible focus; meaningful names/roles; contrast; text resizing/reflow; reduced motion; non-drag alternatives; accessible authentication and error recovery.
- **Targets:** WCAG 2.2 AA uses 24×24 CSS px with specific exceptions; 44×44 belongs to the enhanced AAA criterion. The guide explains the exact distinctions. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum).
- **Testing:** use real content and a slower supported device. Include interrupted requests, offline/reconnect where relevant, rapid repeated input, long strings, large text, and assistive technology.

## Motion timing starting points

Try **80–150 ms** for small feedback, **150–250 ms** for compact enter/exit, **200–400 ms** for larger spatial transitions. These are design heuristics, not standards. Tune by input, travel, platform, audience, and repeated use. Keep direct gesture feedback continuous and preserve velocity when retargeting a spring.

## Five rules for avoiding a fragile “premium” interface

1. Select a primary component system and a principal motion strategy; add specialist tools for concrete requirements.
2. Use real content and real tasks before decorating the UI.
3. Make keyboard, touch, screen reader, reduced-motion, failure, and recovery behavior part of the design.
4. Review current docs, release channel, license, maintenance, and target-platform support before adoption.
5. Judge the delivered experience through task completion and measured runtime behavior, alongside visual quality.

The full guide includes **140 quality checks, 341 catalog entries, 24 motion patterns, and 15 promising design repositories**. Of the catalog entries, **280 have inspected official-source evidence; 61 are clearly marked reference candidates needing a fresh check**. No finite inventory includes every possible tool or technique.
