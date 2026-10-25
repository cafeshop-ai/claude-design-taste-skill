# Platforms: native mobile and cross-platform

Most of this skill applies to any screen. This file covers what changes on phones and tablets, and when designing for (or to feel at home on) iOS and Android. The guiding rule: on native platforms, convention matters even more than on the web, because people's muscle memory comes from the operating system.

## Contents
1. Mobile fundamentals (any platform)
2. iOS (Human Interface Guidelines)
3. Android (Material Design 3)
4. Cross-platform and mobile web
5. Tablets and large screens

---

## 1. Mobile fundamentals (any platform)

- **One primary task per screen.** Small screens punish competing priorities. Push secondary content one level down.
- **Thumb reach:** primary navigation and actions at the bottom; the top corners are hardest to reach one-handed. Put destructive actions out of the easy-reach zone.
- **Targets:** 44×44pt (iOS) / 48×48dp (Android) minimum, with spacing between.
- **Type:** body text 16–17pt/sp. Support the system text-size setting (Dynamic Type on iOS, font scale on Android) and test at the largest sizes; layouts must reflow, not truncate.
- **Safe areas:** respect notches, rounded corners, the home indicator, and the status bar. Content scrolls under translucent bars; controls never sit under the home indicator.
- **Keyboard awareness:** when the keyboard opens, the focused field and the primary action stay visible. Choose the right keyboard type for each field; offer "Next" to move between fields and "Done"/"Go" to submit.
- **Gestures:** support platform gestures (back-swipe, pull to refresh) and provide visible alternatives for custom ones.
- **Offline and flaky networks** are normal on mobile: cache, queue actions, and show clear sync state.
- **Haptics** for meaningful confirmations (success, a toggle, reaching a limit), subtle and sparing.

## 2. iOS (Human Interface Guidelines)

- **Navigation:** a bottom **tab bar** for 3–5 top-level sections (always visible at the top level; labeled icons); **navigation stacks** for hierarchy with a back button (labeled with the previous screen's title) and edge-swipe back. Large titles at the top of top-level screens that collapse on scroll.
- **Modality:** **sheets** for focused tasks, with detents (medium/large) and swipe-to-dismiss; full-screen covers for immersive tasks; **action sheets** for choices related to an action; **alerts** only for important, interrupting information with 1–2 actions.
- **Controls:** native switches for settings, segmented controls for 2–5 views, pickers and date pickers, swipe actions on list rows (with the same actions also reachable via context menu or detail screen), context menus on long-press.
- **Lists:** grouped inset lists for settings; plain lists for content. Disclosure chevrons indicate drill-down.
- **Type:** SF Pro (system font) with Dynamic Type text styles (Large Title, Title 1–3, Headline, Body 17pt, Callout, Subheadline, Footnote, Caption). Use the text styles rather than fixed sizes so user settings apply.
- **Color:** system colors adapt to light/dark and increased contrast automatically; the app's tint color marks interactive elements. Use semantic system backgrounds (systemBackground, secondarySystemBackground, grouped variants).
- **Icons:** SF Symbols, which match the system font's weight and scale with Dynamic Type.
- **Feel:** fluid, interruptible, spring-based motion; content-first with minimal chrome; translucency ("materials") for bars and overlays.

## 3. Android (Material Design 3)

- **Navigation:** a **navigation bar** (bottom) for 3–5 destinations on phones; **navigation rail** on medium screens; **navigation drawer** for many destinations or large screens. Top app bar with the screen title and actions. System back (including predictive back gesture) must always work.
- **Primary action:** a **floating action button (FAB)** for the screen's single most important constructive action (compose, create), when there is one.
- **Modality:** bottom sheets (standard and modal), dialogs for decisions, snackbars (with an optional single action like Undo) for brief feedback.
- **Controls:** switches, chips (filter, input, suggestion, assist), segmented buttons, sliders, Material date and time pickers.
- **Type:** Roboto or the system font (or a brand font) on the Material type scale (Display, Headline, Title, Body, Label; each in Large/Medium/Small; Body Large is 16sp). Use sp so text follows the user's font scale.
- **Color:** tonal palettes with color roles (primary, secondary, tertiary, surface, surface containers at several levels, error, outline). **Dynamic color** can derive the palette from the user's wallpaper; brand apps may opt to keep brand colors.
- **Shape:** a shape scale from extra-small to extra-large corners; larger components get rounder corners.
- **Elevation:** expressed mainly as tonal surface color changes (surface containers) rather than shadows.
- **Motion:** emphasized easing and container transforms that connect elements across screens.

## 4. Cross-platform and mobile web

- **Decide how native it should feel.** Fully platform-adaptive (different navigation and controls per OS), or a consistent brand UI across platforms that still respects key conventions (back behavior, system text size, safe areas, platform gestures, share sheets). The second is fine; ignoring conventions entirely is not.
- **Keep platform-critical behaviors native** even in a branded UI: back navigation, text selection, keyboard handling, date pickers, share and permission dialogs.
- **Mobile web specifics:** `100dvh` (not `100vh`); `env(safe-area-inset-*)` with `viewport-fit=cover`; 16px minimum input text to prevent iOS zoom on focus; `inputmode` and `autocomplete` for the right keyboards and autofill; avoid fixed bottom bars that collide with the browser's own UI; test in real mobile browsers, not just a resized desktop window.
- **Progressive web apps:** a manifest with icons and a theme color, an offline fallback, and installability; still respect the platform's navigation expectations.

## 5. Tablets and large screens

- Don't just stretch the phone layout. Use the space: list–detail side by side, navigation rail or sidebar instead of bottom bar, multi-column content, and popovers instead of full-screen sheets.
- Support both orientations, split-screen/multitasking widths, and pointer and keyboard input (hover states, keyboard shortcuts, right-click menus) on iPad and Android tablets and foldables.
- Keep reading widths constrained on large screens; a 1,200px-wide paragraph is as bad on a tablet as on a desktop.
