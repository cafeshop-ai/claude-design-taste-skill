# Design critique

How to review a design (a screenshot, a live page, a Figma frame, or your own output) and turn "something feels off" into specific, fixable problems. Also the method to use on your own work before calling it done.

## Contents
1. Mindset
2. The review process
3. The systematic pass
4. Diagnosing "it feels off": symptom → cause
5. The highest-leverage fixes
6. Generic and AI-made tells
7. Reporting a critique
8. Self-review before shipping
9. Worked example: a generic hero, redesigned
10. Worked example: a dashboard card, redesigned

---

## 1. Mindset

- **Critique against goals, not taste.** "This doesn't make the primary action obvious" is useful; "I don't like the blue" isn't (unless the blue fails contrast or clashes with meaning).
- **Prioritize ruthlessly.** Three important problems, clearly explained, beat thirty nitpicks. Lead with what most affects the user's success.
- **Be specific and actionable.** Name the element, the problem, why it matters, and a concrete fix ("The 'Export' and 'Delete' buttons have equal weight; make Export primary and move Delete into the overflow menu").
- **Say what works.** It tells the designer what to keep, and it's often true.
- **Look before reasoning.** If you can render or view the design, do. Many issues (alignment, density, contrast in context) only show up visually.

## 2. The review process

1. **Context:** What is this for? Who uses it? What's the primary task? What constraints exist (brand, platform, existing system)? If unknown, infer and state your assumptions.
2. **Five-second impression:** Look briefly, then look away. What is it? What was the first thing you saw? What would you do next? If the answers don't match the goal, hierarchy is the top issue.
3. **Squint test:** Blur your eyes (or literally blur the screenshot). What stands out? The order of visual weight should match the order of importance. Look for areas that are too heavy (dense, dark, colorful) or too uniform.
4. **Task walk-through:** Do the main task step by step. Where is there hesitation, ambiguity, missing feedback, a dead end?
5. **Systematic pass** (below).
6. **Prioritize and report.**

## 3. The systematic pass

Work through each area; note issues with their location.

**Hierarchy and layout**
- Is there one clear focal point and one clear primary action?
- Does grouping (proximity, alignment, common region) match the logical structure?
- Are elements aligned to a few consistent edges? Anything almost-but-not-quite aligned?
- Is spacing consistent and on a scale? Is the space inside groups smaller than between groups?
- Are widths constrained (text measure, form width)? Anything stretched or cramped?

**Typography**
- How many sizes and weights are in use? (More than ~6 sizes or 3 weights is a smell.)
- Are levels clearly distinct? Is body text at least 16px (or 14px in dense apps)?
- Line lengths, line heights, letter spacing on display and uppercase text?
- Are numbers tabular where they align? Real punctuation?

**Color and contrast**
- Does color carry meaning (action, state, status) or is it decorative?
- How many distinct colors and grays? Can they be reduced?
- Text contrast ≥ 4.5:1, UI boundaries ≥ 3:1, including placeholders and disabled states?
- Is color the only signal anywhere?

**Surfaces and detail**
- Consistent radius, border, and shadow logic? Nested boxes? Borders and shadows doubled up?
- Icon set consistent in style, size, and stroke?
- Concentric radii, optical alignment of icons, consistent image treatment?

**Components and states**
- Are interactive elements recognizable as interactive?
- Hover, focus, active, disabled, loading states present?
- Empty, error, loading, and overflow states designed?
- Button hierarchy clear? Labels are verbs?

**Content and copy**
- Is copy specific and scannable? Headings meaningful?
- Labels in the user's language? Sentence case? Error messages helpful?
- Realistic content, or demo content hiding problems?

**Interaction and flow**
- Is feedback immediate and local? Is it clear what happened after each action?
- Are destructive actions protected (undo or confirmation)?
- Is the navigation clear (where am I, how do I get back)?

**Responsiveness and accessibility**
- Does it work at 375px? Touch targets ≥ 44px? Any hover-only interactions?
- Keyboard operable, visible focus, semantic structure, alt text?

## 4. Diagnosing "it feels off": symptom → cause

