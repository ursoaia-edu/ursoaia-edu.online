---
lesson: 2
tags: [web, html, linkuri, imagini, titluri, accesibilitate]
summary: Tagurile HTML esențiale — titluri, paragrafe, link-uri, imagini, formatare text, div și span.
---

# Lecția 02 · HTML: tagurile de bază

!!! tip "Ce vei învăța"
    - Ierarhia titlurilor `<h1>` – `<h6>` și de ce contează
    - Paragrafe corecte și ce să **nu** faci cu `<br>`
    - Link-uri interne, externe, către secțiuni și către e-mail
    - Imagini, atributul `alt` și formatele potrivite
    - Formatare text: `<strong>`, `<em>`, `<mark>`, `<code>`
    - Diferența dintre `<div>` și `<span>`

---

## Titluri: de la `<h1>` la `<h6>`

HTML are **6 nivele de titluri**. Nu sunt doar pentru mărime — sunt **semantice**. Motoarele de căutare și cititoarele de ecran folosesc ierarhia lor pentru a înțelege structura paginii.

```html
<h1>Titlul principal al paginii</h1>
<h2>Secțiune mare</h2>
<h3>Sub-secțiune</h3>
<h4>Detaliu</h4>
```

!!! warning "Un singur `<h1>` per pagină"
    `<h1>` este titlul **principal** — unul per pagină (ca titlul unei cărți). `<h2>` pentru capitole, `<h3>` pentru sub-capitole și așa mai departe.

**Exemplu de structură corectă pentru un articol:**

```html
<h1>Ghid de ciclism pentru începători</h1>
  <h2>Alegerea bicicletei</h2>
    <h3>Bicicletă de oraș</h3>
    <h3>Bicicletă de munte</h3>
  <h2>Echipamentul esențial</h2>
    <h3>Cască</h3>
    <h3>Lumini și reflectorizante</h3>
```

Nu sări peste nivele (`<h1>` → `<h4>` direct) doar pentru „arată frumos” — pentru asta avem CSS (lecțiile 06+).

---

## Paragrafe

`<p>` înseamnă „paragraf”. Browser-ul pune automat spațiu înainte și după:

```html
<p>Acesta este primul paragraf. Poate conține mai multe fraze, nu
   trebuie să rupi linia manual — browser-ul se ocupă de asta.</p>

<p>Al doilea paragraf. Spațiul dintre ele e natural.</p>
```

!!! warning "Nu folosi `<br>` pentru spațiu între paragrafe"
    ```html
    <!-- Greșit: -->
    <p>Primul text</p>
    <br><br>
    <p>Al doilea text</p>

    <!-- Corect: -->
    <p>Primul text</p>
    <p>Al doilea text</p>
    ```
    `<br>` e pentru **o singură rupere de linie** într-un context unde chiar vrei asta (adresă poștală, versuri). Pentru spațiu între paragrafe ai `<p>`, iar pentru spațiu personalizat vei folosi CSS mai târziu.

---

## Link-uri (`<a>`)

Link-ul (anchor) este **inima web-ului** — fără el nu s-ar chema „Web”.

### Link simplu

```html
<a href="https://ursoaia-edu.online">Ursoaia Edu</a>
```

- `href` (hypertext reference) = adresa destinație.
- Textul dintre `<a>` și `</a>` este ce vede utilizatorul.

### URL absolut vs. relativ

```html
<!-- Absolut: funcționează de oriunde -->
<a href="https://ro.wikipedia.org">Wikipedia</a>

<!-- Relativ: la alt fișier din același folder -->
<a href="despre.html">Despre noi</a>

<!-- Relativ: la fișier din folder-ul părinte -->
<a href="../index.html">Acasă</a>

<!-- Relativ: la fișier dintr-un subfolder -->
<a href="./proiecte/lista.html">Proiecte</a>
```

### Tab nou: `target="_blank"` + securitate

```html
<a href="https://example.com" target="_blank" rel="noopener">
  Deschide într-un tab nou
</a>
```

!!! warning "Adaugă mereu `rel=\"noopener\"`"
    Fără `rel="noopener"`, pagina deschisă poate accesa pagina ta prin `window.opener` — o mică breșă de securitate. **Regulă:** `target="_blank"` ⇒ `rel="noopener"`.

### Link către o secțiune din aceeași pagină

Folosește un `id` și un `#`:

