# Aesthetic directions

A visual direction is a coherent set of decisions that all point the same way. Coherence is what makes something look designed: type, color, shape, density, and motion that agree with each other and with the product's personality.

This file gives worked directions as starting points. Pick the one closest to the product, adjust it, and add one signature element of your own. Avoid the default no-direction look (system-blue or indigo accent, Inter at every size, 12px radius, soft shadows on everything, centered sections). It's competent, and it's invisible.

## Contents
1. How to choose a direction
2. Directions
   - Precise utility
   - Editorial
   - Warm and human
   - Dense and technical
   - Swiss / typographic
   - Quiet luxury
   - Bold and playful
   - Raw / neo-brutalist
3. Making it yours: the signature element
4. Translating a brand into a direction
5. Mixing rules

---

## 1. How to choose a direction

Answer three questions:
1. **Who is it for, and what's their state of mind?** A developer debugging at 2am, a parent booking a pediatrician, a CFO scanning a report, a teenager customizing a profile.
2. **What should it feel like in three adjectives?** Be specific: "calm, precise, quietly confident" is useful; "modern, clean, professional" describes everything and so decides nothing.
3. **What's the context of use?** Daily tool vs. occasional visit; desktop-heavy vs. mobile; reading vs. operating; marketing site vs. product UI.

Then pick the direction whose personality matches, and check it against the adjectives. A product can use different intensities across surfaces: a bolder marketing site and a calmer version of the same direction inside the product.

## 2. Directions

Each direction lists its tokens in terms of the DECISIONS block in `assets/tokens.css`.

---

### Precise utility
*Feels like:* calm, fast, exact, trustworthy. The interface gets out of the way.
*Fits:* SaaS products, productivity tools, developer platforms, B2B dashboards. Think Linear, Vercel, Stripe's dashboard.

- **Type:** one neo-grotesque or neutral sans (Geist, Inter, IBM Plex Sans, or system UI). 14px base in the app, 16px on marketing. Headings semibold, modest sizes, slightly tight tracking (−0.01 to −0.02em). Mono for IDs, keys, and code.
- **Color:** cool or pure neutrals (`--neutral-h: 260`, `--neutral-c: 0.004–0.01`). Accent used sparingly, either a specific blue/violet (`--accent-c` 0.12–0.16) or near-black primary buttons with color reserved for links and focus. Dark mode is often the hero.
- **Shape:** 6–8px radius; hairline borders (`--color-border`) instead of shadows on resting surfaces; shadows only for floating layers.
- **Density:** medium-compact. 32–36px controls in the app.
- **Motion:** fast (100–200ms), ease-out, no bounce. Instant for frequent actions.
- **Signature moves:** impeccable alignment, keyboard shortcuts shown in menus, subtle 1px inner highlights on dark surfaces, crisp iconography (Lucide/Phosphor at 1.5px stroke), monospace numerals in data.
- **Pitfalls:** sterile sameness. Without one distinctive choice (a custom accent, a well-chosen typeface, great empty states) it reads as "another dev tool".

---

### Editorial
*Feels like:* thoughtful, literary, considered, authoritative.
*Fits:* publications, blogs, essays, documentation with a voice, cultural institutions, writing tools, premium content.

- **Type:** a serif with character for headlines (Newsreader, Fraunces, Instrument Serif, Source Serif display), the same serif or a quiet sans for text, at generous sizes (18–21px body, line height 1.6–1.7, 65ch measure). Large headline scale (ratio 1.333–1.5). Italics used beautifully. Small caps or tracked uppercase for kickers and bylines.
- **Color:** warm neutrals (`--neutral-h: 70–85`, `--neutral-c: 0.01–0.015`), off-white "paper" background, near-black ink. Accent minimal: a deep red, ink blue, or forest green, mostly for links.
- **Shape:** 0–4px radius; rules (thin horizontal lines) to separate content instead of boxes; almost no shadows.
- **Density:** spacious, with strong vertical rhythm.
- **Motion:** almost none. Gentle fades at most.
- **Signature moves:** drop caps, pull quotes with hanging punctuation, figure captions, asymmetric layouts with wide margins, footnotes as sidenotes, a refined masthead.
- **Pitfalls:** precious and slow if the type is too small or light, or the layout too clever. Keep body text legible and links obvious.

---

