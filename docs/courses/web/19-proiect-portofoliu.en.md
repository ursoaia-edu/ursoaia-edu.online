---
lesson: 19
tags: [web, project, portfolio, html, css, javascript, responsive]
summary: Complete project — build a modern, responsive personal portfolio site, with sticky navigation and smooth scroll.
---

# Lesson 19 · Project: Personal portfolio

!!! tip "What you'll practice"
    - Semantic HTML (header, nav, main, section, footer)
    - Modern CSS (variables, flexbox, grid, media queries)
    - Responsive design (desktop, tablet, phone)
    - Simple JavaScript (smooth scroll, interactions)
    - Accessibility (`alt` labels, contrast, structure)

---

## Project overview

You will build a **personal portfolio site** on a single page, made up of 5 sections:

1. **Hero** — large header with your name and a tagline
2. **About** — short introduction with photo and text
3. **Projects** — grid with 3 project cards
4. **Skills** — list of tags (tag cloud)
5. **Contact** — simple form

The top navigation stays stuck (**sticky**) and has **smooth scroll** to each section.
The site looks good on PC, tablet and phone (**responsive**), and the cards have subtle hover effects.

**Visual structure (simplified):**

```
┌────────────────────────────────────────────┐
│  [Logo]     About  Projects  Skills  Contact  │ ← sticky nav
├────────────────────────────────────────────┤
│                                            │
│             I AM JOHN SMITH                │
│         Web developer in training          │
│             [See projects]                 │
│                                            │
├────────────────────────────────────────────┤
│  [Photo]    About me...                    │
├────────────────────────────────────────────┤
│  [Card]   [Card]   [Card]                  │
├────────────────────────────────────────────┤
│  [HTML] [CSS] [JS] [Git] [Responsive]      │
├────────────────────────────────────────────┤
│  Contact form                              │
├────────────────────────────────────────────┤
│  © 2026 John Smith                         │
└────────────────────────────────────────────┘
```

---

## Step 1: HTML structure

Create the `portfolio/` folder with 3 files: `index.html`, `styles.css`, `app.js`.

We start with a semantic HTML skeleton:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>John Smith · Portfolio</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="nav">
    <div class="nav-container">
      <a href="#hero" class="logo">JS</a>
      <nav aria-label="Main navigation">
        <ul class="nav-links">
          <li><a href="#about">About</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <section id="hero" class="hero">
      <h1>Hi, I'm <span class="accent">John Smith</span></h1>
      <p class="tagline">Web developer in training · Passionate about technology</p>
      <a href="#projects" class="btn">See my projects</a>
    </section>

    <section id="about" class="section">
      <h2>About me</h2>
      <div class="about-grid">
        <img src="profile.jpg" alt="Portrait of John Smith" class="avatar">
        <div>
          <p>I'm a 9th grade student and I learn web development at the computer science club.</p>
          <p>I love building beautiful and accessible interfaces.</p>
        </div>
      </div>
    </section>

    <section id="projects" class="section">
      <h2>Projects</h2>
      <div class="projects-grid">
        <!-- cards here -->
      </div>
    </section>

    <section id="skills" class="section">
      <h2>Skills</h2>
      <ul class="skills">
        <!-- tags here -->
      </ul>
    </section>

    <section id="contact" class="section">
      <h2>Contact</h2>
      <form class="form">
        <!-- fields here -->
      </form>
    </section>
  </main>

  <footer class="footer">
    <p>&copy; 2026 John Smith · Built with HTML, CSS and JavaScript</p>
  </footer>

  <script src="app.js"></script>
</body>
</html>
```

!!! note "Why semantic HTML?"
    The tags `header`, `nav`, `main`, `section`, `footer` tell screen readers and search engines **what role** each area has — not just how it looks.

---

## Step 2: CSS reset and variables

Open `styles.css` and start with a reset and the theme variables:

```css
/* === Minimal reset === */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* === Theme variables === */
:root {
  --color-primary: #3b82f6;
  --color-background: #0f172a;
  --color-surface: #1e293b;
  --color-text: #e2e8f0;
  --color-text-soft: #94a3b8;
  --color-accent: #06b6d4;
  --radius: 12px;
  --transition: 0.25s ease;
  --font-main: "Inter", system-ui, sans-serif;
}

