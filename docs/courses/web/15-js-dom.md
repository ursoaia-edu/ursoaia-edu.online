---
lesson: 15
tags: [javascript, dom, querySelector, element, html]
summary: Selectează și modifică elementele paginii cu DOM API — textContent, classList, createElement.
---

# Lecția 15 · DOM — Manipulare HTML

!!! tip "Ce vei învăța"
    - Ce este **DOM**-ul și cum îl vede JavaScript-ul
    - Cum selectezi elemente cu `querySelector` / `querySelectorAll`
    - Cum citești și modifici textul (`textContent` vs `innerHTML`)
    - Cum modifici stil, clase și atribute
    - Cum **creezi** și **ștergi** elemente dinamic

---

## Ce este DOM-ul?

**DOM** = **Document Object Model**. Când browserul citește HTML-ul, îl transformă într-un **arbore de obiecte** în memorie. JavaScript poate:

- **Citi** arborele (ce scrie în pagină).
- **Modifica** arborele (schimbă text, adaugă elemente).
- **Reacționa** la evenimente (click, tastare — vom vedea în lecția 16).

Un HTML simplu:

```html
<html>
  <body>
    <h1>Titlu</h1>
    <p>Salut!</p>
  </body>
</html>
```

E reprezentat ca arbore:

```
document
 └── html
      ├── head
      └── body
           ├── h1  →  "Titlu"
           └── p   →  "Salut!"
```

Fiecare nod e un obiect cu proprietăți și metode.

---

## Selectarea elementelor

### `document.getElementById(id)`

Returnează elementul cu `id="..."`, sau `null` dacă nu există. **Cel mai rapid** selector:

```html
<h1 id="titlu">Bun venit!</h1>
```

```js
const titlu = document.getElementById("titlu");
console.log(titlu);   // <h1 id="titlu">Bun venit!</h1>
```

### `document.querySelector(selector)`

Acceptă orice selector CSS, returnează **primul** match:

```js
document.querySelector("#titlu");        // după ID
document.querySelector(".clasa");         // după clasă
document.querySelector("p");              // primul p
document.querySelector("ul li.activ");   // combinații CSS
```

### `document.querySelectorAll(selector)`

Returnează **toate** match-urile (NodeList):

```js
const toateP = document.querySelectorAll("p");
console.log(toateP.length);   // câte paragrafe există
```

### Metode legacy (evită-le)

- `document.getElementsByClassName("x")` — HTMLCollection **live** (se actualizează singur, surprinzător).
- `document.getElementsByTagName("p")` — la fel, legacy.

!!! tip "Folosește `querySelector` / `querySelectorAll`"
    Sunt cele mai flexibile (acceptă orice selector CSS) și cele mai previzibile. Celelalte sunt utile doar în situații foarte specifice.

---

## Citirea conținutului

```html
<h1 id="titlu">Bun <em>venit</em>!</h1>
<input id="varsta" value="14">
```

```js
const titlu = document.getElementById("titlu");

console.log(titlu.textContent);   // "Bun venit!"   — doar textul
console.log(titlu.innerHTML);     // "Bun <em>venit</em>!" — cu tag-uri HTML

const input = document.getElementById("varsta");
console.log(input.value);         // "14"   — pentru input-uri
```

- **`textContent`** — textul „curat”. **Recomandat** pentru scris — e sigur.
- **`innerHTML`** — include HTML. Util când ai nevoie real de HTML, dar **atenție la XSS** (vezi mai jos).
- **`.value`** — specific pentru `<input>`, `<textarea>`, `<select>`.

---

## Modificarea conținutului

```js
const titlu = document.querySelector("h1");
titlu.textContent = "Nou titlu!";
```

Browserul actualizează instant.

### `innerHTML` — cu atenție

```js
elem.innerHTML = "<strong>Important!</strong>";   // randează HTML
```

!!! warning "Pericol XSS cu `innerHTML`"
    Dacă pui text de la utilizator în `innerHTML` fără să-l sanitizezi, atacatorul poate injecta `<script>` și îți poate fura date. **Regula:** dacă nu ai nevoie specială de HTML, folosește `textContent`.

