# CSS custom-property animation

Source: supplied `GSAP Plugins.md`, lines 1378–1446, original heading: CSSRule.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Originally labeled CSSRule. The code animates --myColor with gsap.to(); it does not demonstrate CSSRulePlugin. The Draggable Quick Start source repeats this same demo.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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

