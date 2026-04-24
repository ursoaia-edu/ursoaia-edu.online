---
lesson: 11
tags: [javascript, introduction, console, devtools, script]
summary: First steps in JavaScript — how to include scripts in a page and how to use DevTools.
---

# Lesson 11 · JavaScript: introduction

!!! tip "What you'll learn"
    - What JavaScript is and where it runs
    - The three ways to include JS in an HTML page
    - How to use `console.log()` and the DevTools Console
    - Basic functions: `alert`, `prompt`, `confirm`
    - How to read errors from the console

---

## What is JavaScript?

**JavaScript** (JS) is the language that **brings web pages to life**. If HTML is the "skeleton" and CSS is the "skin", JS is the "muscle" — it makes pages react to clicks, validate forms, load data from the network and update without reloading.

It was created in **1995** by Brendan Eich (at Netscape) in just **10 days**. The name "JavaScript" is pure marketing — it has **NO connection to the Java language**. It's like comparing "ham" with "hamster".

Today, JS runs on **almost every modern browser** and is one of the most popular languages in the world.

---

## Where does JavaScript run?

JS can run in two main places:

- **In the browser (client-side)** — what we are learning here. The code runs on the visitor's computer.
- **On the server (Node.js)** — we'll discuss later. The code runs on a server.

In this section of the guide we focus on JS in the browser.

---

## Three ways to include JS

### 1. Inline, in an HTML attribute (AVOID)

```html
<button onclick="alert('hello')">Click me</button>
```

It works, but it mixes logic with structure and becomes impossible to maintain for large pages. **Don't use this style** in real projects.

### 2. In HTML, with a `<script>` tag

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Hello!</h1>
    <script>
      console.log("Hello from inline script!");
    </script>
  </body>
</html>
```

Useful for quick tests, but the code mixes with the HTML.

### 3. External JS file (RECOMMENDED)

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>My first page with JS</title>
    <script src="app.js" defer></script>
  </head>
  <body>
    <h1>Hello!</h1>
  </body>
</html>
```

And the `app.js` file:

```js
// My first JavaScript code
console.log("Hello, world!");
```

!!! tip "What does `defer` do?"
    Without `defer`, the browser downloads and runs the script **immediately**, stopping HTML parsing. With `defer`, the browser **waits** to finish parsing the HTML, then runs the script. Result: the page loads faster and the script finds all elements already created.

---

## Where do you put `<script>`?

There are two good places:

- **In `<head>` with `defer`** — clean, recommended.
- **At the end of `<body>`** — classic alternative (without `defer`), still works because the HTML above is already parsed.

```html
<!-- Option 1: in head with defer -->
<head>
  <script src="app.js" defer></script>
</head>

<!-- Option 2: at the end of body -->
<body>
  <!-- ... content ... -->
  <script src="app.js"></script>
</body>
```

---

## Your first JS code

The simplest instruction: print to the console.

```js
console.log("Hello, world!");
console.log("I learned JavaScript!");
```

`console.log(...)` does not appear on the page — it appears in the **DevTools Console**.

---

## DevTools Console

Every modern browser has a set of tools for developers called **DevTools**. You open them with:

- **F12** (on most browsers)
- **Ctrl + Shift + I** (Windows / Linux)
- **Cmd + Option + I** (macOS)
- Right-click on the page → **Inspect**

Then click the **Console** tab.

In the Console:

- You see everything you wrote with `console.log(...)`.
- You can type **JS commands directly** and press Enter.

Try typing these commands in the Console:

```js
2 + 2                    // 4
"Ana".toUpperCase()      // "ANA"
Math.random()            // a random number between 0 and 1
new Date()               // current date and time
```

---

## Other useful functions

### `alert()` — informative popup

```js
alert("Good day!");
```

Opens a popup window with a message. Useful for quick debugging, **annoying for the user** — avoid it in real applications.

### `prompt()` — ask for input

