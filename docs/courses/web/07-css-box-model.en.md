---
lesson: 7
tags: [web, css, box-model, margin, padding, border, position, display]
summary: Every HTML element is a box. Learn how to control spacing, size, and position.
---

# Lesson 07 · Box Model and positioning

!!! tip "What you will learn"
    - The 4 layers of the Box Model: content, padding, border, margin
    - How to control size with `width`, `height`, and `box-sizing`
    - Values for `display`: block, inline, inline-block, none
    - Positioning: `static`, `relative`, `absolute`, `fixed`, `sticky`
    - Backgrounds and images

---

## Box Model — the 4 layers

Every HTML element is **a rectangular box**. Around the content there are three concentric layers:

```
┌─────────────── margin ───────────────┐
│  ┌────────── border ──────────────┐  │
│  │  ┌──────── padding ─────────┐  │  │
│  │  │         content          │  │  │
│  │  └──────────────────────────┘  │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
```

- **content** — the actual text or image
- **padding** — the inner space between content and border
- **border** — the border (line)
- **margin** — the outer space, between the box and its neighbors

!!! note "How to see the Box Model"
    In Chrome / Firefox, press **F12** → **Elements** tab → the **Computed** panel on the right shows the colored box (blue, green, orange, yellow) for any selected element.

---

## Margin — the outer space

```css
/* All 4 margins equal */
.box {
  margin: 10px;
}

/* Top/bottom = 10px, left/right = 20px */
.box {
  margin: 10px 20px;
}

/* Top = 10, right = 20, bottom = 15, left = 5 (clockwise) */
.box {
  margin: 10px 20px 15px 5px;
}

/* Individual */
.box {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 15px;
  margin-left: 5px;
}
```

### `margin: auto` — horizontal centering

```css
.card {
  width: 400px;
  margin: 0 auto;   /* 0 top/bottom, auto left/right */
}
```

The browser splits the remaining space equally → the box is centered.

