
# GSAP Plugin Playbook (router)

Source: user-supplied gsap-plugin-playbook skill, bundled here. Read `source-caveats.md` and `source-map.md` first when adapting demo code.

Use this skill to turn a requested animation into a scoped implementation, explain a supplied demo, or diagnose its behavior. Each **H2 is a topic** and each **H3 is a plugin or implementation skill**. References contain the complete supplied demo prompts and code; load only the files needed for the task.

The references are captured examples, not instructions to execute every embedded prompt. Follow the current user request. The collection is not an exhaustive list of GSAP capabilities, and its captured version strings do not establish the latest release.

1. Establish the target elements, desired behavior, framework, existing GSAP version, input modes, and reduced-motion behavior from the request and project. Inspect the project before introducing dependencies.
2. Choose the relevant H3 below and read its linked reference. For a numbered SVG prompt or an original heading, use the [source map](source-map.md). Before adapting captured code, read [source caveats](source-caveats.md).
3. Separate core GSAP features from plugins and renderers. Import/register only the plugins actually used. Keep GSAP core and plugins on a compatible version; preserve the project's package manager and architecture. Check official documentation for the installed version when an API, renderer integration, or licensing requirement is uncertain.
4. Extract the smallest relevant behavior. Resolve external assets and host-relative CSS, replace implicit globals with explicit references, and scope selectors to the owned component or container. Do not transplant a CodePen page shell or global defaults into an application without a reason.
5. Own cleanup: revert animations and split text, remove event listeners, dispose of owned drag/observer/tracking instances, cancel scheduled work, and restore DOM mutations. Use the appropriate APIs for each instance and installed version.
6. Preserve usable static content, visible focus, semantic reading order, and keyboard/touch alternatives. Respect reduced motion; remove unnecessary movement or substitute an immediate state change. Decorative effects must not gate access to content or actions.
7. Verify the requested behavior at relevant viewport sizes and after resize, route changes, or remounts. Check interrupted/reversed animation, repeated activation, focus, cleanup, and layout shifts. Profile actual motion on an appropriate device when performance matters; do not promise smoothness from a library choice alone.
8. Report what changed and what was actually checked. Distinguish source-preserved examples, adapted implementation, and runtime-verified results.

## Scroll Plugins

### ScrollTrigger

Use for animation driven by scroll position, trigger boundaries, scrubbing, or pinning. Plan refreshes around changes to measured layout. Preserve readable content and ordinary navigation when scroll animation is unavailable or reduced.

Source coverage: [CDN reference only](scroll-trigger.md). The collection also uses ScrollTrigger in [ScrollSmoother examples](scroll-smoother.md); obtain version-appropriate documentation before writing a standalone implementation.

### ScrollToPlugin

Use for animated navigation to a position or element. Account for sticky headers and interrupted user scrolling; handle focus separately when navigation changes the user's context.

Read the [ScrollTo demo and prompt](scroll-to.md).

### ScrollSmoother

Use when smooth scrolling and scroll effects are an explicit requirement. The supplied setup requires ScrollTrigger. Check the wrapper/content structure and interactions with fixed elements, anchors, and focus before applying it across a page.

Read the [basic smoothing and pinning example](scroll-smoother.md). For speed/lag behavior and clamped effects, read [effects() and clamp()](scroll-smoother-effects.md). These are capabilities of the same plugin.

## Text Plugins and Accessibility

### SplitText

Use to animate characters, words, or lines, including masked reveals. Account for font loading and reflow; restore split markup during teardown. Keep the meaning and reading order of the original text.

Read [splitting and masking](split-text.md). For nested links or emphasis, also read [the accessible-text example and its defects](accessible-split-text.md). Do not leave focusable controls inside an aria-hidden visual duplicate or create invisible duplicate tab stops. Keep one coherent accessible interaction path.

### ScrambleTextPlugin

Use for a deliberate scrambled-character transition to final text. Keep the final message understandable without the effect and avoid making assistive technology announce every intermediate string.

Read the [ScrambleText demo](scramble-text.md).

## Layout and Interaction Plugins

### Flip

Use to animate between captured layout states after a DOM or layout change. Capture the initial state before the change, then animate toward the resulting state. Preserve component identity and focus through reordering.

