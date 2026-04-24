---
lesson: 18
tags: [javascript, fetch, api, json, async, await, promises]
summary: Încarcă date de pe internet cu fetch și async/await, parsează JSON și afișează rezultate în DOM.
---

# Lecția 18 · Fetch și API-uri

!!! tip "Ce vei învăța"
    - Ce este **JSON** și cum îl parsezi în JS
    - Ce este un **API** și cum îl apelezi cu `fetch`
    - Sintaxa modernă **`async`/`await`** — vs `.then().then()`
    - Gestionarea erorilor: network vs HTTP
    - API-uri publice gratuite pentru exersat
    - Cum afișezi rezultatele în DOM

---

## Ce este JSON?

**JSON** = **JavaScript Object Notation**. Un format text pentru schimbul de date între aplicații. Arată foarte similar cu un obiect JS, dar cu câteva reguli mai stricte:

- Cheile sunt **mereu în ghilimele duble**.
- Valorile pot fi: string, number, boolean, null, array, obiect imbricat.
- Nu se permit virgule trailing.

```json
{
  "nume": "Ana",
  "varsta": 14,
  "student": true,
  "hobbyuri": ["muzică", "fotbal", "programare"],
  "adresa": {
    "oras": "Chișinău",
    "tara": "Moldova"
  }
}
```

### JSON în JS

Două funcții principale:

```js
// JSON text → obiect JS
const text = '{"nume":"Ana","varsta":14}';
const obj = JSON.parse(text);
console.log(obj.nume);    // "Ana"

// Obiect JS → JSON text
const persoana = { nume: "Mihai", varsta: 15 };
const json = JSON.stringify(persoana);
console.log(json);   // '{"nume":"Mihai","varsta":15}'

// Cu indentare frumoasă
console.log(JSON.stringify(persoana, null, 2));
```

---

## Ce este un API?

**API** = **Application Programming Interface**. Pe web, un API e de obicei **un URL** care returnează date (adesea JSON) când îl ceri.

Exemple tipice:

- Lista țărilor lumii cu capitale și populație.
- Prognoza meteo pentru un oraș.
- Scoruri live de la meciuri.
- Poze random cu pisici.

Când navighezi la un URL de API, browserul îți arată **textul JSON** brut. JS-ul tău îl parsează și îl transformă în ceva util.

---

## `fetch()` — cum funcționează

`fetch(url)` **cere** date de la un URL. Returnează o **Promise** (promisiune) — un obiect care „va avea” răspunsul mai târziu.

### Varianta cu `.then()`

```js
fetch("https://jsonplaceholder.typicode.com/users/1")
  .then(response => response.json())   // parsează JSON-ul
  .then(data => console.log(data))      // folosește obiectul
  .catch(error => console.error(error));
```

Flow:

1. `fetch(url)` trimite cererea, returnează o Promise pentru `response`.
2. `.then(response => response.json())` — când răspunsul a venit, parsează-l ca JSON (și asta returnează o Promise).
3. `.then(data => ...)` — când JSON-ul e parsat, ai obiectul JS.
4. `.catch(error => ...)` — dacă ceva a mers prost.

---

## `async` / `await` — sintaxă modernă

Aceeași operație, mult mai clar:

```js
async function incarcaUser() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

incarcaUser();
```

Comparație:

| `.then()` | `async/await` |
|-----------|---------------|
| „chaining” de funcții | cod secvențial, de sus în jos |
| `.catch()` la sfârșit | `try { ... } catch { ... }` clasic |
| greu cu multe pași dependenți | arată ca un cod sincron |

Reguli:

- `await` funcționează **doar în funcții `async`**.
- `async function` returnează mereu o **Promise**.
- `await` „așteaptă” ca Promise-ul să termine și îți dă valoarea.

!!! tip "Preferă `async/await` în cod nou"
    E mai ușor de citit, mai ușor de debug (poți pune `breakpoint` normal) și permite `try/catch` uzual pentru erori.

---

## Răspunsul `fetch`

Obiectul `response` are proprietăți utile:

