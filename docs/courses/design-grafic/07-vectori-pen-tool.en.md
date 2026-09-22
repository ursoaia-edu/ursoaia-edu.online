---
lesson: 7
tags: [figma, vectors, pen tool, bezier, svg, icons]
summary: The difference between vector and raster, nodes and Bézier handles, the Pen tool and boolean operations for building icons.
---

# Lesson 07 · Vectors and the Pen Tool

!!! tip "What you will learn"
    - The real difference between **vector** and **raster**
    - What **nodes** and **Bézier handles** are
    - How to use the **Pen** tool without losing your mind
    - **Stroke**: weight, caps, joins and dashes
    - How to build a coherent **icon set**
    - What **SVG** is and why it matters for the web

---

## Vector vs. raster

| | Vector | Raster |
|---|--------|--------|
| **How it is stored** | Mathematical formulas: points, curves, fills | A grid of pixels, each with its own colour |
| **When enlarged** | Stays perfectly sharp at any size | Pixelates |
| **File size** | Small, grows with shape complexity | Large, grows with pixel dimensions |
| **Good for** | Logos, icons, flat illustrations, text | Photos, textures, complex effects |
| **Formats** | SVG, AI, EPS, PDF | PNG, JPG, WebP, GIF |

!!! note "Why a logo has to be vector"
    Your school's logo will appear on a business card (2 cm) and on an entrance banner (2 m). A PNG good enough for the banner would be tens of MB; one good enough for the card would be blurry on the banner.

    A 4 KB SVG looks perfect in both cases. That is why lesson 12 requires the logo in vector form.

Figma is essentially a vector editor. Everything you draw with Rectangle, Ellipse or Pen is vector. Only imported images are raster.

---

## Nodes and handles

Any vector shape is defined by **nodes** (points) connected by **segments**.

```
    ●────────────●        two nodes, straight segment

         ╭───╮
    ●───╯     ╰───●       two nodes, curved segment

    ●─ ─ ─○               a node (●) and its handle (○)
```

### The node types

| Type | What it looks like | Effect |
|------|-------------------|--------|
| **Corner** | No handles, or independent handles | A sharp angle |
| **Smooth** (mirrored) | Two symmetric handles on the same line | A continuous curve, no kink |
| **Asymmetric** (angle) | Two handles on the same line, different lengths | A continuous curve, different radii |

In Figma, with the node selected, the right panel shows the type and lets you change it.

!!! tip "Fewer nodes = a better curve"
    The illustrators' practical rule: **one node at every change of direction, not one more**. A perfect circle has 4 nodes, not 12. A curve with 20 nodes will always look "wobbly", no matter how much you adjust it.

    If a shape came out badly, it usually does not need adjusting — it needs redrawing with fewer nodes.

---

## The Pen tool

Press ++p++. Then:

| Action | Result |
|--------|--------|
| **Click** | Adds a corner node — a straight segment |
| **Click and drag** | Adds a smooth node — a curved segment; the drag length sets the curve radius |
| **Click on the first node** | Closes the shape |
| ++esc++ or ++enter++ | Ends an open shape |
| ++alt++ + click on a node | Turns a smooth node into a corner node |

### Editing an existing shape

Double-click the shape → you enter **vector edit mode**. Now:

- ++v++ (Move) moves individual nodes.
- ++p++ (Pen) adds new nodes on segments.
- The ++delete++ key removes a node and joins the neighbouring segments.
- The **Bend tool** (++shift+b++) curves a segment without adding nodes.

!!! warning "The Pen takes hours to learn, not minutes"
    Nobody draws well with the Pen on their first try. It is the one tool in Figma that requires muscle practice, not just understanding. Exercise 2 below exists exactly for that — do it three times, not once.

    The good news: for 90% of your real work you will use rectangles, circles and boolean operations, not the Pen.

---

## Stroke — the outline

Any vector shape can have a **Fill** and a **Stroke**, independently.

### Stroke properties

| Property | Options | When it matters |
|----------|---------|-----------------|
| **Weight** | Thickness in px | The consistency of an icon set |
| **Align** | `Inside`, `Center`, `Outside` | The final size of the shape |
| **Cap** | `None`, `Round`, `Square`, `Arrow` | The ends of open lines |
| **Join** | `Miter`, `Bevel`, `Round` | How corners look |
| **Dash** | Dash length / gap length | Dashed lines |

!!! note "Align changes the real size"
    A 100 × 100 px square with a 10 px stroke:
    - `Inside` → occupies exactly 100 × 100 px
    - `Center` → occupies 110 × 110 px (5 px outside on each side)
    - `Outside` → occupies 120 × 120 px

    If you align elements and one has an `Outside` stroke, it will look offset. For icons, use `Center` everywhere, consistently.

### Converting a stroke into a shape

Sometimes you need an outline to become a real shape (for example so you can scale it without it thickening). Menu: **Object → Outline stroke** (++ctrl+shift+o++).

