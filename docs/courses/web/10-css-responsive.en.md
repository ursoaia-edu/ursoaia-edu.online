---
lesson: 10
tags: [web, css, responsive, media-queries, mobile-first, viewport]
summary: A single site that looks great on phone, tablet, and desktop. Learn media queries and mobile-first.
---

# Lesson 10 · Responsive design

!!! tip "What you will learn"
    - What responsive design means and why it's mandatory
    - The `viewport` meta tag — without it there is no mobile
    - CSS units: `px`, `em`, `rem`, `%`, `vw`, `vh`
    - **Media queries** — different styles based on screen size
    - The **mobile-first** approach and common breakpoints
    - Images and layouts that adapt

---

## What does responsive mean

A **responsive** site is **a single** HTML + CSS codebase that adapts automatically to any screen size — phone, tablet, laptop, 4K monitor.

**The old (and dead) alternative:** a separate site for mobile (e.g., `m.example.com`). Two different codebases, double the maintenance, SEO problems.

!!! note "Why responsive is mandatory in 2024+"
    Over **60% of global web traffic** comes from phones. A site that looks bad on mobile loses most of its visitors. Google also penalizes non-responsive sites in search results (*mobile-first indexing*).

---

## Viewport meta tag — mandatory

**Without** this tag, the mobile browser will display the site at desktop size, zoomed in. With it, the site adapts.

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My page</title>
</head>
```

- `width=device-width` — viewport width = the actual width of the screen
- `initial-scale=1.0` — initial zoom 100% (no zoom out)

!!! warning "Forgetting the viewport = the most frequent mobile bug"
    Always check `<head>`. Without it, all the media queries CSS is **ignored** on phones.

---

## CSS units — which and when

| Unit | Type | Good for |
|---------|-----|-------------|
| `px` | absolute | fine borders, shadows, things that should not scale |
| `em` | relative to the parent | padding / margin in components |
| `rem` | relative to `<html>` | **font-size**, main dimensions |
| `%` | percent of parent | `width` in containers |
| `vw` | 1% of the window's width | "hero" sections, large titles |
| `vh` | 1% of the window's height | hero height, full-screen modals |
| `ch` | width of the "0" character | text column widths |

### How `rem` works

```css
html {
  font-size: 16px;        /* default in all browsers */
}

h1 {
  font-size: 2rem;        /* = 2 × 16px = 32px */
}

p {
  font-size: 1rem;        /* = 16px */
}

small {
  font-size: 0.875rem;    /* = 14px */
}
```

If the user increases the font size in their browser, all `rem` values grow **proportionally** — accessibility for free.

### `vw` / `vh` examples

```css
.hero {
  height: 100vh;          /* as tall as the screen */
}

.huge-title {
  font-size: 8vw;         /* scales with the screen width */
}
```

!!! tip "Don't put everything in `vw`"
    Text with `font-size: 8vw` becomes **tiny** on mobile (8 × 375 = 30px) and **huge** on a 4K monitor (8 × 2560 = 205px). Use `clamp()`:
    ```css
    font-size: clamp(2rem, 5vw, 4rem);
    /*          ^min  ^preferred ^max */
    ```

---

## Media queries

A **media query** applies CSS rules only when a condition is true (e.g., screen width below 768px).

### Syntax

```css
/* Style applied ONLY when the screen is ≤ 768px (phone + small tablet) */
@media (max-width: 768px) {
  .container {
    padding: 1rem;
  }

  nav {
    flex-direction: column;
  }
}
```

### Operators

```css
/* Up to 767px */
@media (max-width: 767px) { ... }

/* From 768px and up */
@media (min-width: 768px) { ... }

/* Between 768px and 1024px */
@media (min-width: 768px) and (max-width: 1024px) { ... }

/* Orientation */
@media (orientation: landscape) { ... }
@media (orientation: portrait)  { ... }

/* Preference for dark mode */
@media (prefers-color-scheme: dark) { ... }
```

---

## Mobile-first — why and how

There are two approaches:

### Desktop-first (old)

```css
/* Default style for desktop */
.card { width: 400px; }

/* Then narrow for smaller screens */
@media (max-width: 767px) {
  .card { width: 100%; }
}
```

### Mobile-first (modern, recommended)

```css
/* Default style for mobile */
.card { width: 100%; }