| Symptom | Usual causes | Try |
|---|---|---|
| Looks amateur or cheap | inconsistent spacing; too many font sizes and weights; off-scale values; misalignments; heavy or muddy shadows; default browser controls mixed with styled ones; low-quality images | apply a spacing and type scale strictly; align everything to a grid; lighten shadows; restyle or consistently use native controls |
| Cluttered, busy | no hierarchy; every element boxed; too many colors; too many borders and dividers; everything the same weight; too much content per screen | remove boxes and borders, group with space; mute secondary elements; cut or defer content; one accent |
| Bland, generic | no point of view; default font and accent; template layout; generic copy and imagery | choose a direction and a signature element; real product imagery; specific copy; let type lead |
| Hard to scan | long lines; weak heading contrast; centered text blocks; dense paragraphs; labels as loud as values | constrain measure; stronger heading hierarchy; left-align; break up text; de-emphasize labels |
| Dated | heavy gradients, bevels, glossy effects; hard dark drop shadows; tiny text; cramped spacing; overly decorative fonts; very saturated colors on large areas | flatten; softer shadows; bigger type and more space; calmer palette |
| Cold, clinical | pure grays; sharp corners; small, light type; no imagery or warmth in copy | warm the neutrals slightly; adjust radius; warmer accent; human imagery; friendlier microcopy |
| Unbalanced, lopsided | visual weight concentrated on one side; large dark elements without counterweight; inconsistent margins | redistribute weight; balance a heavy image with a strong headline; check that margins match |
| Text-heavy wall | no visual anchors; uniform paragraphs | headings, lists, a figure, a pull quote; shorter paragraphs; bold lead-ins |
| Confusing, "where do I click?" | weak signifiers; flat buttons that look like labels; multiple competing CTAs; links not styled as links | one primary button; clear button styling; underline links; reduce choices |
| Feels slow or janky | no feedback on press; spinners for short waits; layout shift; long or blocking animations | immediate press states; delay spinners; reserve space; shorter ease-out animations |
| Dark mode looks wrong | inverted light theme; pure black; saturated accents vibrating; shadows used for elevation; same borders as light | dedicated dark palette (see color.md) |

## 5. The highest-leverage fixes

When improving an existing design, these usually help most, roughly in this order:
1. **Clarify hierarchy:** decide the single most important element and action; make everything else quieter.
2. **Fix spacing:** apply a consistent scale; increase space between groups, tighten within groups.
3. **Reduce:** fewer colors, fewer sizes, fewer weights, fewer borders, fewer boxes, fewer words.
4. **Improve type:** larger, more legible body text; tighter headings; a constrained measure; a better typeface if needed.
5. **Align:** snap everything to a small set of edges.
6. **Improve copy:** specific headings, verb buttons, helpful empty and error states.
7. **Add the missing states:** hover, focus, loading, empty, error.
8. **Polish details:** consistent radii and icons, refined shadows, real punctuation, tabular numbers.

Most designs improve more from removal than from addition.

## 6. Generic and AI-made tells

