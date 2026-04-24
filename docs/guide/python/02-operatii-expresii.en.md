---
lesson: 2
tags: [python, operators, arithmetic, f-strings, conversions]
summary: Work with numbers and text — arithmetic operations, f-strings, and type conversions.
---

# Lesson 02 · Operations and expressions

!!! tip "What you'll learn"
    - Arithmetic operators and the order of operations
    - String operations
    - F-strings — the modern way to format text
    - Conversion between types: `int()`, `float()`, `str()`

---

## Arithmetic operators

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | addition | `3 + 4` | `7` |
| `-` | subtraction | `10 - 3` | `7` |
| `*` | multiplication | `3 * 4` | `12` |
| `/` | division (float result) | `7 / 2` | `3.5` |
| `//` | integer division | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | exponentiation | `2 ** 8` | `256` |

```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.3333...
print(10 // 3)  # 3
print(10 % 3)   # 1
print(2 ** 10)  # 1024
```

### Order of operations

Python follows standard math rules: `**` → `* / // %` → `+ -`

```python
print(2 + 3 * 4)    # 14 (not 20!)
print((2 + 3) * 4)  # 20 — parentheses change the order
```

### The `%` operator — what's it for?

`%` returns the **remainder** of division. Useful for checking parity:

```python
print(10 % 2)   # 0 — even
print(11 % 2)   # 1 — odd
print(15 % 5)   # 0 — divisible by 5
```

---

## String operations

### Concatenation with `+`

```python
first_name = "Anna"
last_name = "Pop"
print(first_name + " " + last_name)   # Anna Pop
```

### Repetition with `*`

```python
print("Ha" * 3)    # HaHaHa
print("-" * 30)    # ------------------------------
```

### Useful functions

```python
message = "  Welcome!  "
print(len(message))           # 12
print(message.upper())        # "  WELCOME!  "
print(message.lower())        # "  welcome!  "
print(message.strip())        # "Welcome!"
print(message.strip().upper()) # "WELCOME!"
```

---

## F-strings

F-strings let you insert variables directly into text:

```python
name = "Michael"
age = 14
print(f"My name is {name} and I am {age} years old.")
# My name is Michael and I am 14 years old.
```

### Number formatting

```python
pi = 3.14159265
print(f"Pi ≈ {pi:.2f}")   # Pi ≈ 3.14
print(f"Pi ≈ {pi:.4f}")   # Pi ≈ 3.1416
```

### Calculations inside f-strings

```python
width = 4
length = 7
print(f"Rectangle area: {width * length} m²")
# Rectangle area: 28 m²
```

---

## Type conversions

| Function | What it does |
|----------|--------------|
| `int(x)` | converts to whole number |
| `float(x)` | converts to decimal number |
| `str(x)` | converts to text |

```python
print(int(3.9))      # 3  (truncates decimals, doesn't round!)
print(int("42"))     # 42
print(float(5))      # 5.0
print(float("3.14")) # 3.14
print(str(100))      # "100"
```

!!! warning "Invalid conversions"
    ```python
    int("hello")    # ValueError
    int("3.14")     # ValueError — use int(float("3.14"))
    ```

---

## Exercises

### Exercise 1 — Calculate
Without running the code, calculate:

```python
print(17 % 5)
print(2 ** 3 + 1)
print(15 // 4)
```

??? success "Answer"
    - `17 % 5` → `2`
    - `2 ** 3 + 1` → `9`
    - `15 // 4` → `3`

### Exercise 2 — F-string
```python
product = "notebook"
price = 3.5
quantity = 4
```
Display: `4 notebooks cost 14.0 lei.`

??? success "Solution"
    ```python
    print(f"{quantity} {product}s cost {price * quantity} lei.")
    ```

### Exercise 3 — Even or odd?
Display the remainder of dividing 47 by 2.

??? success "Solution"
    ```python
    print(47 % 2)   # 1 — so it's odd
    ```

---

## Mini-project: Temperature converter

Convert 100 °C to Fahrenheit and Kelvin.

**Formulas:** `F = C × 9/5 + 32` and `K = C + 273.15`

**Output:**
```
Temperature: 100 °C
In Fahrenheit: 212.0 °F
In Kelvin: 373.15 K
```

??? success "Solution"
    ```python
    celsius = 100
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    print(f"Temperature: {celsius} °C")
    print(f"In Fahrenheit: {fahrenheit} °F")
    print(f"In Kelvin: {kelvin} K")
    ```

---

## Summary

- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- `%` returns the remainder — useful for parity
- F-strings `f"text {variable}"` — modern formatting
- Conversions: `int()`, `float()`, `str()`

---

**Next step:** [→ Lesson 03: Input and Output](03-input-output.md)