---

## Modificarea stilului

```js
const titlu = document.querySelector("h1");

titlu.style.color = "red";
titlu.style.fontSize = "32px";        // camelCase!
titlu.style.backgroundColor = "yellow"; // nu background-color
```

!!! note "Proprietăți CSS cu cratimă devin camelCase"
    `font-size` → `fontSize`, `background-color` → `backgroundColor`, `border-radius` → `borderRadius`.

### Stil direct vs clase CSS

**Preferă modificarea de clase** față de styling direct — e mai ușor de menținut:

```css
.activ { color: red; font-weight: bold; }
.ascuns { display: none; }
```

```js
elem.classList.add("activ");
elem.classList.remove("ascuns");
```

Stilurile rămân în CSS, JS-ul doar „spune” ce clase să aplice.

---

## Lucrul cu clase — `classList`

```js
const btn = document.querySelector("#meniu-btn");

btn.classList.add("deschis");       // adaugă
btn.classList.remove("inchis");     // scoate
btn.classList.toggle("activ");      // invers (add dacă nu e, remove dacă e)
btn.classList.contains("activ");    // true / false
btn.classList.replace("vechi", "nou");  // înlocuiește
```

`toggle` e extrem de util — e **standard** pentru butoane de tipul „deschide / închide meniul”, „mod dark”.

---

## Atribute

```html
<a id="link-docs" href="/home">Acasă</a>
<img id="poza" src="default.jpg" alt="Poză">
```

```js
const link = document.getElementById("link-docs");

link.getAttribute("href");              // "/home"
link.setAttribute("href", "/contact");
link.removeAttribute("target");

// Shortcut direct pentru atribute comune:
link.href = "/contact";    // același efect ca setAttribute
link.id = "link-nou";

const poza = document.getElementById("poza");
poza.src = "noua.jpg";
poza.alt = "O poză nouă";
```

---

## Crearea de elemente

Pași:

1. Creează elementul în memorie.
2. Configurează-l (text, clase, atribute).
3. **Atașează-l** în arbore.

```js
// 1. Creează
const nou = document.createElement("li");

// 2. Configurează
nou.textContent = "Item nou";
nou.classList.add("important");

// 3. Atașează în <ul>
const lista = document.querySelector("ul");
lista.appendChild(nou);
```

### `append` vs `appendChild`

`append()` e mai modern și acceptă și text:

```js
lista.append(nou);                      // adaugă un element
lista.append("text simplu");             // adaugă un nod text
lista.append(nou, "și text", altElem);  // mai multe odată
```

### `prepend`, `before`, `after`

```js
lista.prepend(primulItem);    // adaugă la început
el.before(inainteDeEl);        // inserează frate înainte
el.after(dupaEl);              // inserează frate după
```

---

## Ștergerea elementelor

```js
const item = document.querySelector(".de-sters");
item.remove();       // modern, simplu
```

Sau clasic (mai verbos):

```js
item.parentNode.removeChild(item);
```

---

## Iterarea peste NodeList

`querySelectorAll` returnează o **NodeList**, pe care o poți parcurge:

```js
const paragrafe = document.querySelectorAll("p");

// Cu forEach
paragrafe.forEach((p) => {
  p.style.color = "blue";
});

// Sau cu for...of
for (const p of paragrafe) {
  p.classList.add("citit");
}
```

---

## `textContent` vs `innerHTML` — siguranță

```js
// Sigur — textul apare așa cum e
elem.textContent = inputUtilizator;

// PERICULOS — dacă inputUtilizator conține <script>...</script>, se execută
elem.innerHTML = inputUtilizator;
```

Regula simplă: **folosește `textContent`** pentru date provenite de la utilizator. Folosește `innerHTML` doar pentru HTML static, controlat de tine.

---

## Exerciții

