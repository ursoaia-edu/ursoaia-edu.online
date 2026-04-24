---
lesson: 15
tags: [javascript, dom, querySelector, element, html]
summary: Select and modify page elements with the DOM API — textContent, classList, createElement.
---

# Lesson 15 · DOM — HTML manipulation

!!! tip "What you'll learn"
    - What the **DOM** is and how JavaScript sees it
    - How to select elements with `querySelector` / `querySelectorAll`
    - How to read and modify text (`textContent` vs `innerHTML`)
    - How to modify styles, classes and attributes
    - How to **create** and **delete** elements dynamically

---

## What is the DOM?

**DOM** = **Document Object Model**. When the browser reads the HTML, it transforms it into a **tree of objects** in memory. JavaScript can:

- **Read** the tree (what's written on the page).
- **Modify** the tree (change text, add elements).
- **React** to events (click, typing — we'll see in lesson 16).

A simple HTML:

```html
<html>
  <body>
    <h1>Title</h1>
    <p>Hello!</p>
  </body>
</html>
```

It's represented as a tree:

```
document
 └── html
      ├── head
      └── body
           ├── h1  →  "Title"
           └── p   →  "Hello!"
```

Each node is an object with properties and methods.

---

## Selecting elements

### `document.getElementById(id)`

Returns the element with `id="..."`, or `null` if it doesn't exist. **The fastest** selector:

```html
<h1 id="title">Welcome!</h1>
```

```js
const title = document.getElementById("title");
console.log(title);   // <h1 id="title">Welcome!</h1>
```

### `document.querySelector(selector)`

Accepts any CSS selector, returns the **first** match:

```js
document.querySelector("#title");        // by ID
document.querySelector(".class");        // by class
document.querySelector("p");             // first p
document.querySelector("ul li.active");  // CSS combinations
```

### `document.querySelectorAll(selector)`

Returns **all** matches (NodeList):

```js
const allP = document.querySelectorAll("p");
console.log(allP.length);   // how many paragraphs exist
```

### Legacy methods (avoid them)

- `document.getElementsByClassName("x")` — **live** HTMLCollection (updates by itself, surprisingly).
- `document.getElementsByTagName("p")` — same, legacy.

!!! tip "Use `querySelector` / `querySelectorAll`"
    They are the most flexible (accept any CSS selector) and the most predictable. The others are useful only in very specific situations.

---

## Reading content

```html
<h1 id="title">Wel<em>come</em>!</h1>
<input id="age" value="14">
```

```js
const title = document.getElementById("title");

console.log(title.textContent);   // "Welcome!"   — only the text
console.log(title.innerHTML);     // "Wel<em>come</em>!" — with HTML tags

const input = document.getElementById("age");
console.log(input.value);         // "14"   — for inputs
```

- **`textContent`** — "clean" text. **Recommended** for writing — it's safe.
- **`innerHTML`** — includes HTML. Useful when you really need HTML, but **watch out for XSS** (see below).
- **`.value`** — specific for `<input>`, `<textarea>`, `<select>`.

---

## Modifying content

```js
const title = document.querySelector("h1");
title.textContent = "New title!";
```

The browser updates instantly.

### `innerHTML` — with caution

```js
elem.innerHTML = "<strong>Important!</strong>";   // renders HTML
```

!!! warning "XSS danger with `innerHTML`"
    If you put user text into `innerHTML` without sanitizing it, an attacker can inject `<script>` and steal data. **Rule:** if you don't have a special HTML need, use `textContent`.

---

## Modifying the style

```js
const title = document.querySelector("h1");

title.style.color = "red";
title.style.fontSize = "32px";        // camelCase!
title.style.backgroundColor = "yellow"; // not background-color
```

!!! note "CSS properties with hyphens become camelCase"
    `font-size` → `fontSize`, `background-color` → `backgroundColor`, `border-radius` → `borderRadius`.

### Direct style vs CSS classes

**Prefer modifying classes** rather than direct styling — it's easier to maintain:

```css
.active { color: red; font-weight: bold; }
.hidden { display: none; }
```

```js
elem.classList.add("active");
elem.classList.remove("hidden");
```

The styles stay in CSS, the JS only "tells" which classes to apply.

---

## Working with classes — `classList`

```js
const btn = document.querySelector("#menu-btn");

btn.classList.add("open");          // add
btn.classList.remove("closed");     // remove
btn.classList.toggle("active");     // invert (add if missing, remove if present)
btn.classList.contains("active");   // true / false
btn.classList.replace("old", "new");  // replace
```

`toggle` is extremely useful — it's **standard** for buttons like "open / close menu", "dark mode".

---

## Attributes

```html
<a id="link-docs" href="/home">Home</a>
<img id="photo" src="default.jpg" alt="Photo">
```

```js
const link = document.getElementById("link-docs");

link.getAttribute("href");              // "/home"
link.setAttribute("href", "/contact");
link.removeAttribute("target");

// Direct shortcut for common attributes:
link.href = "/contact";    // same effect as setAttribute
link.id = "new-link";

const photo = document.getElementById("photo");
photo.src = "new.jpg";
photo.alt = "A new photo";
```

---

## Creating elements

Steps:

1. Create the element in memory.
2. Configure it (text, classes, attributes).
3. **Attach it** to the tree.

```js
// 1. Create
const newItem = document.createElement("li");

// 2. Configure
newItem.textContent = "New item";
newItem.classList.add("important");

// 3. Attach to <ul>
const list = document.querySelector("ul");
list.appendChild(newItem);
```

### `append` vs `appendChild`

`append()` is more modern and also accepts text:

```js
list.append(newItem);                          // adds an element
list.append("plain text");                     // adds a text node
list.append(newItem, "and text", otherElem);   // multiple at once
```

### `prepend`, `before`, `after`

```js
list.prepend(firstItem);    // adds at the beginning
el.before(beforeEl);        // inserts sibling before
el.after(afterEl);          // inserts sibling after
```

---

## Removing elements

```js
const item = document.querySelector(".to-delete");
item.remove();       // modern, simple
```

Or classic (more verbose):

```js
item.parentNode.removeChild(item);
```

---

## Iterating over a NodeList

`querySelectorAll` returns a **NodeList**, which you can iterate:

```js
const paragraphs = document.querySelectorAll("p");

// With forEach
paragraphs.forEach((p) => {
  p.style.color = "blue";
});

// Or with for...of
for (const p of paragraphs) {
  p.classList.add("read");
}
```

---

## `textContent` vs `innerHTML` — safety

```js
// Safe — the text appears as is
elem.textContent = userInput;

// DANGEROUS — if userInput contains <script>...</script>, it executes
elem.innerHTML = userInput;
```

The simple rule: **use `textContent`** for data coming from the user. Use `innerHTML` only for static HTML, controlled by you.

---

## Exercises

### Exercise 1 — Change a title
Select the `<h1>` from the page and change its text to "Hello from JS!".

??? success "Solution"
    ```html
    <h1>Original title</h1>
    <script src="app.js" defer></script>
    ```

    ```js
    const title = document.querySelector("h1");
    title.textContent = "Hello from JS!";
    ```

### Exercise 2 — Color the paragraphs
Select all `<p>` from the page and make them green.

??? success "Solution"
    ```js
    const paragraphs = document.querySelectorAll("p");
    paragraphs.forEach((p) => {
      p.style.color = "green";
    });
    ```

    **Cleaner — with a CSS class:**

    ```css
    .green { color: green; }
    ```

    ```js
    document.querySelectorAll("p").forEach(p => p.classList.add("green"));
    ```

### Exercise 3 — Add to a list
Given `<ul id="fruits"></ul>`, dynamically add three `<li>` with "apple", "pear", "banana".

??? success "Solution"
    ```js
    const list = document.getElementById("fruits");
    const fruits = ["apple", "pear", "banana"];

    for (const fruit of fruits) {
      const li = document.createElement("li");
      li.textContent = fruit;
      list.appendChild(li);
    }
    ```

### Exercise 4 — Delete the second paragraph
The page has multiple `<p>`. Delete the second one.

??? success "Solution"
    ```js
    const paragraphs = document.querySelectorAll("p");
    if (paragraphs.length >= 2) {
      paragraphs[1].remove();   // index 1 = the second
    }
    ```

---

## Mini-project: Add to a list

The page has an `<input>`, an "Add" button and an empty `<ul>`. When the user types something and presses the button, a new `<li>` appears in the list.

!!! note "Preview for the next lesson"
    We'll use `addEventListener` — leave it for lesson 16. For now, understand that `btn.addEventListener("click", () => { ... })` runs the function on every click.

**Complete code:**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Add to list</title>
    <script src="app.js" defer></script>
    <style>
      body { font-family: sans-serif; padding: 2rem; }
      #fruits-list li { padding: 0.25rem 0; }
    </style>
  </head>
  <body>
    <h1>Favorite fruits</h1>

    <input id="new-fruit" type="text" placeholder="Type a fruit..." />
    <button id="btn-add">Add</button>

    <ul id="fruits-list"></ul>
  </body>
</html>
```

```js
// Select the elements once
const input = document.getElementById("new-fruit");
const button = document.getElementById("btn-add");
const list = document.getElementById("fruits-list");

// On every click of the button, add a new <li>
button.addEventListener("click", () => {
  const text = input.value.trim();
  if (!text) return;   // ignore empty input

  const li = document.createElement("li");
  li.textContent = text;
  list.appendChild(li);

  input.value = "";    // clear the input
  input.focus();       // return to the input for the next entry
});
```

---

## Summary

- The **DOM** is the object tree of the HTML, accessible from JS.
- Select with **`querySelector`** (first) / **`querySelectorAll`** (all) — accepts any CSS selector.
- Read / write the text with **`textContent`** (safe) or **`innerHTML`** (watch out for XSS).
- For inputs: **`.value`**.
- Modify the style via `classList.add/remove/toggle` (preferred) or `.style.*` directly.
- Create elements with `createElement`, then attach with `appendChild` / `append`.
- Remove with `elem.remove()`.

---

**Next step:** [→ Lesson 16: Events](16-js-evenimente.md)
