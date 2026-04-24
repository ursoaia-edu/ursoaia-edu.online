---
lesson: 5
tags: [web, html, navigare, semantica, header, nav, footer, github-pages]
summary: Construiește un site cu mai multe pagini — organizare foldere, link-uri relative, taguri semantice și structura header/nav/main/footer.
---

# Lecția 05 · Site multi-pagină

!!! tip "Ce vei învăța"
    - De ce împărțim conținutul pe **mai multe pagini**
    - Organizarea **folderelor** pentru un site
    - Link-uri relative: `./`, `../`, subfoldere
    - Taguri semantice: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`
    - Convenția `index.html`
    - Cum publici repede site-ul cu **GitHub Pages**

---

## De ce mai multe pagini?

Ai putea pune tot conținutul pe `index.html` — ar funcționa, dar:

- Pagina devine **imensă** și încet de încărcat.
- Meniul/navigarea n-are sens.
- **SEO mai slab** — Google preferă pagini focusate (o temă per pagină).
- Ești pierdut când cauți să editezi ceva.

Regula: **o pagină, o temă**. Site-ul cursului tău ar putea avea:

- `index.html` — pagina Acasă (ce e cursul, ce vei învăța)
- `despre.html` — Despre tine / profesor
- `proiecte.html` — Lista proiectelor
- `contact.html` — Formular de contact

---

## Organizarea folderelor

Un proiect curat arată așa:

```
site-meu/
├── index.html          ← pagina principală (Acasă)
├── despre.html
├── proiecte.html
├── contact.html
├── imagini/
│   ├── profil.jpg
│   ├── logo.png
│   └── proiecte/
│       └── robot.jpg
└── stiluri/
    └── style.css       ← (vine în Lecția 06)
```

!!! tip "Reguli simple de denumire"
    - **Fără spații** în nume. Folosește `despre-noi.html`, nu `despre noi.html`.
    - **Doar litere mici**. Unele servere fac diferența `Poza.jpg` ≠ `poza.jpg`.
    - **Fără diacritice**. Folosește `orar-scolar.html`, nu `orar-școlar.html`.

---

## Link-uri relative

### Același folder

```html
<!-- În index.html, link către despre.html -->
<a href="despre.html">Despre</a>
<!-- echivalent cu: -->
<a href="./despre.html">Despre</a>
```

`./` înseamnă „folder-ul curent” — opțional dar explicit.

### Subfolder

```
site-meu/
├── index.html
└── proiecte/
    └── robot.html
```

```html
<!-- În index.html: -->
<a href="proiecte/robot.html">Vezi proiectul robot</a>
```

### Folder părinte

```html
<!-- În proiecte/robot.html, înapoi la pagina principală: -->
<a href="../index.html">Acasă</a>
```

`..` înseamnă „un nivel mai sus”.

### Absolut vs. relativ — pe scurt

| Tip | Exemplu | Când |
|-----|---------|------|
| **Relativ** | `despre.html` | Link-uri în interiorul site-ului tău |
| **Absolut de domeniu** | `/proiecte.html` | Site-uri complexe cu rooting clar |
| **Absolut complet** | `https://alt-site.ro/...` | Link-uri **externe**, spre alte site-uri |

**Recomandare pentru început:** relativ (`despre.html`, `./proiecte/...`, `../index.html`). Funcționează și local, și în producție.

---

## Meniu de navigare

Pe fiecare pagină ai același meniu, care permite utilizatorului să navigheze oriunde.

```html
<nav>
  <a href="index.html">Acasă</a>
  <a href="despre.html">Despre</a>
  <a href="proiecte.html">Proiecte</a>
  <a href="contact.html">Contact</a>
</nav>
```

!!! warning "Repetiție — o problemă pe care o rezolvăm mai târziu"
    Dacă meniul e în 5 fișiere și vrei să adaugi un link nou, trebuie să-l adaugi în toate 5. E plictisitor și greșesc frecvent.

    **Soluții pe care le vei învăța:**

    - **JavaScript** (ES modules, `fetch` de componente) — Lecția 17+
    - **Framework-uri** (React, Vue) — cursuri avansate
    - **Generatoare de site-uri statice** (ca MkDocs, pe care rulează acest site!) — cursuri avansate

    Pentru început, copiază-lipește. E OK.

### Evidențierea paginii curente

Poți marca vizual pagina pe care ești acum (cu CSS, în Lecția 06):

```html
<!-- În despre.html: -->
<nav>
  <a href="index.html">Acasă</a>
  <a href="despre.html" class="activ" aria-current="page">Despre</a>
  <a href="proiecte.html">Proiecte</a>
</nav>
```

`aria-current="page"` spune cititoarelor de ecran „ești pe această pagină”.

---

## Taguri semantice HTML5

