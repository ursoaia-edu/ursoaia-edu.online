---
lesson: 19
tags: [web, proiect, portofoliu, html, css, javascript, responsive]
summary: Proiect complet — construiești un site de portofoliu personal modern, responsive, cu navigație sticky și smooth scroll.
---

# Lecția 19 · Proiect: Portofoliu personal

!!! tip "Ce vei exersa"
    - HTML semantic (header, nav, main, section, footer)
    - CSS modern (variabile, flexbox, grid, media queries)
    - Design responsive (desktop, tabletă, telefon)
    - JavaScript simplu (smooth scroll, interacțiuni)
    - Accesibilitate (etichete `alt`, contraste, structură)

---

## Prezentarea proiectului

Vei construi un **site de portofoliu personal** pe o singură pagină, format din 5 secțiuni:

1. **Hero** — antet mare cu numele tău și un slogan
2. **Despre** — scurtă prezentare cu poză și text
3. **Proiecte** — grilă cu 3 carduri de proiecte
4. **Competențe** — listă de etichete (tag cloud)
5. **Contact** — formular simplu

Navigația din partea de sus rămâne lipită (**sticky**) și are **smooth scroll** către fiecare secțiune.
Site-ul arată bine pe PC, tabletă și telefon (**responsive**), iar cardurile au efecte subtile la hover.

**Structura vizuală (simplificat):**

```
┌────────────────────────────────────────────┐
│  [Logo]     Despre  Proiecte  Skills  Contact  │ ← nav sticky
├────────────────────────────────────────────┤
│                                            │
│           EU SUNT ION POPESCU              │
│         Dezvoltator web în formare         │
│             [Vezi proiectele]              │
│                                            │
├────────────────────────────────────────────┤
│  [Poză]     Despre mine...                 │
├────────────────────────────────────────────┤
│  [Card]   [Card]   [Card]                  │
├────────────────────────────────────────────┤
│  [HTML] [CSS] [JS] [Git] [Responsive]      │
├────────────────────────────────────────────┤
│  Formular contact                          │
├────────────────────────────────────────────┤
│  © 2026 Ion Popescu                        │
└────────────────────────────────────────────┘
```

---

## Pasul 1: Structura HTML

Creează folderul `portofoliu/` cu 3 fișiere: `index.html`, `styles.css`, `app.js`.

Începem cu scheletul HTML semantic:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ion Popescu · Portofoliu</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="nav">
    <div class="nav-container">
      <a href="#hero" class="logo">IP</a>
      <nav aria-label="Navigație principală">
        <ul class="nav-links">
          <li><a href="#despre">Despre</a></li>
          <li><a href="#proiecte">Proiecte</a></li>
          <li><a href="#skills">Competențe</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <section id="hero" class="hero">
      <h1>Salut, sunt <span class="accent">Ion Popescu</span></h1>
      <p class="tagline">Dezvoltator web în formare · Pasionat de tehnologie</p>
      <a href="#proiecte" class="btn">Vezi proiectele mele</a>
    </section>

    <section id="despre" class="sectiune">
      <h2>Despre mine</h2>
      <div class="despre-grid">
        <img src="profil.jpg" alt="Portret Ion Popescu" class="avatar">
        <div>
          <p>Sunt elev în clasa a IX-a și învăț dezvoltare web în cadrul cercului de informatică.</p>
          <p>Îmi place să construiesc interfețe frumoase și accesibile.</p>
        </div>
      </div>
    </section>

    <section id="proiecte" class="sectiune">
      <h2>Proiecte</h2>
      <div class="proiecte-grid">
        <!-- carduri aici -->
      </div>
    </section>

    <section id="skills" class="sectiune">
      <h2>Competențe</h2>
      <ul class="skills">
        <!-- etichete aici -->
      </ul>
    </section>

    <section id="contact" class="sectiune">
      <h2>Contact</h2>
      <form class="formular">
        <!-- câmpuri aici -->
      </form>
    </section>
  </main>

  <footer class="footer">
    <p>&copy; 2026 Ion Popescu · Construit cu HTML, CSS și JavaScript</p>
  </footer>

  <script src="app.js"></script>
