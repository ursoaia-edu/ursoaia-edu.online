---
lesson: 12
tags: [project, logo, visual identity, branding, svg]
summary: A complete project — from concept to vector logo, with variants, a monochrome version, clear space and usage rules.
---

# Lesson 12 · Logo and visual identity

!!! tip "What you will build"
    A **complete logo**, with everything that means in practice:

    - A concept that starts from a brief, not from inspiration
    - Three sketched directions, one developed
    - A vector construction on a grid
    - **Variants:** primary, horizontal, mark, monochrome, reversed
    - **Clear space** and minimum size
    - A page of **usage rules**

---

## What a logo is (and is not)

A logo does **not** explain what the organisation does. It is not an illustration, not a story, and it does not have to contain a brilliant metaphor.

A logo is an **identification mark**: something you recognise quickly, at any size, in any context. A transport company's logo does not need to contain a truck; it only needs to be recognised as belonging to that company.

!!! note "The recognition test"
    Think of three logos you recognise instantly. Almost certainly they are **simple**: one shape, one or two colours, sometimes just letters. Complexity does not help recognition, it hinders it.

### The types of logo

| Type | What it contains | Example structure |
|------|------------------|-------------------|
| **Wordmark** | Just the name, carefully drawn | The full name, custom typography |
| **Lettermark** | Just the initials | "CS" for Computer Science club |
| **Mark** | An abstract or figurative symbol | A geometric sign |
| **Combination** | Mark + text, usable together or apart | The most practical |
| **Emblem** | Text enclosed in a shape (a badge) | Hard to use at small sizes |

!!! tip "For a school club, pick the combination"
    You need flexibility: the mark alone for an avatar and a favicon, the combination for posters and the site header. An emblem looks good on a t-shirt and bad on everything else.

---

## The five criteria of a good logo

| Criterion | The check question |
|-----------|--------------------|
| **Simple** | Can you draw it from memory after seeing it twice? |
| **Memorable** | Can you tell it apart from others in the same field? |
| **Timeless** | Will it look good in 10 years, or is it tied to a fashion? |
| **Versatile** | Does it work at 16 px and at 2 metres, in colour and in black and white? |
| **Appropriate** | Does the tone match the organisation? |

!!! warning "Patterns that age badly"
    3D shadows, complex gradients, "glossy" reflections, trendy fonts, lighting effects. All of these date a logo to the year it was made.

    A logo drawn flat, from simple geometric shapes, looked good in 1970 and looks good now.

---

## Step 1 — The identity brief

Before any sketch, answer in writing:

1. **Who are we?** — one sentence.
2. **For whom?** — the real audience.
3. **Three words** describing the tone you want.
4. **Three words** describing what you do **not** want to look like.
5. **Where will the logo appear?** — list every concrete place.
6. **What similar logos exist?** — so you do not resemble them.

!!! note "A completed brief — the computer science club"
    1. **Who:** a club of students who build electronics and programming projects.
    2. **For whom:** middle and high school students, plus parents and teachers.
    3. **Tone wanted:** technical, approachable, practical.
    4. **Tone unwanted:** corporate, childish, elitist.
    5. **Where:** Instagram avatar (round, 110 px), favicon (32 px), site header, A3 posters, t-shirts, stickers, presentations.
    6. **Similar:** most clubs use a cog or a chip with pins. We avoid both.

---

## Step 2 — Sketches

**On paper, not in Figma.** A pencil draws ten times faster than a mouse, and at this stage quantity matters more than quality.

The rule: **20 small sketches** (4 × 4 cm each), in 30 minutes. Do not evaluate while drawing. Only at the end do you pick three.

### Starting ideas for the computer science club

| Direction | Concept | Risk |
|-----------|---------|------|
| Geometric lettermark | `CS` built from straight segments, like traces on a printed circuit board | May resemble other initials |
| Network node | Three or four points connected by lines, suggesting connection | Very widely used |
| The "less than" sign | A stylised `</>`, the universal sign of code | Too literal |
| Modular shape | A square made of 4 modules that can be rearranged | Abstract, but distinctive |

!!! tip "How to recognise a good sketch"
    Cover it with your thumb. If the remaining silhouette is still distinct, it is a good direction. If it becomes a shapeless blob, it is not.

---

## Step 3 — The vector construction

Pick a direction and build it properly, in Figma.

### The construction grid

1. A **240 × 240 px** frame, named `logo/construction`.
2. Layout grid: `Grid`, size **24** — so 10 × 10 modules.
3. A second layout grid: `Grid`, size **8**, in a more discreet colour — for fine detail.

Draw using **only** coordinates that land on the grid. A logo built on a grid looks deliberate; one drawn by eye looks approximate.

### The construction rules

| Rule | Why |
|------|-----|
| Identical line weights | A logo with 8 px and 9 px lines looks careless |
| Angles from the 0° / 45° / 90° set | Arbitrary angles look accidental |
| Identical corner radii | The same radius everywhere, or zero |
| Whole-number coordinates | Half-pixels give blurry edges |
| Symmetry where possible | The eye detects it and reads it as order |

