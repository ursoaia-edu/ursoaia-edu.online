---
lesson: 12
tags: [javascript, variables, types, string, number, boolean, template-literals]
summary: Variables with let and const, primitive types, template literals and useful methods for string and number.
---

# Lesson 12 · Variables and data types

!!! tip "What you'll learn"
    - The difference between `let`, `const` and `var`
    - The primitive types: number, string, boolean, null, undefined
    - How to use **template literals** (strings with backticks)
    - Arithmetic operators and the pitfalls with strings
    - Useful methods for string and number

---

## Declaring variables

In modern JavaScript we use **`let`** and **`const`** to declare variables:

```js
let name = "Ana";       // value that can change
const PI = 3.14;        // fixed value (cannot be reassigned)

name = "Maria";         // OK
// PI = 3.14159;        // Error! "Assignment to constant variable"
```

**The golden rule:** prefer `const`. Use `let` only when you know the value will change.

```js
const maxAttempts = 3;          // constant
let attempts = 0;                // counter — grows over time
attempts = attempts + 1;
```

### What is `var`?

`var` is the **old** variant, from before 2015. It has weird scope rules (we'll see in the functions lesson). **Don't use it in new code** — use `let` / `const`.

### Naming conventions

| Style | When to use | Example |
|------|-------------------|---------|
| `camelCase` | variables and functions | `studentName`, `calculateAverage` |
| `PascalCase` | classes and components | `User`, `ProductCard` |
| `UPPER_SNAKE` | "system" constants | `MAX_SCORE`, `API_URL` |

### Naming rules

- Can start with a letter, `_` or `$`.
- Can contain digits, but **not at the beginning**.
- **Are case-sensitive:** `name` and `Name` are different variables.
- You can't use reserved words: `let`, `const`, `if`, `function`, `class`, etc.

---

## Primitive types

JavaScript has a few basic types called **primitives**:

```js
const age = 14;                 // Number
const price = 3.14;             // Number (no separate type for float)
const name = "Ana";             // String
const isAdult = false;          // Boolean
const nothing = null;           // null — "intentionally empty"
let uninitialized;              // undefined — "no value given"
```

### `null` vs `undefined`

- **`undefined`** — the value of a variable **declared but without a value**.
- **`null`** — the value you set **intentionally** when you want to say "no object".

```js
let x;                  // undefined (no value given)
let y = null;           // null (I said: it's empty)
```

---

## Template literals

The most elegant way to build strings in modern JS: **backticks** `` ` ``.

```js
const name = "Mihai";
const age = 14;

// Old way — concatenation with +
const oldWay = "Hello, " + name + "! You are " + age + " years old.";

// Modern way — template literal
const newWay = `Hello, ${name}! You are ${age} years old.`;
```

Advantages:

- `${expression}` interpolates any JS expression.
- Works on **multiple lines** without `\n`:

```js
const message = `Line 1
Line 2
Line 3`;
```

!!! tip "When do you use backticks?"
    Almost always in modern JS. Even if you don't have interpolation, it's readable and flexible.

---

## Arithmetic operators

```js
const a = 10;
const b = 3;

console.log(a + b);    // 13
console.log(a - b);    // 7
console.log(a * b);    // 30
console.log(a / b);    // 3.3333...
console.log(a % b);    // 1 — remainder of division (modulo)
console.log(a ** b);   // 1000 — exponentiation (10³)
```

### The pitfall with strings

`+` has two meanings in JS:

```js
console.log(2 + 2);        // 4   — numeric addition
console.log("2" + 2);      // "22" — string concatenation!
console.log("2" + "2");    // "22"
```

But the operators `-`, `*`, `/` automatically convert string to number:

```js
console.log("10" - 2);     // 8
console.log("5" * "3");    // 15
```

!!! warning "Implicit conversion is a classic source of bugs"
    If you read a number from an HTML input, it comes as a **string**. Convert it explicitly before calculations (see below).

---

## Useful methods for string

```js
const text = "  Hello, Ana!  ";

text.length              // 16 — number of characters (with spaces)
text.toUpperCase()       // "  HELLO, ANA!  "
text.toLowerCase()       // "  hello, ana!  "
text.trim()              // "Hello, Ana!" — removes leading/trailing spaces
text.includes("Ana")     // true
text.slice(2, 7)         // "Hello" — substring from index 2 to 7 (exclusive)
text.replace("Ana", "Maria")  // "  Hello, Maria!  "
text.split(",")          // ["  Hello", " Ana!  "] — splits by comma
```

The methods **do not modify** the original string (strings are immutable) — they return a new one.

---

## Useful methods for number

```js
const price = 19.9876;

price.toFixed(2);           // "19.99" — round to 2 decimals (WARNING: returns string!)

Number.parseInt("42");      // 42
Number.parseFloat("3.14");  // 3.14
Number("3.14");             // 3.14 — direct conversion

Math.round(3.6);     // 4
Math.floor(3.9);     // 3
Math.ceil(3.1);      // 4
Math.abs(-5);        // 5
Math.max(2, 9, 4);   // 9
Math.min(2, 9, 4);   // 2
Math.random();       // 0.7231... — random number in [0, 1)
```

### Conversion string → number

When you read from an input:

```js
const ageText = "14";                   // came as string
const age = Number(ageText);             // 14 as number
const total = age + 1;                   // 15 (correct!)
```

---

## The `typeof` operator

Find the type of a value:

```js
typeof 42          // "number"
typeof "ana"       // "string"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object" — historic bug in JS!
typeof [1, 2, 3]   // "object"
typeof { a: 1 }    // "object"
```

!!! note "`typeof null` is `\"object\"`"
    It's an old bug in JavaScript that can no longer be fixed without breaking the internet. Remember it's an exception.

---

## Arrays — briefly

An **array** stores an ordered list of values. Details in the next lessons; for now:

```js
const colors = ["red", "green", "blue"];

console.log(colors[0]);       // "red"
console.log(colors.length);   // 3

colors.push("yellow");        // adds at the end
console.log(colors);           // ["red", "green", "blue", "yellow"]

const last = colors.pop();    // removes the last element
console.log(last);             // "yellow"
```

---

## Objects — briefly

An **object** stores key-value pairs:

```js
const person = {
  name: "Ana",
  age: 14,
  grade: "8A"
};

console.log(person.name);     // "Ana"
console.log(person["age"]);   // 14
```

We'll come back in detail.

---

## Exercises

### Exercise 1 — Personal introduction
Create the variables `name`, `age` and `student` (boolean). Display them with a template literal.

??? success "Solution"
    ```js
    const name = "Mihai";
    const age = 14;
    const student = true;

    console.log(`My name is ${name}, I'm ${age} years old, student: ${student}.`);
    // My name is Mihai, I'm 14 years old, student: true.
    ```

### Exercise 2 — Cleaning a string
Starting from `"  Ana Pop  "`, get the version without leading/trailing spaces and in uppercase.

??? success "Solution"
    ```js
    const original = "  Ana Pop  ";
    const cleaned = original.trim().toUpperCase();
    console.log(cleaned);   // "ANA POP"
    ```

    You can chain methods: `trim()` returns a string, on which you then call `toUpperCase()`.

### Exercise 3 — Convert and add
Convert the string `"42"` to a number and add `8` to it. Display the result.

??? success "Solution"
    ```js
    const text = "42";
    const number = Number(text);     // or Number.parseInt(text)
    const result = number + 8;
    console.log(result);              // 50
    ```

    If you forget the conversion: `"42" + 8` → `"428"` (concatenation). Classic!

### Exercise 4 — Check types
What does each of these `console.log` show?

```js
console.log(typeof "14");
console.log(typeof 14);
console.log(typeof (14 > 10));
console.log(typeof undefined);
```

??? success "Solution"
    ```text
    "string"
    "number"
    "boolean"   — comparison returns true/false
    "undefined"
    ```

---

## Mini-project: Area calculator

Write a program that calculates the area of a rectangle and displays the result nicely.

**Requirement:**

- Define `length` and `width` with `let` / `const`.
- Calculate the area.
- Display with a template literal: `"The area of the 5x3 rectangle is 15 m²"`.

??? success "Solution"
    ```js
    const length = 5;
    const width = 3;
    const area = length * width;

    console.log(`The area of the ${length}x${width} rectangle is ${area} m².`);
    // The area of the 5x3 rectangle is 15 m².
    ```

    **Bonus:** ask the user for the values with `prompt()` and convert them with `Number()`.

    ```js
    const length = Number(prompt("Length:"));
    const width = Number(prompt("Width:"));
    const area = length * width;

    alert(`The area is ${area} m².`);
    ```

---

## Summary

- Prefer **`const`**; use **`let`** only when you reassign; **don't use `var`**.
- Primitive types: `number`, `string`, `boolean`, `null`, `undefined`.
- Template literals with `` ` `` and `${}` are the modern way to build strings.
- `"2" + 2` is `"22"` (concatenation) — be careful with implicit conversions.
- `Number(x)`, `Number.parseInt(x)`, `Number.parseFloat(x)` convert string to number.
- `typeof` tells you the type of a value.

---

**Next step:** [→ Lesson 13: Conditions and loops](13-js-conditii-bucle.md)
