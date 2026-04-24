---
lesson: 4
tags: [web, html, forms, input, label, validation, accessibility]
summary: HTML forms — input types, label, attribute-based validation, checkbox, radio, select, textarea, and buttons.
---

# Lesson 04 · Forms

!!! tip "What you'll learn"
    - The basic `<form>` structure and the `GET` vs `POST` difference
    - Common `<input>` types: text, email, password, number, date...
    - Why **label** is mandatory for accessibility
    - Validation from HTML alone (no JavaScript): `required`, `minlength`, `pattern`
    - Checkbox, radio, select, textarea
    - Buttons `submit`, `reset`, `button`

---

## What are forms for?

Forms are how the **user sends data**: search, login, sign-up, feedback, comments, online ordering. Without forms, the web would be read-only.

---

## Basic structure

```html
<form action="/submit" method="POST">
  <!-- form fields -->
  <button type="submit">Send</button>
</form>
```

- `action` — the address where the data is sent (a program on the server).
- `method` — **how** it is sent: `GET` or `POST`.

### GET vs POST

| `GET` | `POST` |
|-------|--------|
| Data appears in the URL (`?name=Anna&age=14`) | Data is hidden in the body of the request |
| Suitable for **search**, filters | Suitable for **login**, sign-up, any sensitive data |
| Length-limited | No practical limit |
| Can be bookmarked | Cannot |

**Rule:** if the data would be embarrassing to appear in a URL screenshot — use `POST`.

!!! note "Without a server, the form does not actually \"do\" anything"
    In this lesson you'll build the appearance and the validation of forms. Real submission to a server you can do with JavaScript (Lesson 17) or with a backend (a different course).

---

## Common inputs

### `text` — short single-line text

```html
<input type="text" name="name" placeholder="Your name">
```

### `email` — validates email format

```html
<input type="email" name="email" placeholder="anna@example.com">
```

The browser refuses to send if the value doesn't look like an email.

### `password` — hides the characters

```html
<input type="password" name="password">
```

### `number` — numbers only

```html
<input type="number" name="age" min="0" max="120">
```

### `tel` — phone numbers

```html
<input type="tel" name="phone" placeholder="+40 712 345 678">
```

On mobile, opens the numeric keypad.

### `date` / `time` — calendar / clock picker

```html
<label for="b">Date of birth:</label>
<input type="date" id="b" name="birth">

<label for="t">Meeting time:</label>
<input type="time" id="t" name="time">
```

### `url` — web addresses

```html
<input type="url" name="site" placeholder="https://...">
```

---

## Label: accessibility's invisible friend

You're **not allowed** to put an input without an associated `<label>`. There are two options:

### Option 1: `for` + `id`

```html
<label for="name-input">Name:</label>
<input type="text" id="name-input" name="name">
```

### Option 2: wrapped label

```html
<label>
  Name:
  <input type="text" name="name">
</label>
```

!!! tip "Why does label matter?"
    - **Screen readers** announce the field: "Name, text field".
    - The user can **click on the text** to focus the input (very useful for tiny checkboxes).
    - Forms without labels are **inaccessible** and lower SEO.

---

## Useful input attributes

### `placeholder` — ghost text in the field

```html
<input type="email" placeholder="anna@example.com">
```

**Important:** doesn't replace `<label>`! It disappears as soon as the user starts typing.

### `required` — required field

```html
<input type="text" name="name" required>
```

The browser stops the submission and shows a message: "Please fill out this field".

### `value` — default value

```html
<input type="text" name="city" value="Cluj-Napoca">
```

### `min`, `max` — for number/date

```html
<input type="number" name="grade" min="1" max="10">
<input type="date" name="release" min="2000-01-01" max="2030-12-31">
```

### `minlength`, `maxlength` — text length

```html
<input type="text" name="name" minlength="2" maxlength="50">
```

### `pattern` — regex for custom validation

```html
<!-- 6-digit postal code: -->
<input type="text" name="zip" pattern="[0-9]{6}"
       title="6 digits, e.g. 400001">
```

