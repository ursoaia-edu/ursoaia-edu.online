---
lesson: 2
tags: [design, shape, line, white space, gestalt]
summary: The basic elements of any composition — line, shape and empty space — plus the Gestalt laws that explain why the eye groups things.
---

# Lesson 02 · Shape, line, space

!!! tip "What you will learn"
    - What a **line** communicates and how to use it properly
    - The three **primary shapes** and the association each carries
    - Why **empty space** is the most underrated design element
    - **Visual weight**: why a small element can weigh more than a big one
    - The **Gestalt** laws — how the eye groups automatically
    - How to build complex shapes from simple ones in Figma

---

## The line

A line does three things: it **separates**, it **connects** or it **guides the eye**. Nothing else. If a line in your composition does none of these three, take it out.

### What direction communicates

| Direction | Feeling | Where you use it |
|-----------|---------|------------------|
| Horizontal | Calm, stability, rest | Separators between sections |
| Vertical | Strength, formality, height | Accent bars, columns |
| Diagonal | Movement, energy, tension | Sports posters, dynamic elements |
| Curved | Softness, natural, organic | Illustrations, "warm" brands |

### Thickness matters

A 1 px line says "a section ends here". An 8 px line says "look here". The practical rule:

- **Separators:** 1 px, a very discreet colour (light grey on white, `rgba(255,255,255,0.08)` on a dark background).
- **Accents:** 4–8 px, the main identity colour.
- **Title underlines:** 3–4 px, 40–60 px wide, not the full width of the title.

!!! warning "The too-visible separator mistake"
    A beginner draws separators in 2 px black. The result: the lines shout louder than the content. A good separator is **barely visible** — the eye feels it, it does not notice it.

!!! note "The invisible line"
    The most powerful line in a design is often **the one you do not draw**: the shared edge several elements are aligned to. The eye completes it by itself. More in lesson 05.

---

## Shape

Three primary shapes, three associations. They are learned at an early age and work across almost all cultures.

| Shape | Association | Real examples |
|-------|-------------|---------------|
| **Square / rectangle** | Stability, order, trust, seriousness | Banks, institutions, app windows |
| **Circle** | Unity, community, movement, friendliness | Social networks, avatars, play buttons |
| **Triangle** | Direction, tension, hierarchy, attention | Hazard signs, play buttons, arrows |

!!! note "Why the hazard sign is a triangle"
    A triangle has a vertex. The vertex is a direction, and direction forces attention. A circle has no direction — that is why you will never see a round warning sign pointing up.

### Rounded corners

The corner radius (`corner radius` in Figma) changes the tone without changing the shape:

| Radius | Tone | Typical use |
|--------|------|-------------|
| 0 px | Severe, technical, precise | Tables, data interfaces, print |
| 4–8 px | Neutral, modern | Buttons, form fields, cards |
| 16–24 px | Friendly, soft | Apps for children, "warm" brands |
| 50% (pill) | Very friendly, playful | Labels, badges, action buttons |

!!! tip "Radius consistency"
    Pick **at most two radii** for the whole project: one for small elements (8 px) and one for large containers (16 px). A design with five different radii looks careless, even if nobody can say exactly why.

### Complex shapes from simple ones

Almost any icon is built from rectangles and circles, using **boolean operations**. In Figma, with two shapes selected, the button in the top bar gives you:

| Operation | Result |
|-----------|--------|
| **Union** | Merges the shapes into one |
| **Subtract** | Subtracts the top shape from the one beneath |
| **Intersect** | Keeps only the common area |
| **Exclude** | Keeps everything except the common area |

Example: a **crescent moon** = a circle minus another circle, offset. An **arrow** = a rectangle plus a triangle, merged.

---

## Empty space

Empty space (**white space** — it is called that even when the background is black) is not "unused" space. It is what makes the rest legible.

### What empty space does

1. **Separates** groups of information without needing lines.
2. **Creates hierarchy** — whatever has space around it looks important.
3. **Rests the eye** — a dense design is tiring and gets abandoned.
4. **Signals quality.** It is no accident that ads for expensive products carry a lot of emptiness; high density is associated with discounts and urgency.

!!! note "The squint test"
    Squint until the text becomes illegible. What remains are **grey blobs** — the content blocks. If the blobs are glued together, you have too little space. If you clearly see separate groups, the spacing is good.

### Micro-space and macro-space

- **Micro-space:** between letters, between lines, between a button and its label. Affects legibility.
- **Macro-space:** between sections, around the page, between columns. Affects structure.

A design can have generous macro-space and bad micro-space (text crammed into buttons) and still look unprofessional.

### The page margin

The minimum rule for a poster: **the margin never drops below 5% of the short side**.

| Format | Short side | Minimum margin |
|--------|-----------|----------------|
| A4 (210 × 297 mm) | 210 mm | ~10 mm |
| A3 (297 × 420 mm) | 297 mm | ~15 mm |
| Instagram post (1080 px) | 1080 px | ~54 px |

!!! warning "The trim zone in print"
    When you send a poster to a print shop, the paper is cut with a 2–3 mm tolerance. If the text sits 5 mm from the edge, you risk having it cut off. Keep text at **at least 10 mm** from the physical edge.

---

## Visual weight

Every element "weighs" something on the page. Weight is not only given by size:

| Factor | Increases weight |
|--------|------------------|
| Size | A bigger element |
| Colour | Saturated, warm colours (red, orange) |
| Contrast | A big difference from the background |
| Isolation | An element on its own, with a lot of space around |
| Complexity | A photo weighs more than a flat rectangle |
| Position | The top and the right feel "heavier" |