</body>
</html>
```

!!! note "De ce HTML semantic?"
    Etichetele `header`, `nav`, `main`, `section`, `footer` spun cititoarelor de ecran și motoarelor de căutare **ce rol** are fiecare zonă — nu doar cum arată.

---

## Pasul 2: Reset CSS și variabile

Deschide `styles.css` și începe cu un reset și variabilele de temă:

```css
/* === Reset minimal === */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* === Variabile de temă === */
:root {
  --culoare-primara: #3b82f6;
  --culoare-fundal: #0f172a;
  --culoare-suprafata: #1e293b;
  --culoare-text: #e2e8f0;
  --culoare-text-moale: #94a3b8;
  --culoare-accent: #06b6d4;
  --radius: 12px;
  --tranzitie: 0.25s ease;
  --font-principal: "Inter", system-ui, sans-serif;
}

/* === Stil de bază === */
body {
  font-family: var(--font-principal);
  background: var(--culoare-fundal);
  color: var(--culoare-text);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

img {
  max-width: 100%;
  display: block;
}

a {
  color: var(--culoare-accent);
  text-decoration: none;
  transition: color var(--tranzitie);
}

a:hover {
  color: var(--culoare-primara);
}

h1, h2, h3 {
  line-height: 1.2;
  margin-bottom: 1rem;
}
```

---

## Pasul 3: Navigația sticky

Bara de sus trebuie să rămână vizibilă când derulăm pagina:

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
  color: var(--culoare-text);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 2rem;
}

.nav-links a {
  color: var(--culoare-text-moale);
  font-weight: 500;
}

.nav-links a:hover {
  color: var(--culoare-text);
}
```

---

## Pasul 4: Hero section

Prima impresie: antet mare, pe toată înălțimea ecranului.

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
  color: var(--culoare-primara);
}

.tagline {
  color: var(--culoare-text-moale);
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.85rem 2rem;
  background: var(--culoare-primara);
  color: white;
  border-radius: var(--radius);
  font-weight: 600;
  transition: transform var(--tranzitie), background var(--tranzitie);
}

.btn:hover {
  background: var(--culoare-accent);
  transform: translateY(-2px);
  color: white;
}
```

!!! tip "clamp() — dimensiuni adaptive"
    `clamp(2.5rem, 6vw, 4.5rem)` înseamnă: minim 2.5rem, ideal 6% din lățimea ferestrei, maxim 4.5rem. Textul scalează singur cu ecranul.

---

## Pasul 5: Secțiunea „Despre”

Două coloane pe desktop, una sub alta pe telefon:

```css
.sectiune {
  max-width: 1100px;
  margin: 0 auto;
  padding: 5rem 1.5rem;
}

.sectiune h2 {
  font-size: 2.25rem;
  margin-bottom: 2rem;
  text-align: center;
}

.despre-grid {
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
  border: 3px solid var(--culoare-primara);
}
```

---

## Pasul 6: Grid Proiecte

Înlocuiește comentariul din `#proiecte` cu carduri:

```html
<div class="proiecte-grid">
  <article class="card">
    <img src="proiect-quiz.jpg" alt="Captură din aplicația Quiz">
    <h3>Aplicație Quiz</h3>
    <p>Quiz de cultură generală cu feedback instant și scor final.</p>
    <a href="#">Vezi demo →</a>
  </article>

  <article class="card">
    <img src="proiect-meteo.jpg" alt="Captură din aplicația Meteo">
    <h3>Aplicație Meteo</h3>
    <p>Prognoză meteo pentru orașele României, folosind Open-Meteo API.</p>
    <a href="#">Vezi demo →</a>
  </article>

  <article class="card">
    <img src="proiect-todo.jpg" alt="Captură din lista To-Do">
    <h3>Listă To-Do</h3>
    <p>Gestionare sarcini cu salvare în localStorage.</p>
    <a href="#">Vezi demo →</a>
  </article>
</div>
```

CSS pentru grilă responsivă (fără media queries datorită `auto-fit`):

```css
.proiecte-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.card {
  background: var(--culoare-suprafata);
  border-radius: var(--radius);
  overflow: hidden;
  transition: transform var(--tranzitie), box-shadow var(--tranzitie);
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
  color: var(--culoare-text-moale);
  margin: 0.5rem 0 1rem;
}

.card a {
  display: block;
  padding-bottom: 1.25rem;
  font-weight: 600;
}
```