### Warm and human
*Feels like:* friendly, approachable, reassuring, optimistic.
*Fits:* consumer apps, health, education, personal finance for beginners, community products, onboarding-heavy products.

- **Type:** a humanist or soft geometric sans (Figtree, DM Sans, Nunito Sans, Plus Jakarta Sans, Manrope), or a soft serif display (Fraunces with soft optical settings, Young Serif) paired with a friendly sans. 16–17px base.
- **Color:** warm neutrals (`--neutral-h: 60–80`), a warm or fresh accent (coral, terracotta, sunflower, teal, leafy green) at moderate chroma (0.12–0.16). Tinted section backgrounds (accent-50) used sparingly. Illustrations with a limited palette.
- **Shape:** 12–16px radius; pill buttons fit; soft, diffuse shadows.
- **Density:** comfortable. 44–48px controls, generous whitespace.
- **Motion:** soft ease-out, slight spring on celebratory moments; still quick.
- **Signature moves:** custom illustrations or real photography of people, conversational microcopy, encouraging empty states, celebratory moments for milestones (once, briefly).
- **Pitfalls:** saccharine or childish when overdone. Too many colors, bouncy animations everywhere, and cutesy copy in serious moments (errors, payments).

---

### Dense and technical
*Feels like:* powerful, information-rich, expert, no-nonsense.
*Fits:* trading, monitoring, analytics, logs, IDEs, admin consoles, scientific tools.

- **Type:** a compact sans with excellent tabular figures (Inter, IBM Plex Sans, Geist, Roboto) at 13–14px; mono (JetBrains Mono, IBM Plex Mono, Geist Mono) for data, logs, IDs. Tight scale (ratio 1.125–1.2).
- **Color:** neutral-dominant, often dark-first. Color reserved for status and data, and used consistently (green up, red down, plus signs and arrows). Accent subdued so status colors stay legible.
- **Shape:** 2–6px radius; dividers and gridlines rather than cards; panels split by 1px lines.
- **Density:** compact (`--density: 0.875`). 28–32px rows, small paddings, resizable panes.
- **Motion:** minimal and fast; live data updates with subtle highlight flashes, not animations.
- **Signature moves:** keyboard-everything, command palette, sticky headers and columns, sparkline-rich tables, monospace alignment, configurable layouts.
- **Pitfalls:** clutter. Density demands strict alignment, consistent row heights, and clear typographic hierarchy, or it becomes a wall of noise.

---

### Swiss / typographic
*Feels like:* rational, bold, confident, graphic.
*Fits:* design studios, architecture, events, cultural organizations, portfolios, brands that want typographic presence.

- **Type:** a strong grotesque (Inter Display, Archivo, Schibsted Grotesk; commercial: Helvetica Now, Neue Haas Grotesk) used at dramatic size contrasts: huge headlines (80–160px, tight leading 0.9–1.0, tight tracking), small body. Flush-left, ragged-right always.
- **Color:** black, white, and one strong primary (red, cobalt, signal orange, or yellow) used in large confident blocks. Or monochrome.
- **Shape:** 0 radius. Visible grid. Rules and blocks of color instead of shadows.
- **Density:** generous whitespace with dense information blocks; strong asymmetric grid.
- **Motion:** crisp, linear-ish or no motion; hard cuts over fades.
- **Signature moves:** oversized numerals, text running at the grid edge, information arranged like a poster, captions and metadata set small in a grid.
- **Pitfalls:** cold or illegible when the hierarchy relies only on size; huge type must still read well on mobile (fluid type with sane minimums).

---

### Quiet luxury
*Feels like:* refined, calm, expensive, restrained.
*Fits:* fashion, hospitality, premium goods, jewelry, real estate, high-end services.

- **Type:** an elegant high-contrast serif (Cormorant, Instrument Serif, Playfair, a Didone) at large sizes with light-to-regular weight; a small, widely tracked sans (uppercase, +0.1em) for navigation and labels.
- **Color:** a restrained palette: ivory, stone, charcoal, maybe a single muted accent (deep green, oxblood, champagne). Very low chroma overall.
- **Shape:** 0 radius, or very small. Hairlines. No shadows.
- **Density:** very spacious; lots of empty space; few elements per screen.
- **Motion:** slow, gentle fades (300–500ms) and subtle image reveals; never bouncy.
- **Signature moves:** full-bleed photography of exceptional quality, generous margins, minimal copy, thoughtful details (custom cursor, refined hover states on images).
- **Pitfalls:** light-gray thin type that fails contrast; navigation so minimal it's undiscoverable; slowness. Luxury still has to work.