!!! warning "Optical correction"
    A circle and a square of the same height **do not look** the same size — the circle looks smaller. The rule: round shapes are drawn 2–4% larger than straight ones so they appear equal.

    Likewise, a triangle pointing up looks taller than a square of the same height. The eye is right, the ruler is not.

### Typography inside the logo

If the logo contains text:

1. Pick a font that matches the tone (lesson 04).
2. Adjust the spacing between letters **by hand**. A logo never uses default kerning.
3. At the end, **convert the text to vector**: right-click → **Outline stroke** for strokes, or **Flatten** (++ctrl+e++) for text.

!!! warning "Why logo text gets converted to shapes"
    If the logo stays as text, anyone who opens the file without that font will see something else. A logo converted to vector looks identical on any computer, in any program.

    **Keep two files:** one with editable text (for the future) and one converted (for delivery).

---

## Step 4 — The variants

A logo is not a file. It is a **set**.

| Variant | When it is used | File |
|---------|-----------------|------|
| **Primary** (vertical) | Posters, presentations, square spaces | `logo-primary.svg` |
| **Horizontal** | Site header, signatures, wide banners | `logo-horizontal.svg` |
| **Mark** | Avatar, favicon, small stickers | `logo-mark.svg` |
| **Monochrome (black)** | Faxes, stamps, black and white printing | `logo-black.svg` |
| **Monochrome (white)** | On dark backgrounds or photos | `logo-white.svg` |

!!! note "The horizontal variant is not the primary one stretched"
    Going from vertical to horizontal means **recomposing**: the mark moves to the left of the text, the relative size is adjusted, the spacing is recalculated. You do not scale non-proportionally.

### The reduction test

Put the mark variant at **16 px**. What happens?

- If the details melt into a blob → simplify. Remove the small elements.
- If the interior gaps close up → enlarge them or thin the lines.
- If it is still recognisable → the logo passes.

!!! tip "Make a simplified version for small sizes"
    Many professional logos have a "compact" variant with fewer details, used below 32 px. That is not a defeat, it is normal practice.

---

## Step 5 — Clear space and minimum size

### Clear space

The minimum empty space around the logo, which nothing may enter — no text, no other logos, not the page edge.

**It is defined relatively**, not in millimetres, so it works at any size:

> Clear space = **the height of the letter "C" in the logo**, on all four sides.

Or, for a logo with no text: half the width of the mark.

### Minimum size

The smallest size at which the logo is still legible. It is established **by testing**, not by calculation:

| Variant | Typical minimum (screen) | Typical minimum (print) |
|---------|--------------------------|-------------------------|
| Primary | 120 px wide | 30 mm wide |
| Horizontal | 160 px wide | 40 mm wide |
| Mark | 24 px | 8 mm |

Print them at these sizes and look at them. If something is lost, raise the minimum.

---

## Step 6 — The usage rules

One page, with visual examples. This is the document that makes the difference between a logo and a visual identity.

### What it contains

1. **The variants** — all five, with their file names.
2. **Clear space** — drawn, with the measuring unit marked.
3. **Minimum sizes** — for each variant.
4. **The colours** — HEX, RGB, and the CMYK equivalent if it goes to print.
5. **Which backgrounds** — examples: on white, on the brand colour, on a photo, on black.
6. **What not to do** — the most useful chapter.

### The "what not to do" list

Draw each mistake, with a red X over it:

- Do not stretch it non-proportionally
- Do not rotate it
- Do not change the colours
- Do not add shadows or effects
- Do not rearrange the elements
- Do not place it on backgrounds with insufficient contrast
- Do not put it in a box that is not part of the logo
- Do not change the font

!!! note "Why the negative chapter is the most useful"
    The people who will use the logo (teachers, classmates, the print shop) will not read the theory. They will look at the images with the red X and understand in 5 seconds. Put your effort there.

---

## Exercises

### Exercise 1 — 20 sketches
On paper, in 30 minutes, draw 20 logo sketches for the computer science club. Do not evaluate while drawing. At the end, pick three and justify each choice in one sentence.

??? success "Solution"
    There is no correct answer, but the process has clear indicators:

    - **If you made fewer than 12 sketches**, you were evaluating while drawing. Next time set a 90-second timer per sketch.
    - **If all 20 look alike**, you got stuck on one idea. Force yourself: make 5 from letters only, 5 from geometric shapes only, 5 abstract, 5 figurative.
    - **If you like none of them at the end**, that is normal. Pick the three with the most distinct silhouette, not the "prettiest" — beauty comes with refinement, silhouette does not.

    **Good justifications sound like:** "This one stays recognisable when I cover half of it." "This one does not look like any cog." "This one can be drawn with 4 lines — it will work at 16 px."

    **Weak justifications:** "I like this one." "This one looks professional."

