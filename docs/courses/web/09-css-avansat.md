---
lesson: 9
tags: [web, css, pseudo-clase, tranzitii, animatii, transform, hover]
summary: Efecte interactive și animații folosind doar CSS — fără JavaScript.
---

# Lecția 09 · CSS avansat: pseudo-clase, tranziții și animații

!!! tip "Ce vei învăța"
    - **Pseudo-clase** (`:hover`, `:focus`, `:nth-child`) și pseudo-elemente (`::before`, `::after`)
    - **Tranziții** netede între două stări
    - **Transform**: rotire, scalare, translație
    - **@keyframes** — animații complete
    - Efecte moderne populare pe care le folosești în orice site

---

## Pseudo-clase

O pseudo-clasă se atașează la un selector cu `:` și selectează elementul într-o anumită **stare**.

### Pseudo-clase de interacțiune

```css
/* Mouse-ul este deasupra elementului */
.buton:hover {
  background-color: #4338ca;
}

/* Elementul este focusat (tab în formular) */
input:focus {
  border-color: #4f46e5;
  outline: 2px solid #c7d2fe;
}

/* În momentul click-ului (apăsat) */
.buton:active {
  transform: translateY(1px);
}

/* Link deja vizitat */
a:visited {
  color: #7c3aed;
}
```

!!! warning "Nu elimina `:focus` vizual"
    `outline: none` fără a pune altceva în loc **sparge accesibilitatea**. Utilizatorii cu tastatura (inclusiv cei cu dizabilități) nu mai știu unde se află. Lasă întotdeauna un chenar vizibil la `:focus`.

### Pseudo-clase structurale

```css
/* Primul copil al părintelui */
li:first-child {
  font-weight: 700;
}

/* Ultimul copil */
li:last-child {
  border-bottom: none;
}

/* Rândurile pare dintr-un tabel */
tr:nth-child(even) {
  background-color: #f9fafb;
}

/* Rândurile impare */
tr:nth-child(odd) {
  background-color: white;
}

/* Fiecare al treilea element */
.card:nth-child(3n) {
  background-color: #ede9fe;
}

/* Toate, CU EXCEPȚIA .activ */
.tab:not(.activ) {
  opacity: 0.6;
}
```

### Pseudo-clase pentru formulare

```css
input:disabled {
  background-color: #f3f4f6;
  cursor: not-allowed;
}

input:checked + label {
  font-weight: 700;
}

input:required {
  border-left: 3px solid red;
}

input:valid {
  border-color: green;
}

input:invalid {
  border-color: red;
}
```

---

## Pseudo-elemente

Două puncte (`::`) în loc de unul. Creează conținut **virtual** care nu există în HTML.

```css
.citat::before {
  content: "„";
  color: #9ca3af;
  font-size: 2rem;
}

.citat::after {
  content: "”";
  color: #9ca3af;
  font-size: 2rem;
}
```

Uzul obișnuit:

- Ghilimele decorative
- Icon-uri înainte de link
- Separator între link-uri (`::after { content: " · "; }`)
- Overlay-uri peste imagini

```css
/* Breadcrumb cu separator automat */
.breadcrumb li + li::before {
  content: " › ";
  color: #9ca3af;
  padding: 0 0.5rem;
}
```

---

## Tranziții

O tranziție animează schimbarea unei proprietăți de la o valoare la alta.

### Sintaxă

```css
.buton {
  background-color: #4f46e5;
  transition: background-color 0.3s ease;
  /*          ^propr         ^durată ^curbă */
}

.buton:hover {
  background-color: #4338ca;   /* trece lin de la o culoare la alta */
}
```

### Mai multe proprietăți

```css
.card {
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
```

### `all` — toate proprietățile

```css
.buton {
  transition: all 0.2s ease;   /* comod, dar mai puțin performant */
}
```

### Timing functions (curbele de animație)