---

### Bold and playful
*Feels like:* energetic, confident, fun, youthful.
*Fits:* creative tools, consumer social, games, youth brands, events, products that want to stand out.

- **Type:** an expressive display face (Bricolage Grotesque, Syne, Unbounded; free from Fontshare: Clash Display, Cabinet Grotesk; or a chunky serif) at big sizes; a friendly sans for text.
- **Color:** a vivid palette of 2–3 saturated colors with good contrast between them, or one vivid color against black and white. High chroma (0.18+) used in large blocks.
- **Shape:** large radii (16–24px) or mixed shapes (circles, blobs, stickers) used deliberately; chunky outlines.
- **Density:** comfortable, with oversized elements.
- **Motion:** springy, characterful, with some overshoot; hover interactions with personality (still fast and non-blocking).
- **Signature moves:** custom illustration or 3D with a consistent style, playful cursors or hover states, unexpected color combinations, stickers and badges, big emoji used intentionally.
- **Pitfalls:** chaos and low contrast. Vivid backgrounds with white text often fail contrast; keep the content areas calm so the playfulness frames, rather than fights, the content.

---

### Raw / neo-brutalist
*Feels like:* honest, unpolished on purpose, rebellious, memorable.
*Fits:* indie products, portfolios, zines, developer side projects, brands targeting designers and developers.

- **Type:** mono or a plain grotesque, sometimes system defaults used deliberately; strong size contrast.
- **Color:** high contrast: black, white, and one or two loud flat colors (acid yellow, hot pink, electric blue). No gradients.
- **Shape:** thick black borders (2–3px), hard offset shadows (`4px 4px 0 #000`, no blur), 0 radius or a uniform chunky radius.
- **Density:** variable; often dense with visible structure.
- **Motion:** snappy, no easing finesse needed; hover states that shift elements by the shadow offset ("press").
- **Signature moves:** exposed grid lines, marquee text, visible structure, raw HTML aesthetics with deliberate polish underneath.
- **Pitfalls:** it's a costume if it doesn't fit the brand. Accessibility still matters: thick borders help, but loud colors must still pass contrast.

---

## 3. Making it yours: the signature element

A direction gets you coherence. A signature element gets you identity. Choose one or two, never all:
- **A distinctive typeface** used confidently (the biggest single lever).
- **An ownable color:** not "blue" but a specific blue, or an unexpected hue that fits (a deep teal for a bank, a warm orange for a dev tool).
- **A layout idea from the product's own world:** a ledger for an accounting tool, a timeline for a scheduling app, index cards for a research tool, a terminal for a CLI.
- **An illustration or photography style** that's consistent and recognizable.
- **A detail system:** a particular corner treatment, a distinctive focus ring, a custom cursor, a texture, a characteristic micro-interaction.
- **A voice:** copy with a recognizable personality (which also shapes the visual tone).

Repeat the signature consistently, and keep everything else quiet so it can stand out.

## 4. Translating a brand into a direction

When given brand assets (logo, colors, guidelines):
1. **Extract the essentials:** brand color(s) → `color.py convert` to get hue and chroma; logo shapes → radius and geometry cues (a rounded wordmark suggests softer radii); brand fonts (check licensing for web use).
2. **Decide where brand color lives.** Often it's the accent; but if the brand color is red/orange/green, or very light, it may work better in brand moments (marketing, illustrations, logo) while the UI uses a near-black or derived accent.
3. **Derive neutrals** with a hint of the brand hue (`--neutral-h` = brand hue, `--neutral-c` ≈ 0.006–0.012).
4. **Pick the closest direction** above for everything the brand guide doesn't specify (density, motion, depth).
5. **Product UI is quieter than marketing.** A brand's loudest expression belongs on the website and in campaigns. Inside a tool used daily, calm wins.

## 5. Mixing rules

- One direction per product surface. Elements from different directions (Swiss grids with bubbly buttons, luxury serifs with neo-brutalist shadows) look accidental unless the clash is the concept and is executed with conviction.
- Tone down, don't mix: a marketing site and its app can share type, color, and radius while differing in intensity (bigger type, more color, more motion on the site).
- When unsure, go quieter. Restraint rarely looks wrong; excess often does.
