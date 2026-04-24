---
lesson: 7
tags: [web, css, box-model, margin, padding, border, position, display]
summary: Fiecare element HTML este o cutie. Învață cum controlezi spațiile, dimensiunile și poziția.
---

# Lecția 07 · Box Model și poziționare

!!! tip "Ce vei învăța"
    - Cele 4 straturi ale Box Model-ului: content, padding, border, margin
    - Cum controlezi dimensiunea cu `width`, `height` și `box-sizing`
    - Valorile pentru `display`: block, inline, inline-block, none
    - Poziționarea: `static`, `relative`, `absolute`, `fixed`, `sticky`
    - Fundaluri (background) și imagini

---

## Box Model — cele 4 straturi

Fiecare element HTML este **o cutie dreptunghiulară**. În jurul conținutului se află trei straturi concentrice:

```
┌─────────────── margin ───────────────┐
│  ┌────────── border ──────────────┐  │
│  │  ┌──────── padding ─────────┐  │  │
│  │  │         content          │  │  │
│  │  └──────────────────────────┘  │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
```

- **content** — textul sau imaginea propriu-zisă
- **padding** — spațiul interior dintre conținut și chenar
- **border** — chenarul (linia)
- **margin** — spațiul exterior, între cutie și vecini

!!! note "Cum vezi Box Model-ul"
    În Chrome / Firefox, apasă **F12** → tab **Elements** → panoul **Computed** din dreapta arată cutia colorată (albastru, verde, portocaliu, galben) pentru oricare element selectat.

---

## Margin — spațiul exterior

```css
/* Toate cele 4 margini egale */
.cutie {
  margin: 10px;
}

/* Top/bottom = 10px, left/right = 20px */
.cutie {
  margin: 10px 20px;
}

/* Top = 10, right = 20, bottom = 15, left = 5 (în sens orar) */
.cutie {
  margin: 10px 20px 15px 5px;
}

/* Individual */
.cutie {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 15px;
  margin-left: 5px;
}
```

### `margin: auto` — centrare orizontală

```css
.card {
  width: 400px;
  margin: 0 auto;   /* 0 sus/jos, auto stânga/dreapta */
}
```

Browserul împarte egal spațiul rămas → cutia se centrează.

!!! warning "Margin collapse"
    Când două elemente vecine au margin vertical (ex. două paragrafe cu `margin-bottom: 20px` și `margin-top: 20px`), browserul **NU** le adună (nu obții 40px), ci păstrează **cea mai mare** (20px). Se numește *margin collapse* și este normal.

---

## Padding — spațiul interior

Aceeași sintaxă ca la `margin`:

```css
.buton {
  padding: 12px 24px;    /* vertical 12px, orizontal 24px */
  background-color: royalblue;
  color: white;
}
```

Padding-ul crește **cutia** vizibilă (adăugând spațiu între conținut și margine).

---

## Border — chenarul

```css
.card {
  border: 2px solid #4f46e5;   /* lățime, stil, culoare */
}

/* Doar o latură */
.card {
  border-bottom: 1px solid #e5e7eb;
}
```

### Stiluri disponibile

```css
border-style: solid;    /* linie continuă */
border-style: dashed;   /* linie întreruptă */
border-style: dotted;   /* puncte */
border-style: double;   /* două linii */
border-style: none;     /* fără chenar */
```

### Colțuri rotunjite cu `border-radius`

```css
.card {
  border-radius: 8px;       /* colțuri ușor rotunjite */
}

.avatar {
  border-radius: 50%;       /* cerc perfect (dacă width = height) */
}

.capsula {
  border-radius: 999px;     /* formă de pastilă */
}
```

---

## Width și height

```css
.card {
  width: 300px;
  height: 200px;
}
```

### Width/height responsive

```css
.card {
  max-width: 600px;     /* niciodată mai lat de 600px */
  min-width: 200px;     /* niciodată mai îngust de 200px */
  width: 100%;          /* ocupă tot spațiul părintelui */
}
```

!!! tip "Preferă `max-width` în loc de `width` fix"
    `max-width: 600px` lasă cutia să se micșoreze natural pe ecrane mici. `width: 600px` o forțează să rămână la 600px și poate ieși în afara ecranului pe telefon.

### Valori implicite

