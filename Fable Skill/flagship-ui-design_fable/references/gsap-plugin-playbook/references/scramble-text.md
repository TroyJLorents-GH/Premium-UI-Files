# ScrambleTextPlugin

Source: supplied `GSAP Plugins.md`, lines 4143–4302, original heading: ScrambleText.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


[ScrambleText CDN Link](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/ScrambleTextPlugin.min.js)


#### ScrambleText Prompt

I'm working with a GSAP demo from the GSAP docs: "Scramble Text ".
Docs page: https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin
CodePen: https://codepen.io/GreenSock/pen/jOjaoYJ
GSAP plugins used: ScrambleTextPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrambleTextPlugin.min.js

HTML:
```html
<div class="text-scramble__content">
  <p id="scramble-text-original">Mix it up with ScrambleText. Animate using characters, numbers, UPPERCASE or lowercase.</p>

  <p class="text-scramble__text" aria-hidden="true">
    <span id="scramble-text-1"></span>
    <span id="scramble-text-2"></span>
    <span id="scramble-text-3"></span>
    <span id="scramble-text-4"></span>
    <span id="scramble-text-5"></span>

    <img id="scramble-cursor" src="https://gsap.com/demo-assets/scramble-cursor.webp" alt="" />
  </p>
</div>
```

CSS:
```css
@font-face {
  font-display: block;
  font-family: Mori;
  font-style: normal;
  font-weight: 600;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
   font-family: "Space Mono", monospace;
  background: #0e100f;
  text-align: center;
  color: #dfdcff;
  line-height: 1;
}

.text-scramble__content {
  max-width: 40ch;
  font-size: max(2rem, min(5.69579vw + 0.665049rem, 3rem));
  font-weight: 600;
  letter-spacing: -0.01em;
  line-height: 1.1;
  margin-top: max(2rem, min(2.0712vw + 1.51456rem, 4rem));
  padding-bottom: 1.1em;
  position: relative;
}

.text-scramble__text {
  bottom: 0;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
}

.text-scramble__text span {
  word-break: break-word;
}

.text-scramble__text img {
  display: inline-block;
  height: 0.9em;
  width: auto;
}
```

JS:
```js
const tl = gsap.timeline({
  id: "text-scramble",
  defaults: { ease: "none" }
});

const cursorTl = gsap.timeline({ repeat: -1 });

gsap.set("#scramble-text-original", {
  opacity: 0
});

cursorTl
  .to("#scramble-cursor", {
    opacity: 0,
    duration: 0.5,
    ease: "none",
    delay: 0.2
  })
  .to("#scramble-cursor", {
    opacity: 1,
    duration: 0.5,
    ease: "none",
    delay: 0.2
  });

tl.to("#scramble-text-1", {
  scrambleText: {
    text: "Mix it up with ScrambleText.",
    chars: "lowerCase"
  },
  duration: 2
})
  .to("#scramble-text-2", {
    scrambleText: {
      text: "Animate using characters",
      chars: "XO",
      speed: 0.4
    },
    duration: 2
  })
  .to("#scramble-text-3", {
    scrambleText: { text: " numbers,", chars: "0123456789" },
    duration: 2
  })
  .to("#scramble-text-4", {
    scrambleText: { text: "UPPERCASE", chars: "upperCase", speed: 0.3 },
    duration: 1
  })
  .to("#scramble-text-5", {
    scrambleText: {
      text: "or lowercase.",
      chars: "lowerCase",
      speed: 0.3
    },
    duration: 1.5
  })
  .add(cursorTl);

window.onclick = () => tl.play(0); // click to replay
```

Explain how this demo works, then help me adapt it for my own project.


