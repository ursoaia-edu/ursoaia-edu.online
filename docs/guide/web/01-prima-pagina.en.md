---
lesson: 1
tags: [web, html, vscode, live-server, doctype, utf-8]
summary: Create your first HTML page, understand the minimum structure of an HTML5 document, and establish a save→refresh workflow.
---

# Lesson 01 · Your first page

!!! tip "What you'll learn"
    - How to create an `.html` file and a project folder
    - The **minimum structure** of an HTML5 document
    - What each line of `<head>` and `<body>` is for
    - The workflow: **editor → save → browser**
    - Common beginner errors (special characters, unclosed tags)

---

## Creating the file

Every site starts with a **folder** where you keep your files. On your computer:

1. Create a new folder, for example `my-site` on your Desktop.
2. Open **VS Code** → `File` → `Open Folder...` → choose `my-site`.
3. In VS Code, right-click in the left panel → `New File` → name it **`index.html`**.

!!! warning "The `.html` extension is required"
    If you save the file as `index.txt`, the browser won't know it's a web page — it'll display it as plain text. The name `index` is a convention: the browser automatically loads `index.html` when you open a folder.

---

## Minimum HTML5 structure

Type (or copy) into `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My first page</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <p>This is my first web page.</p>
</body>
</html>
```

Save it (`Ctrl+S`). Let's understand each line.

### Line by line

| Line | What it's for |
|------|---------------|
| `<!DOCTYPE html>` | Tells the browser: "we're using HTML5" (the modern standard). |
| `<html lang="en">` | The document root. `lang="en"` declares the page is in English (useful for search engines and screen readers). |
| `<head>` | Information **about** the page (metadata). Not visible. |
| `<meta charset="UTF-8">` | Character encoding. **Required** for special letters like `é à ñ ç ä`. |
| `<meta name="viewport" ...>` | Makes the page display correctly on phones. |
| `<title>` | The text that appears in the **browser tab** and in Google results. |
| `<body>` | The **visible content** of the page. |
| `<h1>` | Main heading (level 1). |
| `<p>` | A paragraph of text. |

!!! note "Head vs. Body"
    **Head = behind the scenes.** Title, encoding, links to CSS, settings for search engines.

    **Body = the stage.** Everything the user sees: text, images, buttons, forms.

---

## Opening it in the browser

You have two options:

### Simple option (no extensions)
Double-click `index.html` in File Explorer / Finder. It opens in your default browser.

**Drawback:** for every change you have to press `F5` (refresh) manually.

### Recommended option: Live Server

1. In VS Code, install the **Live Server** extension (author: Ritwick Dey).
2. Right-click on `index.html` → `Open with Live Server`.
3. The browser opens automatically at `http://127.0.0.1:5500/index.html`.
4. Now, **every time you save**, the page refreshes itself.

!!! tip "What 127.0.0.1 means"
    `127.0.0.1` is **your computer**. Live Server starts a tiny local server on your computer — only you can access it.

---

## The workflow

```
┌──────────┐      Ctrl+S      ┌──────────┐     reload    ┌──────────┐
│  Editor  │ ───────────────> │   File   │ ────────────> │ Browser  │
│ (VS Code)│                  │ .html    │  (Live Server)│          │
└──────────┘                  └──────────┘               └──────────┘
     ^                                                        │
     │                  "hmm, let me change something"        │
     └────────────────────────────────────────────────────────┘
```

The golden rule: **edit → save → look at the browser**. If you don't see the change, you forgot to save.

---

## HTML comments

A comment is a note for yourself — it **doesn't appear** in the browser:

```html
<!-- This is a note, the browser ignores it -->
<h1>Hello!</h1>
<!-- TODO: add a picture here -->
```

Use comments to explain your sections or to leave reminders.

---

## Indentation

Indentation (the spaces at the start of a line) **doesn't change** how the browser displays the page, but it makes the code **much easier to read** for you and whoever reads it later.

Use **2 or 4 spaces** for each nesting level. VS Code adds them automatically.

```html
<body>
  <main>
    <section>
      <h2>Section title</h2>
      <p>Content...</p>
    </section>
  </main>
</body>
```

---

## Common beginner errors

### 1. Unclosed tags

```html
<!-- Wrong: -->
<h1>Title
<p>Paragraph</p>

<!-- Correct: -->
<h1>Title</h1>
<p>Paragraph</p>
```

### 2. Missing quotes in attributes

```html
<!-- Wrong: -->
<html lang=en>

<!-- Correct: -->
<html lang="en">
```

### 3. Special characters showing as `???` or `Ã®`

You forgot `<meta charset="UTF-8">` in `<head>`. Add it as the **first line in head** and save.

### 4. "Nothing happens on refresh"

Did you save the file? `Ctrl+S`. In VS Code, the tab title shows a `●` when there are unsaved changes.

---

## Exercises

### Exercise 1 — Your personal page
Create `index.html` with the title "My first page" and an `<h1>` containing your name.

??? success "Solution"
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>My first page</title>
    </head>
    <body>
      <h1>Anna Parker</h1>
    </body>
    </html>
    ```

### Exercise 2 — Add content
Below the `<h1>`, add another heading (e.g. "8th grade student") and a descriptive paragraph of 2-3 sentences.

??? success "Solution"
    ```html
    <body>
      <h1>Anna Parker</h1>
      <h2>8th grade student, Cluj-Napoca</h2>
      <p>I love math, books and drawing. I'm learning HTML
         right now because I want to build my own site.</p>
    </body>
    ```

### Exercise 3 — Intentional break
Close `<h1>` with `</h2>` (wrong, on purpose). Save. What do you notice in the browser? Then fix it.

??? success "Solution"
    The browser is **forgiving**: it'll probably display the title anyway, but the page structure will be corrupted. If you have multiple elements, they may show up in odd positions or with the wrong styles. **Lesson learned:** close tags correctly; validators and automated tools will complain.

---

## Mini-project: "About me" page

Build a complete page about yourself containing:

- `<title>` with your name
- An `<h1>` with your name
- A `<p>` with your age and city
- An `<h2>` "Hobbies"
- A `<p>` with 2-3 hobbies

??? success "Solution"
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Mike Johnson – About me</title>
    </head>
    <body>
      <h1>Mike Johnson</h1>
      <p>I'm 14 and I'm from Chișinău.</p>

      <h2>Hobbies</h2>
      <p>I like football, programming and building things
         out of Lego. Recently I started experimenting with Arduino.</p>
    </body>
    </html>
    ```

---

## Summary

- Every HTML5 page starts with `<!DOCTYPE html>`.
- `<head>` = metadata (invisible), `<body>` = visible content.
- `<meta charset="UTF-8">` is **required** for non-ASCII characters.
- `<title>` appears in the browser tab.
- Workflow: **editor → save → browser** (with Live Server the reload is automatic).
- Always close your tags and use consistent indentation.

---

**Next step:** [→ Lesson 02: HTML – the basic tags](02-html-bazele.md)
