# Playback controls and callbacks

Source: supplied `GSAP Plugins.md`, lines 5274–5421, original heading: Control and Callbacks.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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


