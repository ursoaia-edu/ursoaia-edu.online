---
lesson: 13
tags: [project, canva, social media, instagram, story, templates]
summary: Formats and safe zones for social media, how to use Canva properly and how to build a set of reusable templates.
---

# Lesson 13 · Social media post

!!! tip "What you will build"
    A **set of templates** for the computer science club's communications:

    - Square post, vertical post, story and event cover
    - A **brand kit** in Canva, with the colours and fonts of the identity from lesson 12
    - **Safe zones** respected on every format
    - A **series** of three posts recognisable as one family
    - A practical comparison: when to use Canva and when Figma

---

## The formats

Platforms change their specs often, but the ratios stay stable. Remember the **ratios**, not the numbers.

| Format | Ratio | Recommended size | Where |
|--------|-------|------------------|-------|
| **Square** | 1:1 | 1080 × 1080 px | Instagram and Facebook feeds |
| **Vertical** | 4:5 | 1080 × 1350 px | Instagram feed — takes the most screen |
| **Story / Reels** | 9:16 | 1080 × 1920 px | Instagram stories, TikTok, YouTube Shorts |
| **Landscape** | 16:9 | 1920 × 1080 px | YouTube, presentations, corridor screens |
| **Event cover** | 1.91:1 | 1920 × 1005 px | Facebook events |

!!! tip "The 4:5 vertical is the default feed format"
    At the same screen width, a 4:5 post takes 25% more height than a square one. More space = more viewing time. If you have a choice, make it 1080 × 1350.

### Safe zones

The app's interface covers parts of the image. Do not put anything important there.

**Story (1080 × 1920):**

```
┌──────────────────┐  ← 250 px: avatar, name, time
│ ~~~~~~~~~~~~~~~~ │
├──────────────────┤
│                  │
│    SAFE ZONE     │  ← 1420 usable px
│   1080 × 1420    │
│                  │
├──────────────────┤
│ ~~~~~~~~~~~~~~~~ │  ← 250 px: reply bar, buttons
└──────────────────┘
```

**Vertical post (1080 × 1350):** in the profile grid it appears **cropped to a square**, centred. So the essential elements must fit inside the central 1080 × 1080 area.

!!! warning "The profile grid test"
    Place a semi-transparent 1080 × 1080 rectangle centred over your vertical post. Whatever falls outside it **is not visible** in the profile grid. If the title is cut off, move it.

---

## Canva: how to use it properly

Canva is fast, but easy to use badly. Three rules.

### Rule 1 — Set up the brand kit first

**Brand Hub → Brand Kit** (available on the free plan too, with limitations):

1. **Colours:** add the palette from lesson 03. With Canva for Education you can save complete palettes.
2. **Fonts:** set the heading and body fonts from lesson 04.
3. **Logo:** upload the SVG variants from lesson 12.

The result: on every new element, your colours and fonts appear first in the list. You no longer pick "roughly orange".

!!! note "If you have no Brand Kit access"
    On the free plan without Education, keep a list of the 5 HEX codes in a text file and paste them by hand. In Canva's colour picker there is a HEX field and a "Recently used colours" section.

### Rule 2 — A template is structure, not a result

When you start from a Canva template:

| What you keep | What you **must** change |
|---------------|--------------------------|
| The composition structure | All colours → your palette |
| The size hierarchy | All fonts → your fonts |
| The block positions | All images → your own |
| — | Generic decorative elements → removed or replaced |

!!! warning "Pro elements with a crown"
    Always filter by **Free** before picking an element. Otherwise the export will ask for payment or carry a watermark. The filter is at the top of the Elements panel.

### Rule 3 — Check what you imported

Canva does not tell you whether your text has enough contrast or whether the image resolution is too low. The checks from lessons 03 and 10 still apply — you just have to run them manually.

---

## Canva vs. Figma

| Situation | The tool |
|-----------|----------|
| You need a post in 10 minutes | **Canva** |
| You are making a coherent set of 20 posts | **Figma** (components + variants) |
| You need ready-made shapes and illustrations | **Canva** |
| You are building the visual identity | **Figma** |
| You work with someone who does not know Figma | **Canva** |
| You need simple animation | **Canva** (it has a video timeline) |
| You need exact pixel control | **Figma** |
| You are making an interactive prototype | **Figma** |

