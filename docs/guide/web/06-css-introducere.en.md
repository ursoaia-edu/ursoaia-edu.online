---
lesson: 6
tags: [web, css, selectors, colors, fonts, styling]
summary: Learn CSS from scratch — how to style HTML with selectors, colors, fonts, and text.
---

# Lesson 06 · CSS: introduction

!!! tip "What you will learn"
    - What CSS is and how to include it in a page
    - The anatomy of a CSS rule and the basic selectors
    - How colors are chosen (names, hex, rgb, hsl)
    - Properties for text and fonts
    - How to add Google Fonts

---

## What is CSS

**CSS** (Cascading Style Sheets) is the language that styles web pages. While HTML defines the **structure** (titles, paragraphs, lists), CSS handles the **appearance** (colors, fonts, spacing, layout).

!!! note "A simple analogy"
    - **HTML** = bones and organs (the page's skeleton)
    - **CSS** = clothes, hairstyle, makeup (how it looks)
    - **JavaScript** = muscles that make it move

The separation between structure and appearance means you can completely change how a site looks without modifying a single line of HTML.

---

## Three ways to include CSS

### 1. Inline — directly on the element

```html
<p style="color: red;">Red text</p>
```

The style is written directly in the `style` attribute. **Avoid** this method — it's hard to maintain, can't be reused, and mixes structure with appearance.

### 2. Internal — in `<head>`

```html
<head>
  <style>
    p {
      color: red;
    }
  </style>
</head>
```

OK for small pages or quick tests. Cannot be reused across multiple pages.

### 3. External — separate file (recommended)

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

And in the `styles.css` file:

```css
p {
  color: red;
}
```

!!! tip "Always use external CSS"
    A single `styles.css` file can style dozens of pages. When you want to change the main color, you change it in just one place.

---

## The anatomy of a CSS rule

```css
selector {
  property: value;
  property2: value2;
}
```

Example:

```css
h1 {
  color: navy;
  font-size: 32px;
}
```

- **selector**: which element(s) you style (`h1`)
- **property**: what you change (`color`, `font-size`)
- **value**: how you change it (`navy`, `32px`)
- Each line ends with `;`
- The block is delimited by `{ }`

---

## Basic selectors

| Selector | Syntax | Selects |
|----------|---------|------------|
| Element | `p` | all `<p>` |
| Class | `.button` | elements with `class="button"` |
| ID | `#header` | the element with `id="header"` (unique) |
| Universal | `*` | all elements |
| Group | `h1, h2, h3` | all three types |
| Descendant | `article p` | `<p>` inside `<article>` |
| Direct child | `nav > a` | `<a>` direct child of `<nav>` |

```css
/* Element: all paragraphs */
p {
  color: #333;
}

/* Class: reusable, applied with class="button" */
.button {
  background-color: royalblue;
  color: white;
}

/* ID: unique on the page, applied with id="header" */
#header {
  background-color: black;
}

/* Group: same styles for multiple elements */
h1, h2, h3 {
  font-family: serif;
}

/* Descendant: only paragraphs inside articles */
article p {
  line-height: 1.7;
}
```

---

## Specificity — who wins

If two rules target the same element, the most **specific** one wins:

```
element  <  class  <  id
   1     <   10   <  100
```

```css
p { color: blue; }           /* specificity: 1 */
.text { color: green; }      /* specificity: 10 */
#title { color: red; }       /* specificity: 100 — wins */
```

!!! warning "Avoid `!important`"
    `color: red !important;` forces the rule to win regardless. Used often → CSS becomes impossible to maintain. Reserve it for extreme cases.

---

## Colors

### Predefined names

```css
color: red;
color: tomato;
color: rebeccapurple;
color: steelblue;
```

There are over 140 standard names ([full list](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)).

### Hexadecimal

```css
color: #ff0000;   /* red */
color: #00ff00;   /* green */
color: #0000ff;   /* blue */
color: #f00;      /* short = #ff0000 */
```

Format: `#RRGGBB` — each pair is a value 00–FF (0–255) for red, green, blue.

### RGB and RGBA

```css
color: rgb(255, 0, 0);            /* pure red */
color: rgba(255, 0, 0, 0.5);      /* red at 50% opacity */
```

`rgba` has a fourth parameter — **alpha** (transparency), between 0 and 1.

### HSL

```css
color: hsl(0, 100%, 50%);         /* red */
color: hsl(120, 100%, 50%);       /* green */
color: hsl(240, 100%, 50%);       /* blue */
```

- **H** (hue) — the shade, 0–360 (like a color wheel)
- **S** (saturation) — saturation, 0%–100%
- **L** (lightness) — lightness, 0% (black) – 100% (white)

!!! tip "HSL is more intuitive"
    Want the same red, but lighter? You only change `L` from 50% to 70%. With hex you would have to calculate.

---

## Properties for text

```css
p {
  color: #333;                         /* text color */
  background-color: #fffbea;           /* background */
  font-family: "Inter", Arial, sans-serif;
  font-size: 16px;
  font-weight: 400;                    /* normal=400, bold=700 */
  text-align: left;                    /* left, center, right, justify */
  text-decoration: none;               /* underline, line-through, none */
  line-height: 1.6;                    /* line height */
  letter-spacing: 0.02em;              /* spacing between letters */
  text-transform: none;                /* uppercase, lowercase, capitalize */
}
```

### Font family — fallback stack

```css
body {
  font-family: "Inter", "Segoe UI", Arial, sans-serif;
}
```

The browser tries fonts from left to right. If `Inter` is missing, it tries `Segoe UI`, then `Arial`, then any available `sans-serif` font.

### Units for font-size

| Unit | Description | Example |
|---------|-----------|---------|
| `px` | absolute pixels | `font-size: 16px;` |
| `rem` | relative to the `<html>` root | `font-size: 1rem;` (= 16px by default) |
| `em` | relative to the parent | `font-size: 1.25em;` |

!!! tip "Use `rem` for text"
    `rem` respects the user's preferences (if they increase the font in browser settings) — more **accessible** than `px`.

### Line-height — how airy the text is

```css
p {
  line-height: 1.6;   /* recommended for paragraphs */
}
```

A `line-height` that's too small makes text hard to read. Between **1.5** and **1.7** is ideal.

---

## Google Fonts

Google offers hundreds of free fonts. How you use them:

### 1. Add a `<link>` in `<head>`

```html
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
</head>
```

### 2. Use the font in CSS

```css
body {
  font-family: "Inter", sans-serif;
}
```

!!! note "Choose 1–2 families maximum"
    Each downloaded font slows the page. One for titles + one for body text is enough.

---

## Exercises

### Exercise 1 — Yellow background for paragraphs

Put all paragraphs on a light yellow background with darker text.

??? success "Solution"
    ```css
    p {
      background-color: #fffbea;
      color: #333;
      padding: 8px;
    }
    ```

### Exercise 2 — `.important` and `.small` classes

Create two classes and apply them to elements in HTML.

??? success "Solution"
    ```html
    <p class="important">Attention!</p>
    <p class="small">Footnote</p>
    ```
    ```css
    .important {
      color: #c00;
      font-weight: 700;
    }

    .small {
      font-size: 12px;
      color: #666;
    }
    ```

### Exercise 3 — Google Font for the entire page

Set the `Poppins` font from Google Fonts for all the content.

??? success "Solution"
    ```html
    <head>
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="styles.css">
    </head>
    ```
    ```css
    body {
      font-family: "Poppins", sans-serif;
      font-size: 1rem;
      line-height: 1.6;
      color: #222;
    }

    h1, h2, h3 {
      font-weight: 600;
    }
    ```

---

## Mini-project: Style the "About me" page

Take the HTML page from the previous lesson and turn it into a clean design with a coherent color palette and Google font.

??? success "Solution"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>About me</title>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <header>
        <h1>Ana Popescu</h1>
        <p class="subtitle">Student · web enthusiast</p>
      </header>

      <section>
        <h2>Hobbies</h2>
        <ul>
          <li>Programming</li>
          <li>Music</li>
          <li>Digital drawing</li>
        </ul>
      </section>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    /* Color palette */
    body {
      background-color: #f7f7fb;
      color: #1f2937;
      font-family: "Inter", sans-serif;
      font-size: 1rem;
      line-height: 1.6;
      margin: 2rem;
    }

    header {
      background-color: #4f46e5;
      color: white;
      padding: 1.5rem;
      border-radius: 8px;
    }

    h1 {
      margin: 0;
    }

    .subtitle {
      color: #e0e7ff;
      margin: 0.5rem 0 0;
    }

    h2 {
      color: #4f46e5;
    }

    ul {
      line-height: 1.8;
    }
    ```

---

## Summary

- **CSS** styles HTML — colors, fonts, spacing
- Use **external CSS** (`<link>`) for real pages
- CSS rule = **selector + properties + values**
- Basic selectors: **element**, **class** (`.`), **ID** (`#`)
- Specificity: `element < class < id`
- Colors: **names**, **#hex**, **rgb/rgba**, **hsl**
- `rem` > `px` for `font-size` (accessibility)
- **Google Fonts** adds modern fonts for free

---

**Next step:** [→ Lesson 07: Box Model and positioning](07-css-box-model.md)