### Exercise 2 — Construction on a grid
Take one of the three sketches and build it as a vector on a 10 × 10 module grid. Every coordinate must land on the grid.

??? success "Solution"
    **Example — a geometric `CS` lettermark:**

    1. A 240 × 240 frame, 24 px grid (10 modules).
    2. The letter `C`: a 144 × 144 px circle (6 modules), Fill `none`, Stroke 24 px (1 module), `Align: Center`. Then subtract a 72 × 48 px rectangle from the right side → that creates the letter's opening.
    3. The letter `S`: built from two arcs of the same 24 px weight, on the same 6-module height, 24 px away from the C.
    4. Check: every coordinate is a multiple of 24, every weight is 24.

    **The optical correction needed:** the 144 px circle looks smaller than a 144 px vertical bar. Enlarge the circle to 150 px (Y: −3) so they appear equal. **This is the only place where you are allowed to leave the grid** — and note why.

    **The final check:** copy the logo at 16 px. Is the C's opening still visible? If not, widen it from 48 to 60 px in the original construction.

### Exercise 3 — The variant set
Generate all five variants from the logo built in exercise 2 and test them on five different backgrounds.

??? success "Solution"
    **The variants:**

    | File | Construction |
    |------|-------------|
    | `logo-primary.svg` | Mark on top, name underneath, centred. Ratio: the name is 1.6 × the mark's width |
    | `logo-horizontal.svg` | Mark on the left, name on the right, vertically aligned on the optical centre. Gap = half the mark's width |
    | `logo-mark.svg` | The mark only, in a square frame with a margin equal to 1 module |
    | `logo-black.svg` | Everything in `#111827`, zero colours |
    | `logo-white.svg` | Everything in `#FFFFFF`, zero colours |

    **The background tests:**

    | Background | Which variant | Expected result |
    |------------|---------------|-----------------|
    | White | primary, in colour | Passes |
    | `brand/primary` orange | `logo-white` | Passes |
    | `#0F172A` dark | `logo-white` | Passes |
    | A bright photo | `logo-black` + a discreet shadow | Passes with the shadow |
    | A busy photo | None | **Fails** — you do not put a logo directly here; place it on a flat band |

    **The last row is the most important takeaway:** a logo does not work over everything. The usage rules must say explicitly that "on highly detailed photos, the logo sits on a flat colour band".

---

## Mini-project: your club's visual identity

Build the complete set for your computer science club (or another real organisation at your school): the logo with all its variants, a palette, fonts and a page of usage rules.

??? success "Deliverables and criteria"
    **The Figma file** with three pages:

    | Page | Content |
    |------|---------|
    | `Explorations` | The 20 scanned sketches + the 3 digitised directions |
    | `Logo` | The construction grid, the 5 variants, the reduction tests, the background tests |
    | `Guidelines` | The rules page, ready to export as a PDF |

    **The exported files:**

    ```
    logo/
      logo-primary.svg
      logo-horizontal.svg
      logo-mark.svg
      logo-black.svg
      logo-white.svg
      logo-mark-32.png      (favicon)
      logo-mark-512.png     (social media avatar)
    guidelines.pdf
    ```

    **The evaluation criteria:**

    | # | Criterion | Check |
    |---|-----------|-------|
    | 1 | The logo can be drawn from memory | Show it to a classmate for 10 seconds, ask them to draw it |
    | 2 | It works at 16 px | Export it and look at it on a phone |
    | 3 | It works in monochrome | The black version on white, from 3 metres |
    | 4 | Built on a grid | All coordinates on modules, with exceptions documented |
    | 5 | The text is converted to vector | Open the SVG on a computer without that font |
    | 6 | Clear space defined relatively | Not in mm, but relative to a part of the logo |
    | 7 | The "what not to do" chapter has ≥ 6 drawn examples | Count them |
    | 8 | The palette passes the contrast tests | The Contrast plugin on every pair |

    **The final test, the one that counts:** give the file set to a classmate who did not work on the project and ask them to make a simple poster using only the guidelines. If they succeed without asking you anything, the visual identity is complete. If they ask "what colour do I put here?", the guide has a gap — fill it.

---

## Summary

- A logo is an **identification mark**, not an explanation and not an illustration.
- Five types: wordmark, lettermark, mark, **combination** (the most practical), emblem.
- Five criteria: **simple, memorable, timeless, versatile, appropriate**.
- You start with an **identity brief**, then **20 sketches on paper**, then three directions.
- You build **on a grid**, with identical weights and angles from the 0/45/90 set.
- **Optical correction** is allowed and necessary — document it.
- Logo text gets **converted to vector** on delivery.
- A logo is a **set of 5 variants**, not one file.
- **Clear space** is defined relative to the logo, not in millimetres.
- The **"what not to do"** chapter is the most-read part of the whole guide.

---

**Next step:** [→ Lesson 13: Social media post](13-proiect-social-media.md)
