---
lesson: 17
tags: [javascript, forms, validation, events, form, input]
summary: Validate forms in JavaScript — custom error messages and clear feedback for the user.
---

# Lesson 17 · Forms with JavaScript validation

!!! tip "What you'll learn"
    - How to listen for the `submit` event and stop the page reload
    - How to read values from `<input>`, `<textarea>`, `<select>`, checkbox
    - How to display **error messages** below each field
    - How to write combined validations (minimum length, email format, range)
    - How to use the **HTML5 Validation API** (`checkValidity`, `validity`)

---

## Why JavaScript validation?

HTML5 already has native validation:

```html
<input type="email" required minlength="3" maxlength="50" pattern="[a-z]+" />
```

It's useful, but limited:

- You can't combine complex conditions (e.g. "the age must be between 10 and 18, AND if it's under 14, the parent must be in the list").
- Native messages are in the browser's language and you can't style them.
- For good UX you need feedback **as the user types**.

!!! warning "Client validation is NOT enough"
    Browser JS validation can be bypassed (the user can delete your script from DevTools). **The server must re-validate** all received data. In this guide we deal with UX, not security.

---

## Listening for submit

```html
<form id="contact-form">
  <input name="name" />
  <button type="submit">Send</button>
</form>
```

```js
const form = document.getElementById("contact-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();   // stop the page reload
  // validate, send with fetch, show confirmation, etc.
});
```

**Without `preventDefault()`**, the browser submits the form to the URL in `action` and reloads the page — you lose control.

---

## Reading values

### Text input

```js
const inputName = document.getElementById("name");
console.log(inputName.value);   // "Ana"
```

### Checkbox

```js
const consent = document.getElementById("terms-consent");
console.log(consent.checked);   // true / false
```

### Radio

```js
const selectedRadio = document.querySelector('input[name="gender"]:checked');
console.log(selectedRadio?.value);   // "M" / "F" / undefined
```

### Select

```js
const grade = document.getElementById("grade");
console.log(grade.value);   // value of the selected option
```

### Textarea

```js
const message = document.getElementById("message");
console.log(message.value);
```

### `FormData` — shortcut

Instead of reading each field separately:

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const data = new FormData(form);
  console.log(data.get("name"));
  console.log(data.get("email"));

  // or all at once as an object
  const obj = Object.fromEntries(data);
  console.log(obj);
});
```

Each `<input name="...">` becomes a key. Super useful.

---

## Common validations

### Empty field

```js
if (!input.value.trim()) {
  // show error "required field"
}
```

`trim()` removes leading/trailing spaces — a user typing `"   "` has an "empty" field.

### Minimum / maximum length

```js
if (input.value.trim().length < 3) {
  // "too short"
}

if (input.value.length > 200) {
  // "too long"
}
```

### Valid email (simple)

A complete regex is complicated. For beginners, check something basic:

```js
const email = input.value.trim();
if (!email.includes("@") || !email.includes(".")) {
  // "invalid format"
}
```

Or use `type="email"` + `checkValidity()` (see below).

### Number in range

```js
const age = Number(input.value);
if (Number.isNaN(age) || age < 10 || age > 18) {
  // "age must be between 10 and 18"
}
```

### Required checkbox

```js
if (!consent.checked) {
  // "you must accept the terms"
}
```

---

## Displaying errors

**Strategy:** below each input, you put a `<span class="error">` that displays the message when needed.

```html
<label for="email">Email:</label>
<input id="email" name="email" />
<span class="error" id="err-email"></span>
```

```css
.error {
  color: #dc2626;
  font-size: 0.85rem;
  display: block;
  min-height: 1rem;
}

input.invalid {
  border: 2px solid #dc2626;
}
```

```js
const email = document.getElementById("email");
const errEmail = document.getElementById("err-email");

// Show error
errEmail.textContent = "Invalid email";
email.classList.add("invalid");

// Clear when the user starts to correct
email.addEventListener("input", () => {
  errEmail.textContent = "";
  email.classList.remove("invalid");
});
```

---

## Common validation pattern

Separate **validation** from **submission**:

```js
const form = document.getElementById("form");
const inputName = document.getElementById("name");
const inputEmail = document.getElementById("email");
const errName = document.getElementById("err-name");
const errEmail = document.getElementById("err-email");

