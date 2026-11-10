# Morphing SVG shapes

Source: supplied `GSAP Plugins.md`, lines 6955–7046, original heading: Prompt 9 Morph SVG.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Original SVG Prompt9. Repeats the first MorphSVG demo.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


I'm working with a GSAP demo from the GSAP docs: "MorphSVG - simple morph".
Docs page: https://gsap.com/resources/svg
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