/* === Base style === */
body {
  font-family: var(--font-main);
  background: var(--color-background);
  color: var(--color-text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

img {
  max-width: 100%;
  display: block;
}

a {
  color: var(--color-accent);
  text-decoration: none;
  transition: color var(--transition);
}

a:hover {
  color: var(--color-primary);
}

h1, h2, h3 {
  line-height: 1.2;
  margin-bottom: 1rem;
}
```

---

## Step 3: Sticky navigation

The top bar must stay visible when we scroll the page:

```css
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.nav-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  font-weight: 800;
  font-size: 1.5rem;
  color: var(--color-text);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 2rem;
}

.nav-links a {
  color: var(--color-text-soft);
  font-weight: 500;
}

.nav-links a:hover {
  color: var(--color-text);
}
```

---

## Step 4: Hero section

First impression: large header, full screen height.

```css
.hero {
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  background: radial-gradient(circle at 50% 20%, rgba(59, 130, 246, 0.15), transparent 60%);
}

.hero h1 {
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 800;
}

.accent {
  color: var(--color-primary);
}

.tagline {
  color: var(--color-text-soft);
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.85rem 2rem;
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius);
  font-weight: 600;
  transition: transform var(--transition), background var(--transition);
}

.btn:hover {
  background: var(--color-accent);
  transform: translateY(-2px);
  color: white;
}
```

!!! tip "clamp() — adaptive sizes"
    `clamp(2.5rem, 6vw, 4.5rem)` means: minimum 2.5rem, ideal 6% of the window width, maximum 4.5rem. The text scales by itself with the screen.

---

## Step 5: "About" section

Two columns on desktop, one below the other on phone:

```css
.section {
  max-width: 1100px;
  margin: 0 auto;
  padding: 5rem 1.5rem;
}

.section h2 {
  font-size: 2.25rem;
  margin-bottom: 2rem;
  text-align: center;
}

.about-grid {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 2.5rem;
  align-items: center;
}

.avatar {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--color-primary);
}
```

---

## Step 6: Projects grid

Replace the comment in `#projects` with cards:

```html
<div class="projects-grid">
  <article class="card">
    <img src="project-quiz.jpg" alt="Screenshot of the Quiz app">
    <h3>Quiz App</h3>
    <p>General knowledge quiz with instant feedback and final score.</p>
    <a href="#">See demo →</a>
  </article>

  <article class="card">
    <img src="project-weather.jpg" alt="Screenshot of the Weather app">
    <h3>Weather App</h3>
    <p>Weather forecast for cities, using the Open-Meteo API.</p>
    <a href="#">See demo →</a>
  </article>

  <article class="card">
    <img src="project-todo.jpg" alt="Screenshot of the To-Do list">
    <h3>To-Do List</h3>
    <p>Task management with localStorage persistence.</p>
    <a href="#">See demo →</a>
  </article>
</div>
```

CSS for a responsive grid (no media queries thanks to `auto-fit`):

```css
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.card {
  background: var(--color-surface);
  border-radius: var(--radius);
  overflow: hidden;
  transition: transform var(--transition), box-shadow var(--transition);
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.3);
}

.card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.card h3,
.card p,
.card a {
  padding: 0 1.25rem;
}

.card h3 {
  margin-top: 1rem;
}

.card p {
  color: var(--color-text-soft);
  margin: 0.5rem 0 1rem;
}

.card a {
  display: block;
  padding-bottom: 1.25rem;
  font-weight: 600;
}
```

---

## Step 7: Skills (tag cloud)

Flexbox with `wrap` makes lists go to a new row naturally:

```html
<ul class="skills">
  <li>HTML5</li>
  <li>CSS3</li>
  <li>JavaScript</li>
  <li>Responsive Design</li>
  <li>Git</li>
  <li>Accessibility</li>
  <li>Flexbox</li>
  <li>CSS Grid</li>
</ul>
```

```css
.skills {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.75rem;
}

.skills li {
  padding: 0.5rem 1.25rem;
  background: var(--color-surface);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  font-size: 0.95rem;
  color: var(--color-text-soft);
  transition: background var(--transition), color var(--transition);
}

.skills li:hover {
  background: var(--color-primary);
  color: white;
}
```

---

## Step 8: Contact form

We reuse the basics from Lesson 17 (form + labels):

```html
<form class="form">
  <label>
    Name
    <input type="text" name="name" required>
  </label>
  <label>
    Email
    <input type="email" name="email" required>
  </label>
  <label>
    Message
    <textarea name="message" rows="5" required></textarea>
  </label>
  <button type="submit" class="btn">Send</button>
</form>
```

```css
.form {
  max-width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form label {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  color: var(--color-text-soft);
  font-size: 0.95rem;
}

.form input,
.form textarea {
  padding: 0.75rem 1rem;
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius);
  font-family: inherit;
  font-size: 1rem;
}

.form input:focus,
.form textarea:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.form button {
  align-self: flex-start;
  border: none;
  cursor: pointer;
}
```

!!! warning "Accessibility — labels"
    Each `input` is wrapped in a `<label>`. Screen readers announce the field correctly and users can click the text to focus the field.