```js
const response = await fetch(url);

response.status;      // 200, 404, 500, etc.
response.ok;          // true dacă status e 200–299
response.statusText;  // "OK", "Not Found", etc.
await response.json();  // parsează ca JSON
await response.text();  // text brut
```

---

## Gestionarea erorilor

Aici sunt două lucruri diferite:

### 1. Network error (fetch aruncă)

Dacă nu e internet, DNS eșuează, etc. — `fetch` aruncă o eroare. `catch` o prinde.

### 2. HTTP error (fetch NU aruncă)

Dacă serverul răspunde cu `404` sau `500`, `fetch` **consideră că a mers bine** (a primit răspuns). Trebuie să verifici manual:

```js
async function incarca() {
  try {
    const response = await fetch("https://exemplu.ro/api");

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Eroare:", error.message);
  }
}
```

!!! warning "Nu uita să verifici `response.ok`"
    E una dintre capcanele cele mai frecvente la `fetch`. Ai putea să primești `{"error": "Not authorized"}` cu status 401 și să ignori complet.

---

## API-uri publice fără cheie

Perfecte pentru exersat — nu ai nevoie de cont sau token:

| API | URL exemplu | Returnează |
|-----|-------------|------------|
| **JSONPlaceholder** | `https://jsonplaceholder.typicode.com/users/1` | user fake |
| **JSONPlaceholder (toți)** | `https://jsonplaceholder.typicode.com/users` | array de users |
| **REST Countries** | `https://restcountries.com/v3.1/name/romania` | date despre România |
| **Open-Meteo** | `https://api.open-meteo.com/v1/forecast?latitude=47&longitude=28&current=temperature_2m` | vremea |
| **Dog CEO** | `https://dog.ceo/api/breeds/image/random` | URL poză random de câine |
| **Cat Facts** | `https://catfact.ninja/fact` | fapt random despre pisici |

Deschide un URL în browser ca să vezi JSON-ul brut, apoi apelează-l din cod.

---

## CORS — o avertizare scurtă

**CORS** = Cross-Origin Resource Sharing. Browserul blochează implicit cererile JS către alte domenii decât cel al paginii tale, dacă serverul destinație nu permite explicit.

- API-urile listate mai sus **permit** CORS — funcționează.
- Unele API-uri nu permit — vei vedea în consolă o eroare `CORS policy...`.

Dacă întâlnești asta, ai nevoie de un server intermediar (backend) — subiect pentru mai târziu.

---

## Afișarea datelor în DOM

Flow tipic:

1. Apelează `fetch`.
2. Parsează JSON.
3. Selectează un container din pagină.
4. Construiește HTML-ul / textul și setează.

```js
async function incarcaUser() {
  const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
  const user = await response.json();

  document.querySelector("#nume").textContent = user.name;
  document.querySelector("#email").textContent = user.email;
  document.querySelector("#oras").textContent = user.address.city;
}

incarcaUser();
```

---

## Exerciții

### Exercițiu 1 — Fetch la un user
Apelează `https://jsonplaceholder.typicode.com/users/1` și afișează obiectul primit în Console.

??? success "Soluție"
    ```js
    async function main() {
      const r = await fetch("https://jsonplaceholder.typicode.com/users/1");
      const user = await r.json();
      console.log(user);
    }

    main();
    ```

    În Console vei vedea obiectul cu `name`, `email`, `address`, `phone`, `company`, etc.

### Exercițiu 2 — Afișează numele și email-ul
Pagina are `<p id="info"></p>`. Afișează acolo „Nume: ... — Email: ...”.

??? success "Soluție"
    ```html
    <p id="info">Se încarcă...</p>
    ```

    ```js
    async function main() {
      const r = await fetch("https://jsonplaceholder.typicode.com/users/1");
      const user = await r.json();

      document.getElementById("info").textContent =
        `Nume: ${user.name} — Email: ${user.email}`;
    }

    main();
    ```

### Exercițiu 3 — Poză random de câine
Buton „Random câine”. La click, schimbă `<img>` cu o poză random.