Până acum am folosit `<div>` pentru orice container. HTML5 a introdus **taguri cu semnificație** — browser-ele, Google și tehnologiile asistive le „înțeleg”.

```
┌─────────────────────────────────────────────┐
│ <header>  Logo | Titlu site                 │
│    <nav>  Acasă Despre Proiecte Contact     │
├─────────────────────────────────────────────┤
│                                   ┌───────┐ │
│ <main>                            │       │ │
│   <article>                       │<aside>│ │
│     Conținut principal            │ Bară  │ │
│   </article>                      │ later │ │
│                                   │       │ │
│                                   └───────┘ │
├─────────────────────────────────────────────┤
│ <footer>  © 2026 Ana · contact@...           │
└─────────────────────────────────────────────┘
```

| Tag | Rol |
|-----|-----|
| `<header>` | Antetul paginii (logo, titlu, meniu) |
| `<nav>` | Meniul de navigare |
| `<main>` | Conținutul principal al paginii (unul singur) |
| `<article>` | Un articol / un post independent |
| `<section>` | O secțiune tematică în articol |
| `<aside>` | Conținut secundar (sidebar, anunțuri) |
| `<footer>` | Subsolul paginii (copyright, link-uri) |

### Exemplu complet

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <title>Acasă — Site-ul meu</title>
</head>
<body>
  <header>
    <h1>Site-ul Anei</h1>
    <nav>
      <a href="index.html">Acasă</a>
      <a href="despre.html">Despre</a>
      <a href="proiecte.html">Proiecte</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Bine ai venit!</h2>
      <p>Sunt Ana și acest este site-ul meu personal.</p>
    </article>
  </main>

  <footer>
    <p>© 2026 Ana Popescu · Cluj-Napoca</p>
  </footer>
</body>
</html>
```

---

## Convenția `index.html`

Când un utilizator vizitează `https://site-meu.ro/`, serverul trimite implicit fișierul numit `index.html` din folder-ul rădăcină.

De aceea, pagina principală se numește **mereu** `index.html`, nu `acasa.html` sau `principal.html`.

La fel pentru subfoldere:

```
/proiecte/          → /proiecte/index.html
/proiecte/robot/    → /proiecte/robot/index.html
```

---

## Publicare rapidă: GitHub Pages

Ca să-ți arăți site-ul colegilor, **GitHub Pages** e gratuit și simplu:

