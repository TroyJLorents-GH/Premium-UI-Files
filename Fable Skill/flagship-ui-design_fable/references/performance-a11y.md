# Performance and accessibility

Budgets, rendering-pipeline rules, loading, the exact WCAG 2.2 numbers that polished interfaces get wrong, and the manual test protocol. Field targets are at the 75th percentile of real users; a lab score or one good trace proves little.

## Contents

1. Budgets
2. Rendering pipeline rules
3. Loading and network
4. Perceived performance
5. Exact WCAG 2.2 requirements
6. Accessibility checklist for premium UI
7. Measurement tools
8. Manual test protocol (DevTools)
9. Release review checklist

## 1. Budgets

| Metric | Target | Notes |
|---|---|---|
| LCP | ≤2.5 s (aim 1.5) | Hero image/text; `fetchpriority="high"`; no lazy-load on the LCP element; preload hero font |
| INP | ≤200 ms (aim 100) | Every click/tap/key; break long tasks with `scheduler.yield()`; visual feedback on pointer-down. Claims of a March 2026 tightening were unverified at snapshot; check web.dev/vitals |
| CLS | ≤0.1 (aim 0) | `aspect-ratio`/`min-height` reservations, `font-display: optional` or metric-matched fallbacks, `scrollbar-gutter: stable` |
| TTFB / FCP | ≤0.8 s / ≤1.8 s | Edge rendering, caching, 103 Early Hints |
| Frame budget | 16.7 ms @60 Hz, 8.3 ms @120 Hz for the whole pipeline | Track missed deadlines and p95/p99 frame time, not average FPS; Long Animation Frames (>50 ms) are the INP culprits |
| JS shipped (mobile) | ≤300 KB compressed initial; motion libs lazy | Islands/RSC cut this fastest |
| Hero media | image ≤200 KB AVIF, video ≤2 MB, 3D ≤3 MB | Poster first, then enhance |
| Response acknowledgement | ≤100 ms visible | Independent of network completion |

Set route-specific budgets from a measured baseline rather than universal KB limits; keep a baseline before adding animation or dependencies.

## 2. Rendering pipeline rules

- Animate only `transform`, `opacity`, and sparingly `clip-path`/`filter`. Never `top/left/width/height/margin/box-shadow/border-width/background-position` on a continuous path. Compositing is still scene-dependent: inspect traces rather than assuming.
- Batch DOM reads before writes; a style write followed by `offsetWidth`/`getBoundingClientRect` forces synchronous layout. Pointer and scroll handlers are the usual offenders.
- `will-change` on 2–5 elements right before they animate, removed after. Many promoted layers exhaust mobile GPU memory.
- `backdrop-filter` and large `filter: blur()` are expensive; limit area and count, especially on iOS.
- `content-visibility: auto` + `contain-intrinsic-size` on long pages; `contain: layout paint` on independent widgets.
- Prefer CSS/WAAPI/scroll-driven animations (compositor) over per-frame JS; GSAP/Motion are fine when they touch only transforms.
- Pause everything off-screen and in hidden tabs: Lottie, Rive, canvas, marquees, shaders, ambient loops.
- Workers for heavy compute (`OffscreenCanvas`, WASM); Partytown-style isolation for third-party scripts (verify its status).
- Adaptive quality: cap DPR, reduce particles, drop post-processing, honor `prefers-reduced-data`, `Save-Data`, `navigator.connection.effectiveType`, `deviceMemory`.
- Test on a mid-range Android with 4× CPU throttling and on a 120 Hz iPhone; they expose different jank.

## 3. Loading and network

| Area | Techniques |
|---|---|
| Images | AVIF (WebP fallback; JPEG XL arriving), `srcset`/`sizes`, `<picture>` art direction, `loading="lazy"` below the fold, `decoding="async"`, dimensions set, LQIP/BlurHash/ThumbHash; `next/image`, Astro `<Image>`, Unpic; Sharp/Squoosh/CDN transforms |
| Video | `preload="metadata"`, poster, AV1/HEVC, HLS via Mux/Cloudflare Stream for >10 s |
| Fonts | Self-host, preload body font, subset, variable, `size-adjust` fallbacks (Capsize, Fontaine, `next/font`) |
| JavaScript | Route-level splitting; `import()` motion libs after idle or first interaction; `LazyMotion`; islands/partial hydration (`client:visible`, `client:idle`); RSC; React Compiler; avoid barrel imports; `modulepreload`; `useTransition`/`useDeferredValue` for heavy state |
| Network | HTTP/3, Brotli/Zstd, immutable hashed assets, `preconnect`, Speculation Rules `prerender` for likely next pages, bfcache-safe pages (no `unload`), streaming SSR/PPR, no redirect chains |
| Third parties | Load after consent/idle, self-host where licensed, facade pattern for embeds (lite YouTube, chat widgets) |

