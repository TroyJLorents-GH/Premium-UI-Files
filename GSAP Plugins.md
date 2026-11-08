# GSAP Skills and plugins

- Plugins Page and Overview: https://gsap.com/resources/Plugins/

## Scroll Plugins

### ScrollTrigger

```
https://cdn.jsdelivr.net/npm/gsap@3.14.1/dist/ScrollTrigger.min.js
```

### ScrollTo

```
https://cdn.jsdelivr.net/npm/gsap@3.14.1/dist/ScrollToPlugin.min.js
```

> The demo below uses the offsetY so that each section scrolls into view just under the navigation. Click the section buttons in the demo below. Check out the JS source.

#### ScrollTo Demo and prompt 

I'm working with a GSAP demo from the GSAP docs: "ScrollToPlugin: Scroll to Element".
Docs page: https://gsap.com/docs/v3/Plugins/ScrollToPlugin
CodePen: https://codepen.io/GreenSock/pen/4be7ea5c962b62bcd156612524687a5a
GSAP plugins used: ScrollToPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollToPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<nav class="hr-bottom">
  <button id="section1Btn">Section 1</button>
  <button id="section2Btn">Section 2</button>
  <button id="section3Btn">Section 3</button>
</nav>
<div class="content">
  <h2 class="heading-scroll heading-l" id="section1">Section 1</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nibh quam, egestas eu eros molestie, eleifend viverra augue. Suspendisse potenti. Quisque commodo consectetur quam, non pretium orci viverra at. Maecenas eget iaculis nunc. </p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>

  <h2 class="heading-scroll heading-l" id="section2">Section 2</h2>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>

  <h2 class="heading-scroll heading-l" id="section3">Section 3</h2>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementes, nascetur ridiculus mus.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec nibh quam, egestas eu eros molestie, eleifend viverra augue. Suspendisse potenti. Quisque commodo consectetur quam, non pretium orci viverra at. Maecenas eget iaculis nunc. </p>
  <p>Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
  <p>consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa.</p>
  <p>Praesent at pellentesque augue. Nunc sed ullamcorper risus. Duis tincidunt consectetur condimentum. Suspendisse pharetra purus urna, ac pretium mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
  <p>Mi elementum et. Praesent dui nibh, ullamcorper in justo sed, volutpat cursus orci. Etiam vitae sodales massa. Cum sociis natoque penatibus et magnis dis parturient montes,</p>
</div>
```

CSS:
```css
/* Global styles come from external css */
body {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.content {
  margin: 20px;
  padding-top: 4rem;
  width: 100%;
  max-width: 80ch;
}

nav {
  position: fixed;
  top: 0;
  width: 100%;
  background: var(--color-just-black);
  margin: 0;
  padding: 1rem 10px;
  display: flex;
  justify-content: space-around;
}

h2 {
  color: var(--color-surface-white);
  font-size: 2rem;
  margin-top: 4rem;
}

button {
  border-color: transparent;
}

button:hover {
  border-color: transparent;
}
```

JS:
```js
document.querySelectorAll("nav button").forEach((btn, index) => {
  btn.addEventListener("click", () => {
    gsap.to(window, {duration: 1, scrollTo:{y:"#section" + (index + 1), offsetY:120}});
  });
});
```

Explain how this demo works, then help me adapt it for my own project.

### ScrollSmoother (requires ScrollTrigger)

```
https://cdn.jsdelivr.net/npm/gsap@3.14.1/dist/ScrollSmoother.min.js
```

#### Prompt for ScrollSmoother
  
I'm working with a GSAP demo from the GSAP docs: "ScrollSmoother".
Docs page: https://gsap.com/docs/v3/Plugins/ScrollSmoother/
CodePen: https://codepen.io/GreenSock/pen/d03d2e4695cf6a87ebc59a2fbbbdef53
GSAP plugins used: ScrollSmoother, ScrollTrigger

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollSmoother.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollToPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div id="smooth-wrapper">
  <div id="smooth-content">
    <header class="header">
      <h1 class="heading-l heading-scroll">ScrollSmoother</h1>
      <button class="button">Jump to shape</button>
    </header>
    <div class="box box-a gradient-pink" data-speed="clamp(0.5)">a</div>
    <div class="box box-b gradient-purple" data-speed="clamp(0.8)">b</div>
    <img class="shape" data-speed="1.5" src="https://gsap.com/demo-assets/2D-keyframe-2.webp" alt="" />
    <div class="line"></div>
  </div>
</div>
```

CSS:
```css
body {
  background-color: var(--color-just-black);
  overscroll-behavior: none;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.header {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding-top: 2.5rem;
}

#smooth-content {
  overflow: visible;
  width: 100%;
  /* set a height because the contents are position: absolute, thus natively there's no height */
  height: 4000px;
  background-image: linear-gradient(
      rgba(255, 255, 255, 0.07) 2px,
      transparent 2px
    ),
    linear-gradient(90deg, rgba(255, 255, 255, 0.07) 2px, transparent 2px),
    linear-gradient(rgba(255, 255, 255, 0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.06) 1px, transparent 1px);
  background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px;
  background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px;
}

button {
  position: relative;
  margin-top: 1rem;
}

heading-l {
  margin-top: 2rem;
}

.box,
.shape {
  width: 100px;
  height: 100px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  z-index: 100;
  line-height: 100px;
  text-align: center;
  will-change: transform;
}
.box.active {
  outline: 2px var(--color-surface-white);
}

.box-a {
  top: 400px;
}

.box-b {
  top: 900px;
}

.shape {
  top: 1300px;
  will-change: transform;
}

.line {
  visibility: hidden;
  width: 2px;
  height: 4000px;
  position: absolute;
  left: 400px;
  top: 0px;
  background-color: #777;
}

footer {
  position: fixed;
  right: 0px;
  bottom: 0px;
  padding: 6px 10px 10px 12px;
  border-top-left-radius: 26px;
  z-index: 100;
  background-color: rgba(0, 0, 0, 0.5);
}

.end {
  position: absolute;
  /*   bottom: 0; */
  top: 2400px;
  transform: translateY(-100%);
  font-size: 30px;
  color: white;
}
```

JS:
```js
gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

// create the smooth scroller FIRST!
let smoother = ScrollSmoother.create({
  smooth: 2,
  effects: true,
  normalizeScroll: true
});

// pin shape when it reaches the center of the viewport, for 300px
ScrollTrigger.create({
  trigger: ".shape",
  pin: true,
  start: "center center",
  end: "+=300"
});

document.querySelector("button").addEventListener("click", (e) => {
  // scroll to the spot where the shape is in the center.
  // parameters: element, smooth, position
  smoother.scrollTo(".shape", true, "center center");

  // or you could animate the scrollTop:
  // gsap.to(smoother, {
  // 	scrollTop: smoother.offset(".shape", "center center"),
  // 	duration: 1
  // });
});
```

Explain how this demo works, then help me adapt it for my own project.

---

### ScrollSmoother `.effects()` `clamp()`  

#### ScrollSmoother Prompt below 


I'm working with a GSAP demo from the GSAP docs: "ScrollSmoother Parallax Offsets".
Docs page: https://gsap.com/docs/v3/Plugins/ScrollSmoother/effects()
CodePen: https://codepen.io/GreenSock/pen/NPpwNXB
GSAP plugins used: ScrollSmoother, ScrollTrigger

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollSmoother.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js

HTML:
```html
<div id="smooth-wrapper">
  <div id="smooth-content">
    <div class="box box-ref">ref</div>
    <div class="box box-a" data-speed="0.5">a</div>
    <div class="box box-b" data-speed="0.5">b</div>
    <div class="box box-c" data-speed="0.5">c</div>
    <div class="refline"></div>
  </div>
</div>
<div class="middle"></div>

<h2>
  ref scrolls normally.<br/>
  all divs have position of top:80vh.<br/>
  a, b, and c all have data-speed:0.5<br/>
  Each object will be at it's "native" placement (with it's top edge aligned to the top of the ref element) when it is centered vertically in the viewport</h2>
```

CSS:
```css
* {
  box-sizing: border-box;
}

/* Typography */

@font-face {
  font-display: block;
  font-family: Mori;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}

@font-face {
  font-display: block;
  font-family: Mori;
  font-style: normal;
  font-weight: 600;
  src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}

@font-face {
  font-display: block;
  font-family: Fraktion Mono;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff)
    format("woff");
}

:root {
  --color-shockingly-green: #0ae448;
  --color-just-black: #0e100f;
  --color-surface-white: #fffce1;
  --color-pink: #fec5fb;
  --color-shockingly-pink: #f100cb;
  --color-orangey: #ff8709;
  --color-lilac: #9d95ff;
  --color-lt-green: #abff84;
  --color-blue: #00bae2;
  --color-grey: #191919;
  --color-grey-dark: #191919;
  --color-surface75: #bbbaa6;
  --color-surface50: #7c7c6f;
  --color-surface25: #42433d;
  --gradient-macha: linear-gradient(
    114.41deg,
    var(--color-shockingly-green) 20.74%,
    var(--color-lt-green) 65.5%
  );
  --gradient-orange-crush: linear-gradient(
    111.45deg,
    var(--color-orangey) 19.42%,
    #f7bdf8 73.08%
  );
  --gradient-lipstick: linear-gradient(
    165.72deg,
    #f7bdf8 21.15%,
    #cd237f 81.93%
  );
  --gradient-purple-haze: linear-gradient(
    153.58deg,
    #f7bdf8 32.25%,
    #2f3cc0 92.68%
  );
  --gradient-skyfall: linear-gradient(
    131.77deg,
    #0a157a 30.82%,
    #15bfe4 81.82%
  );
  --gradient-emerald-city: linear-gradient(
    166.9deg,
    var(--color-shockingly-green) 53.19%,
    #0085d0 107.69%
  );
  --gradient-summer-fair: linear-gradient(
    144.02deg,
    var(--color-blue) 4.56%,
    var(--color-pink) 72.98%
  );
  --color-core-green: #dfffd1;
  --color-core-green-lt: #f3ffee;
  --color-core-gradient: radial-gradient(
    89.08% 84.62% at 16.54% 78.46%,
    #fbfefa 0%,
    #c9f6b4 39.58%,
    #abff84 77.6%,
    #2fee65 100%
  );
  --color-core-button-gradient: linear-gradient(
    114.41deg,
    #0ae448 20.74%,
    #abff84 65.5%
  );
  --color-core-heading-gradient: linear-gradient(
      180deg,
      #d6ffc3 0%,
      rgba(214, 255, 195, 0) 100%
    ),
    #f3ffee;
  --color-core-intro-gradient: linear-gradient(
      144.5deg,
      #e8ffdd 65.09%,
      #7dea7b 122.73%
    ),
    linear-gradient(311.31deg, #7ef89e 36.08%, #e5ffd9 106.98%);
  --color-text-purple: #d2ceff;
  --color-text-purple-lt: #dfdcff;
  --color-text-gradient: radial-gradient(
    129.03% 100% at 120.97% 81.45%,
    #dfdcff 27.08%,
    #a69eff 100%
  );
  --color-svg-tangerine: #ffe3c7;
  --color-svg-tangerine-lt: #fff0e0;
  --color-svg-gradient: radial-gradient(
    70.77% 70.77% at 0% 70.77%,
    #ffd9b0 0%,
    #fd9f3b 80.73%,
    #ff8709 100%
  );
  --color-svg-heading-gradient: linear-gradient(
      180deg,
      #ffbd77 0%,
      rgba(254, 197, 251, 0) 100%
    ),
    #ffe4c7;
  --color-ui-blue: #bef3fe;
  --color-ui-blue-lt: #e1faff;
  --color-ui-blue-codeblk: #f6feff;
  --color-ui-text-gradient: linear-gradient(
    168.89deg,
    #fec5fb -21.3%,
    #00bae2 89.88%
  );
  --color-ui-code-blocktext-gradient: linear-gradient(
    142.91deg,
    #cef6ff 18.75%,
    #a6efff 54.93%
  );
  --color-ui-gradient: radial-gradient(
    78.77% 78.77% at 71.71% 30.77%,
    #f0fcff 0%,
    #9bedff 67.21%,
    #98ecff 76.04%,
    #5be1ff 84.9%,
    #00bae2 94.79%
  );
  --color-ui-gradient-background: linear-gradient(
    137.1deg,
    #ecfcff 27.5%,
    #a6efff 94.09%
  );
  --color-ui-gradient-flip-background: radial-gradient(
    140% 190% at 117.54% 131.12%,
    #f0fcff 0%,
    #9bedff 25.52%,
    #98ecff 42.71%,
    #5be1ff 60.94%,
    #00bae2 94.79%
  );
  --color-scroll-pink: #ffd7fd;
  --color-scroll-pink-lt: #ffe9fe;
  --color-scroll-gradient: linear-gradient(
    317.42deg,
    #ffe9fe 10.4%,
    #ff96f9 83.03%
  );
  --ease-in: cubic-bezier(0.755, 0.05, 0.855, 0.06);
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.86, 0, 0.07, 1);
  --ease-out-quart: cubic-bezier(0.175, 0.79, 0.38, 0.905);
  --ease-in-out-quart: cubic-bezier(0.645, 0.045, 0.355, 1);
}

body {
  background-color: var(--color-just-black);
  font-family: "Mori", sans-serif, Arial;
  overscroll-behavior: none;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}


#smooth-content {
  overflow: visible;
  width: 100%;
  /* set a height because the contents are position: absolute, thus natively there's no height */
  height: 4000px;

  background-image:
    linear-gradient(rgba(255,255,255,.07) 2px, transparent 2px),
    linear-gradient(90deg, rgba(255,255,255,.07) 2px, transparent 2px),
    linear-gradient(rgba(255,255,255,.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.06) 1px, transparent 1px);
  background-size: 100px 100px, 100px 100px, 20px 20px, 20px 20px;
  background-position: -2px -2px, -2px -2px, -1px -1px, -1px -1px;
}

button {
  position: relative; 
}

.box {
  width: 100px;
  height: 100px;
  background: var(--gradient-macha);
  border-radius: 10px;
  position: absolute;
  z-index: 100;
  line-height: 100px;
  font-size: 18px;
  text-align: center;
  will-change: transform;
}
.box-ref {
  top: 80vh;
  left : 100px;
}
.box-a {
  top: 80vh;
  left : 250px;
  height:100px;

}

.box-b {
  left : 400px;
  top: 80vh;
  height:200px
}
.box-c {
  width: 100px;
  height: 400px;
  left : 550px;
  top: 80vh;

}

.middle {
  position:fixed;
  top:50%;
  height:2px;
  width:100%;
  background:red;
  transform:translateY(-50%);
}

.refline {
  position:absolute;
  top:80vh;
  background:var(--color-shockingly-green);
  height:2px;
  width:100%;
  z-index:200;
}

h2 {
  margin:0;
  position:fixed;
  color:var(--color-surface75);
  font-size: 1rem;
  padding:1em;
  font-weight:normal;
  background: var(--color-grey-dark);
  border-radius: 20px;
  max-width: 60ch;
  bottom: 1rem;
  right: 1rem;
}
```

JS:
```js
gsap.registerPlugin(ScrollTrigger, ScrollSmoother);

// create the smooth scroller FIRST!
let smoother = ScrollSmoother.create({
  smooth: 2,   // seconds it takes to "catch up" to native scroll position
  effects: true // look for data-speed and data-lag attributes on elements and animate accordingly
});
```

Explain how this demo works, then help me adapt it for my own project.


---


### SplitText

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


### Screen reader-only 

In the example below, the link may not be recognized as such by some screen readers:

```html
<h2 aria-label="This link isn't accessible">
  <div aria-hidden="true">This</div>
  <div aria-hidden="true"><a href="#">link</a></div>
  <div aria-hidden="true">isn't</div>
  <div aria-hidden="true">accessible</div>
</h2>
```


If you need to preserve the semantics and functionality of nested elements - like links, <strong> tags or <em> tags - we recommend disabling the default aria settings for the SplitText with aria: "none"*, and creating a screen reader-only duplicate of your element instead. This way, sighted users will see the animated text, while visually impaired people will get the screenreader-only content announced to them.</strong> </em>


#### Prompt netsed link


I'm working with a GSAP demo from the GSAP docs: "Accessible text by duplication".
Docs page: https://gsap.com/docs/v3/Plugins/SplitText/
CodePen: https://codepen.io/GreenSock/pen/12697152a77fa81cefd0e6bb3d87c2da
GSAP plugins used: SplitText

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="container">
  <div class="animate-me" aria-hidden="true">
    This text has a <a href="https://testlink.com">nested link</a> so we have created a duplicate "screenreader-only" element to preserve the semantics of child elements for screenreaders.
  </div>
  <p class="sr-only">
    This text has a <a href="https://testlink.com">nested link</a> so we have created a duplicate "screenreader-only" element to preserve the semantics of child elements for screenreaders.
  </p>
</div>
```

CSS:
```css
/* Hiding class, making content visible only to screen readers but not visually */
/* "sr" meaning "screen-reader" */
/* https://css-tricks.com/inclusively-hidden/ */
.sr-only:not(:focus):not(:active) {
  clip: rect(0 0 0 0); 
  clip-path: inset(50%);
  height: 1px;
  overflow: hidden;
  position: absolute;
  white-space: nowrap; 
  width: 1px;
}

html, body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
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
  opacity: 0;
}

.animate-me {
  color: #dfdcff;
  font-size: 25px;
  box-sizing: border-box;
  padding: 5%;
  width: 100%;
  text-align: left;
  perspective: 500px;
}

a {
  color: var(--color-orangey)
}
```

JS:
```js
gsap.registerPlugin(SplitText);

document.fonts.ready.then(() => {
  gsap.set(".container", { opacity: 1 });
  let split = SplitText.create(".animate-me", { type: "words", aria: "hidden" });

  gsap.from(split.words, {
    opacity: 0,
    duration: 2,
    ease: "sine.out",
    stagger: 0.1,
  });
});
```

Explain how this demo works, then help me adapt it for my own project.


### Flip

https://cdn.jsdelivr.net/npm/gsap@3.15/dist/Flip.min.js

#### Flip Prompt


I'm working with a GSAP demo from the GSAP docs: "How GSAP's Flip Plugin Works".
A step by step instruction of how the FLIP technique works in GSAP's Flip Plugin.

Loosely based on David K Piano's original pen: https://codepen.io/davidkpiano/pen/EbwrQQ?editors=0100
Docs page: https://gsap.com/docs/v3/Plugins/Flip/
CodePen: https://codepen.io/GreenSock/pen/ad75564d0ac3e9c6dcaf26e85838ee2a
GSAP plugins used: Flip

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Flip.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<section id="flip" data-state="initial">
	<button id="prev">&lsaquo;</button>

	<div class="window">
		<div class="boxPosition initialPosition"></div>
		<div class="box gradient-blue">Flip</div>
		<div class="finalContainer"><div class="boxPosition finalPosition"></div></div>
	</div>

	<div class="steps">
		<p>If we reparent the blue div into a new rotated &amp; scaled container (altering the DOM structure), how could we animate there seamlessly? Use the "FLIP" animation technique! Press the right arrow to begin.</p>

		<p><strong>"First":</strong> Get the initial state.<br/><code>const state = <a href="https://greensock.com/docs/v3/Plugins/Flip/static.getState()">Flip.getState(targets)</a></code></p>
		<p><strong>"Last":</strong> Put elements in their final state. In this case we'll place the element in the new container &lt;div&gt; which results in a totally different position, scale, and rotation.</p>
		<p><strong>"Invert":</strong> Make the element <i>appear</i> in its previous position/size by applying offsets instantly. That way, it <i>looks</i> like it hasn't moved yet. <i>Note: we animate this step in the demo to illustrate what normally happens immediately.</i></p>
		<p><strong>"Play":</strong> Animate the removal of those offsets.<br/>
			<code><a href="https://greensock.com/docs/v3/Plugins/Flip/static.from()">Flip.from(state, options)</a></code> returns a GSAP timeline so you can add other animations, control it, etc.
		</p>

		<p>GSAP's <a href="https://greensock.com/docs/v3/Plugins/Flip">Flip Plugin</a> makes this a breeze! </p>
	</div>

	<button id="next">&rsaquo;</button>
</section>
```