---

## Pasul 7: Competențe (tag cloud)

Flexbox cu `wrap` face listele să treacă pe rând nou natural:

```html
<ul class="skills">
  <li>HTML5</li>
  <li>CSS3</li>
  <li>JavaScript</li>
  <li>Responsive Design</li>
  <li>Git</li>
  <li>Accesibilitate</li>
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
  background: var(--culoare-suprafata);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 999px;
  font-size: 0.95rem;
  color: var(--culoare-text-moale);
  transition: background var(--tranzitie), color var(--tranzitie);
}

.skills li:hover {
  background: var(--culoare-primara);
  color: white;
}
```

---

## Pasul 8: Formular contact

Reluăm bazele de la Lecția 17 (formular + etichete):

```html
<form class="formular">
  <label>
    Nume
    <input type="text" name="nume" required>
  </label>
  <label>
    Email
    <input type="email" name="email" required>
  </label>
  <label>
    Mesaj
    <textarea name="mesaj" rows="5" required></textarea>
  </label>
  <button type="submit" class="btn">Trimite</button>
</form>
```

```css
.formular {
  max-width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.formular label {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  color: var(--culoare-text-moale);
  font-size: 0.95rem;
}

.formular input,
.formular textarea {
  padding: 0.75rem 1rem;
  background: var(--culoare-suprafata);
  color: var(--culoare-text);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius);
  font-family: inherit;
  font-size: 1rem;
}

.formular input:focus,
.formular textarea:focus {
  outline: 2px solid var(--culoare-primara);
  outline-offset: 2px;
}

.formular button {
  align-self: flex-start;
  border: none;
  cursor: pointer;
}
```

!!! warning "Accesibilitate — etichete"
    Fiecare `input` este înfășurat într-un `<label>`. Cititoarele de ecran anunță corect câmpul iar utilizatorii pot da click pe text pentru a activa câmpul.

---

## Pasul 9: Footer simplu

```css
.footer {
  padding: 2rem 1.5rem;
  text-align: center;
  color: var(--culoare-text-moale);
  font-size: 0.9rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}
```

---

## Pasul 10: Smooth scroll cu JavaScript

În `app.js` adăugăm o singură funcție care transformă clickul pe linkurile interne într-o derulare lină:

```js
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener("click", e => {
    const destinatie = document.querySelector(link.getAttribute("href"));
    if (!destinatie) return;
    e.preventDefault();
    destinatie.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});
```

!!! tip "Alternativă pură CSS"
    Poți pune `html { scroll-behavior: smooth; }` în CSS și scăpa de JavaScript — dar versiunea JS îți lasă loc să adaugi offset-uri sau animații mai târziu.

---

## Pasul 11: Responsive (media queries)

La final, potrivim layoutul pentru telefon. Punem blocul acesta **la sfârșitul** `styles.css`:

```css
@media (max-width: 768px) {
  .nav-links {
    gap: 1rem;
    font-size: 0.9rem;
  }

  .despre-grid {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .avatar {
    margin: 0 auto;
  }

  .sectiune {
    padding: 3rem 1rem;
  }

  .hero h1 {
    font-size: 2.5rem;
  }
}
```

!!! note "Mobile-first sau desktop-first?"
    Aici am scris întâi desktop, apoi am adaptat pentru telefon cu `max-width`. E cea mai simplă abordare pentru începători. În proiectele mari, se preferă **mobile-first** (cu `min-width`), dar principiul e același: testezi pe ecrane diferite.

---

## Codul complet