## 4. Perceived performance

Respond within 100 ms (press states, optimistic UI); skeletons only after ~300 ms and matching the final layout; determinate progress for anything over 1 s; prefetch on hover/viewport; stale-while-revalidate data with freshness indicated where it matters; persistent shells during navigation; never let an animation exceed the latency it masks; a success state only when the action succeeded; visible rollback with retry context on optimistic failure.

## 5. Exact WCAG 2.2 requirements

WCAG 2.2 AA is the bar (EU EAA since 28 June 2025; US ADA Title II deadlines from April 2027; Title III litigation treats 2.2 AA as the standard). WCAG 3.0 is a draft: watch, do not build to it.

| Criterion | Requirement |
|---|---|
| 1.4.3 Contrast (Minimum), AA | 4.5:1 ordinary text; 3:1 large text (≥18 pt / 24 px, or ≥14 pt / ~18.67 px bold). Test every real background, including gradients, video, glass, and images |
| 1.4.11 Non-text Contrast, AA | 3:1 for visual information needed to identify controls and states and for meaningful graphics; not every decorative border |
| 1.4.4 Resize Text, AA | 200% enlargement without loss; never `maximum-scale=1` or `user-scalable=no` |
| 1.4.10 Reflow, AA | No two-dimensional scrolling at 320 CSS px width (vertical content) or 256 CSS px height (horizontal content), except content that genuinely needs 2D layout |
| 1.4.12 Text Spacing, AA | Survives user overrides: line-height 1.5×, paragraph spacing 2×, letter spacing 0.12 em, word spacing 0.16 em |
| 2.2.2 Pause, Stop, Hide, A | Anything moving/blinking/scrolling that starts automatically and lasts >5 s alongside other content needs pause/stop/hide; auto-updating content needs control regardless of duration |
| 2.3.1 Three Flashes, A | Nothing flashes more than three times per second |
| 2.3.3 Animation from Interactions, AAA (treat as required) | Motion triggered by interaction can be disabled (reduced motion) |
| 2.4.11 Focus Not Obscured (Minimum), AA | Focused element not entirely hidden by sticky headers, banners, drawers |
| 2.5.7 Dragging Movements, AA | Every drag function also works with a single pointer without dragging (buttons, selectable destination); keyboard support alone does not satisfy it |
| 2.5.8 Target Size (Minimum), AA | 24×24 CSS px, or a 24 px-diameter spacing circle that overlaps no other target; exceptions: equivalent control on the same page, inline text targets, user-agent default size, essential presentation. **44×44 is 2.5.5 (AAA)**, a good target for touch, not the AA rule |
| 2.4.13 Focus Appearance, AAA | 2 px perimeter-equivalent area and 3:1 change is **AAA**; AA requires a visible focus indicator meeting non-text contrast. Do not cite it as a new AA rule |
| 3.3.7 Redundant Entry, A | Information already entered in the same process is auto-populated or selectable |
| 3.3.8 Accessible Authentication (Minimum), AA | No cognitive test (memorize, transcribe, solve) without an alternative; allow paste and password managers |

## 6. Accessibility checklist for premium UI

- Semantic HTML first (`<button>`, `<nav>`, `<dialog>`, `<details>`, headings in order, landmarks, skip link); ARIA only to fill gaps.
- Keyboard: every control reachable and operable, visible `:focus-visible`, logical order, `inert` background during modals, Escape closes overlays, arrow-key patterns per the ARIA APG.
- Contrast per §5; APCA Lc 60+ body as the perceptual check; test light, dark, `prefers-contrast`, `forced-colors`.
- Targets ≥24 px (≥44 px for primary touch controls), spacing between targets, `touch-action: manipulation`.
- Text resizable to 200%, spacing overrides survive, `lang` set per element where it changes.
- Media: captions, transcripts, no autoplay with sound.
- Forms: labels, error identification linked by `aria-describedby`, no CAPTCHA-only authentication.
- Live regions: `aria-live="polite"` for toasts, counters, streaming text; `role="status"` for loaders; do not announce every intermediate scramble/typewriter string.
- Reduced motion and reduced transparency honored; motion toggle for app-like products.
- Split text keeps reading order (SplitText `aria` handling or a single accessible copy); no focusable element inside an `aria-hidden` duplicate.
- Canvas/WebGL content: text and controls remain in the DOM.
- Screen readers to test: VoiceOver (macOS/iOS), NVDA + Firefox, JAWS + Chrome, TalkBack.