### Exercițiu 1 — Schimbă un titlu
Selectează `<h1>` din pagină și schimbă-i textul la "Salutare din JS!".

??? success "Soluție"
    ```html
    <h1>Titlu original</h1>
    <script src="app.js" defer></script>
    ```

    ```js
    const titlu = document.querySelector("h1");
    titlu.textContent = "Salutare din JS!";
    ```

### Exercițiu 2 — Colorează paragrafele
Selectează toate `<p>` din pagină și fă-le verzi.

??? success "Soluție"
    ```js
    const paragrafe = document.querySelectorAll("p");
    paragrafe.forEach((p) => {
      p.style.color = "green";
    });
    ```

    **Mai curat — cu clasă CSS:**

    ```css
    .verde { color: green; }
    ```

    ```js
    document.querySelectorAll("p").forEach(p => p.classList.add("verde"));
    ```

### Exercițiu 3 — Adaugă la listă
Dată fiind `<ul id="fructe"></ul>`, adaugă dinamic trei `<li>` cu "măr", "pară", "banană".

??? success "Soluție"
    ```js
    const lista = document.getElementById("fructe");
    const fructe = ["măr", "pară", "banană"];

    for (const fruct of fructe) {
      const li = document.createElement("li");
      li.textContent = fruct;
      lista.appendChild(li);
    }
    ```

### Exercițiu 4 — Șterge al doilea paragraf
Pagina are mai multe `<p>`. Șterge-l pe al doilea.

??? success "Soluție"
    ```js
    const paragrafe = document.querySelectorAll("p");
    if (paragrafe.length >= 2) {
      paragrafe[1].remove();   // index 1 = al doilea
    }
    ```

---

## Mini-proiect: Adaugă la listă

Pagina are un `<input>`, un buton „Adaugă” și un `<ul>` gol. Când utilizatorul scrie ceva și apasă butonul, un nou `<li>` apare în listă.

!!! note "Preview pentru lecția următoare"
    Vom folosi `addEventListener` — rețin e pentru lecția 16. Pentru moment, înțelege că `btn.addEventListener("click", () => { ... })` rulează funcția la fiecare click.

**Cod complet:**

```html
<!DOCTYPE html>
<html lang="ro">
  <head>
    <meta charset="UTF-8" />
    <title>Adaugă la listă</title>
    <script src="app.js" defer></script>
    <style>
      body { font-family: sans-serif; padding: 2rem; }
      #lista-fructe li { padding: 0.25rem 0; }
    </style>
  </head>
  <body>
    <h1>Fructe preferate</h1>

    <input id="nou-fruct" type="text" placeholder="Scrie un fruct..." />
    <button id="btn-adauga">Adaugă</button>

    <ul id="lista-fructe"></ul>
  </body>
</html>
```

```js
// Selectăm elementele o singură dată
const input = document.getElementById("nou-fruct");
const buton = document.getElementById("btn-adauga");
const lista = document.getElementById("lista-fructe");

// La fiecare click pe buton, adăugăm un <li> nou
buton.addEventListener("click", () => {
  const text = input.value.trim();
  if (!text) return;   // ignoră input gol

  const li = document.createElement("li");
  li.textContent = text;
  lista.appendChild(li);

  input.value = "";    // curăță input-ul
  input.focus();        // revine la input pentru următoarea intrare
});
```

---

## Rezumat

- **DOM**-ul e arborele de obiecte al HTML-ului, accesibil din JS.
- Selectează cu **`querySelector`** (primul) / **`querySelectorAll`** (toate) — acceptă orice selector CSS.
- Citește / scrie textul cu **`textContent`** (sigur) sau **`innerHTML`** (cu atenție la XSS).
- Pentru input-uri: **`.value`**.
- Modifică stilul prin `classList.add/remove/toggle` (preferat) sau `.style.*` direct.
- Creează elemente cu `createElement`, apoi atașează cu `appendChild` / `append`.
- Șterge cu `elem.remove()`.

---

**Pasul următor:** [→ Lecția 16: Evenimente](16-js-evenimente.md)