```js
const name = prompt("What's your name?");
console.log("Hello,", name);
```

Returns a **string** (or `null` if the user presses Cancel).

### `confirm()` — ask yes / no

```js
const sure = confirm("Are you sure you want to continue?");
console.log(sure);   // true or false
```

### `console` variants

```js
console.log("normal message");
console.warn("yellow warning");
console.error("red error");
console.info("info");
```

Each appears with a different color / icon in the Console.

---

## Reading errors

When something goes wrong, the Console shows you the **error type** and the **line** where it appeared:

```text
Uncaught ReferenceError: conzole is not defined
    at app.js:3
```

Common types:

- **`ReferenceError`** — you used a name that doesn't exist (e.g. `conzole` instead of `console`).
- **`TypeError`** — you tried an operation not allowed on a type (e.g. `null.length`).
- **`SyntaxError`** — you wrote code that doesn't follow JS grammar (missing parenthesis, unclosed quote).

!!! warning "Read the error message!"
    Many beginners ignore the message and look directly at the code. The message tells you **where** and **what** broke — it's the first place you should look.

---

## Comments in JS

```js
// This is a single-line comment

/*
   This is a comment
   on multiple lines.
*/

const pi = 3.14;   // you can also put it at the end of a line
```

Comments are not executed — they are just for you and for the colleagues who read the code.

---

## Exercises

### Exercise 1 — First page with JS
Create a new folder with two files: `index.html` and `app.js`. Link them correctly and print `"it works!"` to the Console.

??? success "Solution"
    `index.html`:

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <title>JS Test</title>
        <script src="app.js" defer></script>
      </head>
      <body>
        <h1>Check the Console!</h1>
      </body>
    </html>
    ```

    `app.js`:

    ```js
    console.log("it works!");
    ```

    Open `index.html` in the browser, press F12 → Console and you should see `it works!`.

### Exercise 2 — Console experiments
Open the Console on any page and type:

1. `5 + 5 * 2`
2. `"hello".length`
3. `prompt("Your age?")`

What do you notice?

??? success "Solution"
    ```js
    5 + 5 * 2             // 15 — multiplication has priority
    "hello".length        // 5 — number of characters
    prompt("Your age?")   // opens popup, returns string (e.g. "14")
    ```

### Exercise 3 — Force an error
In `app.js`, intentionally write an incorrect line: `conzole.log("test")`. Reload the page and read the message in the Console.

??? success "Solution"
    You'll see something like:

    ```text
    Uncaught ReferenceError: conzole is not defined
        at app.js:1
    ```

    The browser tells you the exact line (`app.js:1`) and the reason (`conzole` doesn't exist). Fix to `console` and the error disappears.

---

## Mini-project: Greeting banner

The page asks for the visitor's name on load and shows a personalized alert.

**Requirement:**

- Use `prompt()` to ask for the name.
- Use `alert()` to show a personalized greeting.
- Log the entered name to the console.

??? success "Solution"
    `index.html`:

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <title>Greeting banner</title>
        <script src="app.js" defer></script>
      </head>
      <body>
        <h1>Welcome to the site!</h1>
      </body>
    </html>
    ```

    `app.js`:

    ```js
    // Ask for the visitor's name
    const name = prompt("What's your name?");

    // Log to the console for debug
    console.log("Name entered:", name);

    // Show a personalized greeting
    alert("Hello, " + name + "! Glad to see you.");
    ```

---

## Summary

- JavaScript runs in the browser and makes pages interactive.
- Include scripts with `<script src="app.js" defer></script>` in `<head>`.
- `console.log(...)` shows messages in the **DevTools Console** (F12).
- `alert`, `prompt`, `confirm` are simple popups — useful for debug, not for real UI.
- Read the **type** and the **line** of the error — they are the best guide when something fails.
- `//` and `/* */` are comments, ignored by the browser.

---

**Next step:** [→ Lesson 12: Variables and data types](12-js-variabile-tipuri.md)