Patterns that show that no particular decisions were made. None is forbidden, but each needs a reason:
- **Color:** indigo/violet (#6366f1, #8b5cf6) accents; purple-to-pink or blue-to-purple gradients; gradient text on headlines; glowing blurred orbs behind content; neon accents on near-black.
- **Layout:** centered everything; every section as heading + subtitle + 3-card grid; symmetrical feature grids of identical cards; bento grids of icon + title + sentence.
- **Decoration:** emoji as icons; icons in pastel circles or rounded squares atop every card; colored left-border on every callout; glassmorphism without a reason; a pill badge above the headline; decorative dot grids and noise everywhere.
- **Shape and depth:** the same 12–16px radius and soft drop shadow on every element; cards with border and shadow and tinted background; cards that lift and scale on hover.
- **Type:** Inter at every level with no typographic contrast; headlines in Title Case; weight 800 everywhere; mono for headings to look "techy".
- **Motion:** everything fades and slides in on scroll; perpetual floating animations; typewriter headlines.
- **Copy:** "Unlock the power of…", "Supercharge your workflow", "Seamless", "Revolutionize", "Elevate", "Built for the future"; triplet slogans ("Fast. Simple. Powerful."); invented statistics and testimonials; feature names without explanation.
- **Content:** placeholder avatars; "John Doe"; lorem ipsum; fake logos; a dashboard screenshot with nonsensical charts.

The fix is never more decoration. It's a real decision: a typeface with character, a specific color, a layout that comes from the content, real imagery, copy that says something only this product could say.

## 7. Reporting a critique

Use this structure unless the user asks for something different:

```
**What's working**
- 2–3 genuine strengths worth keeping.

**Top issues** (most impact first)
1. **[Problem in a few words]**, where it is. Why it matters for the user. → Specific fix.
2. …
3. …

**Further refinements**
- Shorter, lower-priority items grouped by area (type, color, spacing, states, copy, accessibility).

**If you only change one thing:** the single highest-impact fix.
```

Guidelines:
- Reference elements precisely ("the stat cards in the second row", "the 'Continue' button in the footer").
- Quantify when possible ("body text is 13px with 1.3 line height, which is cramped for reading; 16px / 1.5").
- Show the fix as values, CSS, or a short before/after when it helps.
- If code is available, offer to apply the fixes.

## 8. Self-review before shipping

Before presenting your own design work, do this pass:
1. **Render it** and look, at mobile and desktop widths (and dark mode if supported). Screenshots catch what code review doesn't.
2. **Squint test** for hierarchy.
3. **Hunt for the generic tells** above in your own output, and replace each with a deliberate choice.
4. **Check states:** hover, focus (tab through it), empty, loading, error, long content.
5. **Check contrast** of any color pairs you weren't sure about (`scripts/color.py contrast`).
6. **Read the copy aloud.** Cut filler; make buttons verbs; make headings say something.
7. **Ask: what would a great designer change?** Then change it.

## 9. Worked example: a generic hero, redesigned

The brief: a landing page hero for **Ledgerly**, bookkeeping software for freelance designers and developers.

**Before: the template default**

```html
<section style="text-align:center; padding:120px 24px; background:radial-gradient(circle at top, #312e81, #0f0f1a)">
  <span class="pill">✨ Introducing Ledgerly 2.0 →</span>
  <h1 style="font-size:64px; font-weight:800; background:linear-gradient(90deg,#818cf8,#ec4899); -webkit-background-clip:text; color:transparent">
    Supercharge Your Financial Workflow
  </h1>
  <p style="color:#9ca3af; font-size:20px">The all-in-one platform to seamlessly manage your finances and unlock your business potential.</p>
  <button class="gradient-btn">Get Started</button> <button class="outline-btn">Learn More</button>
  <!-- three cards below: ⚡ Fast · 🔒 Secure · 📊 Insightful -->
</section>
```

What's wrong, in order of impact:
1. **It says nothing.** "Supercharge your financial workflow" and "all-in-one platform" could be any finance product. A visitor can't tell what it does or who it's for.
2. **No product.** Nothing shows what using it is like.
3. **Every element is a default:** indigo-to-pink gradient text, a glow, an announcement pill, emoji feature cards, weight 800, centered everything, Title Case.
4. **Weak CTAs:** "Get Started" and "Learn More" don't say what happens.
5. **Contrast:** #9ca3af on the dark gradient is borderline; gradient text has uneven contrast across its length.

**After: decisions made**

Direction: *precise utility with warmth*. The audience is designers and developers who care about craft and hate bookkeeping. Decisions: warm neutrals (`--neutral-h: 70`) so it doesn't feel like a bank; a deep green accent (`--accent-h: 160`, `--accent-c: 0.11`), which reads as calm and money-positive, avoiding fintech blue and template violet; Instrument Serif for the headline (a touch of editorial confidence that designers notice) with Inter for UI; 6px radius; light theme first.

```html
<section class="hero">
  <div class="hero-copy">
    <h1>Bookkeeping for people who’d rather be making things.</h1>
    <p class="lede">Ledgerly sorts your transactions, tracks what clients owe you, and sets aside tax as you get paid,
       so the books take minutes a month, not weekends.</p>
    <div class="actions">
      <a class="btn btn-primary btn-lg" href="/signup">Start free for 30 days</a>
      <a class="link-arrow" href="/tour">Take the 2-minute tour →</a>
    </div>
    <p class="fine">No card required · Works with Stripe, PayPal, and 9,000+ banks</p>
  </div>
  <figure class="hero-shot">
    <picture>
      <source media="(max-width: 40rem)" srcset="/img/ledgerly-inbox-crop.avif" width="800" height="900">
      <img src="/img/ledgerly-inbox.avif" width="1280" height="860"
           alt="Ledgerly’s transaction inbox: 12 transactions auto-categorized, 2 waiting for review">
    </picture>
  </figure>
</section>
```

```css
.hero { display:grid; grid-template-columns: 5fr 7fr; gap: var(--space-16); align-items:center;
        max-width: var(--container-xl); margin-inline:auto; padding: var(--space-24) var(--gutter) var(--space-16); }
.hero h1 { font-family: "Instrument Serif", serif; font-weight:400; font-size: var(--text-display-1);
           line-height:1.02; letter-spacing:-0.02em; text-wrap:balance; }
.lede { font-size: var(--text-lg); color: var(--color-text-muted); max-width: 34rem; margin-top: var(--space-5); }
.actions { display:flex; flex-wrap:wrap; gap: var(--space-5); align-items:center; margin-top: var(--space-8); }
.fine { font-size: var(--text-sm); color: var(--color-text-subtle); margin-top: var(--space-4); }
.hero-shot img { border-radius: var(--radius-lg); box-shadow: 0 0 0 1px oklch(0 0 0 / 0.06), var(--shadow-xl); }
@media (max-width: 64rem) { .hero { grid-template-columns: 1fr; gap: var(--space-10); } }
```

Why each change:
- **The headline names the audience and the benefit** in their own terms; a competitor couldn't use it verbatim. The serif at weight 400 is confident without shouting, which is quieter and more distinctive than weight 800 gradient text.
- **The subhead lists three concrete jobs** and ends with the outcome (minutes, not weekends).
- **Left-aligned copy with the product on the right:** easier to read, and the screenshot does the persuading. Real UI with a descriptive alt text.
- **One primary CTA that says what you get** ("Start free for 30 days"); the secondary is a quiet text link, not a competing button.
- **Fine print answers the first two objections** (cost, compatibility) right where the decision happens. (Ledgerly is fictional. In real work, facts like integrations and bank counts come from the client; if unknown, leave a clearly marked placeholder rather than inventing one.)
- **On phones, a tighter crop** of the inbox replaces the full screenshot (`<picture>`), because a 1280px UI shrunk to 360px is unreadable.
- **Classes, not descendant selectors, for text roles** (`.lede`, `.fine`). A rule like `.hero-copy > p` would also hit the fine print and silently override its size, a specificity trap that shows up only when rendered.
- **The screenshot gets a 1px ring plus a soft large shadow,** so it reads as a crisp object on the page without a heavy drop shadow.
- **The one bold move is the serif headline.** Everything else is restrained, so it lands.
- **Removed:** the gradient background, glow, pill, gradient text, emoji cards, Title Case, and "Learn More".

## 10. Worked example: a dashboard card, redesigned

**Before:**
```
┌───────────────────────────────────────┐   colored icon circle, bold label,
│ (💰)  TOTAL REVENUE                   │   value same size as label,
│       $48210                          │   no comparison, border + shadow + gradient bg,
│       [View Details]  (blue button)   │   a primary button in every card
└───────────────────────────────────────┘
```

**After:**
```
┌───────────────────────────────────────┐
│ Revenue · last 30 days                │   label: 14px, muted, sentence case
│ $48,210                    ╱╲_╱‾      │   value: 30px semibold, tabular, separator
│ ↑ 12.4% vs previous 30 days           │   delta: 14px, success color + arrow (not color alone)
└───────────────────────────────────────┘   1px border only; whole card links to the detail view
```

Why: the value is the content, so it's the biggest thing; the label explains it quietly. The comparison makes the number meaningful (is $48k good?). The sparkline adds trend context at almost no visual cost. The icon circle was decoration, and the button was redundant: making the whole card a link (with hover and focus states) gives the same affordance with less noise. With six of these on a dashboard, removing six blue buttons and six colored circles is the difference between a calm overview and a noisy one.
