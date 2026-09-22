---
lesson: 5
tags: [composition, grid, alignment, spacing, layout]
summary: Alignment, proximity, the 12-column grid, the 8 px spacing system, the rule of thirds and how to set all of it up in Figma.
---

# Lesson 05 · Composition and grid

!!! tip "What you will learn"
    - Why **alignment** is the visible difference between amateur and professional
    - **Proximity**: how to group information without drawing anything
    - The **8 px spacing system** and why all your numbers should be multiples
    - The **12-column grid** and how to set it up in Figma
    - The **rule of thirds** and the golden section, with the necessary reservations
    - How to lay out a poster from scratch, step by step

---

## Alignment

The rule: **every element must have a visual connection to another one on the page.** Nothing sits "wherever it landed".

```
    BAD                          GOOD
┌──────────────┐            ┌──────────────┐
│  Title       │            │ Title        │
│      Subtitle│            │ Subtitle     │
│   Text text  │            │ Text text    │
│        text  │            │ text         │
│ Button       │            │ Button       │
└──────────────┘            └──────────────┘
  4 different edges           1 shared edge
```

In the left version, the eye hunts every time for where the next line starts. On the right there is an **invisible line** they all sit on — and the eye follows it effortlessly.

### Which alignment to pick

| Alignment | When | Avoid for |
|-----------|------|-----------|
| **Left** | Almost always. Text, lists, forms | — |
| **Centred** | Short headings (1–2 lines), invitations, diplomas | Long paragraphs |
| **Right** | Numbers, prices, dates in tables | Text meant to be read |
| **Justified** | Newspapers, books with wide columns | Narrow columns (creates "rivers") |

!!! warning "Centring is the beginner's trap"
    Centring feels "balanced" and "safe". In fact, a fully centred poster is the fastest way to look amateurish: no shared edge, no structure, everything floats.

    **The rule:** centre **at most one block** on the page, usually the heading. Left-align the rest.

### How to align in Figma

Select two or more elements. In the right panel, at the top, six buttons appear: align left / horizontal centre / right, top / vertical centre / bottom.

The **Tidy up** button (appears when you select 3+ elements) aligns them **and** spaces them evenly, in one click.

!!! tip "Optical vs. mathematical alignment"
    Sometimes an element aligned perfectly by the numbers **looks** misaligned. This happens with round shapes and triangles: a circle aligned to the same X coordinate as a square looks slightly further right, because its edge curves away.

    Likewise, a "play" button (a triangle) inside a circle has to be moved 1–2 px right to **look** centred. The eye is right, not the ruler.

---

## Proximity

Elements close together form a group. The practical consequence: **the space between related things must be smaller than the space to everything else**.

```
BAD                           GOOD

Name                          Name
                              Ana Popescu
Ana Popescu
                              Class
Class                         9B

9B
```

On the left, every label is closer to *someone else's* value than to its own. The reader has to guess what goes with what.

!!! note "The 1:2 rule"
    The space **inside** a group should be about **half** the space **between** groups.

    Example: if you put 8 px between a label and its value, put 16–24 px between two label-value pairs. The difference is small, but it makes the grouping obvious without a single line.

---

## The spacing system

All your spacing values should come from a fixed set. The most used system: **multiples of 8**.

| Step | Value | Use |
|------|-------|-----|
| 1 | 4 px | Between an icon and its label |
| 2 | 8 px | Between a label and its value |
| 3 | 16 px | Button padding, between related elements |
| 4 | 24 px | Between small groups |
| 5 | 32 px | Card padding |
| 6 | 48 px | Between sections |
| 7 | 64 px | Between large blocks |
| 8 | 96 px | Page margins, major separations |

!!! note "Why 8 and not 10"
    8 divides by 2 and by 4 without decimals, and most screens work at densities that are multiples of 2. A padding of 15 px becomes 15.5 px on a retina screen, and Figma and the browser round it differently — you get 1 px lines that appear and disappear as you zoom.

!!! warning "'Almost right' numbers are the most visible sign of amateurism"
    Padding 13 px in one place, 15 px in another, 17 px in a third. Nobody can say what is wrong, but everyone feels that something is. Round **everything** to multiples of 8 (or of 4 for small values).

