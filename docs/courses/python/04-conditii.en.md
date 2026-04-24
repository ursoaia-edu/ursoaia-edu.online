---
lesson: 4
tags: [python, if, elif, else, conditions, logical-operators]
summary: Control what your program does based on conditions with if, elif, and else.
---

# Lesson 04 · Conditions

!!! tip "What you'll learn"
    - The `if / elif / else` structure
    - Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
    - Logical operators: `and`, `or`, `not`
    - Nested conditions

---

## The `if` statement

`if` lets you run code **only when a condition is true**:

```python
temperature = 35

if temperature > 30:
    print("It's hot outside!")
```

**Output:**
```
It's hot outside!
```

If `temperature` were `20`, nothing would be displayed.

!!! warning "Indentation is mandatory"
    The code inside `if` must be indented by **4 spaces** (or one Tab). Python uses indentation to know what belongs to the block.
    ```python
    if True:
        print("This line is inside the if")
    print("This line always runs")
    ```

---

## `if / else`

```python
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

`else` runs when the `if` condition is **false**.

---

## `if / elif / else`

`elif` (short for "else if") checks a new condition if the previous one was false:

```python
grade = 8.5

if grade >= 9.5:
    print("Excellent — rating: Outstanding")
elif grade >= 8.5:
    print("Great — rating: Very good")
elif grade >= 7:
    print("Satisfactory — rating: Good")
elif grade >= 5:
    print("Rating: Sufficient")
else:
    print("Rating: Insufficient")
```

Python checks the conditions **top to bottom** and stops at the first true one.

---

## Comparison operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | equal to | `5 == 5` | `True` |
| `!=` | different from | `5 != 3` | `True` |
| `<` | less than | `3 < 5` | `True` |
| `>` | greater than | `5 > 3` | `True` |
| `<=` | less than or equal | `5 <= 5` | `True` |
| `>=` | greater than or equal | `6 >= 5` | `True` |

!!! warning "= vs =="
    `=` assigns values. `==` compares values.
    ```python
    x = 5      # assignment
    x == 5     # comparison → True
    ```

---

## Logical operators

### `and` — both conditions must be true

```python
age = 16
has_license = False

if age >= 18 and has_license:
    print("Can drive.")
else:
    print("Cannot drive.")
```

### `or` — at least one must be true

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No school!")
```

### `not` — negates the condition

```python
is_raining = False

if not is_raining:
    print("We can go outside.")
```

---

## Nested conditions

You can place an `if` inside another `if`:

```python
score = 85
level = "advanced"

if score >= 50:
    print("You passed the test.")
    if level == "advanced":
        print("You earned the advanced certificate!")
    else:
        print("You earned the basic certificate.")
else:
    print("You did not pass the test.")
```

---

## Exercises

### Exercise 1 — Positive, negative, or zero?
Ask for a number and display whether it's positive, negative, or zero.

??? success "Solution"
    ```python
    number = float(input("Enter a number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
    ```

### Exercise 2 — The largest
Ask for two numbers and display the larger one.

??? success "Solution"
    ```python
    a = float(input("First number: "))
    b = float(input("Second number: "))
    if a > b:
        print(f"The largest is {a}")
    elif b > a:
        print(f"The largest is {b}")
    else:
        print("The numbers are equal")
    ```

### Exercise 3 — Divisible?
Ask for a number and check whether it is divisible by both 3 and 5.

??? success "Solution"
    ```python
    n = int(input("Number: "))
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} is divisible by 3 and 5")
    else:
        print(f"{n} is not divisible by both")
    ```

---

## Mini-project: Grade classifier

Ask for a grade (1–10) and display the rating with a motivational message.

**Example:**
```
Your grade: 9.2
Rating: Very good
Congratulations! You're close to perfection!
```

??? success "Solution"
    ```python
    grade = float(input("Your grade: "))

    if grade < 1 or grade > 10:
        print("Invalid grade. Enter a value between 1 and 10.")
    elif grade >= 9.5:
        print("Rating: Outstanding")
        print("Extraordinary! Top performance!")
    elif grade >= 8.5:
        print("Rating: Very good")
        print("Congratulations! You're close to perfection!")
    elif grade >= 7:
        print("Rating: Good")
        print("Good result! Keep practicing.")
    elif grade >= 5:
        print("Rating: Sufficient")
        print("You passed, but you have potential for more.")
    else:
        print("Rating: Insufficient")
        print("Don't lose heart! Review the material and try again.")
    ```

---

## Summary

- `if condition:` — run a block if the condition is true
- `elif other_condition:` — check another condition if the previous one is false
- `else:` — runs when no previous condition was true
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`
- Indentation (4 spaces) is mandatory!

---

**Next step:** [→ Lesson 05: Loops](05-bucle.md)
