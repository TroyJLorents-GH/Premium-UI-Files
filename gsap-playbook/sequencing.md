# Timelines and sequencing

Source: supplied `GSAP Plugins.md`, lines 5157–5273, original heading: Sequencing asnimations.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material



#### Example and prompt 1 

I'm working with a GSAP demo from the GSAP docs: "Sequencing - delays".
Docs page: https://gsap.com/resources/getting-started/timelines
CodePen: https://codepen.io/GreenSock/pen/eYMWJvP

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="box green">no delay</div>
<div class="box purple">delay: 1</div>
<div class="box orange">delay: 2</div>
```

CSS:
```css
/* Global styles come from external css https://codepen.io/GreenSock/pen/gOWxmWG */


body {
  display: flex;
  align-items: center;
  justify-content: space-around;
  min-height: 100vh;
  margin: 0;
  overflow: hidden;
}

.box {
  display: block;
    display: flex;
  align-items: center;
  justify-content: center;
}
```

JS:
```js
gsap.to(".green", { 
  rotation: 360,
  duration: 1,
});
gsap.to(".purple", { 
  rotation: 360,
  duration: 1,
  delay: 1,
});
gsap.to(".orange", { 
  rotation: 360,
  duration: 1,
  delay: 2,
});
```

Explain how this demo works, then help me adapt it for my own project.


#### Exmaple and prompt 2

I'm working with a GSAP demo from the GSAP docs: "Timeline - special properties".
Docs page: https://gsap.com/resources/getting-started/timelines
CodePen: https://codepen.io/GreenSock/pen/NWYjZqQ

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="box green"></div>
<div class="box purple"></div>
<div class="box orange"></div>
```

CSS:
```css
/* Global styles come from external css https://codepen.io/GreenSock/pen/gOWxmWG */


body {
  display: flex;
  align-items: center;
  justify-content: space-around;
  min-height: 100vh;
  margin: 0;
  overflow: hidden;
}

.box {
  display: block;
    display: flex;
  align-items: center;
  justify-content: center;
}
```

JS:
```js
let tl = gsap.timeline({repeat: -1, repeatDelay: 1, yoyo: true})

tl.to(".green", { rotation: 360 });
tl.to(".purple", { rotation: 360 });
tl.to(".orange", { rotation: 360 });
```

Explain how this demo works, then help me adapt it for my own project.

