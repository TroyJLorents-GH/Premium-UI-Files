# Native and cross-platform mobile (when the request is an app, not a site)

Premium feel on mobile comes from running animation on the UI/render thread, physics springs that follow the finger, and platform idioms: Apple Liquid Glass (iOS 26) and Material 3 Expressive. Cross-platform in 2026 means React Native 0.84 + Expo SDK 55+ (New Architecture only) or Flutter with Impeller.

## Cross-cutting rules

- Touch targets ≥ 44×44 pt (iOS) / 48×48 dp (Android); thumb-zone navigation (bottom tabs, sheets, FABs).
- Gestures interruptible and velocity-aware (springs with initial velocity), rubber-band at edges (`f(x) = 1 − 1/((x·c)/d + 1)`, `c ≈ 0.55`), haptic tick on snap points.
- 120 Hz exposes jank: no JS-thread `setState` per frame; batch layout; profile release/profileable builds on target hardware.
- Respect Reduce Motion (`UIAccessibility.isReduceMotionEnabled`, RN `AccessibilityInfo.isReduceMotionEnabled`), Dynamic Type, dark mode, RTL, insets, predictive back.
- Skeletons and optimistic UI matter more on mobile networks; cache images, prefetch next screens; launch screen matches first frame.

## Stacks

| Platform | Use | Motion-relevant features |
|---|---|---|
| SwiftUI (iOS 26) | Apple-first products | `.glassEffect()`, `GlassEffectContainer`, `glassEffectID` morphs; `.spring(duration:bounce:)` and `.smooth/.snappy/.bouncy`; `matchedGeometryEffect`, `matchedTransitionSource` zoom; `PhaseAnimator`, `KeyframeAnimator`; `.sensoryFeedback()`; SF Symbols `.symbolEffect`; `scrollTransition`, `visualEffect`; Metal `.layerEffect`/`.distortionEffect`; `.contentTransition(.numericText())`; UIKit `UIViewPropertyAnimator` for interruptible sheets |
| Jetpack Compose (M3 Expressive) | Android-first | `MaterialExpressiveTheme`, `MotionScheme.expressive()`, spring `animate*AsState`/`Animatable`, `AnimatedVisibility`, `animateContentSize`, `AnimatedContent`, `SharedTransitionLayout`, `graphicsLayer`, AGSL shaders, predictive back, shape-morphing loaders; Baseline Profiles + Macrobenchmark for startup/scroll |
| React Native + Expo | React teams | Reanimated 4 worklets (`withSpring/withTiming/withDecay`, layout animations, shared elements, CSS-style props), Gesture Handler 2, RN Skia (SkSL shaders, blur/glow, charts), Expo Router native tabs, `expo-glass-effect`, `@gorhom/bottom-sheet`, FlashList v2, `expo-image`, `expo-haptics`; UI kits gluestack v4, Tamagui, NativeWind, Unistyles |
| Flutter | Shared bespoke UI | Impeller (shaders precompiled), implicit animations, `Hero`, `flutter_animate`, custom `Curves`/springs, `CustomPainter` + `FragmentProgram`, Rive/Lottie packages, M3 Expressive widgets |
| Desktop | Electron / Tauri / Qt / .NET (Avalonia, MAUI, WinUI 3) | OS integration, memory/startup, WebView differences, keyboard conventions, multiwindow |

## What the prototype must prove

Apple: text input, accessibility, navigation, window behavior, interruptible motion, deployment targets. Android: back navigation, keyboard/insets, large-screen adaptation, TalkBack, frame-time distribution. RN: native dependency fit, release startup, keyboard transitions, nested scrolling, deep links, accessible gesture alternatives. Flutter/Compose Multiplatform: actual target-device performance, platform input conventions, accessibility tree.

## Verify with

Xcode Instruments, MetricKit, Accessibility Inspector, VoiceOver; Android Studio Profiler, Macrobenchmark, Accessibility Scanner, TalkBack; Flutter DevTools; Flashlight (RN); Maestro/Appium for journeys; Firebase Performance for field data. Read Apple HIG (Liquid Glass, motion, haptics), Material 3 Expressive motion, WWDC18 "Designing Fluid Interfaces", WWDC23 "Animate with springs".