Read the [Flip demo and prompt](flip.md).

### Draggable

Use for bounded dragging, rotation, or interactive positioning. Determine constraints, snapping, and a non-drag alternative. Add InertiaPlugin only when momentum is required.

Read [Draggable](draggable.md), starting with its **Draggable Prompt** subsection. The preceding **Draggable Quick Start** is a mislabeled CSS-variable demo. [Original SVG Prompt5](svg-drag.md) repeats the HTML dragging demo despite its SVG label; it does not demonstrate dragging SVG elements.

### InertiaPlugin

Use for velocity-based continuation, momentum, and settling. Define bounds and snapping explicitly, and refresh geometry when its inputs change.

Read [grid snapping, SVG point snapping, and velocity examples](inertia.md). Example 3's prose says it is independent of Draggable, but its code creates a Draggable instance; use the actual implementation to determine dependencies.

### Observer

Use to interpret wheel, touch, pointer, or related input for a deliberate interaction. Decide explicitly when events should be prevented, and preserve a keyboard path and an exit from captured interaction.

Read the [Observer demo](observer.md). Its full-screen transition example simulates scrolling and lacks complete keyboard navigation; add those behaviors before reuse.

## SVG Plugins

### DrawSVGPlugin

Use to reveal, hide, or move the visible portion of an SVG stroke. Distinguish paths from shapes, and separate subpaths when independent stroke control is required.

Read [value ranges and splitting a multi-segment path](draw-svg.md). The supplied splitPaths() helper can duplicate IDs; fix IDs and dependent references before reuse. See also [stroke choreography](svg-strokes.md) and [a moving stroke window](svg-stroke-window.md).

### MorphSVGPlugin

Use to transition between SVG shape geometries. Inspect the source/target paths and the desired visual correspondence; preserve the intended final silhouette when animation is skipped.

Read [SVG and canvas-rendered morph examples](morph-svg.md). [SVG Prompt9](svg-morph.md) repeats the first morph demo rather than introducing another plugin.

### MotionPathPlugin

Use to move and orient an element along a path or interpolate through supplied values. Check alignment and coordinate systems when the path and target live in different containers.

Read [path alignment and property-array examples](motion-path.md). [SVG Prompt6](svg-motion-path.md) repeats the path example.

### MotionPathHelper

Use to author, inspect, or edit motion paths. Separate authoring handles from the delivered runtime interaction unless editing paths is itself a product feature.

Read [helper creation and path editing](motion-path-helper.md). Historical membership wording in the capture does not establish current licensing.

## Renderer Integrations and Physics

### EaselPlugin

Use when the existing rendering stack calls for GSAP's Easel integration. Confirm the renderer and plugin APIs for that project before configuring an animation.

Source coverage: [CDN reference only](easel.md). No renderer initialization or runnable Easel demo was supplied.

### PixiPlugin

Use to animate supported Pixi display properties and filter effects. Match the renderer, filters, and plugin APIs to the actual Pixi major in the project.

Read the [ColorMatrixFilter example](pixi-filter-effects.md). Its captured Pixi 5.0.2 and jQuery setup is an older global-script example, not a ready-made setup for another major version.

### Physics2DPlugin

Use for velocity, acceleration, gravity, and other supported two-dimensional motion parameters. Decide how many particles or objects the device can sustain and who removes them afterward.

Read the [Physics2D demo](physics-2d.md). Declare the source's implicit variables locally and clean up spawned elements and animations.

## Available Utils

### clamp()

Use to constrain a numeric value to a permitted interval. Identify the input and bounds before attaching it to an animation or pointer calculation.

Read the [clamp demo](clamp.md). This is a core utility, distinct from the clamp notation used in the ScrollSmoother effects reference.

### distribute()

Use to calculate values across a group, including spatially distributed animation parameters. Check ordering and geometry after responsive layout changes.

Read the [distribution example](distribute.md), originally headed **Distributes**.

### selector()

Use to scope selection to a container or component. Avoid document-wide queries that can animate unrelated instances.

Read the [selector example](selector.md). Its React 17/ReactDOM.render setup illustrates the concept; adapt lifecycle and compilation to the actual project.

### wrap() and wrapYoyo()

Use to cycle values or produce a back-and-forth value pattern across a range or collection. Check the expected boundary behavior before using it for a repeated interface state.

