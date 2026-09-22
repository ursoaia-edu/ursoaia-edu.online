---
lesson: 10
tags: [images, masks, export, png, jpg, svg, webp, resolution]
summary: Resolution and DPI, image cropping, masks, effects, and which format to export for screen and for print.
---

# Lesson 10 · Images, masks and export

!!! tip "What you will learn"
    - **Resolution**, **DPI** and why a good on-screen image is a bad printed one
    - The four crop modes: **Fill, Fit, Crop, Tile**
    - **Masks** — how to put an image inside a shape
    - Effects: shadows, blur, overlays for text over photos
    - Which format to pick: **PNG, JPG, WebP, SVG, PDF**
    - **Export scale** (1×, 2×, 3×) and why it matters

---

## Resolution and DPI

This is where almost every beginner trips.

| Term | What it is |
|------|-----------|
| **Resolution** | The total number of pixels: 1920 × 1080 |
| **PPI / DPI** | How many pixels fit into one inch (2.54 cm) in print |

A 1920 × 1080 px image:
- On a screen: excellent, it is Full HD.
- Printed at 300 DPI: 1920 / 300 = **6.4 inches** = 16 cm wide. That is all. On an A3 (42 cm) it would be blurry.

### How many pixels you need

| Destination | Required DPI | Example calculation |
|-------------|--------------|---------------------|
| Screen, web | 72 (by convention) | Width in px = displayed width |
| Quality print | **300** | A4 (21 cm) → 21 / 2.54 × 300 = **2480 px** |
| Large print (banners) | 100–150 | Viewed from a distance |
| Office printing | 150–200 | Enough for internal materials |

!!! warning "You cannot enlarge a small image"
    An 800 × 600 px photo scaled up to 2480 px does not gain detail — it gains blurry pixels. Missing information cannot be invented.

    **The rule:** always take the image **larger than you need** and scale it down. Scaling down harms nothing; scaling up does.

!!! note "How to check whether an image is enough"
    You need an image 12 cm wide on an A3 poster printed at 300 DPI?

    12 cm / 2.54 = 4.72 inches → 4.72 × 300 = **1417 px wide minimum**.

    If your photo is 1200 px, it is not enough. Find another.

---

## Images in Figma

### How to insert one

Three ways:
- **Drag the file** straight onto the canvas.
- ++ctrl+shift+k++ → pick the file.
- Select a shape → right panel, **Fill** → switch from `Solid` to **`Image`**.

The third way is the right one in most cases: the image becomes the **fill of a shape**, so you can control the shape independently of the image.

### The four crop modes

Select a shape with an image fill. In the right panel, under Fill, a menu appears:

| Mode | What it does | When |
|------|--------------|------|
| **Fill** | Covers the whole shape, crops the overflow | The default for photos in cards |
| **Fit** | Fits entirely, leaves empty space | Logos, when you must not crop |
| **Crop** | Gives you handles to choose the area by hand | Fine control |
| **Tile** | Repeats the image as a pattern | Textures, backgrounds |

!!! tip "Fill is almost always the right choice"
    A photo set to `Fit` inside a rectangular card leaves empty bands at the top and bottom. With `Fill` it fills the card and the excess is cropped. The only thing to watch: make sure you are not cutting off someone's head.

    In `Crop` mode you can reposition the visible area without changing the shape — double-click the image and move it.

---

## Masks

A **mask** makes a shape clip whatever sits above it.

### How it works

1. Draw the shape that will be the mask (a circle, a text, a shape from the Pen).
2. Place it **below** the content you want clipped (in the Layers panel, the mask sits lower).
3. Select the mask **and** the content.
4. ++ctrl+alt+m++ or the mask button in the top bar.

The result: the content is visible only inside the mask shape.

!!! note "Mask vs. image fill"
    For a photo in a circle you **do not need a mask** — set the image as the `Fill` of a circle and you are done. A mask is useful when you clip **several layers at once**, or when the mask shape is complex (text, for example).

### Text as a mask

The "image inside the letters" effect:

