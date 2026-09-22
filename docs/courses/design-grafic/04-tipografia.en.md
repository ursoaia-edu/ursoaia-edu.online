---
lesson: 4
tags: [typography, fonts, hierarchy, legibility, google fonts]
summary: The anatomy of a letter, font families, how to pick a pairing that works, size, line height and line length.
---

# Lesson 04 · Typography

!!! tip "What you will learn"
    - The **anatomy of a letter** and why x-height matters
    - The four **font families** and when each is used
    - The difference between **weight**, **style** and **size**
    - **Line height**, **letter spacing** and **line length**
    - How to pick a **font pairing** that works
    - How to install Google Fonts and save text styles in Figma

---

## Why typography is 90% of design

Open any poster, any website, any packaging. Mentally remove the images. What is left? Text. Most of your design decisions will in fact be decisions about text: how big, which font, how far from everything else.

A design with good typography and no images looks professional. A design with excellent images and bad typography looks amateurish. That order never reverses.

---

## The anatomy of a letter

```
      ┌─────────────────────────  ascender line
      │   h        ┌──
  ┌───┼───────────┼──────────────  x-height line
  │   │  x  o  n  │
  └───┴───────────┴──────────────  baseline
          │
          └──────────────────────  descender line (g, p, y)
```

| Term | What it is | Why it matters |
|------|-----------|----------------|
| **Baseline** | The line the letters "stand" on | Aligns text of different sizes |
| **x-height** | The height of the lowercase `x` | Determines real legibility |
| **Ascenders** | The part rising above the x-height (`b`, `d`, `h`, `l`) | Helps word recognition |
| **Descenders** | The part dropping below the baseline (`g`, `p`, `y`) | Demands space between lines |
| **Counter** | The hole inside letters (`o`, `e`, `a`) | If small, the text "closes up" at small sizes |

!!! note "x-height matters more than the point size"
    Two fonts both set at 16 px can look completely different in size. A font with a large x-height (Inter, Roboto) looks much bigger and reads better at small sizes than one with a small x-height (Playfair Display, Garamond).

    Practical consequence: when you change the font, you **must** recheck the sizes. They do not carry over automatically.

---

## The font families

### Serif

They have "feet" — small terminations at the ends of the strokes. Georgia, Times New Roman, Playfair Display, Merriweather.

- **Association:** tradition, authority, editorial, seriousness.
- **Good at:** long printed text, elegant headings, books, diplomas.
- **Weak at:** small screens, sizes under 14 px, interfaces.

### Sans-serif

No feet. Inter, Helvetica, Roboto, Open Sans, Montserrat.

- **Association:** modern, clean, neutral, technological.
- **Good at:** screens, interfaces, headings, short text, anything.
- **Weak at:** nothing major — which is why it is the default choice.

### Monospace

Every letter has the same width. JetBrains Mono, Fira Code, Courier.

- **Association:** code, data, technical, machine.
- **Good at:** code, tables of numbers, technical labels, clocks.
- **Weak at:** long text — it reads slowly.

### Display / decorative

Fonts with a strong personality, drawn for large sizes. Lobster, Bebas Neue, Bangers.

- **Association:** depends entirely on the font.
- **Good at:** **only** very large headings, logos, posters.
- **Weak at:** absolutely everything else.

!!! warning "The decorative font rule"
    A decorative font is used **once per page**, at a large size. If you put it on headings, subheadings and buttons alike, the design becomes tiring within 3 seconds.

---

## Weight, style, size

### Weight

| Name | Numeric value | Where |
|------|---------------|-------|
| Thin | 100 | Almost never |
| Light | 300 | Very large headings |
| Regular | 400 | Body text |
| Medium | 500 | Labels, subheadings |
| Semi Bold | 600 | Headings |
| Bold | 700 | Strong accents, large headings |
| Black | 900 | Posters, big numbers |

!!! tip "Use at most 3 weights"
    Regular for body, Semi Bold for headings, Medium for labels. That is it. A design with 6 weights of the same font looks as messy as one with 6 different fonts.

### Style

**Italic** is used for: book and work titles, foreign words, subtle emphasis. It is **not** used for whole paragraphs — it tires the reader.

!!! warning "Fake italic"
    Some programs artificially "slant" a font when it has no real italic cut. The result looks crooked. In Figma, check whether `Italic` appears in the font's style list; if it does not, the font has no italic and should not be forced.

### Size

A type scale is a set of sizes with a constant ratio between them. You do not pick sizes at random.

**The 1.25 scale (Major Third)** — suited to interfaces:

| Role | Size |
|------|------|
| Small text | 13 px |
| Body text | 16 px |
| Subheading | 20 px |
| Section heading | 25 px |
| Page heading | 31 px |
| Large heading | 39 px |

**The 1.5 scale** — suited to posters, where you want dramatic contrast:

| Role | Size |
|------|------|
| Details | 16 px |
| Information | 24 px |
| Subheading | 36 px |
| Heading | 54 px |
| Dominant heading | 81 px |