!!! warning "The operation is not easily undone"
    After `Outline stroke` you can no longer change the weight — you now have an outline of the outline. Do it **at the end**, and keep a copy of the editable version.

---

## Boolean operations in depth

We touched on them in lesson 02. Now, the details that matter.

| Operation | Shortcut | Result |
|-----------|----------|--------|
| **Union** | ++ctrl+alt+u++ | The union of all the shapes |
| **Subtract** | ++ctrl+alt+s++ | The first shape minus all the ones above it |
| **Intersect** | ++ctrl+alt+i++ | Only the common area |
| **Exclude** | ++ctrl+alt+x++ | Everything except the common area |

!!! tip "Boolean operations stay editable"
    Unlike in other programs, in Figma a boolean group is **not destructive**: you can enter it (double-click) and move the component shapes at any time. The result recalculates.

    When you want to freeze it for good: **Object → Flatten** (++ctrl+e++). Do it only at export time.

### Order matters for Subtract

`Subtract` subtracts **the shapes above** from **the one beneath**. If the result is the opposite of what you expected, select the top shape and press ++ctrl+shift+bracket-left++ to send it back (or rearrange in the Layers panel).

---

## Build an icon set

A coherent icon set does not mean "pretty drawings". It means **rules applied identically** in every drawing.

### The set's rules

1. **A fixed grid.** All icons are drawn inside a square of the same size — the standard is **24 × 24 px**.
2. **A safe area.** The drawing occupies at most **20 × 20 px** of the 24; the rest is margin. That keeps icons from sticking to the text.
3. **A single weight.** All strokes share the same weight — usually **2 px** on a 24 grid.
4. **The same caps and joins.** `Cap: Round` and `Join: Round` everywhere, or `Square` everywhere. Not mixed.
5. **The same corner radius.** If one rectangle has a 2 px radius, they all have 2 px.
6. **Pixel alignment.** Coordinates are whole numbers. A 2 px line at X = 11.5 renders blurry.

!!! note "Why 24 × 24 and a 2 px stroke"
    24 divides by 2, 3, 4, 6, 8 and 12, so you can centre anything easily. A 2 px stroke stays crisp at 16 px (it scales to 1.33) and at 48 px (4 px). It is the standard used by Lucide, Feather and most modern libraries.

### The visual family

| Style | Appearance | When |
|-------|-----------|------|
| **Outline** | Outline only, no fill | Navigation, interfaces, inactive states |
| **Filled** | Solid fill | Active states, accents |
| **Duotone** | Outline + partial fill with opacity | Small illustrations, dashboards |

A professional set has **outline for everything** and, optionally, a filled variant for the "selected" state.

---

## SVG and exporting

**SVG** (Scalable Vector Graphics) is a text format — you can open it in an editor and read it.

```xml
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <circle cx="12" cy="12" r="10"/>
  <path d="M12 8v4l3 3"/>
</svg>
```

This is a clock icon: a circle and two lines (the hands). 150 bytes.

### Why `currentColor` matters

If the `stroke` attribute is `currentColor`, the icon **takes the surrounding text colour** through CSS. One icon works on both light and dark backgrounds, without exporting two files.

### Exporting from Figma

1. Select the icon (the 24 × 24 frame, not the shape inside).
2. In the right panel, at the bottom, under **Export**, press **+**.
3. Choose the **SVG** format.
4. Tick **Include "id" attribute** only if you need it; usually you do not.
5. **Export**.

