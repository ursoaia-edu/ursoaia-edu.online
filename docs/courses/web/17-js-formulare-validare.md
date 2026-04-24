---
lesson: 17
tags: [javascript, formulare, validare, evenimente, form, input]
summary: Validează formularele în JavaScript — mesaje de eroare personalizate și feedback clar pentru utilizator.
---

# Lecția 17 · Formulare cu validare JavaScript

!!! tip "Ce vei învăța"
    - Cum asculți evenimentul `submit` și oprești reîncărcarea paginii
    - Cum citești valorile din `<input>`, `<textarea>`, `<select>`, checkbox
    - Cum afișezi **mesaje de eroare** sub fiecare câmp
    - Cum scrii validări combinate (lungime minimă, format email, interval)
    - Cum folosești **HTML5 Validation API** (`checkValidity`, `validity`)

---

## De ce validare în JavaScript?

HTML5 are deja validare nativă:

```html
<input type="email" required minlength="3" maxlength="50" pattern="[a-z]+" />
```

E utilă, dar limitată:

- Nu poți combina condiții complexe (ex. „vârsta trebuie să fie între 10 și 18, ȘI dacă e sub 14, părintele trebuie să fie în listă”).
- Mesajele native sunt în limba browser-ului și nu le poți stiliza.
- Pentru UX bun ai nevoie de feedback **pe măsură ce utilizatorul scrie**.

!!! warning "Validarea în client NU e suficientă"
    Validarea JS din browser poate fi ocolită (utilizatorul poate șterge scriptul tău din DevTools). **Serverul trebuie să valideze din nou** toate datele primite. În acest ghid ne ocupăm de UX, nu de securitate.

---

## Ascultarea submit-ului

```html
<form id="contact-form">
  <input name="nume" />
  <button type="submit">Trimite</button>
</form>
```

```js
const form = document.getElementById("contact-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();   // oprește reîncărcarea paginii
  // validează, trimite cu fetch, afișează confirmare, etc.
});
```

**Fără `preventDefault()`**, browserul trimite formularul către URL-ul din `action` și reîncarcă pagina — pierzi controlul.

---

## Citirea valorilor

### Input text

```js
const inputNume = document.getElementById("nume");
console.log(inputNume.value);   // "Ana"
```

### Checkbox

```js
const acord = document.getElementById("acord-termeni");
console.log(acord.checked);   // true / false
```

### Radio

```js
const radioSelectat = document.querySelector('input[name="gen"]:checked');
console.log(radioSelectat?.value);   // "M" / "F" / undefined
```

### Select

```js
const clasa = document.getElementById("clasa");
console.log(clasa.value);   // valoarea option-ului selectat
```

### Textarea

```js
const mesaj = document.getElementById("mesaj");
console.log(mesaj.value);
```

### `FormData` — shortcut

În loc să citești fiecare câmp separat:

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const data = new FormData(form);
  console.log(data.get("nume"));
  console.log(data.get("email"));

  // sau toate deodată ca obiect
  const obj = Object.fromEntries(data);
  console.log(obj);
});
```

Fiecare `<input name="...">` devine o cheie. Super util.

---

## Validări comune

### Câmp gol

```js
if (!input.value.trim()) {
  // arată eroare "câmp obligatoriu"
}
```

`trim()` elimină spațiile de la capete — un utilizator care scrie `"   "` are un câmp „gol”.

### Lungime minimă / maximă

```js
if (input.value.trim().length < 3) {
  // "prea scurt"
}

if (input.value.length > 200) {
  // "prea lung"
}
```

### Email valid (simplu)

Un regex complet e complicat. Pentru începători, verifică ceva de bază:

```js
const email = input.value.trim();
if (!email.includes("@") || !email.includes(".")) {
  // "format invalid"
}
```

Sau folosește `type="email"` + `checkValidity()` (vezi mai jos).

### Număr în interval

```js
const varsta = Number(input.value);
if (Number.isNaN(varsta) || varsta < 10 || varsta > 18) {
  // "vârsta trebuie să fie între 10 și 18"
}
```

### Checkbox obligatoriu

```js
if (!acord.checked) {
  // "trebuie să accepți termenii"
}
```

---

## Afișarea erorilor

**Strategia:** sub fiecare input, pui un `<span class="eroare">` care afișează mesajul când e cazul.

```html
<label for="email">Email:</label>
<input id="email" name="email" />
<span class="eroare" id="err-email"></span>
```

```css
.eroare {
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

// Afișează eroare
errEmail.textContent = "Email invalid";
email.classList.add("invalid");

// Curăță când utilizatorul începe să corecteze
email.addEventListener("input", () => {
  errEmail.textContent = "";
  email.classList.remove("invalid");
});
```

---

## Pattern comun pentru validare

Separă **validarea** de **trimitere**:

```js
const form = document.getElementById("form");
const inputNume = document.getElementById("nume");
const inputEmail = document.getElementById("email");
const errNume = document.getElementById("err-nume");
const errEmail = document.getElementById("err-email");

// Verifică toate câmpurile, returnează true dacă totul e OK
const esteValid = () => {
  let valid = true;

  // Reset erori
  errNume.textContent = "";
  errEmail.textContent = "";
  inputNume.classList.remove("invalid");
  inputEmail.classList.remove("invalid");

  // Nume: minim 2 caractere
  if (inputNume.value.trim().length < 2) {
    errNume.textContent = "Numele trebuie să aibă minim 2 caractere.";
    inputNume.classList.add("invalid");
    valid = false;
  }

  // Email: conține @
  if (!inputEmail.value.includes("@")) {
    errEmail.textContent = "Email invalid.";
    inputEmail.classList.add("invalid");
    valid = false;
  }

  return valid;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (esteValid()) {
    alert("Formular trimis!");
    form.reset();
  }
});
```

---

## HTML5 Validation API (opțional)

JS expune starea de validare HTML5:

```js
input.checkValidity();   // true / false

