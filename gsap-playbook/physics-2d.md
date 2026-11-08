# Physics2DPlugin

Source: supplied `GSAP Plugins.md`, lines 3559–3884, original heading: Physics2D.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** The source assigns undeclared i and flairBullet. Declare local variables for strict/module execution and own the lifecycle of spawned elements and tweens.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


[physics2D CDN Link](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/Physics2DPlugin.min.js)

I'm working with a GSAP demo from the GSAP docs: "Physics2D Demo".
Docs page: https://gsap.com/docs/v3/Plugins/Physics2DPlugin
CodePen: https://codepen.io/GreenSock/pen/YzdOVbK
GSAP plugins used: Physics2DPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Physics2DPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="container">
  <div class="wrapper">
    <h4>Click anywhere to fire the Flair Cannon!</h4>
    <div class="cannon flair"></div>
    <div class="flair-container"></div>
  </div>
</div>
```

CSS:
```css
html, body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

h4 {
  color: var(--mid);
  position: absolute;
  width: 100%;
  left: 0;
  right: 0;
  top: 1rem;
  text-align: center;
  pointer-events: none;
}

.container {
  position: relative;
  width: 90vw;
  height: 90vh;
  max-width: 90vh;
  max-height: 90vw;
  display: flex;
  align-items: center;
  justify-content: space-around;
  border-radius: 9px;
  background: #0e100f;
}

.wrapper {
  width: 100%;
  height: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  overflow: hidden;
}

.cannon {
  position: relative;
  z-index: 10;
  background: transparent;
}

.flair-container {
  width: 50px;
  height: 50px;
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}

.flair {
  width: 50px;
  height: 50px;
  background-image: url("https://gsap.com/demo-assets/flair.webp");
  background-size: contain;
  background-repeat: no-repeat;
}

.flair-bullet {
  position: absolute;
  top: 0;
  left: 0;
  width: 50px;
  height: 50px;
  will-change: transform;
  opacity: 0;
}

.flair--2 {
  background-image: url("https://gsap.com/demo-assets/flair-2.webp");
}

.flair--3 {
  background-image: url("https://gsap.com/demo-assets/flair-3.webp");
}

.flair--4 {
  background-image: url("https://gsap.com/demo-assets/flair-4.webp");
}

.flair--5 {
  background-image: url("https://gsap.com/demo-assets/flair-5.webp");
}

.flair--6 {
  background-image: url("https://gsap.com/demo-assets/flair-6.webp");
}

.flair--7 {
  background-image: url("https://gsap.com/demo-assets/flair-7.webp");
}

.flair--8 {
  background-image: url("https://gsap.com/demo-assets/flair-8.webp");
}

.flair--9 {
  background-image: url("https://gsap.com/demo-assets/flair-9.webp");
}

.flair--10 {
  background-image: url("https://gsap.com/demo-assets/flair-10.webp");
}

.flair--11 {
  background-image: url("https://gsap.com/demo-assets/flair-11.webp");
}

.flair--12 {
  background-image: url("https://gsap.com/demo-assets/flair-12.webp");
}

.flair--13 {
  background-image: url("https://gsap.com/demo-assets/flair-13.webp");
}

.flair--14 {
  background-image: url("https://gsap.com/demo-assets/flair-14.webp");
}

.flair--15 {
  background-image: url("https://gsap.com/demo-assets/flair-15.webp");
}

.flair--16 {
  background-image: url("https://gsap.com/demo-assets/flair-16.webp");
}

.flair--17 {
  background-image: url("https://gsap.com/demo-assets/flair-17.webp");
}

.flair--18 {
  background-image: url("https://gsap.com/demo-assets/flair-18.webp");
}

.flair--19 {
  background-image: url("https://gsap.com/demo-assets/flair-19.webp");
}

.flair--20 {
  background-image: url("https://gsap.com/demo-assets/flair-20.webp");
}

.flair--21 {
  background-image: url("https://gsap.com/demo-assets/flair-21.webp");
}

.flair--22 {
  background-image: url("https://gsap.com/demo-assets/flair-22.webp");
}

.flair--23 {
  background-image: url("https://gsap.com/demo-assets/flair-23.webp");
}

.flair--24 {
  background-image: url("https://gsap.com/demo-assets/flair-24.webp");
}

.flair--25 {
  background-image: url("https://gsap.com/demo-assets/flair-25.webp");
}

.flair--26 {
  background-image: url("https://gsap.com/demo-assets/flair-26.webp");
}

.flair--27 {
  background-image: url("https://gsap.com/demo-assets/flair-27.webp");
}

.flair--28 {
  background-image: url("https://gsap.com/demo-assets/flair-28.webp");
}

.flair--29 {
  background-image: url("https://gsap.com/demo-assets/flair-29.webp");
}

.flair--30 {
  background-image: url("https://gsap.com/demo-assets/flair-30.webp");
}

.flair--31 {
  background-image: url("https://gsap.com/demo-assets/flair-31.webp");
}

.flair--32 {
  background-image: url("https://gsap.com/demo-assets/flair-32.webp");
}

.flair--33 {
  background-image: url("https://gsap.com/demo-assets/flair-33.webp");
}

.flair--34 {
  background-image: url("https://gsap.com/demo-assets/flair-34.webp");
}

.flair--35 {
  background-image: url("https://gsap.com/demo-assets/flair-35.webp");
}

@media (min-width: 768px) {
  .flair,
  .flair-container {
    width: 100px;
    height: 100px;
  }
}
```

JS:
```js
console.clear();

const masterTl = gsap.timeline({
  paused: true,
});
const cannon = document.querySelector(".cannon");
const angle = 20;
const tl1 = gsap
  .timeline()
  .to(cannon, {
    rotation: -angle,
    duration: 0.65,
    ease: "power1.inOut"
  })
  .to(
    cannon,
    {
      rotation: angle,
      ease: "power1.inOut",
      duration: 1,
      repeat: 3,
      yoyo: true
    }
  )
.to(cannon, {
    rotation: 0,
    duration: 0.65,
    ease: "power1.inOut"
  });

const bullets = [];
const bulletsContainer = document.querySelector(".flair-container");
const tl1Time = tl1.duration();

for (i = 0; i < 40; i++) {
  const className = "flair--" + gsap.utils.random(2, 35, 1);
  flairBullet = document.createElement("div");
  flairBullet.setAttribute("class", "flair flair-bullet " + className);
  bulletsContainer.appendChild(flairBullet);
  bullets.push(flairBullet);
  gsap.set(flairBullet, { scale: "random(0.4, 0.6)" });
}

const tl2 = gsap
  .timeline()
  .to(bullets, {
    opacity: 1,
    duration: 0.25,
    stagger: {
      amount: tl1Time
    }
  })
  .to(
    bullets,
    {
      duration: tl1Time,
      physics2D: {
        velocity: "random(600, 850)",
        angle: () => 270 + gsap.getProperty(cannon, "rotation"),
        gravity: 600
      },
      stagger: {
        amount: tl1Time
      }
    },
    0
  );
masterTl
  .add(tl1, 0)
  .add(tl2, 0)
  .play();
window.addEventListener("click", () => masterTl.restart());
```

Explain how this demo works, then help me adapt it for my own project.

