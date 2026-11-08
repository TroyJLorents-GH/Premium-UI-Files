# Performance, accessibility, and QA

An interface is only premium if it never drops frames, responds instantly, and works for everyone. Automation covers ~30–40% of accessibility issues; the rest is manual.

## Core Web Vitals and budgets

Verified field targets at the 75th percentile, mobile and desktop assessed separately: **LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1** (web.dev/vitals). Rumors of tighter 2026 thresholds are unverified; quote the official page. FID is retired.

| Metric | Target (aim) | Mechanism |
|---|---|---|
| LCP | ≤ 2.5 s (1.5 s) | Real hero text/image first; `fetchpriority="high"`; no lazy-load on the LCP element; preload the body font; inline critical CSS (< 14 KB); 3D/video after first paint |
| INP | ≤ 200 ms (100 ms) | Visual feedback on pointer-down; `scheduler.yield()`; break long tasks (> 50 ms); defer non-critical hydration; Long Animation Frames attribution |
| CLS | ≤ 0.1 (0) | `aspect-ratio`/width+height on media; skeletons sized to final layout; metric-matched font fallbacks or `font-display: optional`; `scrollbar-gutter: stable` |
| TTFB / FCP | ≤ 0.8 s / ≤ 1.8 s | Edge rendering, caching, 103 Early Hints |
| Frame budget | 16.7 ms @ 60 Hz, 8.3 ms @ 120 Hz, 4.1 ms @ 240 Hz | Whole pipeline; track missed frames and p95/p99 frame time, not average FPS |
| JS (mobile initial) | ≤ ~300 KB compressed | Route-level splitting; `import()` motion libs after idle/first interaction; `LazyMotion`; islands/RSC |
| Hero media | image ≤ 200 KB AVIF · video ≤ 2 MB · 3D ≤ 3 MB | Poster first, then enhance |
| Response | visible acknowledgement < 100 ms | Independent of network; optimistic UI where safe |

Set route-specific budgets from a measured baseline; arbitrary one-size KB limits are not a design.

## Rendering pipeline rules

- Animate only `transform`, `opacity`, and where needed `clip-path`/`filter`; never `top/left/width/height/margin/box-shadow` on the hot path. Fake shadow motion by fading a pseudo-element.
- Batch DOM reads before writes; reading `offsetWidth` after a style write forces synchronous layout (classic jank).
- `will-change` on 2–5 elements right before they animate, removed after; too many layers exhaust mobile GPU memory.
- `backdrop-filter` and large `filter: blur()` are expensive, especially on iOS: limit area and count.
- `content-visibility: auto` + `contain-intrinsic-size` on long pages; `contain: layout paint` on independent widgets.
- Prefer compositor-thread animation (CSS, WAAPI, scroll-driven) over per-frame JS; GSAP/Motion are fine when they only touch transforms/opacity.
- Pause everything offscreen (`IntersectionObserver`, `visibilityState`): Lottie, Rive, canvas, marquees, shaders.
- Heavy compute off the main thread: `OffscreenCanvas` + Worker, WASM, Partytown for third-party scripts.
- One ticker; one owner per property; dispose GPU resources on navigation.
- Test on a mid-range Android with 4× CPU throttling **and** a 120 Hz iPhone; they expose different jank.

## Loading and network

- Images: AVIF default with WebP fallback (JPEG XL arriving), `srcset`/`sizes`, `<picture>` art direction, `loading="lazy"` below the fold only, `decoding="async"`, explicit dimensions, LQIP/ThumbHash placeholders; `next/image`, Astro `<Image>`, Cloudinary/imgix, Sharp/Squoosh.
- Video: `preload="metadata"`, poster, AV1/HEVC, HLS via Mux/Cloudflare Stream for > 10 s; `muted playsinline` for autoplay; pause offscreen.
- Fonts: self-host, preload, subset, variable, `size-adjust` fallbacks.
- JS: code splitting, lazy motion libs, `client:visible`/`client:idle` islands, React Compiler, no barrel imports, `modulepreload`.
- Network: HTTP/3, Brotli/Zstd, immutable hashed assets, `preconnect`, Speculation Rules `prerender` for likely next pages, bfcache-safe (no `unload`), streaming SSR.
- Third parties: after consent/idle, self-host where licensed, facade pattern for embeds.
- Adaptive loading: `prefers-reduced-data`, `Save-Data`, `effectiveType`, `deviceMemory`: lighter media/3D for constrained devices.

