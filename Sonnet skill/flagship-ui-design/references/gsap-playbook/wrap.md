# wrap() and wrapYoyo()

Source: supplied `GSAP Plugins.md`, lines 4973–5041, original heading: Wrap.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


> Returns the next item in an array or number in a range after the given index. Or returns a function that returns that object or value if no index is given.


I'm working with a GSAP demo from the GSAP docs: "GSAP 3 wrap() and wrapYoyo() utilities demo".
Docs page: https://gsap.com/docs/v3/GSAP/UtilityMethods/wrap()
CodePen: https://codepen.io/GreenSock/pen/5364a46c2767c6258132f7805ea0035e

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<h4>GSAP 3 wrap() / wrapYoyo() utilities</h4>
<div id="ball1" class="ball flair flair--2"></div>
<div id="ball2" class="ball flair flair--4"></div>
```

CSS:
```css
body{
  display:flex;
  align-items:stretch;
  justify-content:space-around;
  min-height:100vh;
  flex-direction: column;
}

.ball {
  width: 100px;
  height: 100px;
  will-change: transform;
}

h4 {
  margin: 20px;
  text-align: center
}
```

JS:
```js
gsap.defaults({duration:20, ease:"none"});

var windowWrap = gsap.utils.wrap(0, window.innerWidth),
    windowYoyo = gsap.utils.wrapYoyo(0, window.innerWidth);

gsap.to("#ball1", {
  x: 10000,
  modifiers: {
    x: x => windowWrap(parseFloat(x)) + "px"
  }
});

gsap.to("#ball2", {
  x: 10000,
  modifiers: {
    x: x => windowYoyo(parseFloat(x)) + "px"
  }
});
```

Explain how this demo works, then help me adapt it for my own project.


