---
lesson: 3
tags: [web, html, lists, tables, ul, ol, thead, accessibility]
summary: How to structure data with unordered lists, ordered lists, and semantic tables — thead, tbody, colspan, rowspan, caption.
---

# Lesson 03 · Lists and tables

!!! tip "What you'll learn"
    - **Unordered** lists (`<ul>`) and **ordered** lists (`<ol>`)
    - Nested lists and description lists (`<dl>`)
    - Tables: `<table>`, `<tr>`, `<td>`, `<th>`
    - Semantic structure: `<thead>`, `<tbody>`, `<tfoot>`
    - `colspan` and `rowspan` for larger cells
    - When **NOT** to use tables (for layout)

---

## Unordered lists

`<ul>` = *unordered list*. Each row is an `<li>` (*list item*).

```html
<h2>Ingredients for stuffed cabbage</h2>
<ul>
  <li>Sauerkraut</li>
  <li>Minced meat</li>
  <li>Rice</li>
  <li>Onion</li>
  <li>Spices</li>
</ul>
```

The browser shows bullets (`•`) in front of each item.

---

## Ordered lists

`<ol>` = *ordered list*. It's displayed with numbers `1. 2. 3.`

```html
<h2>Steps to start the engine</h2>
<ol>
  <li>Insert the key into the ignition.</li>
  <li>Turn the key to the "ON" position.</li>
  <li>Press the clutch.</li>
  <li>Start the engine.</li>
</ol>
```

### Useful attributes

```html
<!-- Number with capital letters: A, B, C -->
<ol type="A">
  <li>First option</li>
  <li>Second option</li>
</ol>

<!-- Start at 5: 5, 6, 7... -->
<ol start="5">
  <li>Item five</li>
  <li>Item six</li>
</ol>

<!-- Reverse order: 3, 2, 1 -->
<ol reversed>
  <li>Bronze</li>
  <li>Silver</li>
  <li>Gold</li>
</ol>
```

Values for `type`: `1` (default), `A`, `a`, `I`, `i`.

---

## Nested lists

A list can contain other lists:

```html
<h2>My subjects</h2>
<ul>
  <li>Mathematics
    <ul>
      <li>Algebra</li>
      <li>Geometry</li>
      <li>Calculus</li>
    </ul>
  </li>
  <li>Computer Science
    <ul>
      <li>HTML / CSS</li>
      <li>Python</li>
      <li>Arduino</li>
    </ul>
  </li>
  <li>English Literature</li>
</ul>
```

!!! warning "Put the sub-list INSIDE the `<li>`"
    Nested lists must be **children of an `<li>`**, not between `<li>` items. Here's the classic mistake:

    ```html
    <!-- WRONG -->
    <ul>
      <li>Mathematics</li>
      <ul>
        <li>Algebra</li>
      </ul>
      <li>Computer Science</li>
    </ul>
    ```

---

## Description lists (`<dl>`)

Less common, but perfect for **glossaries** and **term-definition pairs**:

```html
<dl>
  <dt>HTML</dt>
  <dd>Markup language for the structure of pages.</dd>

  <dt>CSS</dt>
  <dd>Language for styling HTML pages.</dd>

  <dt>JavaScript</dt>
  <dd>Language for page interactivity.</dd>
</dl>
```

- `<dl>` = *description list*
- `<dt>` = *description term*
- `<dd>` = *description details*

---

## Tables — basic structure

A table is a matrix: **rows** with **cells**.

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>City</th>
  </tr>
  <tr>
    <td>Anna</td>
    <td>13</td>
    <td>Cluj</td>
  </tr>
  <tr>
    <td>Mike</td>
    <td>14</td>
    <td>Bucharest</td>
  </tr>
</table>
```

- `<table>` — the table.
- `<tr>` (*table row*) — a row.
- `<th>` (*table header*) — a **header** cell (bold + centered by default).
- `<td>` (*table data*) — a normal cell.

---

## Semantic structure

A professional table has **3 zones**:

```html
<table>
  <thead>
    <tr>
      <th>Product</th>
      <th>Price</th>
      <th>Quantity</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Notebook</td>
      <td>5 lei</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Pen</td>
      <td>2 lei</td>
      <td>30</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <td>Total</td>
      <td>120 lei</td>
      <td>42</td>
    </tr>
  </tfoot>
</table>
```

- `<thead>` — the header (columns, titles)
- `<tbody>` — the body (rows of data)
- `<tfoot>` — totals, summary

Browsers and screen readers can treat the 3 zones differently (e.g. the header stays visible when printing).

---

## `colspan` and `rowspan`

Sometimes a cell needs to span **multiple columns** or **multiple rows**.

### colspan (cell across multiple columns)

```html
<table>
  <tr>
    <th colspan="2">Contact</th>
  </tr>
  <tr>
    <td>Email</td>
    <td>anna@example.com</td>
  </tr>
  <tr>
    <td>Phone</td>
    <td>+40 712 345 678</td>
  </tr>
</table>
```

### rowspan (cell across multiple rows)

```html
<table>
  <tr>
    <th>City</th>
    <th>Season</th>
    <th>Temperature</th>
  </tr>
  <tr>
    <td rowspan="2">Cluj</td>
    <td>Summer</td>
    <td>25°C</td>
  </tr>
  <tr>
    <td>Winter</td>
    <td>-5°C</td>
  </tr>