!!! note "Regex is powerful, but tricky"
    `pattern="[0-9]{6}"` means "6 digits". You'll learn more complex regex over time. `title` shows up when the user types something invalid.

---

## Checkbox and radio

### Checkbox — multiple selection

```html
<fieldset>
  <legend>Hobbies (you can pick several):</legend>

  <label>
    <input type="checkbox" name="hobby" value="football">
    Football
  </label>

  <label>
    <input type="checkbox" name="hobby" value="music">
    Music
  </label>

  <label>
    <input type="checkbox" name="hobby" value="drawing">
    Drawing
  </label>
</fieldset>
```

All can be ticked at once. They share the same `name` — the server receives a list of the checked values.

### Radio — single selection

```html
<fieldset>
  <legend>Gender:</legend>

  <label>
    <input type="radio" name="gender" value="female">
    Female
  </label>

  <label>
    <input type="radio" name="gender" value="male">
    Male
  </label>

  <label>
    <input type="radio" name="gender" value="other">
    Other
  </label>
</fieldset>
```

!!! warning "A radio group = the same `name`"
    Two radios become **mutually exclusive** (you pick only one) **only if they share the same `name`**. If the names differ, both can be checked at once — which breaks the meaning of a radio button.

---

## Textarea — multi-line text

```html
<label for="message">Your message:</label>
<textarea id="message" name="message"
          rows="5" cols="40"
          placeholder="Type here..."></textarea>
```

- `rows` — height in lines.
- `cols` — width in characters.
- It's **NOT** self-closing: `<textarea>...</textarea>`.

---

## Select — dropdown

```html
<label for="city">City:</label>
<select id="city" name="city">
  <option value="">— pick a city —</option>
  <option value="cluj">Cluj-Napoca</option>
  <option value="bucharest">Bucharest</option>
  <option value="chisinau">Chișinău</option>
  <option value="iasi">Iași</option>
</select>
```

- `<option value="x">` — the value sent to the server.
- The text between `<option>` and `</option>` — what the user sees.
- `<option value="" disabled selected>` — placeholder that isn't a valid option.

### Multiple selection

```html
<select name="languages" multiple size="4">
  <option>Romanian</option>
  <option>English</option>
  <option>French</option>
  <option>German</option>
</select>
```

The user holds `Ctrl` / `Cmd` to select several.

---

## Buttons

### `<button type="submit">` — submits the form

```html
<button type="submit">Send</button>
```

### `<button type="reset">` — resets the fields

```html
<button type="reset">Clear all</button>
```

### `<button type="button">` — a button that does **not** submit

```html
<button type="button" onclick="alert('Hello!')">Hello</button>
```

Useful for buttons with custom JavaScript behavior.

!!! warning "`type` is important"
    If you have a `<button>` **without `type`** inside a `<form>`, the default is `submit` — it'll submit the form on click. Always set `type` explicitly.

---

## Grouping with `<fieldset>` and `<legend>`

```html
<form>
  <fieldset>
    <legend>Personal details</legend>
    <label>Name: <input type="text" name="name"></label>
    <label>Email: <input type="email" name="email"></label>
  </fieldset>

  <fieldset>
    <legend>Preferences</legend>
    <label><input type="checkbox" name="newsletter"> I want the newsletter</label>
  </fieldset>

  <button type="submit">Send</button>
</form>
```

The browser shows a frame with a title — the structure becomes clearer, especially for long forms.

---

## Modern inputs — in brief

```html
<!-- Color -->
<input type="color" name="color">

<!-- Slider -->
<input type="range" name="level" min="0" max="100" value="50">

<!-- File upload -->
<input type="file" name="avatar" accept="image/*">

<!-- Search -->
<input type="search" name="q">
```

Each has specific UX in browsers and on mobile (e.g. `color` opens the color picker).

---

## Heads up

Without JavaScript or a server, the **form data is just sent** to the URL in `action`. If `action` is missing, it's sent to the same page and nothing visible happens.

