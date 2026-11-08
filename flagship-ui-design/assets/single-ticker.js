/**
 * flagship-ui-design · single-ticker motion runtime
 *
 * One animation loop for Lenis (smooth scroll), GSAP (timelines/ScrollTrigger),
 * optional Three.js rendering, and per-frame DOM sync (3D→2D callouts, cursor lerps).
 * Honors prefers-reduced-motion, pauses when the tab is hidden, and returns a
 * teardown that reverts everything (GSAP context, ScrollTriggers, Lenis, listeners).
 *
 * Usage (vanilla / Astro / any framework; call once per page):
 *   import { createMotionRuntime } from './single-ticker.js';
 *   const runtime = createMotionRuntime({ renderer, scene, camera, onFrame: syncCallouts });
 *   runtime.mm.add({ reduce: '(prefers-reduced-motion: reduce)', desktop: '(min-width: 768px)' }, (ctx) => { ...timelines... });
 *   // on route change / unmount:
 *   runtime.destroy();
 *
 * React: do the same inside useGSAP()/useEffect and call destroy() in the cleanup.
 * Lenis handles reduced motion itself (lerp → 1, instant programmatic scroll) and keeps
 * running so WebGL/DOM sync stays intact; read `lenis.prefersReducedMotion` for your branches.
 */
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import Lenis from 'lenis';

gsap.registerPlugin(ScrollTrigger);

export function createMotionRuntime({
  renderer = null,          // THREE.WebGLRenderer | WebGPURenderer (optional)
  scene = null,
  camera = null,
  onFrame = null,           // (time, deltaTime) => void  — 3D→2D projection, cursor lerps, etc.
  lenisOptions = {},        // { lerp: 0.08, anchors: true, allowNestedScroll: true, ... }
  smoothScroll = true,      // false for app-like / content-heavy surfaces
  maxDpr = 2,               // 1.5 on constrained mobile
} = {}) {
  const ctx = gsap.context(() => {});
  const mm = gsap.matchMedia();
  let lenis = null;
  let renderOnDemand = false;
  let dirty = true;

  if (renderer) {
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, maxDpr));
  }

  if (smoothScroll) {
    lenis = new Lenis({ autoRaf: false, lerp: 0.08, anchors: true, allowNestedScroll: true, ...lenisOptions });
    lenis.on('scroll', ScrollTrigger.update);
  }

  // The single loop. Order matters: scroll → sync → render.
  const tick = (time, deltaTime) => {
    if (lenis) lenis.raf(time * 1000);          // GSAP ticker gives seconds; Lenis wants ms
    if (onFrame) onFrame(time, deltaTime);
    if (renderer && scene && camera && (!renderOnDemand || dirty)) {
      renderer.render(scene, camera);
      dirty = false;
    }
  };
  gsap.ticker.add(tick);
  gsap.ticker.lagSmoothing(0);                  // let Lenis own the easing

  // Pause all work when the tab is hidden; resume without a time jump.
  const onVisibility = () => {
    if (document.hidden) { gsap.ticker.sleep(); lenis?.stop(); }
    else { gsap.ticker.wake(); lenis?.start(); dirty = true; }
  };
  document.addEventListener('visibilitychange', onVisibility);

  // Re-measure pins after fonts/assets settle (prevents pin drift).
  const onFontsReady = () => ScrollTrigger.refresh();
  document.fonts?.ready.then(onFontsReady);
  const onResize = () => { if (renderer) renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, maxDpr)); dirty = true; };
  window.addEventListener('resize', onResize, { passive: true });

  return {
    gsap, ScrollTrigger, lenis, ctx, mm,
    /** mark the 3D scene dirty when rendering on demand */
    invalidate: () => { dirty = true; },
    /** render only when something changed (idle scenes) */
    setRenderOnDemand: (v) => { renderOnDemand = !!v; dirty = true; },
    /** full teardown: timelines, ScrollTriggers, Lenis, listeners, GPU resources */
    destroy() {
      gsap.ticker.remove(tick);
      document.removeEventListener('visibilitychange', onVisibility);
      window.removeEventListener('resize', onResize);
      mm.revert();
      ctx.revert();
      ScrollTrigger.getAll().forEach((st) => st.kill());
      lenis?.destroy();
      if (scene) {
        scene.traverse((obj) => {
          obj.geometry?.dispose?.();
          const mats = Array.isArray(obj.material) ? obj.material : [obj.material];
          mats.forEach((m) => {
            if (!m) return;
            Object.values(m).forEach((v) => v?.isTexture && v.dispose());
            m.dispose?.();
          });
        });
      }
      renderer?.dispose?.();
    },
  };
}

/** Project a 3D anchor to CSS pixels for HTML/SVG callouts (call inside onFrame). */
export function projectToScreen(object3D, camera, tmpVec, out = {}) {
  object3D.getWorldPosition(tmpVec);
  tmpVec.project(camera);                       // NDC −1..1
  out.x = (tmpVec.x * 0.5 + 0.5) * window.innerWidth;
  out.y = (-(tmpVec.y * 0.5) + 0.5) * window.innerHeight;
  out.behind = tmpVec.z > 1;                    // hide callouts behind the camera
  return out;
}

/** Frame-rate-independent damping for cursor followers, parallax, etc. */
export function damp(current, target, lambda, deltaTime) {
  return current + (target - current) * (1 - Math.exp(-lambda * deltaTime));
}