</table>
```

The "Cluj" cell stretches across 2 rows; you don't write it a second time.

---

## When NOT to use tables

In the 2000s, people used `<table>` for **the entire page layout** (columns, sidebars, etc.). **Wrong!**

- Tables are for **tabular data**: rows × columns of related information.
- For **page layout** (top navigation, middle content, sidebar) we use **Flexbox** and **Grid** — you'll learn this in Lesson 08.

!!! warning "Simple rule"
    If the data would also make sense in Excel/Sheets — it's a table. If it's just "I want two columns on the page" — it's **NOT** a table.

---

## Accessibility for tables

### `<caption>` — title for a table

```html
<table>
  <caption>Schedule for class 8A</caption>
  <thead>
    ...
  </thead>
</table>
```

It appears above the table and is read by screen readers.

### `scope` for headers

```html
<tr>
  <th scope="col">Monday</th>
  <th scope="col">Tuesday</th>
</tr>
<tr>
  <th scope="row">08:00</th>
  <td>Math</td>
  <td>English</td>
</tr>
```

- `scope="col"` — **column** header.
- `scope="row"` — **row** header.

Screen readers use `scope` to tell the user: "the Math cell is at the intersection of the 08:00 row and the Monday column".

---

## Exercises

### Exercise 1 — Your TV shows
Make an unordered list of 5 favorite shows / series.

??? success "Solution"
    ```html
    <h2>My favorite shows</h2>
    <ul>
      <li>Stranger Things</li>
      <li>Las Fierbinți</li>
      <li>MasterChef</li>
      <li>Pro TV News</li>
      <li>The Voice of Romania</li>
    </ul>
    ```

### Exercise 2 — Nested lists
Make a list with 3 subjects, and under each, 3 sub-topics.

??? success "Solution"
    ```html
    <ul>
      <li>Mathematics
        <ul>
          <li>Equations</li>
          <li>Geometry</li>
          <li>Probability</li>
        </ul>
      </li>
      <li>Physics
        <ul>
          <li>Mechanics</li>
          <li>Optics</li>
          <li>Electricity</li>
        </ul>
      </li>
      <li>Chemistry
        <ul>
          <li>Elements</li>
          <li>Reactions</li>
          <li>Organic substances</li>
        </ul>
      </li>
    </ul>
    ```

### Exercise 3 — A 4-column table
Build a table with the columns Name, Age, City, Class and 3 rows of students.

??? success "Solution"
    ```html
    <table>
      <caption>Students in the computer science club</caption>
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Age</th>
          <th scope="col">City</th>
          <th scope="col">Class</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Anna Pop</td>
          <td>13</td>
          <td>Cluj</td>
          <td>7B</td>
        </tr>
        <tr>
          <td>Mike Radu</td>
          <td>14</td>
          <td>Bucharest</td>
          <td>8A</td>
        </tr>
        <tr>
          <td>Elena Ionescu</td>
          <td>12</td>
          <td>Chișinău</td>
          <td>6C</td>
        </tr>
      </tbody>
    </table>
    ```

---

## Mini-project: "School timetable"

Build a table with the weekly timetable: **columns** = the days (Monday–Friday), **rows** = the hours (08:00, 09:00, 10:00, ...).

- Use `<thead>` for the days of the week.
- Use `<tbody>` for the hours and subjects.
- Add a `<caption>` titled "Timetable for class 8A".
- Use `scope="col"` and `scope="row"` correctly.
- For a longer break (e.g. 12:00–13:00), use `colspan="5"` on the "Lunch break" cell.

??? success "Solution"
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>School timetable</title>
    </head>
    <body>
      <h1>Weekly timetable</h1>

      <table>
        <caption>Timetable for class 8A</caption>

        <thead>
          <tr>
            <th scope="col">Hour</th>
            <th scope="col">Monday</th>
            <th scope="col">Tuesday</th>
            <th scope="col">Wednesday</th>
            <th scope="col">Thursday</th>
            <th scope="col">Friday</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <th scope="row">08:00</th>
            <td>Mathematics</td>
            <td>English</td>
            <td>Physics</td>
            <td>French</td>
            <td>Computer Science</td>
          </tr>
          <tr>
            <th scope="row">09:00</th>
            <td>English</td>
            <td>Mathematics</td>
            <td>Chemistry</td>
            <td>History</td>
            <td>Math</td>
          </tr>
          <tr>
            <th scope="row">10:00</th>
            <td>French</td>
            <td>Computer Science</td>
            <td>Biology</td>
            <td>Math</td>
            <td>English</td>
          </tr>
          <tr>
            <th scope="row">11:00</th>
            <td>PE</td>
            <td>Geography</td>
            <td>English</td>
            <td>Physics</td>
            <td>Art</td>
          </tr>
          <tr>
            <th scope="row">12:00</th>
            <td colspan="5">Lunch break</td>
          </tr>
          <tr>
            <th scope="row">13:00</th>
            <td>Art</td>
            <td>Music</td>
            <td>IT Club</td>
            <td>—</td>
            <td>—</td>
          </tr>
        </tbody>
      </table>
    </body>
    </html>
    ```

---

## Summary

- `<ul>` for unordered lists; `<ol>` when order matters.
- Nesting: put the sub-list **inside** an `<li>`.
- Tables = tabular data, **not** for layout.
- Use `<thead>`, `<tbody>`, `<tfoot>` for serious tables.
- `colspan` / `rowspan` for larger cells.
- `<caption>` + `scope` = accessible table.

---

**Next step:** [→ Lesson 04: Forms](04-html-formulare.md)
