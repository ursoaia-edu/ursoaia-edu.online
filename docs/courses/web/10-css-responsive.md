---
lesson: 10
tags: [web, css, responsive, media-queries, mobile-first, viewport]
summary: Un singur site care arată bine pe telefon, tabletă și desktop. Învață media queries și mobile-first.
---

# Lecția 10 · Design responsive

!!! tip "Ce vei învăța"
    - Ce înseamnă design responsive și de ce este obligatoriu
    - Meta tag-ul `viewport` — fără el nu există mobil
    - Unități CSS: `px`, `em`, `rem`, `%`, `vw`, `vh`
    - **Media queries** — stiluri diferite pe baza dimensiunii ecranului
    - Abordarea **mobile-first** și breakpoints comune
    - Imagini și layout-uri care se adaptează

---

## Ce înseamnă responsive

Un site **responsive** este **un singur cod** HTML + CSS care se adaptează automat la orice dimensiune de ecran — telefon, tabletă, laptop, monitor 4K.

**Alternativa veche (și moartă):** un site separat pentru mobil (ex. `m.exemplu.ro`). Două coduri diferite, dublu de mentenanță, probleme SEO.

!!! note "De ce responsive este obligatoriu în 2024+"
    Peste **60% din traficul web mondial** vine de pe telefoane. Un site care arată prost pe mobil pierde majoritatea vizitatorilor. Google de asemenea penalizează site-urile ne-responsive în rezultatele căutării (*mobile-first indexing*).

---

## Viewport meta tag — obligatoriu