### `index.html`

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ion Popescu · Portofoliu</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="nav">
    <div class="nav-container">
      <a href="#hero" class="logo">IP</a>
      <nav aria-label="Navigație principală">
        <ul class="nav-links">
          <li><a href="#despre">Despre</a></li>
          <li><a href="#proiecte">Proiecte</a></li>
          <li><a href="#skills">Competențe</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <section id="hero" class="hero">
      <h1>Salut, sunt <span class="accent">Ion Popescu</span></h1>
      <p class="tagline">Dezvoltator web în formare · Pasionat de tehnologie</p>
      <a href="#proiecte" class="btn">Vezi proiectele mele</a>
    </section>

    <section id="despre" class="sectiune">
      <h2>Despre mine</h2>
      <div class="despre-grid">
        <img src="profil.jpg" alt="Portret Ion Popescu" class="avatar">
        <div>
          <p>Sunt elev în clasa a IX-a și învăț dezvoltare web în cadrul cercului de informatică.</p>
          <p>Îmi place să construiesc interfețe frumoase, rapide și accesibile.</p>
        </div>
      </div>
    </section>

    <section id="proiecte" class="sectiune">
      <h2>Proiecte</h2>
      <div class="proiecte-grid">
        <article class="card">
          <img src="proiect-quiz.jpg" alt="Captură din aplicația Quiz">
          <h3>Aplicație Quiz</h3>
          <p>Quiz de cultură generală cu feedback instant și scor final.</p>
          <a href="#">Vezi demo →</a>
        </article>
        <article class="card">
          <img src="proiect-meteo.jpg" alt="Captură din aplicația Meteo">
          <h3>Aplicație Meteo</h3>
          <p>Prognoză meteo pentru orașele României, folosind Open-Meteo API.</p>
          <a href="#">Vezi demo →</a>
        </article>
        <article class="card">
          <img src="proiect-todo.jpg" alt="Captură din lista To-Do">
          <h3>Listă To-Do</h3>
          <p>Gestionare sarcini cu salvare în localStorage.</p>
          <a href="#">Vezi demo →</a>
        </article>
      </div>
    </section>

    <section id="skills" class="sectiune">
      <h2>Competențe</h2>
      <ul class="skills">
        <li>HTML5</li><li>CSS3</li><li>JavaScript</li>
        <li>Responsive Design</li><li>Git</li><li>Accesibilitate</li>
        <li>Flexbox</li><li>CSS Grid</li>
      </ul>
    </section>

    <section id="contact" class="sectiune">
      <h2>Contact</h2>
      <form class="formular">
        <label>Nume<input type="text" name="nume" required></label>
        <label>Email<input type="email" name="email" required></label>
        <label>Mesaj<textarea name="mesaj" rows="5" required></textarea></label>
        <button type="submit" class="btn">Trimite</button>
      </form>
    </section>
  </main>

  <footer class="footer">
    <p>&copy; 2026 Ion Popescu · Construit cu HTML, CSS și JavaScript</p>
  </footer>

  <script src="app.js"></script>
