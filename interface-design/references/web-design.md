# Web design: sites, landing pages, and editorial pages

Apps are used; websites are read, scanned, and judged in seconds. A site has to answer a visitor's questions in the order they arise, earn trust, and lead to one clear next step, while loading fast on a mediocre phone.

## Contents
1. Start with the visitor's questions
2. The hero
3. Page structure and section rhythm
4. Copy that does the work
5. Imagery and visuals
6. Navigation, header, footer
7. Social proof and trust
8. Pricing pages
9. Editorial and long-form pages
10. Documentation sites
11. Performance is design
12. Semantics, SEO, and sharing
13. Avoiding the template look

---

## 1. Start with the visitor's questions

Before designing sections, write down what a first-time visitor needs to know, in order. For a product page, usually:
1. **What is this?** (in one sentence, in plain words)
2. **Is it for me?** (who it's for, what problem it solves)
3. **Why this one?** (what's different or better, with evidence)
4. **Does it actually work?** (show the product; proof from real users)
5. **What does it cost / what's the catch?**
6. **What do I do next?**

The page is those answers, in that order, with the call to action available whenever someone is convinced. Every section should answer a question; sections that don't are filler.

## 2. The hero

The first screen gets a few seconds. It must deliver:
- **A headline that says what it is or what it does for them,** specifically. 4–10 words. "Accounting software for freelancers who hate accounting" beats "The future of finance." If you could swap in a competitor's name and the headline still works, it's too generic.
- **A subhead** (1–2 sentences, ~20–30 words) adding the how or the who.
- **One primary CTA** with a specific label ("Start free trial", "Book a demo", "Download for Mac"), and optionally one secondary, lower-emphasis action ("See how it works").
- **The product itself:** a real screenshot, a short looping demo, the actual object. People want to see what they're getting. Abstract 3D shapes, gradient meshes, and stock photos of people pointing at laptops communicate nothing.

Layout notes:
- Left-aligned hero text with the visual on the right (or below on mobile) is the most readable. Centered heroes work for short headlines with a strong visual below.
- The hero doesn't need to be 100vh. A hint of the next section below the fold invites scrolling; a full-screen hero with a lonely headline wastes the most valuable space.
- Headline size: 40–72px on desktop, 32–44px on mobile (use fluid type), with tight leading (1.05–1.15) and tight tracking.
- The "✨ New: we raised a Series A →" pill badge above every headline is a cliché. Use an announcement only when there's real news.

## 3. Page structure and section rhythm

A common, effective order for product landing pages (use what applies):
1. Hero
2. Logos or a one-line proof point (only if real and recognizable)
3. The problem, or the key benefit, in a strong statement
4. How it works (3 steps, or a walkthrough with real screenshots)
5. Features, each shown with a visual and tied to a benefit
6. Testimonials or case studies with specifics
7. Pricing or a pricing teaser
8. FAQ (handles objections)
9. Final CTA
10. Footer

**Rhythm:** vary the layout from section to section: a split (text + image), a full-width visual, a single large statement, a grid, a quote. A page where every section is "centered heading, gray subtitle, three cards" is the defining template look.

**Spacing:** consistent vertical spacing between sections (96–160px desktop, 64–96px mobile; `--space-section` in tokens.css). Within a section, the heading-to-content gap is much smaller than the section gap.

**Backgrounds:** an occasional full-bleed tinted or dark band can mark a shift (a testimonial, the final CTA), but alternating backgrounds on every section is noisy. Whitespace separates sections well enough.

**Width:** content inside a ~1120–1280px container; paragraphs no wider than ~65ch even inside wide sections.

## 4. Copy that does the work

On marketing pages, copy is the design. Layout only stages it.
- **Specific over grand:** "Close your books in 2 hours, not 2 days" over "Revolutionize your financial workflow." Numbers, names, concrete outcomes.
- **Benefits backed by features:** lead with what the user gets, then the feature that delivers it.
- **Headings carry the message.** Someone who reads only the headings should get the pitch. "Features" is a label; "Every invoice reconciled automatically" is a message.
- **Cut the clichés:** unlock, supercharge, seamless, revolutionize, next-generation, cutting-edge, empower, leverage, game-changer, all-in-one platform, "built for the modern…". They signal that nothing specific was said.
- **Use the customer's words.** Lift phrases from reviews, support tickets, and interviews.
- **Short paragraphs, plain words, active voice.** Read it aloud; if it sounds like a press release, rewrite it.
- **CTA labels name the outcome:** "Get my free report", "Start building". Not "Submit" or "Learn more" everywhere.
- **Never invent stats, testimonials, customer logos, or awards.** If real ones aren't available, use clearly marked placeholders and tell the user, or design the section around something true (a product screenshot, a clear explanation).

## 5. Imagery and visuals

- **Show the real product.** Screenshots at actual size or cropped to the relevant part, in a simple frame or device. Annotate them if a detail matters. Keep the UI in screenshots current.
- **Crop for focus:** a tight crop of the key interaction beats a full-screen screenshot shrunk to illegibility.
- **People photos:** real customers or team over stock. If stock is unavoidable, choose candid, specific images and treat them consistently (same crop style, color grade).
- **Illustrations:** one style, one hand, consistent palette and stroke weight. Generic "blob people" illustration sets read as default.
- **Consistency of treatment:** same corner radius, shadow, and border on all screenshots; the same aspect ratios in a set.
- **Technical:** always set `width`/`height` or `aspect-ratio` to prevent layout shift; use `srcset`/`sizes` and modern formats (AVIF/WebP); `loading="lazy"` below the fold; `fetchpriority="high"` on the hero (LCP) image; use `<picture>` for art direction (a different crop on mobile).
- **Alt text** describes the content and purpose ("Dashboard showing monthly revenue trending up 12%"); decorative images get `alt=""`.

## 6. Navigation, header, footer

- **Header:** logo left (links home), 3–6 links, one CTA button right; login as a text link beside it. Sticky headers should be compact (56–64px) and may shrink or gain a background and border on scroll.
- **Mega menus** only for genuinely large sites; organize with clear group labels and short descriptions.
- **Mobile:** a menu button opening a full-screen or sheet menu with large tap targets; keep the primary CTA visible outside the menu.
- **Footer:** the place for completeness: product links, company, resources, legal, social, a newsletter signup. Organized in labeled columns, quieter type, generous spacing. It's also a navigation fallback for people who scroll to the bottom looking for something.
- **Anchor links** to sections need `scroll-margin-top` equal to the sticky header height.

## 7. Social proof and trust

- **Testimonials:** a specific quote about a specific result, with a real name, role, company, and photo. "This tool is amazing!" from "Sarah K." persuades no one.
- **Logos:** grayscale or single-color, consistent optical size (not equal width; visually equal weight), 5–8 max, labeled honestly ("Used by teams at…").
- **Numbers:** only real, sourced, meaningful ones ("4,200 accountants", not "10x productivity").
- **Case studies** with a before/after and concrete numbers outperform quote walls.
- **Trust details:** clear pricing, a real address and contact, security and compliance info where relevant, a visible privacy policy, no dark patterns (pre-checked marketing boxes, fake countdown timers, hidden cancel flows).

## 8. Pricing pages

- **2–4 tiers**, side by side, with the recommended one highlighted (border, badge "Most popular", slight emphasis), not shouted.
- **Each tier:** name, who it's for (one line), price with billing period clear ("$12 per user / month, billed annually"), primary CTA, and the 4–8 features that differentiate it ("Everything in Starter, plus:").
- **Monthly/annual toggle** with the saving stated; the default should match what most customers choose.
- **Full comparison table** below for detail-seekers, with sticky tier headers.
- **FAQ** for billing, cancellation, trials, refunds.
- Align prices, buttons, and feature lists across cards on a shared baseline (CSS subgrid helps).

## 9. Editorial and long-form pages

Reading experience is everything:
- **Body text 18–21px** with line height 1.6–1.75 and a measure of 60–70ch. A serif often reads beautifully at these sizes.
- **Strong heading hierarchy** and more space above headings than below.
- **Typographic texture:** pull quotes, drop caps (once, at the start), figures with captions, footnotes or sidenotes on wide screens.
- **Images** can break wider than the text column for emphasis (a "breakout" grid: text column centered, images spanning wider).
- **Table of contents** for long pieces (sticky on desktop, highlighting the current section), estimated reading time, and a visible publish/updated date.
- **Minimal chrome:** reduce or hide navigation while reading; no sidebars of ads and "related content" competing with the text.
- **Links** clearly underlined; citations accessible.

## 10. Documentation sites

- Three-column layout on desktop: section nav (left), content (center, ~65–75ch), on-page table of contents (right).
- Search is the primary navigation; make it fast and prominent (⌘K).
- Code blocks: syntax highlighting with a calm theme, copy button, language label, line highlighting for the important part, horizontal scroll rather than wrapping.
- Callouts (note, warning, tip) used sparingly and consistently.
- Every page answers "what is this, how do I use it, show me an example". Examples first, reference second.
- Previous/next links at the bottom; "Edit this page" and last-updated date.

## 11. Performance is design

A beautiful page that takes 6 seconds to appear on a phone is a bad design. Targets (Core Web Vitals, 75th percentile of real users):
- **LCP** (largest content visible) ≤ 2.5s
- **INP** (response to interaction) ≤ 200ms
- **CLS** (layout shift) ≤ 0.1

Design decisions that affect them:
- **Hero media:** an optimized image (AVIF/WebP, correctly sized, `fetchpriority="high"`) beats an autoplay video. If video, use a poster image, keep it short and muted, and lazy-load.
- **Fonts:** 2–4 files, preloaded, `font-display: swap` with metric-matched fallbacks (see typography.md).
- **Avoid shift:** dimensions on all media, reserved space for embeds and banners, no content injected above what the user is reading.
- **JavaScript:** static content shouldn't require a heavy client framework to render. Ship HTML; hydrate only interactive islands.
- **Effects budget:** large `backdrop-filter` blurs, many box-shadows on scroll, and scroll-linked JS animations hurt low-end devices.

## 12. Semantics, SEO, and sharing

- **One `<h1>` per page** (the main headline), with headings in logical order. Landmarks: `<header>`, `<nav>`, `<main>`, `<footer>`, `<section>`s with headings.
- `<html lang="…">`, a unique `<title>` ("Page – Brand"), and a `<meta name="description">` written like ad copy.
- **Open Graph and Twitter card** tags with a designed 1200×630 share image; it's often the first impression of the page.
- **Favicon** set (SVG plus PNG fallbacks, apple-touch-icon) and `theme-color`.
- Real text, not text baked into images.
- A skip link to main content (see accessibility.md).

## 13. Avoiding the template look

The default AI/template landing page: centered hero with gradient text, an indigo-to-purple glow, a pill badge, two buttons, a fake dashboard floating at an angle, a logo strip, three feature cards with emoji icons, a testimonial carousel, a 3-tier pricing table, and a gradient CTA band. Each element is fine; together they say "nobody decided anything".

To make it particular:
- **Start from the content and audience,** not the section list. What would a thoughtful designer at this specific company emphasize?
- **Make one strong choice that's ownable:** a distinctive typeface, an unexpected but fitting color, a layout idea that comes from the product (a timeline for a scheduling tool, a document metaphor for a writing app), photography with a point of view, or a signature illustration style.
- **Show, don't decorate.** Real product, real numbers, real people.
- **Let typography lead.** Big, well-set type with confident whitespace is more distinctive than any amount of gradients and glow.
- **Edit ruthlessly.** Fewer sections, each excellent.

See `aesthetic-directions.md` for concrete directions to start from.
