---
lesson: 14
tags: [javascript, functions, arrow, callback, scope, parameters]
summary: Function declarations, function expressions and arrow functions — the building block of reusable code.
---

# Lesson 14 · Functions

!!! tip "What you'll learn"
    - Why we need functions (avoiding repetition, organization)
    - Three ways to define a function: declaration, expression, arrow
    - Default parameters, rest parameters
    - `return` and multiple returns
    - What **scope** is: global, function, block
    - What **callbacks** are (preview for DOM events)

---

## Why functions?

A **function** is a block of code that you can **reuse** by giving it a name. You call it wherever you need, with different data.

Without functions:

```js
// Calculate the area for three rectangles — repetitive code
const area1 = 5 * 3;
console.log(`Rectangle 1: ${area1}`);

const area2 = 10 * 4;
console.log(`Rectangle 2: ${area2}`);

const area3 = 7 * 2;
console.log(`Rectangle 3: ${area3}`);
```

With functions:

```js
function area(length, width) {
  return length * width;
}

console.log(`Rectangle 1: ${area(5, 3)}`);
console.log(`Rectangle 2: ${area(10, 4)}`);
console.log(`Rectangle 3: ${area(7, 2)}`);
```

You gain: **less code, fewer mistakes, easy to modify**.

---

## Function declaration

The "classic" style:

```js
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet("Ana"));    // "Hello, Ana!"
console.log(greet("Mihai"));  // "Hello, Mihai!"
```

Parts:

- `function` — keyword.
- `greet` — function name.
- `(name)` — parameter list.
- `{ ... }` — function body.
- `return` — what the function "returns" (sends back).

---

## Function expression

A function can be **stored in a variable**:

```js
const greet = function(name) {
  return `Hello, ${name}!`;
};

console.log(greet("Ana"));
```

Notice:

