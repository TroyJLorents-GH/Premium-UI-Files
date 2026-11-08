# SplitText: splitting and masking

Source: supplied `GSAP Plugins.md`, lines 645–895, original heading: SplitText.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Preserve readable unsplit content and restore split DOM during teardown. Choose an accessibility strategy appropriate to nested semantics.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


#### Animating SplitText Prompt

[SplitText page](https://gsap.com/docs/v3/Plugins/SplitText/)

- Prompt below
---

I'm working with a GSAP demo from the GSAP docs: "SplitText Demo".
Docs page: https://gsap.com/docs/v3/Plugins/SplitText/
CodePen: https://codepen.io/GreenSock/pen/xxmaNYj
GSAP plugins used: SplitText

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="container">
  <div class="button-wrapper">
    <button id="chars" class="button">Characters</button>
    <button id="words" class="button">Words</button>
    <button id="lines" class="button">Lines</button>
  </div>
  <div class="text">
    Break apart HTML text into characters, words, and/or lines for easy animation.
  </div>

</div>
```

CSS:
```css
html,
body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  overflow: hidden;
}

.container {
  position: relative;
  width: 90vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  border-radius: 9px;
}

.text {
  color: #dfdcff;
  font-size: clamp(2rem, 12rem, 5vw);
  line-height: 1.2;
  box-sizing: border-box;
  padding: 5%;
  width: 100%;
  text-align: center;
  perspective: 500px;
}

.button-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}
```

JS:
```js
gsap.registerPlugin(SplitText);

let split, animation;
document.querySelector("#chars").addEventListener("click", () => {
  animation && animation.revert();
  animation = gsap.from(split.chars, {
    x: 150,
    opacity: 0,
    duration: 0.7, 
    ease: "power4",
    stagger: 0.04
  })
});

document.querySelector("#words").addEventListener("click", () => {
  animation && animation.revert();
  animation = gsap.from(split.words, {
    y: -100,
    opacity: 0,
    rotation: "random(-80, 80)",
    duration: 0.7, 
    ease: "back",
    stagger: 0.15
  })
});

document.querySelector("#lines").addEventListener("click", () => {
  animation && animation.revert();
  animation = gsap.from(split.lines, {
    rotationX: -100,
    transformOrigin: "50% 50% -160px",
    opacity: 0,
    duration: 0.8, 
    ease: "power3",
    stagger: 0.25
  })
});

function setup() {
  split && split.revert();
  animation && animation.revert();
  split = SplitText.create(".text", {type:"chars,words,lines"});
}
setup();
window.addEventListener("resize", setup);
```

Explain how this demo works, then help me adapt it for my own project.


#### Masking (SplitText) Prompt



I'm working with a GSAP demo from the GSAP docs: "Masked Lines with SplitText".
Docs page: https://gsap.com/docs/v3/Plugins/SplitText/
CodePen: https://codepen.io/GreenSock/pen/a28f78aa1b47e6fa3ad56684564fdf81
GSAP plugins used: SplitText

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js

HTML:
```html
<div class="container">
  <h1 class="split">The text in this paragraph is split by words and lines. We have enabled masking on the lines so that we can animate the lines to create a fun 'reveal' animation.</h1>
</div>

<button>Replay Slowly</button>
```

CSS:
```css
@font-face {
  font-display: block;
  font-family: Mori;
  font-style: normal;
  font-weight: 900;
  src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}

html, body {
  margin:0;
  padding:0;
  width:100%;
  height:100vh;
}
  
body {
  display:flex;
  align-items:center;
  justify-content:center;
  flex-direction: column;
  font-family: "Mori";
/*   background: #0e100f; */
  background: radial-gradient(129% 99% at 112% 85%, rgb(223, 220, 255) 20%, rgb(166, 158, 255) 90%),    
    url('https://gsap.com/demo-assets/noise-e82662fe.webp');  
  background-blend-mode: color-dodge;
}

.container {
  max-width: 80vw;
}

.split {
  opacity: 0;
  text-align:center;
  color: rgb(14, 16, 15);
  font-size: clamp(2rem, 5rem, 3vw);
  letter-spacing: 0.05rem;
  will-change: transform;
  color: #0e100f;
}

.split * {
  will-change: transform;
}

button {
  display: inline-block;
  outline: none;
  padding: 8px 14px;
  background: transparent;
  border: solid 4px #0e100f;
  color: #0e100f;
  text-decoration: none;
  border-radius: 99px;
  padding: 12px 25px;
  text-transform: uppercase;
  font-weight: 600;
  cursor: pointer;
  line-height: 18px;
}
```

JS:
```js
gsap.registerPlugin(SplitText);

console.clear();

document.fonts.ready.then(() => {
  gsap.set(".split", { opacity: 1 });

  let split;
  SplitText.create(".split", {
    type: "words,lines",
    linesClass: "line",
    autoSplit: true,
    mask: "lines",
    onSplit: (self) => {
      split = gsap.from(self.lines, {
        duration: 0.6,
        yPercent: 100,
        opacity: 0,
        stagger: 0.1,
        ease: "expo.out",
      });
      return split;
    }
  });

  document.querySelector("button").addEventListener("click", (e) => {
    split.timeScale(0.2).play(0);
  });
});
```

Explain how this demo works, then help me adapt it for my own project.