!!! note "Why a scale rather than random sizes"
    The sizes 14, 15, 17, 18 look like a mistake — the differences are too small to seem intentional, but too large to be identical. The eye reads this as "careless". A scale guarantees that every step is visible and deliberate.

---

## Spacing

### Line height

The distance between the baselines of two consecutive lines.

| Text type | Line height |
|-----------|-------------|
| Large headings (above 32 px) | 1.1 – 1.2 |
| Subheadings | 1.3 |
| Body text | 1.5 – 1.6 |
| Small, dense text | 1.4 |

!!! warning "The default line height is almost always wrong"
    Figma sets `Auto`, which means roughly 1.2. For a heading that is fine. For a paragraph it is too tight — the lines stick together and the eye jumps to the wrong line when it returns from the end of a line.

    **The inverse rule:** the larger the text, the smaller the line height. A 60 px heading at line height 1.5 has huge gaps between lines.

### Letter spacing (tracking)

| Situation | Value |
|-----------|-------|
| Body text | 0 (leave the font alone) |
| Very large headings | −1% to −3% (tightens them, looks more compact) |
| ALL CAPS | +5% to +10% (mandatory) |
| Small caps labels | +10% to +15% |

!!! tip "Capitals need air"
    `COMPUTER SCIENCE CLUB` set without extra spacing looks cramped, because capital letters all share the same height and leave no natural gaps. Always add 5–10% tracking to all-caps text.

### Line length (measure)

**45–75 characters per line**, ideally ~66. Spaces included.

- **Too short** (under 45): the eye jumps to the next line too often, the rhythm breaks.
- **Too long** (over 75): at the end of a line, the eye can no longer find the start of the next one.

In practice, on an A4 poster, a text column should not exceed ~12 cm in width at 12 pt.

---

## How to pick a font pairing

### The rule: contrast, not conflict

Two fonts must be **clearly different**. Two similar sans-serifs (Helvetica + Arial) look like a mistake, not a choice.

| Combination | Does it work? | Why |
|-------------|---------------|-----|
| Serif heading + sans-serif body | Yes | Clear family contrast |
| Sans-serif heading + serif body | Yes | The classic editorial pairing, reversed |
| Same font, different weights | Yes | The safest option |
| Two different sans-serifs | Risky | Only if their personalities differ a lot |
| Two different serifs | No | Almost impossible to make look intentional |
| Two decorative fonts | No | Never |

!!! tip "The safest pairing: a single font"
    Take **Inter** and use Bold 40 for the heading, Medium 18 for the subheading, Regular 16 for the body. You get clear contrast and zero risk. Many large brands do exactly this.

### Pairings that are guaranteed to work

| Heading | Body | Tone |
|---------|------|------|
| Playfair Display | Source Sans 3 | Elegant, editorial |
| Montserrat | Merriweather | Modern + readable |
| Bebas Neue | Inter | Poster, impact |
| Inter Bold | Inter Regular | Technical, clean, safe |
| Space Grotesk | IBM Plex Sans | Tech, contemporary |
| Lora | Lato | Warm, friendly |

---

## Google Fonts in Figma

