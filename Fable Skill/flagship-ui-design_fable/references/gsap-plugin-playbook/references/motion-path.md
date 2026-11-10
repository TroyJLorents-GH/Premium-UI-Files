# MotionPathPlugin

Source: supplied `GSAP Plugins.md`, lines 2741–3133, original heading: MotionPath.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** The SVG path demo is repeated under SVG Prompt6; another example interpolates an array of property values.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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