---

## The grid

A grid is a set of invisible columns that give the page structure. Nobody sees it in the final result, but it decides where things sit.

### The 12-column grid

12 is the standard number because it divides nicely: 12 = 2×6 = 3×4 = 4×3 = 6×2. You can build layouts with 2, 3, 4 or 6 equal columns from the same grid.

```
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │

│      3 columns       │      (4+4+4)          │
│         2 columns (6+6)                      │
│  4 columns (3+3+3+3)                         │
```

### The terms

| Term | What it is | Typical value |
|------|-----------|---------------|
| **Column** | The area the content sits in | Variable width |
| **Gutter** | The space between columns | 16–32 px |
| **Margin** | The space from the page edge | 24–96 px |

### How to set up the grid in Figma

1. Select the frame.
2. In the right panel, under **Layout grid**, press **+**.
3. In the dropdown, change `Grid` to **`Columns`**.
4. Set: **Count** 12, **Type** `Stretch`, **Margin** 64, **Gutter** 24.
5. Toggle grid visibility with ++ctrl+shift+4++ (Windows) or ++ctrl+g++ (macOS — the `control` key, not `cmd`).

!!! tip "Different grids for different devices"
    - **Phone** (390 px): 4 columns, margin 16, gutter 16
    - **Tablet** (768 px): 8 columns, margin 32, gutter 24
    - **Desktop** (1440 px): 12 columns, margin 96, gutter 24

    You will use these in lesson 14, when you design interfaces.

### The baseline grid

For print you add a second, **horizontal** grid, with a step equal to the body text's line height (e.g. 24 px). Every line of text in every column sits on it. It is what makes a magazine look tidy.

In Figma: add another **Layout grid**, type `Rows`, `Count: Auto`, `Height: 24`.

---

## The rule of thirds

Divide the page into 3 × 3 with two vertical and two horizontal lines. Place the important elements **on the lines** or **at the intersection points**, not in the exact centre.

```
┌───────┬───────┬───────┐
│       │       │       │
├───────●───────●───────┤   ● = strong points
│       │       │       │
├───────●───────●───────┤
│       │       │       │
└───────┴───────┴───────┘
```

It is inherited from photography and works because a slightly off-centre element creates tension and movement, while the exact centre is static.

!!! note "The golden section — with reservations"
    You will often hear about the golden ratio (1:1.618) presented as "the secret law of beauty". The truth is more modest: it is a pleasant ratio, but it is **not** a law and it does not explain why a design works.

    The rule of thirds (1:2) is simpler, gives very similar results and requires no arithmetic. Use that one.

---

## How to build a composition, step by step

Do not start by drawing. Start by ordering.

### Step 1 — List the content and rank it

Write down everything that has to appear and number it in order of importance. For an event poster:

1. The event title
2. The date
3. Time and place
4. The short description
5. Who organises it
6. Details (entry, contact, website)

### Step 2 — Group

How many groups result? Ideally **3–5**. If you have 9 groups, the reader has no way of knowing where to start.

For the example above: `[title]`, `[date + time + place]`, `[description]`, `[organiser + details]`. Four groups.

### Step 3 — Pick a structure

| Structure | What it looks like | Good for |
|-----------|-------------------|----------|
| **Single column** | Everything vertical, left-aligned | Simple posters, posts |
| **Two columns** | Image / text, or content / details | Leaflets, web pages |
| **Z pattern** | The eye goes top-left → top-right → bottom-left → bottom-right | Posters with few elements |
| **F pattern** | Horizontal scanning, decreasing | Web pages with a lot of text |
| **Modular** | Cards in a grid | Portfolios, galleries, dashboards |

### Step 4 — Place on the grid and check

- Does every element start on a grid column?
- Is every space a multiple of 8?
- Is the space inside groups smaller than the space between groups?
- Is the most important element also the most visible?

### Step 5 — The blur test

Apply a strong blur (lesson 02). Do you see 3–5 blobs, with the strongest on the most important information? If so, the composition is done.

---

## Exercises

### Exercise 1 — Fix the alignment
In a 600 × 800 px frame, deliberately place 6 text elements at slightly offset positions (all at different X coordinates: 40, 47, 52, 41, 58, 45). Then fix it.

