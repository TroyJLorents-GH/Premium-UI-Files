# Motion routing

Motion must clarify the hero's story, reveal hierarchy, demonstrate the product, or connect scenes. A premium static composition does not need motion to prove its quality.

## GSAP core

Read the current `gsap-core` skill before implementation. Use it for coordinated entrances, staged typography, product demonstrations, SVG motion, controlled loops, and animations that need interruption or runtime control. Keep simple state transitions in CSS when a GSAP runtime adds no value.

- Prefer transform aliases such as `x`, `y`, `scale`, and `rotation`; use `autoAlpha` when an invisible element must stop intercepting interaction.
- Use timelines for sequences instead of chains of unrelated delays.
- Scope selectors to the hero and clean up animations on unmount. Load the framework-specific GSAP skill when one is available and relevant.
- Use `gsap.matchMedia()` for responsive behavior and `prefers-reduced-motion`. The reduced path must reveal the complete content without requiring animation.
- Do not animate layout-heavy properties when transforms achieve the same result.

## GSAP ScrollTrigger

Read the current `gsap-scrolltrigger` skill when motion responds to scroll, pins a scene, scrubs a timeline, or creates parallax. Register the plugin once and attach ScrollTrigger to a top-level tween or timeline.

- Choose scrub for scroll-linked progress or toggle actions for discrete playback; do not combine both on one trigger.
- If pinning, animate a child rather than the pinned element. Create triggers in page order and refresh after fonts, images, or dynamic layout changes.
- Use `ease: "none"` for a containerAnimation-driven horizontal sequence. Do not leave development markers in shipped code.
- Keep native scrolling usable and avoid long pinned passages that trap the visitor between the hero and the page content.
- Kill triggers or use the framework's GSAP cleanup mechanism on unmount. Verify forward/backward scroll, resize, mobile behavior, and reduced motion.

## scroll-world

Read the complete `scroll-world` skill only when the brief calls for its actual product: a continuous pre-rendered camera flight through multiple connected scenes, a diorama world, or a scroll-scrubbed cinematic. Ordinary parallax, a pinned product showcase, or one background video belongs to GSAP/ScrollTrigger instead.

`scroll-world` depends on specialized media generation, video encoding, seam construction, and paid rendering. Follow its current interview, tooling, model-qualification, frame-handoff, native-mobile, and QA instructions. Before any paid generation:

- Inspect the current provider capabilities and balances.
- Price the real scene count, mobile option, and re-roll headroom.
- Present the estimate and obtain the user's explicit approval for that spend.
- Create and approve the required static visual direction before rendering the complete chain.

Never describe a generic set of crossfaded clips as a seamless scroll world. Its neighboring clips must use actual rendered boundary frames, and the implementation must pass seam and seeking QA. If the media pipeline is unavailable or unapproved, keep the static/GSAP hero complete and present scroll-world as a separate optional production phase.

## Motion review

Review the motion in the real page, not as an isolated animation demo:

- The first useful hero state appears quickly and remains understandable with JavaScript delayed or motion reduced.
- Text stays readable; motion does not fight scrolling, navigation, or the primary action.
- Mobile receives its own motion/layout decision rather than a scaled desktop timeline.
- No flash of hidden content, stale ScrollTriggers, console errors, scroll jumps, or invisible click blockers remain.
- Asset weight and decode cost are proportionate to the result. Record what was tested on desktop, mobile/emulation, and reduced motion.
