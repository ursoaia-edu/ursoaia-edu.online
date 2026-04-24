---
lesson: 13
tags: [javascript, conditions, if, else, for, while, loops, operators]
summary: Control your program's flow with if/else, switch and for/while loops.
---

# Lesson 13 · Conditions and loops

!!! tip "What you'll learn"
    - How to make decisions with `if / else if / else`
    - The difference between `==` and `===` (spoiler: use `===`)
    - Logical operators `&&`, `||`, `!` and the ternary operator
    - The `for`, `while`, `do...while`, `for...of` loops
    - How to control execution with `break` and `continue`

---

## `if / else if / else`

The simplest decision:

```js
const age = 16;

if (age >= 18) {
  console.log("Can vote.");
} else if (age >= 16) {
  console.log("Can get a category AM license.");
} else {
  console.log("Still too young for a license.");
}
```

Structure:

- `if (condition) { ... }` — if `condition` is `true`, run the block.
- `else if (otherCondition) { ... }` — checked only if the previous one is `false`.
- `else { ... }` — runs if nothing above matched.

The braces are optional for a single line, but **always put them** — it's safer and clearer.

---

## Comparison operators

| Operator | Meaning | Example | Result |
|----------|--------------|---------|----------|
| `===` | strictly equal | `5 === 5` | `true` |
| `!==` | strictly different | `"5" !== 5` | `true` |
| `==` | equal with coercion | `"5" == 5` | `true` |
| `!=` | different with coercion | `"5" != 5` | `false` |
| `<`, `>`, `<=`, `>=` | numeric comparison | `3 < 5` | `true` |

### `==` vs `===` — the classic pitfall

`==` does **type coercion** before comparing — tries to make the values "compatible":

```js
console.log("2" == 2);      // true  — string is converted to number
console.log("2" === 2);     // false — different types, done

console.log(0 == false);    // true  — coerce to boolean
console.log(null == undefined);  // true — special case

console.log(0 === false);   // false
```

!!! warning "Always use `===` and `!==`"
    `==` has complicated coercion rules that lead to subtle bugs. `===` compares type + value — simple and predictable.

---

## Logical operators

```js
const a = true;
const b = false;

console.log(a && b);   // false — AND: true only if both are true
console.log(a || b);   // true  — OR: true if at least one is true
console.log(!a);       // false — NOT: inverts
```

Practical example:

```js
const age = 17;
const hasLicense = false;

if (age >= 18 && hasLicense) {
  console.log("Can drive.");
} else {
  console.log("Not yet.");
}
```

### Short-circuit (lazy evaluation)

- `&&` stops at the **first `false`**.
- `||` stops at the **first `true`**.

```js
// b() will not be called, because a() returned false
a() && b();

// b() will not be called, because a() returned true
a() || b();
```

Useful for default values:

```js
const name = userInput || "Unknown";
// if userInput is "" / null / undefined, use "Unknown"
```

---

## Ternary operator

A short form of `if / else` that returns a value:

```js
// condition ? valueIfTrue : valueIfFalse
const age = 16;
const label = age >= 18 ? "adult" : "minor";

console.log(label);   // "minor"
```

It can be useful, but **don't bury it** in nested expressions — it becomes unreadable.

---

## `switch / case`

When you have many branches based on the same variable:

```js
const day = "monday";

switch (day) {
  case "monday":
  case "tuesday":
  case "wednesday":
  case "thursday":
  case "friday":
    console.log("Weekday");
    break;
  case "saturday":
  case "sunday":
    console.log("Weekend!");
    break;
  default:
    console.log("Unknown day");
}
```

!!! note "Don't forget `break`!"
    Without `break`, execution "falls" into the next case (fall-through). Useful intentionally (as above, where multiple days run the same code), but dangerous if you forget.

---

## The `for` loop

```js
for (let i = 0; i < 5; i++) {
  console.log(`Iteration ${i}`);
}
// Iteration 0
// Iteration 1
// Iteration 2
// Iteration 3
// Iteration 4
```

Three parts in parentheses:

1. **Initialization** — `let i = 0` (runs once, at the start).
2. **Condition** — `i < 5` (checked before each iteration).
3. **Step** — `i++` (runs after each iteration).

`i++` is shorthand for `i = i + 1`. Similar: `i--`, `i += 2`, `i *= 3`.

---

## The `while` loop

```js
let n = 0;

while (n < 5) {
  console.log(n);
  n++;
}
```

