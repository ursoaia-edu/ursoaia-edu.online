---
lesson: 2
tags: [web, html, links, images, headings, accessibility]
summary: The essential HTML tags — headings, paragraphs, links, images, text formatting, div and span.
---

# Lesson 02 · HTML: the basic tags

!!! tip "What you'll learn"
    - The hierarchy of headings `<h1>` – `<h6>` and why it matters
    - Proper paragraphs and what **not** to do with `<br>`
    - Internal, external, in-page, and email links
    - Images, the `alt` attribute, and the right formats
    - Text formatting: `<strong>`, `<em>`, `<mark>`, `<code>`
    - The difference between `<div>` and `<span>`

---

## Headings: from `<h1>` to `<h6>`

HTML has **6 heading levels**. They're not just about size — they're **semantic**. Search engines and screen readers use their hierarchy to understand the page structure.

```html
<h1>The main title of the page</h1>
<h2>Major section</h2>
<h3>Sub-section</h3>
<h4>Detail</h4>
```

!!! warning "One `<h1>` per page"
    `<h1>` is the **main** title — one per page (like the title of a book). `<h2>` for chapters, `<h3>` for sub-chapters and so on.

**Example of correct structure for an article:**

```html
<h1>Cycling guide for beginners</h1>
  <h2>Choosing a bike</h2>
    <h3>City bike</h3>
    <h3>Mountain bike</h3>
  <h2>Essential gear</h2>
    <h3>Helmet</h3>
    <h3>Lights and reflectors</h3>
```

Don't skip levels (`<h1>` straight to `<h4>`) just because "it looks nice" — for that we have CSS (lessons 06+).

---

## Paragraphs

`<p>` means "paragraph". The browser automatically adds space before and after:

```html
<p>This is the first paragraph. It can contain several sentences,
   you don't have to break the line manually — the browser handles
   that for you.</p>

<p>The second paragraph. The space between them is natural.</p>
```

!!! warning "Don't use `<br>` for spacing between paragraphs"
    ```html
    <!-- Wrong: -->
    <p>First text</p>
    <br><br>
    <p>Second text</p>

    <!-- Correct: -->
    <p>First text</p>
    <p>Second text</p>
    ```
    `<br>` is for **a single line break** in a context where you actually want one (postal address, song lyrics). For spacing between paragraphs use `<p>`, and for custom spacing you'll use CSS later.

---

## Links (`<a>`)

The link (anchor) is the **heart of the web** — without it, it wouldn't be called "the Web".

### Simple link

```html
<a href="https://ursoaia-edu.online">Ursoaia Edu</a>
```

- `href` (hypertext reference) = the destination address.
- The text between `<a>` and `</a>` is what the user sees.

### Absolute vs. relative URL

```html
<!-- Absolute: works from anywhere -->
<a href="https://en.wikipedia.org">Wikipedia</a>

<!-- Relative: to another file in the same folder -->
<a href="about.html">About us</a>

<!-- Relative: to a file in the parent folder -->
<a href="../index.html">Home</a>

<!-- Relative: to a file in a subfolder -->
<a href="./projects/list.html">Projects</a>
```

### New tab: `target="_blank"` + security

```html
<a href="https://example.com" target="_blank" rel="noopener">
  Open in a new tab
</a>
```

!!! warning "Always add `rel=\"noopener\"`"
    Without `rel="noopener"`, the opened page can access your page through `window.opener` — a small security hole. **Rule:** `target="_blank"` ⇒ `rel="noopener"`.

### Link to a section in the same page

Use an `id` and a `#`:

```html
<nav>
  <a href="#history">Jump to History</a>
</nav>

<!-- Further down the page: -->
<h2 id="history">History</h2>
<p>In 1989...</p>
```

### Email link

```html
<a href="mailto:anna@example.com">Email me</a>
```

Opens the default mail client with the address pre-filled.

---

## Images (`<img>`)

```html
<img src="assets/landscape.jpg" alt="View from the Apuseni Mountains" width="400">
```

- `src` (source) = the path to the image file.
- `alt` = the description of the image (alternative text).
- `width` / `height` (optional) = dimensions in pixels.

!!! tip "`alt` is NOT optional"
    `alt` has **two critical roles**:

    1. **Accessibility:** screen readers read it to people who can't see.
    2. **SEO:** Google uses it to understand what's in the image.

    Plus: if the image fails to load, the `alt` text is shown in its place.

    Describe **what is shown**, not "image" or "picture". Bad: `alt="img1"`. Good: `alt="A Golden Retriever running on a beach"`.

### The right format

| Format | When to use it |
|--------|----------------|
| **JPG** / **JPEG** | Photos (many colors, no transparency) |
| **PNG** | Graphics, screenshots, **transparency** |
| **SVG** | Icons, logos (scalable, small) |
| **WebP** | Modern, smaller than JPG/PNG — supported in all modern browsers |

### Relative path — example

Folder structure:

```
my-site/
├── index.html
└── images/
    └── landscape.jpg
```

In `index.html`:

```html
<img src="images/landscape.jpg" alt="Mountain landscape">
```

---

## Text formatting

### `<strong>` — important (bold by default)

```html
<p>This field is <strong>required</strong>.</p>
```

### `<em>` — emphasis (italic by default)

```html
<p>He really <em>did</em> want to go.</p>
```

!!! note "Semantics, not just style"
    `<strong>` is different from `<b>`, and `<em>` is different from `<i>`. The short ones (`<b>`, `<i>`) only mean "show as bold/italic" — no meaning. The long ones (`<strong>`, `<em>`) say "this is important" / "this is emphasized". Screen readers pronounce them differently.