1. **Cont GitHub** (gratis la [github.com](https://github.com)).
2. Creează un repository public numit `numele-tau.github.io` (ex: `ana-pop.github.io`).
3. Urcă fișierele tale (`index.html`, imagini, etc.).
4. În Settings → Pages, activează „Deploy from branch: main”.
5. După 1-2 minute, site-ul e live la `https://numele-tau.github.io`.

!!! tip "Detalii complete"
    Dacă nu cunoști încă Git / GitHub, vom face un tutorial separat. Pentru acum, reține doar că **publicarea e gratuită și durează 2-3 minute**.

Alternative: [Netlify](https://www.netlify.com/), [Vercel](https://vercel.com/), [Cloudflare Pages](https://pages.cloudflare.com/).

---

## Exerciții

### Exercițiu 1 — Două pagini cu link-uri reciproce
Creează `index.html` și `despre.html` în același folder. Fiecare să conțină un link către cealaltă.

??? success "Soluție"
    **`index.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Acasă</title>
    </head>
    <body>
      <h1>Pagina principală</h1>
      <p>Vezi și <a href="despre.html">pagina Despre</a>.</p>
    </body>
    </html>
    ```

    **`despre.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Despre</title>
    </head>
    <body>
      <h1>Despre mine</h1>
      <p>Sunt Ana. <a href="index.html">Înapoi la Acasă</a>.</p>
    </body>
    </html>
    ```

### Exercițiu 2 — Structură semantică
Adaugă pe pagina `despre.html` structura: `<header>` cu `<h1>` și `<nav>`, `<main>` cu conținut, `<footer>` cu copyright.

??? success "Soluție"
    ```html
    <body>
      <header>
        <h1>Site-ul Anei</h1>
        <nav>
          <a href="index.html">Acasă</a>
          <a href="despre.html" aria-current="page">Despre</a>
        </nav>
      </header>

      <main>
        <h2>Despre mine</h2>
        <p>Sunt Ana Popescu, elevă în clasa a VIII-a la Cluj-Napoca.</p>
      </main>

      <footer>
        <p>© 2026 Ana Popescu</p>
      </footer>
    </body>
    ```

### Exercițiu 3 — Navigare identică
Copiază exact același bloc `<header>...</header>` pe ambele pagini. Observă cum e identic — și cum ar fi o problemă dacă ai 20 de pagini.

??? success "Soluție"
    Exact — navigarea se repetă. Rezolvarea corectă se face cu un **generator de site-uri statice** sau cu **JavaScript**. Pentru acum, copy-paste e acceptabil.

---

## Mini-proiect: „Mini-site cu 3 pagini”

Construiește un site cu **3 pagini**: Acasă, Proiecte, Contact. Structură comună:

- `<header>` cu `<h1>` (numele tău) + `<nav>` (link-uri la cele 3 pagini)
- `<main>` cu conținut diferit pe fiecare pagină
- `<footer>` cu copyright și anul curent

**Pagini:**

- **Acasă** — mesaj de bun venit + 2–3 „carduri” (pot fi simplu paragrafe cu titluri) despre ce găsești pe site.
- **Proiecte** — listă de proiecte școlare (`<ul>` cu titluri + descrieri scurte).
- **Contact** — formularul din Lecția 04 (refolosit, fără stilizare).

Nu stilizăm încă — focusul e pe **structură** și **navigare**. Aspectul vine la Lecția 06.

??? success "Soluție"
    **`index.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Acasă — Site-ul lui Mihai</title>
    </head>
    <body>
      <header>
        <h1>Mihai Ionescu</h1>
        <nav>
          <a href="index.html" aria-current="page">Acasă</a>
          <a href="proiecte.html">Proiecte</a>
          <a href="contact.html">Contact</a>
        </nav>
      </header>

      <main>
        <h2>Bine ai venit!</h2>
        <p>Sunt Mihai, elev la Chișinău. Pe acest site găsești
           proiectele mele școlare și o formă de contact.</p>

        <section>
          <h3>Proiecte</h3>
          <p>Ce am construit la cercul de informatică.
             <a href="proiecte.html">Vezi lista</a>.</p>
        </section>

        <section>
          <h3>Contact</h3>
          <p>Ai o întrebare? <a href="contact.html">Scrie-mi</a>.</p>
        </section>
      </main>

      <footer>
        <p>© 2026 Mihai Ionescu · Chișinău</p>
      </footer>
    </body>
    </html>
    ```

    **`proiecte.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Proiecte — Site-ul lui Mihai</title>
    </head>
    <body>
      <header>
        <h1>Mihai Ionescu</h1>
        <nav>
          <a href="index.html">Acasă</a>
          <a href="proiecte.html" aria-current="page">Proiecte</a>
          <a href="contact.html">Contact</a>
        </nav>
      </header>

      <main>
        <h2>Proiectele mele</h2>
        <ul>
          <li>
            <strong>LED Blink cu Arduino</strong> —
            primul meu program pe microcontroler.
          </li>
          <li>
            <strong>Calculator în Python</strong> —
            aplicație de consolă pentru operații aritmetice.
          </li>
          <li>
            <strong>Site „Școala mea”</strong> —
            pagină HTML/CSS despre liceul meu.
          </li>
        </ul>
      </main>

      <footer>
        <p>© 2026 Mihai Ionescu · Chișinău</p>
      </footer>
    </body>
    </html>
    ```

    **`contact.html`:**
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Contact — Site-ul lui Mihai</title>
    </head>
    <body>
      <header>
        <h1>Mihai Ionescu</h1>
        <nav>
          <a href="index.html">Acasă</a>
          <a href="proiecte.html">Proiecte</a>
          <a href="contact.html" aria-current="page">Contact</a>
        </nav>
      </header>

      <main>
        <h2>Scrie-mi</h2>

        <form action="#" method="POST">
          <p>
            <label for="nume">Nume *</label><br>
            <input type="text" id="nume" name="nume"
                   required minlength="2">
          </p>
          <p>
            <label for="email">Email *</label><br>
            <input type="email" id="email" name="email" required>
          </p>
          <p>
            <label for="mesaj">Mesaj *</label><br>
            <textarea id="mesaj" name="mesaj"
                      rows="5" cols="40" required></textarea>
          </p>
          <p>
            <button type="submit">Trimite</button>
          </p>
        </form>
      </main>

      <footer>
        <p>© 2026 Mihai Ionescu · Chișinău</p>
      </footer>
    </body>
    </html>
    ```

---

## Rezumat

- Un site modern = **mai multe pagini**, fiecare cu o temă.
- Organizează **folderele**: HTML în rădăcină, imagini în `imagini/`, stiluri în `stiluri/`.
- Link-uri relative: `despre.html`, `./imagini/x.png`, `../index.html`.
- Folosește taguri **semantice**: `<header>`, `<nav>`, `<main>`, `<footer>`.
- Un singur `<main>` per pagină; `<nav>` pentru meniul principal.
- **`index.html`** este pagina implicită a unui folder.
- Publici gratuit pe **GitHub Pages**, Netlify, Vercel.

---

**Pasul următor:** [→ Lecția 06: CSS — introducere](06-css-introducere.md)
