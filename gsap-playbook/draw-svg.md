# DrawSVGPlugin

Source: supplied `GSAP Plugins.md`, lines 1687–1973, original heading: Draw SVG.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** The multi-segment splitPaths() helper copies every attribute, including id, to each new path. Remove or uniquely remap duplicated IDs and dependent references when adapting. Its script list includes plugins that the implementation does not need.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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

