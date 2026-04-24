---
lesson: 3
tags: [python, input, output, interactivity]
summary: Make programs interactive with input() and format output with print().
---

# Lesson 03 · Input and Output

!!! tip "What you'll learn"
    - How to read data from the user with `input()`
    - Why `input()` always returns `str`
    - How to convert input into numbers
    - Advanced output formatting

---

## The `input()` function

`input()` pauses the program and waits for the user to type something and press Enter:

```python
name = input("What's your name? ")
print("Hello,", name)
```

**Run:**
```
What's your name? Andrew
Hello, Andrew
```

The text inside the parentheses is the **prompt** — the message shown to the user.

---

## `input()` ALWAYS returns `str`

This is the most common source of errors for beginners:

```python
age = input("Your age: ")
print(type(age))   # <class 'str'>
```

Even if the user types `14`, Python receives the string `"14"`, not the number `14`.

### Converting input

```python
age = int(input("Your age: "))
print(type(age))   # <class 'int'>
print(age + 1)     # works!
```

```python
height = float(input("Your height (m): "))
print(f"Height in cm: {height * 100}")
```

!!! warning "If the user types something else"
    `int(input(...))` will raise an error if the user types text instead of a number. We'll solve that in the lesson on conditions and exceptions.

---

## The `print()` function — details

### The `sep` separator

```python
print("Mon", "Tue", "Wed")              # Mon Tue Wed
print("Mon", "Tue", "Wed", sep=", ")    # Mon, Tue, Wed
print("Mon", "Tue", "Wed", sep="\n")    # each on a new line
```

### The `end` terminator

```python
print("One", end=" ")
print("Two", end=" ")
print("Three")
# One Two Three — all on the same line
```

### Empty line

```python
print()   # prints an empty line
```

---

## Combined examples

### Simple greeting program

```python
first_name = input("Your first name: ")
age = int(input("Your age: "))

print()
print(f"Hello, {first_name}!")
print(f"Next year you will be {age + 1} years old.")
```

### Reading multiple values

```python
a = float(input("First number: "))
b = float(input("Second number: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} × {b} = {a * b}")
```

---

## Exercises

### Exercise 1 — Personalized greeting
Write a program that asks for name and age, then displays: `"Hi, [name]! You are [age] years old."`

??? success "Solution"
    ```python
    name = input("Your name: ")
    age = int(input("Your age: "))
    print(f"Hi, {name}! You are {age} years old.")
    ```

### Exercise 2 — Rectangle area
Ask for the length and width of a rectangle, calculate the area and the perimeter.

??? success "Solution"
    ```python
    length = float(input("Length (m): "))
    width = float(input("Width (m): "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area: {area} m²")
    print(f"Perimeter: {perimeter} m")
    ```

### Exercise 3 — How many seconds?
Ask for hours and minutes, display the total in seconds.

??? success "Solution"
    ```python
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = hours * 3600 + minutes * 60
    print(f"{hours}h {minutes}min = {seconds} seconds")
    ```

---

## Mini-project: Interactive calculator

Write a program that asks for two numbers and displays all the basic operations.

**Example run:**
```
First number: 10
Second number: 3

10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 × 3.0 = 30.0
10.0 / 3.0 = 3.3333333333333335
10.0 // 3.0 = 3.0
10.0 % 3.0 = 1.0
10.0 ^ 3.0 = 1000.0
```

??? success "Solution"
    ```python
    a = float(input("First number: "))
    b = float(input("Second number: "))

    print()
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} × {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ^ {b} = {a ** b}")
    ```

---

## Summary

- `input("message")` reads text from the keyboard — ALWAYS returns `str`
- Convert with `int(input(...))` or `float(input(...))`
- `print(a, b, sep=", ")` controls the separator
- `print("text", end="")` controls what comes after the line

---

**Next step:** [→ Lesson 04: Conditions](04-conditii.md)
