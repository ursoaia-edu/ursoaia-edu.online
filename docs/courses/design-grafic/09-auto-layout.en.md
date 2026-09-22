---
lesson: 9
tags: [figma, auto layout, flexbox, spacing, responsive]
summary: Automatic arrangement, direction, spacing and padding, resizing behaviour and how Auto Layout maps onto CSS Flexbox.
---

# Lesson 09 · Auto Layout

!!! tip "What you will learn"
    - What **Auto Layout** is and which problem it solves
    - **Direction**, **gap** and **padding**
    - **Alignment** inside the container and `Space between`
    - **Hug**, **Fill** and **Fixed** — the three resizing behaviours
    - **Nested** Auto Layout, the most important concept of the lesson
    - How all of it translates into **CSS Flexbox**

---

## The problem

You have a button labelled "Save". You make it look good: centred text, 16 px of space around it. Then you change the label to "Save all changes".

Without Auto Layout: the text overflows the button. You resize the button by hand, recentre the text, check the spacing. Then you change the label once more.

With Auto Layout: the button grows by itself. The space stays exactly 16 px.

The same problem shows up in any list you add items to, any card with variable-length text, any menu. **Auto Layout is what turns a static drawing into a structure.**

---

## The basics

### How to apply it

Select one or more elements and press ++shift+a++. A frame with Auto Layout is created around them.

To remove it: ++shift+alt+a++.

### The four basic settings

A new **Auto layout** section appears in the right panel:

| Setting | What it does | Values |
|---------|--------------|--------|
| **Direction** | The orientation | Vertical ↓, Horizontal →, Wrap |
| **Gap** | The space between elements | A number, or `Auto` |
| **Padding** | The inner space, from the edges | One number, or 4 separate |
| **Alignment** | How elements sit in the container | A 9-point grid |

```
┌─────────────────────────────┐
│  padding-top                │
│  ┌───────┐ gap ┌───────┐    │  padding-right
│  │  el 1 │─────│  el 2 │    │
│  └───────┘     └───────┘    │
│  padding-bottom             │
└─────────────────────────────┘
   padding-left
```

!!! tip "Separate paddings"
    Click the four-sided icon next to the padding field → it splits into four fields: top, right, bottom, left. A button usually has more horizontal than vertical padding (e.g. 24 horizontal, 12 vertical) — it looks better balanced.

### Space between

If you set **Gap** to `Auto` (the opposing-arrows icon), the elements push to the edges of the container and the space is distributed between them. This is exactly what you need for a navigation bar: logo on the left, menu on the right.

```
┌────────────────────────────────────────┐
│ [logo]                     [menu] [cta]│
└────────────────────────────────────────┘
   gap = Auto
```

---

## Resizing behaviour

This is the part that confuses everyone at first. Every element inside an Auto Layout has two independent settings — one for width, one for height.

| Behaviour | Icon | What it does |
|-----------|------|--------------|
| **Hug contents** | Arrows pointing inwards | The container shrinks exactly onto its content |
| **Fill container** | Arrows pointing outwards | The element stretches over all available space |
| **Fixed** | A number | A fixed size, never changes |

### The practical rules

| Element | Width | Height | Why |
|---------|-------|--------|-----|
| Button | Hug | Hug | Grows with the label |
| Full-width button | Fill | Hug | Takes the card's width, height follows the text |
| Card in a grid | Fill | Hug | Width comes from the grid, height from the content |
| Text in a card | Fill | Hug | It wraps and grows downwards |
| Icon | Fixed | Fixed | 24 × 24, always |
| Screen / page | Fixed | Fixed or Hug | The format is given |

!!! warning "`Fill` only works inside an Auto Layout"
    If the `Fill container` option is greyed out, the element is **not** inside an Auto Layout frame. Apply Auto Layout to the parent first.

!!! note "Hug + text = the most useful pairing"
    A card with `Fill` width and `Hug` height, containing a text with `Fill` width and `Hug` height: if the text is 2 lines, the card is short; if it is 6 lines, the card grows. You touch nothing.

---

## Nested Auto Layout

This is where all the power lies. An Auto Layout frame can contain other Auto Layout frames.

A real project card:

```
card/project                    ← vertical Auto Layout, gap 16, padding 24
├── header                      ← horizontal Auto Layout, gap 12, Fill
│   ├── ◇ icon (24×24)          ← Fixed
│   └── title                   ← Fill
├── description                 ← Fill / Hug
└── footer                      ← horizontal Auto Layout, gap Auto, Fill
    ├── tags                    ← horizontal Auto Layout, gap 8, Hug
    │   ├── badge
    │   └── badge
    └── button                  ← Hug
```

Four levels of Auto Layout. The result: you change the title, the description, the number of badges or the button label, and the card rearranges correctly every time, without you touching anything.

