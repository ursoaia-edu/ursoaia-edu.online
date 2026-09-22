---
lesson: 15
tags: [capstone, visual identity, brand book, design system, portfolio]
summary: Capstone project — assembling every lesson into a complete visual identity, with a brand book and a set of real applications.
---

# Lesson 15 · Project: a complete visual identity

!!! tip "What you will build"
    A **complete visual identity** for the computer science club — everything needed for anyone to produce coherent materials without asking you a single question:

    - The brand platform: who we are, for whom, what tone
    - The logo with all its variants (from lesson 12)
    - A colour, typography and spacing system
    - A component library in Figma
    - **Six real applications**: poster, post, presentation, member card, t-shirt, site header
    - A **brand book** exportable as a PDF

---

## What separates a logo from an identity

A logo answers the question "how do people recognise us".

A visual identity answers a much harder one: **"what does *any* material we produce look like, made by *anyone*, two years from now?"**

The practical test: if a new club member has to make a poster and sends you three questions on WhatsApp ("which font?", "which orange?", "how big is the logo?"), your identity is not complete. The answers should already be written down.

---

## The project structure

```
Figma file: "Visual identity — Computer science club"
│
├── 01 · Brand platform      → who we are, tone, audience
├── 02 · Logo                → construction, variants, rules
├── 03 · Foundations         → colour, typography, spacing, grid
├── 04 · Components          → buttons, cards, badges, icons
├── 05 · Applications        → the 6 real applications
└── 06 · Brand book          → the pages for the PDF export
```

---

## Page 01 — The brand platform

A page of text, but the one that decides everything else. Six blocks:

| Block | Content | Length |
|-------|---------|--------|
| **Mission** | What we do and why | 1 sentence |
| **Audience** | Who sees our materials | 2–3 concrete groups |
| **Personality** | 3 adjectives we aim for | 3 words |
| **Anti-personality** | 3 adjectives we avoid | 3 words |
| **Tone of voice** | How we write: formal / direct / friendly, with examples | 3 "do / don't" pairs |
| **Differentiation** | What keeps us from looking like other clubs | 1–2 sentences |

!!! note "A completed example"
    **Mission:** we build real electronics and programming projects and publish everything we learn, for free.

    **Audience:** middle school students who have never programmed; high school students looking for projects; teachers and parents who want to understand what we do.

    **Personality:** technical, approachable, practical.

    **Anti-personality:** corporate, childish, elitist.

    **Tone:**

    | Do | Don't |
    |----|-------|
    | "Light up an LED in 10 minutes" | "Discover the fascinating world of electronics" |
    | "Not working? Check the LED polarity" | "Some technical difficulties may arise" |
    | "Come on Thursday at 15:00 to lab 2" | "We warmly await you at our weekly gathering" |

    **Differentiation:** we publish the full code and schematics, not just photos of the result.

!!! tip "Why the 'do / don't' table matters"
    It is the part of the brand book that the people writing the copy will actually read. An abstract principle ("approachable tone") helps nobody; two concrete examples side by side change how someone writes immediately.

---

## Page 02 — Logo

Bring everything over from lesson 12 and organise it for quick reference:

1. The construction grid, with the modules visible.
2. The five variants, each with its file name underneath.
3. Clear space, drawn with the unit marked.
4. Minimum sizes, with examples at actual size.
5. The background tests (the five from lesson 12).
6. The "what not to do" chapter, with at least six examples.

---

## Page 03 — Foundations

### Colour

Document it visually, not just as invisible styles:

| What you show | How |
|---------------|-----|
| Every colour | A 96 × 96 square, the style name, HEX, HSL |
| The verified pairs | A table of contrast ratios for every text/background combination |
| The 60-30-10 proportions | A visual bar showing the distribution |
| The semantic colours | Success, warning, error, with a usage example |

!!! warning "Document what is forbidden too"
    Add explicitly: "orange is not used as a background for large blocks of text" or "green is used **only** for confirmations, never decoratively".

    Without those rules, in six months someone will make an entirely green poster and will be right to point out that nothing said they could not.

### Typography

| What you show | How |
|---------------|-----|
| The chosen fonts | The full alphabet, digits, Romanian diacritics (ă â î ș ț) |
| The type scale | The 6 steps, applied to real text, with specs |
| The weight pairings | What combines with what |
| Alignment rules | When you centre, when you do not |

!!! warning "Check the diacritics"
    Many free fonts draw `ș` and `ț` with a **cedilla** (ş, ţ) instead of a **comma below** (ș, ț). That is the wrong form for Romanian.

    Check before choosing the font: type `Știință și țară` and look closely. Inter, Source Sans 3, Lato and IBM Plex Sans have the correct forms.

### Spacing and grid

