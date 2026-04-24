---
lesson: 1
tags: [python, variables, data-types, int, float, str, bool]
summary: Understand variables and the four basic data types in Python.
---

# Lesson 01 · Variables and data types

!!! tip "What you'll learn"
    - What a variable is and how to create one
    - The 4 basic types: `int`, `float`, `str`, `bool`
    - How to find the type of a value with `type()`
    - The rules for naming variables

---

## What is a variable?

A variable is a **labeled box** in which you store a value. The label is the **name** of the variable, and the contents of the box is its **value**.

```python
age = 14
name = "Andrew"
is_honor_student = True
```

Every time you write `age`, Python gives you the value `14`.

### Creating a variable

```python
# syntax: variable_name = value
score = 100
city = "Bucharest"
temperature = 36.6
```

The `=` sign is the **assignment operator** — it doesn't mean "equal", but "store the value on the right into the variable on the left".

!!! note "Variables can be changed"
    ```python
    score = 100
    print(score)   # 100
    score = 250
    print(score)   # 250
    ```

---

## The 4 basic types

### 1. `int` — whole numbers

```python
age = 14
student_count = 32
min_temperature = -5
```

No decimal point, no quotes.

### 2. `float` — decimal numbers

```python
height = 1.75
grade = 9.5
pi = 3.14159
```

!!! note "Period, not comma"
    Python uses the **period** as the decimal separator: `9.5` ✓, not `9,5` ✗

### 3. `str` — strings of characters (text)

```python
first_name = "Anna"
message = 'Welcome!'
sentence = "I am 14 years old and I live in Cluj."
```

Single `'...'` and double `"..."` quotes work the same.

### 4. `bool` — logical values

```python
is_adult = False
got_high_grade = True
```

Only two possible values: `True` or `False` (capital letter is mandatory!).

---

## The `type()` function

```python
print(type(14))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
```

---

## Naming rules

| Rule | Correct | Wrong |
|------|---------|-------|
| Letter or `_` at start | `age`, `_x` | `1age`, `@score` |
| No spaces | `student_count` | `student count` |
| Letters, digits, `_` | `game_score2` | `game-score` |
| Case-sensitive | `Age ≠ age` | — |
| No reserved words | — | `if`, `for`, `while` |

### Writing conventions

```python
# snake_case — recommended for variables
number_of_students = 32
max_temperature = 37.5

# UPPERCASE — for constants (values that don't change)
PI = 3.14159
SPEED_OF_LIGHT = 299792458
```

---

## Displaying variables

```python
name = "Helen"
age = 15

print(name)           # Helen
print(age)            # 15
print(name, age)      # Helen 15
```

---

## Exercises

### Exercise 1 — Define variables
Create variables for: your name (`str`), your age (`int`), your math grade average (`float`), and whether you are in 9th grade (`bool`).

??? success "Solution"
    ```python
    name = "Michael"
    age = 15
    math_average = 9.25
    is_grade_9 = True
    ```

### Exercise 2 — Which type?
What type is each value?

```python
x = 42
y = "42"
z = 42.0
w = False
```

??? success "Answer"
    - `x = 42` → `int`
    - `y = "42"` → `str` (the quotes make the difference!)
    - `z = 42.0` → `float` (the decimal point matters)
    - `w = False` → `bool`

### Exercise 3 — Track the value
What does the following program display?

```python
points = 10
points = points + 5
points = points * 2
print(points)
```

??? success "Answer"
    ```
    30
    ```
    `10 + 5 = 15`, then `15 × 2 = 30`.

### Exercise 4 — Find the errors
What's wrong?

```python
student count = 30
2score = 100
if = "word"
```

??? success "Answer"
    - `student count` → space not allowed → `student_count`
    - `2score` → cannot start with a digit → `score2`
    - `if` → Python reserved word → choose another name, e.g. `word`

---

## Mini-project: Personal record card

Create variables for a person and display them in a formatted way.

**Expected output:**
```
=== Personal record card ===
Name: Robert Popescu
Age: 13
Grade: 7
Overall average: 9.8
Is honor student: True
```

??? success "Solution"
    ```python
    name = "Robert Popescu"
    age = 13
    grade = 7
    average = 9.8
    is_honor_student = True

    print("=== Personal record card ===")
    print("Name:", name)
    print("Age:", age)
    print("Grade:", grade)
    print("Overall average:", average)
    print("Is honor student:", is_honor_student)
    ```

---

## Summary

- A **variable** stores a value under a name you choose
- Basic types: `int`, `float`, `str`, `bool`
- `type(x)` tells you the type of value `x`
- Use `snake_case` for naming variables

---

**Next step:** [→ Lesson 02: Operations and expressions](02-operatii-expresii.md)