CSS:
```css
* {
  box-sizing: border-box;
}

html, body {
	width: 100%;
	height: 100%;
	margin: 0;
	padding: 0;
	font-weight: 300;
  font-size: 1rem;
}

.window {
	position: relative;
	height: 70vh;
	width: 40vw;
	border-top: 2rem solid #474b4c;
	border-radius: .5rem;
	background-color: #252525;
	overflow: hidden;
}

body, section {
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
}

#flip {
	width: 100%;
}

section > .steps, section > .window {
	flex-basis: 50%;
}

button {
	appearance: none;
	flex: 0 0 auto;
	display: flex;           
	align-items: center;     
	justify-content: center;
	width: 2.75rem;
	height: 2.75rem;
	margin: 0 1rem;
	padding: 0;
	border: 1px solid var(--color-surface25, #42433d);
	border-radius: 50%;
	background: transparent;
	color: var(--color-surface50, #7c7c6f);
	font-size: 0; /* hides the ‹ › characters */
	cursor: pointer;
	transition: color 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}

button::before {
	content: "";
	width: 1.25rem;
	height: 1.25rem;
	background: currentColor; /* so hover/focus colors still apply */
	-webkit-mask: var(--chevron) center / contain no-repeat;
	mask: var(--chevron) center / contain no-repeat;
}

#prev {
	--chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M15 6l-6 6 6 6'/%3E%3C/svg%3E");
}

#next {
	--chevron: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M9 6l6 6-6 6'/%3E%3C/svg%3E");
}

button:hover {
	color: var(--color-surface-white, #fffce1);
	border-color: var(--color-surface-white, #fffce1);
}

#prev:hover { transform: translateX(-2px); }
#next:hover { transform: translateX(2px); }

button:active {
	transform: scale(0.94);
}

button:focus-visible {
	outline: none;
	border-color: var(--color-shockingly-green, #0ae448);
	box-shadow: 0 0 0 3px rgba(10, 228, 72, 0.3);
}

button:disabled {
	opacity: 0.3;
	cursor: default;
	pointer-events: none;
}


.steps {
	padding: 0 2rem;
  font-size: 1.1em;
}

.steps p:not(:first-child) {
	display: none;
}

.box, .boxPosition {
	position: absolute;
	top: 8px;
	left: 8px;
	height: 10vmin!important;
	width: 10vmin!important;
  box-sizing: content-box;
}

.boxPosition {
	top: 6px;
	left: 6px;
	visibility: hidden;
	opacity: 0;
}

.box {
	text-align: center;
	line-height: 10vmin;
	font-size: 3.5vmin;
	font-weight: 400;
	border-radius: 1vmin;
}

.initialPosition {
  border-radius: 5px;
	border: 2px dashed var(--color-blue);
}

.finalPosition {
  border-radius: 10px;
	border: 2px dashed var(--color-surface-white);
}

.finalContainer {
  position: relative;
	width: 36vmin;
	height: 36vmin;
	position: absolute;
	bottom: 0;
	right: 0;
	border: 1px dashed var(--color-surface50);
  border-radius: 10px;
	transform: translate(15vmin, -12vmin) scale(1.5) rotate(-30deg);
	color: var(--color-surface75);
	padding: 1vmin;
	font-size: 2vmin;
  overflow: visible;
}

.finalContainer:after {
  content: "new container";
  position: absolute;
  bottom: 100%;
  left: 0;
  padding-bottom: 0.25rem;
  font-size: 0.9rem;
  z-index: -1;
}
.logo {
  position: absolute;
  width: 60px;
  bottom: 20px;
  right: 30px;
}

code {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  display: inline-block;
  font-size: 1rem;
}

.gsap-logo {
  max-width: 100px;
}
```

JS:
```js
gsap.registerPlugin(Flip);

let states = [ toInitState, toFirstState, toLastState, toInvertState, toPlayState, toEndState ],
	stateIndex = 0,
	stateIndexWrap = gsap.utils.wrap(0, states.length),
	stepBlurbs = gsap.utils.toArray('.steps p'),
	boxEl = document.querySelector(".box"),
	windowEl = document.querySelector(".window"),
	finalContainerEl = document.querySelector(".finalContainer");

gsap.defaults({ duration: 0.4, overwrite: 'auto' });

document.querySelector('#prev').addEventListener('click', () => goToState(stateIndex - 1));
document.querySelector('#next').addEventListener('click', () => goToState(stateIndex + 1));

let transition;
function resize() {
  transition && transition.kill();

	// reset (put back in original container and remove any inline styles)
	windowEl.appendChild(boxEl);
	boxEl.style.cssText = "";

	// grab the original state
	const state = Flip.getState(boxEl);

	// put into the new container
	finalContainerEl.appendChild(boxEl);

	// FLIP!
	transition = Flip.from(state, {
		scale: true,
		duration: 1,
		repeat: -1,
		repeatDelay: 1.5,
		ease: "power1.inOut",
		paused: true
	}).progress(1).progress(0); // lock in the starting/ending values.

	if (stateIndex === 2 || stateIndex === 3) {
		transition.progress(1);
	} else if (stateIndex === 4 || stateIndex === 5) {
		transition.play();
	}
}

function goToState(newState) {
	stateIndex = stateIndexWrap(newState);
	states[stateIndex]();
}

function updateBlurb() {
	const textState = Flip.getState(stepBlurbs);

	gsap.set(stepBlurbs, { display: 'none' });
  gsap.set(stepBlurbs[stateIndex], { display: 'block' });

	Flip.from(textState, {
		duration: 0.4,
		absolute: true,
		onLeave: elements => gsap.to(elements, {opacity: 0, duration: 0.3}),
		onEnter: elements => gsap.fromTo(elements, {opacity: 0}, {opacity: 1, duration: 0.3})
	});
}

function toInitState() {
	transition.pause(0);
	gsap.to(boxEl, {opacity: 1});
	gsap.to(".boxPosition", {autoAlpha: 0});
	updateBlurb();
}

function toFirstState() {
	transition.pause(0);
	gsap.to(boxEl, {opacity: 0.5});
	gsap.to(".initialPosition", {autoAlpha: 1});
	gsap.to(".finalPosition", {autoAlpha: 0});
	updateBlurb();
}

function toLastState() {
	gsap.killTweensOf(transition);
	gsap.set(boxEl, {opacity: 1});
	transition.progress(1).pause();
	gsap.to(".finalPosition", {autoAlpha: 1});
	updateBlurb();
}

function toInvertState() {
	transition.tweenFromTo(">", 0, {duration: 1, overwrite: true});
	updateBlurb();
}

function toPlayState() {
	gsap.killTweensOf(transition);
	gsap.to('.boxPosition', { autoAlpha: 1 });
	transition.play();
	updateBlurb();
}

function toEndState() {
	gsap.to(boxEl, { opacity: 1 });
	gsap.to('.boxPosition', { autoAlpha: 1 });
	transition.play();
	updateBlurb();
}

function init() {
	window.addEventListener('resize', resize);
	resize();
}

init();

// document.addEventListener("click", e => {
//   if (e.target.tagName.toLowerCase() === "button") {
//     return;
//   }
//   if (e.pageX < window.innerWidth / 4) {
//     goToState(stateIndex - 1);
//   } else {
//     goToState(stateIndex + 1);
//   }
// });
```

Explain how this demo works, then help me adapt it for my own project.


### CSSRule

#### CSSRule Prompt

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

### Draggable

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

### Draw SVG

[Draw SVG `Quick Start`](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/DrawSVGPlugin.min.js)


#### DrawSVG Prompt 


I'm working with a GSAP demo from the GSAP docs: "DrawSVGPlugin Values".
Demonstrates the various types of values that can be passed to GSAP's DrawSVGPlugin. This pen is used on the DrawSVGPlugin product page.
Learn more at www.greensock.com/drawSVG
Docs page: https://gsap.com/docs/v3/Plugins/DrawSVGPlugin
CodePen: https://codepen.io/GreenSock/pen/d99f307bef8b65451613ba899154515b
GSAP plugins used: DrawSVGPlugin, TextPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/DrawSVGPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/TextPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<svg version="1.1"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 width="516.3px" height="190px" viewBox="0 0 516.3 190" style="enable-background:new 0 0 516.3 211.99;"
	 xml:space="preserve">
<defs>
  <linearGradient id="orange" gradientUnits="userSpaceOnUse"
    x1="23.2" y1="-11.7" x2="493.1" y2="201.7">
    <stop offset="19.42%" stop-color="#ff8709"/>
    <stop offset="73.08%" stop-color="#f7bdf8"/>
  </linearGradient>
</defs>
  <path id="template" d="M9.13,99.99c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
	<path id="path" d="M9.13,99.99c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
</svg>

<div id="code">drawSVG:<div id="current">"100%"</div></div>
<button id="next">Next Example</button>
```

CSS:
```css
@font-face {
	font-display: swap;
	font-family: Mori;
	font-weight: 400;
	src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}
@font-face {
	font-display: swap;
	font-family: Mori;
	font-weight: 600;
	src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}

:root {
	--color-shockingly-green: #0ae448;
	--color-lt-green: #abff84;
	--color-just-black: #0e100f;
	--color-surface-white: #fffce1;
	--color-surface75: #bbbaa6;
}

body {
	background-color: #1b1b1d;
	color: #ccc;
	text-align: center;
	padding-top: 1rem;
	margin: 0;
	font-family: Mori, system-ui, sans-serif;
	font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
	line-height: 1.45;
	-webkit-font-smoothing: antialiased;
}

/* Line */
#template,
#path {
	fill: none;
}

#template {
	stroke-width: 5px;
	stroke: #444;
}

#path {
	stroke: url(#orange);
	stroke-width: 20px;
	visibility: hidden;
}

#macha stop:first-child { stop-color: var(--color-shockingly-green); }
#macha stop:last-child  { stop-color: var(--color-lt-green); }

/* Code readout */
#code {
	font-size: 2rem;
	font-family: monospace;
	color: #777;
	margin: 20px;
	position: relative;
	visibility: hidden;
}

#current {
	display: inline-block;
	color: white;
}

/* Button */
button {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	gap: 0.5em;
	min-height: 2.5rem;
	padding: 0 1.25rem;
	border: 2px solid var(--color-surface75);
	border-radius: 99px;
	background: transparent;
	color: var(--color-surface75);
	font: 600 0.9rem/1 Mori, system-ui, sans-serif;
	cursor: pointer;
	transition: border-color 0.2s, color 0.2s;
}

button:hover {
	border-color: var(--color-surface-white);
	color: var(--color-surface-white);
}

button:focus-visible {
	outline: none;
	border-color: var(--color-shockingly-green);
	box-shadow: 0 0 0 3px rgba(10, 228, 72, 0.35);
}
```

JS:
```js
var values = "100%;40% 60%;20 350;50% 50%;true;10%".split(";"),
    currentIndex = 0;

//set the initial value
gsap.set("#path, #code", {visibility:"visible"});

function next() {
  
  gsap.killTweensOf(next); //in case the user clicks, clear any delayed calls to this method. 
  if (++currentIndex === values.length) {
    currentIndex = 0;
  }
  if (values[currentIndex] === "true") {
    gsap.set("#current", {text:(values[currentIndex])});
  } else {
  	gsap.set("#current", {text:('"' + values[currentIndex] + '"')});
  }
  gsap.to("#path", {drawSVG:values[currentIndex], duration: 1, ease:"power1.inOut"});
  
}

document.querySelector("#next").addEventListener("click", next);
```

Explain how this demo works, then help me adapt it for my own project.



#### Splitting a multi-segment  (Drawing a house) prompt

I'm working with a GSAP demo from the GSAP docs: "DrawSVG with splitPaths() helper function".
Docs page: https://gsap.com/docs/v3/Plugins/DrawSVGPlugin
CodePen: https://codepen.io/GreenSock/pen/yLEzJNE
GSAP plugins used: DrawSVGPlugin, MotionPathPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/CustomEase.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/DrawSVGPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MorphSVGPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Draggable.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Flip.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathHelper.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/GSDevTools.min.js

Stylesheets it loads:
- /demo-assets/pens/JGaKdQ.css

HTML:
```html
<svg width="221" viewBox="30 0 221 167" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
<linearGradient id="orange" gradientUnits="userSpaceOnUse"
  x1="45.2" y1="55.4" x2="234.1" y2="129.7">
  <stop offset="19.42%" stop-color="#ff8709"/>
  <stop offset="73.08%" stop-color="#f7bdf8"/>
</linearGradient>
  </defs>

  <path id="house" d="M61.0478 144.196V165.498C61.0478 165.498 85.042 166.284 94.0655 165.859C103.091 165.435 125.685 165.259 133.89 165.498C140.208 165.681 146.894 165.683 151.473 165.598C153.401 165.561 154.94 163.996 154.94 162.071V125.831C154.94 124.209 156.257 122.895 157.884 122.895H174.657C176.258 122.895 177.554 124.189 177.554 125.787V162.042C177.554 163.949 178.363 165.101 181.014 165.496C182.785 165.671 219.681 165.659 219.681 165.659M70.6818 102.437H199.213V156.28M66.8866 84.3983V48.0715M193.372 48.367V102.439M121.775 120.183H90.9849C84.9154 120.183 86.7854 140.902 87.0651 143.463C87.3428 146.026 116.088 143.95 120.563 144.531C123.901 144.965 121.775 120.181 121.775 120.181M122.041 63.8285H91.2503C83.5374 63.8285 87.157 84.5369 87.3305 87.1084C88.9086 89.8143 119.73 89.309 120.828 88.1761C123.168 85.7615 122.041 67.2456 122.041 67.2456M173.99 63.8285H143.199C137.13 63.8285 139 84.5471 139.279 87.1084C139.559 89.6717 168.302 87.5953 172.777 88.1761C176.115 88.6101 173.99 67.2456 173.99 67.2456M112.343 18.8418H73.3991L59.5861 48.0715C59.5861 48.0715 93.1101 47.1057 122.706 48.0715C140.982 48.6686 200.674 48.0715 200.674 48.0715L186.861 18.8418H153.25M160.366 143.728C160.914 143.151 161.755 143.053 162.349 143.618C162.945 144.182 162.986 145.107 162.437 145.684C161.889 146.261 160.961 146.269 160.364 145.706C159.768 145.142 159.817 144.305 160.364 143.728H160.366Z"
    stroke="url(#orange)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

CSS:
```css
body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: 0e100f;
}

svg {
  overflow: visible;
  width: 100%;
  height: 90vh;
}
```

JS:
```js
gsap.registerPlugin(MotionPathPlugin, DrawSVGPlugin);

/* 
There's only one <path> but it has a bunch of individual, disconnected segments ("M" commands)
so we'll use the helper function to split that into a bunch of <path> elements so that the browser
can render the stroke progressively in a correct manner.
*/

let paths = splitPaths("#house");
// to animate all the segments at once...
// gsap.from(paths, { drawSVG: 0, duration: 5 });

// but instead, let's animate each segment one-after-the-other and make sure there's a consistent speed.
let duration = 5,
    distance = 0,
    tl = gsap.timeline();
paths.forEach(segment => distance += segment.getTotalLength());
paths.forEach(segment => {
  tl.from(segment, {
    drawSVG: 0,
    ease: "none",
    duration: duration * (segment.getTotalLength() / distance)
  });
});

// helper function that busts apart a single <path> that has multiple segments into a <path> for each segment (indicated by an "M" command);
function splitPaths(paths) {
  let toSplit = gsap.utils.toArray(paths),
      newPaths = [];
  if (toSplit.length > 1) {
    toSplit.forEach(path => newPaths.push(...splitPaths(path)));
  } else {
    let path = toSplit[0],
        rawPath = MotionPathPlugin.getRawPath(path),
        parent = path.parentNode,
        attributes = [].slice.call(path.attributes);
    newPaths = rawPath.map(segment => {
      let newPath = document.createElementNS("http://www.w3.org/2000/svg", "path"),
          i = attributes.length;
      while (i--) {
        newPath.setAttributeNS(null, attributes[i].nodeName, attributes[i].nodeValue);
      }
      newPath.setAttributeNS(null, "d", "M" + segment[0] + "," + segment[1] + "C" + segment.slice(2).join(",") + (segment.closed ? "z" : ""));
      parent.insertBefore(newPath, path);
      return newPath;
    });
    parent.removeChild(path);
  }
  return newPaths;
}
```

Explain how this demo works, then help me adapt it for my own project.


---

### Easel

[Easel quick start plugin](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/EaselPlugin.min.js)

---

### GSDevTools

[GSDEevTools quick start plugin](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/GSDevTools.min.js)

#### GSDevTools prompts (methods -> GSDevTools.create() ) 

I'm working with a GSAP demo from the GSAP docs: "GSDevTools - Step 1: Load and Instantiate with default settings".
A demo explaining the basics of GSDevTools.
Visit https://greensock.com/gsdevtools for more info.

GSDevTools gives you a visual UI for interacting with and debugging GSAP animations, complete with advanced playback controls, keyboard shortcuts, global synchronization and more. Jump to specific scenes, set in/out points, play in slow motion to reveal intricate details, and even switch to a "minimal" mode on small screens.
Docs page: https://gsap.com/docs/v3/Plugins/GSDevTools
CodePen: https://codepen.io/GreenSock/pen/611c82e0d3531b431617f8adbfeb71fd
GSAP plugins used: GSDevTools

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/GSDevTools.min.js

Stylesheets it loads:
- /demo-assets/pens/JGaKdQ.css

HTML:
```html
<div class="boxes">
  <div class="box green"></div>
  <div class="box orange"></div>
  <div class="box purple"></div>
</div>
```

CSS:
```css
/* Global styles come from external css https://codepen.io/GreenSock/pen/JGaKdQ*/

body{display:flex;align-items:center;justify-content:center;min-height:100vh;}

.boxes {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width:100vw;
  margin-bottom: 100px;
}


.box {
  width: 50px;
  height: 50px;
}
```

JS:
```js
//timeline animates green and orange
var tl = gsap.timeline()
tl.to(".orange", {duration: 1, x: "100vw", xPercent: -100})
  .to(".green", {duration: 2, x: "100vw", xPercent: -100, ease:"bounce"})

//separate tween with a delay which makes it play after the timeline
gsap.to(".purple", {duration: 1, x: "100vw", xPercent: -100, rotation: 360, delay: 3})

//instantiate GSDevTools with default settings
GSDevTools.create();

// GSDevTools will control all animations on the Global Timeline
```

Explain how this demo works, then help me adapt it for my own project.

---

### Inertia

#### Example 1 
> Following example and prompt shows where you can drag and toss a green and bluwe box around the screen in a natural, fluid way


I'm working with a GSAP demo from the GSAP docs: "Draggable Demo".
Drag and throw elements and watch them continue naturally with momentum, respect bounds and optionally snap to a grid. This is the demo seen at http://www.greensock.com/draggable/
Docs page: https://gsap.com/docs/v3/Plugins/InertiaPlugin/
CodePen: https://codepen.io/GreenSock/pen/JjwZzNG
GSAP plugins used: Draggable, InertiaPlugin

Scripts it loads, in order:
- //cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Draggable.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/InertiaPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div>
<div id="container">
		<div class="box gradient-green" id="box1"><p>Drag and throw me</p></div>
		<div class="box gradient-blue" id="box2" ><p>Drag and throw me too</p></div>
</div>
<div class="controls">
				<ul>
					<li class="controlsTitle">Options</li>
					<li>
						<label><input type="checkbox" name="snap" id="snap" value="1" /> Snap end position to grid</label>
					</li>
					<li>
						<label><input type="checkbox" name="liveSnap" id="liveSnap" value="1" /> Live snap</label>
					</li>
				</ul>
			</div>