1. Write the text, large and bold (thin fonts do not work).
2. Place the photo above the text in the Layers panel.
3. Select both → ++ctrl+alt+m++.

!!! warning "After masking, the text stays editable"
    Good: you can change the word. Careful: if you switch to a thin font the effect disappears — there is no longer enough surface for the image to show through.

---

## Effects

Right panel, the **Effects** section, the **+** button:

| Effect | What it does | Use |
|--------|--------------|-----|
| **Drop shadow** | A shadow outside the shape | Lifts a card off the background |
| **Inner shadow** | A shadow inside | "Recessed" form fields |
| **Layer blur** | Blurs the element | Backgrounds, the composition test |
| **Background blur** | Blurs **what is behind** | Frosted glass (glassmorphism) |

### Shadows that look good

The typical mistake: a hard black shadow at 50% opacity. It looks like Word 2003.

A believable shadow has:
- A **colour** close to the background, not pure black. On a light blue background, a dark blue shadow.
- **Low opacity**: 8–15%.
- A **large blur** relative to the offset: `Y: 4, Blur: 16` looks better than `Y: 4, Blur: 4`.
- **Offset on Y only**, not on X (light comes from above).

```
Bad shadow:    X:4  Y:4   Blur:4   #000000 50%
Good shadow:   X:0  Y:4   Blur:16  #0F172A 12%
Large shadow:  X:0  Y:12  Blur:32  #0F172A 16%
```

!!! tip "Two stacked shadows look the most realistic"
    Add two `Drop shadow` effects: a small tight one (`Y: 1, Blur: 2, 8%`) for the contact with the surface, and a large diffuse one (`Y: 8, Blur: 24, 10%`) for volume. That is what every modern design system does.

### Text over a photo

The problem: the photo has light and dark areas, and the text is illegible over some of them.

Four solutions, starting from the simplest:

| Solution | How | When |
|----------|-----|------|
| **Flat overlay** | A coloured rectangle over the whole image, 40–65% opacity | The safest |
| **Gradient** | A rectangle with a gradient from opaque at the bottom to transparent at the top | Text only at the bottom |
| **Band** | An opaque rectangle only under the text | Short text |
| **Flat area** | Pick a photo with plain sky / wall and put the text there | The most elegant, but depends on the image |

!!! warning "Check the contrast here too"
    A 40% overlay may not be enough over a very light area. Apply the test from lesson 03: the Contrast plugin, on the lightest part of the image.

---

## Export formats

| Format | Type | Transparency | When you use it |
|--------|------|--------------|-----------------|
| **PNG** | Raster | Yes | Screenshots, graphics with text, anything needing a transparent background |
| **JPG** | Raster | No | Photos; a much smaller file than PNG |
| **WebP** | Raster | Yes | Modern web; ~30% smaller than JPG at the same quality |
| **SVG** | Vector | Yes | Logos, icons, flat illustrations |
| **PDF** | Mixed | Yes | Print, multi-page documents |

!!! note "The short rule"
    - Does it have text or crisp lines and need to be vector? → **SVG**
    - Is it a photo? → **JPG** (or WebP on the web)
    - Does it need a transparent background and is not vector? → **PNG**
    - Is it going to print? → **PDF**

### Export scale

Modern screens have double or triple density. An image exported at 1× will look blurry on a phone.

| Scale | For | A 400 × 300 frame becomes |
|-------|-----|---------------------------|
| **1×** | Reference, mockups | 400 × 300 px |
| **2×** | Retina screens (most phones and laptops) | 800 × 600 px |
| **3×** | Very dense phone screens | 1200 × 900 px |

In the Export panel you can add several rows, each with its own scale and suffix (`@2x`, `@3x`).

!!! tip "For the web, export at 2× and scale down in CSS"
    You export an 800 px `card@2x.jpg` and display it at 400 px. It looks crisp on any screen. For SVG the question does not arise — it scales perfectly anyway.

### Export for print

