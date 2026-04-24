---
lesson: 5
tags: [web, html, navigation, semantics, header, nav, footer, github-pages]
summary: Build a site with multiple pages — folder organization, relative links, semantic tags, and the header/nav/main/footer structure.
---

# Lesson 05 · Multi-page site

!!! tip "What you'll learn"
    - Why we split the content across **several pages**
    - How to organize **folders** for a site
    - Relative links: `./`, `../`, subfolders
    - Semantic tags: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`
    - The `index.html` convention
    - How to publish the site quickly with **GitHub Pages**

---

## Why several pages?

You could put all the content into `index.html` — it would work, but:

- The page becomes **enormous** and slow to load.
- The menu/navigation makes no sense.
- **Worse SEO** — Google prefers focused pages (one topic per page).
- You get lost when looking for something to edit.

The rule: **one page, one topic**. Your course site might have:

- `index.html` — the Home page (what the course is, what you'll learn)
- `about.html` — About you / the teacher
- `projects.html` — The list of projects
- `contact.html` — Contact form

---

## Folder organization

A clean project looks like this:

```
my-site/
├── index.html          ← main page (Home)
├── about.html
├── projects.html
├── contact.html
├── images/
│   ├── profile.jpg
│   ├── logo.png
│   └── projects/
│       └── robot.jpg
└── styles/
    └── style.css       ← (coming in Lesson 06)
```

!!! tip "Simple naming rules"
    - **No spaces** in names. Use `about-us.html`, not `about us.html`.
    - **Lowercase only**. Some servers treat `Photo.jpg` ≠ `photo.jpg` differently.
    - **No special characters**. Use `school-timetable.html`, not `school-timetable-ă.html`.

---

## Relative links

### Same folder

```html
<!-- In index.html, link to about.html -->
<a href="about.html">About</a>
<!-- equivalent to: -->
<a href="./about.html">About</a>
```

`./` means "the current folder" — optional but explicit.

### Subfolder

```
my-site/
├── index.html
└── projects/
    └── robot.html
```

```html
<!-- In index.html: -->
<a href="projects/robot.html">See the robot project</a>
```

### Parent folder

```html
<!-- In projects/robot.html, back to the home page: -->
<a href="../index.html">Home</a>
```

`..` means "one level up".

### Absolute vs. relative — in brief

| Type | Example | When |
|------|---------|------|
| **Relative** | `about.html` | Links inside your own site |
| **Domain-absolute** | `/projects.html` | Complex sites with clear routing |
| **Fully absolute** | `https://other-site.com/...` | **External** links, to other sites |

**Recommendation for beginners:** relative (`about.html`, `./projects/...`, `../index.html`). Works both locally and in production.

---

## Navigation menu

On every page you have the same menu, which lets the user go anywhere.

```html
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="projects.html">Projects</a>
  <a href="contact.html">Contact</a>
</nav>
```

!!! warning "Repetition — a problem we'll fix later"
    If the menu is in 5 files and you want to add a new link, you have to add it in all 5. It's tedious and easy to mess up.

    **Solutions you'll learn:**

    - **JavaScript** (ES modules, `fetch` of components) — Lesson 17+
    - **Frameworks** (React, Vue) — advanced courses
    - **Static site generators** (like MkDocs, which runs this very site!) — advanced courses

    For now, copy and paste. That's OK.

### Highlighting the current page

You can visually mark the page you're on (with CSS, in Lesson 06):

```html
<!-- In about.html: -->
<nav>
  <a href="index.html">Home</a>
  <a href="about.html" class="active" aria-current="page">About</a>
  <a href="projects.html">Projects</a>
</nav>
```

`aria-current="page"` tells screen readers "you are on this page".

---

## HTML5 semantic tags

So far we've used `<div>` for any container. HTML5 introduced **meaningful tags** — browsers, Google, and assistive tech "understand" them.

