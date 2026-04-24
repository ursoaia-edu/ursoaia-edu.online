---
lesson: 8
tags: [web, css, flexbox, grid, layout, responsive]
summary: Build modern layouts with Flexbox (1D) and Grid (2D). No floats, no hacks.
---

# Lesson 08 · Flexbox and Grid

!!! tip "What you will learn"
    - Why Flexbox and Grid replaced `float`
    - How to align elements on one axis with **Flexbox**
    - How to build 2D layouts with **CSS Grid**
    - The differences and when to use each
    - Responsive tricks (auto-fit + minmax)

---

## The problem before 2015

Layouts were built with `float: left` + `clear: both` — fragile hacks inherited from arranging images within text. Vertical centering was **impossible** without tricks involving `table-cell` or `transform`.

Since 2015, CSS has gained two modern tools:

- **Flexbox** — alignment on **one axis** (1D): ideal for menus, cards in a row, navigation bars
- **Grid** — **2D** layouts: galleries, dashboards, full pages

!!! note "Forget about `float` for layout"
    `float` is used today **exclusively** to wrap text around an image. Anything else → Flexbox or Grid.

---

## Flexbox — alignment on one axis

You enable Flexbox on the **parent** with `display: flex`:

```html
<div class="bar">
  <span>1</span>
  <span>2</span>
  <span>3</span>
</div>
```

```css
.bar {
  display: flex;          /* enables flex on direct children */
  gap: 1rem;              /* space between children */
}
```

The children become **flex items** aligned horizontally.

### Properties on the parent

```css
.container {
  display: flex;
  flex-direction: row;           /* row (default) | column | row-reverse | column-reverse */
  justify-content: flex-start;   /* alignment on the main axis */
  align-items: stretch;          /* alignment on the cross axis */
  flex-wrap: nowrap;             /* nowrap (default) | wrap */
  gap: 1rem;                     /* space between elements */
}
```

### `justify-content` — main axis

| Value | Effect |
|---------|-------|
| `flex-start` | all at the start (left) |
| `center` | centered |
| `flex-end` | all at the end (right) |
| `space-between` | first at the start, last at the end, the rest equally between |
| `space-around` | equal space around each element |
| `space-evenly` | equal space between and at the edges |

### `align-items` — cross axis

| Value | Effect |
|---------|-------|
| `stretch` (default) | stretched to fill the height |
| `flex-start` | aligned at the top |
| `center` | vertically centered |
| `flex-end` | aligned at the bottom |
| `baseline` | aligned to the text baseline |

### Properties on children

```css
.element {
  flex: 1;                 /* grows to fill the space (shorthand for flex-grow: 1) */
  flex-basis: 200px;       /* base size */
  flex-shrink: 0;          /* 0 = does not shrink */
  align-self: flex-end;    /* override align-items just for this element */
}
```

---

## Flexbox examples

### 1. Navigation bar (logo left, links right)

```html
<nav class="nav">
  <a class="logo" href="/">Logo</a>
  <ul class="links">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

```css
.nav {
  display: flex;
  justify-content: space-between;   /* logo left, menu right */
  align-items: center;              /* vertically centered alignment */
  padding: 1rem 2rem;
  background: #1f2937;
  color: white;
}

.links {
  display: flex;
  gap: 1.5rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.links a {
  color: white;
  text-decoration: none;
}
```

### 2. Three equal cards on a row

```html
<div class="cards">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</div>
```

```css
.cards {
  display: flex;
  gap: 1rem;
}

.card {
  flex: 1;                   /* each card gets an equal share */
  padding: 1.5rem;
  background: #f3f4f6;
  border-radius: 8px;
}
```

### 3. Perfect centering (horizontal + vertical)

```css
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;     /* 100% of the window's height */
}
```

!!! tip "The simplest centering in CSS history"
    Before Flexbox, vertical centering required 5–10 lines of hacks. Now it's three properties.

---

## Grid — 2D layouts

You enable Grid on the parent with `display: grid`:

```html
<div class="gallery">
  <img src="1.jpg" alt="">
  <img src="2.jpg" alt="">
  <img src="3.jpg" alt="">
  <img src="4.jpg" alt="">
  <img src="5.jpg" alt="">
  <img src="6.jpg" alt="">