??? success "Soluție"
    ```html
    <img id="caine" alt="câine" style="max-width: 300px;" />
    <button id="btn">Alt câine</button>
    ```

    ```js
    const img = document.getElementById("caine");
    const btn = document.getElementById("btn");

    const incarca = async () => {
      const r = await fetch("https://dog.ceo/api/breeds/image/random");
      const data = await r.json();
      img.src = data.message;   // URL-ul pozei
    };

    btn.addEventListener("click", incarca);
    incarca();   // încarcă una la start
    ```

### Exercițiu 4 — Parsează un JSON hardcoded
Ai string-ul `'{"note": [8, 9, 7, 10]}'`. Parsează-l și afișează media.

??? success "Soluție"
    ```js
    const text = '{"note": [8, 9, 7, 10]}';
    const obj = JSON.parse(text);

    const suma = obj.note.reduce((total, n) => total + n, 0);
    const media = suma / obj.note.length;

    console.log(`Media: ${media.toFixed(2)}`);   // Media: 8.50
    ```

---

## Mini-proiect: Galerie de utilizatori

Aduci toți userii de la JSONPlaceholder și afișezi câte un „card” pentru fiecare, într-o grilă responsive.

**Cod complet:**

```html
<!DOCTYPE html>
<html lang="ro">
  <head>
    <meta charset="UTF-8" />
    <title>Galerie de utilizatori</title>
    <script src="app.js" defer></script>
    <style>
      body {
        font-family: sans-serif;
        padding: 2rem;
        background: #f9fafb;
      }
      h1 { text-align: center; }
      #grila {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1rem;
        max-width: 1200px;
        margin: 0 auto;
      }
      .card {
        background: white;
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        transition: transform 0.15s;
      }
      .card:hover {
        transform: translateY(-2px);
      }
      .card h3 {
        margin: 0 0 0.5rem 0;
        color: #2563eb;
      }
      .card .muted {
        color: #64748b;
        font-size: 0.9rem;
      }
      #stare {
        text-align: center;
        color: #64748b;
        padding: 2rem;
      }
    </style>
  </head>
  <body>
    <h1>Utilizatori</h1>

    <div id="stare">Se încarcă...</div>
    <div id="grila"></div>
  </body>
</html>
```

```js
const grila = document.getElementById("grila");
const stare = document.getElementById("stare");

// Construiește un card DOM pentru un user
const creeazaCard = (user) => {
  const card = document.createElement("div");
  card.className = "card";

  const titlu = document.createElement("h3");
  titlu.textContent = user.name;

  const email = document.createElement("p");
  email.textContent = user.email;

  const oras = document.createElement("p");
  oras.className = "muted";
  oras.textContent = `${user.address.city} · ${user.company.name}`;

  card.append(titlu, email, oras);
  return card;
};

// Încarcă și afișează toți userii
const incarcaUseri = async () => {
  try {
    const r = await fetch("https://jsonplaceholder.typicode.com/users");

    if (!r.ok) {
      throw new Error(`HTTP ${r.status}`);
    }

    const useri = await r.json();

    stare.style.display = "none";

    for (const user of useri) {
      grila.appendChild(creeazaCard(user));
    }
  } catch (err) {
    stare.textContent = `Eroare la încărcare: ${err.message}`;
  }
};

incarcaUseri();
```

**Idei de extindere:**

- Adaugă un input de căutare care filtrează userii după nume (event `input` pe input).
- Salvează userii în `localStorage` ca să nu-i ceri de fiecare dată.
- Fă click pe card să afișeze postările acelui user (din `/posts?userId=1`).

---

## Rezumat

- **JSON** e un format text pentru date. `JSON.parse` îl convertește la obiect, `JSON.stringify` invers.
- **API** = un URL care returnează date. Apelezi cu **`fetch(url)`**.
- Preferă **`async/await`** în loc de `.then().then()` — e mai lizibil.
- `fetch` NU aruncă eroare la HTTP 404/500 — verifică `response.ok`.
- API-uri publice gratuite: **JSONPlaceholder**, **REST Countries**, **Open-Meteo**, **Dog CEO**.
- Flow tipic: fetch → parsează → construiește DOM → afișează.
- **CORS** poate bloca unele API-uri — necesită backend ca să le ocoleștI.

---

**Pasul următor:** [→ Lecția 19: Proiect portofoliu](19-proiect-portofoliu.md)
