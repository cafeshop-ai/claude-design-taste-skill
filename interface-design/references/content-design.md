# Content design: scope, words, and restraint

The most common way generated interfaces go wrong isn't ugliness. It's excess: sections nobody asked for, paragraphs that restate the heading, invented facts, and decoration that competes with the one thing the page is for. This file is about deciding what goes on the page, and then saying it in as few words as do the job.

## Contents
1. Build what was asked
2. Never invent facts
3. Every element earns its place
4. Writing interface text
5. Over-design: decoration that adds noise
6. Calibration: one brief, two answers
7. The final reply

---

## 1. Build what was asked

The request defines the scope. A volunteer sign-up page is a form with the facts volunteers need; it is not the organization's website. A 404 page is a sentence and a way back; it is not a sitemap. A CRM screen shows contacts; it doesn't need a marketing banner.

- **List what the request explicitly asks for, then what the page obviously needs to work** (a submit button, a confirmation, an error state). That's the scope. Everything else is an addition, and additions need a reason the user would agree with.
- **"Obviously needs" is narrow.** It means the page fails without it. A countdown timer, an "Our story" section, a FAQ, a newsletter signup, a testimonial strip, a stats band, or a footer with twelve links are not needed by a page whose job is collecting sign-ups.
- **If you think something extra would genuinely help, offer it in your reply instead of building it.** "I kept this to the sign-up form. If you want, I can add a map and parking details once you have them." The user can say yes in five words; they can't easily un-build a page.
- **Match the page type to the job.** Single-purpose pages (forms, confirmations, auth, 404, coming soon, unsubscribe) should feel single-purpose: one column, one action, nothing competing. Marketing pages have more sections, but each must answer a question a visitor actually has (see `web-design.md`).
- **Don't preselect answers people must give.** Attendance, consent, a plan, a payment method: a preselected choice records answers from everyone who skimmed. Start unselected and validate.
- **Features, too.** Don't add filters, sorting, dark-mode toggles, export buttons, keyboard-shortcut modals, or settings that weren't requested unless the page is unusable without them. Unrequested features are untested surface area and visual noise.

## 2. Never invent facts

Anything presented as true about a real or fictional product, event, or person must come from the user. Inventing it is worse than leaving a gap, because it looks finished and gets shipped.

- **Never invent:** statistics ("10,000+ teams"), ratings ("4.9/5"), testimonials or quotes, customer logos, team members, awards, press mentions, prices, fees, addresses, phone numbers, dates, times, schedules, dress codes, cancellation or refund policies, guarantees and "promises", trust badges ("Certified experts", "Satisfaction guaranteed", "Trusted by…"), what's included in a service, what happens at an event, or legal claims.
- **These slip in as small print.** A line under a button ("Free returns within 30 days"), a trust row under a form, or a fee note under a price are all claims. Check the fine print as carefully as the headline.
- **When a section genuinely needs facts you don't have, prefer leaving it out.** If it's essential to the layout (pricing on a pricing page), use an unmistakable placeholder: `[Price]`, `[Customer quote: name, role, company]`, styled so it can't be mistaken for real copy, and list the placeholders in your reply.
- **Sample data uses fictional people and companies.** Never use real companies' names or logos as customers, clients, or users of the product; it implies relationships that don't exist. The same goes for photos: a stock landscape presented beside an event's details reads as the venue.
- **Sample data in app screens is different:** a project tracker needs realistic tasks to show the design. Make it plausible and internally consistent (counts add up, dates make sense, names are diverse but unremarkable), and don't dress it up as claims about the product.
- **Use exactly the facts you were given, in full.** If the prompt says "Saturday April 12, 9am to noon, meet at the Linden Park gazebo", those details are the page's most important content: make them prominent and correct, and add nothing beside them (no "coffee and donuts provided!", no invented agenda).

## 3. Every element earns its place

Before adding anything, ask what it does for the person using the page. Before shipping, delete everything that doesn't have an answer.

- **The print test:** if the user printed the page, would every block be something they asked for or obviously need? Circle the rest. That's the clutter.
- **One message per section, one primary action per view.** Two equal buttons split attention; a third secondary link usually means a decision wasn't made.
- **Cut the intro that restates the heading.** "Contact us" followed by "Have questions? We'd love to hear from you! Fill out the form below to get in touch" carries no information. The heading and the form are enough.
- **Cut instructions for the obvious.** "Fill out the form below", "Click the button to submit", "Scroll down to learn more."
- **Cut throat-clearing and enthusiasm.** "Welcome to…", "We're so excited…", "We can't wait…", exclamation marks, and emoji. Warmth comes from specific, plain words, not volume.
- **Cut redundant labels and repeated information.** If the date is in the header, don't repeat it in a card, a banner, and the footer.
- **Collapse the long tail.** Secondary information (policies, fine print, rare cases) goes behind a link or a disclosure, not in the main flow.
- **Delete these filler patterns on sight.** They're the most common padding in generated interfaces:
  - *Paired-fragment slogans:* "A little X. A lot of Y.", "Less X. More Y.", "X, made simple.", "Your X, refreshed." At most one per page, and only if it says something specific about this product.
  - *Taglines where content should be:* an eyebrow label above every heading restating it, a slogan under the logo, a line in the footer ("Made with care for people who…"), reassurance under buttons ("No strings attached.").
  - *Cheerleading inside tools:* "You're crushing it!", "Every step counts", "Keep up the momentum". Tools inform; they don't encourage.
  - *Promo cards nobody asked for* inside an app screen: "Upgrade to Business", "Try the new AI assistant", "Need a hand?".
  - *Reassurance without substance:* "We respect your privacy." If the user gave you a privacy policy, link it; otherwise leave the line out.

  The test: delete the sentence. If no information is lost, leave it deleted.