!!! tip "Build from the inside out"
    Do not try to build the structure top-down. Make the small groups first (the badges, then the row of badges), apply Auto Layout to them, then group those into bigger rows, then into the card.

    ++shift+a++ on the small group, ++shift+a++ on the bigger group, and so on.

### Rename the frames

Nested Auto Layout with layers named `Frame 12`, `Frame 13`, `Frame 14` becomes impossible to maintain. Name them by role: `header`, `content`, `footer`, `tags`, `actions`.

---

## Advanced settings

### Absolute position

Sometimes you want an element **inside** an Auto Layout that does not take part in the arrangement — for example a notification dot over an avatar, or a "New" tag in a card's corner.

Select the element → the right panel shows an icon of a square with a dot in the corner → **Absolute position**. The element leaves the flow and you position it freely, while staying a child of the container.

### Canvas stacking

When elements overlap (for example cascading avatars with a negative gap), the **Canvas stacking** setting decides which one is on top: the first or the last.

### Strokes: included / excluded in layout

By default Figma does **not** count stroke weight in spacing calculations. If you work with outlined buttons and want them to align perfectly with unoutlined ones, switch to `Strokes: included in layout`.

### Wrap

The third direction, **Wrap**, makes elements move to the next line when they no longer fit. Useful for tag lists or galleries that have to adapt to different widths.

---

## The link to CSS

Auto Layout is essentially **CSS Flexbox** with a different interface. If you took the Web course, this is familiar.

| Figma | CSS |
|-------|-----|
| Auto layout | `display: flex` |
| Direction: Horizontal | `flex-direction: row` |
| Direction: Vertical | `flex-direction: column` |
| Direction: Wrap | `flex-wrap: wrap` |
| Gap | `gap` |
| Padding | `padding` |
| Gap: Auto | `justify-content: space-between` |
| Alignment (the 9-point grid) | `justify-content` + `align-items` |
| Fill container | `flex: 1` |
| Hug contents | `width: fit-content` / default size |
| Fixed | `width: 320px` |
| Absolute position | `position: absolute` |

!!! note "Why it matters"
    When you hand a design to a developer (or build it yourself, in lesson 14), a layout made with Auto Layout translates **directly** into CSS. A layout made from manually positioned elements has to be reinterpreted, and reinterpretation introduces differences.

    See [lesson 08 of the Web course](../web/08-css-flexbox-grid.md) for the CSS side.

---

## Common mistakes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Text overflows the button | The button is `Fixed` in width | Set width to `Hug` |
| The card does not grow with the text | Height is `Fixed` | Set height to `Hug` |
| `Fill` is greyed out | The parent has no Auto Layout | ++shift+a++ on the parent |
| Spacing looks uneven | Some elements have their own margins | Delete the margins, use gap |
| An element "jumps" when resizing | It has `Absolute position` without constraints | Set the constraints in the right panel |
| Everything collapses into a thin column | The container is `Hug` in width when it should be `Fixed` | Set the container width |

!!! warning "Do not mix Auto Layout with manual positioning"
    If half a card is arranged with Auto Layout and half with elements nudged by hand, the manual half breaks at the first content change. **All or nothing**, at every level.

---

## Exercises

### Exercise 1 — A button that grows
Build a button with Auto Layout: 12 vertical / 24 horizontal padding, gap 8, with a 16 px icon and a label. Test it with the labels `OK`, `Save` and `Save all changes`.

??? success "Solution"
    1. Write the label, place the icon next to it.
    2. Select both → ++shift+a++.
    3. Direction: **Horizontal**, Gap: **8**, Padding: **12 / 24**.
    4. Alignment: **centre-left** (the middle-left point of the 9-point grid).
    5. Width and height: both on **Hug**.
    6. Add a `brand/primary` fill and an 8 radius.

    Now change the label three times. The button changes width, the icon stays 8 px from the text, the padding stays 24. You touched nothing.

    **The mistake to check for:** if you left the icon on `Fill` instead of `Fixed`, it will stretch unpleasantly on short labels. Icons are always `Fixed`.

### Exercise 2 — A navigation bar
Build a 1440 px wide navigation bar with: the logo on the left, four links towards the right and a button at the far right. It must work correctly at 1024 px too.

