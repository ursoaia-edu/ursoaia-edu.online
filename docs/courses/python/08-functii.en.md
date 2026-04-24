---
lesson: 8
tags: [python, functions, def, parameters, return, scope]
summary: Organize your code into reusable blocks with Python functions.
---

# Lesson 08 · Functions

!!! tip "What you'll learn"
    - How to define and call a function with `def`
    - Parameters and arguments
    - The return value with `return`
    - Scope: local vs global
    - Parameters with default values

---

## Why functions?

Without functions, if you want to compute the area of a rectangle three times, you write the code three times. With functions, you write it once and **call** it as many times as you need:

```python
def rectangle_area(length, width):
    return length * width

print(rectangle_area(4, 5))    # 20
print(rectangle_area(10, 3))   # 30
print(rectangle_area(7, 7))    # 49
```

---

## Basic syntax

```python
def greet():
    print("Good day!")

greet()   # function call → Good day!
```

### Anatomy of a function

```python
def calculate_average(grades):     # 'grades' is the parameter
    total = sum(grades)
    average = total / len(grades)
    return average                 # the returned value

result = calculate_average([8, 9, 7, 10])
print(result)   # 8.5
```

- `def` — the keyword for defining a function
- `calculate_average` — the function name
- `grades` — the parameter (the input data)
- `return` — sends back a value

---

## Parameters and arguments

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Anna", 14)        # Anna, 14
introduce("Michael", 16)     # Michael, 16
```

### Keyword arguments

```python
introduce(age=15, name="Helen")   # order doesn't matter
```

### Parameters with default values

```python
def greet(name, message="Good day"):
    print(f"{message}, {name}!")

greet("Anna")              # Good day, Anna!
greet("Michael", "Hi")     # Hi, Michael!
```

---

## Functions without `return`

A function without `return` implicitly returns `None`:

```python
def show_title(text):
    print("=" * len(text))
    print(text)
    print("=" * len(text))

show_title("Leaderboard")
# ===========
# Leaderboard
# ===========
```

---

## Scope

Variables created **inside** a function are **local** — they don't exist outside it:

```python
def calc():
    x = 10   # local variable
    print(x)

calc()
print(x)   # NameError — x doesn't exist here!
```

Variables defined **outside** any function are **global**:

```python
name = "Global"   # global variable

def show():
    print(name)   # can be read

show()   # Global
```

!!! warning "Avoid modifying global variables from inside functions"
    Modifying global variables from inside functions makes the code hard to follow. Prefer passing values as parameters and returning them.

---

## Multiple return values

Python can return multiple values at once (as a tuple):

```python
def min_max(values):
    return min(values), max(values)

minimum, maximum = min_max([3, 7, 1, 9, 4])
print(minimum)   # 1
print(maximum)   # 9
```

---

## Exercises

### Exercise 1 — Simple function
Write a function `square(n)` that returns the square of `n`.

??? success "Solution"
    ```python
    def square(n):
        return n ** 2

    print(square(5))    # 25
    print(square(12))   # 144
    ```

### Exercise 2 — Celsius to Fahrenheit
Write a function `celsius_to_fahrenheit(c)` that converts the temperature.

??? success "Solution"
    ```python
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

    print(celsius_to_fahrenheit(0))    # 32.0
    print(celsius_to_fahrenheit(100))  # 212.0
    ```

### Exercise 3 — Validation
Write a function `is_even(n)` that returns `True` if `n` is even, `False` otherwise.

??? success "Solution"
    ```python
    def is_even(n):
        return n % 2 == 0

    print(is_even(4))   # True
    print(is_even(7))   # False
    ```

---

## Mini-project: Password generator

Write a function that generates a random password using uppercase letters, lowercase letters, and digits.

```python
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

print(generate_password())      # e.g., "aB3xKp9Q"
print(generate_password(12))    # e.g., "kR7mNq2xPa5L"
```

??? note "What are `string.ascii_letters` and `random.choice`?"
    - `string.ascii_letters` = all lowercase and uppercase letters: `abcde...XYZ`
    - `string.digits` = the digits: `0123456789`
    - `random.choice(s)` = picks a random character from the string `s`

---

## Summary

- `def name(param):` defines a function
- `return value` sends back the result
- Parameters with default values: `def f(x, y=0):`
- Local variables only exist inside the function
- Functions can return multiple values: `return a, b`

---

**Next step:** [→ Lesson 09: Files](09-fisiere.md)
