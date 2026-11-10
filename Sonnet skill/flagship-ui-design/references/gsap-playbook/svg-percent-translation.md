# SVG percentage translation

Source: supplied `GSAP Plugins.md`, lines 6040–6146, original heading: Prompt 4.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Original SVG Prompt4. Declare tl locally and use playBtn rather than the implicit play browser global.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


I'm working with a GSAP demo from the GSAP docs: "SVG Percent-based translation".
to be embedded in blog post
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/f3acfdfb2847f7f79d1d4817cc0f3ecd

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css

HTML:
```html
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" width="600px" height="205.061px" viewBox="0 0 600 205.061">
  <defs>
    <linearGradient id="box-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0.19" stop-color="#ff8709"/>
      <stop offset="0.73" stop-color="#f7bdf8"/>
    </linearGradient>
  </defs>
  <line class="rule" x1="181.223" y1="0" x2="181.223" y2="205.061"/>
  <rect id="test" x="18.24" y="11.245" class="box" width="163.319" height="38.865"/>
  <rect x="53.611" y="58.843" class="box" width="127.948" height="38.865"/>
  <rect x="105.14" y="107.314" class="box" width="76.419" height="38.865"/>
  <rect x="142.694" y="154.773" class="box" width="38.865" height="38.865"/>
</svg><br>
<button id="play">play</button>
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

:root {
  --dark: #0e100f;
  --light: #fffce1;
  --grey: #191919;
  --surface75: #bbbaa6;
  --surface25: #42433d;
}

body {
  margin-top: 10px;
  background: var(--dark);
  text-align: center;
  color: var(--surface75);
  font-family: Mori, sans-serif;
}

svg {
  max-width: 100%;
  height: auto;
  background: var(--grey);
  border-radius: 12px;
  margin-bottom: 10px;
}

.rule {
  stroke: var(--surface25);
  stroke-miterlimit: 10;
}

.box {
  fill: url(#box-gradient);
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
var playBtn = document.getElementById("play")
    tl = gsap.timeline({repeat:1, yoyo:true, paused:true});

tl.to("rect", {duration:0.5, xPercent:100, stagger:0.4});



play.onclick = function() {
  tl.restart();
}
```

Explain how this demo works, then help me adapt it for my own project.

