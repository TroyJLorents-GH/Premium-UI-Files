# SVG transform origins and smoothOrigin

Source: supplied `GSAP Plugins.md`, lines 5626–5916, original heading: Prompt 2.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Original SVG Prompt2.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


I'm working with a GSAP demo from the GSAP docs: "smoothOrigin demo".
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/053d0ee8da31db3bdca1a4531e0628ee
GSAP plugins used: TextPlugin

Scripts it loads, in order:
- //cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js
- //cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/TextPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css
- //ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css

HTML:
```html
<div id="wrapper">
  <div class="overlay" id="overlay1"><code>smoothOrigin:true</code><br>element doesn't jump when origin changes.</div>
  <div class="overlay" id="overlay2"><code>smoothOrigin:false</code><br>element jumps when origin changes.</div>
  <div class="bottomOverlay"><h2 id="transform"></h2></div>

  <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="800px" height="300px" viewBox="0 0 800 300">
    <defs>
      <linearGradient id="true-gradient" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0.19" stop-color="#ff8709"/>
        <stop offset="0.73" stop-color="#f7bdf8"/>
      </linearGradient>
      <linearGradient id="false-gradient" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0.21" stop-color="#f7bdf8"/>
        <stop offset="0.82" stop-color="#cd237f"/>
      </linearGradient>
    </defs>

    <g id="boxFalseGhost" class="box">
      <rect x="420" y="100" class="false ghost" width="50" height="50"/>
      <g>
        <g>
          <path d="M430.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C431.277,135.167,430.669,133.738,430.669,131.898z"/>
          <path d="M447.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C448.309,137.562,447.829,137.307,447.829,136.794z M451.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="430.459,118.931 444.481,110.931 458.503,118.931"/>
      </g>
    </g>

    <g id="boxTrueGhost" class="box">
      <rect y="100" class="true ghost" width="50" height="50"/>
      <g>
        <g>
          <path d="M10.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C11.277,135.167,10.669,133.738,10.669,131.898z"/>
          <path d="M27.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C28.309,137.562,27.829,137.307,27.829,136.794z M31.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="10.459,118.931 24.481,110.931 38.503,118.931"/>
      </g>
    </g>

    <g id="boxFalse" class="box">
      <rect x="420" y="100" class="false" width="50" height="50"/>
      <g>
        <g>
          <path d="M430.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C431.277,135.167,430.669,133.738,430.669,131.898z"/>
          <path d="M447.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C448.309,137.562,447.829,137.307,447.829,136.794z M451.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="430.459,118.931 444.481,110.931 458.503,118.931"/>
      </g>
      <circle class="originMarker" cx="422.5" cy="102.5" r="2.5"/>
    </g>

    <g id="boxTrue" class="box">
      <rect y="100" class="true" width="50" height="50"/>
      <g>
        <g>
          <path d="M10.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C11.277,135.167,10.669,133.738,10.669,131.898z"/>
          <path d="M27.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C28.309,137.562,27.829,137.307,27.829,136.794z M31.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="10.459,118.931 24.481,110.931 38.503,118.931"/>
      </g>
      <circle class="originMarker" cx="2.5" cy="102.5" r="2.5"/>
    </g>
  </svg>

  <div class="nav">
    <input type="range" id="slider" min="0" max="100" step="0.02" value="0">
    <button id="play">restart</button>
  </div>
</div>

<p>Initial scale of the boxes is <code>scale:2</code> with their transform origin in the upper left corner,
<code>transformOrigin:"left top"</code>. The white dots indicate the transformOrigin position.</p>
<p><code>smoothOrigin:false</code> is actually the "proper" implementation based on the SVG and CSS specs, but <code>smoothOrigin:true</code> looks more natural and smooth.</p>
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
  --orange: #ff8709;
}

body {
  margin: 0;
  padding: 12px;
  background: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
  font-size: 16px;
}

p {
  max-width: 75ch;
  margin: 1rem auto;
  text-align: center;
  line-height: 1.5;
}

code {
  background-color: #28292b;
  color: var(--light);
  padding: 2px 4px;
  border-radius: 5px;
  font-family: Fraktion Mono, monospace;
  font-size: 0.9em;
}

#wrapper {
  position: relative;
  width: 800px;
  margin: auto;
}

svg {
  display: block;
  background: var(--grey);
  border-radius: 12px;
}

.true { fill: url(#true-gradient); }
.false { fill: url(#false-gradient); }
.ghost { opacity: 0.3; }

/* "UP" label and arrow inside each box */
.box path,
.box polygon {
  fill: var(--dark);
}

.originMarker {
  fill: var(--light);
  stroke: var(--dark);
  stroke-width: 1px;
}

.overlay {
  position: absolute;
  top: 10px;
  left: 10px;
  line-height: 1.6;
}

#overlay2 {
  left: 420px;
}

.bottomOverlay {
  position: absolute;
  top: 250px;
  width: 800px;
  text-align: center;
}

.bottomOverlay h2 {
  margin: 0;
  color: var(--light);
  font-family: Fraktion Mono, monospace;
  font-size: 1.1rem;
  font-weight: 400;
}

.nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin: 20px auto;
}

#slider {
  width: 400px;
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

//CSSPlugin.defaultSmoothOrigin = false;
var boxTrue = document.getElementById("boxTrue");
var boxFalse = document.getElementById("boxFalse");
var boxTrueGhost = document.getElementById("boxTrueGhost");
var text = document.getElementById("transform");
var originMarkers = document.querySelectorAll(".originMarker");
var slider = document.getElementById("slider");

var tl = gsap.timeline({onUpdate:updateSlider, paused:true, defaults:{duration: 0.5}});

tl.add("scaleUp1")
  .set(text, {text:'transformOrigin:"left top"'})
  .to(boxTrue, {scale:2}, "scaleUp1")
  .to(boxFalse, {scale:2}, "scaleUp1")
  .set(originMarkers, {x:"-50%", y:"-50%"}, "scaleUp1+=-0.01")

  .add("rotate1")
  .set(originMarkers, {x:25, y:25}, "rotate1") //move them inside box so they don't alter bounds / transformOrigin of boxes
  .set(text, {text:'transformOrigin:"right bottom"'}, "rotate1")
  .to(boxTrue, {rotation:"+=90", transformOrigin:"right bottom"}, "rotate1")
  .to(boxFalse, {rotation:"+=90", transformOrigin:"right bottom", smoothOrigin:false}, "rotate1")
  .set(originMarkers, {x:50, y:50}, "rotate1")

  .add("rotate2")
  .set(originMarkers, {x:25, y:25}, "rotate2")
  .set(text, {text:'transformOrigin:"right top"'}, "rotate2")
  .to(boxTrue, {rotation:"+=90", transformOrigin:"right top"}, "rotate2")
  .to(boxFalse, {rotation:"+=90", transformOrigin:"right top", smoothOrigin:false}, "rotate2")
  .set(originMarkers, {x:50, y:0}, "rotate2")

  .add("rotate3")
  .set(originMarkers, {x:25, y:25}, "rotate3")
  .set(text, {text:'transformOrigin:"left top"'}, "rotate3")
  .to(boxTrue, {rotation:"+=90", transformOrigin:"left top"}, "rotate3")
  .to(boxFalse, {rotation:"+=90", transformOrigin:"left top", smoothOrigin:false}, "rotate3")
  .set(originMarkers, {x:0, y:0}, "rotate3");

tl.timeScale(0.3);
gsap.set(".box", {y:45});
gsap.set([boxTrue, boxTrueGhost], {x:10});

document.getElementById("play").addEventListener("click", function() {
  tl.restart();
});

//--- SLIDER ---
slider.addEventListener("input", function() {
  tl.progress(slider.value / 100).pause();
});

function updateSlider() {
  slider.value = tl.progress() * 100;
}
```

Explain how this demo works, then help me adapt it for my own project.