- The spacing scale (4, 8, 16, 24, 32, 48, 64, 96), drawn visually.
- The grids for the three breakpoints.
- The print grid (A4 and A3).

---

## Page 04 — Components

The library from lesson 08, completed:

| Group | Components |
|-------|-----------|
| **Primitives** | `button` (9 variants), `input` (6 states), `badge` (4 types), `avatar` (3 sizes) |
| **Icons** | The 8+ set from lesson 07, as instances |
| **Composites** | `card/project`, `card/feature`, `nav/mobile`, `nav/desktop`, `footer` |
| **Social templates** | The 4 from lesson 13 |

All of them must use **only** the styles from page 03.

---

## Page 05 — Applications

This is where you find out whether the identity really works. Six real materials, built only from what is defined above.

| # | Application | Format | What it demonstrates |
|---|-------------|--------|----------------------|
| 1 | **Event poster** | A3, 842 × 1191 pt | Large-scale typography, hierarchy, print |
| 2 | **Post + story** | 1080 × 1350 and 1080 × 1920 | Adapting across formats |
| 3 | **Presentation slide** | 1920 × 1080, 3 slides | A repeatable layout pattern |
| 4 | **Member card** | 85 × 54 mm (bank card format) | The logo at a small size, print |
| 5 | **T-shirt** | Mockup, 25 × 30 cm print | Monochrome logo, applied to fabric |
| 6 | **Site header** | 1440 × 800 px | Components, grid, responsive |

!!! tip "The member card is the best test"
    At 85 × 54 mm, the logo ends up ~20 mm wide and the text at 7–8 pt. If your identity works on a member card, it works almost anywhere.

    If the logo turns into a blob at that size, go back to lesson 12 and make the compact variant.

### Mockups