</div>
```

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);   /* 3 equal columns */
  gap: 1rem;
}
```

### `grid-template-columns` — defines the columns

```css
/* 3 equal columns */
grid-template-columns: 1fr 1fr 1fr;

/* Same thing, shorthand */
grid-template-columns: repeat(3, 1fr);

/* Different proportions: 1-2-1 (the middle column is double) */
grid-template-columns: 1fr 2fr 1fr;

/* Mix: first fixed, second flexible, third fixed */
grid-template-columns: 200px 1fr 200px;
```

!!! note "`fr` = fraction"
    The `fr` unit distributes **the remaining space**. `1fr 2fr` means 1/3 and 2/3 of the available space.

### `grid-template-rows` — defines the rows

```css
.page {
  display: grid;
  grid-template-rows: auto 1fr auto;   /* header, content, footer */
  min-height: 100vh;
}
```

### `gap` — space between cells

```css
gap: 1rem;              /* same space on both axes */
gap: 1rem 2rem;         /* row 1rem, column 2rem */
row-gap: 1rem;
column-gap: 2rem;
```

### `grid-column` — an item spans multiple columns

```css
.hero {
  grid-column: span 2;     /* spans 2 columns */
}

.full-row {
  grid-column: 1 / -1;     /* from the first to the last column */
}
```

---

## The magic of `auto-fit` + `minmax` (responsive)

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
```

What happens:

- Each column is at **minimum 250px**, **maximum 1fr** of the available space
- `auto-fit` packs **as many columns as fit** in the container
- On wide desktop → 4 columns. On tablet → 3. On phone → 1.

!!! tip "Responsive layout without media queries"
    This line replaces dozens of lines of breakpoints. A must-have trick in any web developer's toolkit.

---

## Flexbox vs Grid — when to use what

| Situation | Right tool |
|----------|------------------------|
| Navigation bar | **Flexbox** |
| Cards on a single row | **Flexbox** |
| Horizontal + vertical centering | **Flexbox** |
| Aligning buttons on a line | **Flexbox** |
| Photo gallery in rows and columns | **Grid** |
| Whole-page layout (header + sidebar + main + footer) | **Grid** |
| Dashboard with widgets | **Grid** |
| Form with aligned labels and fields | **Grid** |

!!! tip "You can combine them"
    Most often: **Grid** for the overall page layout + **Flexbox** inside each cell (e.g., inside a card, flexbox aligns the avatar and the text).

---

## Exercises

### Exercise 1 — Navigation bar with Flexbox

Logo on the left, 4 links on the right, all vertically aligned.

??? success "Solution"
    ```html
    <nav class="nav">
      <a class="logo" href="/">Site</a>
      <ul class="links">
        <li><a href="#">Home</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    ```
    ```css
    .nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      background: white;
      border-bottom: 1px solid #e5e7eb;
    }

    .logo {
      font-weight: 700;
      text-decoration: none;
      color: #4f46e5;
    }

    .links {
      display: flex;
      gap: 2rem;
      list-style: none;
      margin: 0;
      padding: 0;
    }

    .links a {
      color: #1f2937;
      text-decoration: none;
    }

    .links a:hover {
      color: #4f46e5;
    }
    ```

### Exercise 2 — Three equal pricing cards

```html
<div class="pricing">
  <div class="card">Basic</div>
  <div class="card">Pro</div>
  <div class="card">Enterprise</div>
