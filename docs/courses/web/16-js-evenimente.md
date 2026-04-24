---
lesson: 16
tags: [javascript, evenimente, addEventListener, click, submit, dom]
summary: Răspunde la acțiunile utilizatorului cu addEventListener — click, submit, input, keydown.
---

# Lecția 16 · Evenimente

!!! tip "Ce vei învăța"
    - Ce sunt evenimentele și trei moduri de a le asculta
    - De ce `addEventListener` e alegerea modernă
    - Evenimentele comune: `click`, `submit`, `input`, `change`, `keydown`
    - Obiectul `event`: `e.target`, `e.preventDefault`, `e.stopPropagation`
    - Event bubbling și delegation (pe scurt)

---

## Ce sunt evenimentele?

Un **eveniment** e o „întâmplare” în browser: un click, o tastă apăsată, un formular trimis, o pagină încărcată. JavaScript poate **asculta** aceste evenimente și rula cod ca răspuns.

Exemple de evenimente pe care le vei folosi des:

- **`click`** — utilizatorul apasă un buton sau un link.
- **`submit`** — un `<form>` e trimis.
- **`input`** — textul dintr-un `<input>` s-a schimbat.
- **`change`** — s-a schimbat valoarea unui `<select>` sau unui checkbox.
- **`keydown`** — s-a apăsat o tastă.
- **`DOMContentLoaded`** — HTML-ul e parsat și DOM-ul e gata.

---

## Trei moduri (din vechi în nou)

### 1. Inline în HTML (EVITĂ)

```html
<button onclick="alert('salut')">Apasă</button>
```

Amestecă logică cu structură. **Nu folosi.**

### 2. Proprietate `on<eveniment>`

```js
const btn = document.querySelector("button");
btn.onclick = () => alert("salut");
```

Limitat la **un singur handler** — dacă îl setezi de două ori, al doilea îl suprascrie.

### 3. `addEventListener` (RECOMANDAT)

```js
const btn = document.querySelector("button");
btn.addEventListener("click", () => {
  alert("salut");
});
```

Avantaje:

- Poți adăuga **multiple** handlere pentru același eveniment.
- Poți specifica opțiuni (`once`, `passive`, `capture`).
- Ușor de scos cu `removeEventListener`.

---

## `addEventListener`

Semnătura:

```js
elem.addEventListener(tipEveniment, handler, optiuni);
```

- **`tipEveniment`** — un string: `"click"`, `"submit"`, `"keydown"`, etc. (fără „on”).
- **`handler`** — funcția care se rulează la eveniment.
- **`optiuni`** — opțional, obiect: `{ once: true }`, `{ passive: true }`, `{ capture: true }`.

Exemple:

```js
const btn = document.querySelector("#salut-btn");

btn.addEventListener("click", () => {
  console.log("Ai dat click!");
});

// Handler care rulează o singură dată
btn.addEventListener("click", () => alert("doar o dată"), { once: true });
```

---

## Evenimente comune

### `click` și `dblclick`

```js
btn.addEventListener("click", () => console.log("click simplu"));
btn.addEventListener("dblclick", () => console.log("dublu click"));
```

### `input` — la fiecare tastă

```js
const cautare = document.querySelector("#cautare");
cautare.addEventListener("input", (e) => {
  console.log("Utilizatorul a scris:", e.target.value);
});
```

### `change` — când se schimbă un select / checkbox

```js
const optiune = document.querySelector("#optiune");
optiune.addEventListener("change", (e) => {
  console.log("Nouă valoare:", e.target.value);
});
```

### `submit` — la trimiterea unui form

```js
const form = document.querySelector("#formular");
form.addEventListener("submit", (e) => {
  e.preventDefault();   // oprește reîncărcarea paginii
  console.log("Form trimis!");
});
```

### `keydown`, `keyup`, `keypress`

