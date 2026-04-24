---
lesson: 8
tags: [web, css, flexbox, grid, layout, responsive]
summary: Construiește layout-uri moderne cu Flexbox (1D) și Grid (2D). Fără float-uri, fără hack-uri.
---

# Lecția 08 · Flexbox și Grid

!!! tip "Ce vei învăța"
    - De ce Flexbox și Grid au înlocuit `float`
    - Cum aliniezi elemente pe o axă cu **Flexbox**
    - Cum construiești layout-uri 2D cu **CSS Grid**
    - Diferențele și când folosești fiecare
    - Trucuri responsive (auto-fit + minmax)

---

## Problema dinainte de 2015

Layout-urile se construiau cu `float: left` + `clear: both` — hack-uri fragile moștenite de la aranjarea imaginilor în text. Centrarea verticală era **imposibilă** fără trucuri cu `table-cell` sau `transform`.

Din 2015 încoace, CSS a primit două instrumente moderne:

- **Flexbox** — aliniere pe **o axă** (1D): ideal pentru meniuri, carduri pe rând, bare de navigație
- **Grid** — layout-uri **2D**: galerii, dashboard-uri, pagini complete

!!! note "Uită de `float` pentru layout"
    `float` este folosit azi **exclusiv** pentru a înfășura textul în jurul unei imagini. Orice altceva → Flexbox sau Grid.

---

## Flexbox — aliniere pe o axă

Activezi Flexbox pe **părinte** cu `display: flex`:

```html
<div class="bara">
  <span>1</span>
  <span>2</span>
  <span>3</span>
</div>
```

```css
.bara {
  display: flex;          /* activează flex pe copiii direcți */
  gap: 1rem;              /* spațiu între copii */
}
```

Copiii devin **flex items** aliniați orizontal.

### Proprietăți pe părinte

```css
.container {
  display: flex;
  flex-direction: row;           /* row (implicit) | column | row-reverse | column-reverse */
  justify-content: flex-start;   /* aliniere pe axa principală */
  align-items: stretch;          /* aliniere pe axa perpendiculară */
  flex-wrap: nowrap;             /* nowrap (implicit) | wrap */
  gap: 1rem;                     /* spațiu între elemente */
}
```

### `justify-content` — axa principală

| Valoare | Efect |
|---------|-------|
| `flex-start` | toate la început (stânga) |
| `center` | centrat |
| `flex-end` | toate la final (dreapta) |
| `space-between` | primul la început, ultimul la final, restul egal între |
| `space-around` | spațiu egal în jurul fiecărui element |
| `space-evenly` | spațiu egal între și la capete |

### `align-items` — axa perpendiculară

| Valoare | Efect |
|---------|-------|
| `stretch` (implicit) | întinse să umple înălțimea |
| `flex-start` | aliniate sus |
| `center` | centrate vertical |
| `flex-end` | aliniate jos |
| `baseline` | aliniate după baza textului |

### Proprietăți pe copii

```css
.element {
  flex: 1;                 /* crește pentru a umple spațiul (shorthand pentru flex-grow: 1) */
  flex-basis: 200px;       /* dimensiunea de bază */
  flex-shrink: 0;          /* 0 = nu se micșorează */
  align-self: flex-end;    /* override pe align-items doar pentru acest element */
}
```

---

## Exemple Flexbox

### 1. Bară de navigație (logo stânga, link-uri dreapta)