!!! note "Why a small red dot beats a big grey rectangle"
    A 20 px red circle on a white background catches the eye before a 400 px grey rectangle. Contrast and saturation beat size. That is exactly why the notification dot on app icons works.

### Balance

- **Symmetrical** — the same weight left and right. Formal, calm, sometimes boring. Suitable for diplomas and official invitations.
- **Asymmetrical** — different weights, balanced through position and space. Dynamic, modern. A large element on the left is balanced by a small but intensely coloured one at the bottom right.

---

## The Gestalt laws

Gestalt is a set of observations about how the human brain groups visual elements, **automatically, before conscious thought**. Five of them are useful to you daily.

### 1. Proximity

Elements close together look like a group. It is the most powerful organising tool you have.

```
●  ●        ●  ●          ●  ●  ●  ●  ●  ●

two groups                one single group
```

### 2. Similarity

Elements that look alike (same colour, shape, size) look like they belong to the same category — even when they are far apart.

### 3. Closure

The brain completes incomplete shapes. That is why a logo made of three arcs reads as a circle.

### 4. Continuity

The eye follows lines and curves. Elements aligned along a direction read as a sequence, not as separate things.

### 5. Figure and ground

The eye automatically separates "object" from "background". Some images exploit the ambiguity: in the WWF logo, the white space between the black patches forms the panda.

!!! tip "How to use Gestalt in practice"
    When a design looks messy, ask yourself: **what groups should the reader see?** Then move the elements of the same group closer and push the groups apart. This usually solves 80% of the problem without adding anything.

---

## Exercises

### Exercise 1 — Three separators
In an 800 × 400 px frame on a white background, draw three horizontal separators: one correct (discreet), one too thick and one too colourful. Look at them from 2 metres away.

??? success "Solution"
    - **Correct:** 1 px line, colour `E5E7EB`, the full width of the content.
    - **Too thick:** 4 px, black — it becomes the main element although it is only a separator.
    - **Too colourful:** 2 px red — the eye goes to it before the text.

    From 2 metres the first one disappears (exactly what you want: you feel it as structure), the other two jump out. A separator that shows more than the content is a hierarchy mistake.

### Exercise 2 — Three icons from simple shapes
Build, using only rectangles and circles plus boolean operations: a **crescent moon**, a **right-pointing arrow** and a **"forbidden" sign** (a circle with a diagonal bar).

??? success "Solution"
    **The moon:** two 100 × 100 px circles overlapping, the second offset 25 px to the right. Select both → **Subtract**. The top circle subtracts from the bottom one.

    **The arrow:** an 80 × 12 px rectangle (the body) plus a 32 × 32 px triangle attached to the right end. The triangle is made with the Polygon tool (set to 3 sides) rotated 90°. Select both → **Union**.

    **The forbidden sign:** a 100 × 100 px circle with **Fill: none** and **Stroke: 10 px red**, plus a 100 × 10 px red rectangle rotated 45° and centred. Group them with ++ctrl+g++.

    Note: in all three cases you worked with primary shapes. Almost every icon you see daily is built this way.

### Exercise 3 — The squint test
Take a poster or a post made by someone else, screenshot it, drop it into Figma and apply a strong blur on top (**Effects → Layer blur → 12**). How many distinct groups do you see?

??? success "Solution"
    After the blur you should make out **3–5 blobs**: the title, the main information, the details, possibly the image and the logo.

    - If you see **one single big blob**, the spacing is insufficient — the groups do not separate.
    - If you see **more than 8 blobs**, the design is fragmented; the reader does not know where to start.
    - If the darkest blob **is not** the most important information, the hierarchy is wrong.

    The blur trick is the fastest composition test you have. You will reuse it in every project.

---

## Mini-project: a poster with no text

Build an A4 frame that communicates the idea of "**movement**" using **only** lines and geometric shapes. No text, no images, at most two colours plus the background.

??? success "Solution"
    One direction that works:

    1. A4 frame, Fill `FFFFFF`.
    2. Seven parallel diagonal lines at 45°, thickness growing from 2 px to 14 px, spaced 24 px apart. Colour `1F2937`.
    3. A 120 px circle, Fill `F97316`, placed at the top right, right over the thick lines.
    4. Margins: at least 30 px from the page edge, everywhere.

    **Why it communicates movement:** the diagonal is the direction that suggests travel; growing thickness creates acceleration (the eye reads thin-to-thick as slow-to-fast); the orange circle is the "object" that moves, and its position at the top right gives it somewhere to arrive.

    **Versions that do not work:**
    - All lines the same thickness → repetition, not movement.
    - Horizontal lines → calm, the exact opposite.
    - Five colours → the eye can no longer tell object from background.

    **Extension:** make a second version with the same elements, but communicating "**calm**". You will see that you only change the direction of the lines and the saturation of the colour — the rest can stay identical.

---

## Summary

- A line **separates, connects or guides**. Otherwise, remove it.
- Good separators are barely visible; accents are thick and coloured.
- **Square** = stability, **circle** = unity, **triangle** = direction.
- At most **two corner radii** across the whole project.
- Complex shapes are built from simple ones with **Union, Subtract, Intersect, Exclude**.
- **Empty space** is not wasted space — it creates groups, hierarchy and the impression of quality.
- Minimum margin: **5% of the short side**; in print, at least 10 mm.
- Visual weight comes from size, **colour, contrast, isolation, complexity and position**.
- Gestalt: **proximity, similarity, closure, continuity, figure-ground**.
- The fastest composition test: **a strong blur**, then count the blobs.

---

**Next step:** [→ Lesson 03: Colour](03-culoarea.md)
