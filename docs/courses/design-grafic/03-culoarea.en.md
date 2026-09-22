---
lesson: 3
tags: [colour, hex, rgb, hsl, contrast, accessibility, palette]
summary: The colour wheel, the HEX, RGB and HSL systems, how to build a 3–5 colour palette and how to check contrast for accessibility.
---

# Lesson 03 · Colour

!!! tip "What you will learn"
    - How to read the **colour wheel** and what colour schemes are
    - The **HEX**, **RGB** and **HSL** systems — and why HSL is the most useful in practice
    - The **60-30-10** rule for building a palette
    - The difference between **RGB (screen)** and **CMYK (print)**
    - How to check **contrast** and why it matters for accessibility
    - How to create a palette in Figma and save it as styles

---

## The colour wheel

The colour wheel arranges colours in the order in which they mix. Every colour scheme is read off it.

```
                     RED
         RED-VIOLET       RED-ORANGE
    VIOLET                        ORANGE
  BLUE-VIOLET                YELLOW-ORANGE
    BLUE                           YELLOW
         BLUE-GREEN       YELLOW-GREEN
                    GREEN
```

**Warm colours** (red → yellow): advance towards the viewer, energy, urgency, appetite.
**Cool colours** (green → violet): recede, calm, trust, professionalism, technology.

### The colour schemes

| Scheme | How it is picked | Effect | When to use it |
|--------|------------------|--------|----------------|
| **Monochromatic** | One colour, several lightnesses | Very coherent, calm, safe | When you do not trust your own choices |
| **Analogous** | 2–3 neighbouring colours on the wheel | Harmonious, natural, gentle | Posters, illustrations, "warm" brands |
| **Complementary** | 2 opposite colours on the wheel | Maximum contrast, energetic | Sports, promotions, warnings |
| **Triadic** | 3 colours 120° apart | Lively, balanced, playful | Materials for children, events |
| **Split-complementary** | One colour + the two neighbours of its opposite | Contrast without aggression | The safest choice for beginners |

!!! tip "Start monochromatic"
    If in doubt, take **one single colour** and work with 5 different lightnesses of it, plus a neutral grey and a single accent colour. It is almost impossible to get wrong and the result looks deliberate.

---

## HEX, RGB, HSL

The same colour, three ways of writing it.

### HEX — for copying

`#F97316` — six hexadecimal characters: two for red, two for green, two for blue, each from `00` to `FF` (0–255).

```
#F9 73 16
 │  │  │
 │  │  └── blue:  0x16 = 22
 │  └───── green: 0x73 = 115
 └──────── red:   0xF9 = 249
```

This is the format you copy between Figma, CSS and Canva. It is not useful for thinking.

### RGB — how the screen works

`rgb(249, 115, 22)` — the same colour. Screens **add** light: red + green + blue at maximum give white. This is called **additive** mixing.

The variant with transparency: `rgba(249, 115, 22, 0.5)` — the last number is opacity, from 0 (invisible) to 1 (opaque).

### HSL — for thinking

`hsl(25, 95%, 53%)` — three values that match the way people talk about colour:

| Component | Range | What it means |
|-----------|-------|---------------|
| **H** (hue) | 0–360° | The position on the colour wheel |
| **S** (saturation) | 0–100% | How intense it is; 0% = grey |
| **L** (lightness) | 0–100% | How light it is; 0% = black, 100% = white |

!!! note "Why HSL makes your life easier"
    Want a darker version of your orange for a button's `hover` state? In HEX you have to guess. In HSL you subtract 10 from L: `hsl(25, 95%, 43%)`. Done.

    A whole palette is built by keeping H constant and varying L: `hsl(25, 95%, 95%)` for a very light background, `hsl(25, 95%, 53%)` for the main colour, `hsl(25, 95%, 25%)` for text on a light background.

In Figma, in the colour picker, the three-dot button lets you switch between HEX, RGB, HSL and CSS.

---

## RGB vs. CMYK

This is the difference that ruins most printed posters.

| | RGB | CMYK |
|---|-----|------|
| **Where** | Screens | Print |
| **How it works** | Adds light | Subtracts light (ink on paper) |
| **Components** | Red, Green, Blue | Cyan, Magenta, Yellow, Key (black) |
| **Colour gamut** | Wider | Narrower |
| **White** | Everything at maximum | The absence of ink (the paper) |

!!! warning "Fluorescent colours do not print"
    A bright neon green on screen (`#39FF14`) will come out of the press as a sad olive green. CMYK inks cannot reproduce the highly saturated colours of RGB.

    **What you do:** if the work goes to print, avoid saturations above ~85% and check a printed proof before the main run. Figma works natively in RGB — for real CMYK you need a conversion step at the print shop.

---

## The 60-30-10 rule

A balanced palette distributes colours in unequal proportions:

- **60% — the dominant colour.** Usually a neutral: white, very light grey, or a very dark grey. This is the background.
- **30% — the secondary colour.** Supports the structure: cards, bars, sections.
- **10% — the accent colour.** Only for what must be pressed or noticed: the main button, a badge, an important number.

