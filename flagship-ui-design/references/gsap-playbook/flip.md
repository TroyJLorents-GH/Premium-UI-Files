# Flip

Source: supplied `GSAP Plugins.md`, lines 1009–1377, original heading: Flip.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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


