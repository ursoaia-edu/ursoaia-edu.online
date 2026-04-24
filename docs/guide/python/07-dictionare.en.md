---
lesson: 7
tags: [python, dictionaries, dict, keys, values]
summary: Store structured data with Python dictionaries — key-value pairs.
---

# Lesson 07 · Dictionaries

!!! tip "What you'll learn"
    - What a dictionary is and when to use it
    - How to create, access, and modify a dictionary
    - The main methods: `.keys()`, `.values()`, `.items()`
    - Iterating over a dictionary

---

## What is a dictionary?

A **dictionary** stores **key → value** pairs, like a real dictionary where the word is the key and the definition is the value:

```python
student = {
    "name": "Andrew",
    "age": 14,
    "average": 9.5,
    "is_honor_student": True
}
```

Unlike lists (where you access elements via a numeric index), dictionaries are accessed via **keys**:

```python
print(student["name"])      # Andrew
print(student["average"])   # 9.5
```

---

## Creating a dictionary

```python
# Empty dictionary
data = {}

# Dictionary with initial values
car = {
    "brand": "Dacia",
    "model": "Logan",
    "year": 2020,
    "km": 45000
}
```

Keys can be `str`, `int`, or `float`. Values can be any type.

---

## Accessing values

### With `[]`

```python
print(car["brand"])   # Dacia
```

If the key doesn't exist, you get a `KeyError`.

### With `.get()` — safer

```python
print(car.get("color"))                  # None (no error)
print(car.get("color", "unknown"))       # unknown
```

---

## Adding and modifying

```python
car["color"] = "white"   # add a new key
car["km"] = 46000         # modify an existing value
print(car)
```

---

## Deleting keys

```python
del car["km"]              # delete the key
year = car.pop("year", None)   # delete and return the value
```

---

## Checking key existence

```python
if "brand" in car:
    print("We have brand:", car["brand"])
```

---

## The main methods

```python
person = {"name": "Helen", "age": 16, "city": "Cluj"}

print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Helen', 16, 'Cluj'])
print(person.items())   # dict_items([('name', 'Helen'), ...])
print(len(person))      # 3
```

---

## Iterating

### Just the keys

```python
for key in person:
    print(key)
# name
# age
# city
```

### Keys and values with `.items()`

```python
for key, value in person.items():
    print(f"{key}: {value}")
# name: Helen
# age: 16
# city: Cluj
```

---

## Nested dictionaries

```python
classroom = {
    "Andrew": {"romanian_grade": 9, "math_grade": 8},
    "Mary": {"romanian_grade": 10, "math_grade": 9},
}

print(classroom["Mary"]["math_grade"])   # 9
```

---

## Exercises

### Exercise 1 — The capital
Create a dictionary with 5 country-capital pairs. Ask the user for a country and display the capital (or "Unknown" if it doesn't exist).

??? success "Solution"
    ```python
    capitals = {
        "Romania": "Bucharest",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid"
    }
    country = input("Country: ")
    print(capitals.get(country, "Unknown"))
    ```

### Exercise 2 — Counting occurrences
Count how many times each letter appears in the word `"programming"`.

??? success "Solution"
    ```python
    word = "programming"
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    for letter, count in frequency.items():
        print(f"{letter}: {count}")
    ```

### Exercise 3 — Update
Starting from `{"apples": 5, "pears": 3}`, add `"cherries": 10`, change apples to `8`, and delete pears.

??? success "Solution"
    ```python
    basket = {"apples": 5, "pears": 3}
    basket["cherries"] = 10
    basket["apples"] = 8
    del basket["pears"]
    print(basket)   # {'apples': 8, 'cherries': 10}
    ```

---

## Mini-project: Contact book

Build a small contact-management program that lets you add, search, and list contacts.

**Example run:**
```
1. Add contact
2. Search contact
3. List all
4. Exit
Your choice: 1
Name: Anna
Phone: 0722123456
Contact added!
```

??? success "Solution"
    ```python
    contacts = {}

    while True:
        print("\n1. Add contact")
        print("2. Search contact")
        print("3. List all")
        print("4. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            contacts[name] = phone
            print("Contact added!")
        elif choice == "2":
            name = input("Search by name: ")
            print(contacts.get(name, "Contact not found."))
        elif choice == "3":
            if contacts:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
            else:
                print("No contacts saved.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
    ```

---

## Summary

- Dictionaries store key-value pairs: `{"key": value}`
- Access: `dict["key"]` or `dict.get("key", default)`
- Add/modify: `dict["key"] = value`
- Delete: `del dict["key"]` or `dict.pop("key")`
- Iterate with `.items()` for keys and values together
- Check: `"key" in dict`

---

**Next step:** [→ Lesson 08: Functions](08-functii.md)