- Elementele **block** (`<div>`, `<p>`, `<h1>`): `width: auto` → ocupă tot rândul
- Elementele **inline** (`<span>`, `<a>`): `width` și `height` sunt **ignorate**

---

## `box-sizing: border-box` — esențial

Acesta este cel mai important concept din Box Model.

### Comportament implicit: `content-box`

```css
.cutie {
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
```

**Lățimea reală vizibilă = 200 + 20 + 20 + 2 + 2 = 244 px.**

Adică `width` se referă doar la conținut — padding și border **se adaugă peste**. Complet neintuitiv.

### `box-sizing: border-box` — predictibil

```css
.cutie {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 2px solid black;
}
```

**Lățimea reală vizibilă = 200 px.** Padding și border sunt **incluse** în width.

### Regula de aur (folosește mereu)

```css
/* La începutul fiecărui fișier CSS */
* {
  box-sizing: border-box;
}
```

!!! tip "De ce `* { box-sizing: border-box; }`"
    Aplică regula pentru **toate** elementele. Te scutește de calcule mentale și face layout-urile responsive mult mai ușor de controlat. Standardul modern în toate framework-urile (Bootstrap, Tailwind etc.).

---

## Display — cum se comportă elementul

```css
div    { display: block; }         /* ocupă tot rândul, acceptă width/height */
span   { display: inline; }        /* cât textul, NU acceptă width/height */
a      { display: inline-block; }  /* cât textul, DAR acceptă width/height */
.ascuns { display: none; }         /* dispare complet din pagină */
```

| Valoare | Pe rând nou? | Acceptă width/height? |
|---------|---------------|------------------------|
| `block` | da | da |
| `inline` | nu | nu |
| `inline-block` | nu | da |
| `none` | — dispare — | — |

!!! warning "`display: none` vs `visibility: hidden`"
    - `display: none` — elementul **dispare**, nu ocupă loc, nu se aude de screen-reader.
    - `visibility: hidden` — elementul este invizibil dar **ocupă locul**.

---

## Position — poziționarea elementelor

### `static` (implicit)

Elementul urmează fluxul normal al documentului. `top`, `left` nu au efect.

### `relative` — mutat față de poziția normală

```css
.card {
  position: relative;
  top: 10px;
  left: 20px;   /* se mută 20px la dreapta, 10px în jos */
}
```

Important: `relative` păstrează locul original (alte elemente nu se mișcă).

### `absolute` — scos din flux

```css
.parinte {
  position: relative;   /* necesar pentru ancorare */
}

.copil {
  position: absolute;
  top: 0;
  right: 0;             /* în colțul dreapta-sus al părintelui */
}
```

`absolute` se poziționează față de **primul părinte cu position diferit de static**. Dacă nu găsește, se raportează la `<body>`.

### `fixed` — fix față de viewport

```css
.floating-button {
  position: fixed;
  bottom: 20px;
  right: 20px;          /* rămâne acolo chiar și când faci scroll */
}
```

Util pentru butoane „Back to top”, notificări, chat widget.

### `sticky` — hibrid static/fixed

```css
header {
  position: sticky;
  top: 0;               /* se lipește sus când faci scroll la el */
  background: white;
  z-index: 10;
}
```

Se comportă ca `static` până când ajungi la prag, apoi devine `fixed`. Excelent pentru bare de navigație.

### Comparație rapidă

| Valoare | În flux? | Față de ce se mișcă? |
|---------|----------|------------------------|
| `static` | da | — (nu se poate muta) |
| `relative` | da | poziția sa originală |
| `absolute` | nu | cel mai apropiat părinte poziționat |
| `fixed` | nu | viewport (fereastra) |
| `sticky` | da până la prag | viewport după prag |

---

## z-index — ordinea pe axa Z

Când elementele se suprapun, `z-index` decide care e **deasupra**.

```css
.modal {
  position: fixed;
  z-index: 1000;   /* deasupra oricărui alt element */
}

.fundal-modal {
  position: fixed;
  z-index: 999;    /* sub modal, dar peste restul paginii */
}
```

!!! note "`z-index` funcționează doar pe elemente poziționate"
    Trebuie să ai și `position: relative/absolute/fixed/sticky` ca `z-index` să aibă efect.

---

## Background — fundalul

