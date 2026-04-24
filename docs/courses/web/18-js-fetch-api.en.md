---
lesson: 18
tags: [javascript, fetch, api, json, async, await, promises]
summary: Load data from the internet with fetch and async/await, parse JSON and display results in the DOM.
---

# Lesson 18 · Fetch and APIs

!!! tip "What you'll learn"
    - What **JSON** is and how to parse it in JS
    - What an **API** is and how to call it with `fetch`
    - The modern **`async`/`await`** syntax — vs `.then().then()`
    - Error handling: network vs HTTP
    - Free public APIs to practice with
    - How to display the results in the DOM

---

## What is JSON?

**JSON** = **JavaScript Object Notation**. A text format for exchanging data between applications. It looks very similar to a JS object, but with a few stricter rules:

- The keys are **always in double quotes**.
- The values can be: string, number, boolean, null, array, nested object.
- Trailing commas are not allowed.

```json
{
  "name": "Ana",
  "age": 14,
  "student": true,
  "hobbies": ["music", "football", "programming"],
  "address": {
    "city": "Chișinău",
    "country": "Moldova"
  }
}
```

### JSON in JS

Two main functions:

```js
// JSON text → JS object
const text = '{"name":"Ana","age":14}';
const obj = JSON.parse(text);
console.log(obj.name);    // "Ana"

// JS object → JSON text
const person = { name: "Mihai", age: 15 };
const json = JSON.stringify(person);
console.log(json);   // '{"name":"Mihai","age":15}'

// With nice indentation
console.log(JSON.stringify(person, null, 2));
```

---

## What is an API?

**API** = **Application Programming Interface**. On the web, an API is usually **a URL** that returns data (often JSON) when you request it.

Typical examples:

- The list of world countries with capitals and population.
- The weather forecast for a city.
- Live scores from games.
- Random pictures of cats.

When you navigate to an API URL, the browser shows you the raw **JSON text**. Your JS parses it and turns it into something useful.

---

## `fetch()` — how it works

`fetch(url)` **requests** data from a URL. It returns a **Promise** — an object that "will have" the response later.

### Variant with `.then()`

```js
fetch("https://jsonplaceholder.typicode.com/users/1")
  .then(response => response.json())   // parse the JSON
  .then(data => console.log(data))     // use the object
  .catch(error => console.error(error));
```

Flow:

1. `fetch(url)` sends the request, returns a Promise for the `response`.
2. `.then(response => response.json())` — when the response has come, parse it as JSON (and that returns a Promise).
3. `.then(data => ...)` — when the JSON is parsed, you have the JS object.
4. `.catch(error => ...)` — if something went wrong.

---

## `async` / `await` — modern syntax

The same operation, much clearer:

```js
async function loadUser() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

loadUser();
```

Comparison:

| `.then()` | `async/await` |
|-----------|---------------|
| function "chaining" | sequential code, top to bottom |
| `.catch()` at the end | classic `try { ... } catch { ... }` |
| difficult with many dependent steps | looks like synchronous code |

Rules:

- `await` works **only in `async` functions**.
- An `async function` always returns a **Promise**.
- `await` "waits" for the Promise to finish and gives you the value.

!!! tip "Prefer `async/await` in new code"
    It's easier to read, easier to debug (you can put a normal `breakpoint`) and allows the usual `try/catch` for errors.

---

## The `fetch` response

The `response` object has useful properties:

```js
const response = await fetch(url);

response.status;      // 200, 404, 500, etc.
response.ok;          // true if status is 200–299
response.statusText;  // "OK", "Not Found", etc.
await response.json();  // parse as JSON
await response.text();  // raw text
```

---

## Error handling

There are two different things here:

### 1. Network error (fetch throws)

If there's no internet, DNS fails, etc. — `fetch` throws an error. `catch` catches it.

### 2. HTTP error (fetch does NOT throw)

If the server responds with `404` or `500`, `fetch` **considers it went well** (it received a response). You have to check manually:

```js
async function load() {
  try {
    const response = await fetch("https://example.com/api");

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error.message);
  }
}
```

!!! warning "Don't forget to check `response.ok`"
    It's one of the most common pitfalls with `fetch`. You could receive `{"error": "Not authorized"}` with status 401 and ignore it completely.

---

## Public APIs without a key

Perfect for practice — you don't need an account or a token:

| API | Example URL | Returns |
|-----|-------------|------------|
| **JSONPlaceholder** | `https://jsonplaceholder.typicode.com/users/1` | fake user |
| **JSONPlaceholder (all)** | `https://jsonplaceholder.typicode.com/users` | array of users |
| **REST Countries** | `https://restcountries.com/v3.1/name/romania` | data about Romania |
| **Open-Meteo** | `https://api.open-meteo.com/v1/forecast?latitude=47&longitude=28&current=temperature_2m` | weather |
| **Dog CEO** | `https://dog.ceo/api/breeds/image/random` | random dog photo URL |
| **Cat Facts** | `https://catfact.ninja/fact` | random cat fact |

Open a URL in the browser to see the raw JSON, then call it from code.

---

## CORS — a brief warning

