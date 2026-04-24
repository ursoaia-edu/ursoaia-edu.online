---
lesson: 6
tags: [web, css, selectori, culori, fonturi, stilizare]
summary: Învață CSS de la zero — cum stilizezi HTML-ul cu selectori, culori, fonturi și text.
---

# Lecția 06 · CSS: introducere

!!! tip "Ce vei învăța"
    - Ce este CSS și cum îl incluzi în pagină
    - Anatomia unei reguli CSS și selectorii de bază
    - Cum se aleg culorile (nume, hex, rgb, hsl)
    - Proprietăți pentru text și fonturi
    - Cum adaugi fonturi Google Fonts

---

## Ce este CSS

**CSS** (Cascading Style Sheets) este limbajul care stilizează paginile web. Dacă HTML definește **structura** (titluri, paragrafe, liste), CSS se ocupă de **aspect** (culori, fonturi, spațieri, layout).

!!! note "O analogie simplă"
    - **HTML** = oasele și organele (scheletul paginii)
    - **CSS** = hainele, frizura, machiajul (cum arată)
    - **JavaScript** = mușchii care o fac să se miște

Separarea dintre structură și aspect înseamnă că poți schimba complet felul în care arată un site fără să modifici o singură linie de HTML.

---

## Trei moduri de a include CSS

### 1. Inline — direct pe element

```html
<p style="color: red;">Text roșu</p>
```

Se scrie stilul direct în atributul `style`. **Evită** această metodă — este greu de mentenat, nu se poate refolosi și amestecă structura cu aspectul.

### 2. Internal — în `<head>`

```html
<head>
  <style>
    p {
      color: red;
    }
  </style>
</head>
```

OK pentru pagini mici sau pentru teste rapide. Nu se poate refolosi între mai multe pagini.

### 3. External — fișier separat (recomandat)

```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

Și în fișierul `styles.css`:

```css
p {
  color: red;
}
```

!!! tip "Folosește întotdeauna CSS extern"
    Un singur fișier `styles.css` poate stiliza zeci de pagini. Când vrei să schimbi culoarea principală, o schimbi într-un singur loc.

---

## Anatomia unei reguli CSS

```css
selector {
  proprietate: valoare;
  proprietate2: valoare2;
}
```

Exemplu:

```css
h1 {
  color: navy;
  font-size: 32px;
}
```

- **selector**: ce element(e) stilizezi (`h1`)
- **proprietate**: ce schimbi (`color`, `font-size`)
- **valoare**: cum schimbi (`navy`, `32px`)
- Fiecare linie se termină cu `;`
- Blocul este delimitat de `{ }`

---

## Selectorii de bază

| Selector | Sintaxă | Selectează |
|----------|---------|------------|
| Element | `p` | toate `<p>` |
| Clasă | `.buton` | elementele cu `class="buton"` |
| ID | `#header` | elementul cu `id="header"` (unic) |
| Universal | `*` | toate elementele |
| Grupare | `h1, h2, h3` | toate trei tipurile |
| Descendent | `article p` | `<p>` din interiorul `<article>` |
| Copil direct | `nav > a` | `<a>` copil direct al `<nav>` |

```css
/* Element: toate paragrafele */
p {
  color: #333;
}

/* Clasă: reutilizabilă, se aplică cu class="buton" */
.buton {
  background-color: royalblue;
  color: white;
}

/* ID: unic pe pagină, se aplică cu id="header" */
#header {
  background-color: black;
}

/* Grupare: aceleași stiluri pentru mai multe elemente */
h1, h2, h3 {
  font-family: serif;
}

/* Descendent: doar paragrafele din articole */
article p {
  line-height: 1.7;
}
```

---

## Specificitate — cine câștigă

Dacă două reguli vizează același element, câștigă cea mai **specifică**:

```
element  <  clasă  <  id
   1     <   10   <  100
```

```css
p { color: blue; }           /* specificitate: 1 */
.text { color: green; }      /* specificitate: 10 */
#titlu { color: red; }       /* specificitate: 100 — câștigă */
```

!!! warning "Evită `!important`"
    `color: red !important;` forțează regula să câștige oricum. Folosit des → CSS devine imposibil de întreținut. Rezervă-l pentru cazuri extreme.

---

## Culori

### Nume predefinite

```css
color: red;
color: tomato;
color: rebeccapurple;
color: steelblue;
```

Există peste 140 de nume standard ([listă completă](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)).

### Hexazecimal

```css
color: #ff0000;   /* roșu */
color: #00ff00;   /* verde */
color: #0000ff;   /* albastru */
color: #f00;      /* scurt = #ff0000 */
```

Format: `#RRGGBB` — fiecare pereche este valoare 00–FF (0–255) pentru roșu, verde, albastru.

### RGB și RGBA

```css
color: rgb(255, 0, 0);            /* roșu pur */
color: rgba(255, 0, 0, 0.5);      /* roșu la 50% opacitate */
```

