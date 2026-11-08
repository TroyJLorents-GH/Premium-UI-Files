# Moving stroke windows through an SVG maze

Source: supplied `GSAP Plugins.md`, lines 6796–6954, original heading: Prompt 8 animation snake in a maze effect.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Original SVG Prompt8. DrawSVG technique, not a separate plugin.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


I'm working with a GSAP demo from the GSAP docs: "SVG Tips: DrawSVGPlugin Values".
Demonstrates the various types of values that can be passed to GSAP's DrawSVGPlugin. This pen is used on the DrawSVGPlugin product page.
Learn more at www.greensock.com/drawSVG
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/GJpGdm
GSAP plugins used: DrawSVGPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/DrawSVGPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<p>DrawSVGPlugin Values</p>

<svg version="1.1"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 width="300" viewBox="0 0 516.3 190" style="enable-background:new 0 0 516.3 211.99;"
	 xml:space="preserve">
  <defs>
    <linearGradient id="svg-gradient" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0.19" stop-color="#ff8709"/>
      <stop offset="0.73" stop-color="#f7bdf8"/>
    </linearGradient>
  </defs>
  <path id="template" d="M9.13,99.99c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
	<path id="path" d="M9.13,99.99c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
</svg>

<div id="code">drawSVG:<div id="current">"100%"</div></div>
<button id="next">Next Example</button>
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
  --surface75: #bbbaa6;
  --surface50: #7c7c6f;
  --surface25: #42433d;
}

body {
  background-color: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
  font-weight: 400;
  text-align: center;
}

p {
  font-family: Mori, sans-serif;
}

#template, #path {
  fill: none;
}
#template {
  stroke-width: 5px;
  stroke: var(--surface25);
}
#path {
  stroke: url(#svg-gradient);
  stroke-width: 20px;
  visibility: hidden;
}
#code, #value {
  font-size: 20px;
  font-family: Fraktion Mono, monospace;
}
#code {
  color: var(--surface50);
  margin: 20px;
  position: relative;
  visibility: hidden;
}
#current {
  display: inline-block;
  color: var(--light);
}
#description {
  max-width: 530px;
  color: var(--surface50);
  font-family: Mori, sans-serif;
  font-size: 24px;
  display: inline-block;
  text-align: left;
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
gsap.registerPlugin(DrawSVGPlugin);

var values = "100%;40% 60%;20 350;50% 50%;true;10%".split(";"),
    currentIndex = 0;

//set the initial value
gsap.set("#path", {visibility:"visible"});
gsap.set("#code", {visibility:"visible"});

function next() {

  gsap.killTweensOf(next); //in case the user clicks, clear any delayed calls to this method.
  if (++currentIndex === values.length) {
    currentIndex = 0;
  }
  if (values[currentIndex] === "true") {
    gsap.set("#current", {innerText:(values[currentIndex]), ease:"none"});
  } else {
    gsap.set("#current", {innerText:('"' + values[currentIndex] + '"'), ease:"none"});
  }
  gsap.to("#path", {duration: 1, drawSVG:values[currentIndex], ease:"power1.inOut"});

}

document.getElementById("next").addEventListener("click", next);
```

Explain how this demo works, then help me adapt it for my own project.