```js
document.addEventListener("keydown", (e) => {
  console.log(`Ai apăsat tasta: ${e.key}`);
});
```

`e.key` e string-ul tastei: `"a"`, `"Enter"`, `"ArrowUp"`, `" "` (spațiu), etc.

### `mouseenter` / `mouseleave`

```js
const card = document.querySelector(".card");
card.addEventListener("mouseenter", () => card.classList.add("hover"));
card.addEventListener("mouseleave", () => card.classList.remove("hover"));
```

### `load` / `DOMContentLoaded`

```js
// HTML-ul e parsat (fără a aștepta imagini mari)
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM gata!");
});

// Totul e încărcat: HTML + CSS + imagini + scripturi
window.addEventListener("load", () => {
  console.log("Totul e gata!");
});
```

Dacă folosești `<script defer>`, scriptul rulează automat după ce DOM-ul e parsat — deci de obicei nu mai ai nevoie de `DOMContentLoaded`.

---

## Obiectul `event`

Handler-ul primește automat un obiect `event` (de obicei numit `e` sau `event`):

```js
btn.addEventListener("click", (e) => {
  console.log(e.type);      // "click"
  console.log(e.target);    // elementul pe care s-a declanșat
  console.log(e.clientX, e.clientY);  // coordonatele mouse-ului
});
```

Cele mai utile proprietăți / metode:

| Proprietate / metodă | Ce face |
|----------------------|---------|
| `e.target` | elementul pe care s-a **declanșat** evenimentul |
| `e.currentTarget` | elementul pe care ai **atașat listener**-ul |
| `e.type` | tipul evenimentului (`"click"`, etc.) |
| `e.preventDefault()` | oprește comportamentul default |
| `e.stopPropagation()` | oprește propagarea spre părinți |
| `e.key` | tasta apăsată (pentru keydown) |

---

## `preventDefault()`

Unele elemente au comportament **default**:

- Un `<a href>` navighează când e click.
- Un `<form>` reîncarcă pagina când e `submit`.
- `Space` pe pagină o scrollează.

Ca să-l oprești:

```js
const link = document.querySelector("a");
link.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("Am oprit navigarea.");
});

const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();   // procesează în JS, nu reîncărca
  // ... validează, trimite cu fetch, etc.
});
```

---

## Event bubbling

Când apeși pe un element, evenimentul **urcă** (bubble) prin părinți până la `document`:

```html
<div id="exterior">
  <button id="buton">Click</button>
</div>
```

```js
document.getElementById("exterior").addEventListener("click", () => {
  console.log("div exterior");
});

document.getElementById("buton").addEventListener("click", () => {
  console.log("buton");
});
```

Click pe buton afișează:

```text
buton
div exterior
```

Evenimentul „a urcat” de la buton la div.

### `stopPropagation`

Dacă nu vrei propagarea:

```js
document.getElementById("buton").addEventListener("click", (e) => {
  e.stopPropagation();
  console.log("Doar buton.");
});
```

### Event delegation (pe scurt)

Bubbling-ul permite o șmecherie elegantă: atașezi listener pe **un părinte** și folosești `e.target` ca să știi pe ce s-a dat click. Util pentru **copii dinamici** (creați după ce ai pornit):

```js
document.querySelector("#lista").addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    e.target.classList.toggle("selectat");
  }
});
```

Nu mai trebuie să pui listener pe fiecare `<li>` nou creat.

---

## Scoaterea unui listener — `removeEventListener`

Ca să poți scoate un listener, trebuie să ai **referința** la funcție (deci nu anonimă):

```js
function handler() {
  console.log("odată");
}

btn.addEventListener("click", handler);
btn.removeEventListener("click", handler);
```

Dacă ai nevoie doar să ruleze o dată, folosește opțiunea `once`:

```js
btn.addEventListener("click", () => alert("doar o dată"), { once: true });
```

---

## Exerciții

### Exercițiu 1 — Alert la click
Un buton care la click afișează un alert cu „Salut!”.

