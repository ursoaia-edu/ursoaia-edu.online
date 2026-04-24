---
lesson: 9
tags: [python, files, reading, writing, csv, json]
summary: Read and write data from text, CSV, and JSON files.
---

# Lesson 09 · Files

!!! tip "What you'll learn"
    - Opening and closing files with `with open()`
    - Reading: `read()`, `readline()`, `readlines()`
    - Writing: `write()`, `writelines()`
    - Working with CSV and JSON files

---

## Why files?

Until now, the data in our programs disappeared when the program closed. Files allow **data persistence** — you save data and read it back later.

---

## Opening a file

```python
with open("data.txt", "r") as f:
    content = f.read()
print(content)
```

- `"data.txt"` — the file name
- `"r"` — the open mode (read)
- `as f` — the variable through which you access the file
- `with` — automatically closes the file when leaving the block

### Open modes

| Mode | Meaning |
|------|---------|
| `"r"` | read (file must exist) |
| `"w"` | write (creates or overwrites the file) |
| `"a"` | append at end |
| `"r+"` | read and write |

---

## Reading

### `read()` — the whole file as a single string

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
```

### `readlines()` — a list of lines

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())   # .strip() removes the trailing \n
```

### `readline()` — one line at a time

```python
with open("hello.txt", "r", encoding="utf-8") as f:
    first = f.readline()
    second = f.readline()
```

!!! tip "encoding='utf-8'"
    Always add `encoding="utf-8"` to support Romanian diacritics (ă, î, ș, ț, â).

---

## Writing

```python
with open("results.txt", "w", encoding="utf-8") as f:
    f.write("Andrew: 95\n")
    f.write("Mary: 87\n")
    f.write("Robert: 91\n")
```

!!! warning "`'w'` mode overwrites!"
    If the file already exists, `"w"` deletes it and starts over. Use `"a"` to add to the end.

### Append to an existing file

```python
with open("results.txt", "a", encoding="utf-8") as f:
    f.write("Helen: 99\n")
```

---

## CSV files

CSV (Comma-Separated Values) = values separated by commas. Ideal for simple tables.

```python
import csv

# Write CSV
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade", "Class"])   # header
    writer.writerow(["Anna", 9.5, "8A"])
    writer.writerow(["Michael", 8.0, "8B"])

# Read CSV
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['Name', 'Grade', 'Class']
# ['Anna', '9.5', '8A']
# ['Michael', '8.0', '8B']
```

---

## JSON files

JSON (JavaScript Object Notation) = a structured data format. Ideal for dictionaries and lists.

```python
import json

# Write JSON
data = {
    "student": "Andrew",
    "grades": [8, 9, 7, 10],
    "average": 8.5
}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Read JSON
with open("student.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data["student"])   # Andrew
print(loaded_data["grades"])    # [8, 9, 7, 10]
```

---

## Exercises

### Exercise 1 — Write and read
Write a program that saves 3 sentences to a file, then reads them back and displays them numbered.

??? success "Solution"
    ```python
    sentences = [
        "Python is fun.",
        "Files keep your data.",
        "Programming opens doors."
    ]

    with open("sentences.txt", "w", encoding="utf-8") as f:
        for s in sentences:
            f.write(s + "\n")

    with open("sentences.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"{i}. {line.strip()}")
    ```

### Exercise 2 — Word count
Read a text file and display the number of lines and words.

??? success "Solution"
    ```python
    with open("sentences.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    print(f"Lines: {line_count}, Words: {word_count}")
    ```

---

## Mini-project: Persistent scoreboard

Build a program that saves and displays a leaderboard of scores in JSON format.

**Functionality:**
- Asks for a name and a score
- Adds it to the leaderboard
- Displays the sorted top
- Persists between runs

??? success "Solution"
    ```python
    import json
    import os

    FILE = "scores.json"

    def load_scores():
        if os.path.exists(FILE):
            with open(FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_scores(scores):
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)

    scores = load_scores()

    name = input("Your name: ")
    score = int(input("Your score: "))
    scores.append({"name": name, "score": score})

    scores.sort(key=lambda x: x["score"], reverse=True)
    save_scores(scores)

    print("\n=== LEADERBOARD ===")
    for i, entry in enumerate(scores[:5], 1):
        print(f"#{i}: {entry['name']} — {entry['score']}")
    ```

---

## Summary

- `with open("file", "mode", encoding="utf-8") as f:` — opens the file safely
- Modes: `"r"` read, `"w"` write, `"a"` append
- `f.read()` — everything as a string; `f.readlines()` — list of lines
- The `csv` module for tables; the `json` module for structured data
- `encoding="utf-8"` — required for Romanian characters

---

**Next step:** [→ Project: Text adventure game](10-proiect-joc-aventura.md)