</div>
```

CSS:
```css
html,
body {
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow: hidden;
}
body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

#container {
  height: 801px;
  overflow: visible;
  padding: 0;
  position: relative;
}

.box {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 196px;
  height: 100px;
  position: absolute;
  top: 0;
  border-radius: 10px;
}

.controls {
  border: 1px solid #555;
  font-size: 18px;
  margin: 20px 0;
}
.controls ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.controls li {
  display: inline-block;
  padding: 8px 0 8px 10px;
  margin: 0;
}
.controls input {
  vertical-align: middle;
  cursor: pointer;
}
.controls .controlsTitle {
  border-right: 1px solid #555;
  border-bottom: none;
  padding-right: 10px;
}
```

JS:
```js
/*
See https://gsap.com/draggable/ for details. 
This demo uses InertiaPlugin which is a membership benefit of Club GreenSock, https://gsap.com/pricing/
*/
gsap.registerPlugin(InertiaPlugin);

var $snap = $("#snap"),
  $liveSnap = $("#liveSnap"),
	$container = $("#container"),
	gridWidth = $("body").width() / 5,
	gridHeight = 100,
	gridRows = 3,
	gridColumns = 5,
	i, x, y;

//loop through and create the grid (a div for each cell). Feel free to tweak the variables above
for (i = 0; i < gridRows * gridColumns; i++) {
	y = Math.floor(i / gridColumns) * gridHeight;
	x = (i * gridWidth) % (gridColumns * gridWidth);
	$("<div/>").css({position:"absolute", border:"1px solid #454545", width:gridWidth-1, height:gridHeight-1, top:y, left:x}).prependTo($container);
}

//set the container's size to match the grid, and ensure that the box widths/heights reflect the variables above
gsap.set($container, {height: gridRows * gridHeight + 1, width: gridColumns * gridWidth + 1});
gsap.set(".box", {width:gridWidth, height:gridHeight});
gsap.set("#box2", {left: gridWidth * 2})

//the update() function is what creates the Draggable according to the options selected (snapping).
function update() {
  var snap = $snap.prop("checked"),
      liveSnap = $liveSnap.prop("checked");
	Draggable.create(".box", {
		bounds: $container,
		edgeResistance: 0.65,
		type: "x,y",
		inertia: true,
    autoScroll: true,
		liveSnap: liveSnap,
		snap:{
			x: function(endValue) {
				return (snap || liveSnap) ? Math.round(endValue / gridWidth) * gridWidth : endValue;
			},
			y: function(endValue) {
				return (snap || liveSnap) ? Math.round(endValue / gridHeight) * gridHeight : endValue;
			}
		}
	});
}

//when the user toggles one of the "snap" modes, make the necessary updates...
$snap.on("change", applySnap);
$liveSnap.on("change", applySnap);

function applySnap() {
	if ($snap.prop("checked") || $liveSnap.prop("checked")) {
		$(".box").each(function(index, element) {
			gsap.to(element, {
				x: Math.round(gsap.getProperty(element, "x") / gridWidth) * gridWidth,
				y: Math.round(gsap.getProperty(element, "y") / gridHeight) * gridHeight,
				delay: 0.1,
				ease: "power2.inOut"
			});
		});
	}
	update();
}

update();
```

Explain how this demo works, then help me adapt it for my own project.

#### Example 2

> The following example demonstrates using a custom end function for complex snapping that requires both x and y values, thus linkedProps is used:

I'm working with a GSAP demo from the GSAP docs: "Draggable 3 with snapping".
Docs page: https://gsap.com/docs/v3/Plugins/InertiaPlugin/
CodePen: https://codepen.io/GreenSock/pen/qBBWPPe
GSAP plugins used: Draggable, InertiaPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Draggable.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/InertiaPlugin.min.js

HTML:
```html
<!-- forked from <a href="https://codepen.io/osublake/">Blake Bowen.</a>
 -->
<svg id="svg" viewBox="0 0 400 400">

  <defs>
    <circle class="handle" r="10" />
    <circle class="marker" r="4" />  
    
    <linearGradient id="grad-1" x1="0" y1="0" x2="400" y2="400" gradientUnits="userSpaceOnUse">
       <stop offset="0.2" stop-color="#00bae2"></stop>
       <stop offset="0.8" stop-color="#fec5fb"></stop>
    </linearGradient>
  </defs>
  
  <polygon id="star" stroke="url(#grad-1)" points="261,220 298,335 200,264 102,335 139,220 42,149 162,148 200,34 238,148 358,149" />  
  <g id="marker-layer"></g>
  <g id="handle-layer"></g>
</svg>
```

CSS:
```css
body {
  background: #0e100f;
  font-family:sans-serif;
  color:#7c7c6f;
}

#svg {
  position: fixed;
  top: 10%;
  left: 10%;
  width: 80%;
  height: 80%;
  overflow: visible
}

#star {
  stroke-width: 20;
  stroke-linejoin: round;
  fill: none;
}

.handle {
  fill: transparent;
  stroke-width: 4;
  stroke: #fff;
}

.marker {
  fill: #fec5fb;
  stroke: #fec5fb;
  pointer-events: none;
}



a:link, a:visited, a:active {
  color:#7c7c6f;
  text-decoration:none;
}

a:hover {
  color:#00bae2;
}
```

JS:
```js
//original by Blake Bowen https://codepen.io/osublake/
var star = document.querySelector("#star");
var markerDef = document.querySelector("defs .marker");
var handleDef = document.querySelector("defs .handle");
var markerLayer = document.querySelector("#marker-layer");
var handleLayer = document.querySelector("#handle-layer");

var points = [];
var numPoints = star.points.numberOfItems;

for (var i = 0; i < numPoints; i++) {  
  var point = star.points.getItem(i);
  points[i] = {x:point.x, y:point.y};
  createHandle(point);
}

function createHandle(point) {
    
  var marker = createClone(markerDef, markerLayer, point);
  var handle = createClone(handleDef, handleLayer, point);
  var update = function() { point.x = this.x; point.y = this.y; };
  
  var draggable = new Draggable(handle, {
    onDrag: update,
    onThrowUpdate: update,
    inertia: true,
    bounds: window,
    liveSnap:{
      points:points,
      radius:15
    }
  });
}

function createClone(node, parent, point) {
  var element = node.cloneNode(true);
  parent.appendChild(element);
  gsap.set(element, { x: point.x, y: point.y });
  return element;
}
```

Explain how this demo works, then help me adapt it for my own project.

#### Example 3

> Although InertiaPlugin is commonly used with Draggable, Draggable is not required an InertiaPlugin can be used independently from Draggable.. Here's an example of Inertia's tracking being used directly:

I'm working with a GSAP demo from the GSAP docs: "Draggable bounce".
Docs page: https://gsap.com/docs/v3/Plugins/InertiaPlugin/
CodePen: https://codepen.io/GreenSock/pen/myyJrLE
GSAP plugins used: Draggable, InertiaPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Draggable.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/InertiaPlugin.min.js

HTML:
```html
<img class="ball" src="https://gsap.com/demo-assets/circle.webp" alt="" />
```

CSS:
```css
body {
  background: #0e100f;
  font-family:sans-serif;
  color:#7c7c6f;
  overflow: hidden;
}

.ball {
  width: 125px;
  height: 125px;
  border-radius: 50%;
  box-sizing: border-box;
  will-change: transform;
  position: absolute;
}
```

JS:
```js
//original by Blake Bowen https://codepen.io/osublake/
console.clear();

const friction = -0.5;

const ball = document.querySelector(".ball");
const ballProps = gsap.getProperty(ball);
const radius = ball.getBoundingClientRect().width / 2;
const tracker = InertiaPlugin.track(ball, "x,y")[0];

let vw = window.innerWidth;
let vh = window.innerHeight;

gsap.defaults({
  overwrite: true
});

gsap.set(ball, {
  xPercent: -50,
  yPercent: -50,
  x: vw / 2,
  y: vh / 2
});

const draggable = new Draggable(ball, {
  bounds: window,
  onPress() {
    gsap.killTweensOf(ball);
    this.update();
  },
  onDragEnd: animateBounce,
  onDragEndParams: []
});

window.addEventListener("resize", () => {
  vw = window.innerWidth;
  vh = window.innerHeight;
});

function animateBounce(x = "+=0", y = "+=0", vx = "auto", vy = "auto") {
    
  gsap.fromTo(ball, { x, y }, {
    inertia: {
      x: vx,
      y: vy,
    },
    onUpdate: checkBounds
  });  
}

function checkBounds() {
  
  let r = radius;    
  let x = ballProps("x");
  let y = ballProps("y");
  let vx = tracker.get("x");
  let vy = tracker.get("y");
  let xPos = x;
  let yPos = y;

  let hitting = false;

  if (x + r > vw) {
    xPos = vw - r;
    vx *= friction;
    hitting = true;

  } else if (x - r < 0) {
    xPos = r;
    vx *= friction;
    hitting = true;
  }

  if (y + r > vh) {
    yPos = vh - r;
    vy *= friction;
    hitting = true;

  } else if (y - r < 0) {
    yPos = r;
    vy *= friction;
    hitting = true;
  }

  if (hitting) {
    animateBounce(xPos, yPos, vx, vy);
  } 
}
```

Explain how this demo works, then help me adapt it for my own project.


### MorphSVG

[MorphSVG CDN Link](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/MorphSVGPlugin.min.js)

#### Example 1

> MorphSVG morphs an SVG <path> by animating the data inside the d attribute. For example, you can morph a diamond into a lightning bolt with a single line of code:

I'm working with a GSAP demo from the GSAP docs: "MorphSVG - simple morph".
Docs page: https://gsap.com/docs/v3/Plugins/MorphSVGPlugin
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


#### Example 2 Prompt

> Morph into multiple shapes

> Rendering to canvas
> SVG is fantastic, but sometimes developers prefer a canvas-based animation (often for rendering performance reasons). The MorphSVG plugin allows you to define a render function that'll be called every time the path updates.



I'm working with a GSAP demo from the GSAP docs: "Canvas Morphing".
Using GreenSock's MorphSVG Plugin to do morphing on the canvas.
Docs page: https://gsap.com/docs/v3/Plugins/MorphSVGPlugin
CodePen: https://codepen.io/GreenSock/pen/WYWZab
GSAP plugins used: MorphSVGPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MorphSVGPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<div class="container">
  <h2>Canvas</h2>
  <canvas></canvas>
</div>

<div class="container">
  <h2>SVG</h2>

<div class="container">
  <svg id="svg-stage" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" fill="none">
    <defs>
      <linearGradient id="grad" x1="0" y1="0" x2="99" y2="99" gradientUnits="userSpaceOnUse">
        <stop offset="0.2" stop-color="rgb(255, 135, 9)" />
        <stop offset="0.7" stop-color="rgb(247, 189, 248)" />
      </linearGradient>
      <path id="shape2" d="M20,1 85,1 85,66 51,98 51,66 20,66z">
        <path id="shape3" d="M47.1,0.8 73.3,0.8 61.9,37.2 77.1,37.2 30.7,99.4 45.8,51.9 29,51.9z" />
        <path id="shape4" d="M50,1l49,49L50,99L1,50L50,1z" />
    </defs>

    <path id="shape1" fill="url(#grad)" d="M74.6 50.2h-.2v-.4h.2a24.4 24.4 0 1 0-24.4-24.4v.2h-.4v-.2a24.4 24.4 0 1 0-24.4 24.4h.2v.4h-.2a24.4 24.4 0 1 0 24.4 24.4v-.2h.4v.2a24.4 24.4 0 1 0 24.4-24.4z" />
  </svg>

</div>
```

CSS:
```css
body {
  width:100%;
  height:100vh;
  margin:0;
  padding:0;
  background:#0e100f;
  display:flex;
  align-items:center;
  justify-content:center;
  flex-wrap: wrap;
  gap:1rem;
}

.container svg, canvas {
  width: 200px;
  height: 200px;  
}

.container {
  display: inline-block;  
  text-align: center;
  visibility: hidden;
}
```

JS:
```js
let shape    = document.querySelector("#shape1");
let canvas   = document.querySelector("canvas");
let ctx      = canvas.getContext("2d");
let size     = 200;
let viewBox  = {x:0, y:0, width:100, height:100};
let sizeRatio = size / viewBox.width;

const gradient = ctx.createLinearGradient(0, 0, viewBox.width, viewBox.height);
gradient.addColorStop(0.2, "rgb(255, 135, 9)");
gradient.addColorStop(0.7, "rgb(247, 189, 248)");

setDisplay();

gsap.defaults({ease: "power2.inOut"});
gsap.set(".container", { autoAlpha: 1 });

//set a default render function for all morphSVG animations. You can set it on a per-animation basis too, like morphSVG:{shape:"#id", render:yourFunction}
// MorphSVGPlugin.defaultRender = draw;

var tl = gsap.timeline({ repeat: -1, id:"morphing", paused:false,  defaults: { duration: 2, ease: "expo.inOut" }})  
  .to(shape, { morphSVG: {shape: "#shape2", render: draw} })
  .to(shape, { morphSVG: {shape: "#shape3", render: draw} }, "+=0.5")
  .to(shape, { morphSVG: {shape: "#shape4", render: draw} }, "+=0.5")
  .to(shape, { morphSVG: {shape: "#shape1", render: draw} }, "+=0.5")

tl.progress(0.0001); //just to force the first render;
// GSDevTools.create({animation:tl, globalSync:false, paused:true});

document.body.addEventListener("click", function() {
  tl.paused(!tl.paused());
});


function draw(rawPath, target) {
  var l, segment, j, i;
  ctx.clearRect(0, 0, size, size);
  ctx.fillStyle = gradient;
  ctx.fill("evenodd");
  ctx.beginPath();
  for (j = 0; j < rawPath.length; j++) {
    segment = rawPath[j];
    l = segment.length;
    ctx.moveTo(segment[0], segment[1]);
    for (i = 2; i < l; i+=6) {
      ctx.bezierCurveTo(segment[i], segment[i+1], segment[i+2], segment[i+3], segment[i+4], segment[i+5]);
    }
    if (segment.closed) {
      ctx.closePath();
    }
  }
  ctx.fill("evenodd");
}





function setDisplay() {
  var ratio = window.devicePixelRatio || 1;
  canvas.width  = size * ratio;
  canvas.height = size * ratio;
  gsap.set(canvas, { width: size, height: size });
  ratio *= sizeRatio;
  ctx.translate(-viewBox.x * ratio, -viewBox.y * ratio);
  ctx.scale(ratio, ratio);
}
```

Explain how this demo works, then help me adapt it for my own project.

---

### MotionPath