## 7. Measurement tools

Chrome DevTools Performance (field-data overlay, Rendering → paint flashing, layer borders, Layers, Animations panel); Safari Web Inspector (necessary for iOS issues); Firefox Profiler; Lighthouse / PageSpeed Insights / CrUX / Search Console CWV; WebPageTest filmstrips; `web-vitals` attribution build + RUM (Vercel Speed Insights, Cloudflare Web Analytics, SpeedCurve, Calibre, DebugBear, Sentry); Lighthouse CI, Unlighthouse, `size-limit` in CI; React Profiler, react-scan, `r3f-perf`, Spector.js; axe DevTools / `axe-core`, Accessibility Insights (WCAG 2.1 AA scope: add 2.2 checks manually), WAVE, Polypane, `eslint-plugin-jsx-a11y`, Storybook a11y addon, Playwright + `@axe-core/playwright`, Pa11y CI. Automation catches roughly 30–40% of accessibility issues.

## 8. Manual test protocol (browser)

Motion and composition first; a static screenshot passes a motionless page, so capture frames over time.

0. **Motion and composition frames** (expressive surfaces fail on any of these): at 1440 × 900 and 390 × 844, capture the hero at about 0, 300, 700, and 1200 ms after load and the page at 0/25/50/75/100% scroll depth plus the set piece at 0/50/100% progress. Fail if consecutive hero frames are identical (reads as static), if the first viewport reads as a common template (split hero with a card, centered headline over a mockup, three equal cards), if a card's content occupies well under half its area, if any text is clipped (masked reveals need 0.1–0.15 em of block padding) or two text nodes overlap, if a pinned stage's copy or figure leaves the viewport (size stages in `dvh`), or if `document.documentElement.scrollWidth > window.innerWidth` on the phone viewport. Also read the copy for layout-position words ("at right", "below"). Script the checks where you can:

```js
// run in the page at 390 px
({ overflow: document.documentElement.scrollWidth - innerWidth,
   clipped: [...document.querySelectorAll("h1,h2,h3,p,li,a,button")].filter(e => e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1).map(e => e.textContent.trim().slice(0, 40)) })
```

1. **Throttled scroll trace**: Performance panel → gear → CPU 4× (or 6×) slowdown, Network Fast 4G → record a full top-to-bottom scroll and the main interactions. Zero red long-task markers (>50 ms); no purple layout/recalc spikes during scrub or pointer tracking.
2. **Reduced motion**: Command menu → "Emulate CSS prefers-reduced-motion: reduce". Parallax, pins, orbits, loops gone; feedback intact.
3. **Keyboard-only pass**: Tab through the page; focus visible everywhere, never trapped in off-screen stages, restored after modals and route changes; Escape closes overlays.
4. **Reflow**: 320 px wide viewport; 200% zoom; text-spacing bookmarklet; nothing lost or overlapping.
5. **Color modes**: light, dark, `prefers-contrast: more`, `forced-colors: active` (Rendering panel).
6. **Layers**: Layers panel → count promoted layers; Rendering → paint flashing during animation shows nothing repainting except intended areas.
7. **Animations panel**: slow to 10% and scrub; check origins, overshoot, and that exits are shorter than entrances.
8. **Real devices**: mid-range Android (4G) and 120 Hz iPhone; thermal behavior after 30 s of scrolling a 3D hero.
9. **States**: empty, loading, error, long content, interrupted request, offline/reconnect, rapid repeated input.
10. **Cleanup**: navigate away and back four times; memory and `renderer.info` return to baseline.

## 9. Release review checklist

- Journeys: main task, interrupted task, undo/retry, expired session, timeout/offline, validation errors, empty/loading/partial, long content; content order sensible without animation.
- Layout: narrow phones, tablets, resizing, landscape, safe areas, virtual keyboard, 200% text, 320 px reflow, RTL where supported.
- Input: keyboard only, visible focus, Escape/back, pointer/touch/stylus, single-pointer alternative for drag, nested scroll regions, no accidental gesture capture.
- Assistive tech: roles/names/states; real NVDA/VoiceOver/TalkBack runs; focus after modals and navigation; live announcements bounded.
- Motion: reduced motion, autoplay controls, fast repeated actions, cancellation, slow network, low-power devices, background/resume; controls usable while animating.
- Visual: real media and fonts, all color modes, every control state, contrast over gradients/video/glass.
- Performance: production build on a slower device; startup plus repeated navigation, typing, scrolling, heavy scenes; lab regressions vs field p75.
- Production: errors and performance correlated by release, route, device class; telemetry overhead measured; rollback threshold owned.