!!! tip "Clean up the SVG"
    Figma exports SVG with extra attributes (`width`, `height`, hard-coded colours). For the web, run the file through [SVGOMG](https://jakearchibald.github.io/svgomg/) — it cuts the size by 30–60% and strips the junk.

    Then manually replace the hard-coded colour with `currentColor`.

---

## Exercises

### Exercise 1 — Three icons on the grid
Build, on a 24 × 24 px grid with a 2 px stroke, `Cap: Round`, `Join: Round`: a **house** icon, a **user** icon and a **settings** icon (a cog or three sliders). Use only primary shapes and boolean operations — no Pen.

??? success "Solution"
    **The house:** a triangle (Polygon with 3 sides) of 20 × 10 px for the roof, at the top; a 14 × 10 px rectangle underneath for the walls; a small 5 × 6 px rectangle for the door, centred at the bottom. All with Fill `none`, Stroke 2.

    **The user:** an 8 × 8 px circle for the head, centred at X = 12, Y = 8; below it a shoulders shape made from an 18 × 18 px circle with a rectangle covering the lower half subtracted (Subtract). The result is an arc.

    **The settings:** the simple three-slider version — three 18 px horizontal lines at Y = 7, 12, 17, plus three small 4 px circles sitting on them at different X positions (8, 15, 10). It is easier to build and more legible at 16 px than a toothed cog.

    **Consistency check:** place all three side by side at 24 px and then at 16 px. If one looks thicker or denser than the others, you broke one of the six rules.

### Exercise 2 — Pen Tool: trace a letter
Import into Figma a screenshot of the letter `S` from a serif font, 400 px tall. Lock the image (++ctrl+shift+l++), drop its opacity to 30% and trace the letter's outline with the Pen.

??? success "Solution"
    The method that works:

    1. Start with the nodes at the **curve extremes** — the topmost, bottommost, leftmost and rightmost points. For an `S` there are roughly 8 such points.
    2. At each one, **click and drag** along the tangent direction (horizontal at the top/bottom extremes, vertical at the left/right ones). The handles should be **horizontal or vertical**, not slanted.
    3. Do not add nodes "to make it come out better". If a curve is wrong, adjust the **handles** of the existing nodes.
    4. Close the shape on the first node.

    **Check:** hide the background image. Your letter must still look like a letter without the reference. If it has "bulges", you have too many nodes or slanted handles.

    Do the exercise three times, on different days. The difference between the first and the third attempt will be bigger than you expect.

### Exercise 3 — Three shapes from boolean operations
Build, using only rectangles and circles plus boolean operations: a **speech bubble** (with a tail), a **download icon** (a down arrow over a line) and a **location pin** (the map teardrop).

??? success "Solution"
    **The speech bubble:** a 20 × 14 px rectangle with a 4 px radius, plus a small 5 × 5 px triangle attached to the bottom-left edge. **Union**.

    **The download:** a 2 × 10 px vertical line, plus a 10 × 6 px triangle beneath it (Union for the arrow), plus a separate 16 × 2 px horizontal line at the bottom — this one stays separate, it is not merged.

    **The location pin:** a 14 × 14 px circle at the top, plus a 14 × 10 px triangle pointing down, overlapping by ~4 px. **Union** → the teardrop. Then a small 5 × 5 px circle at the centre of the round part, selected together with the shape → **Subtract** → the hole.

    **Observation:** none of the three required the Pen. That is the general rule — try primary shapes first, reach for the Pen only when there is genuinely no other way.

---

## Mini-project: an 8-icon set for the computer science club

Build a coherent set of **8 icons** at 24 × 24 px on club-related themes: `code`, `dev board`, `sensor`, `wifi`, `battery`, `soldering iron`, `calendar`, `user`. Export them as SVG.

??? success "Solution"
    **The setup:**
    1. Create a 24 × 24 px frame and rename it `icon/code`.
    2. Add a layout grid to it: `Grid`, size 1, a very discreet colour — it helps with pixel alignment.
    3. Draw inside the 20 × 20 px safe area (a 2 px margin on each side).
    4. Duplicate the frame (++ctrl+d++) for each new icon and rename.

    **Rules applied identically:** Stroke 2 px, `Align: Center`, `Cap: Round`, `Join: Round`, 2 px corner radius, whole-number coordinates.

    **A few constructions:**

    | Icon | Construction |
    |------|-------------|
    | `code` | Two pairs of lines forming `<` and `>`, plus a slanted line in the middle |
    | `dev board` | A 16 × 16 rectangle with a 2 px radius, plus 3 short lines on each side (the pins), plus a small 6 × 6 square in the centre (the chip) |
    | `wifi` | Three concentric arcs (circles with a rectangle subtracted for the lower half), plus a 2 px dot |
    | `battery` | An 18 × 10 rectangle with a 2 px radius, plus a 2 × 4 rectangle attached on the right (the terminal) |
    | `calendar` | An 18 × 16 rectangle with a 2 px radius, a horizontal line 4 px from the top, two short vertical lines above |

    **The export:**
    - Select all 8 frames.
    - **Export → SVG → Export 8 layers**. Figma saves them under the frame names.
    - Run the files through SVGOMG and replace the colour with `currentColor`.

    **The final coherence test:** line up all 8 at 24 px, then make a copy at 16 px and one at 48 px. In a good set, all eight appear to have the same "density" at every size. If one looks heavier, it has too much detail — simplify it.

---

## Summary

- **Vector** = formulas, scales perfectly; **raster** = pixels, pixelates.
- Logos and icons are **always** vector.
- A shape = **nodes** + **segments**; nodes can be corner, smooth or asymmetric.
- **Fewer nodes give better curves.** A circle has 4 nodes.
- Pen: **click** = corner, **click and drag** = curve. It is learned by repetition.
- `Stroke Align` changes the **real size** of the shape — use `Center` consistently.
- Booleans: **Union, Subtract, Intersect, Exclude** — they stay editable until `Flatten`.
- Icons: a **24 × 24** grid, a **20 × 20** safe area, a **2 px** stroke, identical caps and joins.
- **SVG** with `currentColor` works on any background; clean it with SVGOMG.

---

**Next step:** [→ Lesson 08: Styles and components](08-stiluri-si-componente.md)