[CDN Link](https://cdn.jsdelivr.net/npm/gsap@3.15/dist/MotionPathPlugin.min.js)

> MotionPath prompt

#### Example and prompt 1


I'm working with a GSAP demo from the GSAP docs: "MotionPathPlugin Demo".
GSAP 3.0 introduces a brand new MotionPathPlugin which replaces BezierPlugin. Much more powerful and convenient.
Docs page: https://gsap.com/docs/v3/Plugins/MotionPathPlugin
CodePen: https://codepen.io/GreenSock/pen/9bdac66e1cb0ad0aa24396565f340e9c
GSAP plugins used: MotionPathPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathHelper.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<svg width="100%" height="100%" viewBox="-20 0 557 190" id="svg">
  	<defs>
		<linearGradient id="orange-crush" gradientUnits="userSpaceOnUse" x1="0.6" y1="-1.5" x2="84.4" y2="31.5">
			<stop offset="19.42%" style="stop-color: var(--color-orangey, #ff8709)" />
			<stop offset="73.08%" style="stop-color: #f7bdf8" />
		</linearGradient>
	</defs>
	<path id="path" fill="none" d="M9,100c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
	<g id="rect">
		<rect width="85" height="30"  />
		<text x="18" y="19" font-size="10">SVG &lt;rect&gt;</text>
	</g>
</svg>

<div id="div">#div</div>
```

CSS:
```css
/* GSAP brand: fonts, type sizes, colour vars, buttons and form controls.
   Element selectors only, so a demo's own class-based styles still win. */

/* Fonts */
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 600;
  src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: "Fraktion Mono";
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

/* Colours */
:root {
  --color-shockingly-green: #0ae448;
  --color-just-black: #0e100f;
  --color-surface-white: #fffce1;
  --color-pink: #fec5fb;
  --color-shockingly-pink: #f100cb;
  --color-orangey: #ff8709;
  --color-lilac: #9d95ff;
  --color-lt-green: #abff84;
  --color-blue: #00bae2;
  --color-grey: #191919;
  --color-surface75: #bbbaa6;
  --color-surface50: #7c7c6f;
  --color-surface25: #42433d;

  --gradient-macha: linear-gradient(114.41deg, var(--color-shockingly-green) 20.74%, var(--color-lt-green) 65.5%);
  --gradient-orange-crush: linear-gradient(111.45deg, var(--color-orangey) 19.42%, #f7bdf8 73.08%);
  --gradient-lipstick: linear-gradient(165.72deg, #f7bdf8 21.15%, #cd237f 81.93%);
  --gradient-purple-haze: linear-gradient(153.58deg, #f7bdf8 32.25%, #2f3cc0 92.68%);
  --gradient-skyfall: linear-gradient(131.77deg, #0a157a 30.82%, #15bfe4 81.82%);
  --gradient-emerald-city: linear-gradient(166.9deg, var(--color-shockingly-green) 53.19%, #0085d0 107.69%);
  --gradient-summer-fair: linear-gradient(144.02deg, var(--color-blue) 4.56%, var(--color-pink) 72.98%);

  /* Short names many demos use */
  --dark: var(--color-just-black);
  --light: var(--color-surface-white);
  --mid: var(--color-surface50);
  --grey: var(--color-grey);
  --gray: var(--color-grey);
  --green: var(--color-shockingly-green);
  --green-light: var(--color-lt-green);
  --blue: var(--color-blue);
  --purple: var(--color-lilac);
  --pink: var(--color-pink);
  --orange: var(--color-orangey);
  --red: #cd237f;

  /* Form controls */
  --field-bg: #1c1d1f;
  --field-border: var(--color-surface25);
  --field-radius: 8px;
  --focus-ring: 0 0 0 3px rgba(10, 228, 72, 0.35);

  accent-color: var(--color-shockingly-green);
  color-scheme: dark;
}

/* Type */
* { box-sizing: border-box; }

body {
  margin: 0;
  background-color: var(--color-just-black);
  color: var(--color-surface75);
  font-family: Mori, system-ui, sans-serif;
  font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  line-height: 1.45;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  margin: 0.5em 0;
  color: var(--color-surface-white);
  font-weight: 400;
  line-height: 1.2;
}
h1 { font-size: clamp(2rem, 1.6rem + 2vw, 2.875rem); }
h2 { font-size: clamp(1.625rem, 1.4rem + 1.2vw, 2.2rem); }
h3 { font-size: clamp(1.375rem, 1.25rem + 0.6vw, 1.75rem); }
h4 { font-size: clamp(1.125rem, 1rem + 0.5vw, 1.4rem); }

a { color: inherit; text-underline-offset: 0.15em; }

code, pre, kbd { font-family: "Fraktion Mono", ui-monospace, Menlo, monospace; }

/* Buttons */
button,
input[type="button"],
input[type="submit"],
input[type="reset"] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
  min-height: 2.5rem;
  padding: 0 1.25rem;
  border: 2px solid var(--color-surface75);
  border-radius: 99px;
  background: var(--color-just-black);
  color: var(--color-surface75);
  font: 600 0.9rem/1 Mori, system-ui, sans-serif;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}
button:hover,
input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {
  border-color: var(--color-surface-white);
  color: var(--color-surface-white);
}
button:disabled,
input:disabled { opacity: 0.4; cursor: not-allowed; }

/* Form controls */
label { color: var(--color-surface75); font-size: 0.9rem; }

input[type="text"],
input[type="number"],
input[type="email"],
input[type="search"],
input[type="url"],
input:not([type]),
select,
textarea {
  min-height: 2.5rem;
  padding: 0 0.75rem;
  border: 1px solid var(--field-border);
  border-radius: var(--field-radius);
  background: var(--field-bg);
  color: var(--color-surface-white);
  font: 400 0.9rem/1.2 Mori, system-ui, sans-serif;
  transition: border-color 0.2s, box-shadow 0.2s;
}
textarea { padding: 0.6rem 0.75rem; line-height: 1.45; }
input::placeholder,
textarea::placeholder { color: var(--color-surface50); }

input[type="checkbox"],
input[type="radio"] {
  width: 1.1em;
  height: 1.1em;
  margin: 0 0.4em 0 0;
  vertical-align: -0.15em;
}
input[type="range"] { width: min(100%, 18rem); }

button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: none;
  border-color: var(--color-shockingly-green);
  box-shadow: var(--focus-ring);
}


html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

body {
  min-height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px 15px;
}

svg {
  overflow: visible;
  height: 100%;

  /* Fix Safari rendering bug */
  transform: translateZ(0);
}

circle {
  fill: var(--color-surface50);
}

path {
  stroke-width: 2;
  stroke: var(--color-surface50);
}

/* SVG rect: orange gradient */
#rect rect {
  fill: url(#orange-crush);
  rx: 8px;
}

#rect text {
  pointer-events: none;
  fill: var(--color-just-black);
  font-family: Mori, system-ui, sans-serif;
  font-weight: 600;
}

/* DIV: green gradient */
#div {
  position: absolute;
  top: 30%;
  left: 60%;
  width: 120px;
  height: 60px;
  pointer-events: none;
  background: var(--gradient-macha);
  border-radius: 12px;
  color: var(--color-just-black);
  font-size: 32px;
  font-weight: 600;
  line-height: 60px;
  text-align: center;
}

a {
  color: var(--color-shockingly-green);
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}

.gsap-3-logo {
  width: 20vw;
  max-width: 150px;
  position: fixed;
  bottom: 15px;
  right: 15px;
}
```

JS:
```js
//register the plugin (just once)
gsap.registerPlugin(MotionPathPlugin);

gsap.to("#rect", {
  duration: 5, 
  repeat: 12,
  repeatDelay: 3,
  yoyo: true,
  ease: "power1.inOut",
  motionPath:{
    path: "#path",
    align: "#path",
    autoRotate: true,
    alignOrigin: [0.5, 0.5]
  }
});
```

Explain how this demo works, then help me adapt it for my own project.

#### Example and prompt 2

I'm working with a GSAP demo from the GSAP docs: "GSAP 3 motionPath applied to scale with curviness".
Docs page: https://gsap.com/docs/v3/Plugins/MotionPathPlugin
CodePen: https://codepen.io/GreenSock/pen/vYBVQap
GSAP plugins used: MotionPathPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/xxmzBrw.css

HTML:
```html
<main>
  <div>
    <div class="box gradient-green" id="box-1"></div>
  <p>curviness: 0</p>
  </div>
  <div>
    <div class="box gradient-green" id="box-2"></div>
     <p>curviness: 2</p>
  </div>
	
	
</main>
```

CSS:
```css
main {
  text-align: center;
	width: 100%; min-height: 100vh;
	display: flex; flex-flow: row nowrap; justify-content: space-evenly; align-items: center;
}

main div {
  display:flex;align-items:center;justify-content:center;flex-direction: column;
}
.box {
  will-change: transform;
  margin-bottom: 2rem;
}
```

JS:
```js
var scales = [{scale:1.3}, {scale:0.2},	{scale:1}];

gsap.to('#box-1', {
	motionPath: {
		path: scales, 
		curviness: 0
	}, 
	duration: 3, 
	ease: "none",
	repeat: -1,
	repeatDelay: 1
});

gsap.to('#box-2', {
	motionPath: {
		path: scales, 
		curviness: 2
	}, 
	duration: 3, 
	ease: "none",
	repeat: -1,
	repeatDelay: 1
});
```

Explain how this demo works, then help me adapt it for my own project.


### MotionPathHelper


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


### Observer 


#### Demo
>Notice there's no actual scrolling in the demo below but you can use your mouse wheel (or swipe on touch devices) to initiate movement so it "feels" like a scroll:


I'm working with a GSAP demo from the GSAP docs: "Animated Continuous Sections with GSAP Observer".
Docs page: https://gsap.com/docs/v3/Plugins/Observer/
CodePen: https://codepen.io/GreenSock/pen/XWzRraJ
GSAP plugins used: Observer, SplitText

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Observer.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js

Stylesheets it loads:
- /demo-assets/pens/qEWKyrL.css

HTML:
```html
<!--
Sections animate in and out on scroll. Scroll up or down and the sections will wrap around after hitting the start or end. Uses GSAP for the animations.
-->

<header>
  <div>Animated Sections</div>
  <div><a href="https://codepen.io/BrianCross/pen/PoWapLP">Original Inspiration</a></div>
</header>
<section class="first">
  <div class="outer">
    <div class="inner">
      <div class="bg one">
        <h2 class="section-heading">Scroll down</h2>
      </div>
    </div>
  </div>

</section>
<section class="second">
  <div class="outer">
    <div class="inner">
      <div class="bg">
        <h2 class="section-heading">Animated with GSAP</h2>
      </div>
    </div>
  </div>
</section>
<section class="third">
  <div class="outer">
    <div class="inner">
      <div class="bg">
        <h2 class="section-heading">GreenSock</h2>
      </div>
    </div>
  </div>
</section>
<section class="fourth">
  <div class="outer">
    <div class="inner">
      <div class="bg">
        <h2 class="section-heading">Animation platform</h2>
      </div>
    </div>
  </div>
</section>
<section class="fifth">
  <div class="outer">
    <div class="inner">
      <div class="bg">
        <h2 class="section-heading">Keep scrolling</h2>
      </div>
    </div>
  </div>
</section>
```

CSS:
```css
* {
  box-sizing: border-box;
  user-select: none;
}

a {
  color: var(--color-surface-white);
  text-decoration: none;
}

body {
  margin: 0;
  padding: 0;
  height: 100vh;
  color: var(--light);
  text-transform: uppercase;
}

h2 {
  font-size: clamp(1rem, 6vw, 10rem);
  font-weight: 600;
  line-height: 1.2;
  text-align: center;
  margin-right: -0.5em;
  width: 90vw;
  max-width: 1200px;
  text-transform: none;
}

header {
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 5%;
  width: 100%;
  z-index: 3;
  height: 7em;
  font-size: clamp(0.66rem, 2vw, 1rem);
  letter-spacing: 0.5em;
}

section {
  height: 100%;
  width: 100%;
  top: 0;
  position: fixed;
  visibility: hidden;
}
section .outer,
section .inner {
  width: 100%;
  height: 100%;
  overflow-y: hidden;
}
section .bg {
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  background-size: cover;
  background-position: center;
}
section .bg h2 {
  z-index: 999;
}
section .bg .clip-text {
  overflow: hidden;
}

.first .bg {
  background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.6) 50%, rgba(0, 0, 0, 0.1) 100%), url("https://gsap.com/demo-assets/site-landscape-1.jpg");
}

.second .bg {
  background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.6) 50%, rgba(0, 0, 0, 0.1) 100%), url("https://gsap.com/demo-assets/site-landscape-2.jpg");
}

.third .bg {
  background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.6) 50%, rgba(0, 0, 0, 0.1) 100%), url("https://gsap.com/demo-assets/site-landscape-3.jpg");
}

.fourth .bg {
  background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.6) 50%, rgba(0, 0, 0, 0.1) 100%), url("https://gsap.com/demo-assets/site-landscape-4.jpg");
}

.fifth .bg {
  background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.6) 50%, rgba(0, 0, 0, 0.1) 100%), url("https://gsap.com/demo-assets/site-landscape-5.jpg");
  background-position: 50% 45%;
}

h2 * {
  will-change: transform;
}
```

JS:
```js
gsap.registerPlugin(Observer);

let sections = document.querySelectorAll("section"),
  images = document.querySelectorAll(".bg"),
  headings = gsap.utils.toArray(".section-heading"),
  outerWrappers = gsap.utils.toArray(".outer"),
  innerWrappers = gsap.utils.toArray(".inner"),
  splitHeadings = headings.map(heading => new SplitText(heading, { type: "chars,words,lines", linesClass: "clip-text" })),
  currentIndex = -1,
  wrap = gsap.utils.wrap(0, sections.length),
  animating;

gsap.set(outerWrappers, { yPercent: 100 });
gsap.set(innerWrappers, { yPercent: -100 });

function gotoSection(index, direction) {
  index = wrap(index); // make sure it's valid
  animating = true;
  let fromTop = direction === -1,
      dFactor = fromTop ? -1 : 1,
      tl = gsap.timeline({
        defaults: { duration: 1.25, ease: "power1.inOut" },
        onComplete: () => animating = false
      });
  if (currentIndex >= 0) {
    // The first time this function runs, current is -1
    gsap.set(sections[currentIndex], { zIndex: 0 });
    tl.to(images[currentIndex], { yPercent: -15 * dFactor })
      .set(sections[currentIndex], { autoAlpha: 0 });
  }
  gsap.set(sections[index], { autoAlpha: 1, zIndex: 1 });
  tl.fromTo([outerWrappers[index], innerWrappers[index]], { 
      yPercent: i => i ? -100 * dFactor : 100 * dFactor
    }, { 
      yPercent: 0 
    }, 0)
    .fromTo(images[index], { yPercent: 15 * dFactor }, { yPercent: 0 }, 0)
    .fromTo(splitHeadings[index].chars, { 
        autoAlpha: 0, 
        yPercent: 150 * dFactor
    }, {
        autoAlpha: 1,
        yPercent: 0,
        duration: 1,
        ease: "power2",
        stagger: {
          each: 0.02,
          from: "random"
        }
      }, 0.2);

  currentIndex = index;
}

Observer.create({
  type: "wheel,touch,pointer",
  wheelSpeed: -1,
  onDown: () => !animating && gotoSection(currentIndex - 1, -1),
  onUp: () => !animating && gotoSection(currentIndex + 1, 1),
  tolerance: 10,
  preventDefault: true
});

gotoSection(0, 1);

// original: https://codepen.io/BrianCross/pen/PoWapLP
// horizontal version: https://codepen.io/GreenSock/pen/xxWdeMK
```

Explain how this demo works, then help me adapt it for my own project.


### Physics2D

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

### PixiPlugin Filter Effects

#### ColorMatrixFilter Prompt

> Another big convenience is that PixiPlugin recognizes some special values like saturation, brightness, contrast, hue, and colorize (which all leverage a ColorMatrixFilter under the hood).

I'm working with a GSAP demo from the GSAP docs: "PixiPlugin for GSAP v3".
Demonstrates some of the fun filter-based effects that PixiPlugin for GSAP can do. PixiPlugin is new in GSAP 1.20.0. See https://greensock.com/1-20-0/
Docs page: https://gsap.com/docs/v3/Plugins/PixiPlugin/
CodePen: https://codepen.io/GreenSock/pen/e1f256723ce102d6b9a776fa7f6da9f4
GSAP plugins used: PixiPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- //cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/TextPlugin.min.js
- //cdnjs.cloudflare.com/ajax/libs/pixi.js/5.0.2/pixi.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/PixiPlugin.min.js
- https://cdnjs.cloudflare.com/ajax/libs/prettify/r298/prettify.min.js

Stylesheets it loads:
- /demo-assets/pens/JGaKdQ.css

HTML:
```html
<link href='//fonts.googleapis.com/css?family=Signika+Negative:300,400' rel='stylesheet' type='text/css'>

<div class="wrapper">
  
  <h2>PixiPlugin Filter Effects</h2>
  <div class="demo">
  <img src="https://gsap.com/demo-assets/car-dashboard-blur.jpg" width="300" height="300" cross-origin="anonymous">
  <canvas id="PixiApp" width="300" height="300"></canvas>
  </div>
  
  <pre class="code prettyprint lang-js">//sample code</pre>
  <div class="nav"></div>
  <form>
  <div>
    <input type="checkbox" id="combineCMF" name="combineCMF" value="false">
    <label for="combineCMF">combineCMF:true</label>
  </div>
    <p class="explanation">When combineCMF is set to true, the newly applied ColorMatrixFilter will preserve any previously-set "hue", "saturation", "brightness", "contrast", and "colorize" values. So if you desaturate the image and then increase brightness you will get a very bright grayscale image. However, if you desaturate the image and then click "colorize red" or "hue 180" you will not see any color change as the image will still have saturation of 0. combineCMF is false by default.</p>
</form>
  
  
</div>
```

CSS:
```css
/* Global styles come from external css https://codepen.io/GreenSock/pen/JGaKdQ*/
button {
  margin:0 6px 6px 0;
  padding: 9px 18px;
}
.explanation {
  font-weight: 300;
}



/*
 * Derived from einaros's Sons of Obsidian theme at
 * http://studiostyl.es/schemes/son-of-obsidian by
 * Alex Ford of CodeTunnel:
 * http://CodeTunnel.com/blog/post/71/google-code-prettify-obsidian-theme
 */

.str
{
    color: #EC7600;
}
.kwd
{
    color: #93C763;
}
.com
{
    color: #66747B;
}
.typ
{
    color: #678CB1;
}
.lit
{
    color: #FACD22;
}
.pun
{
    color: #F1F2F3;
}
.pln
{
    color: #9a8297;
}
.tag
{
    color: #8AC763;
}
.atn
{
    color: #E0E2E4;
}
.atv
{
    color: #EC7600;
}
.dec
{
    color: purple;
}
pre.prettyprint
{
    border: 0px solid #888;
}
ol.linenums
{
    margin-top: 0;
    margin-bottom: 0;
}
.prettyprint {
    background: #000;
}
li.L0, li.L1, li.L2, li.L3, li.L4, li.L5, li.L6, li.L7, li.L8, li.L9
{
    color: #555;
    list-style-type: decimal;
}
li.L1, li.L3, li.L5, li.L7, li.L9 {
    background: #111;
}
@media print
{
    .str
    {
        color: #060;
    }
    .kwd
    {
        color: #006;
        font-weight: bold;
    }
    .com
    {
        color: #600;
        font-style: italic;
    }
    .typ
    {
        color: #404;
        font-weight: bold;
    }
    .lit
    {
        color: #044;
    }
    .pun
    {
        color: #440;
    }
    .pln
    {
        color: #000;
    }
    .tag
    {
        color: #006;
        font-weight: bold;
    }
    .atn
    {
        color: #404;
    }
    .atv
    {
        color: #060;
    }
}

pre.prettyprint.code {
  padding:10px;
  margin-left:0px;
}

button:hover {
  background-color: #333;
  background-image: none;
}
```

JS:
```js
var image, currentButton, 
    combineCMF = false;
var app = new PIXI.Application({
    width:300,
    height:300,
		backgroundColor: 0x000000, 
    autoResize: true, 
    view:document.getElementById("PixiApp")
});

function createEffect(name, code, onVars, offVars){
  var button = $("<button/>").text(name).appendTo(".nav"),
      style = button[0].style;
  button[0]._enabled = false;
  button.click(function() {
    var isEnabled = !this._enabled;
    if (!combineCMF || name === "reset") {
      $(".nav button").each(function() {
        this.style.removeProperty("background-image");
        this.style.removeProperty("background-color");
        this._enabled = false;
      });
    }
    currentButton = this;
    this._enabled = isEnabled;
    var vars = isEnabled ? onVars : offVars;
    vars.combineCMF = combineCMF;
    gsap.to(image, {duration:1, pixi:vars});
    if (isEnabled) {
      style.backgroundImage = "none";
      style.backgroundColor = "#4e9816";
      $(".code").text("gsap.to(image, {duration: 1, pixi:{" + code + ((combineCMF && name.indexOf("blur") === -1 && name !== "reset")  ? ", combineCMF:true" : "") + "}});").removeClass("prettyprinted");
    } else {
      gsap.set(this, {clearProps:"backgroundImage,backgroundColor"});
    }
    
    PR.prettyPrint(); 
  });
}

//toggle combineCMF
$('#combineCMF').click(function(){
  combineCMF = $(this).is(':checked');
  if (currentButton) {
    currentButton.click();
  }
});


image = PIXI.Sprite.from("https://gsap.com/demo-assets/car-dashboard-blur.jpg"); //previously used this, but ran into CORS issues: new PIXI.Sprite(resources.image.texture);
image.width = image.height = 300;
app.stage.addChild(image);
createEffect("colorize red", 'colorize:"red", colorizeAmount:1', {colorize:"red", colorizeAmount:1}, {colorize:"red", colorizeAmount:0});
createEffect("desaturate", "saturation:0", {saturation:0}, {saturation:1});
createEffect("hue 180", 'hue:180', {hue:180}, {hue:0});
createEffect("brightness", 'brightness:3', {brightness:3}, {brightness:1});
createEffect("contrast", 'contrast:3', {contrast:3}, {contrast:1});
createEffect("blur", 'blur:20', {blur:10}, {blur:0});
createEffect("reset", 'colorMatrixFilter:null, blur:0', {colorMatrixFilter:null, blur:0}, {colorMatrixFilter:null, blur:0});
```

Explain how this demo works, then help me adapt it for my own project.


### ScrambleText

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


# Useful Features and Tools

## Available Utils

### Clamp

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

### Distributes

I'm working with a GSAP demo from the GSAP docs: "distributor demo basic".
Docs page: https://gsap.com/docs/v3/GSAP/UtilityMethods/distribute()
CodePen: https://codepen.io/GreenSock/pen/qBVyZmd

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/CustomEase.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js

Stylesheets it loads:
- https://unpkg.com/magic-input/dist/magic-input.min.css

HTML:
```html
<div id="demo">
	<svg id="ease-vis" viewBox="0 0 650 650">
		<defs>
			<linearGradient id="macha" gradientUnits="userSpaceOnUse"
				x1="29.1" y1="190.6" x2="620.9" y2="459.4">
				<stop offset="20.74%" style="stop-color: var(--color-shockingly-green, #0ae448)" />
				<stop offset="65.5%" style="stop-color: var(--color-lt-green, #abff84)" />
			</linearGradient>
		</defs>

		<!-- bars are generated by JS -->
		<g id="bars"></g>

		<!-- y axis: positioned by gsap -->
		<g id="markers">
			<text x="0" y="0" fill="#fff">1</text>
			<line x1="40" y1="0" x2="650" y2="0" stroke="#fff" />
			<text x="0" y="0" fill="#fff">0.75</text>
			<line x1="40" y1="0" x2="650" y2="0" stroke="#fff" />
			<text x="0" y="0" fill="#fff">0.5</text>
			<line x1="40" y1="0" x2="650" y2="0" stroke="#fff" />
			<text x="0" y="0" fill="#fff">0.25</text>
			<line x1="40" y1="0" x2="650" y2="0" stroke="#fff" />
			<text x="0" y="0" fill="#fff">0</text>
			<line x1="40" y1="0" x2="650" y2="0" stroke="#fff" />
		</g>
	</svg>
</div>
```

CSS:
```css
/* GSAP brand: fonts, type sizes, colour vars, buttons and form controls.
   Element selectors only, so a demo's own class-based styles still win. */

/* Fonts */
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 600;
  src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: "Fraktion Mono";
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