??? success "Soluție"
    ```html
    <button id="btn-salut">Apasă-mă</button>
    ```

    ```js
    const btn = document.getElementById("btn-salut");
    btn.addEventListener("click", () => {
      alert("Salut!");
    });
    ```

### Exercițiu 2 — Log la tastare
Un `<input>` care loghează valoarea curentă la fiecare tastă.

??? success "Soluție"
    ```html
    <input id="text" placeholder="Scrie ceva..." />
    ```

    ```js
    const input = document.getElementById("text");
    input.addEventListener("input", (e) => {
      console.log("Ai scris:", e.target.value);
    });
    ```

### Exercițiu 3 — Schimbă culoarea fundalului
Un buton care la fiecare click schimbă culoarea fundalului paginii (random).

??? success "Soluție"
    ```html
    <button id="schimba">Schimbă culoarea</button>
    ```

    ```js
    const btn = document.getElementById("schimba");

    const culoareRandom = () => {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      return `rgb(${r}, ${g}, ${b})`;
    };

    btn.addEventListener("click", () => {
      document.body.style.backgroundColor = culoareRandom();
    });
    ```

### Exercițiu 4 — Afișează tasta apăsată
Pagina afișează pe ecran ce tastă a fost apăsată ultima.

??? success "Soluție"
    ```html
    <p>Ultima tastă: <span id="tasta">—</span></p>
    ```

    ```js
    const span = document.getElementById("tasta");
    document.addEventListener("keydown", (e) => {
      span.textContent = e.key;
    });
    ```

---

## Mini-proiect: Click counter

Un buton care numără câte click-uri a primit și afișează rezultatul. Plus un buton „Reset” care pune contorul la zero.

**Cod complet:**

```html
<!DOCTYPE html>
<html lang="ro">
  <head>
    <meta charset="UTF-8" />
    <title>Click counter</title>
    <script src="app.js" defer></script>
    <style>
      body {
        font-family: sans-serif;
        padding: 2rem;
        text-align: center;
      }
      #scor {
        font-size: 3rem;
        font-weight: bold;
        color: #2563eb;
      }
      button {
        font-size: 1rem;
        padding: 0.75rem 1.5rem;
        margin: 0.5rem;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <h1>Click counter</h1>
    <p>Scor: <span id="scor">0</span></p>
    <button id="btn-click">Apasă-mă!</button>
    <button id="btn-reset">Reset</button>
  </body>
</html>
```

```js
// Selectăm elementele
const scor = document.getElementById("scor");
const btnClick = document.getElementById("btn-click");
const btnReset = document.getElementById("btn-reset");

let counter = 0;

// Incrementează la click
btnClick.addEventListener("click", () => {
  counter++;
  scor.textContent = counter;
});

// Resetează
btnReset.addEventListener("click", () => {
  counter = 0;
  scor.textContent = counter;
});
```

**Idei de extindere:**

- Salvează scorul în `localStorage` ca să rămână după reîncărcare.
- Schimbă culoarea scorului după prag (100 = auriu, 500 = curcubeu).
- Adaugă un al doilea buton cu valoare negativă („scade”).

---

## Rezumat

- **Evenimentele** sunt acțiunile utilizatorului (click, tastare, submit) la care JS poate reacționa.
- Folosește **`addEventListener(tip, handler)`** — permite multiple handlere și opțiuni.
- Handler-ul primește un obiect `event` cu `target`, `type`, `key`, etc.
- **`e.preventDefault()`** oprește comportamentul default (navigare, reload de form).
- **Event bubbling:** evenimentul urcă prin părinți. **Delegation:** ascultă pe părinte pentru copii dinamici.
- Pentru a rula o dată, folosește `{ once: true }` în opțiuni.

---

**Pasul următor:** [→ Lecția 17: Formulare cu validare JS](17-js-formulare-validare.md)