In this lesson we work on the **appearance and validation** of forms. We'll process the data in Lesson 17.

---

## Exercises

### Exercise 1 — Minimal form
Build a form with: a name field, an email field, and a Submit button.

??? success "Solution"
    ```html
    <form>
      <label for="n">Name:</label>
      <input type="text" id="n" name="name">

      <label for="e">Email:</label>
      <input type="email" id="e" name="email">

      <button type="submit">Send</button>
    </form>
    ```

### Exercise 2 — Validation
On the form from Exercise 1, make the **email field required** and the **name** field have a minimum of 2 characters.

??? success "Solution"
    ```html
    <form>
      <label for="n">Name:</label>
      <input type="text" id="n" name="name" required minlength="2">

      <label for="e">Email:</label>
      <input type="email" id="e" name="email" required>

      <button type="submit">Send</button>
    </form>
    ```
    Try leaving the fields empty — the browser will refuse to submit.

### Exercise 3 — Checkbox + radio
Add a `<fieldset>` with 4 checkboxes for hobbies and a `<fieldset>` with 3 radios for gender.

??? success "Solution"
    ```html
    <fieldset>
      <legend>Hobbies</legend>
      <label><input type="checkbox" name="hobby" value="sport"> Sport</label>
      <label><input type="checkbox" name="hobby" value="reading"> Reading</label>
      <label><input type="checkbox" name="hobby" value="music"> Music</label>
      <label><input type="checkbox" name="hobby" value="travel"> Travel</label>
    </fieldset>

    <fieldset>
      <legend>Gender</legend>
      <label><input type="radio" name="gender" value="f"> Female</label>
      <label><input type="radio" name="gender" value="m"> Male</label>
      <label><input type="radio" name="gender" value="o"> Other</label>
    </fieldset>
    ```

---

## Mini-project: "Contact form"

Build a complete contact form with:

- Name (required, minimum 2 characters)
- Email (required, email type)
- Phone (optional)
- Subject (select: Feedback / Question / Suggestion)
- Message (textarea, required)
- Checkbox "I agree to the terms" (required)
- Send and Reset buttons

??? success "Solution"
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Contact</title>
    </head>
    <body>
      <h1>Contact us</h1>

      <form action="#" method="POST">
        <fieldset>
          <legend>Contact details</legend>

          <p>
            <label for="name">Name *</label><br>
            <input type="text" id="name" name="name"
                   required minlength="2" maxlength="60">
          </p>

          <p>
            <label for="email">Email *</label><br>
            <input type="email" id="email" name="email" required>
          </p>

          <p>
            <label for="tel">Phone</label><br>
            <input type="tel" id="tel" name="phone"
                   placeholder="+40 712 345 678">
          </p>
        </fieldset>

        <fieldset>
          <legend>Your message</legend>

          <p>
            <label for="subject">Subject *</label><br>
            <select id="subject" name="subject" required>
              <option value="">— pick one —</option>
              <option value="feedback">Feedback</option>
              <option value="question">Question</option>
              <option value="suggestion">Suggestion</option>
            </select>
          </p>

          <p>
            <label for="message">Message *</label><br>
            <textarea id="message" name="message"
                      rows="6" cols="50" required
                      placeholder="Type here..."></textarea>
          </p>
        </fieldset>

        <p>
          <label>
            <input type="checkbox" name="agree" required>
            I agree to the terms and conditions *
          </label>
        </p>

        <p>
          <button type="submit">Send</button>
          <button type="reset">Reset</button>
        </p>
      </form>
    </body>
    </html>
    ```

---

## Summary

- `<form action="..." method="POST">` wraps all fields.
- `<input type="...">` covers most data types.
- **Every input needs a `<label>`** — accessibility + UX.
- `required`, `minlength`, `pattern` = free validation from HTML.
- Radios are grouped through the same `name`.
- `<fieldset>` + `<legend>` = clear sections in long forms.

---

**Next step:** [→ Lesson 05: Multi-page site](05-html-multi-pagina.md)