```
┌─────────────────────────────────────────────┐
│ <header>  Logo | Site title                 │
│    <nav>  Home About Projects Contact       │
├─────────────────────────────────────────────┤
│                                   ┌───────┐ │
│ <main>                            │       │ │
│   <article>                       │<aside>│ │
│     Main content                  │ Side  │ │
│   </article>                      │ bar   │ │
│                                   │       │ │
│                                   └───────┘ │
├─────────────────────────────────────────────┤
│ <footer>  © 2026 Anna · contact@...          │
└─────────────────────────────────────────────┘
```

| Tag | Role |
|-----|------|
| `<header>` | The page's header (logo, title, menu) |
| `<nav>` | The navigation menu |
| `<main>` | The main content of the page (only one) |
| `<article>` | An independent article / post |
| `<section>` | A thematic section in an article |
| `<aside>` | Secondary content (sidebar, ads) |
| `<footer>` | The page's footer (copyright, links) |

### Complete example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Home — My site</title>
</head>
<body>
  <header>
    <h1>Anna's site</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="projects.html">Projects</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Welcome!</h2>
      <p>I'm Anna and this is my personal site.</p>
    </article>
  </main>

  <footer>
    <p>© 2026 Anna Popescu · Cluj-Napoca</p>
  </footer>
</body>
</html>
```

---

## The `index.html` convention

When a user visits `https://my-site.com/`, the server implicitly serves the file named `index.html` from the root folder.

That's why the main page is **always** named `index.html`, not `home.html` or `main.html`.

The same applies to subfolders:

```
/projects/         → /projects/index.html
/projects/robot/   → /projects/robot/index.html
```

---

## Quick publishing: GitHub Pages

To show your site to your classmates, **GitHub Pages** is free and simple:

