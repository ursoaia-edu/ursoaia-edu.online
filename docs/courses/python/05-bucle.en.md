---
lesson: 5
tags: [python, for, while, loops, break, continue, range]
summary: Repeat actions with for and while loops. Control the flow with break and continue.
---

# Lesson 05 · Loops

!!! tip "What you'll learn"
    - The `for` loop with `range()`
    - The `while` loop
    - The `break` and `continue` statements
    - Nested loops

---

## The `for` loop

`for` repeats a block of code for each element in a sequence:

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### The `range()` function

| Call | Generated values |
|------|------------------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, 8, ..., 1 |

```python
# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# Count down
for i in range(5, 0, -1):
    print(i)
print("Start!")
```

### `for` over a string

```python
for letter in "Python":
    print(letter)
# P
# y
# t
# h
# o
# n
```

---

## The `while` loop

`while` repeats a block **as long as a condition is true**:

```python
number = 1
while number <= 5:
    print(number)
    number += 1   # number = number + 1
```

**Output:**
```
1
2
3
4
5
```

!!! warning "Infinite loop"
    If you forget to update the variable, the loop never ends:
    ```python
    # WRONG — infinite loop!
    x = 1
    while x <= 5:
        print(x)
        # forgot x += 1
    ```
    Stop the program with `Ctrl+C`.

### `while` for input validation

```python
answer = ""
while answer != "yes" and answer != "no":
    answer = input("Did you understand? (yes/no): ")
print("Thank you!")
```

---

## `break` — forced exit from the loop

```python
for i in range(1, 100):
    if i == 5:
        break
    print(i)
# Prints: 1, 2, 3, 4
```

---

## `continue` — skip to the next iteration

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)
# Prints: 1, 3, 5, 7, 9
```

---

## Nested loops

A loop inside another loop:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()
```

**Output:**
```
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3

2 × 1 = 2
...
```

---

## Exercises

### Exercise 1 — Sum from 1 to N
Ask for a number N and calculate the sum 1 + 2 + ... + N.

??? success "Solution"
    ```python
    n = int(input("N = "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum = {total}")
    ```

### Exercise 2 — Prime numbers
Display all prime numbers smaller than 50.

??? success "Solution"
    ```python
    for n in range(2, 50):
        is_prime = True
        for d in range(2, n):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            print(n)
    ```

### Exercise 3 — Guess the number
Generate a "secret" number (hardcoded) and let the user guess with feedback.

??? success "Solution"
    ```python
    secret = 42
    attempts = 0

    while True:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed in {attempts} attempts.")
            break
    ```

---

## Mini-project: Multiplication table

Display the multiplication table for numbers 1–10 in a tabular format.

**Output (first rows):**
```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
...
```

??? success "Solution"
    ```python
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()
    ```
    `{i*j:4}` formats the number across 4 characters for alignment.

---

## Summary

- `for i in range(n):` — repeat `n` times
- `range(start, stop, step)` — generate sequences of numbers
- `while condition:` — repeat as long as the condition is true
- `break` — forced exit from the loop
- `continue` — skip to the next iteration
- Indentation is mandatory!

---

**Next step:** [→ Lesson 06: Lists](06-liste.md)