// Check all fields, return true if everything is OK
const isValid = () => {
  let valid = true;

  // Reset errors
  errName.textContent = "";
  errEmail.textContent = "";
  inputName.classList.remove("invalid");
  inputEmail.classList.remove("invalid");

  // Name: minimum 2 characters
  if (inputName.value.trim().length < 2) {
    errName.textContent = "Name must have at least 2 characters.";
    inputName.classList.add("invalid");
    valid = false;
  }

  // Email: contains @
  if (!inputEmail.value.includes("@")) {
    errEmail.textContent = "Invalid email.";
    inputEmail.classList.add("invalid");
    valid = false;
  }

  return valid;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (isValid()) {
    alert("Form sent!");
    form.reset();
  }
});
```

---

## HTML5 Validation API (optional)

JS exposes the HTML5 validation state:

```js
input.checkValidity();   // true / false

input.validity.valueMissing;   // true if required and empty
input.validity.tooShort;        // below minlength
input.validity.tooLong;         // above maxlength
input.validity.typeMismatch;    // doesn't match type (email, url)
input.validity.patternMismatch; // doesn't match pattern
input.validity.rangeUnderflow;  // below min
input.validity.rangeOverflow;   // above max
```

Useful to reuse HTML5 validation and put your own messages:

```js
if (inputEmail.validity.valueMissing) {
  errEmail.textContent = "Email is required.";
} else if (inputEmail.validity.typeMismatch) {
  errEmail.textContent = "Email format is not correct.";
}
```

---

## Exercises

### Exercise 1 — Name minimum 2 characters
Form with a single input `<input id="name">` and a button. On submit, check that the name has at least 2 characters. Show an error below the input.

??? success "Solution"
    ```html
    <form id="f">
      <input id="name" />
      <span id="err" class="error"></span>
      <button>Send</button>
    </form>
    ```

    ```js
    const f = document.getElementById("f");
    const name = document.getElementById("name");
    const err = document.getElementById("err");

    f.addEventListener("submit", (e) => {
      e.preventDefault();
      if (name.value.trim().length < 2) {
        err.textContent = "The name is too short.";
      } else {
        err.textContent = "";
        alert("OK!");
      }
    });
    ```

### Exercise 2 — Email with @
An email input. On submit, check that the value contains `@` and at least one `.`.

??? success "Solution"
    ```js
    const val = email.value.trim();
    if (!val.includes("@") || !val.includes(".")) {
      err.textContent = "Invalid email format.";
    }
    ```

### Exercise 3 — Age in range
A number input for age. On submit, check that it's between 18 and 99.

??? success "Solution"
    ```js
    const n = Number(age.value);
    if (Number.isNaN(n) || n < 18 || n > 99) {
      err.textContent = "Age must be between 18 and 99.";
    }
    ```

### Exercise 4 — Show the collected data
On valid submit, show in a `<div>` all the values from the form (use `FormData`).

??? success "Solution"
    ```js
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const obj = Object.fromEntries(data);

      const summary = document.getElementById("summary");
      summary.textContent = JSON.stringify(obj, null, 2);
    });
    ```

---

## Mini-project: Computer Science Club registration form

Complete registration form for the Computer Science Club, with validation for all fields.

**Fields:**

- **Name** (minimum 2 characters, required)
- **Email** (contains `@` and `.`, required)
- **Age** (between 10 and 18, required)
- **Grade** (select, required)
- **Message** (textarea, minimum 10 characters)
- **Terms consent** (checkbox, required)

On valid submit, show a success message with the summary.

**Complete code:**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Register for the Computer Science Club</title>
    <script src="app.js" defer></script>
    <style>
      body {
        font-family: sans-serif;
        max-width: 500px;
        margin: 2rem auto;
        padding: 1rem;
      }
      label { display: block; margin-top: 1rem; font-weight: bold; }
      input, select, textarea {
        width: 100%;
        padding: 0.5rem;
        margin-top: 0.25rem;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        font-size: 1rem;
      }
      .error {
        color: #dc2626;
        font-size: 0.85rem;
        display: block;
        min-height: 1rem;
        margin-top: 0.25rem;
      }
      input.invalid, select.invalid, textarea.invalid {
        border-color: #dc2626;
      }
      button {
        margin-top: 1rem;
        padding: 0.75rem 1.5rem;
        background: #2563eb;
        color: white;
        border: none;
        border-radius: 6px;
        font-size: 1rem;
        cursor: pointer;
      }
      #success {
        margin-top: 1rem;
        padding: 1rem;
        background: #dcfce7;
        border: 1px solid #16a34a;
        border-radius: 6px;
        display: none;
      }
    </style>
  </head>
  <body>
    <h1>Registration — Computer Science Club</h1>

    <form id="registration">
      <label for="name">Full name</label>
      <input id="name" name="name" />
      <span class="error" id="err-name"></span>

      <label for="email">Email</label>
      <input id="email" name="email" type="email" />
      <span class="error" id="err-email"></span>

      <label for="age">Age</label>
      <input id="age" name="age" type="number" />
      <span class="error" id="err-age"></span>

      <label for="grade">Grade</label>
      <select id="grade" name="grade">
        <option value="">— choose —</option>
        <option value="5">Grade 5</option>
        <option value="6">Grade 6</option>
        <option value="7">Grade 7</option>
        <option value="8">Grade 8</option>
        <option value="9">Grade 9</option>
      </select>
      <span class="error" id="err-grade"></span>

      <label for="message">Why do you want to register?</label>
      <textarea id="message" name="message" rows="4"></textarea>
      <span class="error" id="err-message"></span>

      <label>
        <input id="consent" name="consent" type="checkbox" style="width:auto" />
        I agree to the club's rules.
      </label>
      <span class="error" id="err-consent"></span>

      <button type="submit">Submit registration</button>
    </form>

    <div id="success"></div>
  </body>
</html>
```

