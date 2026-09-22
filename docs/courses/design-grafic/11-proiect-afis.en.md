---
lesson: 11
tags: [project, poster, print, a3, composition]
summary: A complete project — an A3 poster for a school event, from the brief to a PDF ready for the print shop.
---

# Lesson 11 · Poster for a school event

!!! tip "What you will build"
    A **complete A3 poster**, starting from the brief and ending with a print-ready PDF:

    - A completed brief and ranked content
    - Two different visual directions, for feedback
    - The final version, with a coherent grid, palette and typography
    - Contrast, margin and resolution checks
    - A PDF export with bleed, plus a digital version for screens

---

## Step 1 — The brief

We use the brief from lesson 00. Here it is, filled in for our project:

| Question | Answer |
|----------|--------|
| **What** | A3 portrait poster, colour print, 15 copies |
| **For whom** | Students in grades 5–12 walking the corridors during breaks |
| **Message** | "On Saturday you can see the projects your classmates built." |
| **Action** | Come on Saturday, 12 April, between 10:00 and 14:00, to the sports hall |
| **Where** | Three corridors, at eye level, next to the stairs |
| **Constraints** | School logo mandatory, no photos of students, ready in 7 days |

!!! note "Reading distance changes everything"
    A corridor poster is read from **2–4 metres**. At A3 (29.7 × 42 cm) that means:

    - The title must be readable from 4 m → at least **90 pt**
    - The main information (the date) from 3 m → at least **50 pt**
    - The details from 1 m → at least **16 pt**

    The rule of thumb: **1 cm of letter height ≈ 3 metres of reading distance**.

---

## Step 2 — Ranked content

Write all the text before you draw anything. Then number it.

```
1. PROJECT FAIR
2. Saturday, 12 April · 10:00 – 14:00
3. Sports hall, floor 1
4. Robots, sensors, games and websites built
   by the computer science club students.
5. Free entry
6. Ursoaia computer science club · ursoaia-edu.online
```

**The grouping:** `[1]`, `[2 + 3]`, `[4]`, `[5 + 6]` → four groups. Exactly within the 3–5 range from lesson 05.

!!! warning "Cut the text before it goes on the poster"
    The first version of point 4 read: "Come and discover the fascinating projects created by your classmates throughout the entire school year, in an event that promises to be memorable." 24 words, zero information.

    The final version: "Robots, sensors, games and websites built by the computer science club students." 11 words, four concrete nouns. A poster is not a text, it is a list of facts.

---

## Step 3 — Setting up the file

1. New frame: ++f++ → the **Paper** category → **A3**. You get 842 × 1191 pt (Figma points = 1/72 inch; A3 = 29.7 × 42 cm).
2. Rename it `poster-project-fair`.
3. **Grid:** Layout grid → Columns → Count **6**, Type `Stretch`, Margin **60**, Gutter **24**.
4. **Second grid:** Rows → Count `Auto`, Height **24** — the baseline grid.
5. **The safe margin:** draw a rectangle 60 pt from every edge, no fill, 1 pt red stroke. Lock it (++ctrl+shift+l++). Nothing important goes outside it.

!!! note "Why 6 columns and not 12"
    A poster has far fewer elements than a web page. 6 columns give enough flexibility (1/2, 1/3, 2/3) without tempting you to fragment the content.

### The styles

Import or recreate the styles from lessons 03 and 04. For this poster:

| Style | Value |
|-------|-------|
| `surface/base` | `#0F172A` |
| `brand/primary` | `#F97316` |
| `text/strong` | `#F8FAFC` |
| `text/base` | `#CBD5E1` |
| `text/muted` | `#64748B` |
| `poster/title` | Inter Bold, 104 pt, line height 1.05, tracking −2% |
| `poster/date` | Inter Semi Bold, 52 pt, line height 1.2 |
| `poster/body` | Inter Regular, 26 pt, line height 1.4 |
| `poster/label` | Inter Medium, 18 pt, all caps, tracking +12% |
| `poster/detail` | Inter Regular, 16 pt, line height 1.4 |

---

## Step 4 — Two directions

The rule from lesson 00: **never show a single version**. Build two, visibly different.

### Direction A — typographic