</div>
```

??? success "Solution"
    ```css
    .pricing {
      display: flex;
      gap: 1.5rem;
      padding: 2rem;
    }

    .card {
      flex: 1;
      padding: 2rem;
      background: white;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      text-align: center;
    }
    ```

### Exercise 3 — 3x3 gallery with Grid

9 images arranged in a 3x3 grid.

??? success "Solution"
    ```html
    <div class="gallery">
      <img src="1.jpg" alt="Photo 1">
      <img src="2.jpg" alt="Photo 2">
      <img src="3.jpg" alt="Photo 3">
      <img src="4.jpg" alt="Photo 4">
      <img src="5.jpg" alt="Photo 5">
      <img src="6.jpg" alt="Photo 6">
      <img src="7.jpg" alt="Photo 7">
      <img src="8.jpg" alt="Photo 8">
      <img src="9.jpg" alt="Photo 9">
    </div>
    ```
    ```css
    .gallery {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.5rem;
    }

    .gallery img {
      width: 100%;
      aspect-ratio: 1;       /* perfect square */
      object-fit: cover;     /* no deformation */
      border-radius: 8px;
    }
    ```

### Exercise 4 — Responsive gallery with `auto-fit`

The same gallery, but the columns adapt automatically to the screen size.

??? success "Solution"
    ```css
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.5rem;
    }
    ```
    Test by resizing the window — the number of columns changes automatically.

---

## Mini-project: Magazine-style photo gallery

A responsive gallery with 3 columns on desktop, title overlaid on the image, subtle hover effect.

??? success "Solution"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Gallery</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <h1>My gallery</h1>

      <div class="gallery">
        <figure class="card">
          <img src="photo1.jpg" alt="Sunrise over the mountain">
          <figcaption>Sunrise at 1500m</figcaption>
        </figure>
        <figure class="card">
          <img src="photo2.jpg" alt="City at night">
          <figcaption>City at night</figcaption>
        </figure>
        <figure class="card">
          <img src="photo3.jpg" alt="Forest in autumn">
          <figcaption>Forest in autumn</figcaption>
        </figure>
        <figure class="card">
          <img src="photo4.jpg" alt="Tropical beach">
          <figcaption>Tropical beach</figcaption>
        </figure>
        <figure class="card">
          <img src="photo5.jpg" alt="Desert at sunset">
          <figcaption>Desert at sunset</figcaption>
        </figure>
        <figure class="card">
          <img src="photo6.jpg" alt="Street with lanterns">
          <figcaption>Street with lanterns</figcaption>
        </figure>
      </div>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: "Inter", sans-serif;
      background: #fafafa;
      padding: 2rem;
    }

    h1 {
      margin-bottom: 2rem;
      color: #1f2937;
    }

    /* Responsive grid — adapts automatically */
    .gallery {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
    }

    .card {
      position: relative;
      overflow: hidden;
      border-radius: 12px;
      aspect-ratio: 4 / 3;
      cursor: pointer;
    }

    .card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;   /* details in lesson 09 */
    }

    .card:hover img {
      transform: scale(1.05);
    }

    .card figcaption {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 1rem;
      color: white;
      font-weight: 600;
      background: linear-gradient(
        to top,
        rgba(0, 0, 0, 0.7),
        transparent
      );
    }
    ```

---

## Summary

- **Flexbox** = alignment on **one axis** — perfect for menus, bars, cards on a row
- **Grid** = **2D** layouts — galleries, dashboards, page structure
- Key Flexbox properties: `justify-content`, `align-items`, `gap`, `flex: 1`
- Key Grid properties: `grid-template-columns`, `repeat()`, `gap`, `fr`
- `repeat(auto-fit, minmax(250px, 1fr))` = responsive layout without media queries
- The combination **Grid (structure) + Flexbox (in cells)** covers 99% of cases
- **Stop using `float`** for layout

---

**Next step:** [→ Lesson 09: Advanced CSS — pseudo-classes, transitions, and animations](09-css-avansat.md)