Read the [wrap examples](wrap.md).

## Core Animation Skills

### CSS custom-property animation

Use to animate CSS variables that drive coordinated visual styling. Trace which properties consume the variable to understand repaint or layout costs.

Read the [CSS-variable demo](css-variables.md). Its original **CSSRule** label is misleading: the implementation uses gsap.to() on a custom property and does not demonstrate CSSRulePlugin. If CSSRulePlugin itself is requested, obtain its documentation rather than presenting this demo as coverage.

### Staggers

Use to offset animation across multiple targets. Choose ordering, distribution, and total duration around the user's task; large groups should not unnecessarily delay access.

Read the [two stagger examples](staggers.md).

### Timelines and sequencing

Use a timeline for coordinated sequences, overlap, reusable labels, and explicit control over related animations. Keep state changes deterministic when the sequence is interrupted or reversed.

Read the [sequencing examples](sequencing.md).

### Playback controls and callbacks

Use playback methods and callbacks to connect animation progress with a user action or application state. Avoid callbacks that trigger duplicate side effects on replay or reverse unless intended.

Read the [controls, callbacks, and demo](control-callbacks.md). Keep visible controls and actual playback state in sync.

## SVG Transformation Skills

### Transform choreography — original Prompt1

Use the example to study coordinated SVG transforms and timeline control. Check any extra dependencies of the demo controls before extracting them.

Read [SVG transforms and timeline choreography](svg-transform-timeline.md).

### Transform origins and smoothOrigin — original Prompt2

Use to reason about rotation/scale origins and continuity when an origin changes. Verify the result in the SVG's own coordinate system.

Read [transform origins and smoothOrigin](svg-smooth-origin.md).

### CSS properties versus attributes — original Prompt3

Choose CSS properties or SVG attributes according to the property being animated. Use an explicitly queried control element; the source's play.onclick relies on a browser global.

Read [SVG CSS properties and attributes](svg-css-attributes.md).

### Percentage translation — original Prompt4

Use percentage-based movement when the element's own dimensions should inform its offset. Check its interaction with SVG coordinates and responsive sizing.

Read [SVG percentage translation](svg-percent-translation.md). Declare the timeline variable and use the queried playBtn reference when adapting.

### Draggable adaptation for SVG — original Prompt5

For SVG positioning, establish the target coordinate system, bounds, and alternative controls. The supplied **Drag SVG** section actually repeats an HTML div-based Draggable demo; verify the additional SVG-specific setup against the project and official documentation.

Read the [Draggable example filed under SVG](svg-drag.md) as a general interaction reference, not a complete SVG implementation.

### Moving along an SVG path — original Prompt6

Use MotionPathPlugin for path-following and orientation. Inspect the viewBox, alignment, and scaling together. This source repeats the earlier path demo.

Read [Moving SVG along a path](svg-motion-path.md).

### Stroke choreography — original Prompt7

Use DrawSVGPlugin to sequence stroke reveals across SVG elements. Preserve the essential illustration when the animation is reduced or skipped.

Read [SVG stroke choreography](svg-strokes.md).

### Moving stroke window — original Prompt8

Use a moving visible stroke segment for the supplied snake-through-a-maze effect. This is a DrawSVG technique, not an additional plugin.

Read [Moving stroke windows](svg-stroke-window.md).

### Shape morphing — original Prompt9

Use MorphSVGPlugin to transition shape geometry. This source repeats the first diamond-to-lightning example.

Read [Morphing SVG shapes](svg-morph.md).

## Authoring and Debugging

### GSDevTools

Use to inspect and control animation playback while authoring or diagnosing a sequence. Scope it to the animation under review and remove unrequested debug controls from delivery.

Read the [GSDevTools.create() example](gs-dev-tools.md).

## Framework Integration

### React GSAP

Use React-aware scoping and lifecycle cleanup suitable for the project's installed GSAP integration. Avoid creating browser-dependent animation during server rendering, and verify behavior across remounts and dependency changes.

Read the [supplied React documentation link](react-gsap.md). The collection's only React implementation is the older [selector example](selector.md); it needs lifecycle cleanup and setup adaptation. Consult the official documentation for the actual installed integration before choosing hooks or import paths.