No images. The title takes the top third, over three lines. Below it, an orange 8 × 240 pt bar. The large date under the bar. The description on columns 1–4. The details at the bottom, on a single line.

**Strength:** impossible to miss, readable from 5 metres, prints perfectly even in black and white.
**Weakness:** it says nothing about *what kind* of event this is.

### Direction B — with an image

A photo of a project (an ESP32 board with LEDs lit, macro) takes the top third, bleeding to the frame edges. A gradient from opaque at the bottom to transparent at the top. The title over the gradient. The rest of the content on a flat background underneath.

**Strength:** immediately says what this is about; catches the eye from a distance.
**Weakness:** depends on photo quality; it is lost in black and white printing.

!!! tip "How to ask for feedback on the two directions"
    Do not ask "which do you like". Ask:

    - "Look at each for 3 seconds. What did you take in from each?"
    - "Which would make you more likely to come?"
    - "From which did you work out faster what kind of event this is?"

---

## Step 5 — Building the final version

Assume the feedback picked direction B. The build, element by element.

### 5.1 — The background

1. A rectangle over the whole frame, Fill `surface/base`. Rename it `bg`.

### 5.2 — The photo

1. A 842 × 480 pt rectangle, flush with the top edge (X: 0, Y: 0).
2. Fill → `Image` → pick the photo. Mode **Fill**.
3. Double-click and reposition it so the main subject sits in the right half (the title will sit on the left).

!!! warning "Check the resolution now, not at the end"
    The poster is 29.7 cm wide. At 300 DPI: 29.7 / 2.54 × 300 = **3508 px**. Your photo must be **at least 3508 px wide** if it spans the full width.

    If it is 1800 px, either use it across half the width or find another one. Check in the right panel: Fill → click the image → Figma shows the original dimensions.

### 5.3 — The gradient

1. A 842 × 480 pt rectangle, exactly over the photo.
2. Fill → `Linear gradient`.
3. The bottom stop: `#0F172A`, opacity **100%**. The top stop: `#0F172A`, opacity **0%**.
4. Drag the gradient handle vertically, bottom to top.

### 5.4 — The title

1. Text over three lines: `PROJECT / FAIR / 2026`.
2. Style `poster/title`, colour `text/strong`.
3. Positioned on columns 1–4, with the baseline of the last line about 60 pt below the photo's bottom edge.

!!! note "Why the title overlaps the photo"
    The overlap ties the two zones together. If the title sat entirely below the photo, the poster would split into two independent horizontal bands. An overlap of ~80 pt creates continuity.

### 5.5 — The accent bar

An 8 × 200 pt rectangle, Fill `brand/primary`, 40 pt below the title, left-aligned with it.

### 5.6 — Date and place

1. `Saturday, 12 April` — style `poster/date`, colour `brand/primary`.
2. `10:00 – 14:00 · Sports hall, floor 1` — style `poster/body`, colour `text/base`, 12 pt below the date.

The two form a group: 12 pt of space between them, 48 pt from the bar above.

### 5.7 — The description

Text on columns 1–4 (not all 6 — line length!), style `poster/body`, colour `text/base`, 48 pt below the date group.

Check: **at most 66 characters per line**. At 26 pt, that means a width of roughly 460 pt.

### 5.8 — The bottom zone

A horizontal Auto Layout, gap `Auto`, width `Fill`, anchored 60 pt from the bottom edge:

- Left: the school logo (SVG, 48 pt tall) + the text `Ursoaia computer science club`, style `poster/detail`.
- Right: `Free entry` (style `poster/label`, colour `brand/primary`) + `ursoaia-edu.online` (style `poster/detail`, colour `text/muted`).

Above the zone, a 1 pt separating line, colour `#1E293B`.

---

## Step 6 — The checks

Go through the list before exporting. Every point comes from an earlier lesson.