| Valoare | Caracter |
|---------|----------|
| `linear` | viteză constantă (robotic) |
| `ease` (implicit) | pornește încet, accelerează, încetinește |
| `ease-in` | pornește încet, termină repede |
| `ease-out` | pornește repede, termină lin |
| `ease-in-out` | încet la capete, rapid la mijloc |
| `cubic-bezier(...)` | curbă personalizată |

!!! tip "`ease-out` pentru UI"
    Efectele care apar la utilizator (hover, fade-in) se simt cel mai natural cu `ease-out` — se mișcă repede apoi încetinesc.

---

## Transform — rotire, scalare, translație

`transform` aplică **transformări geometrice** fără să afecteze layout-ul. Alte elemente **nu se mișcă** atunci când un element este transformat.

```css
.element {
  /* Translație — mutare pe X / Y */
  transform: translate(10px, -5px);
  transform: translateX(20px);
  transform: translateY(-10px);

  /* Scalare */
  transform: scale(1.1);         /* 110% */
  transform: scaleX(2);          /* de 2 ori mai larg */

  /* Rotire */
  transform: rotate(45deg);
  transform: rotate(-90deg);

  /* Înclinare */
  transform: skew(10deg, 0);

  /* Combinate — se aplică de la dreapta la stânga */
  transform: translateY(-4px) scale(1.05) rotate(2deg);
}
```

!!! note "De ce e `transform` așa de puternic"
    Browserul rulează `transform` și `opacity` pe **GPU**, folosind compositing. Animațiile sunt netede chiar și pe telefoane vechi — spre deosebire de `margin` sau `top` care declanșează layout reflow (lent).

---

## Animații cu `@keyframes`

Pentru animații complexe (mai multe pași) folosești `@keyframes` + `animation`.

### Sintaxă

```css
@keyframes pulse {
  0%   { transform: scale(1); }
  50%  { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.pulsator {
  animation: pulse 2s ease-in-out infinite;
  /*         ^nume ^durată ^curbă ^repetare */
}
```

### Sintaxă detaliată

```css
.element {
  animation-name: pulse;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-delay: 0s;
  animation-iteration-count: infinite;   /* sau un număr: 3, 1, ... */
  animation-direction: normal;           /* normal | reverse | alternate */
  animation-fill-mode: forwards;         /* păstrează starea finală */
}
```

### Exemple

```css
/* Fade-in la încărcarea paginii */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero {
  animation: fadeIn 0.6s ease-out;
}

/* Spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.loader {
  animation: spin 1s linear infinite;
}

/* Shake (pentru erori de formular) */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25%      { transform: translateX(-8px); }
  75%      { transform: translateX(8px); }
}

.input-eroare {
  animation: shake 0.3s ease;
}
```

!!! warning "Respectă `prefers-reduced-motion`"
    Unii utilizatori dezactivează animațiile din motive medicale (rău de mișcare, epilepsie). Oferă o variantă simplificată:
    ```css
    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
      }
    }
    ```

---

## Efecte populare

### Buton cu „lift” la hover

```css
.buton {
  background: #4f46e5;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.buton:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(79, 70, 229, 0.3);
}
```

### Card care crește la hover

```css
.card {
  transition: transform 0.3s ease;
}

.card:hover {
  transform: scale(1.03);
}
```

### Underline animat

```css
.link {
  position: relative;
  text-decoration: none;
  color: #1f2937;
}

.link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: #4f46e5;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.link:hover::after {
  transform: scaleX(1);
}
```

---

## Exerciții

### Exercițiu 1 — Buton cu hover colorat

Butonul își schimbă culoarea de fundal lin (0.3s) la hover.

??? success "Soluție"
    ```html
    <button class="cta">Abonează-te</button>
    ```
    ```css
    .cta {
      background-color: #10b981;
      color: white;
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .cta:hover {
      background-color: #059669;
    }
    ```

### Exercițiu 2 — Primul element cu stil diferit

