# Implementation: tokens in real stacks

How to carry the design system into the tools most front-end work actually uses: plain CSS, Tailwind (v4 and v3), shadcn/ui and other component libraries, and single-file HTML. The goal everywhere is the same: decisions live in tokens, components use only tokens, and the framework's defaults don't leak through as "the look".

## Contents
1. Plain CSS
2. Tailwind CSS v4
3. Tailwind CSS v3
4. Avoiding the default Tailwind look
5. shadcn/ui
6. Other component libraries
7. Component code that covers every state
8. Single-file HTML pages and prototypes
9. Theme switching without a flash

---

## 1. Plain CSS

Copy `assets/tokens.css` into the project, edit its DECISIONS block, and write components against the semantic tokens (`var(--color-surface)`, `var(--space-4)`, `var(--radius-md)`). Use `@layer` to keep resets, tokens, components, and utilities in a predictable order:

```css
@layer reset, tokens, components, utilities;
@import url("tokens.css") layer(tokens);
```

## 2. Tailwind CSS v4

Tailwind v4 is configured in CSS with `@theme`. Variables in theme namespaces (`--color-*`, `--font-*`, `--text-*`, `--radius-*`, `--shadow-*`, `--ease-*`, `--spacing`, …) generate utilities. tokens.css deliberately uses the same namespaces, so semantic tokens map directly to classes like `bg-surface`, `text-text-muted`, `border-border-control`, `rounded-md`, `shadow-md`.

Pattern:
- Keep DECISIONS, ramps, and status hues in plain `:root` (copied from tokens.css).
- Put the **light** semantic values in `@theme`, so Tailwind generates the utilities.
- Keep the **dark** overrides as ordinary CSS blocks. Utilities read the variables at runtime, so dark mode follows automatically.
- **Reset Tailwind's default palette** with `--color-*: initial;` so classes like `bg-indigo-500` don't exist and can't creep in.

```css
@import "tailwindcss";

:root {
  --neutral-h: 70; --neutral-c: 0.010;
  --accent-h: 160; --accent-c: 0.11;
  --radius-base: 6px;
  /* …neutral and accent ramps, status hues from tokens.css… */
}

@theme {
  --color-*: initial;                     /* remove the default palette */
  --color-bg: oklch(0.99 0.002 var(--neutral-h));
  --color-surface: var(--neutral-0);
  --color-surface-sunken: var(--neutral-100);
  --color-text: var(--neutral-950);
  --color-text-muted: oklch(0.46 var(--neutral-c) var(--neutral-h));
  --color-text-subtle: oklch(0.51 var(--neutral-c) var(--neutral-h));
  --color-border: var(--neutral-200);
  --color-border-control: oklch(0.64 var(--neutral-c) var(--neutral-h));
  --color-accent: var(--accent-600);
  --color-accent-hover: var(--accent-700);
  --color-accent-contrast: var(--neutral-0);
  --color-accent-subtle: var(--accent-100);
  --color-focus: var(--accent-500);
  --color-danger: oklch(0.52 0.18 25);
  /* …the rest of the semantic roles… */

  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-display: "Instrument Serif", ui-serif, serif;
  --radius-sm: calc(var(--radius-base) * 0.5);
  --radius-md: var(--radius-base);
  --radius-lg: calc(var(--radius-base) * 1.5);
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
}

:root[data-theme="dark"] {
  --color-bg: oklch(0.17 0.006 var(--neutral-h));
  --color-surface: oklch(0.205 0.006 var(--neutral-h));
  /* …dark values from tokens.css (and the same block inside a prefers-color-scheme query)… */
}

@custom-variant dark (&:where([data-theme="dark"], [data-theme="dark"] *));
```

Notes:
- Tailwind's spacing is already a 4px scale (`--spacing: 0.25rem`; `p-4` = 16px). Stay on the scale steps (1, 2, 3, 4, 6, 8, 12, 16, 24, 32) and avoid arbitrary values like `p-[13px]`.
- With semantic tokens that switch per theme, you rarely need `dark:` variants. Use them for one-off exceptions only.
- Since the namespace is `--color-*`, a token named `--color-text` produces `text-text`. That's slightly awkward but explicit. Rename to `--color-fg`, `--color-fg-muted` if you prefer `text-fg`.

## 3. Tailwind CSS v3

Point the theme at CSS variables defined in a global stylesheet (tokens.css), and replace rather than extend the color palette:

```js
// tailwind.config.js
module.exports = {
  darkMode: ["selector", '[data-theme="dark"]'],
  theme: {
    colors: {                             // replaces the default palette
      transparent: "transparent", current: "currentColor",
      bg: "var(--color-bg)", surface: "var(--color-surface)", sunken: "var(--color-surface-sunken)",
      fg: "var(--color-text)", muted: "var(--color-text-muted)", subtle: "var(--color-text-subtle)",
      border: "var(--color-border)", control: "var(--color-border-control)",
      accent: { DEFAULT: "var(--color-accent)", hover: "var(--color-accent-hover)", contrast: "var(--color-accent-contrast)", subtle: "var(--color-accent-subtle)" },
      danger: "var(--color-danger)", success: "var(--color-success)", warning: "var(--color-warning)",
    },
    extend: {
      borderRadius: { sm: "var(--radius-sm)", md: "var(--radius-md)", lg: "var(--radius-lg)", xl: "var(--radius-xl)" },
      boxShadow: { xs: "var(--shadow-xs)", sm: "var(--shadow-sm)", md: "var(--shadow-md)", lg: "var(--shadow-lg)", xl: "var(--shadow-xl)" },
      fontFamily: { sans: "var(--font-sans)", display: "var(--font-display)", mono: "var(--font-mono)" },
      transitionTimingFunction: { out: "var(--ease-out)", in: "var(--ease-in)" },
    },
  },
};
```