```html
<nav>
  <a href="#istoric">Sari la Istoric</a>
</nav>

<!-- Mai jos în pagină: -->
<h2 id="istoric">Istoric</h2>
<p>În 1989...</p>
```

### Link email

```html
<a href="mailto:ana@exemplu.ro">Scrie-mi</a>
```

Deschide clientul de e-mail implicit cu adresa pre-completată.

---

## Imagini (`<img>`)

```html
<img src="assets/peisaj.jpg" alt="Vedere din Munții Apuseni" width="400">
```

- `src` (source) = calea către fișierul imagine.
- `alt` = descrierea imaginii (text alternativ).
- `width` / `height` (opțional) = dimensiuni în pixeli.

!!! tip "`alt` NU este opțional"
    `alt` are **două roluri critice**:

    1. **Accesibilitate:** cititoarele de ecran îl citesc persoanelor nevăzătoare.
    2. **SEO:** Google îl folosește pentru a înțelege ce e în imagine.

    Plus: dacă imaginea nu se încarcă, se afișează textul `alt` în locul ei.

    Descrie **ce se vede**, nu „imagine” sau „poză”. Rău: `alt="img1"`. Bine: `alt="Câine Golden Retriever alergând pe o plajă"`.

### Format potrivit

| Format | Când îl folosești |
|--------|-------------------|
| **JPG** / **JPEG** | Fotografii (multe culori, fără transparență) |
| **PNG** | Grafică, capturi de ecran, **transparență** |
| **SVG** | Icon-uri, logo-uri (scalabile, mici) |
| **WebP** | Modern, mai mic decât JPG/PNG — suportat în toate browser-ele moderne |

### Cale relativă — exemplu

Structura folder-ului:

```
site-meu/
├── index.html
└── imagini/
    └── peisaj.jpg
```

În `index.html`:

```html
<img src="imagini/peisaj.jpg" alt="Peisaj montan">
```

---

## Formatare de text

### `<strong>` — important (implicit bold)

```html
<p>Acest câmp este <strong>obligatoriu</strong>.</p>
```

### `<em>` — accentuat (implicit italic)

```html
<p>El chiar <em>voia</em> să meargă.</p>
```

!!! note "Semantică, nu doar stil"
    `<strong>` e diferit de `<b>` și `<em>` e diferit de `<i>`. Cele scurte (`<b>`, `<i>`) înseamnă doar „arată bold/italic” — fără semnificație. Cele lungi (`<strong>`, `<em>`) spun „este important” / „este accentuat”. Cititoarele de ecran rostesc diferit.

### `<mark>` — evidențiere

```html
<p>Întâlnirea este <mark>marți, ora 15:00</mark>.</p>
```

Text cu fundal galben, ca un marker highlighter.

### `<code>` — cod inline

```html
<p>Scrie <code>print("salut")</code> în terminal.</p>
```

### `<br>` — rupere de linie (folosește-l RAR)

Util în versuri, adrese poștale:

```html
<p>Str. Republicii nr. 10<br>
400001, Cluj-Napoca<br>
România</p>
```

### `<hr>` — separator orizontal

```html
<h2>Capitolul 1</h2>
<p>...</p>
<hr>
<h2>Capitolul 2</h2>
```

---

## `<div>` vs `<span>` — containere

Uneori vrei să **grupezi** elemente pentru stilizare sau interactivitate. Ai două containere neutre:

### `<div>` — bloc

Ocupă **tot rândul** (merge cu alineat nou).

```html
<div>
  <h2>Titlu card</h2>
  <p>Conținutul card-ului.</p>
</div>
```

### `<span>` — inline

Ocupă **doar cât textul lui** (nu rupe linia).

```html
<p>Prețul este <span>199 lei</span> doar azi.</p>
```