??? success "Solution"
    **The structure:**

    ```
    navbar                  ← horizontal Auto Layout, gap Auto,
    │                          padding 0/32, width Fixed 1440, height Hug
    ├── logo                ← Hug
    └── right               ← horizontal Auto Layout, gap 32, Hug
        ├── links           ← horizontal Auto Layout, gap 24, Hug
        │   ├── link × 4
        └── ◇ button        ← Hug
    ```

    **The steps:**
    1. Make the 4 links, select them → ++shift+a++ → horizontal, gap 24. Rename `links`.
    2. Select `links` + the button → ++shift+a++ → horizontal, gap 32. Rename `right`.
    3. Select the logo + `right` → ++shift+a++ → horizontal, **gap Auto**. Rename `navbar`.
    4. Set `navbar` width to 1440, horizontal padding 32, vertical alignment centred.

    **The test:** change the `navbar` width to 1024. The logo stays pinned left, the right group stays right, and the space between them shrinks. Exactly as it should.

    **Without gap Auto:** you would have had to move the right-hand group by hand at every width change.

### Exercise 3 — A card with nested Auto Layout
Build the project card from the diagram above (four levels). Test it with a 2-word title and an 8-word title, with 1 badge and with 4 badges.

??? success "Solution"
    **Building it, from the inside out:**

    1. **Badge:** text + Auto Layout, padding 4/10, radius 4, Hug/Hug.
    2. **Tags:** select 2 badges → ++shift+a++ → horizontal, gap 8, Hug.
    3. **Footer:** select `tags` + the button → ++shift+a++ → horizontal, **gap Auto**, width **Fill**.
    4. **Header:** icon (Fixed 24×24) + title (Fill) → ++shift+a++ → horizontal, gap 12, width Fill, alignment centred vertically.
    5. **Card:** select `header` + description + `footer` → ++shift+a++ → vertical, gap 16, padding 24, width **Fill**, height **Hug**.

    **The tests:**
    - An 8-word title → wraps onto 2 lines, the header grows, the card grows, the footer moves down. Correct.
    - 4 badges → the tags row widens; if it exceeds the space, switch `tags` to the **Wrap** direction.
    - The card placed in a 3-column grid with different widths → each card adjusts its height to its content.

    **Final check:** put three cards in a horizontal Auto Layout with gap 24, each on `Fill`. All three get the same width automatically. Change the container width and the three adapt together.

---

## Mini-project: a complete app screen with Auto Layout

Build a **390 × 844 px** screen (iPhone 14) for a computer science club app: a header with title and avatar, a list of 5 projects (cards), and a bottom navigation bar with 4 icons. **Everything** must be Auto Layout — zero manually positioned elements.

??? success "Solution"
    **The structure:**

    ```
    screen                        ← Fixed 390 × 844, vertical Auto Layout, gap 0
    ├── header                    ← horizontal, gap Auto, padding 16/20, Fill
    │   ├── title                 ← Hug
    │   └── ◇ avatar (40×40)      ← Fixed
    ├── content                   ← vertical, gap 12, padding 20, Fill / Fill
    │   └── ◇ card/project × 5    ← each Fill / Hug
    └── tabbar                    ← horizontal, gap Auto, padding 12/24, Fill
        └── ◇ tab-item × 4        ← each Hug
    ```

    **The details that matter:**

    - `content` has its height on **Fill** — it takes all the space left between the header and the tab bar. That single setting is what keeps the bottom bar pinned to the screen edge no matter how many cards you have.
    - Each `tab-item` is a vertical Auto Layout with a 24 px icon + a 10 px label, gap 4, centred alignment.
    - `tabbar` uses **Auto** gap — the 4 items distribute evenly across the width.
    - The cards are instances of the component from exercise 3.

    **The final tests:**

    | Test | Correct result |
    |------|----------------|
    | Delete 2 cards | The remaining 3 move up; the tab bar stays at the bottom |
    | Add 3 cards | The list grows; the content exceeds the screen (normal — it will scroll) |
    | Change the screen width to 320 | All cards narrow; nothing overflows |
    | Change a card's title to a long one | The card grows taller, the ones below move down |
    | Change `content` padding from 20 to 24 | All cards narrow by 8 px, uniformly |

    **The pass criterion:** if in any of the five tests you had to move something by hand, somewhere in the structure there is an element that is not in Auto Layout or is `Fixed` where it should be `Fill`.

---

## Summary

- **Auto Layout** (++shift+a++) turns a drawing into a structure that adapts to its content.
- Four basic settings: **direction, gap, padding, alignment**.
- **Gap: Auto** = `space-between` — elements push to the edges.
- Three behaviours: **Hug** (shrink onto content), **Fill** (take the space), **Fixed** (a fixed size).
- Icons are **always Fixed**; texts are usually **Fill / Hug**.
- **Nested Auto Layout** is what makes a real card work; build **from the inside out**.
- **Absolute position** takes an element out of the flow without taking it out of the container.
- Auto Layout ≈ **CSS Flexbox**; a design built this way translates straight into code.
- Do not mix Auto Layout with manual positioning at the same level.

---

**Next step:** [→ Lesson 10: Images, masks and export](10-imagini-masti-export.md)
