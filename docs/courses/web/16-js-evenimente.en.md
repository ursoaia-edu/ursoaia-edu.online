---
lesson: 16
tags: [javascript, events, addEventListener, click, submit, dom]
summary: Respond to user actions with addEventListener — click, submit, input, keydown.
---

# Lesson 16 · Events

!!! tip "What you'll learn"
    - What events are and three ways to listen for them
    - Why `addEventListener` is the modern choice
    - Common events: `click`, `submit`, `input`, `change`, `keydown`
    - The `event` object: `e.target`, `e.preventDefault`, `e.stopPropagation`
    - Event bubbling and delegation (briefly)

---

## What are events?

An **event** is something that happens in the browser: a click, a key pressed, a form submitted, a page loaded. JavaScript can **listen** for these events and run code in response.

Examples of events you'll often use:

- **`click`** — the user presses a button or a link.
- **`submit`** — a `<form>` is submitted.
- **`input`** — the text in an `<input>` has changed.
- **`change`** — the value of a `<select>` or a checkbox has changed.
- **`keydown`** — a key was pressed.
- **`DOMContentLoaded`** — the HTML is parsed and the DOM is ready.

---

## Three ways (from old to new)

### 1. Inline in HTML (AVOID)

```html
<button onclick="alert('hello')">Click</button>
```

Mixes logic with structure. **Don't use.**

### 2. `on<event>` property

```js
const btn = document.querySelector("button");
btn.onclick = () => alert("hello");
```

Limited to **one single handler** — if you set it twice, the second overwrites it.

### 3. `addEventListener` (RECOMMENDED)

```js
const btn = document.querySelector("button");
btn.addEventListener("click", () => {
  alert("hello");
});
```

Advantages:

- You can add **multiple** handlers for the same event.
- You can specify options (`once`, `passive`, `capture`).
- Easy to remove with `removeEventListener`.

---

## `addEventListener`

Signature:

```js
elem.addEventListener(eventType, handler, options);
```

- **`eventType`** — a string: `"click"`, `"submit"`, `"keydown"`, etc. (without "on").
- **`handler`** — the function that runs on the event.
- **`options`** — optional, object: `{ once: true }`, `{ passive: true }`, `{ capture: true }`.

Examples:

```js
const btn = document.querySelector("#hello-btn");

btn.addEventListener("click", () => {
  console.log("You clicked!");
});

// Handler that runs only once
btn.addEventListener("click", () => alert("only once"), { once: true });
```

---

## Common events

### `click` and `dblclick`

```js
btn.addEventListener("click", () => console.log("simple click"));
btn.addEventListener("dblclick", () => console.log("double click"));
```

### `input` — on every keystroke

```js
const search = document.querySelector("#search");
search.addEventListener("input", (e) => {
  console.log("The user typed:", e.target.value);
});
```

### `change` — when a select / checkbox changes

```js
const option = document.querySelector("#option");
option.addEventListener("change", (e) => {
  console.log("New value:", e.target.value);
});
```

### `submit` — when a form is submitted

```js
const form = document.querySelector("#form");
form.addEventListener("submit", (e) => {
  e.preventDefault();   // stop the page reload
  console.log("Form submitted!");
});
```

### `keydown`, `keyup`, `keypress`

```js
document.addEventListener("keydown", (e) => {
  console.log(`You pressed the key: ${e.key}`);
});
```

`e.key` is the key string: `"a"`, `"Enter"`, `"ArrowUp"`, `" "` (space), etc.

### `mouseenter` / `mouseleave`

```js
const card = document.querySelector(".card");
card.addEventListener("mouseenter", () => card.classList.add("hover"));
card.addEventListener("mouseleave", () => card.classList.remove("hover"));
```

### `load` / `DOMContentLoaded`

```js
// HTML is parsed (without waiting for large images)
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM ready!");
});

// Everything is loaded: HTML + CSS + images + scripts
window.addEventListener("load", () => {
  console.log("Everything is ready!");
});
```

If you use `<script defer>`, the script runs automatically after the DOM is parsed — so usually you don't need `DOMContentLoaded` anymore.

---

## The `event` object

The handler automatically receives an `event` object (usually called `e` or `event`):

```js
btn.addEventListener("click", (e) => {
  console.log(e.type);      // "click"
  console.log(e.target);    // the element it was triggered on
  console.log(e.clientX, e.clientY);  // mouse coordinates
});
```

The most useful properties / methods:

| Property / method | What it does |
|----------------------|---------|
| `e.target` | the element on which the event was **triggered** |
| `e.currentTarget` | the element you **attached the listener** to |
| `e.type` | the event type (`"click"`, etc.) |
| `e.preventDefault()` | stops the default behavior |
| `e.stopPropagation()` | stops propagation toward parents |
| `e.key` | the pressed key (for keydown) |