## 4. Avoiding the default Tailwind look

Tailwind's defaults are excellent, which is exactly why they're recognizable. The tells: `bg-indigo-600` buttons, `rounded-2xl shadow-xl` cards, `bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500`, `text-gray-500` everywhere, `tracking-tight` on every heading regardless of size, and `hover:scale-105` on cards.
- **Replace the palette** (above) so color choices are forced through your tokens.
- **Set the radius and shadow scales** to your direction rather than reaching for `rounded-2xl`/`shadow-xl` by habit.
- **Pick a typeface** and set `--font-sans`; the system stack is a decision, not a fallback.
- **Extract repeated class strings into components** (or `@apply` sparingly). A button with 20 utilities copied to 30 places is guaranteed to drift.
- **Order classes predictably** (prettier-plugin-tailwindcss) so reviewers can see what changed.

## 5. shadcn/ui

shadcn/ui gives you accessible, well-built components (on headless primitives such as Radix) as source code you own. Its default theme (neutral grays, Inter or Geist, `--radius: 0.5–0.625rem`, black primary buttons) is now one of the most recognizable looks on the web. Treat it as a starting point.

Its variables map to this skill's tokens:
| shadcn variable | This skill |
|---|---|
| `--background` / `--foreground` | `--color-bg` / `--color-text` |
| `--card`, `--popover` (+ `-foreground`) | `--color-surface`, `--color-surface-raised` |
| `--primary` / `--primary-foreground` | `--color-accent` / `--color-accent-contrast` |
| `--secondary` | neutral button fill (`--color-surface-sunken`) |
| `--muted` / `--muted-foreground` | `--color-surface-sunken` / `--color-text-muted` |
| `--accent` / `--accent-foreground` | **hover/selected surface** (`--color-surface-hover`), not the brand accent |
| `--destructive` | `--color-danger-solid` |
| `--border` | `--color-border` |
| `--input` | `--color-border-control` (needs 3:1; shadcn's default is lighter) |
| `--ring` | `--color-focus` |
| `--radius` | `--radius-base` |

Watch out:
- **shadcn's `--accent` is not a brand accent.** It's the subtle hover background for menu items and ghost buttons. Your brand color goes in `--primary`.
- **Input borders** in the default theme are below 3:1 against the background; darken `--input` for accessible form controls.
- **Customize more than colors:** radius, font, control heights (default `h-9`), and density. Edit the component files directly; that's the point of owning them.
- **Use its semantic variables in your own components** too (`bg-card`, `text-muted-foreground`) so everything themes together.

## 6. Other component libraries

- **Headless primitives** (Radix, React Aria, Headless UI, Ark UI, Base UI, Melt UI) give accessible behavior (focus management, keyboard support, ARIA) with no styling. They're ideal with your own tokens. Don't hand-roll dialogs, comboboxes, menus, or date pickers when these exist.
- **Styled libraries** (MUI, Mantine, Chakra, Ant Design) have their own theme objects. Map your tokens into their theme (palette, typography, shape/radius, spacing) rather than overriding component CSS piecemeal. Expect them to keep some of their character; choose them when speed matters more than identity.
- **In an existing codebase, the existing library wins.** Learn its theming API and work within it.

## 7. Component code that covers every state

Build state coverage into the component API so it can't be forgotten:

```tsx
// Variants and states expressed as props; styles come only from tokens.
type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "ghost" | "danger";
  size?: "sm" | "md" | "lg";
  loading?: boolean;
};

export function Button({ variant = "secondary", size = "md", loading, disabled, children, ...rest }: ButtonProps) {
  return (
    <button
      className={`btn btn-${variant} btn-${size}`}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      {...rest}
    >
      {children}
    </button>
  );
}
```

- Style states from attributes (`[aria-busy]`, `[aria-invalid]`, `[aria-expanded]`, `[data-state="open"]`, `:disabled`), not from parallel class names, so visual state and accessible state can't disagree.
- Data components take `loading`, `error`, and `empty` into account explicitly (or are wrapped by a pattern that does), so each screen has to decide what those look like.
- Keep realistic fixtures (long names, empty arrays, errors) next to components (Storybook stories or a demo page) and look at them.

## 8. Single-file HTML pages and prototypes

For standalone pages, demos, and artifacts:
- Inline the tokens you use in a `<style>` block (the DECISIONS, ramps, and semantic roles from tokens.css are ~150 lines). Don't link to files that won't exist.
- Load fonts from Google Fonts with `preconnect` and `display=swap`, limited to the weights you use:
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  ```
- Use real (or realistic) content and include at least one non-ideal state (empty, error, long content) if the page is a UI demo.
- Support dark mode via the tokens' `prefers-color-scheme` block. It's nearly free once tokens are semantic.
- Inline SVG icons (Lucide, Phosphor, and Heroicons publish raw SVGs) rather than an icon font.

## 9. Theme switching without a flash

Apply the saved theme before first paint with a tiny inline script in `<head>`:

```html
<script>
  try {
    const t = localStorage.getItem("theme");
    if (t === "light" || t === "dark") document.documentElement.dataset.theme = t;
  } catch {}
</script>
```

A three-way control (Light / Dark / System) is the respectful default. "System" removes the attribute and lets `prefers-color-scheme` decide.
