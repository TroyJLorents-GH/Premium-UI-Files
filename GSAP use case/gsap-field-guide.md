# GSAP Field Guide

A working reference for GSAP 3: the core API, every plugin, the helper tools, and the judgment calls about when GSAP is the right tool. Written against GSAP 3.13, where every plugin, including the former Club plugins, is free and ships in the `gsap` npm package.

## Overview & when to use it

```js
npm i gsap
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
gsap.registerPlugin(ScrollTrigger, SplitText); // register once, before use
```

**Use GSAP when**

- You need sequenced, multi-step choreography (timelines).
- Animation is tied to scroll position, pinning, or scrubbing.
- You animate SVG, canvas, WebGL/three.js values, or plain JS objects.
- You need runtime control: pause, reverse, seek, timeScale.
- Text splitting, layout (FLIP) transitions, drag/throw, morphing.
- Cross-browser consistency matters (transforms on SVG, etc.).

**Skip GSAP when**

- A simple hover/focus state change: a CSS `transition` is enough.
- A looping spinner or ambient effect: CSS `@keyframes` runs off the main thread.
- Basic scroll-reveal with no scrubbing: `IntersectionObserver` + CSS class, or CSS scroll-driven animations.
- React state-driven enter/exit with layout: Motion (Framer Motion) may be more idiomatic.
- Page transitions between routes: the View Transitions API covers the basics.
- Bundle budget is very tight and you need one tween (core is ~25 KB gzip).

## Terms to know

| Term                     | Meaning                                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Tween                    | A single animation that changes properties of one or more targets over time. Created by `gsap.to/from/fromTo`.          |
| Timeline                 | A container of tweens/timelines with its own playhead. Used for sequencing and grouping control.                        |
| Target                   | What gets animated: selector string, element, array, NodeList, or any JS object.                                        |
| vars                     | The config object passed to a tween (properties + special props like `duration`, `ease`, callbacks).                    |
| Special properties       | Keys in vars that configure the tween rather than being animated (duration, delay, repeat, yoyo, stagger, onComplete…). |
| Position parameter       | Third arg of timeline methods controlling *where* the child goes: `"<"`, `"+=0.5"`, `"label"`, absolute seconds.        |
| Playhead                 | The current time position of an animation.                                                                              |
| progress / totalProgress | 0–1 position, excluding / including repeats.                                                                            |
| time / totalTime         | Seconds into the animation, excluding / including repeats and repeatDelay.                                              |
| timeScale                | Playback speed multiplier (2 = double speed, 0.5 = half).                                                               |
| Ease                     | Rate-of-change curve, e.g. `"power2.out"`. Types: `.in`, `.out`, `.inOut`.                                              |
| Stagger                  | Offsetting each target's start time in a multi-target tween.                                                            |
| Ticker                   | GSAP's single requestAnimationFrame loop that drives everything.                                                        |
| globalTimeline           | Root timeline every animation lives on by default.                                                                      |
| Immediate render         | `from()`/`fromTo()` render their start values instantly (`immediateRender:true`) to avoid a flash.                      |
| Overwrite                | How a new tween handles conflicting tweens on the same props (`false`, `true`, `"auto"`).                               |
| Lazy rendering           | GSAP batches first renders to the end of the tick to avoid layout thrashing.                                            |
| Context                  | `gsap.context()`: collects animations created inside so they can be reverted together (key for React/SPA cleanup).      |
| matchMedia               | `gsap.matchMedia()`: a context that only runs while a media query matches and auto-reverts when it stops.               |
| Scrub                    | Linking an animation's progress directly to scroll position.                                                            |
| Pin                      | Holding an element fixed while the user scrolls through a section.                                                      |
| Trigger / scroller       | Element whose position starts/ends a ScrollTrigger / the scrolling container (default viewport).                        |
| FLIP                     | First, Last, Invert, Play: record state, change layout, animate from old to new.                                        |
| Quick setter / quickTo   | Optimised functions for setting/animating one property many times per second (e.g. mouse follow).                       |
| Modifiers                | Functions that intercept each property value on every tick (wrapping, snapping).                                        |
| Keyframes                | An array or object of steps inside a single tween.                                                                      |

## gsap.\* methods