| # | Check | How | Lesson |
|---|-------|-----|--------|
| 1 | The blur test | Layer blur 20 on a copy — is the title the dominant blob? | 02 |
| 2 | The 3-second test | Show it to 3 classmates, ask what they remember | 00 |
| 3 | Title contrast | Contrast plugin, on the lightest point under the text | 03 |
| 4 | Detail contrast | `text/muted` on `surface/base` ≥ 4.5:1 | 03 |
| 5 | Margins | Nothing important closer than 60 pt to the edge | 02 |
| 6 | Line length | Description ≤ 66 characters / line | 04 |
| 7 | Alignment | Every element starts on a grid column | 05 |
| 8 | Spacing | All values are multiples of 8 (or 12 pt) | 05 |
| 9 | Photo resolution | ≥ 3508 px across the displayed width | 10 |
| 10 | The black and white test | Saturation −100 — does it still read? | 03 |

!!! warning "Test 10 is not optional here"
    The brief says colour print, but posters get photocopied. If at −100 saturation the date becomes invisible (because it was orange on a dark background and both turn a similar grey), change it: make the date white and keep only the orange bar as the accent.

---

## Step 7 — Exporting

### For print

1. **Bleed.** If the print shop asks for 3 mm bleed: enlarge the frame by 3 mm on each side. 3 mm = 8.5 pt, so the frame becomes **859 × 1208 pt**. Extend `bg` and the photo to the new edges. The content stays where it is.
2. Select the frame → Export → **PDF** → Export.
3. Open the PDF and check: the fonts render correctly, the image is not pixelated at 100% zoom.

!!! note "If the print shop does not ask for bleed"
    Many copy shops print straight onto A3 with no trimming. Then you do not need bleed, but **the background must reach the exact edge** and you have to know the printer may leave a white band of 3–5 mm. Ask beforehand.

### For screens

Many schools have corridor screens or social media accounts.

| Version | Format | Size | Note |
|---------|--------|------|------|
| Corridor screen (landscape) | PNG 2× | 1920 × 1080 | Recompose: the vertical poster does not fit |
| Instagram post | JPG | 1080 × 1080 | Recompose to square |
| Instagram story | JPG | 1080 × 1920 | Almost the same ratio as A3 — the easiest adaptation |

!!! warning "Do not stretch the A3 poster into another format"
    The A3 ratio is 1:1.41. An Instagram post is 1:1. If you scale non-proportionally, the typography distorts and it shows immediately.

    **Make a new frame** for each format and reuse the elements. With styles and components, that takes 10 minutes, not an hour.

---

## Common poster mistakes

| Mistake | Why it is a problem | The fix |
|---------|---------------------|---------|
| Too much text | Nobody reads a poster like a book | At most 6 blocks, at most 40 words total |
| Title too small | Not readable at the actual distance | 1 cm of letter ≈ 3 m of distance |
| Text glued to the edge | It gets trimmed in print | At least 10 mm, ideally 15–20 mm on A3 |
| Low-resolution photo | Pixelated in print | Check before you start, not at the end |
| Five colours | The eye does not know where to go | One primary, one accent, the rest neutral |
| The date smaller than a decorative title | The vital information is lost | The date is secondary, but never tertiary |
| A decorative font throughout | Tiring, illegible from a distance | Decorative font **only** on the title |
| No contact information | Nobody can find out more | At least a website or a room |

---

## Exercises

### Exercise 1 — Cut the text
Take the following brief text and reduce it to at most 40 words total, keeping all the essential information:

> "The computer science club of our school has the great pleasure of inviting you to the Project Fair, a special event that will take place on Saturday, 12 April, starting at 10:00 and running until 14:00, in the sports hall located on the first floor of the main building, where you will be able to admire a wide range of projects created by our talented students throughout the entire school year, including robots, sensors, games and websites. Entry is completely free for everyone."

??? success "Solution"
    83 words → 30 words:

    ```
    PROJECT FAIR

    Saturday, 12 April · 10:00 – 14:00
    Sports hall, floor 1

    Robots, sensors, games and websites built
    by the computer science club students.

    Free entry
    Ursoaia computer science club · ursoaia-edu.online
    ```

    **What was cut and why:**
    - "has the great pleasure of inviting you" → politeness that takes space; the poster *is* the invitation.
    - "a special event that will take place" → redundant, the date already says so.
    - "located on the first floor of the main building" → "floor 1" is enough inside a school.
    - "a wide range of projects created by our talented students throughout the entire school year" → replaced with the four concrete nouns. Concrete things convince, adjectives do not.
    - "completely free for everyone" → "free".

    **Check:** read the short version out loud. Is any information missing that someone would need in order to come? No.