??? success "Solution"
    The fix has one real step: select all 6 texts and press **Align left**. They all move to X = 40 (the coordinate of the leftmost one).

    Comparing before and after, the difference is enormous, even though the largest move was 18 px. That is proof that **alignment is more visible than you think** — including when it is off by very little.

    Extra check: set the vertical spacing between them to multiples of 8 (8 inside groups, 24 between groups) using **Tidy up** or Auto layout.

### Exercise 2 — Grouping through proximity
In a 400 × 500 px frame, place 8 lines of text — 4 label/value pairs — without drawing a single line and without using different colours. The reader must instantly see 4 groups.

??? success "Solution"
    The settings that solve it:

    - Label: 13 px, Medium, colour `#6B7280`, all caps, tracking +8%.
    - Value: 18 px, Regular, colour `#111827`.
    - Space label → value: **4 px**.
    - Space between pairs: **24 px**.

    The ratio 4 : 24 = 1 : 6 makes the grouping obvious immediately. Even 8 : 24 (1 : 3) works.

    What does **not** work: 12 px of space everywhere. Then you have 8 equal lines, not 4 groups, and the reader has to read carefully to understand the structure.

### Exercise 3 — A 12-column grid
Set up a 12-column grid on a Desktop frame (1440 × 1024) and place three equal cards on it, then rearrange the same cards into two unequal columns (8 + 4).

??? success "Solution"
    **The grid:** Layout grid → Columns → Count 12, Type `Stretch`, Margin 96, Gutter 24.
    A column's width follows automatically: (1440 − 2×96 − 11×24) / 12 = **62 px**.

    **Three equal cards:** each spans 4 columns → width = 4×62 + 3×24 = **320 px**. Place them at X = 96, 440, 784.

    **The 8 + 4 layout:** the main card spans 8 columns → 8×62 + 7×24 = **664 px**. The side card spans 4 columns → **320 px**, at X = 96 + 664 + 24 = 784.

    Notice that you **did not eyeball anything**. Every width follows from the grid. That is why you use it: it removes arbitrary decisions.

---

## Mini-project: the same content, three compositions

Take the content of the typographic poster from lesson 04 and build **three different compositions** with exactly the same text: one in a **single column**, one in a **Z pattern**, one **modular** (cards). Same palette, same fonts, same hierarchy.

??? success "Solution"
    **Single column (A3):** a 12-column grid, all content on columns 1–9, left-aligned. Title at the top, then the date, then the description, details at the bottom. Spacing: 16 px within groups, 48 px between them. **The safest version** — hard to break, easy to read.

    **Z pattern (A3 landscape):** the label top-left, the title top-right, the description bottom-left, the large date bottom-right. The eye naturally travels a Z. It works **only** with little content — at most 4 blocks. With 6 blocks it falls apart.

    **Modular (A3):** a 12 × 12 grid; four cards with a `#1E293B` background, 16 px corners, 32 px padding. The title card spans 12 columns × 4 rows; the date 6 × 3; the place 6 × 3; the details 12 × 2. It looks like a dashboard. Good when the information is "data"-like, weak when you want emotional impact.

    **The conclusion:** identical content produces three completely different impressions. Composition is not "the arrangement at the end" — it is a communication decision, exactly like choosing a colour.

    **Check all three:** apply the blur. In every case, the darkest blob should be the title. If in one of the versions the date comes out stronger than the title, you changed the hierarchy without meaning to.

---

## Summary

- **Alignment:** every element connects visually to another. Default — left.
- Centring is used for **at most one block** per page.
- **Proximity:** the space inside a group ≈ half the space between groups.
- All spacing values are **multiples of 8** (or of 4 for small values).
- The **12-column grid** divides into 2, 3, 4 and 6 — that is why it is the standard.
- Grid terms: **column, gutter, margin**.
- **Rule of thirds** > golden section: simpler, similar result.
- You build in 5 steps: **list → group → pick a structure → place on the grid → test with blur**.
- Ideally **3–5** visual groups per page.

---

**Next step:** [→ Lesson 06: Visual hierarchy](06-ierarhie-vizuala.md)