```js
const form = document.getElementById("registration");
const success = document.getElementById("success");

// Helper: show / clear an error
const setError = (input, errSpan, message) => {
  if (message) {
    errSpan.textContent = message;
    input.classList.add("invalid");
  } else {
    errSpan.textContent = "";
    input.classList.remove("invalid");
  }
};

// Full validation — returns true if everything is OK
const validate = () => {
  let valid = true;

  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const age = document.getElementById("age");
  const grade = document.getElementById("grade");
  const message = document.getElementById("message");
  const consent = document.getElementById("consent");

  // Name
  if (name.value.trim().length < 2) {
    setError(name, document.getElementById("err-name"),
              "Name must have at least 2 characters.");
    valid = false;
  } else {
    setError(name, document.getElementById("err-name"), "");
  }

  // Email
  const emailVal = email.value.trim();
  if (!emailVal.includes("@") || !emailVal.includes(".")) {
    setError(email, document.getElementById("err-email"),
              "Invalid email.");
    valid = false;
  } else {
    setError(email, document.getElementById("err-email"), "");
  }

  // Age
  const n = Number(age.value);
  if (Number.isNaN(n) || n < 10 || n > 18) {
    setError(age, document.getElementById("err-age"),
              "Age must be between 10 and 18.");
    valid = false;
  } else {
    setError(age, document.getElementById("err-age"), "");
  }

  // Grade
  if (!grade.value) {
    setError(grade, document.getElementById("err-grade"),
              "Choose a grade.");
    valid = false;
  } else {
    setError(grade, document.getElementById("err-grade"), "");
  }

  // Message
  if (message.value.trim().length < 10) {
    setError(message, document.getElementById("err-message"),
              "Message must have at least 10 characters.");
    valid = false;
  } else {
    setError(message, document.getElementById("err-message"), "");
  }

  // Consent
  if (!consent.checked) {
    document.getElementById("err-consent").textContent =
      "You must accept the rules.";
    valid = false;
  } else {
    document.getElementById("err-consent").textContent = "";
  }

  return valid;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (!validate()) return;

  // Collect data with FormData
  const data = new FormData(form);
  const obj = Object.fromEntries(data);

  // Show summary
  success.style.display = "block";
  success.innerHTML = `
    <strong>Registration submitted successfully!</strong><br>
    Name: ${obj.name}<br>
    Email: ${obj.email}<br>
    Age: ${obj.age}, Grade: ${obj.grade}<br>
    Message: ${obj.message}
  `;

  form.reset();
});
```

---

## Summary

- Listen for `submit` on `<form>` and call **`e.preventDefault()`** to stop the reload.
- Read values with `.value` / `.checked`, or use **`FormData`** for the whole form at once.
- Separate **validation** (function `isValid()`) from **submission** — it's cleaner and more testable.
- Show errors below each field, with `textContent` and a CSS class `.invalid`.
- The HTML5 Validation API (`checkValidity`, `validity.*`) gives you built-in validation that you can complement.
- **Remember:** the server must re-validate everything — the browser is just for UX.

---

**Next step:** [→ Lesson 18: Fetch and APIs](18-js-fetch-api.md)