### Exercise 2 — Fix a poster
Deliberately build an A3 poster with five mistakes from the table above, then make the corrected version. Note each fix.

??? success "Solution"
    An example of the flawed poster and its fixes:

    | Mistake introduced | The effect | The fix |
    |--------------------|-----------|---------|
    | Title at 40 pt | Illegible from 3 m (40 pt ≈ 1.4 cm ≈ 4 m in theory, but with a thin font it disappears) | 104 pt Bold |
    | Text 15 pt from the edge | Trimming risk | 60 pt (≈ 21 mm) |
    | 4 accent colours | No colour hierarchy | Only `brand/primary` |
    | Description across the full width (842 pt) | ~120 characters / line | On 4 columns, ~460 pt |
    | Title centred over 3 lines | Ragged left edge | Left-aligned |

    After the fixes, run the blur test on both versions. The difference must be obvious: in the flawed version the blobs are all the same intensity; in the correct one the title clearly dominates.

### Exercise 3 — Adapting to three formats
Take the final poster and adapt it to: an Instagram post (1080 × 1080), a story (1080 × 1920) and a landscape screen (1920 × 1080). Do not scale — recompose.

??? success "Solution"
    | Format | What changes |
    |--------|--------------|
    | **Story 1080 × 1920** | Ratio 1:1.78 vs. A3's 1:1.41. The photo grows proportionally more, the text stays the same. The easiest adaptation: increase the photo area to 45% of the height and keep the rest structurally identical. |
    | **Post 1080 × 1080** | Square — the vertical structure does not fit. Solution: photo on the top half, content on the bottom half; **drop** the description (it goes in the post caption). Title, date, place and logo remain. |
    | **Screen 1920 × 1080** | Landscape — invert the structure: photo across 45% of the width on the right, all the text left-aligned on the other 55%. The title can drop to 72 pt, because the screen is viewed from 3–5 m but emits its own light. |

    **What stays identical in all four:** the palette, the font, the ratio between hierarchy levels, the orange accent bar, the logo position.

    **This is the test of a real visual identity:** four completely different formats, instantly recognised as the same event. Exactly what you will build systematically in lesson 12.

---

## Mini-project: your poster

Pick a **real** event at your school and go through all seven steps: brief, ranked content, file setup, two directions, final version, the 10 checks, PDF export + a digital version.

??? success "The evaluation criteria"
    A successful poster passes all nine points:

    | # | Criterion | How to check |
    |---|-----------|--------------|
    | 1 | A complete, written brief | All 6 questions answered |
    | 2 | At most 40 words | Count them |
    | 3 | 3–5 visual groups | The blur test |
    | 4 | A clear hierarchy | 3 people × 3 seconds give the same answer |
    | 5 | Title readable from 3 m | Print it and walk 3 metres back |
    | 6 | Contrast ≥ 4.5:1 everywhere | The Contrast plugin |
    | 7 | Margins ≥ 15 mm | The safety rectangle |
    | 8 | One primary + one accent | Count the colours |
    | 9 | A PDF that opens correctly | Open it on another computer |

    **The deliverables:**
    - `poster-<event>.pdf` — for print
    - `poster-<event>-story.jpg` — 1080 × 1920
    - The Figma file with **both directions** kept (do not delete the unselected one — it is the evidence of your process)

    **A real bonus:** print it and actually put it up in the corridor. Then ask three classmates who know nothing about the event what they understood. That is the only test that truly counts.

---

## Summary

- You start with the **brief**, not with Figma.
- **1 cm of letter height ≈ 3 metres** of reading distance.
- At most **40 words** and **6 blocks** on a poster.
- Cut the politeness and the adjectives; keep the **concrete nouns**.
- Build **two visibly different directions** before asking for feedback.
- A **6-column** grid for posters, a minimum **60 pt** margin on A3.
- Overlapping the title onto the photo **ties** the zones together; without it, the poster splits into bands.
- Check the **photo resolution at the start**: A3 at 300 DPI = 3508 px wide.
- The **10 checks** before exporting, including the black and white test.
- Adapting to another format means **recomposing**, not scaling.

---

**Next step:** [→ Lesson 12: Logo and visual identity](12-proiect-logo.md)