---

## `preventDefault()`

Some elements have **default** behavior:

- An `<a href>` navigates when clicked.
- A `<form>` reloads the page when submitted.
- `Space` on the page scrolls it.

To stop it:

```js
const link = document.querySelector("a");
link.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("I stopped the navigation.");
});

const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault();   // process in JS, don't reload
  // ... validate, send with fetch, etc.
});
```

---

## Event bubbling

When you click on an element, the event **bubbles** up through parents to `document`:

```html
<div id="outer">
  <button id="button">Click</button>
</div>
```

```js
document.getElementById("outer").addEventListener("click", () => {
  console.log("outer div");
});

document.getElementById("button").addEventListener("click", () => {
  console.log("button");
});
```

A click on the button shows:

```text
button
outer div
```

The event "bubbled up" from the button to the div.

### `stopPropagation`

If you don't want propagation:

```js
document.getElementById("button").addEventListener("click", (e) => {
  e.stopPropagation();
  console.log("Button only.");
});
```

### Event delegation (briefly)

Bubbling allows an elegant trick: you attach a listener on **a parent** and use `e.target` to know what was clicked. Useful for **dynamic children** (created after you started):

```js
document.querySelector("#list").addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    e.target.classList.toggle("selected");
  }
});
```

You no longer have to put a listener on each newly created `<li>`.

---

## Removing a listener — `removeEventListener`

To be able to remove a listener, you need to have the **reference** to the function (so not anonymous):

```js
function handler() {
  console.log("once");
}

btn.addEventListener("click", handler);
btn.removeEventListener("click", handler);
```

If you only need it to run once, use the `once` option:

```js
btn.addEventListener("click", () => alert("only once"), { once: true });
```

---

## Exercises

### Exercise 1 — Alert on click
A button that on click shows an alert with "Hello!".

??? success "Solution"
    ```html
    <button id="btn-hello">Click me</button>
    ```

    ```js
    const btn = document.getElementById("btn-hello");
    btn.addEventListener("click", () => {
      alert("Hello!");
    });
    ```

### Exercise 2 — Log on typing
An `<input>` that logs the current value on every keystroke.

??? success "Solution"
    ```html
    <input id="text" placeholder="Type something..." />
    ```

    ```js
    const input = document.getElementById("text");
    input.addEventListener("input", (e) => {
      console.log("You typed:", e.target.value);
    });
    ```

### Exercise 3 — Change the background color
A button that on each click changes the background color of the page (random).

??? success "Solution"
    ```html
    <button id="change">Change color</button>
    ```

    ```js
    const btn = document.getElementById("change");

    const randomColor = () => {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      return `rgb(${r}, ${g}, ${b})`;
    };

    btn.addEventListener("click", () => {
      document.body.style.backgroundColor = randomColor();
    });
    ```

### Exercise 4 — Show the pressed key
The page shows on screen which key was last pressed.

??? success "Solution"
    ```html
    <p>Last key: <span id="key">—</span></p>
    ```

    ```js
    const span = document.getElementById("key");
    document.addEventListener("keydown", (e) => {
      span.textContent = e.key;
    });
    ```

---

## Mini-project: Click counter

A button that counts how many clicks it received and shows the result. Plus a "Reset" button that sets the counter to zero.

**Complete code:**

```html
<!DOCTYPE html>
<html lang="en">
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
      #score {
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
    <p>Score: <span id="score">0</span></p>
    <button id="btn-click">Click me!</button>
    <button id="btn-reset">Reset</button>
  </body>
</html>
```

```js
// Select the elements
const score = document.getElementById("score");
const btnClick = document.getElementById("btn-click");
const btnReset = document.getElementById("btn-reset");

let counter = 0;

// Increment on click
btnClick.addEventListener("click", () => {
  counter++;
  score.textContent = counter;
});

// Reset
btnReset.addEventListener("click", () => {
  counter = 0;
  score.textContent = counter;
});
```

**Ideas to extend:**

- Save the score in `localStorage` so it persists after reload.
- Change the score color past a threshold (100 = gold, 500 = rainbow).
- Add a second button with a negative value ("decrease").

---

## Summary

- **Events** are user actions (click, typing, submit) that JS can react to.
- Use **`addEventListener(type, handler)`** — supports multiple handlers and options.
- The handler receives an `event` object with `target`, `type`, `key`, etc.
- **`e.preventDefault()`** stops the default behavior (navigation, form reload).
- **Event bubbling:** the event bubbles up through parents. **Delegation:** listen on the parent for dynamic children.
- To run once, use `{ once: true }` in options.

---

**Next step:** [→ Lesson 17: Forms with JS validation](17-js-formulare-validare.md)