**Fără** acest tag, browserul mobil va afișa site-ul la dimensiunea desktop, zoom-uit. Cu el, site-ul se adaptează.

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pagina mea</title>
</head>
```

- `width=device-width` — lățimea viewport-ului = lățimea reală a ecranului
- `initial-scale=1.0` — zoom inițial 100% (fără zoom out)

!!! warning "Uitarea viewport-ului = cel mai frecvent bug mobil"
    Verifică întotdeauna `<head>`. Lipsa lui face ca tot CSS-ul media queries să fie **ignorat** pe telefon.

---

## Unități CSS — care și când

| Unitate | Tip | Bună pentru |
|---------|-----|-------------|
| `px` | absolută | chenare fine, umbre, lucruri care nu trebuie să scaleze |
| `em` | relativă la părinte | padding / margin în componente |
| `rem` | relativă la `<html>` | **font-size**, dimensiuni principale |
| `%` | procent din părinte | `width` în containere |
| `vw` | 1% din lățimea ferestrei | secțiuni „hero”, titluri mari |
| `vh` | 1% din înălțimea ferestrei | înălțime hero, modal-uri full-screen |
| `ch` | lățimea caracterului „0” | lățime coloane de text |

### Cum funcționează `rem`

```css
html {
  font-size: 16px;        /* implicit în toate browserele */
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

Dacă utilizatorul își mărește dimensiunea fontului în browser, toate `rem`-urile cresc **proporțional** — accesibilitate gratuită.

### Exemple `vw` / `vh`

```css
.hero {
  height: 100vh;          /* cât e înălțimea ecranului */
}

.titlu-uriaș {
  font-size: 8vw;         /* scalează cu lățimea ecranului */
}
```

!!! tip "Nu pune tot în `vw`"
    Text cu `font-size: 8vw` devine **minuscul** pe mobil (8 × 375 = 30px) și **enorm** pe monitor 4K (8 × 2560 = 205px). Folosește `clamp()`:
    ```css
    font-size: clamp(2rem, 5vw, 4rem);
    /*          ^min  ^preferat ^max */
    ```

---

## Media queries

Un **media query** aplică reguli CSS doar când o condiție e adevărată (ex. lățimea ecranului sub 768px).

### Sintaxă

```css
/* Stil aplicat DOAR când ecranul e ≤ 768px (telefon + tabletă mică) */
@media (max-width: 768px) {
  .container {
    padding: 1rem;
  }

  nav {
    flex-direction: column;
  }
}
```

### Operatori

```css
/* Până la 767px */
@media (max-width: 767px) { ... }

/* De la 768px în sus */
@media (min-width: 768px) { ... }

/* Între 768px și 1024px */
@media (min-width: 768px) and (max-width: 1024px) { ... }

/* Orientare */
@media (orientation: landscape) { ... }
@media (orientation: portrait)  { ... }

/* Preferință pentru mod întunecat */
@media (prefers-color-scheme: dark) { ... }
```

---

## Mobile-first — de ce și cum

Există două abordări:

### Desktop-first (veche)

```css
/* Stil implicit pentru desktop */
.card { width: 400px; }

/* Apoi restrânge pentru ecrane mai mici */
@media (max-width: 767px) {
  .card { width: 100%; }
}
```

### Mobile-first (modernă, recomandată)

```css
/* Stil implicit pentru mobil */
.card { width: 100%; }

/* Apoi lărgește pentru ecrane mai mari */
@media (min-width: 768px) {
  .card { width: 400px; }
}
```

**De ce mobile-first câștigă:**

- Mobilul este **cazul cel mai constrâns** — mai ușor să adaugi features pe ecrane mari decât să le îndepărtezi
- CSS-ul implicit e cel mai simplu (fără overrides)
- Performanță mai bună pe telefoane (CSS pe desktop nu se încarcă inutil)

---

## Breakpoints comune

Valori standard din industrie:

| Breakpoint | Dispozitiv |
|------------|-----------|
| `576px` | telefon mare |
| `768px` | tabletă (portrait) |
| `992px` | laptop mic / tabletă landscape |
| `1200px` | desktop |
| `1400px` | monitor lat |

```css
/* Mobile-first structure */

/* Stil implicit = mobil (0–575px) */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

/* Tabletă */
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

/* Desktop */
@media (min-width: 1200px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

!!! note "Nu copia orbește breakpoints"
    Cele de mai sus sunt **ghid**, nu regulă. Alege breakpoints **bazate pe conținut**: dacă designul tău „se strică” la 900px, pune breakpoint la 900px, nu la 992px.

---

## Imagini responsive

### `max-width: 100%` — trucul esențial

```css
img {
  max-width: 100%;
  height: auto;
}
```

- Imaginea **nu depășește niciodată** lățimea containerului
- `height: auto` păstrează proporțiile

### `<picture>` — imagini diferite pentru ecrane diferite

```html
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.jpg">
  <source media="(min-width: 600px)"  srcset="hero-tablet.jpg">
  <img src="hero-mobile.jpg" alt="Descriere">
</picture>
```

Browserul descarcă **doar** imaginea potrivită → trafic economisit pe mobil.

### `srcset` — rezoluții diferite

```html
<img
  src="foto.jpg"
  srcset="foto-1x.jpg 1x, foto-2x.jpg 2x"
  alt="...">
```

Ecrane Retina primesc versiunea de 2x; ecrane normale pe cea de 1x.

---

## Grid / Flexbox responsive

### `auto-fit` (din lecția 08) este natural responsive

```css
.carduri {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
```

Pe mobil → o coloană. Pe tabletă → 2. Pe desktop → 3+. Fără media queries.

### Flexbox cu `wrap`

```css
.nav-links {
  display: flex;
  flex-wrap: wrap;     /* trec pe rând nou dacă nu încap */
  gap: 1rem;
}
```

---

## Ascunderea/afișarea elementelor

```css
/* Afișează doar pe desktop */
.meniu-desktop {
  display: none;
}

@media (min-width: 768px) {
  .meniu-desktop {
    display: flex;
  }
}

/* Afișează doar pe mobil */
.hamburger {
  display: block;
}

@media (min-width: 768px) {
  .hamburger {
    display: none;
  }
}
```

!!! warning "Nu ascunde conținut important"
    `display: none` scoate elementul și din **screen-reader**. Nu ascunde conținut critic (ex. link „Contact”) doar pentru a face designul mai curat pe mobil — găsește o altă soluție (ex. meniu hamburger).

---

## Cum testezi designul responsive

1. **DevTools** (F12 în Chrome/Firefox) → iconița **Toggle device toolbar** (Ctrl+Shift+M / Cmd+Shift+M)
2. Alege un dispozitiv din dropdown (iPhone 14, iPad, Galaxy S22 etc.)
3. Redimensionează manual bara — vei vedea în timp real unde se „strică” designul
4. Verifică la breakpoints critice: **375px** (iPhone), **768px** (iPad), **1440px** (laptop)

!!! tip "Testează și pe un telefon real"
    Simulatorul din DevTools este bun, dar **niciodată** nu înlocuiește testarea pe un telefon real — viteza de atingere, gesturile, viteza de încărcare sunt diferite.

---

## Exerciții

### Exercițiu 1 — Card care își schimbă lățimea

Card de 300px pe desktop, 100% pe mobil (sub 768px).

??? success "Soluție"
    ```css
    .card {
      /* Mobile-first: lățimea implicită e 100% */
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

### Exercițiu 2 — Navigație orizontală → verticală

Pe desktop link-urile sunt pe o linie. Pe mobil se aliniază vertical (coloană).

??? success "Soluție"
    ```html
    <nav>
      <ul class="nav-links">
        <li><a href="#">Acasă</a></li>
        <li><a href="#">Despre</a></li>
        <li><a href="#">Servicii</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    ```
    ```css
    .nav-links {
      display: flex;
      flex-direction: column;   /* implicit pe mobil = coloană */
      gap: 0.5rem;
      list-style: none;
      padding: 0;
      margin: 0;
    }

    @media (min-width: 768px) {
      .nav-links {
        flex-direction: row;    /* pe desktop = orizontal */
        gap: 2rem;
      }
    }
    ```

### Exercițiu 3 — Ascunde imaginea pe mobil

O imagine decorativă trebuie să dispară sub 768px.

??? success "Soluție"
    ```css
    .imagine-decor {
      display: none;
    }

    @media (min-width: 768px) {
      .imagine-decor {
        display: block;
      }
    }
    ```
    Dacă imaginea are conținut informativ, folosește în schimb `<picture>` cu o versiune optimizată pentru mobil — **nu** o ascunde complet.

---

## Mini-proiect: Pagină responsive completă

Pagină landing cu hero, grid de 3 carduri și navigație — toate se adaptează perfect la mobil, tabletă și desktop.

??? success "Soluție"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Ursoaia Edu — Cursuri</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <header class="site-header">
        <a class="logo" href="/">Ursoaia Edu</a>
        <nav>
          <ul class="nav-links">
            <li><a href="#">Cursuri</a></li>
            <li><a href="#">Proiecte</a></li>
            <li><a href="#">Despre</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </header>

      <main>
        <section class="hero">
          <h1>Învață web de la zero</h1>
          <p>Cursuri practice pentru gimnaziu și liceu.</p>
          <a class="cta" href="#">Începe acum</a>
        </section>

        <section class="cursuri">
          <article class="card">
            <h2>HTML</h2>
            <p>Structura paginilor web, taguri, semantică.</p>
          </article>
          <article class="card">
            <h2>CSS</h2>
            <p>Stilizare modernă: flexbox, grid, animații.</p>
          </article>
          <article class="card">
            <h2>JavaScript</h2>
            <p>Interactivitate, DOM, evenimente.</p>
          </article>
        </section>
      </main>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    /* ---------- Reset + baza ---------- */
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
      flex-direction: column;     /* coloană pe mobil */
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

    /* Desktop: header orizontal */
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
      /* Scalează lin între 2rem și 3.5rem, în funcție de lățime */
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

    /* ---------- Grid de cursuri ---------- */
    .cursuri {
      display: grid;
      grid-template-columns: 1fr;      /* 1 coloană pe mobil */
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

    /* Tabletă: 2 coloane */
    @media (min-width: 768px) {
      .cursuri {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        padding: 3rem 2rem;
      }
    }

    /* Desktop: 3 coloane */
    @media (min-width: 1024px) {
      .cursuri {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    /* ---------- Accesibilitate ---------- */
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

    **Ce folosește:**

    - Mobile-first: CSS-ul implicit e pentru mobil, media queries adaugă stiluri pentru ecrane mai mari
    - `clamp(2rem, 5vw, 3.5rem)` — titlul hero scalează lin
    - Grid cu 3 breakpoints: 1 → 2 → 3 coloane
    - `box-sizing: border-box` global
    - Focus vizibil pentru accesibilitate cu tastatura
    - `prefers-reduced-motion` respectat

---

## Rezumat

- **Viewport meta tag** e **obligatoriu** pentru orice site modern
- Unitățile `rem` (font-size) și `%` / `fr` (layout) sunt cele mai potrivite pentru responsive
- `clamp(min, preferat, max)` scalează lin între două limite
- **Media queries** adaptează stilurile la dimensiunea ecranului
- **Mobile-first** (`min-width`) e abordarea modernă — începi de la telefon
- Breakpoints ghid: **576px**, **768px**, **992px**, **1200px** (alege în funcție de conținut)
- `img { max-width: 100%; height: auto; }` — imagini care nu depășesc containerul
- `auto-fit + minmax` din Grid = layout responsive fără media queries
- Testează în DevTools cu **Toggle device toolbar**

---

**Pasul următor:** [→ Lecția 11: Introducere în JavaScript](11-js-introducere.md)