For the t-shirt and the card, present them in context, not as flat files. Free mockup sources: [Mockey](https://mockey.ai/), or build a simple mockup yourself in Figma (a t-shirt photo + the logo with a `Multiply` blend mode and a slight distortion).

---

## Page 06 — The brand book

The document you hand to other people. **At most 20 pages**, A4 landscape (1123 × 794 pt) or 16:9 for reading on screen.

### The structure

| Pages | Content |
|-------|---------|
| 1 | Cover: a large logo, the organisation name, the year |
| 2 | Contents |
| 3–4 | The brand platform (mission, audience, tone) |
| 5–8 | Logo: variants, clear space, minimum sizes, what not to do |
| 9–11 | Colour: the palette, proportions, contrast |
| 12–13 | Typography: fonts, scale, examples |
| 14 | Spacing and grid |
| 15–18 | Applications: one page per material |
| 19 | Where the files live (a link to the assets folder) |
| 20 | Contact: who answers questions |

!!! note "A brand book is not read, it is consulted"
    Nobody will read 20 pages cover to cover. People will open the document with a specific question ("what is the orange's code?") and hunt for the answer.

    Design consequences:
    - **A contents page with page numbers**, mandatory.
    - Large, clear headings on every page.
    - Critical information (colour codes, font names) in **tables**, not in prose.
    - Visual examples next to every rule.

---

## Exercises

### Exercise 1 — The brand platform
Fill in the six blocks of the brand platform for your club. The "do / don't" table must have at least three pairs, taken from your organisation's real texts.

??? success "Solution"
    The indicators of a good platform:

    - **The mission** is a sentence containing a **concrete verb**. "We build and publish" is good; "we promote a passion for technology" says nothing.
    - **The audience** has named groups, not "everybody". If you wrote "all students", subdivide: someone who has never programmed vs. someone looking for advanced projects — they need different messages.
    - **The anti-personality** is as important as the personality. Without it, any direction looks acceptable.
    - **The tone pairs** must come from **real** texts you have written. If you invent them, they will not help you when you write the next poster.

    **Test:** hand the platform to a classmate and ask them to write a post headline. If the resulting tone resembles yours, the platform works.

### Exercise 2 — The contrast audit
Build the full contrast table for your palette: every text colour on every background colour. Mark in green what passes AA, in yellow what passes only for large text, in red what fails.

??? success "Solution"
    An example table, for a 5-colour palette:

    | Text on background → | `#0F172A` | `#1E293B` | `#F8FAFC` | `#F97316` |
    |-------------------|-----------|-----------|-----------|-----------|
    | `#F8FAFC` | 15.8 ✅ | 13.1 ✅ | 1.0 ❌ | 2.7 ❌ |
    | `#CBD5E1` | 11.2 ✅ | 9.3 ✅ | 1.4 ❌ | 1.9 ❌ |
    | `#94A3B8` | 6.4 ✅ | 5.3 ✅ | 2.5 ❌ | 1.1 ❌ |
    | `#64748B` | 3.8 ⚠️ | 3.1 ⚠️ | 4.2 ⚠️ | 1.5 ❌ |
    | `#0F172A` | 1.0 ❌ | 1.2 ❌ | 15.8 ✅ | 5.9 ✅ |
    | `#F97316` | 5.9 ✅ | 4.9 ✅ | 2.7 ❌ | 1.0 ❌ |

    **What the table teaches you:**
    - `#64748B` passes AA nowhere for normal text. You use it **only** for text ≥ 24 px, or for decorative elements. Document that.
    - On an orange background, the only safe text colour is `#0F172A`. So **orange buttons have dark text**, not white. That is a design decision made by the table, not by taste.
    - `#F8FAFC` on `#F97316` gives 2.7 — the combination most people reach for instinctively, and it fails.

    **Put the table in the brand book.** It is one of the most consulted pages.

### Exercise 3 — The coherence test
Place the six applications side by side, at small scale, and run the blur test. Then show them to someone who did not work on the project.

??? success "Solution"
    **The blur test on the set:** at blur 15, all six should show the **same patterns** — the same distribution of dark and light blobs, the same position for the colour accent, the same density.

    If one looks completely different, check:
    - Does it use different colour proportions? (60-30-10 broken)
    - Does it have different margins? (the grid ignored)
    - Does it have a different hierarchy ratio? (the type scale ignored)

    **The test with a new person**, three questions:
    1. "Are these from the same organisation?" — the answer must be yes, instantly.
    2. "What is their colour?" — they must name one single colour.
    3. "How would you describe the tone?" — the answer must contain at least one of the three adjectives from your platform.

    If question 3 returns an adjective from your **anti-personality** list, the identity is communicating something other than you intended. The usual culprit: the font or the corner radius.

---

## Mini-project: the complete identity

Work through all six pages and deliver the full set.

??? success "Deliverables and criteria"
    **The deliverables:**

    ```
    visual-identity/
    ├── brand-book.pdf                  (20 pages)
    ├── logo/
    │   ├── logo-primary.svg
    │   ├── logo-horizontal.svg
    │   ├── logo-mark.svg
    │   ├── logo-black.svg
    │   ├── logo-white.svg
    │   ├── logo-mark-32.png
    │   └── logo-mark-512.png
    ├── fonts/
    │   └── google-fonts-links.txt
    ├── templates/
    │   ├── poster-a3.pdf
    │   ├── post-1080x1350.png
    │   ├── story-1080x1920.png
    │   └── slide-16x9.pdf
    └── README.txt                      (how to use the files)
    ```

    Plus the **Figma link** with view rights to the file with the six pages.

    **The evaluation criteria:**

    | # | Criterion | Check |
    |---|-----------|-------|
    | 1 | A complete brand platform | The 6 blocks, with 3 tone pairs |
    | 2 | The logo in 5 vector variants | Open the SVGs without the original font |
    | 3 | The palette documented with a contrast table | The full, colour-coded table |
    | 4 | The fonts have correct Romanian diacritics | Type `Știință și țară` |
    | 5 | Components that use styles only | Change `brand/primary` — does everything update? |
    | 6 | Six real applications | All present and built from the library |
    | 7 | The member card is legible | Print it at 85 × 54 mm |
    | 8 | Brand book ≤ 20 pages, with contents | Count the pages |
    | 9 | The "what not to do" chapter has ≥ 6 examples | Count them |
    | 10 | The new-person test | The 3 questions from exercise 3 |

    **The final test — the one that really counts:**

    Give **only** `brand-book.pdf` and the file folder to a classmate who did not work on the project. Ask them to make an A3 poster for a real event. Time them and count the questions they ask you.

    | Result | Interpretation |
    |--------|----------------|
    | 0 questions, a coherent poster | A complete identity |
    | 1–2 questions | Almost; add the answers to the brand book |
    | 3+ questions | The guide has structural gaps |
    | An incoherent poster, no questions | Worse than the questions: the rules exist but cannot be found. Reorganise the contents |

    **What you do next:** add the answer to every question you received into the brand book. A good brand book grows through the questions its author had to answer.

---

## Summary

- A logo answers "how do you recognise us"; an identity answers **"what does any material, made by anyone, look like two years from now"**.
- The **brand platform** (mission, audience, personality, anti-personality, tone, differentiation) drives every visual decision.
- The **"do / don't" table** is the most used part of the whole document.
- Document **what is forbidden** too, not only what is allowed.
- Check the **Romanian diacritics** (ș, ț with a comma, not a cedilla) before choosing a font.
- The **full contrast table** makes design decisions instead of taste.
- **Six real applications** prove the system works; the member card is the harshest test.
- Brand book: **at most 20 pages**, with contents, tables and visual examples.
- The final test: a classmate produces a correct material **without asking you anything**.

---

**Next step:** [→ Lesson 16: Interactive landing page prototype](16-proiect-prototip-figma.md)
