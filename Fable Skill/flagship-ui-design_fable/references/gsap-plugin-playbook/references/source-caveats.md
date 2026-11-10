# Source caveats and adaptation checks

These notes come from inspection of the supplied document, not execution of its demos or a current-release audit. The original examples remain intact so their provenance and prompts are recoverable. Use the [source map](source-map.md) to find an original heading or numbered prompt.

## Labels and coverage

- **CSSRule** contains a CSS custom-property tween, not CSSRulePlugin usage.
- **Draggable Quick Start** repeats that CSS-variable demo. Actual dragging begins in the following **Draggable Prompt** subsection.
- **Prompt5 Drag SVG** repeats an HTML div-based Draggable demo with image backgrounds. It does not demonstrate SVG element dragging, coordinate conversion, or SVG-specific bounds despite its section label.
- **Screen reader-only** is a SplitText accessibility technique. ScrollSmoother **effects()/clamp()** is part of ScrollSmoother. Neither is a separate plugin.
- **Distributes** refers to distribute(). Staggers, sequencing, controls, and the utility methods are core features rather than separate plugins.
- ScrollTrigger and Easel have CDN references only. The final React section has a documentation link only. Do not claim these sections supply runnable standalone implementations.
- TextPlugin and CustomEase occur as supporting dependencies, without dedicated tutorial sections. A demo's script manifest is not proof that every listed plugin is needed.

## Repeated demonstrations

- The CSS-variable demo is copied into the Draggable quick-start subsection.
- The actual Draggable demo is repeated under SVG Prompt5.
- The MotionPath SVG example is repeated under SVG Prompt6 with a different CodePen record.
- The first MorphSVG demo is repeated under SVG Prompt9.

Keep those source references available, but do not count repeated examples as new plugins or independently tested implementations. Load one copy when the task does not require comparison.

## Versions and dependencies

The capture mixes GSAP 3.14.1, 3.15, and 3.15.0 references. It also includes React 17.0.2, Pixi 5.0.2, and jQuery 2.1.3/3.1.1. These are captured strings, not recommendations of the latest or best version.

For an implementation, inspect the existing dependency manifest and lockfile. Select compatible core/plugins and renderer APIs; register the plugins actually used. Retain architecture unless the task requires a change. Historical Club GreenSock comments and “new in” release descriptions are not current licensing or availability claims; verify those separately if the user needs them.

ScrollSmoother requires ScrollTrigger in the supplied setup. Inertia Example 3 describes independent usage but constructs a Draggable instance. The multi-segment DrawSVG example lists many plugins while its relevant behavior chiefly uses DrawSVG and MotionPath. Resolve dependencies from the actual code and requested behavior.

## Assets and standalone setup

Host-relative `/demo-assets/pens/*.css` links depend on the originating site's directory structure. Captured fonts, images, CSS variables, noise textures, and demo UI may also depend on remote GSAP resources. Identify those dependencies before adapting; supply appropriate local/project assets and styles rather than assuming the capture will run as-is. Preserve attribution and check reuse rights when redistributing third-party assets.

React's captured JSX needs an appropriate compilation environment. ReactDOM.render and UMD globals are not a universal framework template. Check any jQuery/UI controls and renderer setup independently of the animation itself.

## Accessibility repairs

The SplitText nested-link example places a focusable anchor in an aria-hidden visual copy and another inside a clipped screen-reader copy. The provided `.sr-only:not(:focus)` rule does not reveal a parent when its descendant receives focus. Blind duplication can therefore create invisible or duplicate keyboard stops.

Choose a strategy that preserves nested semantics, one coherent reading order, visible focus, and operable controls. Verify it with the keyboard and relevant assistive technology. An aria-hidden attribute by itself does not remove descendant controls from keyboard navigation.

The Observer demo intercepts wheel/touch/pointer input to simulate scroll-driven sections and lacks a complete keyboard alternative. Provide usable navigation and an exit from input capture. For every effect, preserve the essential content and a reduced-motion path.

## Module safety and ownership

- SVG Prompt3 and Prompt4 declare playBtn but assign play.onclick. Use the queried reference instead of implicit named-window access.
- Physics2D assigns undeclared i and flairBullet; SVG Prompt4 assigns undeclared tl. Declare and scope these variables before using strict mode or modules.
- Scope selectors; avoid accidental global gsap.defaults changes and document-wide listeners that affect other components.
- Own the cleanup of repeating timelines, listeners, split DOM, Draggable/Observer instances, inertia tracking, generated elements, and scheduled callbacks. Use the installed library's correct teardown APIs rather than assuming every resource has the same method.
- React's supplied effect lacks cleanup. Verify remount behavior and prevent duplicate animation/event registration.

## Geometry and SVG integrity

The multi-segment splitPaths() helper copies every source attribute, including id, onto each generated path. Assign unique IDs or remove them when safe, and deliberately repair any references that depend on them.

Several demos use fixed dimensions or measure geometry only once, including an inertia ball radius and canvas size. Refresh relevant calculations after resize, font loading, image loading, or layout changes. Preserve the original DOM or define a reversible reconstruction strategy when a demo creates or replaces SVG nodes.

## Validation boundaries

For this skill conversion, source code preservation and file structure can be checked without running the demos. Those checks do not establish browser compatibility, accessibility, performance, current package maintenance, or production readiness. When applying the skill to an actual project, verify those aspects according to the requested behavior and report only the checks performed.