/* Colours */
:root {
  --color-shockingly-green: #0ae448;
  --color-just-black: #0e100f;
  --color-surface-white: #fffce1;
  --color-pink: #fec5fb;
  --color-shockingly-pink: #f100cb;
  --color-orangey: #ff8709;
  --color-lilac: #9d95ff;
  --color-lt-green: #abff84;
  --color-blue: #00bae2;
  --color-grey: #191919;
  --color-surface75: #bbbaa6;
  --color-surface50: #7c7c6f;
  --color-surface25: #42433d;

  --gradient-macha: linear-gradient(114.41deg, var(--color-shockingly-green) 20.74%, var(--color-lt-green) 65.5%);
  --gradient-orange-crush: linear-gradient(111.45deg, var(--color-orangey) 19.42%, #f7bdf8 73.08%);
  --gradient-lipstick: linear-gradient(165.72deg, #f7bdf8 21.15%, #cd237f 81.93%);
  --gradient-purple-haze: linear-gradient(153.58deg, #f7bdf8 32.25%, #2f3cc0 92.68%);
  --gradient-skyfall: linear-gradient(131.77deg, #0a157a 30.82%, #15bfe4 81.82%);
  --gradient-emerald-city: linear-gradient(166.9deg, var(--color-shockingly-green) 53.19%, #0085d0 107.69%);
  --gradient-summer-fair: linear-gradient(144.02deg, var(--color-blue) 4.56%, var(--color-pink) 72.98%);

  /* Short names many demos use */
  --dark: var(--color-just-black);
  --light: var(--color-surface-white);
  --mid: var(--color-surface50);
  --grey: var(--color-grey);
  --gray: var(--color-grey);
  --green: var(--color-shockingly-green);
  --green-light: var(--color-lt-green);
  --blue: var(--color-blue);
  --purple: var(--color-lilac);
  --pink: var(--color-pink);
  --orange: var(--color-orangey);
  --red: #cd237f;

  /* Form controls */
  --field-bg: #1c1d1f;
  --field-border: var(--color-surface25);
  --field-radius: 8px;
  --focus-ring: 0 0 0 3px rgba(10, 228, 72, 0.35);

  accent-color: var(--color-shockingly-green);
  color-scheme: dark;
}

/* Type */
* { box-sizing: border-box; }

body {
  margin: 0;
  background-color: var(--color-just-black);
  color: var(--color-surface75);
  font-family: Mori, system-ui, sans-serif;
  font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  line-height: 1.45;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  margin: 0.5em 0;
  color: var(--color-surface-white);
  font-weight: 400;
  line-height: 1.2;
}
h1 { font-size: clamp(2rem, 1.6rem + 2vw, 2.875rem); }
h2 { font-size: clamp(1.625rem, 1.4rem + 1.2vw, 2.2rem); }
h3 { font-size: clamp(1.375rem, 1.25rem + 0.6vw, 1.75rem); }
h4 { font-size: clamp(1.125rem, 1rem + 0.5vw, 1.4rem); }

a { color: inherit; text-underline-offset: 0.15em; }

code, pre, kbd { font-family: "Fraktion Mono", ui-monospace, Menlo, monospace; }

/* Buttons */
button,
input[type="button"],
input[type="submit"],
input[type="reset"] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
  min-height: 2.5rem;
  padding: 0 1.25rem;
  border: 2px solid var(--color-surface75);
  border-radius: 99px;
  background: var(--color-just-black);
  color: var(--color-surface75);
  font: 600 0.9rem/1 Mori, system-ui, sans-serif;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}
button:hover,
input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {
  border-color: var(--color-surface-white);
  color: var(--color-surface-white);
}
button:disabled,
input:disabled { opacity: 0.4; cursor: not-allowed; }

/* Form controls */
label { color: var(--color-surface75); font-size: 0.9rem; }

input[type="text"],
input[type="number"],
input[type="email"],
input[type="search"],
input[type="url"],
input:not([type]),
select,
textarea {
  min-height: 2.5rem;
  padding: 0 0.75rem;
  border: 1px solid var(--field-border);
  border-radius: var(--field-radius);
  background: var(--field-bg);
  color: var(--color-surface-white);
  font: 400 0.9rem/1.2 Mori, system-ui, sans-serif;
  transition: border-color 0.2s, box-shadow 0.2s;
}
textarea { padding: 0.6rem 0.75rem; line-height: 1.45; }
input::placeholder,
textarea::placeholder { color: var(--color-surface50); }

input[type="checkbox"],
input[type="radio"] {
  width: 1.1em;
  height: 1.1em;
  margin: 0 0.4em 0 0;
  vertical-align: -0.15em;
}
input[type="range"] { width: min(100%, 18rem); }

button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: none;
  border-color: var(--color-shockingly-green);
  box-shadow: var(--focus-ring);
}

body {
	overflow: hidden;
	display: flex;
	align-items: center;
	justify-content: center;
}

body,
html {
	height: 100%;
	width: 100%;
	margin: 0;
	padding: 0;
	font-size: 20px;
}

svg {
	overflow: visible;
	width: 650px;
	height: 650px;
}

.bar {
	fill: url(#macha);
}

path {
	stroke-width: 2px;
	fill: none;
}
#demo {
	margin-top: 50px;
	text-align: center;
}
```

JS:
```js
createEaseVis();

gsap.set("svg", { scale: 0.75 });
gsap.set(".bar", { transformOrigin: "50% 100%" });

let end = gsap.utils.distribute({
	base: 0.0,
	amount: 0.5,
	ease: "power2.in",
	from: "edges"
});

gsap.to(".bar", {
	scaleY: end
});

function createEaseVis() {
	let svgNS = "http://www.w3.org/2000/svg";
	let bars = document.getElementById("bars");

	for (let i = 0; i < 65; i++) {
		let rect = document.createElementNS(svgNS, "rect");
		rect.setAttribute("width", 9);
		rect.setAttribute("height", 650);
		rect.setAttribute("x", i * 10);
		rect.setAttribute("class", "bar");
		bars.appendChild(rect);
	}

	gsap.set("text", {
		y: gsap.utils.distribute({
			base: 5,
			amount: 650
		})
	});

	gsap.set("line", {
		y: gsap.utils.distribute({
			base: 0,
			amount: 650
		}),
		opacity: 0.4
	});
}
```

Explain how this demo works, then help me adapt it for my own project.


### Selector

> Selector prompt

I'm working with a GSAP demo from the GSAP docs: "React scoped selector".
Docs page: https://gsap.com/docs/v3/GSAP/UtilityMethods/selector()
CodePen: https://codepen.io/GreenSock/pen/BaWOZpM

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdnjs.cloudflare.com/ajax/libs/react/17.0.2/umd/react.production.min.js
- https://cdnjs.cloudflare.com/ajax/libs/react-dom/17.0.2/umd/react-dom.production.min.js

HTML:
```html
<div id="app"></div>
```

CSS:
```css
/* GSAP brand: fonts, type sizes, colour vars, buttons and form controls.
   Element selectors only, so a demo's own class-based styles still win. */

/* Fonts */
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 600;
  src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: "Fraktion Mono";
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

/* Colours */
:root {
  --color-shockingly-green: #0ae448;
  --color-just-black: #0e100f;
  --color-surface-white: #fffce1;
  --color-pink: #fec5fb;
  --color-shockingly-pink: #f100cb;
  --color-orangey: #ff8709;
  --color-lilac: #9d95ff;
  --color-lt-green: #abff84;
  --color-blue: #00bae2;
  --color-grey: #191919;
  --color-surface75: #bbbaa6;
  --color-surface50: #7c7c6f;
  --color-surface25: #42433d;

  --gradient-macha: linear-gradient(114.41deg, var(--color-shockingly-green) 20.74%, var(--color-lt-green) 65.5%);
  --gradient-orange-crush: linear-gradient(111.45deg, var(--color-orangey) 19.42%, #f7bdf8 73.08%);
  --gradient-lipstick: linear-gradient(165.72deg, #f7bdf8 21.15%, #cd237f 81.93%);
  --gradient-purple-haze: linear-gradient(153.58deg, #f7bdf8 32.25%, #2f3cc0 92.68%);
  --gradient-skyfall: linear-gradient(131.77deg, #0a157a 30.82%, #15bfe4 81.82%);
  --gradient-emerald-city: linear-gradient(166.9deg, var(--color-shockingly-green) 53.19%, #0085d0 107.69%);
  --gradient-summer-fair: linear-gradient(144.02deg, var(--color-blue) 4.56%, var(--color-pink) 72.98%);
  --color-ui-gradient: radial-gradient(
    78.77% 78.77% at 71.71% 30.77%,
    #f0fcff 0%,
    #9bedff 67.21%,
    #98ecff 76.04%,
    #5be1ff 84.9%,
    #00bae2 94.79%
  );
  /* Short names many demos use */
  --dark: var(--color-just-black);
  --light: var(--color-surface-white);
  --mid: var(--color-surface50);
  --grey: var(--color-grey);
  --gray: var(--color-grey);
  --green: var(--color-shockingly-green);
  --green-light: var(--color-lt-green);
  --blue: var(--color-blue);
  --purple: var(--color-lilac);
  --pink: var(--color-pink);
  --orange: var(--color-orangey);
  --red: #cd237f;

  /* Form controls */
  --field-bg: #1c1d1f;
  --field-border: var(--color-surface25);
  --field-radius: 8px;
  --focus-ring: 0 0 0 3px rgba(10, 228, 72, 0.35);

  accent-color: var(--color-shockingly-green);
  color-scheme: dark;
}

/* Type */
* { box-sizing: border-box; }

body {
  margin: 0;
  background-color: var(--color-just-black);
  color: var(--color-surface75);
  font-family: Mori, system-ui, sans-serif;
  font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  line-height: 1.45;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  margin: 0.5em 0;
  color: var(--color-surface-white);
  font-weight: 400;
  line-height: 1.2;
}
h1 { font-size: clamp(2rem, 1.6rem + 2vw, 2.875rem); }
h2 { font-size: clamp(1.625rem, 1.4rem + 1.2vw, 2.2rem); }
h3 { font-size: clamp(1.375rem, 1.25rem + 0.6vw, 1.75rem); }
h4 { font-size: clamp(1.125rem, 1rem + 0.5vw, 1.4rem); }

a { color: inherit; text-underline-offset: 0.15em; }

code, pre, kbd { font-family: "Fraktion Mono", ui-monospace, Menlo, monospace; }

/* Buttons */
button,
input[type="button"],
input[type="submit"],
input[type="reset"] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
  min-height: 2.5rem;
  padding: 0 1.25rem;
  border: 2px solid var(--color-surface75);
  border-radius: 99px;
  background: var(--color-just-black);
  color: var(--color-surface75);
  font: 600 0.9rem/1 Mori, system-ui, sans-serif;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}
button:hover,
input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {
  border-color: var(--color-surface-white);
  color: var(--color-surface-white);
}
button:disabled,
input:disabled { opacity: 0.4; cursor: not-allowed; }

/* Form controls */
label { color: var(--color-surface75); font-size: 0.9rem; }

input[type="text"],
input[type="number"],
input[type="email"],
input[type="search"],
input[type="url"],
input:not([type]),
select,
textarea {
  min-height: 2.5rem;
  padding: 0 0.75rem;
  border: 1px solid var(--field-border);
  border-radius: var(--field-radius);
  background: var(--field-bg);
  color: var(--color-surface-white);
  font: 400 0.9rem/1.2 Mori, system-ui, sans-serif;
  transition: border-color 0.2s, box-shadow 0.2s;
}
textarea { padding: 0.6rem 0.75rem; line-height: 1.45; }
input::placeholder,
textarea::placeholder { color: var(--color-surface50); }

input[type="checkbox"],
input[type="radio"] {
  width: 1.1em;
  height: 1.1em;
  margin: 0 0.4em 0 0;
  vertical-align: -0.15em;
}
input[type="range"] { width: min(100%, 18rem); }

button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: none;
  border-color: var(--color-shockingly-green);
  box-shadow: var(--focus-ring);
}


body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  overflow: hidden;
}

h1 {
  text-align: center;
  font-weight: 400;
}

#app {
  display: flex;
  justify-content: center;
}

.box {
  width: 80px;
  height: 80px;
  background: var(--color-ui-gradient);
  margin: 10px;
  float: left;
  opacity: 0;
  border-radius: 10px;
  transform: scale(0.3);
}
```

JS:
```js
let { useRef, useEffect } = React;

let data = [
  { id: 0 },
  { id: 1 },
  { id: 2 },
  { id: 3 },
  { id: 4 }
];

let Box = () => {
  return <div className="box"></div>
};

let App = () => {
  let el = useRef();
  let q = gsap.utils.selector(el);
  
  useEffect(() => {
    
    // The component has been rendered, so we can now select
    // descendants of the component, including descendants
    // nested inside of other components    
    gsap.to(q(".box"), {
      opacity: 1,
      scale: 1,
      duration: 1,
      stagger: 0.1,
      repeat: -1,
      repeatDelay: 1,
      yoyo: true
    });
  }, []);
  
  return (
    <div ref={el}>
      {data.map((item) => <Box key={item.id} />)}
    </div>
  );
}

ReactDOM.render(<App/>, document.querySelector('#app'));
```

Explain how this demo works, then help me adapt it for my own project.


### Wrap

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


### Staggers

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

### Sequencing asnimations


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

### Control and Callbacks 

```
// store the tween or timeline in a variable
let tween = gsap.to("#logo", {duration: 1, x: 100});

//pause
tween.pause();

//resume (honors direction - reversed or not)
tween.resume();

//reverse (always goes back towards the beginning)
tween.reverse();

//jump to exactly 0.5 seconds into the tween
tween.seek(0.5);

//jump to exacty 1/4th into the tween 's progress:
tween.progress(0.25);

//make the tween go half-speed
tween.timeScale(0.5);

//make the tween go double-speed
tween.timeScale(2);

//immediately kill the tween and make it eligible for garbage collection
tween.kill();

// You can even chain control methods
// Play the timeline at double speed - in reverse.
tween.timeScale(2).reverse();
```

#### Prompt and example 1

I'm working with a GSAP demo from the GSAP docs: "Basic Control Methods".
Docs page: https://gsap.com/resources/getting-started/control
CodePen: https://codepen.io/GreenSock/pen/OJLgdyg

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

HTML:
```html
<div class="container">
  <div class="flair flair--25"></div>
  <div class="nav light">
  <button id="play">play()</button>
  <button id="pause">pause()</button>
  <button id="resume">resume()</button>
  <button id="reverse">reverse()</button>
  <button id="restart">restart()</button>
</div>
</div>
```

CSS:
```css
@font-face {
  font-display: block;
  font-family: Fraktion Mono;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

:root {
  --dark: #0e100f;
  --light: #fffce1;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  min-height: 100vh;
  margin: 0;
  background-color: var(--dark);
}

.flair {
  width: 100px;
  height: 100px;
  margin: 0 auto;
  background-size: contain;
  background-repeat: no-repeat;
  will-change: transform;
}

.flair--25 {
  background-image: url("https://gsap.com/demo-assets/flair-25.webp");
}

.nav.light {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding-top: 2rem;
  background-color: transparent;
}
button {
  margin: 0.25rem;
  padding: 10px 20px;
  background: transparent;
  border: 1px solid rgba(255, 252, 225, 0.2);
  border-radius: 99px;
  color: #bbbaa6;
  font-family: Fraktion Mono, monospace;
  font-size: 0.85rem;
  line-height: 1;
  text-transform: none;
  cursor: pointer;
  transition: color 0.2s, border-color 0.2s;
}

button:hover {
  color: #fffce1;
  border-color: rgba(255, 252, 225, 0.6);
}
```

JS:
```js
let nav = document.querySelector('.nav')

let tween = gsap.to(".flair", {
  duration: 2, 
  x: () => nav.offsetWidth, // animate by the px width of the nav
  xPercent: -100, // offset by the width of the box
  rotation: 360, 
  ease: "none", 
  paused: true
});

// click handlers for controlling the tween instance...
document.querySelector("#play").onclick = () => tween.play();
document.querySelector("#pause").onclick = () => tween.pause();
document.querySelector("#resume").onclick = () => tween.resume();
document.querySelector("#reverse").onclick = () => tween.reverse();
document.querySelector("#restart").onclick = () => tween.restart();
```

Explain how this demo works, then help me adapt it for my own project.


# SVG Trnaformation

## Prompt 1 
I'm working with a GSAP demo from the GSAP docs: "SVG + CSS Transform Timeline".
Demonstrates some of the inconsistencies in the ways various browsers apply CSS transforms to SVG elements. GSAP now solves these problems, as of version 1.14.2.
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/17b4f47aa28f02e305dab386e9f79e89
GSAP plugins used: TextPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/TextPlugin.min.js

Stylesheets it loads:
- //ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css

HTML:
```html
<div class="demo">
  <div class="cell">
    <h2>SVG &lt;rect&gt;</h2>
    <svg id="svg" class="container" width="260" height="200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 200">
      <defs>
        <linearGradient id="rect-gradient" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0.19" stop-color="#ff8709"/>
          <stop offset="0.73" stop-color="#f7bdf8"/>
        </linearGradient>
      </defs>
      <rect id="svgRectangle" class="animated" x="20" y="60" width="220" height="80" fill="url(#rect-gradient)"/>
    </svg>
  </div>
  <div class="cell">
    <h2>&lt;div&gt;</h2>
    <div class="container" style="width:260px; height:200px; position:relative;">
      <div id="divRectangle" class="animated"></div>
    </div>
  </div>
</div>

<div id="nav">
  <h3 id="message"></h3>
  <div class="controls">
    <input type="range" id="slider" min="0" max="1" step="0.001" value="0">
    <button id="play">play</button>
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

@font-face {
  font-display: block;
  font-family: Fraktion Mono;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

:root {
  --dark: #0e100f;
  --light: #fffce1;
  --grey: #191919;
  --surface75: #bbbaa6;
  --surface25: #42433d;
  --orange: #ff8709;
}

body {
  margin: 0;
  padding: 18px;
  background-color: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
}

.demo {
  display: flex;
  justify-content: center;
  gap: 18px;
}

.cell {
  text-align: center;
}

h2 {
  margin: 5px 0 0.3em;
  color: var(--light);
  font-family: Fraktion Mono, monospace;
  font-size: 2rem;
  font-weight: 400;
  line-height: 1;
}

.container {
  display: block;
  overflow: hidden;
  background: var(--grey);
  border: 1px solid var(--surface25);
  border-radius: 12px;
}

#divRectangle {
  position: absolute;
  width: 220px;
  height: 80px;
  top: 60px;
  left: 20px;
  background: linear-gradient(90deg, #ff8709 19%, #f7bdf8 73%);
}

#nav {
  width: 560px;
  max-width: 100%;
  margin: 0 auto;
}

#message {
  min-height: 1.5em;
  color: var(--light);
  font-family: Fraktion Mono, monospace;
  font-size: 1rem;
  font-weight: 400;
}

.controls {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

#slider {
  flex: 1;
  accent-color: var(--orange);
}

button {
  background: var(--dark);
  border: solid 2px var(--surface75);
  color: var(--surface75);
  border-radius: 99px;
  padding: 12px 25px;
  cursor: pointer;
  line-height: 1;
  font-family: inherit;
  font-size: 0.9rem;
}
button:hover {
  border-color: var(--light);
  color: var(--light);
}
```

JS:
```js
gsap.registerPlugin(TextPlugin);
gsap.defaults({ smoothOrigin: false });

const elements = "#svgRectangle, #divRectangle";
const message = "#message";
const slider = document.getElementById("slider");

const tl = gsap.timeline({
  paused: true,
  defaults: { duration: 1 },
  onUpdate: () => (slider.value = tl.progress())
});

// both elements use the exact same tweens
tl.set(message, { text: '{rotation:360, transformOrigin:"50% 50%"}' })
  .to(elements, { rotation: 360, transformOrigin: "50% 50%" }, "+=1")
  .set(message, { text: '{rotation:"+=360", transformOrigin:"right bottom"}' }, "+=1")
  .to(elements, { rotation: "+=360", transformOrigin: "right bottom" })
  .set(message, { text: '{scale:0, transformOrigin:"0px 0px"}' }, "+=1")
  .to(elements, { scale: 0, transformOrigin: "0px 0px" })
  .set(message, { text: '{scale:1, transformOrigin:"100% 0%"}' }, "+=1")
  .to(elements, { scale: 1, transformOrigin: "100% 0%" })
  .set(message, { text: '{scaleY:0, transformOrigin:"0% 50%"}' }, "+=1")
  .to(elements, { scaleY: 0, transformOrigin: "0% 50%" })
  .set(message, { text: '{scale:1, transformOrigin:"50% bottom"}' }, "+=1")
  .to(elements, { scale: 1, transformOrigin: "50% bottom" })
  .set(message, { text: '{scale:0.5, rotation:360, transformOrigin:"50% 50%"}' }, "+=1")
  .to(elements, { scale: 0.5, rotation: 360, transformOrigin: "50% 50%" });

// --- SLIDER ---
slider.addEventListener("input", () => tl.progress(slider.value).pause());

// --- PLAY ---
document.getElementById("play").addEventListener("click", () => {
  tl.progress() === 1 ? tl.restart() : tl.play();
});
```

Explain how this demo works, then help me adapt it for my own project.

## Prompt 2

I'm working with a GSAP demo from the GSAP docs: "smoothOrigin demo".
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/053d0ee8da31db3bdca1a4531e0628ee
GSAP plugins used: TextPlugin

Scripts it loads, in order:
- //cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js
- //cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/TextPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css
- //ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css

HTML:
```html
<div id="wrapper">
  <div class="overlay" id="overlay1"><code>smoothOrigin:true</code><br>element doesn't jump when origin changes.</div>
  <div class="overlay" id="overlay2"><code>smoothOrigin:false</code><br>element jumps when origin changes.</div>
  <div class="bottomOverlay"><h2 id="transform"></h2></div>

  <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="800px" height="300px" viewBox="0 0 800 300">
    <defs>
      <linearGradient id="true-gradient" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0.19" stop-color="#ff8709"/>
        <stop offset="0.73" stop-color="#f7bdf8"/>
      </linearGradient>
      <linearGradient id="false-gradient" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0.21" stop-color="#f7bdf8"/>
        <stop offset="0.82" stop-color="#cd237f"/>
      </linearGradient>
    </defs>

    <g id="boxFalseGhost" class="box">
      <rect x="420" y="100" class="false ghost" width="50" height="50"/>
      <g>
        <g>
          <path d="M430.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C431.277,135.167,430.669,133.738,430.669,131.898z"/>
          <path d="M447.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C448.309,137.562,447.829,137.307,447.829,136.794z M451.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="430.459,118.931 444.481,110.931 458.503,118.931"/>
      </g>
    </g>

    <g id="boxTrueGhost" class="box">
      <rect y="100" class="true ghost" width="50" height="50"/>
      <g>
        <g>
          <path d="M10.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C11.277,135.167,10.669,133.738,10.669,131.898z"/>
          <path d="M27.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C28.309,137.562,27.829,137.307,27.829,136.794z M31.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="10.459,118.931 24.481,110.931 38.503,118.931"/>
      </g>
    </g>

    <g id="boxFalse" class="box">
      <rect x="420" y="100" class="false" width="50" height="50"/>
      <g>
        <g>
          <path d="M430.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C431.277,135.167,430.669,133.738,430.669,131.898z"/>
          <path d="M447.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C448.309,137.562,447.829,137.307,447.829,136.794z M451.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="430.459,118.931 444.481,110.931 458.503,118.931"/>
      </g>
      <circle class="originMarker" cx="422.5" cy="102.5" r="2.5"/>
    </g>

    <g id="boxTrue" class="box">
      <rect y="100" class="true" width="50" height="50"/>
      <g>
        <g>
          <path d="M10.669,131.898v-10.464c0-0.512,0.48-0.768,1.44-0.768h0.816c0.96,0,1.44,0.256,1.44,0.768v10.224c0,0.848,0.304,1.544,0.912,2.088c0.608,0.544,1.392,0.816,2.352,0.816s1.748-0.271,2.364-0.816c0.616-0.543,0.924-1.24,0.924-2.088v-10.224c0-0.512,0.48-0.768,1.44-0.768h0.792c0.96,0,1.44,0.256,1.44,0.768v10.464c0,1.84-0.608,3.269-1.824,4.284c-1.216,1.016-2.928,1.524-5.136,1.524s-3.92-0.508-5.136-1.524C11.277,135.167,10.669,133.738,10.669,131.898z"/>
          <path d="M27.829,136.794v-15.12c0-0.64,0.32-0.96,0.96-0.96h5.04c1.872,0,3.32,0.464,4.344,1.392c0.384,0.369,0.708,0.884,0.972,1.548c0.264,0.664,0.396,1.436,0.396,2.316s-0.152,1.652-0.456,2.316c-0.304,0.664-0.668,1.176-1.092,1.536s-0.908,0.652-1.452,0.876c-0.849,0.352-1.672,0.528-2.472,0.528h-2.544v5.568c0,0.513-0.48,0.768-1.44,0.768h-0.816C28.309,137.562,27.829,137.307,27.829,136.794z M31.525,128.058h2.136c0.576,0,1.068-0.152,1.476-0.456c0.408-0.304,0.612-0.848,0.612-1.632c0-0.784-0.204-1.332-0.612-1.644c-0.408-0.312-0.9-0.468-1.476-0.468h-2.136V128.058z"/>
        </g>
        <polygon points="10.459,118.931 24.481,110.931 38.503,118.931"/>
      </g>
      <circle class="originMarker" cx="2.5" cy="102.5" r="2.5"/>
    </g>
  </svg>

  <div class="nav">
    <input type="range" id="slider" min="0" max="100" step="0.02" value="0">
    <button id="play">restart</button>
  </div>
</div>

<p>Initial scale of the boxes is <code>scale:2</code> with their transform origin in the upper left corner,
<code>transformOrigin:"left top"</code>. The white dots indicate the transformOrigin position.</p>
<p><code>smoothOrigin:false</code> is actually the "proper" implementation based on the SVG and CSS specs, but <code>smoothOrigin:true</code> looks more natural and smooth.</p>
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

@font-face {
  font-display: block;
  font-family: Fraktion Mono;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

:root {
  --dark: #0e100f;
  --light: #fffce1;
  --grey: #191919;
  --surface75: #bbbaa6;
  --orange: #ff8709;
}

body {
  margin: 0;
  padding: 12px;
  background: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
  font-size: 16px;
}

p {
  max-width: 75ch;
  margin: 1rem auto;
  text-align: center;
  line-height: 1.5;
}

code {
  background-color: #28292b;
  color: var(--light);
  padding: 2px 4px;
  border-radius: 5px;
  font-family: Fraktion Mono, monospace;
  font-size: 0.9em;
}

#wrapper {
  position: relative;
  width: 800px;
  margin: auto;
}

svg {
  display: block;
  background: var(--grey);
  border-radius: 12px;
}

.true { fill: url(#true-gradient); }
.false { fill: url(#false-gradient); }
.ghost { opacity: 0.3; }

/* "UP" label and arrow inside each box */
.box path,
.box polygon {
  fill: var(--dark);
}

.originMarker {
  fill: var(--light);
  stroke: var(--dark);
  stroke-width: 1px;
}

.overlay {
  position: absolute;
  top: 10px;
  left: 10px;
  line-height: 1.6;
}

#overlay2 {
  left: 420px;
}

.bottomOverlay {
  position: absolute;
  top: 250px;
  width: 800px;
  text-align: center;
}

.bottomOverlay h2 {
  margin: 0;
  color: var(--light);
  font-family: Fraktion Mono, monospace;
  font-size: 1.1rem;
  font-weight: 400;
}

.nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin: 20px auto;
}

#slider {
  width: 400px;
  accent-color: var(--orange);
}

button {
  background: var(--dark);
  border: solid 2px var(--surface75);
  color: var(--surface75);
  border-radius: 99px;
  padding: 12px 25px;
  cursor: pointer;
  line-height: 1;
  font-family: inherit;
  font-size: 0.9rem;
}
button:hover {
  border-color: var(--light);
  color: var(--light);
}
```

JS:
```js
gsap.registerPlugin(TextPlugin);

//CSSPlugin.defaultSmoothOrigin = false;
var boxTrue = document.getElementById("boxTrue");
var boxFalse = document.getElementById("boxFalse");
var boxTrueGhost = document.getElementById("boxTrueGhost");
var text = document.getElementById("transform");
var originMarkers = document.querySelectorAll(".originMarker");
var slider = document.getElementById("slider");

var tl = gsap.timeline({onUpdate:updateSlider, paused:true, defaults:{duration: 0.5}});

tl.add("scaleUp1")
  .set(text, {text:'transformOrigin:"left top"'})
  .to(boxTrue, {scale:2}, "scaleUp1")
  .to(boxFalse, {scale:2}, "scaleUp1")
  .set(originMarkers, {x:"-50%", y:"-50%"}, "scaleUp1+=-0.01")

  .add("rotate1")
  .set(originMarkers, {x:25, y:25}, "rotate1") //move them inside box so they don't alter bounds / transformOrigin of boxes
  .set(text, {text:'transformOrigin:"right bottom"'}, "rotate1")
  .to(boxTrue, {rotation:"+=90", transformOrigin:"right bottom"}, "rotate1")
  .to(boxFalse, {rotation:"+=90", transformOrigin:"right bottom", smoothOrigin:false}, "rotate1")
  .set(originMarkers, {x:50, y:50}, "rotate1")

  .add("rotate2")
  .set(originMarkers, {x:25, y:25}, "rotate2")
  .set(text, {text:'transformOrigin:"right top"'}, "rotate2")
  .to(boxTrue, {rotation:"+=90", transformOrigin:"right top"}, "rotate2")
  .to(boxFalse, {rotation:"+=90", transformOrigin:"right top", smoothOrigin:false}, "rotate2")
  .set(originMarkers, {x:50, y:0}, "rotate2")

  .add("rotate3")
  .set(originMarkers, {x:25, y:25}, "rotate3")
  .set(text, {text:'transformOrigin:"left top"'}, "rotate3")
  .to(boxTrue, {rotation:"+=90", transformOrigin:"left top"}, "rotate3")
  .to(boxFalse, {rotation:"+=90", transformOrigin:"left top", smoothOrigin:false}, "rotate3")
  .set(originMarkers, {x:0, y:0}, "rotate3");

tl.timeScale(0.3);
gsap.set(".box", {y:45});
gsap.set([boxTrue, boxTrueGhost], {x:10});

document.getElementById("play").addEventListener("click", function() {
  tl.restart();
});

//--- SLIDER ---
slider.addEventListener("input", function() {
  tl.progress(slider.value / 100).pause();
});

function updateSlider() {
  slider.value = tl.progress() * 100;
}
```

Explain how this demo works, then help me adapt it for my own project.


## Prompt 3

I'm working with a GSAP demo from the GSAP docs: "SVG CSSPlugin and AttrPlugin".
to be embedded in blog post
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/907579916ec09b51ff63459d6894da5e

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css

HTML:
```html
<svg version="1.1" id="demo" xmlns="http://www.w3.org/2000/svg" width="600px" height="207px" viewBox="0 0 600 207">
  <defs>
    <linearGradient id="stroke-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0.19" stop-color="#ff8709"/>
      <stop offset="0.73" stop-color="#f7bdf8"/>
    </linearGradient>
  </defs>
  <circle id="cssCircle" class="element" cx="57.464" cy="89.464" r="30.131"/>
  <circle id="attrCircle" class="element" cx="358" cy="89.464" r="30.131"/>
  <text transform="matrix(1 0 0 1 32.3333 27)" class="label">CSSPlugin</text>
  <text transform="matrix(1 0 0 1 327.8688 27)" class="label">AttrPlugin</text>
  <rect id="attrRectangle" x="327.869" y="145.667" class="element" width="134" height="49.333" rx="0"/>
  <line class="rule" x1="300" y1="46.595" x2="300" y2="192.595"/>
</svg><br>
<button id="play">play</button>
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
  --grey: #191919;
  --surface75: #bbbaa6;
  --surface25: #42433d;
}

body {
  margin-top: 10px;
  background: var(--dark);
  text-align: center;
  color: var(--surface75);
  font-family: Mori, sans-serif;
}

svg {
  max-width: 100%;
  height: auto;
  background: var(--grey);
  border-radius: 12px;
  margin-bottom: 10px;
}

.element {
  fill: none;
  stroke: url(#stroke-gradient);
  stroke-width: 4px;
}

.label {
  font-family: Mori, sans-serif;
  font-size: 12px;
  fill: var(--light);
}

.rule {
  fill: none;
  stroke: var(--surface25);
  stroke-width: 1px;
}

button {
  background: var(--dark);
  border: solid 2px var(--surface75);
  color: var(--surface75);
  border-radius: 99px;
  padding: 12px 25px;
  cursor: pointer;
  line-height: 1;
  font-family: inherit;
  font-size: 0.9rem;
}
button:hover {
  border-color: var(--light);
  color: var(--light);
}
```

JS:
```js
var cssCircle = document.getElementById("cssCircle"),
    attrCircle = document.getElementById("attrCircle"),
    attrRectangle = document.getElementById("attrRectangle"),
    playBtn = document.getElementById("play"),
		tl = gsap.timeline({repeat:1, yoyo:true, repeatDelay:0.5, paused:true, defaults:{duration: 1}}); 

tl.to(cssCircle, {x:120, scale:2})
  .to(cssCircle, {duration: 0.5, strokeWidth:12, stroke:"white"})
  .to(attrCircle, {attr:{cx:500}})
  .to(attrCircle, {attr:{r:50}})
  .to(attrRectangle, {attr:{rx:"30"}});

play.onclick = function() {
  tl.restart();
}
```

Explain how this demo works, then help me adapt it for my own project.


## Prompt 4

I'm working with a GSAP demo from the GSAP docs: "SVG Percent-based translation".
to be embedded in blog post
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/f3acfdfb2847f7f79d1d4817cc0f3ecd

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js

Stylesheets it loads:
- /demo-assets/pens/ee8ac247ddeb87e229d660127c6fe73d.css

HTML:
```html
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" width="600px" height="205.061px" viewBox="0 0 600 205.061">
  <defs>
    <linearGradient id="box-gradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0.19" stop-color="#ff8709"/>
      <stop offset="0.73" stop-color="#f7bdf8"/>
    </linearGradient>
  </defs>
  <line class="rule" x1="181.223" y1="0" x2="181.223" y2="205.061"/>
  <rect id="test" x="18.24" y="11.245" class="box" width="163.319" height="38.865"/>
  <rect x="53.611" y="58.843" class="box" width="127.948" height="38.865"/>
  <rect x="105.14" y="107.314" class="box" width="76.419" height="38.865"/>
  <rect x="142.694" y="154.773" class="box" width="38.865" height="38.865"/>
</svg><br>
<button id="play">play</button>
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
  --grey: #191919;
  --surface75: #bbbaa6;
  --surface25: #42433d;
}

body {
  margin-top: 10px;
  background: var(--dark);
  text-align: center;
  color: var(--surface75);
  font-family: Mori, sans-serif;
}

svg {
  max-width: 100%;
  height: auto;
  background: var(--grey);
  border-radius: 12px;
  margin-bottom: 10px;
}

.rule {
  stroke: var(--surface25);
  stroke-miterlimit: 10;
}

.box {
  fill: url(#box-gradient);
}

button {
  background: var(--dark);
  border: solid 2px var(--surface75);
  color: var(--surface75);
  border-radius: 99px;
  padding: 12px 25px;
  cursor: pointer;
  line-height: 1;
  font-family: inherit;
  font-size: 0.9rem;
}
button:hover {
  border-color: var(--light);
  color: var(--light);
}
```

JS:
```js
var playBtn = document.getElementById("play")
    tl = gsap.timeline({repeat:1, yoyo:true, paused:true});

tl.to("rect", {duration:0.5, xPercent:100, stagger:0.4});



play.onclick = function() {
  tl.restart();
}
```

Explain how this demo works, then help me adapt it for my own project.

## Prompt 5 Drag SVG

I'm working with a GSAP demo from the GSAP docs: "Draggable Demo".
Docs page: https://gsap.com/resources/svg
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

## Prompt 6 Move along path SVG

I'm working with a GSAP demo from the GSAP docs: "MotionPathPlugin Demo".
GSAP 3.0 introduces a brand new MotionPathPlugin which replaces BezierPlugin. Much more powerful and convenient.
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/LwzMKL
GSAP plugins used: MotionPathPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathHelper.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<svg width="100%" height="100%" viewBox="-20 0 557 190" id="svg">
  	<defs>
		<linearGradient id="orange-crush" gradientUnits="userSpaceOnUse" x1="0.6" y1="-1.5" x2="84.4" y2="31.5">
			<stop offset="19.42%" style="stop-color: var(--color-orangey, #ff8709)" />
			<stop offset="73.08%" style="stop-color: #f7bdf8" />
		</linearGradient>
	</defs>
	<path id="path" fill="none" d="M9,100c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
	<g id="rect">
		<rect width="85" height="30"  />
		<text x="18" y="19" font-size="10">SVG &lt;rect&gt;</text>
	</g>
</svg>

<div id="div">#div</div>
```

CSS:
```css
/* GSAP brand: fonts, type sizes, colour vars, buttons and form controls.
   Element selectors only, so a demo's own class-based styles still win. */

/* Fonts */
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Mori/PPMori-Regular.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: Mori;
  font-weight: 600;
  src: url(https://gsap.com/fonts/Mori/PPMori-SemiBold.woff) format("woff");
}
@font-face {
  font-display: swap;
  font-family: "Fraktion Mono";
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

/* Colours */
:root {
  --color-shockingly-green: #0ae448;
  --color-just-black: #0e100f;
  --color-surface-white: #fffce1;
  --color-pink: #fec5fb;
  --color-shockingly-pink: #f100cb;
  --color-orangey: #ff8709;
  --color-lilac: #9d95ff;
  --color-lt-green: #abff84;
  --color-blue: #00bae2;
  --color-grey: #191919;
  --color-surface75: #bbbaa6;
  --color-surface50: #7c7c6f;
  --color-surface25: #42433d;

  --gradient-macha: linear-gradient(114.41deg, var(--color-shockingly-green) 20.74%, var(--color-lt-green) 65.5%);
  --gradient-orange-crush: linear-gradient(111.45deg, var(--color-orangey) 19.42%, #f7bdf8 73.08%);
  --gradient-lipstick: linear-gradient(165.72deg, #f7bdf8 21.15%, #cd237f 81.93%);
  --gradient-purple-haze: linear-gradient(153.58deg, #f7bdf8 32.25%, #2f3cc0 92.68%);
  --gradient-skyfall: linear-gradient(131.77deg, #0a157a 30.82%, #15bfe4 81.82%);
  --gradient-emerald-city: linear-gradient(166.9deg, var(--color-shockingly-green) 53.19%, #0085d0 107.69%);
  --gradient-summer-fair: linear-gradient(144.02deg, var(--color-blue) 4.56%, var(--color-pink) 72.98%);

  /* Short names many demos use */
  --dark: var(--color-just-black);
  --light: var(--color-surface-white);
  --mid: var(--color-surface50);
  --grey: var(--color-grey);
  --gray: var(--color-grey);
  --green: var(--color-shockingly-green);
  --green-light: var(--color-lt-green);
  --blue: var(--color-blue);
  --purple: var(--color-lilac);
  --pink: var(--color-pink);
  --orange: var(--color-orangey);
  --red: #cd237f;

  /* Form controls */
  --field-bg: #1c1d1f;
  --field-border: var(--color-surface25);
  --field-radius: 8px;
  --focus-ring: 0 0 0 3px rgba(10, 228, 72, 0.35);

  accent-color: var(--color-shockingly-green);
  color-scheme: dark;
}

/* Type */
* { box-sizing: border-box; }

body {
  margin: 0;
  background-color: var(--color-just-black);
  color: var(--color-surface75);
  font-family: Mori, system-ui, sans-serif;
  font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  line-height: 1.45;
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  margin: 0.5em 0;
  color: var(--color-surface-white);
  font-weight: 400;
  line-height: 1.2;
}
h1 { font-size: clamp(2rem, 1.6rem + 2vw, 2.875rem); }
h2 { font-size: clamp(1.625rem, 1.4rem + 1.2vw, 2.2rem); }
h3 { font-size: clamp(1.375rem, 1.25rem + 0.6vw, 1.75rem); }
h4 { font-size: clamp(1.125rem, 1rem + 0.5vw, 1.4rem); }

a { color: inherit; text-underline-offset: 0.15em; }

code, pre, kbd { font-family: "Fraktion Mono", ui-monospace, Menlo, monospace; }

/* Buttons */
button,
input[type="button"],
input[type="submit"],
input[type="reset"] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
  min-height: 2.5rem;
  padding: 0 1.25rem;
  border: 2px solid var(--color-surface75);
  border-radius: 99px;
  background: var(--color-just-black);
  color: var(--color-surface75);
  font: 600 0.9rem/1 Mori, system-ui, sans-serif;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}
button:hover,
input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {
  border-color: var(--color-surface-white);
  color: var(--color-surface-white);
}
button:disabled,
input:disabled { opacity: 0.4; cursor: not-allowed; }

/* Form controls */
label { color: var(--color-surface75); font-size: 0.9rem; }

input[type="text"],
input[type="number"],
input[type="email"],
input[type="search"],
input[type="url"],
input:not([type]),
select,
textarea {
  min-height: 2.5rem;
  padding: 0 0.75rem;
  border: 1px solid var(--field-border);
  border-radius: var(--field-radius);
  background: var(--field-bg);
  color: var(--color-surface-white);
  font: 400 0.9rem/1.2 Mori, system-ui, sans-serif;
  transition: border-color 0.2s, box-shadow 0.2s;
}
textarea { padding: 0.6rem 0.75rem; line-height: 1.45; }
input::placeholder,
textarea::placeholder { color: var(--color-surface50); }

input[type="checkbox"],
input[type="radio"] {
  width: 1.1em;
  height: 1.1em;
  margin: 0 0.4em 0 0;
  vertical-align: -0.15em;
}
input[type="range"] { width: min(100%, 18rem); }

button:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: none;
  border-color: var(--color-shockingly-green);
  box-shadow: var(--focus-ring);
}


html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

body {
  min-height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px 15px;
}

svg {
  overflow: visible;
  height: 100%;

  /* Fix Safari rendering bug */
  transform: translateZ(0);
}

circle {
  fill: var(--color-surface50);
}

path {
  stroke-width: 2;
  stroke: var(--color-surface50);
}

/* SVG rect: orange gradient */
#rect rect {
  fill: url(#orange-crush);
  rx: 8px;
}

#rect text {
  pointer-events: none;
  fill: var(--color-just-black);
  font-family: Mori, system-ui, sans-serif;
  font-weight: 600;
}

/* DIV: green gradient */
#div {
  position: absolute;
  top: 30%;
  left: 60%;
  width: 120px;
  height: 60px;
  pointer-events: none;
  background: var(--gradient-macha);
  border-radius: 12px;
  color: var(--color-just-black);
  font-size: 32px;
  font-weight: 600;
  line-height: 60px;
  text-align: center;
}

a {
  color: var(--color-shockingly-green);
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}

.gsap-3-logo {
  width: 20vw;
  max-width: 150px;
  position: fixed;
  bottom: 15px;
  right: 15px;
}
```

JS:
```js
//register the plugin (just once)
gsap.registerPlugin(MotionPathPlugin);

gsap.to("#rect", {
  duration: 5, 
  repeat: 12,
  repeatDelay: 3,
  yoyo: true,
  ease: "power1.inOut",
  motionPath:{
    path: "#path",
    align: "#path",
    autoRotate: true,
    alignOrigin: [0.5, 0.5]
  }
});
```

Explain how this demo works, then help me adapt it for my own project.

## Prompt 7 Animate SVG Strokes

I'm working with a GSAP demo from the GSAP docs: "DrawSVGPlugin Animation".
Simple demo of GreenSock's new DrawSVGPlugin.
Learn more at www.greensock.com/drawSVG
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/jEEoyw
GSAP plugins used: DrawSVGPlugin, MotionPathPlugin, CustomEase

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/DrawSVGPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/MotionPathPlugin.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/CustomEase.min.js

Stylesheets it loads:
- //ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css

HTML:
```html
<svg class="hero" viewBox="0 0 1466 446" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs>
    <linearGradient id="squiggle-gradient" x1="936" y1="-8.50098" x2="965.779" y2="458.785" gradientUnits="userSpaceOnUse">
      <stop offset="0.140625" stop-color="#FF8709"/>
      <stop offset="0.791667" stop-color="#FEC5FB"/>
    </linearGradient>
    <linearGradient id="star-gradient" x1="1236.31" x2="1472.88" y1="257.796" y2="262.837" gradientUnits="userSpaceOnUse">
      <stop offset=".427" stop-color="#FF8709"/>
      <stop offset=".792" stop-color="#F7BDF8"/>
    </linearGradient>
    <linearGradient id="handle-gradient-left" x1="203.347" x2="227.071" y1="31.277" y2="40.597" gradientUnits="userSpaceOnUse">
      <stop offset=".427" stop-color="#FF8709"/>
      <stop offset=".792" stop-color="#F7BDF8"/>
    </linearGradient>
    <linearGradient id="handle-gradient-right" x1="508.346" x2="532.07" y1="31.277" y2="40.597" gradientUnits="userSpaceOnUse">
      <stop offset=".427" stop-color="#FF8709"/>
      <stop offset=".792" stop-color="#F7BDF8"/>
    </linearGradient>
    <clipPath id="hero-clip">
      <path d="M0 0h1466v446H0z"/>
    </clipPath>
  </defs>

  <g clip-path="url(#hero-clip)">
    <path id="squiggle" stroke="url(#squiggle-gradient)" stroke-width="4" d="M-81.026 101.203c40.388 192.282 162.965 262.446 310.87 254.449 5.702-.308 11.351-1.168 17.001-1.884a543.143 543.143 0 0 0 16.754-2.922 541.57 541.57 0 0 0 16.428-3.933A534.282 534.282 0 0 0 296.054 342a527.555 527.555 0 0 0 15.549-5.854 520.54 520.54 0 0 0 15.003-6.754 511.906 511.906 0 0 0 14.389-7.603 507.271 507.271 0 0 0 13.713-8.399 495.237 495.237 0 0 0 12.979-9.138 483.725 483.725 0 0 0 12.191-9.813 473.047 473.047 0 0 0 11.356-10.422 462.35 462.35 0 0 0 10.478-10.961 446.417 446.417 0 0 0 9.564-11.429 434.791 434.791 0 0 0 8.618-11.819 420.088 420.088 0 0 0 7.648-12.135 406.596 406.596 0 0 0 6.659-12.37 391.33 391.33 0 0 0 5.658-12.526 376.709 376.709 0 0 0 4.65-12.603 359.598 359.598 0 0 0 3.642-12.599 345.005 345.005 0 0 0 2.642-12.515 327.414 327.414 0 0 0 1.653-12.354 312.273 312.273 0 0 0 .683-12.114c-.01-3.962-.097-7.896-.262-11.8-.318-3.839-.71-7.644-1.177-11.413a266.103 266.103 0 0 0-2.057-10.956 250.65 250.65 0 0 0-2.895-10.433 238.047 238.047 0 0 0-3.688-9.847 222.999 222.999 0 0 0-4.43-9.2 210.665 210.665 0 0 0-5.117-8.501 197.48 197.48 0 0 0-5.746-7.75 186.145 186.145 0 0 0-6.312-6.957 176.51 176.51 0 0 0-6.812-6.121 168.978 168.978 0 0 0-7.245-5.253 161.575 161.575 0 0 0-7.608-4.355 155.16 155.16 0 0 0-7.898-3.434 150.6 150.6 0 0 0-8.114-2.498 148.312 148.312 0 0 0-8.256-1.548 145.162 145.162 0 0 0-8.324-.594c-2.776.04-5.548.16-8.317.358-2.755.357-5.5.792-8.235 1.305a149.34 149.34 0 0 0-8.08 2.24 152.775 152.775 0 0 0-7.854 3.154 157.467 157.467 0 0 0-7.557 4.047 163.77 163.77 0 0 0-7.193 4.91 171.704 171.704 0 0 0-6.764 5.738 181.298 181.298 0 0 0-6.273 6.527 189.626 189.626 0 0 0-5.723 7.272 200.992 200.992 0 0 0-5.12 7.969 212.51 212.51 0 0 0-4.465 8.614 223.881 223.881 0 0 0-3.764 9.203 237.327 237.327 0 0 0-3.023 9.733 251.838 251.838 0 0 0-2.244 10.2 266.724 266.724 0 0 0-1.434 10.603c-.27 3.621-.469 7.267-.597 10.939a290.792 290.792 0 0 0 .259 11.207c.304 3.788.682 7.59 1.132 11.406a319.451 319.451 0 0 0 2.015 11.533 333.8 333.8 0 0 0 2.901 11.592 348.6 348.6 0 0 0 3.786 11.578 361.625 361.625 0 0 0 4.666 11.495 370.148 370.148 0 0 0 5.532 11.344 383.876 383.876 0 0 0 6.381 11.125 396.16 396.16 0 0 0 7.208 10.84 407.813 407.813 0 0 0 8.006 10.491 420.94 420.94 0 0 0 8.774 10.082 423.998 423.998 0 0 0 9.503 9.615 438.617 438.617 0 0 0 10.192 9.094 447.654 447.654 0 0 0 10.835 8.521 454.946 454.946 0 0 0 11.43 7.901 459.324 459.324 0 0 0 11.972 7.239 466.18 466.18 0 0 0 12.459 6.539 470.745 470.745 0 0 0 12.889 5.803 476.198 476.198 0 0 0 13.258 5.041 477.882 477.882 0 0 0 13.565 4.252 480.786 480.786 0 0 0 13.808 3.446 482.176 482.176 0 0 0 13.989 2.626 482.396 482.396 0 0 0 14.102 1.797 482.887 482.887 0 0 0 14.151.965c4.715.114 9.427.159 14.134.135 4.694-.162 9.379-.391 14.054-.689a478.522 478.522 0 0 0 13.909-1.5c4.587-.7 9.154-1.464 13.702-2.294a469.06 469.06 0 0 0 13.434-3.067 467.275 467.275 0 0 0 13.108-3.812 456.131 456.131 0 0 0 12.727-4.528 447.83 447.83 0 0 0 12.291-5.207 442.007 442.007 0 0 0 11.807-5.847 440.502 440.502 0 0 0 11.275-6.445 430.89 430.89 0 0 0 10.7-6.997 419.745 419.745 0 0 0 10.086-7.499 405.848 405.848 0 0 0 9.437-7.949 392.888 392.888 0 0 0 8.759-8.345 379.013 379.013 0 0 0 8.052-8.684 367.221 367.221 0 0 0 7.326-8.965 353.98 353.98 0 0 0 6.581-9.186 338.638 338.638 0 0 0 5.826-9.347 325.584 325.584 0 0 0 5.062-9.447 307.845 307.845 0 0 0 4.296-9.486 293.687 293.687 0 0 0 3.533-9.464 278.768 278.768 0 0 0 2.776-9.382 261.518 261.518 0 0 0 2.032-9.241 247.227 247.227 0 0 0 1.303-9.041c.256-2.952.455-5.88.595-8.785a214.65 214.65 0 0 0-.088-8.476 198.74 198.74 0 0 0-.741-8.115 183.468 183.468 0 0 0-1.363-7.703 167.909 167.909 0 0 0-1.947-7.247 154.363 154.363 0 0 0-2.492-6.748 140.822 140.822 0 0 0-2.994-6.208 128.609 128.609 0 0 0-3.45-5.633 117.338 117.338 0 0 0-3.858-5.027 107.95 107.95 0 0 0-4.216-4.392 99.808 99.808 0 0 0-4.522-3.734 91.714 91.714 0 0 0-4.774-3.056 86.505 86.505 0 0 0-4.971-2.364 81.626 81.626 0 0 0-5.114-1.661 78.37 78.37 0 0 0-5.199-.952 76.855 76.855 0 0 0-5.23-.241 76.92 76.92 0 0 0-5.204.466 77.95 77.95 0 0 0-5.123 1.166 81.006 81.006 0 0 0-4.989 1.855 85.72 85.72 0 0 0-4.802 2.527 92.43 92.43 0 0 0-4.562 3.18 98.127 98.127 0 0 0-4.276 3.809 106.634 106.634 0 0 0-3.94 4.411 115.704 115.704 0 0 0-3.562 4.98 125.74 125.74 0 0 0-3.141 5.517 138.053 138.053 0 0 0-2.681 6.015 149.831 149.831 0 0 0-2.186 6.474 160.706 160.706 0 0 0-1.66 6.889 176.54 176.54 0 0 0-1.104 7.259 188.565 188.565 0 0 0-.524 7.583 204.7 204.7 0 0 0 .077 7.859 217.74 217.74 0 0 0 .695 8.084 231.27 231.27 0 0 0 1.326 8.259 246.429 246.429 0 0 0 1.966 8.383 258.798 258.798 0 0 0 2.61 8.454 275.032 275.032 0 0 0 3.254 8.475 288.211 288.211 0 0 0 3.897 8.443 298.856 298.856 0 0 0 4.531 8.362 309.318 309.318 0 0 0 5.153 8.231 323.218 323.218 0 0 0 5.762 8.052 334.663 334.663 0 0 0 6.35 7.825 346.231 346.231 0 0 0 6.917 7.554 354.909 354.909 0 0 0 7.458 7.24 367.98 367.98 0 0 0 7.971 6.887 373.26 373.26 0 0 0 8.451 6.494 382.251 382.251 0 0 0 8.897 6.068 392.222 392.222 0 0 0 9.307 5.609 392.358 392.358 0 0 0 9.677 5.121 401.381 401.381 0 0 0 10.005 4.609 402.915 402.915 0 0 0 10.292 4.074 407.728 407.728 0 0 0 10.535 3.522 410.802 410.802 0 0 0 10.731 2.953 411.835 411.835 0 0 0 10.883 2.376 417.34 417.34 0 0 0 10.987 1.789 415.335 415.335 0 0 0 11.045 1.201 418.008 418.008 0 0 0 11.057.612c3.678.058 7.352.067 11.022.027 3.655-.135 7.303-.319 10.942-.55 3.617-.325 7.223-.697 10.817-1.115a413.271 413.271 0 0 0 10.649-1.667c3.5-.69 6.98-1.423 10.441-2.2a399.634 399.634 0 0 0 10.19-2.712 397.466 397.466 0 0 0 9.904-3.2 393.42 393.42 0 0 0 9.58-3.66 388.74 388.74 0 0 0 9.223-4.092 382.534 382.534 0 0 0 8.837-4.491 365.394 365.394 0 0 0 8.421-4.857 354.037 354.037 0 0 0 7.982-5.185 347.059 347.059 0 0 0 7.519-5.476 337.3 337.3 0 0 0 7.038-5.728 327.633 327.633 0 0 0 6.541-5.939 312.049 312.049 0 0 0 6.033-6.11 299.797 299.797 0 0 0 5.516-6.238 293.603 293.603 0 0 0 4.992-6.324 274.273 274.273 0 0 0 4.466-6.368 260.266 260.266 0 0 0 3.943-6.369 243.506 243.506 0 0 0 3.423-6.33 229.656 229.656 0 0 0 2.911-6.248 215.85 215.85 0 0 0 2.41-6.128 197.627 197.627 0 0 0 1.922-5.968 178.535 178.535 0 0 0 1.453-5.771 166.604 166.604 0 0 0 1.002-5.538 145.364 145.364 0 0 0 .573-5.273 128.69 128.69 0 0 0 .17-4.975 113.777 113.777 0 0 0-.206-4.648 100.214 100.214 0 0 0-.554-4.294 85.219 85.219 0 0 0-.871-3.915 70.68 70.68 0 0 0-1.154-3.516 60.338 60.338 0 0 0-1.405-3.098 48.946 48.946 0 0 0-1.62-2.662 39.407 39.407 0 0 0-1.798-2.215 32.117 32.117 0 0 0-1.94-1.758 26.787 26.787 0 0 0-2.045-1.293c-.7-.314-1.405-.589-2.113-.824a20.097 20.097 0 0 0-2.142-.356 19.76 19.76 0 0 0-2.135.111 20.6 20.6 0 0 0-2.092.574c-.679.305-1.349.647-2.012 1.027a27.235 27.235 0 0 0-1.897 1.471 32.374 32.374 0 0 0-1.749 1.9 40.282 40.282 0 0 0-1.569 2.313 48.858 48.858 0 0 0-1.357 2.709 58.565 58.565 0 0 0-1.118 3.083 70.33 70.33 0 0 0-.85 3.434 84.412 84.412 0 0 0-.558 3.761 97.286 97.286 0 0 0-.243 4.061c.002 1.423.033 2.867.092 4.333a123.514 123.514 0 0 0 .446 4.575 138.457 138.457 0 0 0 .814 4.786c.366 1.642.765 3.298 1.196 4.967a168.274 168.274 0 0 0 1.588 5.114 183.206 183.206 0 0 0 1.988 5.229 196.745 196.745 0 0 0 2.392 5.311c.899 1.784 1.832 3.57 2.799 5.36a228.89 228.89 0 0 0 3.205 5.375 244.168 244.168 0 0 0 3.609 5.358 254.621 254.621 0 0 0 4.006 5.309 268.74 268.74 0 0 0 4.396 5.228 270.726 270.726 0 0 0 4.776 5.118 279.336 279.336 0 0 0 5.141 4.978 295.16 295.16 0 0 0 5.493 4.811 306.202 306.202 0 0 0 5.828 4.617 314.084 314.084 0 0 0 6.143 4.399 323.684 323.684 0 0 0 6.438 4.157 323.892 323.892 0 0 0 6.714 3.895c2.3 1.229 4.62 2.434 6.96 3.614 2.37 1.131 4.77 2.237 7.18 3.317 2.44 1.028 4.9 2.029 7.38 3.004 2.5.921 5.02 1.814 7.55 2.679 2.56.81 5.12 1.592 7.7 2.345 2.59.697 5.2 1.364 7.81 2.003 2.63.581 5.26 1.132 7.9 1.655 2.64.464 5.3.899 7.95 1.304 2.66.347 5.33.665 7.99.954 2.66.23 5.33.432 7.99.604 2.65.115 5.31.201 7.96.259 2.64.001 5.28-.026 7.91-.08 2.62-.11 5.23-.247 7.83-.411 2.58-.218 5.16-.461 7.72-.731a365.9 365.9 0 0 0 7.6-1.04c2.5-.42 4.98-.865 7.45-1.333 2.44-.515 4.86-1.052 7.27-1.612a351.71 351.71 0 0 0 7.08-1.872c2.31-.686 4.6-1.39 6.87-2.114 2.23-.762 4.45-1.54 6.64-2.337a347.86 347.86 0 0 0 6.4-2.537c2.07-.891 4.12-1.796 6.14-2.715 1.98-.945 3.94-1.902 5.88-2.871a326.25 326.25 0 0 0 5.6-3.003 324.205 324.205 0 0 0 5.32-3.112 374.852 374.852 0 0 0 5.03-3.195 387.85 387.85 0 0 0 4.74-3.254 317.665 317.665 0 0 0 4.45-3.29c1.41-1.101 2.79-2.201 4.16-3.301a376.188 376.188 0 0 0 3.87-3.289 360.99 360.99 0 0 0 3.59-3.253 355.11 355.11 0 0 0 3.31-3.194c1.04-1.046 2.05-2.084 3.04-3.115.95-1.014 1.88-2.019 2.79-3.015.87-.975 1.72-1.94 2.54-2.894.79-.932 1.56-1.85 2.31-2.757.72-.881 1.42-1.748 2.1-2.601.64-.826 1.27-1.636 1.89-2.431.58-.765 1.14-1.513 1.7-2.246.52-.7 1.03-1.383 1.53-2.049.47-.631.94-1.245 1.39-1.841.42-.559.84-1.1 1.25-1.623.39-.485.77-.951 1.14-1.398.36-.409.71-.798 1.05-1.168.33-.331.65-.642.97-.933.32-.252.63-.484.93-.697.3-.172.6-.325.89-.458a7.56 7.56 0 0 1 .88-.222 6.757 6.757 0 0 1 .89.011c.31.061.61.142.92.241.31.136.63.291.96.464.33.21.67.437 1.02.681.36.279.72.575 1.1.889.39.346.79.708 1.19 1.086.43.409.86.833 1.31 1.272.46.469.93.951 1.42 1.447a547.94 547.94 0 0 1 1.56 1.608l1.71 1.756c.6.619 1.22 1.248 1.86 1.888.66.659 1.33 1.328 2.02 2.005.72.695 1.45 1.397 2.2 2.107.77.724 1.56 1.455 2.37 2.192.83.749 1.68 1.502 2.55 2.261.89.768 1.81 1.539 2.73 2.314.96.781 1.93 1.564 2.92 2.35 1.02.789 2.05 1.579 3.1 2.37 1.08.791 2.17 1.583 3.28 2.374a301.68 301.68 0 0 0 3.46 2.362c1.19.782 2.4 1.561 3.63 2.337a293.82 293.82 0 0 0 3.8 2.295c1.310.752 2.63 1.5 3.96 2.242 1.36.73 2.73 1.455 4.12 2.174a351.22 351.22 0 0 0 4.26 2.095 288.65 288.65 0 0 0 4.4 2.005c1.49.644 3 1.279 4.52 1.905 1.53.608 3.08 1.207 4.63 1.796 1.57.57 3.15 1.13 4.74 1.68 1.6.529 3.21 1.048 4.83 1.557a363.02 363.02 0 0 0 4.9 1.428c1.66.443 3.31.875 4.97 1.296 1.67.399 3.35.786 5.03 1.161 1.68.353 3.37.694 5.06 1.024 1.69.307 3.38.603 5.08.887 1.7.261 3.4.511 5.1.75 1.7.216 3.4.421 5.1.615 1.7.172 3.39.333 5.09.484 1.69.129 3.38.248 5.06.356 1.68.088 3.36.166 5.03.234 1.67.048 3.33.087 4.99.117 1.64.012 3.29.014 4.93.008 1.63-.023 3.25-.055 4.86-.094"/>

    <path id="star" fill="url(#star-gradient)" fill-rule="evenodd" clip-rule="evenodd" d="m1365.65 283.192-32.23-15.024a7.653 7.653 0 0 1-3.71-10.148c1.76-3.829 6.29-5.508 10.13-3.756l32.34 14.775-12.16-33.412c-1.45-3.963.59-8.346 4.54-9.804a7.667 7.667 0 0 1 9.83 4.51l12.42 33.316 15.02-32.227a7.658 7.658 0 0 1 10.15-3.717 7.66 7.66 0 0 1 3.76 10.133l-14.78 32.343 33.41-12.165a7.66 7.66 0 0 1 9.81 4.547c1.45 3.957-.56 8.349-4.51 9.822l-33.32 12.422 32.23 15.024a7.653 7.653 0 0 1 3.71 10.148c-1.76 3.829-6.29 5.508-10.13 3.756l-32.34-14.774 12.16 33.411c1.45 3.963-.59 8.346-4.540 9.804a7.668 7.668 0 0 1-9.83-4.509l-12.42-33.317-15.02 32.227a7.658 7.658 0 0 1-10.15 3.717 7.66 7.66 0 0 1-3.76-10.133l14.78-32.343-33.41 12.165a7.665 7.665 0 0 1-9.81-4.547c-1.45-3.957.56-8.348 4.51-9.822m33.32-12.422"/>

    <rect class="dot" width="12" height="12" x="194.573" y="346.999" rx="6" fill="#FEC5FB" transform="rotate(51.796 194.573 346.999)"/>
    <rect class="dot" width="12" height="12" x="370.259" y="30.278" rx="6" fill="#FF8709" transform="rotate(51.796 370.259 30.278)"/>
    <rect class="dot" width="12" height="12" x="514.573" y="328.999" rx="6" fill="#FEC5FB" transform="rotate(51.796 514.573 328.999)"/>
    <rect class="dot" width="12" height="12" x="660.572" y="92.999" rx="6" fill="#FF8709" transform="rotate(51.796 660.572 92.999)"/>
    <rect class="dot" width="12" height="12" x="804.572" y="310.999" rx="6" fill="#FEC5FB" transform="rotate(51.796 804.572 310.999)"/>
    <rect class="dot" width="12" height="12" x="954.574" y="154.999" rx="6" fill="#FF8709" transform="rotate(51.796 954.574 154.999)"/>
    <rect class="dot" width="12" height="12" x="1103.57" y="292.999" rx="6" fill="#FEC5FB" transform="rotate(51.796 1103.57 292.999)"/>
    <rect class="dot" width="12" height="12" x="1241.57" y="213.999" rx="6" fill="#FF8709" transform="rotate(51.796 1241.57 213.999)"/>

    <g id="handle">
      <path id="handle-line" stroke="#FF8709" stroke-width="2" d="M214.999 39.559h310.236"/>
      <path class="handle-end" fill="url(#handle-gradient-left)" d="M217.197 33.127a.43.43 0 0 1 .609 0l6.07 6.069a.431.431 0 0 1 0 .61l-6.07 6.068a.43.43 0 0 1-.609 0l-6.069-6.069a.431.431 0 0 1 0-.61l6.069-6.068Z"/>
      <path class="handle-end" fill="url(#handle-gradient-right)" d="M522.196 33.127a.43.43 0 0 1 .609 0l6.07 6.069a.431.431 0 0 1 0 .61l-6.07 6.068a.43.43 0 0 1-.609 0l-6.069-6.069a.431.431 0 0 1 0-.61l6.069-6.068Z"/>
    </g>
  </g>
</svg>

<svg class="hero title" viewBox="70 530 1005 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DrawSVG">
  <path d="M77 699.678V543.08H133.37C148.73 543.08 162.376 546.362 174.306 552.924C186.236 559.486 195.557 568.658 202.267 580.44C208.978 592.073 212.333 605.421 212.333 620.485C212.333 635.846 208.978 649.567 202.267 661.647C195.557 673.579 186.236 682.9 174.306 689.611C162.376 696.323 148.73 699.678 133.37 699.678H77ZM135.16 675.518C144.704 675.518 153.204 673.206 160.661 668.582C168.266 663.959 174.157 657.471 178.332 649.12C182.508 640.768 184.596 631.223 184.596 620.485C184.596 610.343 182.508 601.245 178.332 593.192C174.157 585.138 168.266 578.8 160.661 574.176C153.204 569.553 144.704 567.241 135.16 567.241H103.843V675.518H135.16Z"/>
  <path d="M234.87 699.678V581.111H256.121L259.253 604.377C267.007 587.972 280.727 579.769 300.412 579.769H304.886V605.496H300.412C288.034 605.496 278.416 608.628 271.556 614.892C264.696 621.156 261.266 629.88 261.266 641.066V699.678H234.87Z"/>
  <path d="M359.43 702.139C345.71 702.139 334.749 699.082 326.547 692.967C318.494 686.703 314.468 678.127 314.468 667.24C314.468 654.712 319.091 645.913 328.337 640.842C337.732 635.771 350.035 632.341 365.246 630.552C366.588 630.402 370.614 629.955 377.325 629.209C384.185 628.464 389.106 627.27 392.089 625.63C395.071 623.84 396.563 621.454 396.563 618.471C396.413 612.655 394.177 608.031 389.852 604.601C385.527 601.022 379.637 599.232 372.18 599.232C364.426 599.232 357.938 601.171 352.719 605.048C347.5 608.777 344.517 613.773 343.771 620.037H317.152C317.898 611.834 320.731 604.526 325.652 598.113C330.574 591.551 337.061 586.48 345.113 582.901C353.316 579.322 362.487 577.532 372.628 577.532C388.286 577.532 400.44 581.41 409.089 589.165C417.888 596.92 422.287 607.286 422.287 620.261V673.952C422.287 677.382 424.226 679.097 428.103 679.097H434.59V699.678H422.063C416.098 699.678 411.252 698.485 407.523 696.099C403.944 693.713 401.633 690.282 400.589 685.808C400.142 684.466 399.769 683.124 399.471 681.781C392.163 695.353 378.816 702.139 359.43 702.139ZM364.798 681.334C374.044 681.334 381.65 678.948 387.615 674.175C393.58 669.403 396.563 663.064 396.563 655.16V638.605C394.624 641.737 391.418 643.974 386.944 645.316C382.47 646.51 376.207 647.628 368.154 648.672C358.908 649.716 352.048 651.282 347.574 653.37C343.249 655.458 341.087 659.336 341.087 665.003C341.087 670.223 343.1 674.25 347.127 677.083C351.302 679.917 357.193 681.334 364.798 681.334Z"/>
  <path d="M501.512 699.678H473.775L438.655 581.111H465.722L489.657 667.016L513.144 581.111H535.066L558.777 666.122L582.265 581.111H609.332L574.212 699.678H546.922L524.105 618.695L501.512 699.678Z"/>
  <path d="M692.559 703.034C678.988 703.034 666.983 700.946 656.545 696.77C646.106 692.445 637.829 686.405 631.715 678.649C625.75 670.745 622.469 661.647 621.872 651.357H649.386C650.579 660.007 654.979 666.793 662.584 671.714C670.19 676.636 680.181 679.097 692.559 679.097C702.699 679.097 710.38 677.307 715.599 673.728C720.968 669.999 723.652 664.779 723.652 658.068C723.652 652.401 721.639 648.001 717.612 644.869C713.586 641.737 707.323 638.829 698.822 636.144L673.321 628.538C664.075 625.704 656.321 622.871 650.057 620.037C643.943 617.203 638.426 612.878 633.504 607.062C628.732 601.245 626.346 593.639 626.346 584.243C626.346 575.593 628.583 567.912 633.057 561.201C637.68 554.49 644.167 549.27 652.518 545.541C661.018 541.664 670.935 539.725 682.269 539.725C701.208 539.725 716.345 544.497 727.678 554.042C739.012 563.587 745.201 576.637 746.245 593.192H718.954C718.358 584.094 714.779 576.935 708.217 571.715C701.805 566.346 692.857 563.662 681.374 563.662C672.725 563.662 665.79 565.377 660.571 568.807C655.501 572.237 652.965 576.935 652.965 582.901C652.965 587.077 654.158 590.507 656.545 593.192C659.08 595.727 661.988 597.666 665.269 599.008C668.698 600.351 674.216 602.289 681.822 604.825L705.533 612.207C715.077 615.19 722.906 618.247 729.021 621.379C735.284 624.362 740.503 628.687 744.679 634.355C748.855 640.022 750.942 647.479 750.942 656.726C750.942 666.122 748.556 674.324 743.784 681.334C739.012 688.344 732.227 693.713 723.428 697.441C714.63 701.17 704.34 703.034 692.559 703.034Z"/>
  <path d="M846.838 699.678H818.653L757.809 543.08H786.665L832.745 662.99L877.26 543.08H905.892L846.838 699.678Z"/>
  <path d="M987.112 703.034C972.646 703.034 959.747 699.678 948.413 692.967C937.079 686.107 928.206 676.487 921.794 664.108C915.53 651.73 912.399 637.337 912.399 620.932C912.399 605.123 915.53 591.104 921.794 578.874C928.206 566.496 937.303 556.876 949.084 550.015C961.014 543.155 974.958 539.725 990.914 539.725C1011.2 539.725 1027.97 545.392 1041.24 556.727C1054.52 568.062 1062.87 583.647 1066.3 603.482H1038.78C1036.25 591.104 1030.73 581.41 1022.23 574.4C1013.73 567.39 1003.29 563.886 990.914 563.886C975.256 563.886 962.804 569.031 953.558 579.322C944.461 589.463 939.913 603.333 939.913 620.932C939.913 632.714 941.926 642.93 945.952 651.58C950.128 660.231 955.944 666.942 963.4 671.714C971.006 676.338 979.804 678.649 989.796 678.649C1001.88 678.649 1011.57 675.145 1018.88 668.135C1026.33 660.976 1030.06 651.73 1030.06 640.395H982.861V617.8H1036.32C1046.46 617.8 1054.14 620.261 1059.36 625.182C1064.73 630.104 1067.42 637.337 1067.42 646.882V699.678H1043.71V651.804H1043.26C1041.62 667.613 1035.88 680.141 1026.03 689.388C1016.19 698.485 1003.22 703.034 987.112 703.034Z"/>
</svg>

<input type="range" id="slider" min="0" max="100" step="0.01" value="0">
```

CSS:
```css
:root {
  --dark: #0e100f;
  --light: #fffce1;
}

body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  background-color: var(--dark);
}

.hero {
  width: 90%;
  max-width: 1100px;
  visibility: hidden; /* avoids a flash before the initial state is set */
}

#squiggle {
  stroke-linecap: round;
}

.title {
  width: 55%;
  max-width: 600px;
  fill: var(--light);
}

.title path {
  stroke-width: 3px;
  stroke: var(--light);
  fill: var(--light);
}

#slider {
  width: 400px;
  max-width: 60vw;
  margin-top: 1.5rem;
  accent-color: #ff8709;
}
```

JS:
```js
gsap.registerPlugin(DrawSVGPlugin, MotionPathPlugin, CustomEase);

const pathEase = CustomEase.create("pathEase", "M0,0 C0.096,0.014 0.212,0.101 0.242,0.134 0.418,0.328 0.788,0.754 1,1");
const popIn = () => ({ scale: [0, 1.5, 1], easeEach: "back.out(1.1)" });
const popOut = () => ({ scale: [1, 1.5, 0], easeEach: "back.out(1.1)" });
const slider = document.getElementById("slider");

// initial state
gsap.set(".dot, .handle-end, #star", { scale: 0, transformOrigin: "50% 50%" });
gsap.set("#handle-line", { scaleX: 0, transformOrigin: "50% 50%" });
gsap.set("#handle", { transformOrigin: "50% 50%" });

const tl = gsap.timeline({
  defaults: { ease: "back.inOut(1.1)" },
  onUpdate: () => (slider.value = tl.progress() * 100)
});

tl.from(".title path", { drawSVG: 0, duration: 1.5, stagger: 0.1, ease: "power1.inOut" }, 0)
  .from(".title path", { fillOpacity: 0, duration: 0.6, stagger: 0.1, ease: "none" }, 1.3)
  .fromTo("#squiggle", { drawSVG: 0 }, { drawSVG: "100% 0%", ease: pathEase, duration: 2.5 }, 0)
  .to(".dot", { keyframes: popIn(), stagger: 0.1, duration: 0.5 }, 2)
  .to("#handle-line", { scaleX: 1, duration: 1 }, 2.5)
  .to(".handle-end", { keyframes: popIn(), stagger: 0.1, duration: 0.5 }, 2.75)
  .to("#handle", { rotate: -10, y: -2.5, duration: 0.5 }, 2.75)
  // star rides the path, then the line erases behind it
  .to("#star", {
    motionPath: { path: "#squiggle", align: "#squiggle", alignOrigin: [0.5, 0.5], autoRotate: true },
    ease: pathEase,
    duration: 2.5
  }, 3)
  .to("#star", { scale: 1, duration: 0.5 }, 3)

// from() tweens have rendered their start state, so it's safe to show everything
gsap.set(".hero, .title", { visibility: "visible" });

// --- SLIDER ---
slider.addEventListener("input", () => tl.progress(slider.value / 100).pause());
slider.addEventListener("change", () => tl.play());
```

Explain how this demo works, then help me adapt it for my own project.


## Prompt 8 animation snake in a maze effect

I'm working with a GSAP demo from the GSAP docs: "SVG Tips: DrawSVGPlugin Values".
Demonstrates the various types of values that can be passed to GSAP's DrawSVGPlugin. This pen is used on the DrawSVGPlugin product page.
Learn more at www.greensock.com/drawSVG
Docs page: https://gsap.com/resources/svg
CodePen: https://codepen.io/GreenSock/pen/GJpGdm
GSAP plugins used: DrawSVGPlugin

Scripts it loads, in order:
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js
- https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/DrawSVGPlugin.min.js

Stylesheets it loads:
- /demo-assets/pens/AHquG.css

HTML:
```html
<p>DrawSVGPlugin Values</p>

<svg version="1.1"
	 xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 width="300" viewBox="0 0 516.3 190" style="enable-background:new 0 0 516.3 211.99;"
	 xml:space="preserve">
  <defs>
    <linearGradient id="svg-gradient" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0.19" stop-color="#ff8709"/>
      <stop offset="0.73" stop-color="#f7bdf8"/>
    </linearGradient>
  </defs>
  <path id="template" d="M9.13,99.99c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
	<path id="path" d="M9.13,99.99c0,0,18.53-41.58,49.91-65.11c30-22.5,65.81-24.88,77.39-24.88c33.87,0,57.55,11.71,77.05,28.47c23.09,19.85,40.33,46.79,61.71,69.77c24.09,25.89,53.44,46.75,102.37,46.75c22.23,0,40.62-2.83,55.84-7.43c27.97-8.45,44.21-22.88,54.78-36.7c14.35-18.75,16.43-36.37,16.43-36.37"/>
</svg>

<div id="code">drawSVG:<div id="current">"100%"</div></div>
<button id="next">Next Example</button>
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

@font-face {
  font-display: block;
  font-family: Fraktion Mono;
  font-style: normal;
  font-weight: 400;
  src: url(https://gsap.com/fonts/Fraktion/PPFraktionMono-Bold.woff) format("woff");
}

:root {
  --dark: #0e100f;
  --light: #fffce1;
  --surface75: #bbbaa6;
  --surface50: #7c7c6f;
  --surface25: #42433d;
}

body {
  background-color: var(--dark);
  color: var(--surface75);
  font-family: Mori, sans-serif;
  font-weight: 400;
  text-align: center;
}

p {
  font-family: Mori, sans-serif;
}

#template, #path {
  fill: none;
}
#template {
  stroke-width: 5px;
  stroke: var(--surface25);
}
#path {
  stroke: url(#svg-gradient);
  stroke-width: 20px;
  visibility: hidden;
}
#code, #value {
  font-size: 20px;
  font-family: Fraktion Mono, monospace;
}
#code {
  color: var(--surface50);
  margin: 20px;
  position: relative;
  visibility: hidden;
}
#current {
  display: inline-block;
  color: var(--light);
}
#description {
  max-width: 530px;
  color: var(--surface50);
  font-family: Mori, sans-serif;
  font-size: 24px;
  display: inline-block;
  text-align: left;
}

button {
  background: var(--dark);
  border: solid 2px var(--surface75);
  color: var(--surface75);
  border-radius: 99px;
  padding: 12px 25px;
  cursor: pointer;
  line-height: 1;
  font-family: inherit;
  font-size: 0.9rem;
}
button:hover {
  border-color: var(--light);
  color: var(--light);
}
```

JS:
```js
gsap.registerPlugin(DrawSVGPlugin);

var values = "100%;40% 60%;20 350;50% 50%;true;10%".split(";"),
    currentIndex = 0;

//set the initial value
gsap.set("#path", {visibility:"visible"});
gsap.set("#code", {visibility:"visible"});

function next() {

  gsap.killTweensOf(next); //in case the user clicks, clear any delayed calls to this method.
  if (++currentIndex === values.length) {
    currentIndex = 0;
  }
  if (values[currentIndex] === "true") {
    gsap.set("#current", {innerText:(values[currentIndex]), ease:"none"});
  } else {
    gsap.set("#current", {innerText:('"' + values[currentIndex] + '"'), ease:"none"});
  }
  gsap.to("#path", {duration: 1, drawSVG:values[currentIndex], ease:"power1.inOut"});

}

document.getElementById("next").addEventListener("click", next);
```

Explain how this demo works, then help me adapt it for my own project.

## Prompt 9 Morph SVG

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


# React GSAP

https://gsap.com/resources/React

