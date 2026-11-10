# SVG transforms and timeline choreography

Source: supplied `GSAP Plugins.md`, lines 5424–5625, original heading: Prompt 1.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Original SVG Prompt1. Check all control dependencies in the JS and stylesheet metadata before extracting a standalone demo.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material

I'm working with a GSAP demo from the GSAP docs: "SVG + CSS Transform Timeline".
Demonstrates some of the inconsistencies in the ways various browsers apply CSS transforms to SVG elements. GSAP now solves these problems, as of version 1.14.2.
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/17b4f47aa28f02e305dab386e9f79e89
GSAP plugins used: TextPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/TextPlugin.min.js

Stylesheets it loads:
- //ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css

HTML:
```html
<div class="demo">
  <div class="cell">
    <h2>SVG &lt;rect&gt;</h2>
    <svg id="svg" class="container" width="260" height="200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 200">
      <defs>
        <linearGradient id="rect-gradient" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0.19" stop-color="#ff8709"/>
          <stop offset="0.73" stop-color="#f7bdf8"/>
        </linearGradient>
      </defs>
      <rect id="svgRectangle" class="animated" x="20" y="60" width="220" height="80" fill="url(#rect-gradient)"/>
    </svg>
  </div>
  <div class="cell">
    <h2>&lt;div&gt;</h2>
    <div class="container" style="width:260px; height:200px; position:relative;">
      <div id="divRectangle" class="animated"></div>
    </div>
  </div>
</div>

<div id="nav">
  <h3 id="message"></h3>
  <div class="controls">
    <input type="range" id="slider" min="0" max="1" step="0.001" value="0">
    <button id="play">play</button>
  </div>
</div>
```

CSS:
```css
@font-face {
  font-display: block;
  font-family: Mori;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}

@font-face {
  font-display: block;
  font-family: Fraktion Mono;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

:root {
  --dark: #0e100f;
  --light: #fffce1;
  --grey: #191919;
  --surface75: #bbbaa6;
  --surface25: #42433d;
  --orange: #ff8709;
}

body {
  margin: 0;
  padding: 18px;
  background-color: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
}

.demo {
  display: flex;
  justify-content: center;
  gap: 18px;
}

.cell {
  text-align: center;
}

h2 {
  margin: 5px 0 0.3em;
  color: var(--light);
  font-family: Fraktion Mono, monospace;
  font-size: 2rem;
  font-weight: 400;
  line-height: 1;
}

.container {
  display: block;
  overflow: hidden;
  background: var(--grey);
  border: 1px solid var(--surface25);
  border-radius: 12px;
}

#divRectangle {
  position: absolute;
  width: 220px;
  height: 80px;
  top: 60px;
  left: 20px;
  background: linear-gradient(90deg, #ff8709 19%, #f7bdf8 73%);
}

#nav {
  width: 560px;
  max-width: 100%;
  margin: 0 auto;
}

#message {
  min-height: 1.5em;
  color: var(--light);
  font-family: Fraktion Mono, monospace;
  font-size: 1rem;
  font-weight: 400;
}

.controls {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

#slider {
  flex: 1;
  accent-color: var(--orange);
}

button {
  background: var(--dark);
  border: solid 2px var(--surface75);
  color: var(--surface75);
  border-radius: 99px;
  padding: 12px 25px;
  cursor: pointer;
  line-height: 1;
  font-family: inherit;
  font-size: 0.9rem;
}
button:hover {
  border-color: var(--light);
  color: var(--light);
}
```

JS:
```js
gsap.registerPlugin(TextPlugin);
gsap.defaults({ smoothOrigin: false });

const elements = "#svgRectangle, #divRectangle";
const message = "#message";
const slider = document.getElementById("slider");

const tl = gsap.timeline({
  paused: true,
  defaults: { duration: 1 },
  onUpdate: () => (slider.value = tl.progress())
});

// both elements use the exact same tweens
tl.set(message, { text: '{rotation:360, transformOrigin:"50% 50%"}' })
  .to(elements, { rotation: 360, transformOrigin: "50% 50%" }, "+=1")
  .set(message, { text: '{rotation:"+=360", transformOrigin:"right bottom"}' }, "+=1")
  .to(elements, { rotation: "+=360", transformOrigin: "right bottom" })
  .set(message, { text: '{scale:0, transformOrigin:"0px 0px"}' }, "+=1")
  .to(elements, { scale: 0, transformOrigin: "0px 0px" })
  .set(message, { text: '{scale:1, transformOrigin:"100% 0%"}' }, "+=1")
  .to(elements, { scale: 1, transformOrigin: "100% 0%" })
  .set(message, { text: '{scaleY:0, transformOrigin:"0% 50%"}' }, "+=1")
  .to(elements, { scaleY: 0, transformOrigin: "0% 50%" })
  .set(message, { text: '{scale:1, transformOrigin:"50% bottom"}' }, "+=1")
  .to(elements, { scale: 1, transformOrigin: "50% bottom" })
  .set(message, { text: '{scale:0.5, rotation:360, transformOrigin:"50% 50%"}' }, "+=1")
  .to(elements, { scale: 0.5, rotation: 360, transformOrigin: "50% 50%" });

// --- SLIDER ---
slider.addEventListener("input", () => tl.progress(slider.value).pause());

// --- PLAY ---
document.getElementById("play").addEventListener("click", () => {
  tl.progress() === 1 ? tl.restart() : tl.play();
});
```

Explain how this demo works, then help me adapt it for my own project.