!!! tip "Mai sunt alte opțiuni"
    `<div>` e un container **generic**. HTML5 a adus containere **semantice** mai bune: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` — le vei folosi în Lecția 05. Preferă un container semantic când există.

---

## Erori frecvente

- **Lipsește `alt`** la imagini → problemă de accesibilitate și SEO.
- **Mai multe `<h1>`** per pagină → structură confuză.
- **`<br>` abuzat** în loc de paragrafe separate.
- **Link-uri cu text generic**: „click aici”, „mai multe” — folosește text descriptiv. Rău: `<a href="url">aici</a>`. Bine: `<a href="url">raportul anual</a>`.

---

## Exerciții

### Exercițiu 1 — Pagină completă
Creează o pagină cu: un `<h1>`, două `<h2>`, 3 paragrafe, 2 link-uri (unul intern spre o secțiune, unul extern cu `target="_blank"`) și o imagine cu `alt` descriptiv.

??? success "Soluție"
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Elena Marin – Despre mine</title>
    </head>
    <body>
      <h1>Elena Marin</h1>

      <nav>
        <a href="#hobby">Hobby-uri</a> ·
        <a href="https://ursoaia-edu.online" target="_blank" rel="noopener">
          Ursoaia Edu
        </a>
      </nav>

      <p>Sunt elevă la Liceul „Mihai Eminescu” din București.</p>

      <img src="imagini/profil.jpg" alt="Elena zâmbind într-un parc" width="200">

      <h2 id="hobby">Hobby-uri</h2>
      <p>Îmi place să pictez și să cânt la chitară.</p>
      <p>În weekend merg cu bicicleta prin parcul Herăstrău.</p>
    </body>
    </html>
    ```

### Exercițiu 2 — Formatare în paragraf
Scrie un paragraf unde o parte e `<strong>`, alta `<em>`, iar un cuvânt-cheie e în `<mark>`.

??? success "Soluție"
    ```html
    <p>Radu spune că <strong>siguranța e pe primul loc</strong>,
       dar Ana este <em>absolut convinsă</em> că
       trebuie să ne grăbim. Termen limită:
       <mark>vineri, ora 18:00</mark>.</p>
    ```

### Exercițiu 3 — Cuprins cu ancore
Fă un cuprins la începutul paginii cu 3 link-uri către secțiuni de mai jos (`#intro`, `#capitol-1`, `#capitol-2`).

??? success "Soluție"
    ```html
    <h1>Articolul meu</h1>
    <nav>
      <p>Cuprins:</p>
      <ul>
        <li><a href="#intro">Introducere</a></li>
        <li><a href="#capitol-1">Capitolul 1</a></li>
        <li><a href="#capitol-2">Capitolul 2</a></li>
      </ul>
    </nav>

    <h2 id="intro">Introducere</h2>
    <p>...</p>
    <h2 id="capitol-1">Capitolul 1</h2>
    <p>...</p>
    <h2 id="capitol-2">Capitolul 2</h2>
    <p>...</p>
    ```

---

## Mini-proiect: „Echipa mea preferată”

Fă o pagină despre formația, echipa sportivă sau trupa ta preferată, cu:

- `<h1>` cu numele
- Secțiune „Despre” (`<h2>` + paragrafe)
- Secțiune „Membri” / „Jucători” (`<h2>` + paragrafe)
- Secțiune „Realizări” / „Discografie” (`<h2>` + paragrafe)
- O imagine cu `alt` descriptiv
- Un link către site-ul oficial (extern, tab nou)

??? success "Soluție"
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>CFR Cluj – echipa mea</title>
    </head>
    <body>
      <h1>CFR 1907 Cluj</h1>
      <p>Site oficial:
        <a href="https://www.cfr1907.ro" target="_blank" rel="noopener">
          cfr1907.ro
        </a>
      </p>

      <img src="imagini/stadion.jpg" alt="Vedere de pe tribună a stadionului Dr. Constantin Rădulescu" width="500">

      <h2>Despre</h2>
      <p>Club de fotbal din Cluj-Napoca, fondat în 1907.
         Joacă pe stadionul „Dr. Constantin Rădulescu”.</p>

      <h2>Antrenor și lot</h2>
      <p>Mihai Popescu este antrenor principal. Căpitanul echipei
         este Andrei Ionescu.</p>

      <h2>Realizări</h2>
      <p>Multiplă campioană a României în ultimii ani.
         Participări frecvente în cupele europene.</p>
    </body>
    </html>
    ```

---

## Rezumat

- Un singur `<h1>` per pagină; folosește `<h2>` – `<h6>` ierarhic.
- `<p>` pentru paragrafe; nu abuza de `<br>`.
- `<a href="..." target="_blank" rel="noopener">` pentru tab nou.
- `<img>` cere **mereu** atributul `alt`.
- `<strong>` / `<em>` au **înțeles**, nu doar stil.
- `<div>` = container bloc; `<span>` = container inline.

---

**Pasul următor:** [→ Lecția 03: Liste și tabele](03-html-liste-tabele.md)
