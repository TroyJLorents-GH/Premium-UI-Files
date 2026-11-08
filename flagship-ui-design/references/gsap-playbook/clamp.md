# clamp()

Source: supplied `GSAP Plugins.md`, lines 4307–4390, original heading: Clamp.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


#### Clamp Demo and Prompt

>Clamps a number between a given minimum and maximum. If the number you provide is less than the minimum, it will return the minimum. If it's greater than the maximum, it returns the maximum. If it's between the minimum and maximum, it returns the number unchanged.

I'm working with a GSAP demo from the GSAP docs: "gsap.utils.clamp()".
Docs page: https://gsap.com/docs/v3/GSAP/UtilityMethods/clamp()
CodePen: https://codepen.io/GreenSock/pen/vYqdaKp

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/gOWxmWG.css

HTML:
```html
<svg viewBox="-1 -1 102 20">
  <rect width="100" height="10" rx="5" stroke="rgb(255, 252, 225)" />
  <rect width="50" height="10" x="25" stroke="rgb(255, 252, 225)"/>
  <rect id="ball" width="6" height="6" rx="3" y="2" fill="#0AE448"/>
</svg>

<input id="num" type="text" maxlength="8" value="50"/>

<p>Type a number above.<br>The value will be clamped between 30 & 70.</p>
```

CSS:
```css
html, body {
  margin:0;
  padding:0;
  width:100%;
  height:100vh;
}

body {
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
}

svg {
  width:50%;
  max-width:750px;
}

input {
  text-align:center;
  font-size:2rem;
  background:transparent;
  border:none;
  border-bottom:1px solid rgb(255, 252, 225);
  color:rgb(255, 252, 225);
  width:90px;
  padding: .2rem;
  outline:none;
}

p {
  text-align:center;
  line-height:2rem;
  font-size:1.3rem;
}
```

JS:
```js
gsap.set('#ball', { xPercent:-50, x:50 })

const num = document.querySelector("#num");

window.addEventListener("keyup", (e)=>{
  gsap.set('#ball', {
    x: gsap.utils.clamp(30, 70, num.value)
  })
})
```

Explain how this demo works, then help me adapt it for my own project.