!!! tip "The hybrid workflow, the most practical one"
    Build the **templates** in Figma, as components with text properties and image slots. Export the examples into Canva as brand templates, for the classmates who post every week.

    That way control stays with you, and anyone can produce a correct post in 5 minutes.

---

## The anatomy of a post that works

A feed post has about 1.5 seconds to stop a thumb on the screen.

### The five elements

| Element | Role | How much space |
|---------|------|----------------|
| **The visual hook** | Stops the scroll: a strong image, high contrast, an unexpected colour | The whole surface, or the top third |
| **The title** | Says what it is about in at most 6 words | 20–30% of the height |
| **The information** | The date, the place, the key number | 10–15% |
| **The mark** | The logo or the brand colour | 5% |
| **The call to action** | "Link in bio", "Come on Saturday", "Details in the comments" | 5% |

!!! note "Long text goes in the caption, not in the image"
    The image has to stop the scroll. The explanation belongs in the post text, where it is searchable, copyable and accessible to screen readers.

    The rule: **at most 15 words on the image**.

### Legibility on a phone

A 1080 px post displays on a phone at roughly 400 px wide. That is a **2.7× reduction**.

| Size in the file (1080 px) | How it appears on a phone |
|----------------------------|---------------------------|
| 24 px | ~9 px — illegible |
| 40 px | ~15 px — the absolute minimum |
| 60 px | ~22 px — comfortable for details |
| 90 px | ~33 px — good for information |
| 140 px+ | ~52 px — a title |

!!! warning "The mandatory test"
    Before publishing, **send the image to your phone** and look at it in the feed, not zoomed in. Half the design problems in posts disappear if you run this test.

---

## The series: how you build coherence

A single post does not build an identity. A **series** of recognisable posts does.

### What repeats

| Element | How strictly |
|---------|--------------|
| The palette | Identical, always |
| The fonts | Identical, always |
| The logo position | Same corner, same size |
| The composition structure | Same grid, same margins |
| The accent element | Same bar / shape / treatment |

### What varies

| Element | Why |
|---------|-----|
| The image | Otherwise every post looks identical |
| The title | Obviously |
| The accent colour, from a set of 3 | It distinguishes categories: `event`, `project`, `news` |

!!! tip "The colour category system"
    If event posts are orange, project posts blue and announcements green, anyone following the page learns the code within two weeks and can tell from the grid what each post is without opening it.

    **The condition:** all three colours must pass the contrast test with white text.

---

## Exercises

### Exercise 1 — Safe zones
Build a 1080 × 1920 story and mark the areas covered by the interface with semi-transparent rectangles. Then place the content so nothing important falls outside the safe zone.

??? success "Solution"
    **The build:**
    1. A 1080 × 1920 frame.
    2. A 1080 × 250 rectangle at the top, red fill at 20% — the top interface zone.
    3. A 1080 × 250 rectangle at the bottom, red fill at 20% — the bottom interface zone.
    4. Group and lock them (++ctrl+shift+l++). Rename the group `safe-zones — do not export`.
    5. Hide the group before exporting.

    **Placing the content:**
    - Logo: Y = 300 (just below the top zone).
    - Title: vertically centred in the safe zone, Y ≈ 800.
    - Information: below the title.
    - Call to action: Y ≈ 1550, i.e. 120 px above the bottom zone.

    **The common mistake:** putting the call to action at 1850, because "that's the bottom". It will be completely covered by the reply bar. Nobody will see it.

### Exercise 2 — The profile grid test
Take a 1080 × 1350 vertical post and check what is visible in the profile grid. Fix it if needed.

??? success "Solution"
    **The check:**
    1. Over the 1080 × 1350 post, place a 1080 × 1080 rectangle centred vertically (Y = 135).
    2. Everything falling outside it, top and bottom, disappears from the grid.

    **What is usually lost:** a logo placed very high and a call to action placed very low.

    **The fix:**
    - Move the logo to Y ≥ 180 (instead of 60).
    - Move the call to action to Y ≤ 1120 (instead of 1270).
    - Or: accept their loss and make sure the **title and image** — the only things that matter in the grid — are entirely inside the central area.

    **The right decision depends on the purpose:** if the post is for the feed (where it is seen whole), the central area matters less. If it is meant to build the look of the profile grid, it matters enormously.