Primul `<li>` dintr-o listă să aibă culoare diferită.

??? success "Soluție"
    ```css
    li:first-child {
      color: #4f46e5;
      font-weight: 700;
    }
    ```

### Exercițiu 3 — Rânduri pare într-un tabel

Rândurile pare au fundal gri deschis (efect zebră).

??? success "Soluție"
    ```css
    tr:nth-child(even) {
      background-color: #f9fafb;
    }

    tr:hover {
      background-color: #e0e7ff;
    }
    ```

### Exercițiu 4 — Inimioară care bate

O inimioară care pulsează în buclă, ca bătăile inimii.

??? success "Soluție"
    ```html
    <div class="inima">&#9829;</div>
    ```
    ```css
    .inima {
      font-size: 4rem;
      color: #e11d48;
      display: inline-block;
      animation: heartbeat 1.2s ease-in-out infinite;
    }

    @keyframes heartbeat {
      0%, 100% { transform: scale(1); }
      25%      { transform: scale(1.2); }
      50%      { transform: scale(1); }
      75%      { transform: scale(1.15); }
    }

    /* Respectă preferințele utilizatorului */
    @media (prefers-reduced-motion: reduce) {
      .inima { animation: none; }
    }
    ```

---

## Mini-proiect: Buton „premium” modern

Un buton cu hover: lift, shadow, gradient shift și tranziție lină.

??? success "Soluție"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Buton premium</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <main>
        <button class="buton-premium">
          Începe acum
        </button>
      </main>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: "Inter", sans-serif;
      background: #f9fafb;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }

    .buton-premium {
      position: relative;
      padding: 1rem 2.5rem;
      font-size: 1.1rem;
      font-weight: 600;
      color: white;
      border: none;
      border-radius: 12px;
      cursor: pointer;

      /* Gradient de fundal */
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      background-size: 200% 200%;
      background-position: 0% 50%;

      /* Shadow-ul inițial */
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);

      /* Tranziția atinge toate proprietățile schimbate la hover */
      transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background-position 0.6s ease;
    }

    .buton-premium:hover {
      /* Lift efect */
      transform: translateY(-3px);
      /* Shadow mai mare și mai difuză */
      box-shadow: 0 10px 28px rgba(99, 102, 241, 0.45);
      /* Gradient-ul se deplasează subtil */
      background-position: 100% 50%;
    }

    .buton-premium:active {
      /* Se apasă ușor la click */
      transform: translateY(-1px);
    }

    /* Focus vizibil pentru accesibilitate */
    .buton-premium:focus-visible {
      outline: 3px solid #c7d2fe;
      outline-offset: 2px;
    }

    /* Respectă preferințele utilizatorului */
    @media (prefers-reduced-motion: reduce) {
      .buton-premium { transition: none; }
      .buton-premium:hover { transform: none; }
    }
    ```

    **Cum funcționează:**

    - `background-size: 200%` face gradient-ul mai mare decât butonul
    - `background-position` mută „fereastra” care arată din gradient
    - La hover, poziția se schimbă de la `0%` la `100%` → efect de curgere a culorii
    - `translateY(-3px)` + shadow mai mare → impresie de plutire
    - `:focus-visible` asigură accesibilitate pentru tastatură

---

## Rezumat

- **Pseudo-clase** (`:hover`, `:focus`, `:nth-child`) selectează elementul într-o stare
- **Pseudo-elemente** (`::before`, `::after`) creează conținut decorativ fără HTML
- `transition` animează schimbările între stări — minim pentru UI modern
- `transform` (translate, scale, rotate) e **rapid** — rulează pe GPU
- `@keyframes` + `animation` pentru animații cu mai mulți pași
- Respectă `prefers-reduced-motion` pentru accesibilitate
- Păstrează un indicator vizual la `:focus`

---

**Pasul următor:** [→ Lecția 10: Design responsive](10-css-responsive.md)