</body>
</html>
```

### `styles.css`

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --culoare-primara: #3b82f6;
  --culoare-fundal: #0f172a;
  --culoare-suprafata: #1e293b;
  --culoare-text: #e2e8f0;
  --culoare-text-moale: #94a3b8;
  --culoare-accent: #06b6d4;
  --radius: 12px;
  --tranzitie: 0.25s ease;
  --font-principal: "Inter", system-ui, sans-serif;
}

body {
  font-family: var(--font-principal);
  background: var(--culoare-fundal);
  color: var(--culoare-text);
  line-height: 1.6;
}

img { max-width: 100%; display: block; }
a { color: var(--culoare-accent); text-decoration: none; transition: color var(--tranzitie); }
a:hover { color: var(--culoare-primara); }
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
.logo { font-weight: 800; font-size: 1.5rem; color: var(--culoare-text); }
.nav-links { list-style: none; display: flex; gap: 2rem; }
.nav-links a { color: var(--culoare-text-moale); font-weight: 500; }
.nav-links a:hover { color: var(--culoare-text); }

.hero {
  min-height: 90vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 2rem;
  background: radial-gradient(circle at 50% 20%, rgba(59, 130, 246, 0.15), transparent 60%);
}
.hero h1 { font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; }
.accent { color: var(--culoare-primara); }
.tagline { color: var(--culoare-text-moale); font-size: 1.25rem; margin-bottom: 2rem; }
.btn {
  display: inline-block; padding: 0.85rem 2rem;
  background: var(--culoare-primara); color: white;
  border-radius: var(--radius); font-weight: 600;
  transition: transform var(--tranzitie), background var(--tranzitie);
}
.btn:hover { background: var(--culoare-accent); transform: translateY(-2px); color: white; }

.sectiune { max-width: 1100px; margin: 0 auto; padding: 5rem 1.5rem; }
.sectiune h2 { font-size: 2.25rem; margin-bottom: 2rem; text-align: center; }

.despre-grid { display: grid; grid-template-columns: 200px 1fr; gap: 2.5rem; align-items: center; }
.avatar {
  width: 200px; height: 200px; border-radius: 50%;
  object-fit: cover; border: 3px solid var(--culoare-primara);
}

.proiecte-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
.card {
  background: var(--culoare-suprafata);
  border-radius: var(--radius); overflow: hidden;
  transition: transform var(--tranzitie), box-shadow var(--tranzitie);
}
.card:hover { transform: translateY(-6px); box-shadow: 0 12px 30px rgba(0,0,0,0.3); }
.card img { width: 100%; height: 180px; object-fit: cover; }
.card h3, .card p, .card a { padding: 0 1.25rem; }
.card h3 { margin-top: 1rem; }
.card p { color: var(--culoare-text-moale); margin: 0.5rem 0 1rem; }
.card a { display: block; padding-bottom: 1.25rem; font-weight: 600; }

.skills {
  list-style: none;
  display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem;
}
.skills li {
  padding: 0.5rem 1.25rem;
  background: var(--culoare-suprafata);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 999px; font-size: 0.95rem;
  color: var(--culoare-text-moale);
  transition: background var(--tranzitie), color var(--tranzitie);
}
.skills li:hover { background: var(--culoare-primara); color: white; }

.formular {
  max-width: 600px; margin: 0 auto;
  display: flex; flex-direction: column; gap: 1rem;
}
.formular label {
  display: flex; flex-direction: column; gap: 0.35rem;
  color: var(--culoare-text-moale); font-size: 0.95rem;
}
.formular input, .formular textarea {
  padding: 0.75rem 1rem;
  background: var(--culoare-suprafata);
  color: var(--culoare-text);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius); font-family: inherit; font-size: 1rem;
}
.formular input:focus, .formular textarea:focus {
  outline: 2px solid var(--culoare-primara); outline-offset: 2px;
}
.formular button { align-self: flex-start; border: none; cursor: pointer; }

.footer {
  padding: 2rem 1.5rem; text-align: center;
  color: var(--culoare-text-moale); font-size: 0.9rem;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
}

@media (max-width: 768px) {
  .nav-links { gap: 1rem; font-size: 0.9rem; }
  .despre-grid { grid-template-columns: 1fr; text-align: center; }
  .avatar { margin: 0 auto; }
  .sectiune { padding: 3rem 1rem; }
  .hero h1 { font-size: 2.5rem; }
}
```

### `app.js`

```js
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener("click", e => {
    const destinatie = document.querySelector(link.getAttribute("href"));
    if (!destinatie) return;
    e.preventDefault();
    destinatie.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});
```

---

## Idei de extindere

1. **Modul întunecat / luminos** — buton care schimbă `data-theme` pe `<html>` și override-uiește variabilele CSS.
2. **Animații la derulare** — `IntersectionObserver` care adaugă clasa `.vizibil` când o secțiune intră în ecran.
3. **Efect de scriere (typing)** — litere care apar una câte una în hero folosind `setInterval` și `textContent`.
4. **Formular funcțional** — trimite emailul printr-un serviciu gratuit (Formspree, Netlify Forms) sau printr-un backend propriu.
5. **Deploy pe GitHub Pages** — `Settings → Pages → Deploy from branch` și site-ul tău e online gratuit.
6. **Imagini optimizate** — folosește formatul `.webp` și atributul `loading="lazy"` pentru imaginile de sub fold.

---

## Rezumat

Ai construit **primul tău site complet**:

- Structură HTML semantică și accesibilă
- Design modern cu variabile CSS și grid responsiv
- Navigație sticky cu smooth scroll
- 5 secțiuni tipice: hero, despre, proiecte, skills, contact

Acum ai un șablon reutilizabil pentru orice site personal, landing page sau prezentare.

---

**Pasul următor:** [→ Proiect: Aplicație Quiz](20-proiect-quiz.md)