!!! warning "Margin collapse"
    When two neighboring elements have vertical margin (e.g., two paragraphs with `margin-bottom: 20px` and `margin-top: 20px`), the browser **does NOT** add them (you don't get 40px), it keeps **the larger one** (20px). This is called *margin collapse* and it's normal.

---

## Padding — the inner space

Same syntax as `margin`:

```css
.button {
  padding: 12px 24px;    /* vertical 12px, horizontal 24px */
  background-color: royalblue;
  color: white;
}
```

Padding increases the visible **box** (adding space between content and edge).

---

## Border — the border line

```css
.card {
  border: 2px solid #4f46e5;   /* width, style, color */
}

/* Just one side */
.card {
  border-bottom: 1px solid #e5e7eb;
}
```

### Available styles

```css
border-style: solid;    /* continuous line */
border-style: dashed;   /* dashed line */
border-style: dotted;   /* dots */
border-style: double;   /* two lines */
border-style: none;     /* no border */
```

### Rounded corners with `border-radius`

```css
.card {
  border-radius: 8px;       /* slightly rounded corners */
}

.avatar {
  border-radius: 50%;       /* perfect circle (if width = height) */
}

.pill {
  border-radius: 999px;     /* pill shape */
}
```

---

## Width and height

```css
.card {
  width: 300px;
  height: 200px;
}
```

### Responsive width/height

```css
.card {
  max-width: 600px;     /* never wider than 600px */
  min-width: 200px;     /* never narrower than 200px */
  width: 100%;          /* takes up all the parent's space */
}
```

!!! tip "Prefer `max-width` instead of fixed `width`"
    `max-width: 600px` lets the box shrink naturally on small screens. `width: 600px` forces it to stay at 600px and may overflow the screen on a phone.

### Default values

- **Block** elements (`<div>`, `<p>`, `<h1>`): `width: auto` → take up the full row
- **Inline** elements (`<span>`, `<a>`): `width` and `height` are **ignored**

---

## `box-sizing: border-box` — essential

This is the most important concept in the Box Model.

### Default behavior: `content-box`

```css
.box {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
```

**Actual visible width = 200 + 20 + 20 + 2 + 2 = 244 px.**

That is, `width` only refers to the content — padding and border **are added on top**. Completely unintuitive.

### `box-sizing: border-box` — predictable

```css
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
```

**Actual visible width = 200 px.** Padding and border are **included** in width.

### The golden rule (always use)

```css
/* At the beginning of every CSS file */
* {
  box-sizing: border-box;
}
```

!!! tip "Why `* { box-sizing: border-box; }`"
    Apply the rule for **all** elements. It saves you mental calculations and makes responsive layouts much easier to control. The modern standard in all frameworks (Bootstrap, Tailwind, etc.).

---

## Display — how the element behaves

```css
div    { display: block; }         /* takes the whole row, accepts width/height */
span   { display: inline; }        /* as wide as the text, does NOT accept width/height */
a      { display: inline-block; }  /* as wide as the text, BUT accepts width/height */
.hidden { display: none; }         /* disappears completely from the page */
```

| Value | New row? | Accepts width/height? |
|---------|---------------|------------------------|
| `block` | yes | yes |
| `inline` | no | no |
| `inline-block` | no | yes |
| `none` | — disappears — | — |

!!! warning "`display: none` vs `visibility: hidden`"
    - `display: none` — the element **disappears**, takes no space, isn't heard by screen readers.
    - `visibility: hidden` — the element is invisible but **takes up space**.

---

## Position — positioning elements

### `static` (default)

The element follows the normal flow of the document. `top`, `left` have no effect.

### `relative` — moved relative to its normal position

```css
.card {
  position: relative;
  top: 10px;
  left: 20px;   /* moves 20px right, 10px down */
}
```

Important: `relative` keeps its original spot (other elements don't move).

### `absolute` — taken out of the flow

```css
.parent {
  position: relative;   /* needed for anchoring */
}

.child {
  position: absolute;
  top: 0;
  right: 0;             /* in the parent's top-right corner */
}
```

`absolute` positions itself relative to **the first parent with a position other than static**. If it doesn't find one, it's relative to `<body>`.

### `fixed` — fixed relative to the viewport

```css
.floating-button {
  position: fixed;
  bottom: 20px;
  right: 20px;          /* stays there even when you scroll */
}
```

Useful for "Back to top" buttons, notifications, chat widgets.

### `sticky` — static/fixed hybrid

```css
header {
  position: sticky;
  top: 0;               /* sticks to the top when you scroll to it */
  background: white;
  z-index: 10;
}
```

Behaves like `static` until you reach the threshold, then becomes `fixed`. Excellent for navigation bars.

### Quick comparison

| Value | In flow? | Moves relative to what? |
|---------|----------|------------------------|
| `static` | yes | — (cannot be moved) |
| `relative` | yes | its original position |
| `absolute` | no | the closest positioned parent |
| `fixed` | no | viewport (the window) |
| `sticky` | yes until threshold | viewport after threshold |

---

## z-index — order on the Z axis

When elements overlap, `z-index` decides which is **on top**.

```css
.modal {
  position: fixed;
  z-index: 1000;   /* above any other element */
}

.modal-backdrop {
  position: fixed;
  z-index: 999;    /* below the modal, but above the rest of the page */
}
```

!!! note "`z-index` only works on positioned elements"
    You also need `position: relative/absolute/fixed/sticky` for `z-index` to take effect.

---

## Background

```css
.hero {
  background-color: #4f46e5;
  background-image: url('background.jpg');
  background-size: cover;        /* covers the entire container */
  background-position: center;   /* centered */
  background-repeat: no-repeat;  /* doesn't tile */
}

/* Shorthand — all in one line */
.hero {
  background: #4f46e5 url('background.jpg') center / cover no-repeat;
}
```

| Value for `background-size` | Effect |
|------------------------------------|-------|
| `cover` | image covers the entire container (may be cropped) |
| `contain` | image fits completely (margins may remain) |
| `100% 100%` | stretched (deformed — to be avoided) |

---

## Exercises

### Exercise 1 — Card with padding, border, and rounded corners

Create a `<div class="card">` with text inside, styled as a modern card.

??? success "Solution"
    ```html
    <div class="card">
      <h2>Card title</h2>
      <p>A short descriptive text.</p>
    </div>
    ```
    ```css
    .card {
      box-sizing: border-box;
      padding: 24px;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      background-color: white;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
      max-width: 400px;
    }
    ```

### Exercise 2 — Center a div with fixed width

Use `margin: auto`.

??? success "Solution"
    ```css
    .container {
      max-width: 800px;
      margin: 0 auto;      /* horizontal centering */
      padding: 1rem;
    }
    ```

### Exercise 3 — "Floating" button in the corner

A button that stays fixed in the bottom-right corner of the page.

??? success "Solution"
    ```html
    <button class="fab" aria-label="Add">+</button>
    ```
    ```css
    .fab {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 56px;
      height: 56px;
      border: none;
      border-radius: 50%;
      background-color: #4f46e5;
      color: white;
      font-size: 28px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      z-index: 100;
    }

    .fab:hover {
      background-color: #4338ca;
    }
    ```

---

## Mini-project: Digital business card

Create a card with a round avatar, name, role, and social links.

??? success "Solution"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Business card</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <article class="business-card">
        <img class="avatar" src="avatar.jpg" alt="Photo of Ana Popescu">
        <h1 class="name">Ana Popescu</h1>
        <p class="role">Web Developer</p>
        <ul class="social">
          <li><a href="#">GitHub</a></li>
          <li><a href="#">LinkedIn</a></li>
          <li><a href="#">Email</a></li>
        </ul>
      </article>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    /* Basic reset */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: linear-gradient(135deg, #667eea, #764ba2);
      min-height: 100vh;
      font-family: "Inter", sans-serif;
      /* Centering with flexbox — detailed in lesson 08 */
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }

    .business-card {
      width: 320px;
      padding: 2rem;
      background-color: white;
      border-radius: 16px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .avatar {
      width: 120px;
      height: 120px;
      border-radius: 50%;       /* perfect circle */
      border: 4px solid #4f46e5;
      object-fit: cover;        /* image is not deformed */
      margin-bottom: 1rem;
    }

    .name {
      font-size: 1.5rem;
      color: #1f2937;
      margin-bottom: 0.25rem;
    }

    .role {
      color: #6b7280;
      margin-bottom: 1.5rem;
    }

    .social {
      list-style: none;
      display: flex;
      justify-content: center;
      gap: 1rem;
    }

    .social a {
      color: #4f46e5;
      text-decoration: none;
      font-weight: 600;
    }

    .social a:hover {
      text-decoration: underline;
    }
    ```

---

## Summary

- **Box Model** = content + padding + border + margin
- `margin` = **outer** space, `padding` = **inner** space
- `border-radius: 50%` = perfect circle
- `* { box-sizing: border-box; }` — **mandatory rule** in any modern project
- `display`: block / inline / inline-block / none
- `position`: static (default), relative, absolute, fixed, sticky
- `background` controls the background color and image
- `z-index` only works on positioned elements

---

**Next step:** [→ Lesson 08: Flexbox and Grid](08-css-flexbox-grid.md)
