# Staggers

Source: supplied `GSAP Plugins.md`, lines 5042–5156, original heading: Staggers.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


> Staggers are totally configurable and SUPER powerful. If a tween has multiple targets, you can easily add some delay between the start of each animation:

#### Stagger prompt and example 1

I'm working with a GSAP demo from the GSAP docs: "GSAP 101 - Staggers".
Docs page: https://gsap.com/resources/getting-started/Staggers
CodePen: https://codepen.io/GreenSock/pen/LYdzaoz

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="section">
  <div class="box green"></div>
  <div class="box purple"></div>
  <div class="box orange"></div>
  <div class="box purple"></div>
  <div class="box green"></div>
</div>
  <div class="text">
    <h4 class="braces">click a box to stagger out</h4>
  </div>
```

CSS:
```css
body {
  overflow: hidden;
}
.section {
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-direction: row;
  height: 100vh;
}

.box {
  cursor: pointer;
  opacity: 0;
}

.text {
  position: fixed;
  bottom: 2rem;
  width: 100%;
display:flex;align-items:center;justify-content:center;
}

.braces {
  display: block;
  font-size: 0.8rem;
}
```

JS:
```js
gsap.to(".box", {
  duration: 1,
  rotation: 360,
  opacity: 1,
  delay: 0.5,
  stagger: 0.1, // stagger in from the left with a 0.1 second gap in between animations
  ease: "sine.out"
});

document.querySelectorAll(".box").forEach((box, index) => {
  box.addEventListener("click", () => {
    gsap.to(".box", {
      duration: 0.5,
      opacity: 0,
      y: -100,
      stagger: {
        from: index, // stagger in from the clicked element's index
        amount: 1 // spread the entire stagger out over 1 second
      },
      ease: "back.in",
      overwrite: "auto"
    });
  });
});
```

Explain how this demo works, then help me adapt it for my own project.


#### Staggers example 2

> You can even stagger items that are laid out in a grid just by telling GSAP how many columns and rows your grid has!


https://gsap.com/resources/getting-started/Staggers

```
gsap.to(".box", {
  duration: 1,
  scale: 0.1,
  yoyo: true,
  repeat: 1,
  ease: "power1.inOut",
  stagger: {
    grid: [5, 13],
    from: "end",
    ease: "power3.inOut",
    amount: 1
  }
});
```

