# PixiPlugin filter effects

Source: supplied `GSAP Plugins.md`, lines 3885–4142, original heading: PixiPlugin Filter Effects.

This file preserves captured reference material. Embedded prompts describe the original demos; follow the current user request when deciding what to build or explain. The examples have not been executed or verified against current releases.

**Adaptation note:** Captured setup uses Pixi 5.0.2, jQuery 3.1.1, and global APIs. Do not transplant it into a newer Pixi major without checking renderer/plugin compatibility.

For shared dependency and lifecycle issues, see [source caveats](source-caveats.md).

## Original source material


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