### Exercise 3 — Three posts from one series
Build three square posts that are instantly recognisable as one family, but communicate different things: an event, a project, an announcement.

??? success "Solution"
    **The common structure (identical in all three):**
    - 1080 × 1080, background `#0F172A`, 80 px margins.
    - The club logo, 64 px, top-left corner, 80 px from the edges.
    - An 8 × 160 px accent bar under the title.
    - The category label, top right, all caps, 24 px, tracking +12%.
    - The title, Inter Bold, 88 px, white, left-aligned, at most 3 lines.
    - The information, Inter Regular, 32 px, `#CBD5E1`.

    **What varies:**

    | Post | Label | Accent colour | Content |
    |------|-------|---------------|---------|
    | Event | `EVENT` | `#F97316` orange | `PROJECT FAIR` + the date |
    | Project | `PROJECT` | `#38BDF8` blue | `ESP32 ROBOT` + a photo in the bottom third |
    | Announcement | `NEWS` | `#4ADE80` green | `SIGN-UPS OPEN` + the deadline |

    **Contrast checks on the `#0F172A` background:**
    - `#F97316` → 5.9:1 — passes AA
    - `#38BDF8` → 8.4:1 — passes AAA
    - `#4ADE80` → 11.2:1 — passes AAA

    **The coherence test:** place the three side by side at 200 px wide (as they appear in the profile grid). It must be instantly obvious that they are one family, while the categories remain distinguishable. If they look identical, you varied too little. If they do not look related, you varied too much.

---

## Mini-project: a complete communications kit

Build a set of **four templates** in Figma (square post, vertical post, story, event cover), turn them into components with properties, and replicate them as templates in Canva.

??? success "Deliverables and criteria"
    **In Figma — the components:**

    | Component | Properties | Slots |
    |-----------|------------|-------|
    | `social/post-square` | Category (variant: event/project/news), Title (text), Info (text) | Image |
    | `social/post-vertical` | the same | Image |
    | `social/story` | the same + CTA (text) | Image |
    | `social/event-cover` | Title, Date | Image |

    All four use the **same styles** for colour and text. Changing one style updates every template.

    **In Canva — the templates:**
    1. Create one design per format.
    2. Apply the Brand Kit palette and fonts.
    3. Save each as a **brand template** (Share → Template link), so classmates can reuse it without breaking the original.

    **The evaluation criteria:**

    | # | Criterion | Check |
    |---|-----------|-------|
    | 1 | Safe zones respected | Overlay the test rectangles |
    | 2 | At most 15 words on the image | Count them |
    | 3 | Text legible on a phone | Send yourself the image and look at it in the feed |
    | 4 | Contrast ≥ 4.5:1 | The Contrast plugin on every accent colour |
    | 5 | Logo present and legible | At least 48 px at 1080 |
    | 6 | The series is recognisable | The 4 formats side by side |
    | 7 | Changing one style updates everything | The test from lesson 08 |
    | 8 | The Canva templates are shareable | Open the link in a browser where you are not logged in |

    **The final, practical test:** ask a classmate who did not work on the project to make a post for a real event using your Canva template. Time them. If it takes more than 10 minutes, or if the result no longer looks like your series, the template is too complicated or too permissive — simplify it.

---

## Summary

- Remember the **ratios**, not the numbers: 1:1, 4:5, 9:16, 16:9.
- **4:5 (1080 × 1350)** is the default feed format — it takes the most screen.
- **Safe zones:** 250 px top and bottom on stories; the central 1080 × 1080 area on vertical posts.
- In Canva, set up the **Brand Kit first**; a template is structure, not a result.
- Filter by **Free** to avoid watermarked Pro elements.
- Figma for systems and control, Canva for speed; the hybrid workflow combines them.
- **At most 15 words** on the image — the rest goes in the caption.
- A 1080 px post displays at ~400 px on a phone: at least **40 px** for any text.
- The **series** builds the identity: repeat the palette, fonts and structure; vary the image and title.
- A colour code by category is learned by followers within two weeks.

---

**Next step:** [→ Lesson 14: Web interface design](14-design-interfata-web.md)
