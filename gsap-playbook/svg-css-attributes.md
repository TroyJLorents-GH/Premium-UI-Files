# SVG CSS properties and attributes

Source: supplied `GSAP Plugins.md`, lines 5917–6039, original heading: Prompt 3.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Original SVG Prompt3. The source declares playBtn but uses play.onclick, relying on implicit browser globals. Use the explicitly queried element.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


I'm working with a GSAP demo from the GSAP docs: "SVG CSSPlugin and AttrPlugin".
to be embedded in blog post
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/907579916ec09b51ff63459d6894da5e

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css

HTML:
```html
<svg version="1.1" id="demo" xmlns="http://www.w3.org/2000/svg" width="600px" height="207px" viewBox="0 0 600 207">
  <defs>
    <linearGradient id="stroke-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0.19" stop-color="#ff8709"/>
      <stop offset="0.73" stop-color="#f7bdf8"/>
    </linearGradient>
  </defs>
  <circle id="cssCircle" class="element" cx="57.464" cy="89.464" r="30.131"/>
  <circle id="attrCircle" class="element" cx="358" cy="89.464" r="30.131"/>
  <text transform="matrix(1 0 0 1 32.3333 27)" class="label">CSSPlugin</text>
  <text transform="matrix(1 0 0 1 327.8688 27)" class="label">AttrPlugin</text>
  <rect id="attrRectangle" x="327.869" y="145.667" class="element" width="134" height="49.333" rx="0"/>
  <line class="rule" x1="300" y1="46.595" x2="300" y2="192.595"/>
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

.element {
  fill: none;
  stroke: url(#stroke-gradient);
  stroke-width: 4px;
}

.label {
  font-family: Mori, sans-serif;
  font-size: 12px;
  fill: var(--light);
}

.rule {
  fill: none;
  stroke: var(--surface25);
  stroke-width: 1px;
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
var cssCircle = document.getElementById("cssCircle"),
    attrCircle = document.getElementById("attrCircle"),
    attrRectangle = document.getElementById("attrRectangle"),
    playBtn = document.getElementById("play"),
		tl = gsap.timeline({repeat:1, yoyo:true, repeatDelay:0.5, paused:true, defaults:{duration: 1}}); 

tl.to(cssCircle, {x:120, scale:2})
  .to(cssCircle, {duration: 0.5, strokeWidth:12, stroke:"white"})
  .to(attrCircle, {attr:{cx:500}})
  .to(attrCircle, {attr:{r:50}})
  .to(attrRectangle, {attr:{rx:"30"}});

play.onclick = function() {
  tl.restart();
}
```

Explain how this demo works, then help me adapt it for my own project.