Runs **as long as** the condition is `true`. Use it when you **don't know in advance** how many iterations you'll do.

---

## The `do...while` loop

Similar to `while`, but **runs at least once** (checks the condition at the end):

```js
let answer;

do {
  answer = prompt("Type 'exit' to finish:");
} while (answer !== "exit");
```

---

## `break` and `continue`

- **`break`** exits the loop completely.
- **`continue`** jumps to the next iteration.

```js
for (let i = 0; i < 10; i++) {
  if (i === 5) break;       // stops when i is 5
  if (i % 2 === 0) continue; // skips even numbers
  console.log(i);           // 1, 3
}
```

---

## `for...of` — for iterating over an array

The modern variant, **preferred** for going through an array:

```js
const colors = ["red", "green", "blue"];

for (const color of colors) {
  console.log(color);
}
// red
// green
// blue
```

Simple and clean. You no longer need an index `i`.

!!! note "`for...in` exists, but avoid it for arrays"
    `for...in` iterates over **keys** (including inherited ones) and is designed for objects. For arrays, use `for...of` or `.forEach()`.

---

## Common errors

### Infinite loop

You forget to increment the counter:

```js
// WRONG: n never increases!
let n = 0;
while (n < 5) {
  console.log(n);
  // n++ is missing
}
```

The browser will freeze. Open DevTools and stop the tab.

### `=` vs `==` vs `===`

```js
if (x = 5) { ... }    // assignment! not comparison. Almost always wrong.
if (x == 5) { ... }   // comparison with coercion. Avoid.
if (x === 5) { ... }  // strict equal. Correct.
```

---

## Exercises

### Exercise 1 — Even or odd
Write a program that reads a number and prints whether it's even or odd.

??? success "Solution"
    ```js
    const n = Number(prompt("A number:"));

    if (n % 2 === 0) {
      console.log(`${n} is even.`);
    } else {
      console.log(`${n} is odd.`);
    }
    ```

    `% 2` gives 0 for even numbers, 1 for odd ones.

### Exercise 2 — Numbers from 1 to 10
Print to the console the numbers from 1 to 10 with `for`.

??? success "Solution"
    ```js
    for (let i = 1; i <= 10; i++) {
      console.log(i);
    }
    ```

### Exercise 3 — Largest of three
You receive 3 numbers and print the largest one.

??? success "Solution"
    ```js
    const a = 12;
    const b = 47;
    const c = 8;

    let max = a;
    if (b > max) max = b;
    if (c > max) max = c;

    console.log(`Largest: ${max}`);   // 47

    // Short version, with Math.max:
    console.log(Math.max(a, b, c));    // 47
    ```

### Exercise 4 — Sum from 1 to 100
Calculate the sum of numbers from 1 to 100.

??? success "Solution"
    ```js
    let sum = 0;
    for (let i = 1; i <= 100; i++) {
      sum += i;
    }
    console.log(sum);   // 5050
    ```

---

## Mini-project: Guess the number

A classic game: the computer picks a random number between 1 and 100, you have as many tries as you need to guess it.

**Requirements:**

- Generate a random number between 1 and 100.
- In a loop, ask the user to guess.
- Give feedback: **too small** / **too big** / **correct**.
- At the end, show how many tries were needed.

??? success "Solution"
    ```js
    // Random number between 1 and 100
    const target = Math.floor(Math.random() * 100) + 1;

    let attempts = 0;
    let guessed = false;

    while (!guessed) {
      const answer = Number(prompt("Guess a number between 1 and 100:"));
      attempts++;

      if (answer === target) {
        guessed = true;
        alert(`Congratulations! You guessed in ${attempts} attempts.`);
      } else if (answer < target) {
        alert("Too small. Try again!");
      } else {
        alert("Too big. Try again!");
      }
    }
    ```

    `Math.random()` returns `[0, 1)`. Multiplied by 100 and floored with `Math.floor`, then `+1`, gives an integer `[1, 100]`.

---

## Summary

- `if / else if / else` — branching decisions.
- Use **`===`**, not `==`. This way you avoid implicit type coercion.
- Logical operators: `&&` (and), `||` (or), `!` (not). They use lazy evaluation.
- Ternary `condition ? a : b` — useful for simple assignments.
- `for` when you know how many iterations; `while` when you don't.
- `for...of` for going through the elements of an array.
- `break` exits, `continue` jumps to the next iteration.

---

**Next step:** [→ Lesson 14: Functions](14-js-functii.md)