---

## Step 9: Simple footer

```css
.footer {
  padding: 2rem 1.5rem;
  text-align: center;
  color: var(--color-text-soft);
  font-size: 0.9rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}
```

---

## Step 10: Smooth scroll with JavaScript

In `app.js` we add a single function that turns clicks on internal links into smooth scrolling:

```js
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener("click", e => {
    const destination = document.querySelector(link.getAttribute("href"));
    if (!destination) return;
    e.preventDefault();
    destination.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});
```

!!! tip "Pure CSS alternative"
    You can put `html { scroll-behavior: smooth; }` in CSS and skip the JavaScript — but the JS version leaves room for offsets or animations later.

---

## Step 11: Responsive (media queries)

At the end, we adjust the layout for phone. We put this block **at the end** of `styles.css`:

```css
@media (max-width: 768px) {
  .nav-links {
    gap: 1rem;
    font-size: 0.9rem;
  }

  .about-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .avatar {
    margin: 0 auto;
  }

  .section {
    padding: 3rem 1rem;
  }

  .hero h1 {
    font-size: 2.5rem;
  }
}
```

!!! note "Mobile-first or desktop-first?"
    Here we wrote desktop first, then adapted for phone with `max-width`. It's the simplest approach for beginners. In big projects, **mobile-first** (with `min-width`) is preferred, but the principle is the same: you test on different screens.

---

## Complete code

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>John Smith · Portfolio</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="nav">
    <div class="nav-container">
      <a href="#hero" class="logo">JS</a>
      <nav aria-label="Main navigation">
        <ul class="nav-links">
          <li><a href="#about">About</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <section id="hero" class="hero">
      <h1>Hi, I'm <span class="accent">John Smith</span></h1>
      <p class="tagline">Web developer in training · Passionate about technology</p>
      <a href="#projects" class="btn">See my projects</a>
    </section>

    <section id="about" class="section">
      <h2>About me</h2>
      <div class="about-grid">
        <img src="profile.jpg" alt="Portrait of John Smith" class="avatar">
        <div>
          <p>I'm a 9th grade student and I learn web development at the computer science club.</p>
          <p>I love building beautiful, fast and accessible interfaces.</p>
        </div>
      </div>
    </section>

    <section id="projects" class="section">
      <h2>Projects</h2>
      <div class="projects-grid">
        <article class="card">
          <img src="project-quiz.jpg" alt="Screenshot of the Quiz app">
          <h3>Quiz App</h3>
          <p>General knowledge quiz with instant feedback and final score.</p>
          <a href="#">See demo →</a>
        </article>
        <article class="card">
          <img src="project-weather.jpg" alt="Screenshot of the Weather app">
          <h3>Weather App</h3>
          <p>Weather forecast for cities, using the Open-Meteo API.</p>
          <a href="#">See demo →</a>
        </article>
        <article class="card">
          <img src="project-todo.jpg" alt="Screenshot of the To-Do list">
          <h3>To-Do List</h3>
          <p>Task management with localStorage persistence.</p>
          <a href="#">See demo →</a>
        </article>
      </div>
    </section>

    <section id="skills" class="section">
      <h2>Skills</h2>
      <ul class="skills">
        <li>HTML5</li><li>CSS3</li><li>JavaScript</li>
        <li>Responsive Design</li><li>Git</li><li>Accessibility</li>
        <li>Flexbox</li><li>CSS Grid</li>
      </ul>
    </section>

    <section id="contact" class="section">
      <h2>Contact</h2>
      <form class="form">
        <label>Name<input type="text" name="name" required></label>
        <label>Email<input type="email" name="email" required></label>
        <label>Message<textarea name="message" rows="5" required></textarea></label>
        <button type="submit" class="btn">Send</button>
      </form>
    </section>
  </main>

  <footer class="footer">
    <p>&copy; 2026 John Smith · Built with HTML, CSS and JavaScript</p>
  </footer>

  <script src="app.js"></script>