```html
<nav class="nav">
  <a class="logo" href="/">Logo</a>
  <ul class="links">
    <li><a href="#">Acasă</a></li>
    <li><a href="#">Despre</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

```css
.nav {
  display: flex;
  justify-content: space-between;   /* logo stânga, meniu dreapta */
  align-items: center;              /* aliniere verticală centrată */
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

### 2. Trei carduri egale pe un rând

```html
<div class="carduri">
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</div>
```

```css
.carduri {
  display: flex;
  gap: 1rem;
}

.card {
  flex: 1;                   /* fiecare card primește o cotă egală */
  padding: 1.5rem;
  background: #f3f4f6;
  border-radius: 8px;
}
```

### 3. Centrare perfectă (orizontal + vertical)

```css
.centrat {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;     /* 100% din înălțimea ferestrei */
}
```

!!! tip "Cea mai simplă centrare din istoria CSS"
    Înainte de Flexbox, centrarea verticală cerea 5–10 linii de hack-uri. Acum sunt trei proprietăți.

---

## Grid — layouts 2D

Activezi Grid pe părinte cu `display: grid`:

```html
<div class="galerie">
  <img src="1.jpg" alt="">
  <img src="2.jpg" alt="">
  <img src="3.jpg" alt="">
  <img src="4.jpg" alt="">
  <img src="5.jpg" alt="">
  <img src="6.jpg" alt="">
</div>
```

```css
.galerie {
  display: grid;
  grid-template-columns: repeat(3, 1fr);   /* 3 coloane egale */
  gap: 1rem;
}
```

### `grid-template-columns` — definește coloanele

```css
/* 3 coloane egale */
grid-template-columns: 1fr 1fr 1fr;

/* Același lucru, shorthand */
grid-template-columns: repeat(3, 1fr);

/* Proporții diferite: 1-2-1 (coloana din mijloc e dublă) */
grid-template-columns: 1fr 2fr 1fr;

/* Amestec: prima fixă, a doua flexibilă, a treia fixă */
grid-template-columns: 200px 1fr 200px;
```

!!! note "`fr` = fracție"
    Unitatea `fr` distribuie **spațiul rămas**. `1fr 2fr` înseamnă 1/3 și 2/3 din spațiul disponibil.

### `grid-template-rows` — definește rândurile

```css
.pagina {
  display: grid;
  grid-template-rows: auto 1fr auto;   /* header, conținut, footer */
  min-height: 100vh;
}
```

### `gap` — spațiu între celule

```css
gap: 1rem;              /* același spațiu pe ambele axe */
gap: 1rem 2rem;         /* rând 1rem, coloană 2rem */
row-gap: 1rem;
column-gap: 2rem;
```

### `grid-column` — un item ocupă mai multe coloane

```css
.hero {
  grid-column: span 2;     /* ocupă 2 coloane */
}

.full-row {
  grid-column: 1 / -1;     /* de la prima la ultima coloană */
}
```

---

## Magia `auto-fit` + `minmax` (responsive)

```css
.galerie {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
```

Ce se întâmplă:

- Fiecare coloană are **minim 250px**, **maxim 1fr** din spațiul disponibil
- `auto-fit` împachetează **atâtea coloane câte încap** în container
- Pe desktop lat → 4 coloane. Pe tabletă → 3. Pe telefon → 1.

!!! tip "Layout responsive fără media queries"
    Această linie înlocuiește zeci de linii de breakpoints. Un truc obligatoriu în arsenalul oricărui dezvoltator web.

---

## Flexbox vs Grid — când folosești ce

| Situație | Instrumentul potrivit |
|----------|------------------------|
| Bară de navigație | **Flexbox** |
| Carduri pe un singur rând | **Flexbox** |
| Centrare orizontală + verticală | **Flexbox** |
| Aliniere butoane pe o linie | **Flexbox** |
| Galerie foto în rânduri și coloane | **Grid** |
| Layout întreaga pagină (header + sidebar + main + footer) | **Grid** |
| Dashboard cu widget-uri | **Grid** |
| Formular cu etichete și câmpuri aliniate | **Grid** |

!!! tip "Le poți combina"
    Cel mai des: **Grid** pentru aranjarea generală a paginii + **Flexbox** în interiorul fiecărei celule (ex. într-un card, flexbox aliniază avatar-ul și textul).

---

## Exerciții

### Exercițiu 1 — Bară de navigație cu Flexbox

Logo în stânga, 4 link-uri în dreapta, toate aliniate vertical.

??? success "Soluție"
    ```html
    <nav class="nav">
      <a class="logo" href="/">Site</a>
      <ul class="links">
        <li><a href="#">Acasă</a></li>
        <li><a href="#">Servicii</a></li>
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

### Exercițiu 2 — Trei carduri de preț egale

```html
<div class="preturi">
  <div class="card">Basic</div>
  <div class="card">Pro</div>
  <div class="card">Enterprise</div>
</div>
```

??? success "Soluție"
    ```css
    .preturi {
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

### Exercițiu 3 — Galerie 3x3 cu Grid

9 imagini dispuse într-o grilă 3x3.

??? success "Soluție"
    ```html
    <div class="galerie">
      <img src="1.jpg" alt="Foto 1">
      <img src="2.jpg" alt="Foto 2">
      <img src="3.jpg" alt="Foto 3">
      <img src="4.jpg" alt="Foto 4">
      <img src="5.jpg" alt="Foto 5">
      <img src="6.jpg" alt="Foto 6">
      <img src="7.jpg" alt="Foto 7">
      <img src="8.jpg" alt="Foto 8">
      <img src="9.jpg" alt="Foto 9">
    </div>
    ```
    ```css
    .galerie {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.5rem;
    }

    .galerie img {
      width: 100%;
      aspect-ratio: 1;       /* pătrat perfect */
      object-fit: cover;     /* fără deformare */
      border-radius: 8px;
    }
    ```

### Exercițiu 4 — Galerie responsive cu `auto-fit`

Aceeași galerie, dar coloanele se adaptează automat la mărimea ecranului.

??? success "Soluție"
    ```css
    .galerie {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.5rem;
    }
    ```
    Testează redimensionând fereastra — numărul de coloane se modifică automat.

---

## Mini-proiect: Galerie foto tip revistă

O galerie responsivă cu 3 coloane pe desktop, titlu suprapus pe imagine, efect hover subtil.

??? success "Soluție"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Galerie</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <h1>Galeria mea</h1>

      <div class="galerie">
        <figure class="card">
          <img src="foto1.jpg" alt="Răsărit peste munte">
          <figcaption>Răsărit la 1500m</figcaption>
        </figure>
        <figure class="card">
          <img src="foto2.jpg" alt="Oraș noaptea">
          <figcaption>Oraș noaptea</figcaption>
        </figure>
        <figure class="card">
          <img src="foto3.jpg" alt="Pădure toamna">
          <figcaption>Pădure toamna</figcaption>
        </figure>
        <figure class="card">
          <img src="foto4.jpg" alt="Plajă tropicală">
          <figcaption>Plajă tropicală</figcaption>
        </figure>
        <figure class="card">
          <img src="foto5.jpg" alt="Deșert la apus">
          <figcaption>Deșert la apus</figcaption>
        </figure>
        <figure class="card">
          <img src="foto6.jpg" alt="Stradă cu felinare">
          <figcaption>Stradă cu felinare</figcaption>
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

    /* Grid responsive — se adaptează automat */
    .galerie {
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
      transition: transform 0.3s ease;   /* detalii în lecția 09 */
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

## Rezumat

- **Flexbox** = aliniere pe **o axă** — perfect pentru meniuri, bare, carduri pe rând
- **Grid** = layout-uri **2D** — galerii, dashboard-uri, structura paginii
- Proprietăți cheie Flexbox: `justify-content`, `align-items`, `gap`, `flex: 1`
- Proprietăți cheie Grid: `grid-template-columns`, `repeat()`, `gap`, `fr`
- `repeat(auto-fit, minmax(250px, 1fr))` = layout responsive fără media queries
- Combinația **Grid (structura) + Flexbox (în celule)** acoperă 99% din cazuri
- **Nu mai folosi `float`** pentru layout

---

**Pasul următor:** [→ Lecția 09: CSS avansat — pseudo-clase, tranziții și animații](09-css-avansat.md)
