# Draggable

Source: supplied `GSAP Plugins.md`, lines 1447–1686, original heading: Draggable.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** The first subsection, Draggable Quick Start, is a mislabeled duplicate CSS-variable demo. Use the later Draggable Prompt subsection for actual dragging. The SVG Drag source repeats that dragging demo.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


#### Dragable Quick Start

I'm working with a GSAP demo from the GSAP docs: "CSS Variables Demo".
Docs page: https://gsap.com/docs/v3/Plugins/CSSRulePlugin/
CodePen: https://codepen.io/GreenSock/pen/MoeLdj

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/JGaKdQ.css

HTML:
```html
<link href='//fonts.googleapis.com/css?family=Signika+Negative:300,400' rel='stylesheet' type='text/css'>

<div class="wrapper">
<h2>Apply same --myColor variable to multiple css rules.</h2>
<p>Tweening the <strong> --myColor</strong> variable will update multiple elements.</p>

<div class="cool">this is cool </div>
</div>
```

CSS:
```css
body {
  margin:20px;
}

html {
  --myColor: #00bae2;
}

h2 {
  font-size:20px;
}

.wrapper {
  border: 3px solid var(--myColor);
  border-radius: 10px;
  margin-right:10px;
  padding: 1rem;
}

 h2, strong {
  color:var(--myColor);
}

.cool {
  display:inline-block;
  padding: 0.5rem 1rem;
  color:white;
  border-radius:99px;
  background-color:var(--myColor);
}
```

JS:
```js
gsap.to("html", {"--myColor":"#0ae448", yoyo:true, repeat:20, duration: 1});
```

Explain how this demo works, then help me adapt it for my own project.

---

#### Draggable Prompt

I'm working with a GSAP demo from the GSAP docs: "Draggable Demo".
Docs page: https://gsap.com/docs/v3/Plugins/Draggable/
CodePen: https://codepen.io/GreenSock/pen/yLGqXzZ
GSAP plugins used: Draggable, InertiaPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Draggable.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/InertiaPlugin.min.js

HTML:
```html
<div class="container">
  <div class="wrapper">
    <div class="flair flair--1"></div>
  </div>
  <div class="wrapper">
    <div class="flair flair--3"></div>
  </div>
  <div class="wrapper">
    <div class="flair flair--4"></div>
  </div>

  <div class="text">
    <h4 class="braces">spin us, drag us...</h4>
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

:root {
  --dark: #0e100f;
  --light: #fffce1;
  --surface75: #bbbaa6;
}

* {
  box-sizing: border-box;
}

html,
body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

body {
  margin: 0;
  background-color: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
  font-weight: 400;
  line-height: 1.45;
}

.container {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

h4 {
  position: absolute;
  width: 100%;
  left: 0;
  right: 0;
  bottom: 1rem;
  margin: 0;
  text-align: center;
  pointer-events: none;
  color: var(--light);
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.2;
}

.flair {
  cursor: pointer;
  width: 80px;
  height: 80px;
  background-size: contain;
  background-repeat: no-repeat;
  will-change: transform;
}

.flair--1 {
  background-image: url("https://gsap.com/demo-assets/ui-flair-3.webp");
}

.flair--3 {
  background-image: url(https://gsap.com/demo-assets/ui-flair-2.webp);
}

.flair--4 {
  background-image: url(https://gsap.com/demo-assets/ui-flair-4.webp);
}

.text {
  position: fixed;
  bottom: 1rem;
}

/* brand curly braces around the hint text */
.braces {
  position: relative;
  color: var(--light);
}

.braces::before,
.braces::after {
  position: absolute;
  content: "";
  top: 50%;
  height: 2rem;
  aspect-ratio: 1 / 2;
  background-repeat: no-repeat;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 27 78'%3E%3Cpath fill='%23FFFCE1' d='M26.52 77.21h-5.75c-6.83 0-12.38-5.56-12.38-12.38V48.38C8.39 43.76 4.63 40 .01 40v-4c4.62 0 8.38-3.76 8.38-8.38V12.4C8.38 5.56 13.94 0 20.77 0h5.75v4h-5.75c-4.62 0-8.38 3.76-8.38 8.38V27.6c0 4.34-2.25 8.17-5.64 10.38 3.39 2.21 5.64 6.04 5.64 10.38v16.45c0 4.62 3.76 8.38 8.38 8.38h5.75v4.02Z'%3E%3C/path%3E%3C/svg%3E");
}

.braces::before {
  right: 100%;
  transform: translateY(-50%);
}

.braces::after {
  left: 100%;
  transform: rotate(180deg) translateY(50%);
}
```

JS:
```js
gsap.registerPlugin(Draggable, InertiaPlugin);

Draggable.create(".flair--1", {
  type: "x",
  bounds: ".container"
});

Draggable.create(".flair--3", {
  type: "rotation",
  inertia: true
});

Draggable.create(".flair--4", {
  bounds: ".container",
  inertia: true
});
```

Explain how this demo works, then help me adapt it for my own project.

---