**CORS** = Cross-Origin Resource Sharing. The browser implicitly blocks JS requests to other domains than that of your page, if the destination server doesn't explicitly allow it.

- The APIs listed above **allow** CORS — they work.
- Some APIs don't allow it — you'll see in the console an error `CORS policy...`.

If you encounter this, you need an intermediate server (backend) — a topic for later.

---

## Displaying the data in the DOM

Typical flow:

1. Call `fetch`.
2. Parse JSON.
3. Select a container in the page.
4. Build the HTML / text and set it.

```js
async function loadUser() {
  const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
  const user = await response.json();

  document.querySelector("#name").textContent = user.name;
  document.querySelector("#email").textContent = user.email;
  document.querySelector("#city").textContent = user.address.city;
}

loadUser();
```

---

## Exercises

### Exercise 1 — Fetch a user
Call `https://jsonplaceholder.typicode.com/users/1` and display the received object in the Console.

??? success "Solution"
    ```js
    async function main() {
      const r = await fetch("https://jsonplaceholder.typicode.com/users/1");
      const user = await r.json();
      console.log(user);
    }

    main();
    ```

    In the Console you'll see the object with `name`, `email`, `address`, `phone`, `company`, etc.

### Exercise 2 — Show the name and email
The page has `<p id="info"></p>`. Display there "Name: ... — Email: ...".

??? success "Solution"
    ```html
    <p id="info">Loading...</p>
    ```

    ```js
    async function main() {
      const r = await fetch("https://jsonplaceholder.typicode.com/users/1");
      const user = await r.json();

      document.getElementById("info").textContent =
        `Name: ${user.name} — Email: ${user.email}`;
    }

    main();
    ```

### Exercise 3 — Random dog photo
"Random dog" button. On click, change `<img>` with a random photo.

??? success "Solution"
    ```html
    <img id="dog" alt="dog" style="max-width: 300px;" />
    <button id="btn">Another dog</button>
    ```

    ```js
    const img = document.getElementById("dog");
    const btn = document.getElementById("btn");

    const load = async () => {
      const r = await fetch("https://dog.ceo/api/breeds/image/random");
      const data = await r.json();
      img.src = data.message;   // the photo URL
    };

    btn.addEventListener("click", load);
    load();   // load one at start
    ```

### Exercise 4 — Parse a hardcoded JSON
You have the string `'{"grades": [8, 9, 7, 10]}'`. Parse it and display the average.

??? success "Solution"
    ```js
    const text = '{"grades": [8, 9, 7, 10]}';
    const obj = JSON.parse(text);

    const sum = obj.grades.reduce((total, n) => total + n, 0);
    const average = sum / obj.grades.length;

    console.log(`Average: ${average.toFixed(2)}`);   // Average: 8.50
    ```

---

## Mini-project: User gallery

You fetch all the users from JSONPlaceholder and display a "card" for each one, in a responsive grid.

**Complete code:**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>User gallery</title>
    <script src="app.js" defer></script>
    <style>
      body {
        font-family: sans-serif;
        padding: 2rem;
        background: #f9fafb;
      }
      h1 { text-align: center; }
      #grid {
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
      #status {
        text-align: center;
        color: #64748b;
        padding: 2rem;
      }
    </style>
  </head>
  <body>
    <h1>Users</h1>

    <div id="status">Loading...</div>
    <div id="grid"></div>
  </body>
</html>
```

```js
const grid = document.getElementById("grid");
const status = document.getElementById("status");

// Build a DOM card for a user
const createCard = (user) => {
  const card = document.createElement("div");
  card.className = "card";

  const title = document.createElement("h3");
  title.textContent = user.name;

  const email = document.createElement("p");
  email.textContent = user.email;

  const city = document.createElement("p");
  city.className = "muted";
  city.textContent = `${user.address.city} · ${user.company.name}`;

  card.append(title, email, city);
  return card;
};

// Load and display all users
const loadUsers = async () => {
  try {
    const r = await fetch("https://jsonplaceholder.typicode.com/users");

    if (!r.ok) {
      throw new Error(`HTTP ${r.status}`);
    }

    const users = await r.json();

    status.style.display = "none";

    for (const user of users) {
      grid.appendChild(createCard(user));
    }
  } catch (err) {
    status.textContent = `Error loading: ${err.message}`;
  }
};

loadUsers();
```

**Ideas to extend:**

- Add a search input that filters users by name (`input` event on the input).
- Save the users in `localStorage` so you don't have to request them every time.
- Click a card to display that user's posts (from `/posts?userId=1`).

---

## Summary

- **JSON** is a text format for data. `JSON.parse` converts it to an object, `JSON.stringify` the other way around.
- **API** = a URL that returns data. You call it with **`fetch(url)`**.
- Prefer **`async/await`** instead of `.then().then()` — it's more readable.
- `fetch` does NOT throw on HTTP 404/500 — check `response.ok`.
- Free public APIs: **JSONPlaceholder**, **REST Countries**, **Open-Meteo**, **Dog CEO**.
- Typical flow: fetch → parse → build DOM → display.
- **CORS** can block some APIs — it requires a backend to bypass.

---

**Next step:** [→ Lesson 19: Portfolio project](19-proiect-portofoliu.md)