input.validity.valueMissing;   // true dacă e required și e gol
input.validity.tooShort;        // sub minlength
input.validity.tooLong;         // peste maxlength
input.validity.typeMismatch;    // nu se potrivește cu type (email, url)
input.validity.patternMismatch; // nu se potrivește cu pattern
input.validity.rangeUnderflow;  // sub min
input.validity.rangeOverflow;   // peste max
```

Util ca să reutilizezi validarea HTML5 și să pui mesaje proprii:

```js
if (inputEmail.validity.valueMissing) {
  errEmail.textContent = "Email-ul e obligatoriu.";
} else if (inputEmail.validity.typeMismatch) {
  errEmail.textContent = "Formatul email-ului nu e corect.";
}
```

---

## Exerciții

### Exercițiu 1 — Nume minim 2 caractere
Formular cu un singur input `<input id="nume">` și un buton. La submit, verifică că numele are minim 2 caractere. Afișează eroare sub input.

??? success "Soluție"
    ```html
    <form id="f">
      <input id="nume" />
      <span id="err" class="eroare"></span>
      <button>Trimite</button>
    </form>
    ```

    ```js
    const f = document.getElementById("f");
    const nume = document.getElementById("nume");
    const err = document.getElementById("err");

    f.addEventListener("submit", (e) => {
      e.preventDefault();
      if (nume.value.trim().length < 2) {
        err.textContent = "Numele e prea scurt.";
      } else {
        err.textContent = "";
        alert("OK!");
      }
    });
    ```

### Exercițiu 2 — Email cu @
Un input de email. La submit, verifică că valoarea conține `@` și cel puțin un `.`.

??? success "Soluție"
    ```js
    const val = email.value.trim();
    if (!val.includes("@") || !val.includes(".")) {
      err.textContent = "Format de email invalid.";
    }
    ```

### Exercițiu 3 — Vârstă în interval
Input de tip number pentru vârstă. La submit, verifică că e între 18 și 99.

??? success "Soluție"
    ```js
    const n = Number(varsta.value);
    if (Number.isNaN(n) || n < 18 || n > 99) {
      err.textContent = "Vârsta trebuie să fie între 18 și 99.";
    }
    ```

### Exercițiu 4 — Afișează datele colectate
La submit valid, afișează într-un `<div>` toate valorile din formular (folosește `FormData`).

??? success "Soluție"
    ```js
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const obj = Object.fromEntries(data);

      const rezumat = document.getElementById("rezumat");
      rezumat.textContent = JSON.stringify(obj, null, 2);
    });
    ```

---

## Mini-proiect: Formular de înscriere la cerc

Formular complet de înscriere la cercul de informatică, cu validare pentru toate câmpurile.

**Câmpuri:**

- **Nume** (minim 2 caractere, obligatoriu)
- **Email** (conține `@` și `.`, obligatoriu)
- **Vârstă** (între 10 și 18, obligatoriu)
- **Clasa** (select, obligatoriu)
- **Mesaj** (textarea, minim 10 caractere)
- **Acord termeni** (checkbox, obligatoriu)

La submit valid, afișează un mesaj de succes cu rezumatul.

**Cod complet:**

```html
<!DOCTYPE html>
<html lang="ro">
  <head>
    <meta charset="UTF-8" />
    <title>Înscriere la cercul de informatică</title>
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
      .eroare {
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
      #succes {
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
    <h1>Înscriere — Cercul de Informatică</h1>

    <form id="inscriere">
      <label for="nume">Nume complet</label>
      <input id="nume" name="nume" />
      <span class="eroare" id="err-nume"></span>

      <label for="email">Email</label>
      <input id="email" name="email" type="email" />
      <span class="eroare" id="err-email"></span>

      <label for="varsta">Vârsta</label>
      <input id="varsta" name="varsta" type="number" />
      <span class="eroare" id="err-varsta"></span>

      <label for="clasa">Clasa</label>
      <select id="clasa" name="clasa">
        <option value="">— alege —</option>
        <option value="5">Clasa a V-a</option>
        <option value="6">Clasa a VI-a</option>
        <option value="7">Clasa a VII-a</option>
        <option value="8">Clasa a VIII-a</option>
        <option value="9">Clasa a IX-a</option>
      </select>
      <span class="eroare" id="err-clasa"></span>

      <label for="mesaj">De ce vrei să te înscrii?</label>
      <textarea id="mesaj" name="mesaj" rows="4"></textarea>
      <span class="eroare" id="err-mesaj"></span>

      <label>
        <input id="acord" name="acord" type="checkbox" style="width:auto" />
        Sunt de acord cu regulamentul cercului.
      </label>
      <span class="eroare" id="err-acord"></span>

      <button type="submit">Trimite înscrierea</button>
    </form>

    <div id="succes"></div>
  </body>
</html>
```

```js
const form = document.getElementById("inscriere");
const succes = document.getElementById("succes");

// Helper: afișează / curăță o eroare
const setEroare = (input, errSpan, mesaj) => {
  if (mesaj) {
    errSpan.textContent = mesaj;
    input.classList.add("invalid");
  } else {
    errSpan.textContent = "";
    input.classList.remove("invalid");
  }
};

// Validare completă — returnează true dacă totul e OK
const valideaza = () => {
  let valid = true;

  const nume = document.getElementById("nume");
  const email = document.getElementById("email");
  const varsta = document.getElementById("varsta");
  const clasa = document.getElementById("clasa");
  const mesaj = document.getElementById("mesaj");
  const acord = document.getElementById("acord");

  // Nume
  if (nume.value.trim().length < 2) {
    setEroare(nume, document.getElementById("err-nume"),
              "Numele trebuie să aibă minim 2 caractere.");
    valid = false;
  } else {
    setEroare(nume, document.getElementById("err-nume"), "");
  }

  // Email
  const emailVal = email.value.trim();
  if (!emailVal.includes("@") || !emailVal.includes(".")) {
    setEroare(email, document.getElementById("err-email"),
              "Email invalid.");
    valid = false;
  } else {
    setEroare(email, document.getElementById("err-email"), "");
  }

  // Vârstă
  const n = Number(varsta.value);
  if (Number.isNaN(n) || n < 10 || n > 18) {
    setEroare(varsta, document.getElementById("err-varsta"),
              "Vârsta trebuie să fie între 10 și 18.");
    valid = false;
  } else {
    setEroare(varsta, document.getElementById("err-varsta"), "");
  }

  // Clasă
  if (!clasa.value) {
    setEroare(clasa, document.getElementById("err-clasa"),
              "Alege o clasă.");
    valid = false;
  } else {
    setEroare(clasa, document.getElementById("err-clasa"), "");
  }

  // Mesaj
  if (mesaj.value.trim().length < 10) {
    setEroare(mesaj, document.getElementById("err-mesaj"),
              "Mesajul trebuie să aibă minim 10 caractere.");
    valid = false;
  } else {
    setEroare(mesaj, document.getElementById("err-mesaj"), "");
  }

  // Acord
  if (!acord.checked) {
    document.getElementById("err-acord").textContent =
      "Trebuie să accepți regulamentul.";
    valid = false;
  } else {
    document.getElementById("err-acord").textContent = "";
  }

  return valid;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();

  if (!valideaza()) return;

  // Colectează datele cu FormData
  const data = new FormData(form);
  const obj = Object.fromEntries(data);

  // Afișează rezumat
  succes.style.display = "block";
  succes.innerHTML = `
    <strong>Înscriere trimisă cu succes!</strong><br>
    Nume: ${obj.nume}<br>
    Email: ${obj.email}<br>
    Vârsta: ${obj.varsta}, Clasa: ${obj.clasa}<br>
    Mesaj: ${obj.mesaj}
  `;

  form.reset();
});
```

---

## Rezumat

- Ascultă `submit` pe `<form>` și apelează **`e.preventDefault()`** ca să oprești reîncărcarea.
- Citește valorile cu `.value` / `.checked`, sau folosește **`FormData`** pentru tot formularul deodată.
- Separă **validarea** (funcție `esteValid()`) de **trimitere** — e mai curat și mai testabil.
- Afișează erori sub fiecare câmp, cu `textContent` și o clasă CSS `.invalid`.
- HTML5 Validation API (`checkValidity`, `validity.*`) îți oferă validare built-in pe care o poți completa.
- **Amintește-ți:** serverul trebuie să revalideze tot — browserul e doar pentru UX.

---

**Pasul următor:** [→ Lecția 18: Fetch și API-uri](18-js-fetch-api.md)