1. **GitHub account** (free at [github.com](https://github.com)).
2. Create a public repository named `your-name.github.io` (e.g. `anna-pop.github.io`).
3. Upload your files (`index.html`, images, etc.).
4. In Settings → Pages, enable "Deploy from branch: main".
5. After 1-2 minutes, the site is live at `https://your-name.github.io`.

!!! tip "Full details"
    If you don't know Git / GitHub yet, we'll do a separate tutorial. For now, just remember that **publishing is free and takes 2-3 minutes**.

Alternatives: [Netlify](https://www.netlify.com/), [Vercel](https://vercel.com/), [Cloudflare Pages](https://pages.cloudflare.com/).

---

## Exercises

### Exercise 1 — Two pages with reciprocal links
Create `index.html` and `about.html` in the same folder. Each one should contain a link to the other.

??? success "Solution"
    **`index.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Home</title>
    </head>
    <body>
      <h1>Main page</h1>
      <p>See also the <a href="about.html">About page</a>.</p>
    </body>
    </html>
    ```

    **`about.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>About</title>
    </head>
    <body>
      <h1>About me</h1>
      <p>I'm Anna. <a href="index.html">Back to Home</a>.</p>
    </body>
    </html>
    ```

### Exercise 2 — Semantic structure
Add to the `about.html` page the structure: `<header>` with `<h1>` and `<nav>`, `<main>` with content, `<footer>` with copyright.

??? success "Solution"
    ```html
    <body>
      <header>
        <h1>Anna's site</h1>
        <nav>
          <a href="index.html">Home</a>
          <a href="about.html" aria-current="page">About</a>
        </nav>
      </header>

      <main>
        <h2>About me</h2>
        <p>I'm Anna Popescu, an 8th grade student in Cluj-Napoca.</p>
      </main>

      <footer>
        <p>© 2026 Anna Popescu</p>
      </footer>
    </body>
    ```

### Exercise 3 — Identical navigation
Copy the exact same `<header>...</header>` block on both pages. Notice how it's identical — and how it would be a problem if you had 20 pages.

??? success "Solution"
    Exactly — the navigation repeats. The proper fix is via a **static site generator** or via **JavaScript**. For now, copy-paste is acceptable.

---

## Mini-project: "Mini-site with 3 pages"

Build a site with **3 pages**: Home, Projects, Contact. Shared structure:

- `<header>` with `<h1>` (your name) + `<nav>` (links to the 3 pages)
- `<main>` with different content per page
- `<footer>` with copyright and the current year

**Pages:**

- **Home** — welcome message + 2-3 "cards" (can simply be paragraphs with titles) about what's on the site.
- **Projects** — list of school projects (`<ul>` with titles + short descriptions).
- **Contact** — the form from Lesson 04 (reused, no styling).

We're not styling yet — the focus is on **structure** and **navigation**. The look comes in Lesson 06.

??? success "Solution"
    **`index.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Home — Mike's site</title>
    </head>
    <body>
      <header>
        <h1>Mike Ionescu</h1>
        <nav>
          <a href="index.html" aria-current="page">Home</a>
          <a href="projects.html">Projects</a>
          <a href="contact.html">Contact</a>
        </nav>
      </header>

      <main>
        <h2>Welcome!</h2>
        <p>I'm Mike, a student in Chișinău. On this site you'll find
           my school projects and a contact form.</p>

        <section>
          <h3>Projects</h3>
          <p>What I've built at the computer science club.
             <a href="projects.html">See the list</a>.</p>
        </section>

        <section>
          <h3>Contact</h3>
          <p>Got a question? <a href="contact.html">Write to me</a>.</p>
        </section>
      </main>

      <footer>
        <p>© 2026 Mike Ionescu · Chișinău</p>
      </footer>
    </body>
    </html>
    ```

    **`projects.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Projects — Mike's site</title>
    </head>
    <body>
      <header>
        <h1>Mike Ionescu</h1>
        <nav>
          <a href="index.html">Home</a>
          <a href="projects.html" aria-current="page">Projects</a>
          <a href="contact.html">Contact</a>
        </nav>
      </header>

      <main>
        <h2>My projects</h2>
        <ul>
          <li>
            <strong>LED Blink with Arduino</strong> —
            my first program on a microcontroller.
          </li>
          <li>
            <strong>Calculator in Python</strong> —
            console app for arithmetic operations.
          </li>
          <li>
            <strong>"My school" site</strong> —
            HTML/CSS page about my high school.
          </li>
        </ul>
      </main>

      <footer>
        <p>© 2026 Mike Ionescu · Chișinău</p>
      </footer>
    </body>
    </html>
    ```

    **`contact.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Contact — Mike's site</title>
    </head>
    <body>
      <header>
        <h1>Mike Ionescu</h1>
        <nav>
          <a href="index.html">Home</a>
          <a href="projects.html">Projects</a>
          <a href="contact.html" aria-current="page">Contact</a>
        </nav>
      </header>

      <main>
        <h2>Write to me</h2>

        <form action="#" method="POST">
          <p>
            <label for="name">Name *</label><br>
            <input type="text" id="name" name="name"
                   required minlength="2">
          </p>
          <p>
            <label for="email">Email *</label><br>
            <input type="email" id="email" name="email" required>
          </p>
          <p>
            <label for="message">Message *</label><br>
            <textarea id="message" name="message"
                      rows="5" cols="40" required></textarea>
          </p>
          <p>
            <button type="submit">Send</button>
          </p>
        </form>
      </main>

      <footer>
        <p>© 2026 Mike Ionescu · Chișinău</p>
      </footer>
    </body>
    </html>
    ```

---

## Summary

- A modern site = **multiple pages**, each on a single topic.
- Organize the **folders**: HTML at the root, images in `images/`, styles in `styles/`.
- Relative links: `about.html`, `./images/x.png`, `../index.html`.
- Use **semantic** tags: `<header>`, `<nav>`, `<main>`, `<footer>`.
- A single `<main>` per page; `<nav>` for the main menu.
- **`index.html`** is the default page of a folder.
- You can publish for free on **GitHub Pages**, Netlify, or Vercel.

---

**Next step:** [→ Lesson 06: CSS — introduction](06-css-introducere.md)