/* Then widen for larger screens */
@media (min-width: 768px) {
  .card { width: 400px; }
}
```

**Why mobile-first wins:**

- Mobile is the **most constrained case** — easier to add features on large screens than to remove them
- The default CSS is simpler (no overrides)
- Better performance on phones (desktop CSS is not loaded unnecessarily)

---

## Common breakpoints

Standard industry values:

| Breakpoint | Device |
|------------|-----------|
| `576px` | large phone |
| `768px` | tablet (portrait) |
| `992px` | small laptop / landscape tablet |
| `1200px` | desktop |
| `1400px` | wide monitor |

```css
/* Mobile-first structure */

/* Default style = mobile (0–575px) */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop */
@media (min-width: 1200px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

!!! note "Don't blindly copy breakpoints"
    The values above are a **guide**, not a rule. Choose breakpoints **based on content**: if your design "breaks" at 900px, set the breakpoint at 900px, not at 992px.

---

## Responsive images

### `max-width: 100%` — the essential trick

```css
img {
  max-width: 100%;
  height: auto;
}
```

- The image **never exceeds** the container's width
- `height: auto` keeps the proportions

### `<picture>` — different images for different screens

```html
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.jpg">
  <source media="(min-width: 600px)"  srcset="hero-tablet.jpg">
  <img src="hero-mobile.jpg" alt="Description">
</picture>
```

The browser downloads **only** the right image → traffic saved on mobile.

### `srcset` — different resolutions

```html
<img
  src="photo.jpg"
  srcset="photo-1x.jpg 1x, photo-2x.jpg 2x"
  alt="...">
```

Retina screens get the 2x version; normal screens get the 1x.

---

## Responsive Grid / Flexbox

### `auto-fit` (from lesson 08) is naturally responsive

```css
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
```

On mobile → one column. On tablet → 2. On desktop → 3+. No media queries.

### Flexbox with `wrap`

```css
.nav-links {
  display: flex;
  flex-wrap: wrap;     /* go to a new row if they don't fit */
  gap: 1rem;
}
```

---

## Hiding/showing elements

```css
/* Show only on desktop */
.desktop-menu {
  display: none;
}

@media (min-width: 768px) {
  .desktop-menu {
    display: flex;
  }
}

/* Show only on mobile */
.hamburger {
  display: block;
}

@media (min-width: 768px) {
  .hamburger {
    display: none;
  }
}
```

!!! warning "Don't hide important content"
    `display: none` removes the element from the **screen reader** too. Don't hide critical content (e.g., a "Contact" link) just to make the design cleaner on mobile — find another solution (e.g., a hamburger menu).

---

## How to test responsive design

1. **DevTools** (F12 in Chrome/Firefox) → the **Toggle device toolbar** icon (Ctrl+Shift+M / Cmd+Shift+M)
2. Choose a device from the dropdown (iPhone 14, iPad, Galaxy S22, etc.)
3. Manually resize the bar — you'll see in real time where the design "breaks"
4. Check at critical breakpoints: **375px** (iPhone), **768px** (iPad), **1440px** (laptop)

!!! tip "Also test on a real phone"
    The DevTools simulator is good, but **never** replaces testing on a real phone — touch speed, gestures, and load speed are different.

---

## Exercises

### Exercise 1 — Card that changes its width

Card of 300px on desktop, 100% on mobile (below 768px).

??? success "Solution"
    ```css
    .card {
      /* Mobile-first: default width is 100% */
      width: 100%;
      padding: 1rem;
      background: white;
      border-radius: 12px;
    }

    @media (min-width: 768px) {
      .card {
        width: 300px;
      }
    }
    ```

### Exercise 2 — Horizontal → vertical navigation

On desktop the links are on a line. On mobile they align vertically (column).

??? success "Solution"
    ```html
    <nav>
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    ```
    ```css
    .nav-links {
      display: flex;
      flex-direction: column;   /* default on mobile = column */
      gap: 0.5rem;
      list-style: none;
      padding: 0;
      margin: 0;
    }

    @media (min-width: 768px) {
      .nav-links {
        flex-direction: row;    /* on desktop = horizontal */
        gap: 2rem;
      }
    }
    ```

### Exercise 3 — Hide the image on mobile

A decorative image must disappear below 768px.

??? success "Solution"
    ```css
    .decor-image {
      display: none;
    }

    @media (min-width: 768px) {
      .decor-image {
        display: block;
      }
    }
    ```
    If the image has informative content, instead use `<picture>` with a version optimized for mobile — **don't** hide it completely.

---

## Mini-project: Complete responsive page

A landing page with hero, grid of 3 cards, and navigation — all adapt perfectly to mobile, tablet, and desktop.

??? success "Solution"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ursoaia Edu — Courses</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <header class="site-header">
        <a class="logo" href="/">Ursoaia Edu</a>
        <nav>
          <ul class="nav-links">
            <li><a href="#">Courses</a></li>
            <li><a href="#">Projects</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </header>

      <main>
        <section class="hero">
          <h1>Learn web from scratch</h1>
          <p>Practical courses for middle school and high school.</p>
          <a class="cta" href="#">Get started</a>
        </section>

        <section class="courses">
          <article class="card">
            <h2>HTML</h2>
            <p>Web page structure, tags, semantics.</p>
          </article>
          <article class="card">
            <h2>CSS</h2>
            <p>Modern styling: flexbox, grid, animations.</p>
          </article>
          <article class="card">
            <h2>JavaScript</h2>
            <p>Interactivity, DOM, events.</p>
          </article>
        </section>
      </main>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    /* ---------- Reset + base ---------- */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      font-size: 16px;
    }

    body {
      font-family: "Inter", system-ui, sans-serif;
      color: #1f2937;
      background: #f9fafb;
      line-height: 1.6;
    }

    a { color: inherit; text-decoration: none; }

    /* ---------- Header (mobile-first) ---------- */
    .site-header {
      display: flex;
      flex-direction: column;     /* column on mobile */
      gap: 1rem;
      padding: 1rem;
      background: white;
      border-bottom: 1px solid #e5e7eb;
    }

    .logo {
      font-weight: 700;
      font-size: 1.25rem;
      color: #4f46e5;
    }

    .nav-links {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      list-style: none;
    }

    .nav-links a:hover {
      color: #4f46e5;
    }

    /* Desktop: horizontal header */
    @media (min-width: 768px) {
      .site-header {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
      }

      .nav-links {
        gap: 2rem;
      }
    }

    /* ---------- Hero ---------- */
    .hero {
      text-align: center;
      padding: 3rem 1rem;
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: white;
    }

    .hero h1 {
      /* Scales smoothly between 2rem and 3.5rem, depending on width */
      font-size: clamp(2rem, 5vw, 3.5rem);
      margin-bottom: 1rem;
    }

    .hero p {
      font-size: 1.125rem;
      margin-bottom: 1.5rem;
      opacity: 0.9;
    }

    .cta {
      display: inline-block;
      padding: 0.75rem 2rem;
      background: white;
      color: #4f46e5;
      font-weight: 600;
      border-radius: 8px;
      transition: transform 0.2s ease;
    }

    .cta:hover {
      transform: translateY(-2px);
    }

    /* ---------- Courses grid ---------- */
    .courses {
      display: grid;
      grid-template-columns: 1fr;      /* 1 column on mobile */
      gap: 1rem;
      padding: 2rem 1rem;
      max-width: 1200px;
      margin: 0 auto;
    }

    .card {
      padding: 1.5rem;
      background: white;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    .card h2 {
      color: #4f46e5;
      margin-bottom: 0.5rem;
    }

    /* Tablet: 2 columns */
    @media (min-width: 768px) {
      .courses {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        padding: 3rem 2rem;
      }
    }

    /* Desktop: 3 columns */
    @media (min-width: 1024px) {
      .courses {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    /* ---------- Accessibility ---------- */
    :focus-visible {
      outline: 3px solid #c7d2fe;
      outline-offset: 2px;
    }

    @media (prefers-reduced-motion: reduce) {
      * {
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
      }
    }
    ```

    **What it uses:**

    - Mobile-first: the default CSS is for mobile, media queries add styles for larger screens
    - `clamp(2rem, 5vw, 3.5rem)` — the hero title scales smoothly
    - Grid with 3 breakpoints: 1 → 2 → 3 columns
    - `box-sizing: border-box` globally
    - Visible focus for keyboard accessibility
    - `prefers-reduced-motion` respected

---

## Summary

- **Viewport meta tag** is **mandatory** for any modern site
- The `rem` (font-size) and `%` / `fr` (layout) units are the most suitable for responsive
- `clamp(min, preferred, max)` scales smoothly between two limits
- **Media queries** adapt the styles to the screen size
- **Mobile-first** (`min-width`) is the modern approach — start from the phone
- Guideline breakpoints: **576px**, **768px**, **992px**, **1200px** (choose based on content)
- `img { max-width: 100%; height: auto; }` — images that don't exceed the container
- `auto-fit + minmax` from Grid = responsive layout without media queries
- Test in DevTools with **Toggle device toolbar**

---

**Next step:** [→ Lesson 11: Introduction to JavaScript](11-js-introducere.md)