## Perceived performance

Respond within 100 ms (press states, optimistic UI); skeletons only after ~300 ms; progress for anything > 1 s; notify when done for > 10 s; prefetch on hover/viewport; stale-while-revalidate; persistent shells during navigation; an animation never exceeds the latency it masks. Doherty threshold: system response < 400 ms keeps flow.

## WCAG 2.2 AA: exact requirements that affect polished UI

| Criterion | Requirement |
|---|---|
| 1.4.3 Contrast (AA) | **4.5:1** ordinary text; **3:1** large text (≥ 24 CSS px, or ≥ ~18.67 px bold). Test every real background and state. |
| 1.4.11 Non-text contrast (AA) | **3:1** for UI component boundaries/states and meaningful graphics against adjacent colors (not every decorative border). |
| 1.4.4 Resize text (AA) | Usable at **200%** zoom without loss. Never `maximum-scale=1` / `user-scalable=no`. |
| 1.4.10 Reflow (AA) | No 2D scrolling at **320 CSS px** width (or 256 px height for horizontal content), except content that genuinely needs 2D (maps, tables). |
| 1.4.12 Text spacing (AA) | Survive user overrides: line-height 1.5×, paragraph 2×, letter 0.12×, word 0.16× without loss. |
| 2.2.2 Pause, stop, hide (A) | Auto-moving content > 5 s (marquees, carousels, video) needs pause/stop/hide; auto-updating content needs control regardless. |
| 2.3.1 Three flashes (A) | Nothing flashes > 3×/s. Avoid flashing outright. |
| 2.3.3 Animation from interactions (AAA, but do it) | Motion triggered by interaction can be disabled → honor reduced motion. |
| 2.4.11 Focus not obscured (AA) | Focused element never entirely hidden by sticky headers, banners, drawers. |
| 2.5.7 Dragging movements (AA) | Any drag function also works with single-pointer non-drag (click targets); keyboard alone does not satisfy it. |
| 2.5.8 Target size (AA) | **24×24 CSS px** minimum, with exceptions: spacing (24 px circle not intersecting neighbors), equivalent control on the page, inline text, user-agent default, essential. **44×44 is AAA (2.5.5)**; use it for touch anyway. |
| 2.4.13 Focus appearance (AAA) | 2 px perimeter-equivalent, 3:1 change. AA still requires a visible focus indicator with contrast. |
| 3.3.7 Redundant entry (A) | Information needed again in the same process is prefilled or selectable. |
| 3.3.8 Accessible authentication (AA) | No cognitive tests without alternatives; allow paste and password managers. |

Law: WCAG 2.2 AA is the procurement baseline; the EU Accessibility Act applies since 28 Jun 2025; ADA Title II deadlines moved to Apr 2027 (≥ 50k population) and 2028; Title III litigation treats WCAG 2.2 AA as the bar. Accessibility overlays do not satisfy any of it.

## Core accessibility checklist

- Semantic HTML first (`<button>`, `<nav>`, `<dialog>`, `<details>`, ordered headings, landmarks, skip link); ARIA only to fill gaps (APG patterns).
- Keyboard: every interactive element reachable and operable; visible `:focus-visible` ring (2 px, 3:1); logical order; `inert` on background during modals; Escape closes overlays; arrow-key patterns per widget; no focus trapped in pinned/offscreen containers.
- Names, roles, states: labels persist while typing; errors associated via `aria-describedby`; `aria-live="polite"` for toasts/counters/streaming (bounded); `role="status"` for loaders; `aria-current` for location.
- Contrast in light, dark, `prefers-contrast`, and `forced-colors` (state must not live only in background images).
- Targets ≥ 24 px (44 on touch), `touch-action: manipulation`, spacing between targets.
- Media: captions, transcripts, no autoplay with sound; reduced transparency → solid fallbacks for glass.
- Forms: input types, `autocomplete`, `inputmode`, paste allowed, recoverable drafts (never persist passwords/payment), duplicate-submit protection, timezone/locale clarity.
- Text: `lang`, RTL/logical properties, string expansion, `Intl` formatting.
- Screen readers to test: VoiceOver (macOS/iOS), NVDA + Firefox, JAWS + Chrome, TalkBack. SplitText headlines must read as sentences.