- **Count.** If a single-purpose page has more than about 150 words of copy outside the form, look hard at every sentence.

## 4. Writing interface text

- **Specific beats grand.** "Book a class in two taps" beats "Revolutionize your fitness journey". A specific sentence could only be about this product; a grand one could be about anything.
- **Lead with what the reader needs.** Headings state the point ("3 deploys failed in the last hour"), not the category ("Overview").
- **Buttons are verbs with objects**, saying what happens: "Save draft", "Invite teammate", "Reserve table". Not "Submit", "Continue →" on a final step, or "Get started" when nothing is starting.
- **Labels are nouns, short, sentence case**, above the field: "Email", "Number of people". Helper text only where it prevents a mistake ("We'll send your confirmation here").
- **Confirmation says what happened and what happens next.** "Thanks, Dana. You're signed up for Saturday. We'll email a reminder to dana@example.com the day before." Not "Success!"
- **Errors say what's wrong and how to fix it**, next to the field: "Enter an email so we can send a reminder."
- **Sentence case everywhere.** Title Case On Every Button And Heading reads as shouting and as template.
- **Numbers as numerals; units and context attached.** "3 bedrooms", "$1,240 due in 5 days".
- **Read it aloud.** If it sounds like an ad, rewrite it as a person talking to a person.

## 5. Over-design: decoration that adds noise

Decoration is anything visual that doesn't communicate. Each piece has a small cost; together they bury the content.

- **Background effects:** gradient meshes, glowing blobs, particles, animated gradients, noise overlays, floating 3D shapes, glassmorphism panels. Remove unless they are the product's established brand.
- **Icon inflation:** an icon on every bullet, heading, and button; icons in colored circles; emoji as icons. Use icons only where they speed recognition (navigation, actions, status), from one consistent set.
- **Container inflation:** every section in a card, cards inside cards, borders and shadows on the same element, badges on everything ("New", "Popular", "Beta").
- **Motion inflation:** everything fading up on scroll, hover lifts on non-interactive cards, parallax, looping animations near text. Motion should mark change, not decorate.
- **Typographic inflation:** more than two families, more than 4–6 sizes on a screen, weight 800 for everything important, gradient text.
- **Fake depth:** heavy drop shadows, glossy highlights, bevels. Elevation should mean something (see `layout-and-spacing.md`).

The replacement for decoration is usually nothing: more space, a better typeface, real content, and one deliberate memorable moment (see "Quiet almost everywhere, memorable somewhere" in SKILL.md).

## 6. Calibration: one brief, two answers

**Brief:** "Make a sign-up page for our neighborhood's spring clean-up: Saturday April 12, 9am to noon, meeting at the Linden Park gazebo. Ask for name, email, how many people are coming, and whether they can bring tools."

**The cluttered answer** (what agents often produce): a full-screen hero with a leafy gradient and "Together, we can make a difference! 🌱", a live countdown, a "Why it matters" section with three icon cards and an invented statistic ("Last year we collected 2 tons of trash!"), a schedule with invented times, a "What to bring" list nobody supplied, sponsor logos, an FAQ, a photo gallery of placeholder images, a form with eight fields including "T-shirt size", confetti on submit, and a footer reading "Made with 💚 by volunteers".

Every one of those additions either invents facts (statistics, schedule, what to bring, sponsors) or competes with the form. A neighbor who opens this on their phone has to scroll past five screens to do the one thing they came for.

**The considered answer:**
- One column, max ~32rem, generous space.
- A plain, specific headline ("Spring clean-up at Linden Park") in a typeface with a little character, used once, large.
- The supplied facts directly under it, set clearly: "Saturday, April 12 · 9 am to noon" and "Meet at the Linden Park gazebo".
- The four requested fields: name; email; number of people (a stepper or small number input, default 1); tools (a clear yes/no choice, phrased as a question: "Can you bring tools?").
- One button: "Sign up".
- A confirmation state that repeats what they sent.
- At most one line of welcome, if it fits the voice. No other sections. The reply mentions what was left out and offers to add it ("If you'd like a map, a what-to-bring list, or a contact for questions, send me the details").

The considered answer is shorter, faster on a phone, invents nothing, and feels more personal, because what's there was chosen.

## 7. The final reply

Content discipline applies to your message to the user too.

- **Lead with what you built**, in a sentence or two. Then the decisions they might want to change (direction, anything you deliberately left out), and any placeholders they need to fill.
- **Don't narrate every CSS property** or list features the user can see for themselves.
- **Flag assumptions and gaps** ("I assumed guests can bring up to 4 people; change `max` on the guests field").
- **Offer, don't impose:** extras go in a one-line offer, not in the build.
