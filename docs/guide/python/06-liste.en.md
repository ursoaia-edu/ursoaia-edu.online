---
lesson: 6
tags: [python, lists, indexing, slice, list-methods]
summary: Store and manipulate collections of values with Python lists.
---

# Lesson 06 · Lists

!!! tip "What you'll learn"
    - How to create and access a list
    - Indexing and slicing
    - The main list methods
    - Iterating over lists with `for`

---

## What is a list?

A **list** stores multiple values in a single variable, in order:

```python
grades = [8, 9, 7, 10, 6]
fruits = ["apple", "pear", "cherry"]
mixed = [42, "hello", True, 3.14]   # can contain different types
empty = []                          # empty list
```

---

## Indexing

Each element has an **index** (position), starting from `0`:

```python
fruits = ["apple", "pear", "cherry", "currant"]
#           0        1       2          3

print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[-1])  # currant — last element
print(fruits[-2])  # cherry — second-to-last
```

!!! note "Negative indexing"
    `-1` is the last element, `-2` the second-to-last, etc.

---

## Slicing — sub-lists

```python
grades = [5, 7, 8, 9, 10]
#         0  1  2  3   4

print(grades[1:3])    # [7, 8]      — from index 1 to 3 (exclusive)
print(grades[:3])     # [5, 7, 8]   — from start to 3
print(grades[2:])     # [8, 9, 10]  — from 2 to the end
print(grades[::2])    # [5, 8, 10]  — every other element
print(grades[::-1])   # [10, 9, 8, 7, 5] — reversed list
```

---

## Modifying lists

```python
colors = ["red", "green", "blue"]

colors[1] = "yellow"
print(colors)   # ["red", "yellow", "blue"]
```

---

## The main methods

```python
grades = [8, 6, 9, 7]

grades.append(10)         # add to the end: [8, 6, 9, 7, 10]
grades.insert(0, 5)       # insert at position 0: [5, 8, 6, 9, 7, 10]
grades.remove(6)          # remove the first occurrence of 6
removed_grade = grades.pop()     # remove and return the last element
removed_grade = grades.pop(0)    # remove and return the element at index 0
grades.sort()             # sort ascending (modifies the original list)
grades.sort(reverse=True) # sort descending
grades.reverse()          # reverse the list
print(len(grades))        # number of elements
print(grades.count(9))    # how many times 9 appears
print(grades.index(9))    # index of the first occurrence of 9
```

---

## Iterating with `for`

```python
fruits = ["apple", "pear", "cherry"]

for fruit in fruits:
    print(fruit)
```

### `enumerate()` — index and value

```python
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: pear
# 2: cherry
```

---

## Useful functions

```python
grades = [8, 6, 9, 7, 10]

print(len(grades))    # 5
print(sum(grades))    # 40
print(max(grades))    # 10
print(min(grades))    # 6
print(sorted(grades)) # [6, 7, 8, 9, 10] — does not modify the original
```

---

## Membership check with `in`

```python
fruits = ["apple", "pear", "cherry"]

print("pear" in fruits)        # True
print("pineapple" in fruits)   # False
print("pineapple" not in fruits) # True
```

---

## Exercises

### Exercise 1 — Access
You have the list `planets = ["Mercury", "Venus", "Earth", "Mars"]`. Display the first and last planet.

??? success "Solution"
    ```python
    planets = ["Mercury", "Venus", "Earth", "Mars"]
    print(planets[0])    # Mercury
    print(planets[-1])   # Mars
    ```

### Exercise 2 — Sum of grades
Ask the user for 5 grades, store them in a list, and display the sum and the average.

??? success "Solution"
    ```python
    grades = []
    for i in range(5):
        grade = float(input(f"Grade {i + 1}: "))
        grades.append(grade)
    print(f"Sum: {sum(grades)}")
    print(f"Average: {sum(grades) / len(grades):.2f}")
    ```

### Exercise 3 — Filter
From the list `[3, 7, 2, 9, 4, 6, 1, 8, 5]`, build a new list containing only the numbers greater than 5.

??? success "Solution"
    ```python
    numbers = [3, 7, 2, 9, 4, 6, 1, 8, 5]
    large = []
    for n in numbers:
        if n > 5:
            large.append(n)
    print(large)   # [7, 9, 6, 8]
    ```

---

## Mini-project: Top 5 scores

Ask the user for 5 scores, sort them descending, and display the leaderboard.

**Example:**
```
Score 1: 850
Score 2: 1200
Score 3: 450
Score 4: 990
Score 5: 750

=== TOP 5 SCORES ===
#1: 1200
#2: 990
#3: 850
#4: 750
#5: 450
```

??? success "Solution"
    ```python
    scores = []
    for i in range(5):
        score = int(input(f"Score {i + 1}: "))
        scores.append(score)

    scores.sort(reverse=True)

    print()
    print("=== TOP 5 SCORES ===")
    for i, score in enumerate(scores):
        print(f"#{i + 1}: {score}")
    ```

---

## Summary

- Lists store multiple values: `[val1, val2, val3]`
- Indexing starts at `0`; negative indexes count from the end
- Slicing: `list[start:stop:step]`
- Key methods: `append()`, `remove()`, `sort()`, `pop()`, `len()`
- `for elem in list:` iterates over all elements
- `x in list` checks whether `x` exists in the list

---

**Next step:** [→ Lesson 07: Dictionaries](07-dictionare.md)