- The function has no name after `function` (it's called **anonymous**).
- The line ends with `;` (because it's an expression assigned to a variable).

---

## Arrow function

The **modern** and **compact** form, introduced in ES6:

```js
// Long version
const greet = (name) => {
  return `Hello, ${name}!`;
};

// Short version (implicit return)
const greet = (name) => `Hello, ${name}!`;

// One parameter — parentheses are optional
const greet = name => `Hello, ${name}!`;

// No parameters — parentheses are required
const time = () => new Date().toLocaleTimeString();

// Two or more parameters
const sum = (a, b) => a + b;
```

Rules:

- Single parameter: `()` optional.
- Body of a single expression: `{}` and `return` optional (implicit return).
- Body with multiple lines: `{}` and explicit `return` required.

---

## Arrow vs regular — which to choose?

| Aspect | Traditional `function` | Arrow `=>` |
|--------|------------------------|------------|
| Syntax | more verbose | more compact |
| Own `this` | YES | NO (inherited from parent context) |
| Hoisting | YES (you can call before definition) | NO |
| Useful for | object methods, long functions | callbacks, short functions |

!!! note "About `this`"
    `this` in an arrow is inherited from the parent context. This is often **what you want** when writing callbacks for events and for array methods (`.map`, `.filter`). Details in depth when we get to objects and classes.

For now: use **arrow** for callbacks and short functions, **function declaration** for long top-level functions.

---

## Parameters

### Multiple

```js
const sum = (a, b, c) => a + b + c;
console.log(sum(1, 2, 3));   // 6
```

### Default values

If you call without an argument, the parameter takes the default value:

```js
const greet = (name = "friend") => `Hello, ${name}!`;

console.log(greet());         // "Hello, friend!"
console.log(greet("Ana"));    // "Hello, Ana!"
```

### Rest parameters

For a **variable** number of arguments:

```js
const sum = (...numbers) => {
  let total = 0;
  for (const n of numbers) {
    total += n;
  }
  return total;
};

console.log(sum(1, 2, 3));         // 6
console.log(sum(5, 10, 15, 20));   // 50
```

`...numbers` gathers all arguments into an array called `numbers`.

---

## `return`

- Without `return`, the function returns `undefined`.
- `return` stops the function execution immediately.

```js
const test = () => {
  console.log("before");
  return;
  console.log("after");   // never executes
};
```

### Early exit

Return early to avoid deep nesting:

```js
// HARD to read
const checkAge = (a) => {
  if (a >= 0) {
    if (a >= 18) {
      return "adult";
    } else {
      return "minor";
    }
  } else {
    return "invalid value";
  }
};

// CLEAN with early return
const checkAge = (a) => {
  if (a < 0) return "invalid value";
  if (a >= 18) return "adult";
  return "minor";
};
```

---

## Scope (visibility domain)

**Scope** = where a variable is **visible**.

### Global scope

Declared outside any function — accessible from anywhere:

```js
const siteName = "Computer Science Club";

function show() {
  console.log(siteName);   // OK, sees it
}
```

### Function scope

Declared **inside** a function — accessible only in the function:

```js
function compute() {
  const secret = 42;
  console.log(secret);   // OK
}

compute();
console.log(secret);   // ReferenceError!
```

### Block scope (`let` / `const`)

`let` and `const` are **block-scoped** — limited to the nearest pair of `{}`:

```js
if (true) {
  const x = 10;
  console.log(x);   // 10
}

console.log(x);   // ReferenceError!
```

!!! warning "`var` is function-scoped, not block-scoped"
    This means a `var` declared inside an `if` is accessible outside of it — exactly the opposite of what you'd expect. Another reason to use `let`/`const`.

---

## Callback functions

A **callback** is a function that you **pass** to another function as an argument, to be called later:

```js
const withDelay = (callback) => {
  setTimeout(callback, 1000);   // run callback after 1 second
};

withDelay(() => console.log("A second has passed!"));
```

Callbacks are everywhere in JS — you'll use them heavily for events (lesson 16) and for fetch (lesson 18).

---

## Exercises

### Exercise 1 — The `square` function
Write a function `square(n)` that returns `n²`.

??? success "Solution"
    ```js
    function square(n) {
      return n * n;
    }

    console.log(square(5));   // 25

    // Or as an arrow:
    const square = (n) => n * n;
    ```

### Exercise 2 — Greet with default
Write `greet(name = "friend")` that prints `"Hello, <name>!"`.

??? success "Solution"
    ```js
    const greet = (name = "friend") => `Hello, ${name}!`;

    console.log(greet());         // "Hello, friend!"
    console.log(greet("Maria"));  // "Hello, Maria!"
    ```

### Exercise 3 — Largest of three
The function `largest(a, b, c)` returns the largest of three numbers.

??? success "Solution"
    ```js
    const largest = (a, b, c) => {
      if (a >= b && a >= c) return a;
      if (b >= c) return b;
      return c;
    };

    console.log(largest(3, 9, 5));   // 9

    // Or very short:
    const largest2 = (a, b, c) => Math.max(a, b, c);
    ```

### Exercise 4 — Rewrite as arrow
Rewrite `square` and `greet` above using **arrow functions**, in the shortest possible forms.

??? success "Solution"
    ```js
    const square = n => n * n;
    const greet = (name = "friend") => `Hello, ${name}!`;
    ```

    For `square`, a single parameter → no parentheses. A single expression → no `{}` and no `return`.

---

## Mini-project: Temperature converter

Write two functions that convert temperatures between Celsius and Fahrenheit.

**Formulas:**

- Celsius → Fahrenheit: `F = C * 9/5 + 32`
- Fahrenheit → Celsius: `C = (F - 32) * 5/9`

**Requirements:**

- Two functions: `celsiusToFahrenheit(c)` and `fahrenheitToCelsius(f)`.
- Call them with a few values.
- Display with a template literal: `"0 °C = 32 °F"`.

??? success "Solution"
    ```js
    // Conversion formulas
    const celsiusToFahrenheit = (c) => c * 9 / 5 + 32;
    const fahrenheitToCelsius = (f) => (f - 32) * 5 / 9;

    // A few tests
    console.log(`0 °C = ${celsiusToFahrenheit(0)} °F`);      // 0 °C = 32 °F
    console.log(`100 °C = ${celsiusToFahrenheit(100)} °F`);  // 100 °C = 212 °F
    console.log(`32 °F = ${fahrenheitToCelsius(32)} °C`);    // 32 °F = 0 °C
    console.log(`212 °F = ${fahrenheitToCelsius(212)} °C`);  // 212 °F = 100 °C
    ```

    **Bonus:** ask the user for the temperature:

    ```js
    const c = Number(prompt("Temperature in °C:"));
    const f = celsiusToFahrenheit(c);
    alert(`${c} °C = ${f.toFixed(1)} °F`);
    ```

---

## Summary

- Functions let you **reuse code** with different inputs.
- Three forms: **declaration** (`function name() {}`), **expression** (`const f = function() {}`), **arrow** (`const f = () => {}`).
- Arrow is compact and preferred for short callbacks.
- Parameters can have **default values** and **rest** (`...`).
- `return` stops the function and sends a value back. Use **early return** to avoid nesting.
- The `let`/`const` **scope** is block-scoped (`{}`), `var` is function-scoped (avoid it).
- **Callbacks** are functions passed as arguments — you'll use them a lot for events.

---

**Next step:** [→ Lesson 15: DOM — HTML manipulation](15-js-dom.md)
