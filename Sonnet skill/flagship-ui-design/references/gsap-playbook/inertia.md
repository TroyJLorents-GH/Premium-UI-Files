# InertiaPlugin

Source: supplied `GSAP Plugins.md`, lines 2053–2491, original heading: Inertia.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Example 3 says it is independent of Draggable, but its actual code constructs a Draggable instance. Read the code to identify dependencies. Older jQuery and fixed geometry appear in these examples.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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


