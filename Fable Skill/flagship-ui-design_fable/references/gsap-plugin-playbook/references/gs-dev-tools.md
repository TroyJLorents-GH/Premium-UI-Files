# GSDevTools

Source: supplied `GSAP Plugins.md`, lines 1980–2052, original heading: GSDevTools.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Treat this as development tooling. Decide explicitly whether playback/debug controls belong in the delivered user interface.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


[GSDEevTools quick start plugin](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/GSDevTools.min.js)

#### GSDevTools prompts (methods -> GSDevTools.create() ) 

I'm working with a GSAP demo from the GSAP docs: "GSDevTools - Step 1: Load and Instantiate with default settings".
A demo explaining the basics of GSDevTools.
Visit https://greensock.com/gsdevtools for more info.

GSDevTools gives you a visual UI for interacting with and debugging GSAP animations, complete with advanced playback controls, keyboard shortcuts, global synchronization and more. Jump to specific scenes, set in/out points, play in slow motion to reveal intricate details, and even switch to a "minimal" mode on small screens.
Docs page: https://gsap.com/docs/v3/Plugins/GSDevTools
CodePen: https://codepen.io/GreenSock/pen/611c82e0d3531b431617f8adbfeb71fd
GSAP plugins used: GSDevTools

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/GSDevTools.min.js

Stylesheets it loads:
- /demo-assets/pens/JGaKdQ.css

HTML:
```html
<div class="boxes">
  <div class="box green"></div>
  <div class="box orange"></div>
  <div class="box purple"></div>
</div>
```

CSS:
```css
/* Global styles come from external css https://codepen.io/GreenSock/pen/JGaKdQ*/

body{display:flex;align-items:center;justify-content:center;min-height:100vh;}

.boxes {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width:100vw;
  margin-bottom: 100px;
}


.box {
  width: 50px;
  height: 50px;
}
```

JS:
```js
//timeline animates green and orange
var tl = gsap.timeline()
tl.to(".orange", {duration: 1, x: "100vw", xPercent: -100})
  .to(".green", {duration: 2, x: "100vw", xPercent: -100, ease:"bounce"})

//separate tween with a delay which makes it play after the timeline
gsap.to(".purple", {duration: 1, x: "100vw", xPercent: -100, rotation: 360, delay: 3})

//instantiate GSDevTools with default settings
GSDevTools.create();

// GSDevTools will control all animations on the Global Timeline
```

Explain how this demo works, then help me adapt it for my own project.

---