1. Set the frame to the real physical size. In Figma, for A4 use **595 × 842** (points, i.e. 72 DPI) or **2480 × 3508** (pixels at 300 DPI).
2. Export **PDF**.
3. If the print shop asks for **bleed** (a safety area for trimming), make the frame 3 mm larger on each side and extend the background to the edge.
4. Text stays as text in Figma's PDF — good for crispness. If the print shop does not have the font, ask them to use the PDF as it is rather than re-editing it.

!!! warning "Figma does not do CMYK"
    Figma exports in RGB. The CMYK conversion is done by the print shop. The practical consequence: **ask for a printed proof** before the main run, especially if you have saturated colours.

---

## Optimising for the web

A page with unoptimised images loads slowly, and visitors leave.

| Step | Tool | Typical gain |
|------|------|--------------|
| The right dimensions | Export exactly what you need, ×2 | The biggest gain |
| JPG compression | [Squoosh](https://squoosh.app/), quality 75–85 | 40–60% |
| WebP conversion | Squoosh | another 25–35% |
| SVG cleanup | [SVGOMG](https://jakearchibald.github.io/svgomg/) | 30–60% |

!!! note "A real example — this site"
    The site you are reading automatically generates `.webp` variants for every `.jpg` and `.png`, and the browser picks the smallest one it supports. The result: image loading dropped from 15.4 MB to 3.2 MB — roughly **80% less**, with no visible difference.

---

## Exercises

### Exercise 1 — Resolution calculations
Answer, showing your working:

1. What minimum resolution does an image need if it occupies 15 cm of width on an A3 poster printed at 300 DPI?
2. A 4000 × 3000 px photo printed at 300 DPI — what is its maximum physical size?
3. You need a 2 m wide banner viewed from 5 metres. What resolution is enough?

??? success "Solution"
    **1.** 15 cm / 2.54 = 5.9 inches → 5.9 × 300 = **1772 px wide**.

    **2.** 4000 / 300 = 13.3 inches → 13.3 × 2.54 = **33.8 cm wide**; 3000 / 300 = 10 inches → **25.4 cm tall**. So slightly larger than an A4, smaller than an A3.

    **3.** At 5 metres the eye cannot resolve fine detail. 100 DPI is enough: 200 cm / 2.54 = 78.7 inches → 78.7 × 100 = **7870 px wide**. At 300 DPI it would be 23,600 px — a huge, completely pointless file.

    **The conclusion:** the required DPI drops with viewing distance. 300 DPI is for what you hold in your hand.

### Exercise 2 — Legible text over a photo
Take a photo with uneven contrast (a landscape with a bright sky and dark ground, for example) and place a white heading over it in four versions: untreated, with a flat overlay, with a gradient, with a band. Check the contrast of each.

??? success "Solution"
    | Version | Construction | Minimum measured contrast |
    |---------|--------------|---------------------------|
    | Untreated | White text straight on the photo | ~1.8:1 over the sky — **fails** |
    | Flat overlay | A `#0F172A` rectangle at 55% over the whole image | ~7.2:1 — **passes AAA** |
    | Gradient | A rectangle with a linear gradient from `#0F172A` 85% (bottom) to 0% (top), text at the bottom | ~9.1:1 in the text area |
    | Band | An opaque `#0F172A` rectangle, as tall as the text + 32 px padding | ~15:1 |

    **Which is best?** It depends:
    - **Flat overlay** — the safest, but it darkens the whole photo.
    - **Gradient** — the most elegant; it keeps the photo clean at the top and guarantees legibility at the bottom. The default choice for posters and cards.
    - **Band** — the strongest contrast, but it covers a lot of the image.

    **The mandatory check:** measure the contrast in the **lightest** area under the text, not on average.

### Exercise 3 — A complete export set
Take the project card built in lesson 09 and export it in all the appropriate formats: for the web (2×), for a presentation (1×), for print. Compare the file sizes.

??? success "Solution"
    | Destination | Format | Scale | Typical size |
    |-------------|--------|-------|--------------|
    | Web, with a photo | JPG, quality 80 | 2× | 60–120 KB |
    | Web, optimised | WebP, quality 80 | 2× | 40–80 KB |
    | Presentation / document | PNG | 1× | 150–400 KB |
    | Print | PDF | — | 200 KB – 2 MB |
    | Just the icon from the card | SVG | — | 0.5–2 KB |

    **What you notice:**
    - The PNG is larger than the JPG although the dimensions are the same — PNG is lossless, JPG compresses.
    - WebP is visibly smaller than JPG at the same perceived quality.
    - The SVG is three orders of magnitude smaller than any raster — and looks perfect at any size.

    **Setting it up in Figma:** select the frame, press **+** three times under Export and set: `JPG 2× suffix @2x`, `PNG 1×`, `PDF`. One click exports all three.

---

## Mini-project: an event card with a photo

Build a **1080 × 1350 px** event card (the vertical social media format) containing a background photo, a gradient, a title, the date and the club logo. Export it in three versions: WebP for the web, JPG for sending over WhatsApp, PDF for printing at A5.

??? success "Solution"
    **The build:**

    1. Frame `event-card`, 1080 × 1350 px.
    2. **The photo:** find one on Unsplash at least 2000 px wide. Set it as the `Fill` of a rectangle covering the whole frame, mode `Fill`, repositioned with `Crop` so the interesting area sits in the top third.
    3. **The gradient:** a rectangle over the whole surface, `Linear gradient` fill, from `#0F172A` at 95% opacity at the bottom to `#0F172A` at 0% at 55% of the height.
    4. **The content** (vertical Auto Layout, gap 16, padding 64, anchored to the bottom):
        - Label: `COMPUTER SCIENCE CLUB`, 24 px, Medium, `#F97316`, tracking +12%
        - Title: 88 px, Bold, white, tracking −2%, at most 3 lines
        - Date and place: 32 px, Regular, `#CBD5E1`
    5. **The logo:** SVG, 64 px, top-left corner, 48 px margin. Give it a discreet shadow (`Y: 2, Blur: 8, 25%`) so it stays visible over light areas too.

    **The checks before exporting:**

    | Check | How |
    |-------|-----|
    | Title contrast | The Contrast plugin, on the lightest point under the text — at least 4.5:1 |
    | Photo resolution | Must be ≥ 1080 px on the short side **before** cropping |
    | Text does not touch the edges | At least 54 px (5% of 1080) everywhere |
    | The blur test | The title must be the dominant blob |

    **The exports:**

    | Version | Setting | Why |
    |---------|---------|-----|
    | Web | WebP, 1× (1080 px is already enough) | The native format for social platforms |
    | WhatsApp | JPG, 1×, quality 85 | WhatsApp recompresses anyway; do not send PNG |
    | A5 print | PDF | A5 at 300 DPI = 1748 × 2480 px; your 1080 px card gives ~150 DPI, acceptable for office printing but not for a print shop |

    **The important observation:** if you want professional printing, you have to rebuild the card at 1748 × 2480 px from the start, with a photo of at least 2500 px. You cannot enlarge at the end. That is exactly the mistake this lesson set out to prevent.

---

## Summary

- **Resolution** = total pixels; **DPI** = pixels per inch in print.
- For quality printing: **300 DPI**. A4 = 2480 px wide.
- **You cannot enlarge a small image.** Always take a larger one and scale down.
- The required DPI **drops with viewing distance**: a banner needs 100, not 300.
- Cropping: **Fill** (the default), Fit, Crop, Tile.
- A mask clips what is above it; for a single image in a shape, use `Fill` instead of a mask.
- Good shadows: **offset on Y only**, large blur, 8–15% opacity, a colour close to the background.
- Text over a photo: a **gradient** is the best default solution.
- Formats: **SVG** vector, **JPG/WebP** photos, **PNG** transparency, **PDF** print.
- Export at **2×** for the web; optimise with Squoosh and SVGOMG.

---

**Next step:** [→ Lesson 11: Poster for a school event](11-proiect-afis.md)