```css
.hero {
  background-color: #4f46e5;
  background-image: url('fundal.jpg');
  background-size: cover;        /* acoperă tot containerul */
  background-position: center;   /* centrat */
  background-repeat: no-repeat;  /* nu se repetă în mozaic */
}

/* Shorthand — toate într-o linie */
.hero {
  background: #4f46e5 url('fundal.jpg') center / cover no-repeat;
}
```

| Valoare pentru `background-size` | Efect |
|------------------------------------|-------|
| `cover` | imaginea acoperă tot containerul (poate fi tăiată) |
| `contain` | imaginea se încadrează complet (pot rămâne margini) |
| `100% 100%` | întinsă (deformată — de evitat) |

---

## Exerciții

### Exercițiu 1 — Card cu padding, border și colțuri rotunjite

Creează un `<div class="card">` cu text înăuntru, stilizat ca un card modern.

??? success "Soluție"
    ```html
    <div class="card">
      <h2>Titlu card</h2>
      <p>Un scurt text descriptiv.</p>
    </div>
    ```
    ```css
    .card {
      box-sizing: border-box;
      padding: 24px;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      background-color: white;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
      max-width: 400px;
    }
    ```

### Exercițiu 2 — Centrează un div cu lățime fixă

Folosește `margin: auto`.

??? success "Soluție"
    ```css
    .container {
      max-width: 800px;
      margin: 0 auto;      /* centrare orizontală */
      padding: 1rem;
    }
    ```

### Exercițiu 3 — Buton „plutitor” în colț

Un buton care rămâne fixat în colțul dreapta-jos al paginii.

??? success "Soluție"
    ```html
    <button class="fab" aria-label="Adaugă">+</button>
    ```
    ```css
    .fab {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 56px;
      height: 56px;
      border: none;
      border-radius: 50%;
      background-color: #4f46e5;
      color: white;
      font-size: 28px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
      z-index: 100;
    }

    .fab:hover {
      background-color: #4338ca;
    }
    ```

---

## Mini-proiect: Carte de vizită digitală

Creează un card cu avatar rotund, nume, funcție și link-uri sociale.

??? success "Soluție"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Carte de vizită</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <article class="carte-vizita">
        <img class="avatar" src="avatar.jpg" alt="Fotografie Ana Popescu">
        <h1 class="nume">Ana Popescu</h1>
        <p class="functie">Web Developer</p>
        <ul class="social">
          <li><a href="#">GitHub</a></li>
          <li><a href="#">LinkedIn</a></li>
          <li><a href="#">Email</a></li>
        </ul>
      </article>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    /* Reset de bază */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: linear-gradient(135deg, #667eea, #764ba2);
      min-height: 100vh;
      font-family: "Inter", sans-serif;
      /* Centrare cu flexbox — detaliat în lecția 08 */
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }

    .carte-vizita {
      width: 320px;
      padding: 2rem;
      background-color: white;
      border-radius: 16px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .avatar {
      width: 120px;
      height: 120px;
      border-radius: 50%;       /* cerc perfect */
      border: 4px solid #4f46e5;
      object-fit: cover;        /* imaginea nu se deformează */
      margin-bottom: 1rem;
    }

    .nume {
      font-size: 1.5rem;
      color: #1f2937;
      margin-bottom: 0.25rem;
    }

    .functie {
      color: #6b7280;
      margin-bottom: 1.5rem;
    }

    .social {
      list-style: none;
      display: flex;
      justify-content: center;
      gap: 1rem;
    }

    .social a {
      color: #4f46e5;
      text-decoration: none;
      font-weight: 600;
    }

    .social a:hover {
      text-decoration: underline;
    }
    ```

---

## Rezumat

- **Box Model** = content + padding + border + margin
- `margin` = spațiu **exterior**, `padding` = spațiu **interior**
- `border-radius: 50%` = cerc perfect
- `* { box-sizing: border-box; }` — **regulă obligatorie** în orice proiect modern
- `display`: block / inline / inline-block / none
- `position`: static (implicit), relative, absolute, fixed, sticky
- `background` controlează culoarea și imaginea de fundal
- `z-index` funcționează doar pe elemente poziționate

---

**Pasul următor:** [→ Lecția 08: Flexbox și Grid](08-css-flexbox-grid.md)
