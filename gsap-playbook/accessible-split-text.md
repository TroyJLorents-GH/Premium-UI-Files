# SplitText: nested elements and accessibility

Source: supplied `GSAP Plugins.md`, lines 896–1008, original heading: Screen reader-only.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** The supplied duplicate-text example contains a focusable link in an aria-hidden visual copy. Its clipped accessible copy also does not become visible when a descendant receives focus. Do not reuse unchanged: preserve one coherent reading and keyboard order and visible focus.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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