| Method                            | What it does                                                                                             |
|-----------------------------------|----------------------------------------------------------------------------------------------------------|
| gsap.to(targets, vars)            | Animate from current values to the values in vars.                                                       |
| gsap.from(targets, vars)          | Animate from vars to current values.                                                                     |
| gsap.fromTo(t, from, to)          | Define both ends explicitly. Most predictable.                                                           |
| gsap.set(targets, vars)           | Zero-duration tween; set values immediately.                                                             |
| gsap.timeline(vars)               | Create a Timeline.                                                                                       |
| gsap.registerPlugin(...)          | Register plugins (prevents tree-shaking from dropping them).                                             |
| gsap.registerEase(name, fn)       | Register a custom ease by name.                                                                          |
| gsap.registerEffect({...})        | Package a reusable animation as `gsap.effects.name()`.                                                   |
| gsap.config({...})                | Global settings: `autoSleep`, `force3D`, `nullTargetWarn`, `units`.                                      |
| gsap.defaults({...})              | Default vars for all tweens, e.g. `{ease:"power2.out", duration:0.6}`.                                   |
| gsap.context(fn, scope)           | Scope selectors and collect animations for `ctx.revert()`.                                               |
| gsap.matchMedia()                 | Responsive animations: `mm.add("(min-width:800px)", () => {...})`.                                       |
| gsap.matchMediaRefresh()          | Re-run all matchMedia conditions (e.g. after a reduced-motion toggle).                                   |
| gsap.getProperty(t, prop, unit?)  | Read current value (parsed number unless unit passed).                                                   |
| gsap.quickSetter(t, prop, unit)   | Fast setter function; no tween.                                                                          |
| gsap.quickTo(t, prop, vars)       | Reusable tween function; call with new end values.                                                       |
| gsap.getTweensOf(targets)         | Array of active tweens on targets.                                                                       |
| gsap.isTweening(target)           | Boolean.                                                                                                 |
| gsap.killTweensOf(t, props?)      | Kill tweens of targets (optionally only certain props).                                                  |
| gsap.getById(id)                  | Find an animation by its `id` var.                                                                       |
| gsap.delayedCall(sec, fn, params) | Timer on GSAP's ticker (pauses with the global timeline).                                                |
| gsap.exportRoot()                 | Wrap all current root animations in one timeline (e.g. slow-mo everything).                              |
| gsap.globalTimeline               | Root timeline: `gsap.globalTimeline.timeScale(0.5)`.                                                     |
| gsap.ticker                       | `add(fn)`, `remove(fn)`, `fps(n)`, `lagSmoothing(threshold, adjusted)`, `deltaRatio()`, `time`, `frame`. |
| gsap.updateRoot(time)             | Manually drive the root (used when you own the render loop).                                             |
| gsap.parseEase(str)               | Return the easing function for a string.                                                                 |
| gsap.version                      | Version string.                                                                                          |
| gsap.utils                        | Utility methods; see [Utilities](#utils).                                                                |
| gsap.plugins / gsap.core          | Access registered plugins / core classes (Tween, Timeline, Animation).                                   |

```js
gsap.defaults({ ease: "power3.out", duration: 0.8 });

gsap.registerEffect({
  name: "fadeUp",
  effect: (targets, config) => gsap.from(targets, { y: 40, autoAlpha: 0, duration: config.duration }),
  defaults: { duration: 0.6 },
  extendTimeline: true            // allows tl.fadeUp(".card", {}, "<")
});
gsap.effects.fadeUp(".card");

// Mouse follower: quickTo creates one reusable tween per axis
const xTo = gsap.quickTo(".cursor", "x", { duration: 0.4, ease: "power3" });
const yTo = gsap.quickTo(".cursor", "y", { duration: 0.4, ease: "power3" });
window.addEventListener("pointermove", e => { xTo(e.clientX); yTo(e.clientY); });
```

## Tween

### Special properties (vars)

| Property                                                                     | Default / notes                                                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| duration                                                                     | 0.5 seconds.                                                                                         |
| delay                                                                        | Seconds before start.                                                                                |
| ease                                                                         | `"power1.out"`. String or function.                                                                  |
| repeat                                                                       | Number of repeats; `-1` = infinite.                                                                  |
| repeatDelay                                                                  | Seconds between repeats.                                                                             |
| repeatRefresh                                                                | Re-record start/end values on each repeat (works with function-based values).                        |
| yoyo                                                                         | Alternate direction each repeat.                                                                     |
| yoyoEase                                                                     | Different ease on the yoyo leg (or `true` to flip the ease).                                         |
| stagger                                                                      | Number or object; see [Staggers](#staggers).                                                         |
| paused                                                                       | Start paused.                                                                                        |
| reversed                                                                     | Start reversed.                                                                                      |
| immediateRender                                                              | Render start values now. True for from/fromTo/set.                                                   |
| overwrite                                                                    | `false` (default), `true` (kill all tweens of same targets), `"auto"` (kill only overlapping props). |
| lazy                                                                         | Defer first render to end of tick (default true for to()).                                           |
| id                                                                           | Name for `gsap.getById()` / GSDevTools.                                                              |
| data                                                                         | Arbitrary data stored on the tween.                                                                  |
| keyframes                                                                    | Array of vars, percent object, or per-prop arrays.                                                   |
| modifiers                                                                    | Per-property functions applied each tick.                                                            |
| runBackwards                                                                 | Internal basis of from(); flips direction.                                                           |
| startAt                                                                      | Values to set before the tween starts.                                                               |
| inherit                                                                      | Set false to ignore parent timeline defaults.                                                        |
| callbackScope                                                                | The `this` for callbacks.                                                                            |
| onStart / onUpdate / onComplete / onRepeat / onReverseComplete / onInterrupt | Callbacks. Each has a matching `…Params` array.                                                      |

### Methods

| Method                                             | Notes                                                       |
|----------------------------------------------------|-------------------------------------------------------------|
| play(from?) / pause(at?) / resume()                | Basic control.                                              |
| reverse(from?) / reversed(bool?)                   | Play backward / get-set direction.                          |
| restart(includeDelay?)                             | Back to start and play.                                     |
| seek(time) / progress(v) / totalProgress(v)        | Jump the playhead.                                          |
| time(v) / totalTime(v)                             | Get/set seconds.                                            |
| duration(v) / totalDuration(v)                     | Get/set lengths.                                            |
| delay(v) / repeat(v) / repeatDelay(v) / yoyo(bool) | Getter/setters.                                             |
| timeScale(v)                                       | Speed.                                                      |
| startTime(v) / endTime()                           | Position on parent timeline.                                |
| isActive()                                         | Currently playing and inside its active range.              |
| paused(bool?)                                      | Get/set paused state.                                       |
| kill()                                             | Stop and release for GC.                                    |
| revert()                                           | Kill and restore targets' original inline styles.           |
| invalidate()                                       | Clear recorded start values so they re-read on next render. |
| then()                                             | Promise: `await gsap.to(...)`.                              |
| eventCallback(type, fn, params)                    | Get/set a callback after creation.                          |
| targets()                                          | Array of targets.                                           |
| iteration(n)                                       | Current repeat iteration.                                   |
| globalTime(local)                                  | Convert local time to global time.                          |

Properties: `tween.vars`, `tween.data`, `tween.parent`, `tween.ratio` (eased progress), `tween.scrollTrigger`.

```js
// to / from / fromTo
gsap.to(".box", { x: 200, rotation: 360, duration: 1, ease: "back.out(1.7)" });
gsap.from(".hero h1", { y: 60, autoAlpha: 0 });
gsap.fromTo(".bar", { scaleX: 0 }, { scaleX: 1, transformOrigin: "left center" });

// Function-based values: called per target
gsap.to(".item", { x: (i, el, all) => i * 50 });

// Relative values
gsap.to(".box", { x: "+=100", rotation: "-=45" });

// Keyframes (three syntaxes)
gsap.to(".box", { keyframes: [{ x: 100 }, { y: 100 }, { x: 0, y: 0 }] });
gsap.to(".box", { keyframes: { "0%": { x: 0 }, "50%": { x: 200, ease: "sine.out" }, "100%": { x: 0 } }, duration: 2 });
gsap.to(".box", { keyframes: { x: [0, 100, 0], y: [0, -50, 0], easeEach: "sine.inOut" }, duration: 2 });

// Await
await gsap.to(".modal", { autoAlpha: 0 });
modal.remove();

// Animate any JS object (great for canvas / three.js)
const state = { value: 0 };
gsap.to(state, { value: 100, onUpdate: () => label.textContent = state.value.toFixed(0) });
gsap.to(mesh.rotation, { y: Math.PI * 2, repeat: -1, ease: "none", duration: 6 });
```

## Timeline

A Timeline has every Tween method above, plus child management. Timeline-specific vars:

| Var                                          | Notes                                                                      |
|----------------------------------------------|----------------------------------------------------------------------------|
| defaults                                     | Vars inherited by every child: `{defaults:{duration:0.5, ease:"power2"}}`. |
| autoRemoveChildren                           | Remove children when they finish (root uses this).                         |
| smoothChildTiming                            | Keep children in place when you change their timing on the fly.            |
| repeat / yoyo / repeatDelay / paused / delay | Same as Tween, applied to the whole sequence.                              |
| scrollTrigger                                | Attach a ScrollTrigger to the whole timeline.                              |
| callbacks                                    | Same set as Tween.                                                         |

| Method                                            | Notes                                                    |
|---------------------------------------------------|----------------------------------------------------------|
| to / from / fromTo / set                          | Add a tween; third/fourth arg is the position.           |
| add(child, position)                              | Add a tween, timeline, label, callback, or array.        |
| addLabel(name, position)                          | Named marker.                                            |
| removeLabel(name)                                 | —                                                        |
| addPause(position, cb?)                           | Pause the timeline at that point.                        |
| call(fn, params, position)                        | Call a function at a point.                              |
| remove(child)                                     | —                                                        |
| clear(labels?)                                    | Empty the timeline.                                      |
| getChildren(nested, tweens, timelines)            | List children.                                           |
| getTweensOf(targets)                              | Children affecting targets.                              |
| getById(id)                                       | —                                                        |
| tweenTo(position, vars)                           | Returns a tween that scrubs the playhead to a point.     |
| tweenFromTo(from, to, vars)                       | Same, with a start point. Great for "play this chapter". |
| nextLabel() / previousLabel() / currentLabel()    | Label navigation (slideshows).                           |
| recent()                                          | Most recently added child.                               |
| shiftChildren(amount, adjustLabels, ignoreBefore) | Offset children in time.                                 |
| labels                                            | Object of label times.                                   |

```js
const tl = gsap.timeline({ defaults: { duration: 0.6, ease: "power2.out" }, paused: true });
tl.from(".nav", { y: -40, autoAlpha: 0 })
  .addLabel("content")
  .from(".title", { y: 30, autoAlpha: 0 }, "content")
  .from(".sub",   { y: 30, autoAlpha: 0 }, "<0.15")
  .from(".cta",   { scale: 0.8, autoAlpha: 0 }, "-=0.2")
  .call(() => console.log("done intro"))
  .addPause("+=0.5");
tl.play();

// Nest timelines: build sections as functions, compose in a master
function intro()  { return gsap.timeline().from(".a", { x: -100 }); }
function middle() { return gsap.timeline().to(".b", { rotation: 90 }); }
const master = gsap.timeline().add(intro()).add(middle(), "-=0.3");
```

## CSS (CSSPlugin)

CSSPlugin is built into core. Any numeric CSS property in camelCase works. Prefer transforms and opacity; they skip layout and paint.

| Shortcut                                | Meaning                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------|
| x, y, z                                 | translateX/Y/Z (px by default).                                                         |
| xPercent, yPercent                      | Percentage translate (stacks with x/y; use for centering: `xPercent:-50`).              |
| rotation / rotate, rotationX, rotationY | Degrees (or "1.5rad").                                                                  |
| scale, scaleX, scaleY                   | —                                                                                       |
| skewX, skewY                            | —                                                                                       |
| transformOrigin                         | `"50% 50%"`, `"left top"`.                                                              |
| transformPerspective                    | Per-element perspective.                                                                |
| svgOrigin                               | Origin in SVG global coordinates.                                                       |
| smoothOrigin                            | Avoid jumps when origin changes on SVG (default true).                                  |
| autoAlpha                               | opacity + `visibility:hidden` at 0. Use this for fades.                                 |
| force3D                                 | `"auto"` (default) uses 3D during, 2D after.                                            |
| clearProps                              | Remove inline props on complete: `"all"`, `"transform"`, `"x,y"`.                       |
| "--var"                                 | CSS variables: `{"--hue": 180}`.                                                        |
| Directional rotation                    | `"270_cw"`, `"-90_ccw"`, `"45_short"`.                                                  |
| Complex strings                         | boxShadow, filter, clipPath, backgroundPosition, borderRadius animate if formats match. |
| Width/height "auto"                     | Animating to `height:"auto"` works.                                                     |

```js
gsap.set(".modal", { xPercent: -50, yPercent: -50, left: "50%", top: "50%", position: "fixed" });
gsap.to(".card", { "--glow": 1, boxShadow: "0 20px 40px rgba(0,0,0,.3)", clipPath: "inset(0% 0% 0% 0%)" });
gsap.to(".panel", { height: "auto", duration: 0.4 });
gsap.to(".el", { x: 100, clearProps: "transform" });
```

Avoid animating `top/left/width/height/margin` in hot paths; they trigger layout. Use `x/y/scale`, or Flip for layout changes.

## Eases

### Built-in (core)

`none` (linear), `power1–4` (power1 = quad, power2 = cubic, power3 = quart, power4 = quint), `back(overshoot)`, `bounce`, `circ`, `elastic(amplitude, period)`, `expo`, `sine`, `steps(n)`. Each takes `.in`, `.out` (default), `.inOut`.

Rules of thumb: UI entrances use `.out`; exits use `.in`; things moving across the screen use `.inOut`; scrubbed scroll animations often use `"none"`; continuous rotation uses `"none"`.

### Ease plugins

| Ease          | Use / syntax                                                                                                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CustomEase    | Any curve from SVG path data (copy from the GSAP ease visualizer). `CustomEase.create("hop","M0,0 C0.3,0 0.2,1 1,1")`. Methods: `create`, `get`, `getSVGData`.                           |
| CustomBounce  | Tunable bounce plus a matching squash ease. `CustomBounce.create("myBounce",{strength:0.6, squash:3, squashID:"myBounce-squash", endAtStart:false})`.                                    |
| CustomWiggle  | Oscillation that returns to start. `CustomWiggle.create("wig",{wiggles:8, type:"easeOut"})`. Types: easeOut, easeInOut, anticipate, uniform, random. Also `amplitudeEase`, `timingEase`. |
| ExpoScaleEase | Makes scale tweens feel linear when values differ greatly (zooms). `ease:"expoScale(0.5, 7, power2.inOut)"`.                                                                             |
| RoughEase     | Jittery/shaky. `"rough({template:none.out, strength:1, points:20, taper:'none', randomize:true, clamp:false})"`.                                                                         |
| SlowMo        | Fast–slow–fast (slow middle). `"slow(0.7, 0.7, false)"` = (linearRatio, power, yoyoMode).                                                                                                |
| SteppedEase   | Now core: `"steps(12)"`. Sprite sheets, clocks, typewriter.                                                                                                                              |

```js
import { CustomEase } from "gsap/CustomEase";
import { CustomBounce } from "gsap/CustomBounce";   // requires CustomEase
import { CustomWiggle } from "gsap/CustomWiggle";   // requires CustomEase
import { ExpoScaleEase, RoughEase, SlowMo } from "gsap/EasePack";
gsap.registerPlugin(CustomEase, CustomBounce, CustomWiggle, ExpoScaleEase, RoughEase, SlowMo);

CustomBounce.create("ball", { strength: 0.7, squash: 2 });
gsap.timeline()
  .to(".ball", { y: 300, ease: "ball", duration: 1.5 })
  .to(".ball", { scaleX: 1.4, scaleY: 0.6, ease: "ball-squash", transformOrigin: "bottom", duration: 1.5 }, 0);

CustomWiggle.create("shake", { wiggles: 6, type: "easeOut" });
gsap.to(".input.error", { x: 10, ease: "shake", duration: 0.5 });

gsap.to(".map", { scale: 8, ease: "expoScale(1, 8, power1.inOut)" });
gsap.to(".sprite", { backgroundPosition: "-1200px 0", ease: "steps(12)", repeat: -1, duration: 1 });
```

## ScrollTrigger

Ties animations (or callbacks) to scroll position. Pinning, scrubbing, snapping, toggles, batching.

### Config properties

| Property                                                  | Notes                                                                                                                                                                     |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trigger                                                   | Element whose position defines start/end.                                                                                                                                 |
| start / end                                               | `"top 80%"` = trigger's top hits 80% down viewport. End may be `"+=500"`, `"bottom top"`, a function, or `"max"`. `clamp()` wraps prevent starting before page top.       |
| endTrigger                                                | Different element for the end.                                                                                                                                            |
| scrub                                                     | `true` or seconds of catch-up smoothing (e.g. `1`).                                                                                                                       |
| pin                                                       | `true` or element to pin.                                                                                                                                                 |
| pinSpacing                                                | Add padding so content after waits (default true; `"margin"` option).                                                                                                     |
| pinType                                                   | `"fixed"` or `"transform"`.                                                                                                                                               |
| pinReparent / pinSpacer / anticipatePin / pinnedContainer | Edge cases for pinning (stacking contexts, flicker, nested pins).                                                                                                         |
| toggleActions                                             | 4 actions for onEnter onLeave onEnterBack onLeaveBack. Default `"play none none none"`. Values: play, pause, resume, reset, restart, complete, reverse, none.             |
| toggleClass                                               | Add class while active: `"active"` or `{targets, className}`.                                                                                                             |
| snap                                                      | Number, array, `"labels"`, `"labelsDirectional"`, function, or `{snapTo, duration, delay, ease, directional, inertia}`.                                                   |
| markers                                                   | Debug markers. Remove before shipping.                                                                                                                                    |
| scroller                                                  | Custom scroll container.                                                                                                                                                  |
| horizontal                                                | Horizontal scroller.                                                                                                                                                      |
| once                                                      | Kill after first onEnter.                                                                                                                                                 |
| id                                                        | For `ScrollTrigger.getById`.                                                                                                                                              |
| invalidateOnRefresh                                       | Re-record values on refresh (needed for function-based values that depend on size).                                                                                       |
| refreshPriority                                           | Order of refresh when created out of page order.                                                                                                                          |
| containerAnimation                                        | Trigger on elements inside a horizontally-scrolling (fake) container tween.                                                                                               |
| fastScrollEnd                                             | Force completion when user scrolls past quickly.                                                                                                                          |
| preventOverlaps                                           | Complete previous trigger's animation before this one.                                                                                                                    |
| animation                                                 | Animation to control (when using `ScrollTrigger.create`).                                                                                                                 |
| callbacks                                                 | onEnter, onLeave, onEnterBack, onLeaveBack, onToggle, onUpdate, onRefresh, onRefreshInit, onScrubComplete, onSnapComplete. Each gets the ScrollTrigger instance (`self`). |

### Instance properties / methods

`self.progress`, `self.direction` (1/-1), `self.isActive`, `self.start`, `self.end`, `self.animation`, `self.trigger`, `self.pin`, `self.getVelocity()`, `self.scroll(v)`, `self.disable(revert)`, `self.enable()`, `self.kill()`, `self.refresh()`, `self.labelToScroll(label)`, `self.getTween()`, `self.previous()`, `self.next()`.

### Static methods

`ScrollTrigger.create()`, `batch(targets, vars)`, `refresh()`, `update()`, `getAll()`, `getById()`, `killAll()`, `config({limitCallbacks, ignoreMobileResize, autoRefreshEvents})`, `defaults()`, `scrollerProxy()` (third-party smooth scrollers), `normalizeScroll()` (mobile address-bar jank), `isInViewport(el, ratio)`, `positionInViewport(el, ref)`, `maxScroll(scroller)`, `addEventListener("refresh"|"refreshInit"|"scrollStart"|"scrollEnd"|"matchMedia")`, `clearScrollMemory()`, `saveStyles()`, `sort()`, `isScrolling()`, `observe()`.

```js
gsap.registerPlugin(ScrollTrigger);

// Reveal on enter
gsap.from(".card", {
  y: 60, autoAlpha: 0, stagger: 0.1,
  scrollTrigger: { trigger: ".cards", start: "top 80%", toggleActions: "play none none reverse" }
});

// Pinned, scrubbed story section
const tl = gsap.timeline({
  scrollTrigger: { trigger: ".story", start: "top top", end: "+=2000", scrub: 1, pin: true, snap: "labels" }
});
tl.addLabel("one").to(".slide1", { autoAlpha: 0 }).addLabel("two").from(".slide2", { yPercent: 100 }).addLabel("three");

// Horizontal scroll section
const panels = gsap.utils.toArray(".panel");
const scrollTween = gsap.to(panels, {
  xPercent: -100 * (panels.length - 1), ease: "none",
  scrollTrigger: { trigger: ".h-wrap", pin: true, scrub: 1, end: () => "+=" + document.querySelector(".h-wrap").offsetWidth }
});
// Trigger inside the horizontal section
gsap.to(".panel-3 h2", { rotation: 20, scrollTrigger: { trigger: ".panel-3", containerAnimation: scrollTween, start: "left center" } });

// Batch many elements efficiently
ScrollTrigger.batch(".grid-item", { onEnter: els => gsap.from(els, { autoAlpha: 0, y: 30, stagger: 0.05 }) });

// Progress bar
gsap.to(".progress", { scaleX: 1, ease: "none", scrollTrigger: { scrub: 0.3 } });
```

Create ScrollTriggers in page order (top to bottom), or set `refreshPriority`. Call `ScrollTrigger.refresh()` after images/fonts change layout. Never put a ScrollTrigger on a child tween inside a timeline; put it on the timeline.

## ScrollSmoother

Smooth scrolling built on native scroll (keeps accessibility, find-in-page) and integrated with ScrollTrigger. Requires ScrollTrigger and this markup:

```js
<div id="smooth-wrapper"><div id="smooth-content">...page...</div></div>

const smoother = ScrollSmoother.create({
  wrapper: "#smooth-wrapper", content: "#smooth-content",
  smooth: 1.2,            // seconds to catch up
  smoothTouch: 0.1,       // smoothing on touch (default 0 = native)
  effects: true,          // enable data-speed / data-lag attributes
  normalizeScroll: true,
  ignoreMobileResize: true,
  speed: 1,
  onUpdate: self => {}, onStop: self => {}, onFocusIn: (el, e) => {}
});

// Parallax via attributes
// <img data-speed="0.8">  <div data-lag="0.3">  data-speed="auto" for images in overflow containers
smoother.scrollTo(".contact", true, "top 100px");
```

Instance methods: `scrollTo(target, smooth, position)`, `scrollTop(v)`, `offset(el, position)`, `effects(targets, {speed, lag})`, `paused(bool)`, `smooth(v)`, `getVelocity()`, `progress`, `content()`, `wrapper()`, `scrollTrigger`, `kill()`. Static: `ScrollSmoother.get()`, `ScrollSmoother.refresh()`.

Skip ScrollSmoother on content-heavy, accessibility-critical sites, or when `position:fixed` elements must live inside the content (they won't stay fixed; put them outside the wrapper).

## SplitText

Splits text into chars/words/lines elements for animation. 3.13 rewrite: smaller, accessible by default, auto re-split on resize/font load, masking.

| Config                                                           | Notes                                                                                         |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| type                                                             | `"chars,words,lines"` (split only what you animate).                                          |
| charsClass / wordsClass / linesClass                             | Class names; `"char++"` adds incrementing numbers.                                            |
| mask                                                             | `"lines"`, `"words"` or `"chars"`: wraps each in an overflow-clip element for reveal effects. |
| autoSplit                                                        | Re-split when fonts load or width changes; use with `onSplit`.                                |
| onSplit(self)                                                    | Runs on each split; return your animation so it is reverted/recreated.                        |
| aria                                                             | `"auto"` (aria-label on parent, aria-hidden children), `"hidden"`, `"none"`.                  |
| deepSlice                                                        | Handle nested elements spanning lines.                                                        |
| ignore                                                           | Selector of children to leave unsplit.                                                        |
| propIndex                                                        | Add CSS vars like `--char: 3`.                                                                |
| reduceWhiteSpace / smartWrap / wordDelimiter / prepareText / tag | Fine control of output.                                                                       |

Properties: `chars`, `words`, `lines`, `masks`, `elements`, `isSplit`. Methods: `split(vars)`, `revert()`, `kill()`. Static: `SplitText.create(target, vars)`.

```js
SplitText.create(".headline", {
  type: "words,lines", mask: "lines", autoSplit: true,
  onSplit(self) {
    return gsap.from(self.lines, { yPercent: 100, duration: 0.8, stagger: 0.08, ease: "expo.out" });
  }
});
```

## Flip

Animate between two layout states (reorders, grid/list switch, moving an element to a new parent, shared-element transitions).

| Method                                                              | Notes                                                                                                                                                                                          |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Flip.getState(targets, {props, simple})                             | Record position/size (and extra CSS props).                                                                                                                                                    |
| Flip.from(state, vars)                                              | After DOM change, animate from recorded state. Vars: `duration, ease, absolute, nested, scale, simple, spin, targets, toggleClass, zIndex, fade, prune, onEnter, onLeave, props` + tween vars. |
| Flip.to(state, vars)                                                | Inverse: animate to a state.                                                                                                                                                                   |
| Flip.fit(el, target, vars)                                          | Resize/position one element to fit another.                                                                                                                                                    |
| Flip.isFlipping(el) / Flip.killFlipsOf(el)                          | —                                                                                                                                                                                              |
| Flip.makeAbsolute(targets)                                          | Convert to absolute positioning in place.                                                                                                                                                      |
| Flip.batch(id)                                                      | Coordinate multiple Flips across components.                                                                                                                                                   |
| state.getProperty / getElementState / makeAbsolute / update / clear | FlipState helpers. `data-flip-id` matches different elements across states.                                                                                                                    |

```js
const state = Flip.getState(".item");
container.classList.toggle("grid");          // change layout however you like
Flip.from(state, {
  duration: 0.6, ease: "power2.inOut", absolute: true, stagger: 0.03,
  onEnter: els => gsap.fromTo(els, { autoAlpha: 0, scale: 0 }, { autoAlpha: 1, scale: 1 }),
  onLeave: els => gsap.to(els, { autoAlpha: 0, scale: 0 })
});
```

## Draggable & InertiaPlugin

| Config                                                                                                | Notes                                                                                                                       |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| type                                                                                                  | `"x,y"`, `"x"`, `"y"`, `"rotation"`, `"top,left"`, `"scroll"`, `"scrollTop"`, `"scrollLeft"`.                               |
| bounds                                                                                                | Element, selector, or `{minX,maxX,minY,maxY}` / `{minRotation,maxRotation}`.                                                |
| inertia                                                                                               | Throw with momentum (needs InertiaPlugin). Object form: `{x:{velocity,end,min,max}}`.                                       |
| snap / liveSnap                                                                                       | Snap on release / during drag. Array, function, `{x, y, points, radius}`.                                                   |
| edgeResistance                                                                                        | 0–1 resistance beyond bounds.                                                                                               |
| throwResistance / maxDuration / minDuration / overshootTolerance / throwProps                         | Inertia tuning.                                                                                                             |
| trigger                                                                                               | Different element to start drag from (handle).                                                                              |
| handle (via trigger), cursor, activeCursor                                                            | UX.                                                                                                                         |
| lockAxis                                                                                              | Lock to the first axis moved.                                                                                               |
| dragClickables                                                                                        | Allow drag starting on links/buttons.                                                                                       |
| allowNativeTouchScrolling / allowContextMenu / allowEventDefault                                      | Touch/mouse behavior.                                                                                                       |
| dragResistance / minimumMovement / clickableTest / zIndexBoost / autoScroll / force3D / callbackScope | Misc tuning.                                                                                                                |
| callbacks                                                                                             | onPress, onDragStart, onDrag, onDragEnd, onRelease, onClick, onLockAxis, onThrowUpdate, onThrowComplete, onMove (+…Params). |

Instance props: `x, y, rotation, startX, startY, endX, endY, endRotation, deltaX, deltaY, pointerX, pointerY, minX, maxX, minY, maxY, isDragging, isPressed, isThrowing, lockedAxis, target, vars, tween, pointerEvent`.

Instance methods: `applyBounds()`, `disable()`, `enable()`, `enabled()`, `endDrag(e)`, `startDrag(e)`, `getDirection(from)`, `hitTest(target, threshold)`, `timeSinceDrag()`, `update(applyBounds)`, `kill()`, `addEventListener()`. Static: `Draggable.create()`, `Draggable.get(target)`, `Draggable.hitTest(a, b, threshold)`, `Draggable.timeSinceDrag()`, `Draggable.zIndex`.

```js
gsap.registerPlugin(Draggable, InertiaPlugin);
Draggable.create(".knob", {
  type: "rotation", inertia: true,
  snap: v => Math.round(v / 30) * 30,
  onDrag() { valueEl.textContent = Math.round(this.rotation); }
});
Draggable.create(".card", {
  bounds: ".table", inertia: true, edgeResistance: 0.65,
  onDragEnd() { if (this.hitTest(".bin", "50%")) gsap.to(this.target, { scale: 0 }); }
});

// InertiaPlugin on its own: glide to a stop from a tracked velocity
InertiaPlugin.track(".puck", "x");
gsap.to(".puck", { inertia: { x: "auto", resistance: 200 } }); // or {velocity, min, max, end}
// Static: InertiaPlugin.track(), untrack(), isTracking(), getVelocity()
```

## DrawSVG & MorphSVG

### DrawSVGPlugin

Animates the visible stroke segment (stroke-dasharray/offset) of path, line, polyline, polygon, rect, ellipse, circle. Value is "start end" in % or px; a single value means "0 value".

```js
gsap.from("#signature path", { drawSVG: 0, duration: 2, stagger: 0.2 });   // draw in
gsap.fromTo(".ring", { drawSVG: "0% 10%" }, { drawSVG: "90% 100%", repeat: -1, ease: "none" }); // moving segment
gsap.to(".line", { drawSVG: "50% 50%" });  // collapse to center
// DrawSVGPlugin.getLength(el), DrawSVGPlugin.getPosition(el)
// Add  vector-effect="non-scaling-stroke"  carefully; use "live" keyword if element resizes: drawSVG:"0% 100% live"
```

### MorphSVGPlugin

Morphs one shape's path data into another (shapes need not have matching points).

```js
MorphSVGPlugin.convertToPath("circle, rect, ellipse, line, polygon, polyline");
gsap.to("#play", { morphSVG: "#pause", duration: 0.5 });
gsap.to("#blob", { morphSVG: { shape: "#blob2", type: "rotational", shapeIndex: 3, origin: "50% 50%", map: "complexity", precision: 2 } });
```

Options: `shape`, `type` ("linear" \| "rotational"), `shapeIndex` (number, "auto", or array per sub-path; tune with `findShapeIndex()`), `map` ("size" \| "position" \| "complexity"), `origin`, `precision`, `render` (canvas callback), `updateTarget`, `smooth`, `curveMode`. Static: `convertToPath`, `pathDataToBezier`, `rawPathToString`, `stringToRawPath`, `defaultType`, `defaultMap`, `defaultUpdateTarget`.

## MotionPathPlugin & MotionPathHelper

```js
gsap.to(".plane", {
  duration: 5, ease: "power1.inOut",
  motionPath: {
    path: "#route",           // SVG path, selector, raw data, or array of points [{x,y},…]
    align: "#route",          // put the element on the path
    alignOrigin: [0.5, 0.5],
    autoRotate: true,         // or a degree offset, e.g. 90
    start: 0, end: 1,         // portion of the path
    curviness: 1.5,           // for point arrays
    type: "cubic"             // "thru" (default for arrays) | "cubic"
  }
});
// Utilities: MotionPathPlugin.getRawPath, cacheRawPathMeasurements, getPositionOnPath,
// sliceRawPath, convertToPath, convertCoordinates(from, to, point), getGlobalMatrix,
// getAlignMatrix, getRelativePosition, pointsToSegment, arrayToRawPath, stringToRawPath, rawPathToString

// MotionPathHelper: dev-only visual editor. Drag anchor points, then click "copy motion path".
MotionPathHelper.create(".plane", { path: "#route" });   // or pass the tween directly
// Options: path, pathColor, pathWidth, pathOpacity, selected, handleSize, draggable, onPress, onRelease
```

## Observer

Unified listener for wheel, touch, pointer and scroll with velocity and direction. Built into ScrollTrigger as `ScrollTrigger.observe()`. Use it for full-page "one-swipe-one-section" slideshows without real scrolling.

```js
Observer.create({
  target: window, type: "wheel,touch,pointer",
  wheelSpeed: -1, tolerance: 10, preventDefault: true,
  onDown: () => !animating && goTo(index - 1),
  onUp:   () => !animating && goTo(index + 1),
});
```

Config: `target, type, axis, lockAxis, tolerance, dragMinimum, debounce, capture, preventDefault, wheelSpeed, scrollSpeed, ignore, ignoreCheck, allowClicks, lineHeight`. Callbacks: `onUp, onDown, onLeft, onRight, onChange, onChangeX, onChangeY, onDrag, onDragStart, onDragEnd, onPress, onRelease, onClick, onHover, onHoverEnd, onMove, onWheel, onToggleX, onToggleY, onStop, onStopDelay, onLockAxis`. Instance: `deltaX, deltaY, velocityX, velocityY, x, y, isDragging, isPressed, event, enable(), disable(), kill()`. Static: `Observer.getAll()`, `Observer.getById()`.

## Physics2DPlugin & PhysicsPropsPlugin

Physics-based motion where the end point is not known; duration controls how long it runs.

```js
// Physics2D: angle + velocity + gravity/acceleration in 2D (confetti, particles)
gsap.to(".confetti", {
  duration: 2.5,
  physics2D: { velocity: "random(250, 500)", angle: "random(240, 300)", gravity: 600, friction: 0.02 }
});
// Props: velocity, angle, acceleration, accelerationAngle, gravity, friction, xProp, yProp

// PhysicsProps: independent per-property velocity/acceleration/friction
gsap.to(".wheel", { duration: 4, physicsProps: { rotation: { velocity: 720, friction: 0.15 }, x: { velocity: 300, acceleration: -60 } } });
```

## TextPlugin & ScrambleTextPlugin

```js
// TextPlugin: replace text character by character (or word by word)
gsap.to(".type", { duration: 2, text: { value: "Hello, world", delimiter: "", speed: 1, newClass: "new", oldClass: "old", padSpace: true, preserveSpaces: true, rtl: false, type: "diff" } });

// ScrambleTextPlugin: decode/scramble effect
gsap.to(".code", { duration: 1.5, scrambleText: { text: "ACCESS GRANTED", chars: "01", revealDelay: 0.3, speed: 0.4, newClass: "lit", tweenLength: true, rightToLeft: false, delimiter: "" } });
// chars presets: "upperCase", "lowerCase", "upperAndLowerCase", or any string of characters
```

## ScrollToPlugin

```js
gsap.to(window, { duration: 1, scrollTo: { y: "#pricing", offsetY: 80, autoKill: true } });
gsap.to(".list", { scrollTo: { y: "max" } });
gsap.to(window, { scrollTo: 400 });
// Props: x, y (number, selector, element, "max"), offsetX, offsetY, autoKill, onAutoKill
// Global: ScrollToPlugin.config({ autoKillThreshold: 7 })
// Note: with ScrollSmoother, use smoother.scrollTo() instead.
```

## EaselPlugin, PixiPlugin, GSDevTools

### EaselPlugin

Animates EaselJS (CreateJS) filter properties: `colorFilter`, `colorMatrixFilter` (saturation, contrast, hue, brightness, colorize, tint), plus `frame` for MovieClips. Legacy; only relevant if you still use CreateJS / Adobe Animate canvas output.

```js
gsap.registerPlugin(EaselPlugin); EaselPlugin.registerCreateJS(createjs);
gsap.to(circle, { duration: 1, easel: { colorMatrixFilter: { saturation: 0, brightness: 1.2 } } });
```

### PixiPlugin

Animate PixiJS display objects with friendly props: combined `scale`, `skew`, `positionX/Y`, `pivotX/Y`, `anchorX/Y`, degree-based `rotation`, colors (`tint`, `fillColor`, `lineColor`), and filters (`blur`, `brightness`, `contrast`, `saturation`, `hue`, `colorize`, `colorizeAmount`, `combineCMF`).

```js
PixiPlugin.registerPIXI(PIXI); gsap.registerPlugin(PixiPlugin);
gsap.to(sprite, { pixi: { x: 300, rotation: 90, scale: 1.5, tint: 0xff3366, blur: 4 } });
```

### GSDevTools

Dev-only scrubber UI: timeline bar, play/pause, loop, in/out points, speed, and a dropdown of animations by id. Remove before production.

```js
gsap.registerPlugin(GSDevTools);
GSDevTools.create({ animation: tl, globalSync: false, minimal: false, persist: true, paused: false, keyboard: true, loop: false, inTime: 0, outTime: 2, timeScale: 1, hideGlobalTimeline: true, container: "#tools", id: "intro" });
// Static: GSDevTools.getById(id); instance: kill()
```

## Utility methods (gsap.utils)

Most accept their final argument optionally; omit it and you get a reusable function (e.g. `const clamp01 = gsap.utils.clamp(0,1)`). `pipe` composes them.

| Utility                                         | Example                                                                                                 |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| checkPrefix(prop)                               | `checkPrefix("filter")` → vendor-prefixed name if needed.                                               |
| clamp(min, max, v)                              | `clamp(0, 100, 130)` → 100.                                                                             |
| distribute(config)                              | Spread values across an array of elements (base, amount, from, grid, ease). Basis of advanced staggers. |
| getUnit(v)                                      | `getUnit("30px")` → "px".                                                                               |
| interpolate(a, b, p)                            | Numbers, colors, strings, objects: `interpolate("red","blue",0.5)`.                                     |
| mapRange(inMin, inMax, outMin, outMax, v)       | Map mouse X to rotation.                                                                                |
| normalize(min, max, v)                          | → 0–1.                                                                                                  |
| pipe(...fns)                                    | `pipe(clamp(0,100), snap(5))`.                                                                          |
| random(min, max, snap?) / random(array)         | Also string form in vars: `x:"random(-100,100,5)"`.                                                     |
| selector(scope)                                 | Scoped query function: `const q = gsap.utils.selector(ref)`.                                            |
| shuffle(array)                                  | In-place shuffle.                                                                                       |
| snap(increment \| array \| {values, radius}, v) | Snap to grid or nearest value.                                                                          |
| splitColor(color, hsl?)                         | → \[r,g,b(,a)\] or \[h,s,l\].                                                                           |
| toArray(targets, scope?)                        | Selector/NodeList → Array.                                                                              |
| unitize(fn, unit)                               | Wrap a function so output gets a unit.                                                                  |
| wrap(min, max, v) / wrap(array, i)              | Loop values: infinite carousels.                                                                        |
| wrapYoyo(min, max, v)                           | Ping-pong wrap.                                                                                         |

```js
const { mapRange, clamp, pipe, snap, wrap, toArray } = gsap.utils;
const toRotation = pipe(mapRange(0, innerWidth, -30, 30), snap(1));
addEventListener("pointermove", e => gsap.to(".dial", { rotation: toRotation(e.clientX) }));

// Infinite marquee with wrap + modifiers
const wrapX = wrap(-100, 400);
gsap.to(".tile", { x: "+=500", duration: 10, ease: "none", repeat: -1, modifiers: { x: x => wrapX(parseFloat(x)) + "px" } });

gsap.to(toArray(".star"), { color: "random([#fc0, #f60, #f36])", x: "random(-50, 50)" });
```

## Staggers

```js
gsap.to(".dot", { y: -20, stagger: 0.1 });            // simple: 0.1s between each

gsap.to(".cell", {
  scale: 0.2,
  stagger: {
    each: 0.05,          // or amount: 1 (total spread time)
    from: "center",      // "start" | "end" | "center" | "edges" | "random" | index | [x, y] ratios
    grid: "auto",        // or [rows, cols] for 2D distance
    axis: "x",           // limit grid distance to one axis
    ease: "power2.in",   // distributes start times
    repeat: -1, yoyo: true  // per-element repeat (lives inside stagger object)
  }
});

// Function stagger: full control
gsap.to(".bar", { height: 100, stagger: (i, target, list) => i * 0.05 + Math.random() * 0.1 });
```

Put `repeat`/`yoyo` inside the stagger object to make each element loop on its own; on the outer vars they repeat the whole group.

## Sequencing animations

| Position               | Meaning                                           |
|------------------------|---------------------------------------------------|
| (omitted)              | At the end of the timeline.                       |
| 1                      | Absolute: 1 second in.                            |
| "+=1"                  | 1s after the end (gap).                           |
| "-=1"                  | 1s before the end (overlap).                      |
| "\<"                   | Start of the previous child.                      |
| "\>"                   | End of the previous child.                        |
| "\<0.3" / "\>-0.2"     | Relative to previous start / end.                 |
| "\<25%" / "\>50%"      | Percentage of the previous child's duration.      |
| "label" / "label+=0.5" | At or relative to a label (created if missing).   |
| "+=50%"                | Percent of the inserted animation's own duration. |

Patterns: chain with method calls; build sections as functions that return timelines and nest them; use labels for chapters; use `tweenFromTo` to play segments; avoid chained `delay` math or `onComplete` pyramids.

## Control & callbacks

```js
const anim = gsap.to(".box", { x: 300, paused: true, onComplete: done, onCompleteParams: ["box"] });
btnPlay.onclick    = () => anim.play();
btnPause.onclick   = () => anim.pause();
btnReverse.onclick = () => anim.reversed() ? anim.play() : anim.reverse();
btnToggle.onclick  = () => anim.paused(!anim.paused());
slider.oninput     = e => anim.progress(e.target.value / 100);
anim.timeScale(2);                 // double speed
anim.eventCallback("onUpdate", () => console.log(anim.progress()));

// Hover in/out with one tween: reverse instead of creating new tweens
const hover = gsap.to(".btn", { scale: 1.06, paused: true, duration: 0.2 });
btn.addEventListener("mouseenter", () => hover.play());
btn.addEventListener("mouseleave", () => hover.reverse());

// Global
gsap.globalTimeline.pause();
gsap.ticker.lagSmoothing(0);       // when syncing with another loop (e.g. Lenis)
```

Callback order: `onStart` (first time playhead moves off 0) → `onUpdate` (every render) → `onRepeat` → `onComplete`. Reversing to 0 fires `onReverseComplete`. Killed or overwritten mid-flight fires `onInterrupt`. Inside callbacks `this` is the animation (use regular functions, not arrows, to access it).

## React, cleanup & accessibility

```js
npm i @gsap/react
import { useGSAP } from "@gsap/react";
gsap.registerPlugin(useGSAP);

function Hero() {
  const root = useRef(null);
  const { contextSafe } = useGSAP(() => {
    gsap.from(".title", { y: 40, autoAlpha: 0 });         // selector scoped to root
  }, { scope: root, dependencies: [], revertOnUpdate: false });

  const onClick = contextSafe(() => gsap.to(".title", { rotation: "+=10" })); // event handlers must be wrapped
  return <section ref={root}><h1 className="title" onClick={onClick}>Hi</h1></section>;
}

// Reduced motion + responsive in one place
const mm = gsap.matchMedia();
mm.add({ isDesktop: "(min-width: 800px)", reduce: "(prefers-reduced-motion: reduce)" }, ctx => {
  const { isDesktop, reduce } = ctx.conditions;
  gsap.from(".panel", { x: reduce ? 0 : isDesktop ? 200 : 50, autoAlpha: 0, duration: reduce ? 0 : 1 });
});
```

Common gotchas: register plugins once; avoid `from()` on the same element twice (it reads the already-animated value; use `fromTo`); set `overwrite:"auto"` for rapid-fire interactions; never animate the same property from CSS transitions and GSAP at once; kill/revert on unmount.

Source: gsap.com/docs/v3 (GSAP 3.13). Verify property names against the docs when upgrading versions.