`rgba` are un al patrulea parametru — **alpha** (transparența), între 0 și 1.

### HSL

```css
color: hsl(0, 100%, 50%);         /* roșu */
color: hsl(120, 100%, 50%);       /* verde */
color: hsl(240, 100%, 50%);       /* albastru */
```

- **H** (hue) — nuanța, 0–360 (ca pe un cerc cromatic)
- **S** (saturation) — saturația, 0%–100%
- **L** (lightness) — luminozitatea, 0% (negru) – 100% (alb)

!!! tip "HSL e mai intuitiv"
    Vrei același roșu, dar mai deschis? Schimbi doar `L` de la 50% la 70%. Cu hex ar trebui să calculezi.

---

## Proprietăți pentru text

```css
p {
  color: #333;                         /* culoarea textului */
  background-color: #fffbea;           /* fundalul */
  font-family: "Inter", Arial, sans-serif;
  font-size: 16px;
  font-weight: 400;                    /* normal=400, bold=700 */
  text-align: left;                    /* left, center, right, justify */
  text-decoration: none;               /* underline, line-through, none */
  line-height: 1.6;                    /* înălțimea rândului */
  letter-spacing: 0.02em;              /* spațiul între litere */
  text-transform: none;                /* uppercase, lowercase, capitalize */
}
```

### Font family — stivă de fallback

```css
body {
  font-family: "Inter", "Segoe UI", Arial, sans-serif;
}
```

Browserul încearcă fonturile de la stânga la dreapta. Dacă `Inter` lipsește, încearcă `Segoe UI`, apoi `Arial`, apoi orice font `sans-serif` disponibil.

### Unități pentru font-size

| Unitate | Descriere | Exemplu |
|---------|-----------|---------|
| `px` | pixeli absoluți | `font-size: 16px;` |
| `rem` | relativ la rădăcina `<html>` | `font-size: 1rem;` (= 16px implicit) |
| `em` | relativ la părinte | `font-size: 1.25em;` |

!!! tip "Folosește `rem` pentru text"
    `rem` respectă preferințele utilizatorului (dacă își mărește fontul din setări browser) — mai **accesibil** decât `px`.

### Line-height — cât de aerisit e textul

```css
p {
  line-height: 1.6;   /* recomandat pentru paragrafe */
}
```

Un `line-height` prea mic face textul greu de citit. Între **1.5** și **1.7** este ideal.

---

## Google Fonts

Google oferă sute de fonturi gratuite. Cum le folosești:

### 1. Adaugi `<link>` în `<head>`

```html
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
</head>
```

### 2. Folosești fontul în CSS

```css
body {
  font-family: "Inter", sans-serif;
}
```

!!! note "Alege 1–2 familii maxim"
    Fiecare font descărcat încetinește pagina. Unul pentru titluri + unul pentru text curent este suficient.

---

## Exerciții

### Exercițiu 1 — Fundal galben pentru paragrafe

Pune toate paragrafele pe un fundal galben deschis și text mai întunecat.

??? success "Soluție"
    ```css
    p {
      background-color: #fffbea;
      color: #333;
      padding: 8px;
    }
    ```

### Exercițiu 2 — Clase `.important` și `.mic`

Creează două clase și aplică-le pe elemente din HTML.

??? success "Soluție"
    ```html
    <p class="important">Atenție!</p>
    <p class="mic">Notă de subsol</p>
    ```
    ```css
    .important {
      color: #c00;
      font-weight: 700;
    }

    .mic {
      font-size: 12px;
      color: #666;
    }
    ```

### Exercițiu 3 — Font Google pentru întreaga pagină

Setează fontul `Poppins` de la Google Fonts pentru tot conținutul.

??? success "Soluție"
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

## Mini-proiect: Stilizează pagina „Despre mine”

Ia pagina HTML din lecția anterioară și transform-o într-un design curat cu paletă de culori coerentă și font Google.

??? success "Soluție"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Despre mine</title>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <header>
        <h1>Ana Popescu</h1>
        <p class="subtitlu">Elevă · pasionată de web</p>
      </header>

      <section>
        <h2>Hobby-uri</h2>
        <ul>
          <li>Programare</li>
          <li>Muzică</li>
          <li>Desen digital</li>
        </ul>
      </section>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    /* Paletă de culori */
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

    .subtitlu {
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

## Rezumat

- **CSS** stilizează HTML-ul — culori, fonturi, spații
- Folosește **CSS extern** (`<link>`) pentru pagini reale
- Regula CSS = **selector + proprietăți + valori**
- Selectori de bază: **element**, **clasă** (`.`), **ID** (`#`)
- Specificitate: `element < clasă < id`
- Culori: **nume**, **#hex**, **rgb/rgba**, **hsl**
- `rem` > `px` pentru `font-size` (accesibilitate)
- **Google Fonts** adaugă fonturi moderne gratuit

---

**Pasul următor:** [→ Lecția 07: Box Model și poziționare](07-css-box-model.md)
