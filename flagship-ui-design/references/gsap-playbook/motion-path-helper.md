# MotionPathHelper

Source: supplied `GSAP Plugins.md`, lines 3134–3305, original heading: MotionPathHelper.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Historical Club GreenSock wording is retained as source text, not a current licensing statement. Distinguish authoring controls from runtime motion.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material



[MotionPathHelper CDN Link](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/MotionPathHelper.min.js)

#### Example and prompt 1

I'm working with a GSAP demo from the GSAP docs: "MotionPathHelper demo".
GSAP 3.0 introduces a brand new MotionPathPluginHelper which makes editing curves in the browser a breeze! It's  one of the many Club GreenSock perks https://greensock.com/club/
Docs page: https://gsap.com/docs/v3/Plugins/MotionPathHelper
CodePen: https://codepen.io/GreenSock/pen/oNNEdRV
GSAP plugins used: MotionPathPlugin, MotionPathHelper

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathHelper.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<svg id="motionPath" viewBox="-20 0 557 190">
  <defs>
    <linearGradient id="macha" x1="0.045" y1="0.293" x2="0.955" y2="0.707">
      <stop offset="20.74%" style="stop-color: var(--color-shockingly-green, #0ae448)" />
      <stop offset="65.5%" style="stop-color: var(--color-lt-green, #abff84)" />
    </linearGradient>

    <!-- the flair PNG's alpha becomes the shape's silhouette -->
    <mask id="flair-mask" mask-type="alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="100" height="100">
      <image href="https://gsap.com/demo-assets/2D-star.png" width="100" height="100" />
    </mask>
  </defs>

  <path id="path" fill="none" d="M8,102 C15,83 58,25 131,24 206,24 233,63 259,91 292,125 328,155 377,155 464,155 497,97 504,74"/>

  <g class="star">
    <rect width="100" height="100" fill="url(#macha)" mask="url(#flair-mask)" />
  </g>
</svg>
```

CSS:
```css
body, html {
  padding: 0;
  margin: 0
}
body {
  height: 100vh;
  overflow: hidden;
}
#motionPath {
  overflow: visible;
  height: 100%;
  max-width: 100%;
}

#motionPath path {
  stroke-width: 2;
  stroke: gray;
}

#motionPath .astronaut {
  visibility: hidden;
}

.copy-motion-path {
  background: transparent!important;
  border-radius: 99px!important;
  border: solid 2px #fffce1;
  color: #fffce1!important;
}
```

JS:
```js
//register the plugin (just once)
gsap.registerPlugin(MotionPathPlugin);

gsap.set(".star", {scale: 0.5, autoAlpha: 1});

gsap.to(".star", {
  duration: 5, 
  ease: "power1.inOut",
  immediateRender: true,
  motionPath: {
    path: "#path",
    align: "#path",
    alignOrigin: [0.5, 0.5],
    autoRotate: 90
  }
});

MotionPathHelper.create(".star");
```

Explain how this demo works, then help me adapt it for my own project.


#### MotionPathHelper Demo

I'm working with a GSAP demo from the GSAP docs: "MotionPathHelper.editPath() Demo".
GSAP's MotionPathHelper.editPath() lets you edit any SVG path directly in the browser
Docs page: https://gsap.com/docs/v3/MotionPathHelper/static.editPath()
CodePen: https://codepen.io/GreenSock/pen/wvgGxEr
GSAP plugins used: MotionPathPlugin, MotionPathHelper

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathHelper.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<svg id="motionPath" viewBox="-20 0 557 190">
  <path id="path" fill="none" d="M8,102 C15,83 58,25 131,24 206,24 233,63 259,91 292,125 328,155 377,155 464,155 497,97 504,74"/>
</svg>
```

CSS:
```css
body {
  display: flex;
  align-items: center;
  justify-content:center;
  height: 100vh;
}

#motionPath {
  overflow: visible;
  height: 100%;
  max-width: 100%;
}

#motionPath path {
  stroke-width: 2;
  stroke: gray;
}

#motionPath .astronaut {
  visibility: hidden;
}
```

JS:
```js
gsap.registerPlugin(MotionPathPlugin);

MotionPathHelper.editPath("#path", {
  selected: true,
  draggable: true,
  handleSize: 7,
  onPress: () => console.log("pressed"),
  onRelease: () => {
    console.log("released")
    // get the new path data
    console.log(this.path.getAttribute('d'))
  },
  onUpdate: () => console.log("updated"),
  onDeleteAnchor: () => console.log("deleted anchor")
});
```

Explain how this demo works, then help me adapt it for my own project.