!!! note "Example — this site's palette"
    - **60%** — very dark zinc background (`#0D0D10`) or white, depending on the theme.
    - **30%** — text and card greys (`#27272A`, `#A1A1AA`).
    - **10%** — orange (`#F97316`), used **only** for links, buttons and accents.

    Notice that the orange appears rarely. That is why it works: if it were everywhere it would no longer mean "here".

### The structure of a complete palette

For a serious project you need more than three colours:

| Role | How many | Example |
|------|----------|---------|
| Primary | 1 | The identity colour |
| Neutrals | 4–6 | From near-white to near-black |
| Accent | 1 | Opposite or complementary to the primary |
| Semantic | 3 | Success (green), warning (yellow), error (red) |

!!! warning "Do not use pure black and pure white"
    `#000000` on `#FFFFFF` gives a harsh contrast, tiring over a long read. Use `#111827` for text and `#FAFAFA` for background. The difference is small, but the eye feels it after 5 minutes of reading.

---

## Contrast and accessibility

Roughly **1 in 12 men** and **1 in 200 women** have some form of colour blindness. Many more read on a phone, in sunlight, on a cheap screen. Contrast is not an aesthetic option.

### The contrast ratio

It is measured as the ratio between the luminance of the text and that of the background, from 1:1 (identical) to 21:1 (black on white). The **WCAG** standard requires:

| Level | Normal text | Large text (≥ 24 px or ≥ 19 px bold) |
|-------|-------------|--------------------------------------|
| **AA** (mandatory minimum) | 4.5:1 | 3:1 |
| **AAA** (ideal) | 7:1 | 4.5:1 |

### How to check

- **In Figma:** the free **Contrast** or **Stark** plugin. You select the text and it shows the ratio instantly.
- **In the browser:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — paste the two HEX codes and it gives you the verdict.

!!! warning "The combinations that always fail"
    - Yellow on white (ratio ~1.5:1) — illegible
    - Light grey on white (`#CCCCCC` on `#FFFFFF`, ~1.6:1)
    - White text on light orange (~2:1)
    - Blue on red — almost zero luminance contrast, it vibrates

### Colour cannot be the only information

If in a chart the "sold" line is green and "unsold" is red, a colour-blind reader sees two identical lines. **Always add a second signal**: a label, a different shape, a dashed line, an icon.

!!! tip "The black and white test"
    Screenshot your work and turn it black and white (in Figma: a **Saturation → -100** effect over the whole frame). If the information still reads, the design is robust. If it falls apart, you lean too hard on colour.

---

## How to build a palette in Figma