### `<mark>` — highlight

```html
<p>The meeting is <mark>Tuesday at 3:00 PM</mark>.</p>
```

Text with a yellow background, like a highlighter marker.

### `<code>` — inline code

```html
<p>Type <code>print("hello")</code> in the terminal.</p>
```

### `<br>` — line break (use it RARELY)

Useful in lyrics, postal addresses:

```html
<p>10 Republicii Street<br>
400001, Cluj-Napoca<br>
Romania</p>
```

### `<hr>` — horizontal separator

```html
<h2>Chapter 1</h2>
<p>...</p>
<hr>
<h2>Chapter 2</h2>
```

---

## `<div>` vs `<span>` — containers

Sometimes you want to **group** elements for styling or interactivity. You have two neutral containers:

### `<div>` — block

Takes up **the whole row** (starts on a new line).

```html
<div>
  <h2>Card title</h2>
  <p>The card's content.</p>
</div>
```

### `<span>` — inline

Takes up **only as much space as its text** (doesn't break the line).

```html
<p>The price is <span>199 lei</span> only today.</p>
```

!!! tip "There are other options"
    `<div>` is a **generic** container. HTML5 brought better **semantic** containers: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` — you'll use them in Lesson 05. Prefer a semantic container when one exists.

---

## Common errors

- **Missing `alt`** on images → accessibility and SEO problem.
- **Multiple `<h1>`** per page → confusing structure.
- **Overusing `<br>`** instead of separate paragraphs.
- **Links with generic text**: "click here", "more" — use descriptive text. Bad: `<a href="url">here</a>`. Good: `<a href="url">the annual report</a>`.

---

## Exercises

### Exercise 1 — Complete page
Build a page with: an `<h1>`, two `<h2>`, 3 paragraphs, 2 links (one internal to a section, one external with `target="_blank"`) and an image with a descriptive `alt`.

??? success "Solution"
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Elena Marin – About me</title>
    </head>
    <body>
      <h1>Elena Marin</h1>

      <nav>
        <a href="#hobbies">Hobbies</a> ·
        <a href="https://ursoaia-edu.online" target="_blank" rel="noopener">
          Ursoaia Edu
        </a>
      </nav>

      <p>I'm a student at "Mihai Eminescu" High School in Bucharest.</p>

      <img src="images/profile.jpg" alt="Elena smiling in a park" width="200">

      <h2 id="hobbies">Hobbies</h2>
      <p>I love painting and playing the guitar.</p>
      <p>On weekends I bike through Herăstrău Park.</p>
    </body>
    </html>
    ```

### Exercise 2 — Formatting in a paragraph
Write a paragraph where one part is `<strong>`, another is `<em>`, and a keyword is in `<mark>`.

??? success "Solution"
    ```html
    <p>Radu says that <strong>safety comes first</strong>,
       but Anna is <em>absolutely convinced</em> that
       we have to hurry. Deadline:
       <mark>Friday, 6:00 PM</mark>.</p>
    ```

### Exercise 3 — Table of contents with anchors
Create a table of contents at the top of the page with 3 links to sections below (`#intro`, `#chapter-1`, `#chapter-2`).

??? success "Solution"
    ```html
    <h1>My article</h1>
    <nav>
      <p>Contents:</p>
      <ul>
        <li><a href="#intro">Introduction</a></li>
        <li><a href="#chapter-1">Chapter 1</a></li>
        <li><a href="#chapter-2">Chapter 2</a></li>
      </ul>
    </nav>

    <h2 id="intro">Introduction</h2>
    <p>...</p>
    <h2 id="chapter-1">Chapter 1</h2>
    <p>...</p>
    <h2 id="chapter-2">Chapter 2</h2>
    <p>...</p>
    ```

---

## Mini-project: "My favorite team"

Build a page about your favorite band, sports team or musical group, with:

- `<h1>` with the name
- "About" section (`<h2>` + paragraphs)
- "Members" / "Players" section (`<h2>` + paragraphs)
- "Achievements" / "Discography" section (`<h2>` + paragraphs)
- An image with descriptive `alt`
- A link to the official site (external, new tab)

??? success "Solution"
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>CFR Cluj – my team</title>
    </head>
    <body>
      <h1>CFR 1907 Cluj</h1>
      <p>Official site:
        <a href="https://www.cfr1907.ro" target="_blank" rel="noopener">
          cfr1907.ro
        </a>
      </p>

      <img src="images/stadium.jpg" alt="View from the stands of Dr. Constantin Rădulescu Stadium" width="500">

      <h2>About</h2>
      <p>A football club from Cluj-Napoca, founded in 1907.
         Plays at the "Dr. Constantin Rădulescu" stadium.</p>

      <h2>Coach and squad</h2>
      <p>Mihai Popescu is the head coach. The team captain
         is Andrei Ionescu.</p>

      <h2>Achievements</h2>
      <p>Multiple-time champion of Romania in recent years.
         Frequent participant in European cups.</p>
    </body>
    </html>
    ```

---

## Summary

- A single `<h1>` per page; use `<h2>` – `<h6>` hierarchically.
- `<p>` for paragraphs; don't overuse `<br>`.
- `<a href="..." target="_blank" rel="noopener">` for a new tab.
- `<img>` **always** requires the `alt` attribute.
- `<strong>` / `<em>` carry **meaning**, not just style.
- `<div>` = block container; `<span>` = inline container.

---

**Next step:** [→ Lesson 03: Lists and tables](03-html-liste-tabele.md)