## QA protocol (no special hardware required)

**A. Creative audit**: squint test (one Primary Actor per beat); velocity-curve check (quick initiation, soft settle, no abrupt clunk); typography stability (copy stationary after ≤ 0.8 s).

**B. Engineering audit**: grep for `requestAnimationFrame` and `setAnimationLoop` → one master loop. Chrome DevTools → Performance → gear → CPU 4×/6× slowdown, Fast 4G → record a full scroll: zero red long-task triangles (> 50 ms), zero purple layout spikes during scrub. For 3D log `renderer.info`: draw calls < 60, textures return to 0 after unmount. Animations panel at 10% speed to inspect curves.

**C. Accessibility audit**: DevTools → Cmd/Ctrl+Shift+P → "Emulate CSS prefers-reduced-motion: reduce" → scroll: camera orbits, parallax, pinned traps replaced by crossfades/native flow. Tab through the whole page. Emulate forced colors and vision deficiencies. Zoom 200%; resize to 320 px. Run axe (DevTools, `@axe-core/playwright`, Pa11y) then a real screen reader journey.

**D. Loading audit**: poster/static first paint < 50 KB matching frame 0; LCP element not lazy; fonts stable; 3D/video streams after.

**E. State audit**: empty, loading, long content (400-char names, +35% translated), validation errors, network failure, offline/reconnect, expired session, permission denied, stale data, rapid repeated input, interrupted animation.

## Release review checklist

- Journeys: main task, interrupted task, undo/retry, timeout/offline, empty/loading/partial; content order sensible without animation.
- Layout: narrow phones, tablets, desktop resize, landscape, safe areas, virtual keyboard, 200% text, 320 px reflow, RTL/translations, spacing overrides.
- Input: keyboard-only, visible focus, Escape/back, pointer/touch/stylus, single-pointer drag alternative, nested scroll regions, no accidental gesture capture.
- Assistive tech: roles/names/states; NVDA/VoiceOver/TalkBack journeys; focus after modals and navigation; error announcements; live regions.
- Motion: reduced motion, autoplay controls, fast repeats, cancellation, slow network, low-power devices, background/resume; controls usable while animating.
- Visual: real media and fonts; light/dark/high-contrast; selected/disabled/error/focus; contrast over gradients/video/glass; screenshots at representative sizes.
- Performance: production build on a slower device; startup + repeated navigation, typing, scrolling, heavy scenes; lab regressions vs field p75.
- Automation: a small set of critical behavior/visual/a11y flows (Playwright + axe, Lighthouse CI, visual regression); review false positives and untested states.
- Production: `web-vitals` attribution + error tracking wired; segment by route/device/connection; redact personal data; ownership and rollback threshold.

## Tooling

Chrome DevTools (Performance with field overlay, Rendering → paint flashing/layer borders, Layers, Animations), Safari Web Inspector (iPhone issues), Firefox Profiler, Lighthouse/PSI/webstatus.dev, CrUX, WebPageTest, `web-vitals` + RUM (Vercel Speed Insights, Cloudflare, SpeedCurve, Sentry), Lighthouse CI/`size-limit`, React Profiler/react-scan, r3f-perf/Spector.js, axe/Pa11y/Accessibility Insights/WAVE, `eslint-plugin-jsx-a11y`, Storybook a11y addon, Polypane, Stark.

## Mobile web / PWA

`viewport-fit=cover`, `env(safe-area-inset-*)`, `100dvh`, `interactive-widget=resizes-content`, `touch-action`, `overscroll-behavior`, `-webkit-tap-highlight-color: transparent`, Vibration API (Android), Web App Manifest + service worker offline, `<install>`/`navigator.install()` (Chrome beta). Thumb-zone navigation; 44 px targets; keyboard avoidance; launch screen matching first frame.