1. Pick the primary colour. Do not invent it out of nowhere — start from something: the school colours, a photo you like, an existing logo.
2. Open [coolors.co](https://coolors.co/), lock the primary colour (the `space` key generates variants) and pick 2–4 more that work with it.
3. Generate the neutrals: take the primary, drop saturation to 5–10% and vary lightness from 98% to 10%. You will get greys that "have" your colour, not dead greys.
4. Check every text/background pair with the Contrast plugin.
5. **Save them as styles** in Figma: select an element with that colour, in the right panel under **Fill** click the four dots → **+** → give it a name.

### How to name colours

!!! warning "Do not name them after how they look"
    `Blue` is a bad name. When you change the blue to green a month from now, the style will still be called "Blue" but it will be green.

    Name them **after their role**:

    | Good name | Bad name |
    |-----------|----------|
    | `brand/primary` | `Orange` |
    | `brand/primary-hover` | `Dark orange` |
    | `text/strong` | `Black` |
    | `text/muted` | `Grey` |
    | `surface/base` | `White` |
    | `feedback/error` | `Red` |

The slash in the name automatically creates folders in Figma's style panel.

---

## Colour psychology, briefly and with reservations

The associations are real, but **cultural and contextual**, not universal.

| Colour | Common association in Europe | Used by |
|--------|------------------------------|---------|
| Red | Urgency, passion, danger, appetite | Promotions, fast food, warnings |
| Orange | Energy, approachable, friendly | Action buttons, education |
| Yellow | Optimism, attention, cheap | Warnings, discounts |
| Green | Nature, safety, "go", health | Confirmations, ecology, pharmacies |
| Blue | Trust, calm, technology, corporate | Banks, social networks, software |
| Violet | Creativity, luxury, mystery | Premium brands, cosmetics |
| Black | Elegance, authority, expensive | Fashion, premium technology |

!!! note "Mind the cultural context"
    White means purity in Europe and mourning in several Asian countries. Red is luck in China and danger in Europe. If your work addresses an international audience, check.

---

## Exercises

### Exercise 1 — The same colour in three systems
Take the colour `#2563EB` and write it in RGB and HSL. Then create a version 15% darker, using HSL.

??? success "Solution"
    - **HEX:** `#2563EB`
    - **RGB:** `rgb(37, 99, 235)` — `0x25 = 37`, `0x63 = 99`, `0xEB = 235`
    - **HSL:** `hsl(221, 83%, 53%)`

    The darker version: subtract 15 from L → `hsl(221, 83%, 38%)`, i.e. `#1D4ED8`.

    In Figma: select the element, open the colour picker, click the format label (it says `HEX`) and switch to `HSL`. Change only the third value.

### Exercise 2 — A 60-30-10 palette
Build a palette for a computer science club poster: one primary, four neutrals and one accent. Apply it to an A4 frame in 60-30-10 proportions.

??? success "Solution"
    A palette that works:

    | Role | HEX | HSL | Where |
    |------|-----|-----|-------|
    | `surface/base` | `#0F172A` | `hsl(222, 47%, 11%)` | Background — 60% |
    | `surface/raised` | `#1E293B` | `hsl(217, 33%, 17%)` | Cards — 30% |
    | `text/strong` | `#F1F5F9` | `hsl(210, 40%, 96%)` | Headings |
    | `text/muted` | `#94A3B8` | `hsl(215, 20%, 65%)` | Secondary text |
    | `brand/primary` | `#F97316` | `hsl(25, 95%, 53%)` | Accent — 10% |

    Contrast checks:
    - `text/strong` on `surface/base` → **15.8:1** — passes AAA
    - `text/muted` on `surface/base` → **6.4:1** — passes AA, not AAA. Acceptable for secondary text.
    - `brand/primary` on `surface/base` → **5.9:1** — passes AA for normal text.

    The typical mistake: using the accent on 40% of the surface. Then it is no longer an accent, it is a second dominant colour, and nothing stands out any more.

### Exercise 3 — Fix three combinations
The following pairs fail the contrast test. Fix each one, keeping the hue (H) unchanged.

1. Text `#FFD700` on background `#FFFFFF`
2. Text `#FFFFFF` on background `#FB923C`
3. Text `#9CA3AF` on background `#F3F4F6`

??? success "Solution"
    **1.** `#FFD700` on white = **1.6:1**. Yellow cannot be text on white, full stop. Keep H = 51° and drop L from 50% to 30%: `hsl(51, 100%, 30%)` = `#997A00`, ratio **5.3:1**. Passes AA.

    **2.** White on `#FB923C` = **2.1:1**. Either darken the background: `hsl(27, 96%, 40%)` = `#C2560A`, ratio **4.7:1**. Or keep the light orange and use dark text: `#431407` on `#FB923C` = **7.9:1**. The second option is more pleasant visually.

    **3.** `#9CA3AF` on `#F3F4F6` = **2.4:1**. Drop the text's L: `#4B5563`, ratio **7.3:1**. Passes AAA.

    Notice the pattern: in all three cases the solution was to **increase the lightness (L) difference**, not the hue difference. Colour contrast without luminance contrast helps nobody.

---

## Mini-project: the same poster, three palettes

Take the mini-project from lesson 02 (the "movement" poster) and make three versions identical in form, different only in palette: one **monochromatic**, one **complementary** and one **analogous**. Check the contrast on each.

??? success "Solution"
    **Monochromatic — blue:**
    background `hsl(217, 91%, 96%)`, lines `hsl(217, 91%, 25%)`, circle `hsl(217, 91%, 53%)`.
    Effect: calm, technical, coherent. Line/background contrast: 11.2:1.

    **Complementary — blue and orange:**
    background `hsl(217, 30%, 12%)`, lines `hsl(217, 60%, 70%)`, circle `hsl(25, 95%, 53%)`.
    Effect: energetic, the circle jumps out immediately. It is the most "event poster" of the three.

    **Analogous — blue, blue-green, green:**
    background `hsl(190, 40%, 95%)`, lines `hsl(200, 70%, 30%)`, circle `hsl(160, 70%, 40%)`.
    Effect: harmonious but soft — the circle does not stand out enough. That is the limit of the analogous scheme: it is beautiful, but it has low internal contrast.

    **The point of the exercise:** the palette does not decorate the composition, it **changes** it. The same form communicates "technical", "energetic" or "calm" through colour alone. And if you need an element to jump out, the analogous scheme will give you trouble.

---

## Summary

- The colour wheel gives the schemes: **monochromatic, analogous, complementary, triadic, split-complementary**.
- **HEX** for copying, **RGB** for screens, **HSL** for thinking and generating variants.
- **RGB on screen, CMYK in print.** High saturations do not print.
- **60-30-10**: neutral dominant, structural secondary, rare accent.
- Do not use `#000000` on `#FFFFFF` — it tires the eye.
- Minimum contrast **4.5:1** for normal text, **3:1** for large text (WCAG AA).
- **Colour cannot be the only information** — add a label, a shape or an icon.
- Name styles **by role** (`brand/primary`), not by appearance (`Orange`).
- The black and white test tells you whether the design survives without colour.

---

**Next step:** [→ Lesson 04: Typography](04-tipografia.md)
