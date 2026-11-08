# MorphSVGPlugin

Source: supplied `GSAP Plugins.md`, lines 2492–2740, original heading: MorphSVG.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** The first diamond-to-lightning demo is repeated under SVG Prompt9. A separate example renders a morph to canvas.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


[MorphSVG CDN Link](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/MorphSVGPlugin.min.js)

#### Example 1

> MorphSVG morphs an SVG <path> by animating the data inside the d attribute. For example, you can morph a diamond into a lightning bolt with a single line of code:

I'm working with a GSAP demo from the GSAP docs: "MorphSVG - simple morph".
Docs page: https://gsap.com/docs/v3/Plugins/MorphSVGPlugin
CodePen: https://codepen.io/GreenSock/pen/vEGpawb
GSAP plugins used: MorphSVGPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MorphSVGPlugin.min.js

HTML:
```html
<svg id="svg-stage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <path id="diamond" fill="url(#grad)" d="M50,1l49,49L50,99L1,50L50,1z" />
  <path id="lightning" fill="transparent" d="M47.1,0.8 73.3,0.8 61.9,37.2 77.1,37.2 30.7,99.4 45.8,51.9 29,51.9z" />
</svg>














<svg id="gradient" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
  <defs>
    <linearGradient id="grad" x1="0" y1="0" x2="99" y2="99" gradientUnits="userSpaceOnUse">
      <stop offset="0.2" stop-color="rgb(255, 135, 9)" />
      <stop offset="0.7" stop-color="rgb(247, 189, 248)" />
    </linearGradient>
  </defs>
</svg>
```

CSS:
```css
body {
  margin:0;
  padding:0;
  width:100%;
  height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  background: #0e100f;
  overflow: hidden;
}

.container {
  position: relative;
  width: 90vw;
  height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  border-radius: 9px;
}

#svg-stage {
  width:60%;
  max-height:60vh;
  max-width:500px;
  overflow:visible;
}

#gradient {
  height: 0;
}
```

JS:
```js
gsap.to("#diamond", {
  morphSVG: "#lightning",
  duration: 2,
  ease: "expo.inOut",
  repeat: -1,
  yoyo: true
});
```

Explain how this demo works, then help me adapt it for my own project.


#### Example 2 Prompt

> Morph into multiple shapes

> Rendering to canvas
> SVG is fantastic, but sometimes developers prefer a canvas-based animation (often for rendering performance reasons). The MorphSVG plugin allows you to define a render function that'll be called every time the path updates.



I'm working with a GSAP demo from the GSAP docs: "Canvas Morphing".
Using GreenSock's MorphSVG Plugin to do morphing on the canvas.
Docs page: https://gsap.com/docs/v3/Plugins/MorphSVGPlugin
CodePen: https://codepen.io/GreenSock/pen/WYWZab
GSAP plugins used: MorphSVGPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MorphSVGPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="container">
  <h2>Canvas</h2>
  <canvas></canvas>
</div>

<div class="container">
  <h2>SVG</h2>

<div class="container">
  <svg id="svg-stage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
    <defs>
      <linearGradient id="grad" x1="0" y1="0" x2="99" y2="99" gradientUnits="userSpaceOnUse">
        <stop offset="0.2" stop-color="rgb(255, 135, 9)" />
        <stop offset="0.7" stop-color="rgb(247, 189, 248)" />
      </linearGradient>
      <path id="shape2" d="M20,1 85,1 85,66 51,98 51,66 20,66z">
        <path id="shape3" d="M47.1,0.8 73.3,0.8 61.9,37.2 77.1,37.2 30.7,99.4 45.8,51.9 29,51.9z" />
        <path id="shape4" d="M50,1l49,49L50,99L1,50L50,1z" />
    </defs>

    <path id="shape1" fill="url(#grad)" d="M74.6 50.2h-.2v-.4h.2a24.4 24.4 0 1 0-24.4-24.4v.2h-.4v-.2a24.4 24.4 0 1 0-24.4 24.4h.2v.4h-.2a24.4 24.4 0 1 0 24.4 24.4v-.2h.4v.2a24.4 24.4 0 1 0 24.4-24.4z" />
  </svg>

</div>
```

CSS:
```css
body {
  width:100%;
  height:100vh;
  margin:0;
  padding:0;
  background:#0e100f;
  display:flex;
  align-items:center;
  justify-content:center;
  flex-wrap: wrap;
  gap:1rem;
}

.container svg, canvas {
  width: 200px;
  height: 200px;  
}

.container {
  display: inline-block;  
  text-align: center;
  visibility: hidden;
}
```

JS:
```js
let shape    = document.querySelector("#shape1");
let canvas   = document.querySelector("canvas");
let ctx      = canvas.getContext("2d");
let size     = 200;
let viewBox  = {x:0, y:0, width:100, height:100};
let sizeRatio = size / viewBox.width;

const gradient = ctx.createLinearGradient(0, 0, viewBox.width, viewBox.height);
gradient.addColorStop(0.2, "rgb(255, 135, 9)");
gradient.addColorStop(0.7, "rgb(247, 189, 248)");

setDisplay();

gsap.defaults({ease: "power2.inOut"});
gsap.set(".container", { autoAlpha: 1 });

//set a default render function for all morphSVG animations. You can set it on a per-animation basis too, like morphSVG:{shape:"#id", render:yourFunction}
// MorphSVGPlugin.defaultRender = draw;

var tl = gsap.timeline({ repeat: -1, id:"morphing", paused:false,  defaults: { duration: 2, ease: "expo.inOut" }})  
  .to(shape, { morphSVG: {shape: "#shape2", render: draw} })
  .to(shape, { morphSVG: {shape: "#shape3", render: draw} }, "+=0.5")
  .to(shape, { morphSVG: {shape: "#shape4", render: draw} }, "+=0.5")
  .to(shape, { morphSVG: {shape: "#shape1", render: draw} }, "+=0.5")

tl.progress(0.0001); //just to force the first render;
// GSDevTools.create({animation:tl, globalSync:false, paused:true});

document.body.addEventListener("click", function() {
  tl.paused(!tl.paused());
});


function draw(rawPath, target) {
  var l, segment, j, i;
  ctx.clearRect(0, 0, size, size);
  ctx.fillStyle = gradient;
  ctx.fill("evenodd");
  ctx.beginPath();
  for (j = 0; j < rawPath.length; j++) {
    segment = rawPath[j];
    l = segment.length;
    ctx.moveTo(segment[0], segment[1]);
    for (i = 2; i < l; i+=6) {
      ctx.bezierCurveTo(segment[i], segment[i+1], segment[i+2], segment[i+3], segment[i+4], segment[i+5]);
    }
    if (segment.closed) {
      ctx.closePath();
    }
  }
  ctx.fill("evenodd");
}





function setDisplay() {
  var ratio = window.devicePixelRatio || 1;
  canvas.width  = size * ratio;
  canvas.height = size * ratio;
  gsap.set(canvas, { width: size, height: size });
  ratio *= sizeRatio;
  ctx.translate(-viewBox.x * ratio, -viewBox.y * ratio);
  ctx.scale(ratio, ratio);
}
```

Explain how this demo works, then help me adapt it for my own project.

---