</body>
</html>
```

### `styles.css`

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --color-primary: #3b82f6;
  --color-background: #0f172a;
  --color-surface: #1e293b;
  --color-text: #e2e8f0;
  --color-text-soft: #94a3b8;
  --color-accent: #06b6d4;
  --radius: 12px;
  --transition: 0.25s ease;
  --font-main: "Inter", system-ui, sans-serif;
}

body {
  font-family: var(--font-main);
  background: var(--color-background);
  color: var(--color-text);
  line-height: 1.6;
}

img { max-width: 100%; display: block; }
a { color: var(--color-accent); text-decoration: none; transition: color var(--transition); }
a:hover { color: var(--color-primary); }
h1, h2, h3 { line-height: 1.2; margin-bottom: 1rem; }

.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
.nav-container {
  max-width: 1100px; margin: 0 auto;
  padding: 1rem 1.5rem;
  display: flex; align-items: center; justify-content: space-between;
}
.logo { font-weight: 800; font-size: 1.5rem; color: var(--color-text); }
.nav-links { list-style: none; display: flex; gap: 2rem; }
.nav-links a { color: var(--color-text-soft); font-weight: 500; }
.nav-links a:hover { color: var(--color-text); }

.hero {
  min-height: 90vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 2rem;
  background: radial-gradient(circle at 50% 20%, rgba(59, 130, 246, 0.15), transparent 60%);
}
.hero h1 { font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; }
.accent { color: var(--color-primary); }
.tagline { color: var(--color-text-soft); font-size: 1.25rem; margin-bottom: 2rem; }
.btn {
  display: inline-block; padding: 0.85rem 2rem;
  background: var(--color-primary); color: white;
  border-radius: var(--radius); font-weight: 600;
  transition: transform var(--transition), background var(--transition);
}
.btn:hover { background: var(--color-accent); transform: translateY(-2px); color: white; }

.section { max-width: 1100px; margin: 0 auto; padding: 5rem 1.5rem; }
.section h2 { font-size: 2.25rem; margin-bottom: 2rem; text-align: center; }

.about-grid { display: grid; grid-template-columns: 200px 1fr; gap: 2.5rem; align-items: center; }
.avatar {
  width: 200px; height: 200px; border-radius: 50%;
  object-fit: cover; border: 3px solid var(--color-primary);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
.card {
  background: var(--color-surface);
  border-radius: var(--radius); overflow: hidden;
  transition: transform var(--transition), box-shadow var(--transition);
}
.card:hover { transform: translateY(-6px); box-shadow: 0 12px 30px rgba(0,0,0,0.3); }
.card img { width: 100%; height: 180px; object-fit: cover; }
.card h3, .card p, .card a { padding: 0 1.25rem; }
.card h3 { margin-top: 1rem; }
.card p { color: var(--color-text-soft); margin: 0.5rem 0 1rem; }
.card a { display: block; padding-bottom: 1.25rem; font-weight: 600; }

.skills {
  list-style: none;
  display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem;
}
.skills li {
  padding: 0.5rem 1.25rem;
  background: var(--color-surface);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 999px; font-size: 0.95rem;
  color: var(--color-text-soft);
  transition: background var(--transition), color var(--transition);
}
.skills li:hover { background: var(--color-primary); color: white; }

.form {
  max-width: 600px; margin: 0 auto;
  display: flex; flex-direction: column; gap: 1rem;
}
.form label {
  display: flex; flex-direction: column; gap: 0.35rem;
  color: var(--color-text-soft); font-size: 0.95rem;
}
.form input, .form textarea {
  padding: 0.75rem 1rem;
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius); font-family: inherit; font-size: 1rem;
}
.form input:focus, .form textarea:focus {
  outline: 2px solid var(--color-primary); outline-offset: 2px;
}
.form button { align-self: flex-start; border: none; cursor: pointer; }

.footer {
  padding: 2rem 1.5rem; text-align: center;
  color: var(--color-text-soft); font-size: 0.9rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

@media (max-width: 768px) {
  .nav-links { gap: 1rem; font-size: 0.9rem; }
  .about-grid { grid-template-columns: 1fr; text-align: center; }
  .avatar { margin: 0 auto; }
  .section { padding: 3rem 1rem; }
  .hero h1 { font-size: 2.5rem; }
}
```

### `app.js`

```js
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener("click", e => {
    const destination = document.querySelector(link.getAttribute("href"));
    if (!destination) return;
    e.preventDefault();
    destination.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});
```

---

## Ideas to extend

1. **Dark / light mode** — button that changes `data-theme` on `<html>` and overrides the CSS variables.
2. **Scroll animations** — `IntersectionObserver` that adds the `.visible` class when a section enters the screen.
3. **Typing effect** — letters that appear one by one in the hero using `setInterval` and `textContent`.
4. **Working form** — send the email through a free service (Formspree, Netlify Forms) or through your own backend.
5. **Deploy to GitHub Pages** — `Settings → Pages → Deploy from branch` and your site is online for free.
6. **Optimized images** — use the `.webp` format and the `loading="lazy"` attribute for images below the fold.

---

## Summary

You've built **your first complete site**:

- Semantic and accessible HTML structure
- Modern design with CSS variables and a responsive grid
- Sticky navigation with smooth scroll
- 5 typical sections: hero, about, projects, skills, contact

Now you have a reusable template for any personal site, landing page or presentation.

---

**Next step:** [→ Project: Quiz App](20-proiect-quiz.md)