1. Figma already has **all Google fonts** available in the web version. You search for them directly in the font list.
2. For the desktop app you need **Figma Font Helper** (installed once) or you install the font in your system.
3. To use the font on a website: [fonts.google.com](https://fonts.google.com/) → pick the styles → copy the `<link>` code into `<head>`.

!!! warning "Do not load 8 font styles on a website"
    Every weight and every italic is a separate file to download. A site loading Inter in 9 weights transfers over 1 MB for text alone. Pick **3 weights** and stop there.

### Text styles in Figma

As with colours, you save combinations as reusable styles:

1. Select a correctly formatted piece of text.
2. In the right panel, in the **Text** section, click the four dots → **+**.
3. Give it a name **by role**: `heading/h1`, `heading/h2`, `body/base`, `body/small`, `label/caps`.

When you change the style, **all text using it updates**. In a poster with 20 pieces of text, that is the difference between 2 seconds and 10 minutes.

---

## Common mistakes

| Mistake | Why it is a problem | The fix |
|---------|---------------------|---------|
| Centred text over several lines | Ragged left edge; the eye hunts for the start of every line | Left-align anything over 3 lines |
| Justified text in a narrow column | "Rivers" of vertical white space through the text | Left-align |
| Text on a photo with no treatment | Unpredictable contrast, illegible over busy areas | Dark overlay, blur behind the text, or a colour band |
| All text in capitals | Words lose their shape and are read letter by letter | Capitals only for short labels |
| 5 fonts on one page | There is no hierarchy, only noise | At most 2 fonts |
| Size under 12 px in print | Illegible for many readers | At least 9 pt in print, 14 px on the web |

!!! note "Orphans and widows"
    An **orphan** is a single word left on the last line of a paragraph. It looks careless. It is fixed by forcing an earlier line break or slightly adjusting the column width. On a poster with 3 lines of text, it matters.

---

## Exercises

### Exercise 1 — The same sentence, four families
Write the sentence "The computer science club is taking new members" four times in an 800 × 600 px frame, at 32 px, using a serif, a sans-serif, a monospace and a display font. Note under each what tone it conveys.

??? success "Solution"
    - **Playfair Display** — solemn, like a formal invitation. Fitting if the event is formal.
    - **Inter** — neutral, clear, modern. Works in any context; it is the correct default.
    - **JetBrains Mono** — technical, "programmer-ish". Here it genuinely fits the subject — but it becomes tiring beyond 2 lines.
    - **Bebas Neue** — it shouts. Good for a poster seen from a distance, bad for any text meant to be read.

    Important observation: all four are at the **same size (32 px)** but look like different sizes. Bebas Neue looks bigger, Playfair smaller. That is x-height in action.

### Exercise 2 — Fix a paragraph
In a 600 × 400 px frame, place a ~60-word paragraph with Figma's default settings (16 px, Auto line height, 580 px wide, centred). Then fix it.

??? success "Solution"
    The problems in the initial version:
    - 580 px width at 16 px ≈ **95 characters per line** — too long.
    - Auto line height ≈ 1.2 — too tight for a paragraph.
    - Centred — the ragged left edge makes reading hard.

    The fix:
    - Width **440 px** → ~66 characters per line.
    - Line height **1.6** (i.e. 25.6 px at size 16).
    - **Left** alignment.
    - Text colour `#374151` instead of pure black.

    Read both versions out loud. The second reads visibly more fluently, although you changed only four settings and not a single word.

### Exercise 3 — A type scale
Build a scale with a ratio of 1.25 starting from 16 px, over 6 steps, and apply it to a page with: a heading, a subheading, two section headings, body text and a footnote.

??? success "Solution"
    The scale (each value × 1.25, rounded):

    | Step | Size | Role | Weight | Line height |
    |------|------|------|--------|-------------|
    | −1 | 13 px | Footnote | Regular | 1.4 |
    | 0 | 16 px | Body text | Regular | 1.6 |
    | 1 | 20 px | Subheading | Medium | 1.4 |
    | 2 | 25 px | Section heading | Semi Bold | 1.3 |
    | 3 | 31 px | Page heading | Semi Bold | 1.2 |
    | 4 | 39 px | Dominant heading | Bold | 1.1 |

    Save each step as a text style in Figma: `body/small`, `body/base`, `heading/h4` … `heading/h1`.

    Check: if you now change the font from Inter to Source Sans 3 by editing only the styles, the whole page updates coherently. If you had to fix any text by hand, that text was not using a style.

---

## Mini-project: a typographic poster

Build an A3 poster for a school event using **text only** — no images, no icons, at most one simple geometric shape. One font, at most 3 weights.

??? success "Solution"
    Example — "Researchers' Night" at the computer science club:

    **Settings:** A3 frame (842 × 1191 pt), background `#0F172A`, Inter, 60 pt margins.

    | Element | Text | Size | Weight | Colour | Tracking |
    |---------|------|------|--------|--------|----------|
    | Label | `COMPUTER SCIENCE CLUB` | 18 | Medium | `#F97316` | +12% |
    | Heading | `RESEARCHERS' NIGHT` | 96 | Bold | `#F8FAFC` | −2% |
    | Date | `27 SEPTEMBER` | 54 | Semi Bold | `#F97316` | 0 |
    | Time and place | `18:00 · Lab 2` | 28 | Regular | `#94A3B8` | 0 |
    | Description | 2 lines, max 60 characters | 20 | Regular | `#CBD5E1` | 0 |
    | Details | `Free entry · ursoaia-edu.online` | 16 | Medium | `#64748B` | 0 |

    Plus **one single shape:** an 8 × 200 pt orange bar under the heading, as a separator.

    **Why it works:**
    - One font, three weights → total coherence.
    - The jump from 96 to 54 to 28 is large and deliberate → a hierarchy readable on the move.
    - The orange appears exactly three times (label, date, bar) → the accent stays an accent.
    - The heading with negative tracking (−2%) looks compact and intentional at 96 pt.
    - The all-caps label has +12% tracking → it breathes.

    **Mistakes to avoid:**
    - The heading centred over 3 lines → ragged left edge.
    - The date at the same size as the heading → the reader cannot tell what matters most.
    - More than 6 blocks of text → nobody reads a poster like a book.

---

## Summary

- **x-height** determines real legibility, not the declared point size.
- Four families: **serif** (tradition), **sans-serif** (default), **monospace** (technical), **display** (once, large).
- At most **2 fonts** and **3 weights** per project.
- Sizes come from a **scale** (1.25 for interfaces, 1.5 for posters), not from guesswork.
- Line height: **1.5–1.6** for body text, **1.1–1.2** for large headings.
- Capitals need **+5% to +15% tracking**.
- Line length: **45–75 characters**, ideally 66.
- **Left-align** any paragraph longer than 3 lines.
- Save text styles in Figma, named **by role**, not by appearance.

---

**Next step:** [→ Lesson 05: Composition and grid](05-compozitie-si-grila.md)
