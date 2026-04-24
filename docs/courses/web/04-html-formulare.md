---
lesson: 4
tags: [web, html, formulare, input, label, validare, accesibilitate]
summary: Formulare HTML — tipuri de input, label, validare cu atribute, checkbox, radio, select, textarea și butoane.
---

# Lecția 04 · Formulare

!!! tip "Ce vei învăța"
    - Structura de bază `<form>` și diferența `GET` vs `POST`
    - Tipurile comune de `<input>`: text, email, password, number, date...
    - De ce **label** este obligatoriu pentru accesibilitate
    - Validare din HTML (fără JavaScript): `required`, `minlength`, `pattern`
    - Checkbox, radio, select, textarea
    - Butoane `submit`, `reset`, `button`

---

## La ce folosim formularele?

Formularele sunt modul prin care **utilizatorul trimite date**: căutare, login, înregistrare, feedback, comentarii, comandă online. Fără formulare, web-ul ar fi doar de citit.

---

## Structura de bază

```html
<form action="/trimite" method="POST">
  <!-- câmpurile formularului -->
  <button type="submit">Trimite</button>
</form>
```

- `action` — adresa unde se trimit datele (un program pe server).
- `method` — **cum** se trimit: `GET` sau `POST`.

### GET vs POST

| `GET` | `POST` |
|-------|--------|
| Datele apar în URL (`?nume=Ana&varsta=14`) | Datele sunt ascunse în corpul cererii |
| Potrivit pentru **căutare**, filtre | Potrivit pentru **login**, înregistrare, orice date sensibile |
| Limitat ca lungime | Fără limită practică |
| Poate fi pus la favorite | Nu |

**Regulă:** dacă datele ar fi jenante să apară într-un screenshot cu URL-ul — folosește `POST`.

!!! note "Fără server, formularul nu \"face\" nimic"
    În această lecție vei construi aspectul și validarea formularelor. Trimiterea reală către un server o vei putea face cu JavaScript (Lecția 17) sau cu un backend (un alt curs).

---

## Input-uri comune

### `text` — text scurt pe o linie

```html
<input type="text" name="nume" placeholder="Numele tău">
```

### `email` — validează formatul e-mail

```html
<input type="email" name="email" placeholder="ana@exemplu.ro">
```

Browser-ul refuză să trimită dacă valoarea nu seamănă cu un e-mail.

### `password` — ascunde caracterele

```html
<input type="password" name="parola">
```

### `number` — doar numere

```html
<input type="number" name="varsta" min="0" max="120">
```

### `tel` — numere de telefon

```html
<input type="tel" name="telefon" placeholder="+40 712 345 678">
```

Pe mobil, deschide tastatura numerică.

### `date` / `time` — alegere calendar / ceas

```html
<label for="n">Data nașterii:</label>
<input type="date" id="n" name="nastere">

<label for="o">Ora întâlnirii:</label>
<input type="time" id="o" name="ora">
```

### `url` — adrese web

```html
<input type="url" name="site" placeholder="https://...">
```

---

## Label: prietenul invizibil al accesibilității

**Nu ai voie** să pui un input fără un `<label>` asociat. Sunt două variante:

### Varianta 1: `for` + `id`

```html
<label for="nume-input">Nume:</label>
<input type="text" id="nume-input" name="nume">
```

### Varianta 2: label înfășurat

```html
<label>
  Nume:
  <input type="text" name="nume">
</label>
```

!!! tip "De ce contează label?"
    - **Screen reader-e** anunță câmpul: „Nume, câmp text”.
    - Utilizatorul poate da **click pe text** pentru a focusa input-ul (foarte util la checkbox-uri mici).
    - Formularele fără label sunt **inaccesibile** și scad SEO-ul.

---

## Atribute utile pe input

### `placeholder` — text fantomă în câmp

```html
<input type="email" placeholder="ana@exemplu.ro">
```

**Important:** nu înlocuiește `<label>`! Dispare când utilizatorul începe să tasteze.

### `required` — obligatoriu

```html
<input type="text" name="nume" required>
```

Browser-ul oprește trimiterea și afișează un mesaj: „Completați acest câmp”.

### `value` — valoare implicită

```html
<input type="text" name="oras" value="Cluj-Napoca">
```

### `min`, `max` — pentru number/date

```html
<input type="number" name="nota" min="1" max="10">
<input type="date" name="aparitie" min="2000-01-01" max="2030-12-31">
```

### `minlength`, `maxlength` — lungime text

```html
<input type="text" name="nume" minlength="2" maxlength="50">
```

### `pattern` — regex pentru validare custom

```html
<!-- Cod poștal de 6 cifre: -->
<input type="text" name="cod" pattern="[0-9]{6}"
       title="6 cifre, ex: 400001">
```

!!! note "Regex e puternic, dar complicat"
    `pattern="[0-9]{6}"` înseamnă „6 cifre”. Regex-uri mai complexe le vei învăța pe parcurs. `title` apare când utilizatorul introduce greșit.

---

## Checkbox și radio

### Checkbox — selecții multiple

```html
<fieldset>
  <legend>Hobby-uri (poți alege mai multe):</legend>

  <label>
    <input type="checkbox" name="hobby" value="fotbal">
    Fotbal
  </label>

  <label>
    <input type="checkbox" name="hobby" value="muzica">
    Muzică
  </label>

  <label>
    <input type="checkbox" name="hobby" value="desen">
    Desen
  </label>
</fieldset>
```

Toate pot fi bifate simultan. Toate au același `name` — serverul primește o listă cu valorile bifate.

### Radio — o singură selecție

```html
<fieldset>
  <legend>Gen:</legend>

  <label>
    <input type="radio" name="gen" value="feminin">
    Feminin
  </label>

  <label>
    <input type="radio" name="gen" value="masculin">
    Masculin
  </label>

  <label>
    <input type="radio" name="gen" value="alt">
    Alt
  </label>
</fieldset>
```

!!! warning "Grupul radio = același `name`"
    Două radio-uri devin **mutual exclusive** (alegi doar una) **doar dacă au același `name`**. Dacă `name`-urile diferă, ambele pot fi bifate simultan — ceea ce sparge sensul radio-ului.

---

## Textarea — text multi-linie

```html
<label for="mesaj">Mesajul tău:</label>
<textarea id="mesaj" name="mesaj"
          rows="5" cols="40"
          placeholder="Scrie aici..."></textarea>
```

- `rows` — înălțimea în rânduri.
- `cols` — lățimea în caractere.
- **NU e** self-closing: `<textarea>...</textarea>`.

---

## Select — dropdown

```html
<label for="oras">Oraș:</label>
<select id="oras" name="oras">
  <option value="">— alege un oraș —</option>
  <option value="cluj">Cluj-Napoca</option>
  <option value="bucuresti">București</option>
  <option value="chisinau">Chișinău</option>
  <option value="iasi">Iași</option>
</select>
```

- `<option value="x">` — valoarea trimisă la server.
- Textul dintre `<option>` și `</option>` — ce vede utilizatorul.
- `<option value="" disabled selected>` — placeholder care nu e o opțiune validă.

### Selecție multiplă

```html
<select name="limbi" multiple size="4">
  <option>Română</option>
  <option>Engleză</option>
  <option>Franceză</option>
  <option>Germană</option>
</select>
```

Utilizatorul ține `Ctrl` / `Cmd` pentru a selecta multiple.

---

## Butoane

### `<button type="submit">` — trimite formularul

```html
<button type="submit">Trimite</button>
```

### `<button type="reset">` — resetează câmpurile

```html
<button type="reset">Șterge tot</button>
```

### `<button type="button">` — buton care **nu** trimite

```html
<button type="button" onclick="alert('Salut!')">Salut</button>
```

Util pentru butoane cu comportament JavaScript custom.

!!! warning "`type` este important"
    Dacă ai un `<button>` **fără `type`** într-un `<form>`, implicit este `submit` — va trimite formularul la click. Setează mereu `type` explicit.

---

## Gruparea cu `<fieldset>` și `<legend>`

```html
<form>
  <fieldset>
    <legend>Date personale</legend>
    <label>Nume: <input type="text" name="nume"></label>
    <label>Email: <input type="email" name="email"></label>
  </fieldset>

  <fieldset>
    <legend>Preferințe</legend>
    <label><input type="checkbox" name="newsletter"> Vreau newsletter</label>
  </fieldset>

  <button type="submit">Trimite</button>
</form>
```

Browser-ul afișează un cadru cu titlu — structura devine mai clară, mai ales pentru formulare lungi.

---

## Input-uri moderne — pe scurt

```html
<!-- Culoare -->
<input type="color" name="culoare">

<!-- Slider -->
<input type="range" name="nivel" min="0" max="100" value="50">

<!-- Upload fișier -->
<input type="file" name="avatar" accept="image/*">

<!-- Căutare -->
<input type="search" name="q">
```

Fiecare are UX specific pe browser și pe mobil (ex: `color` deschide paleta de culori).

---

## Atenție

Fără JavaScript sau un server, **datele din formular doar se trimit** la URL-ul din `action`. Dacă `action` lipsește, se trimit la aceeași pagină și nu se întâmplă nimic vizibil.

În această lecție lucrăm pe **aspectul și validarea** formularelor. Procesarea datelor o facem în Lecția 17.

---

## Exerciții

### Exercițiu 1 — Formular minim
Fă un formular cu: câmp nume, câmp email, buton Submit.

??? success "Soluție"
    ```html
    <form>
      <label for="n">Nume:</label>
      <input type="text" id="n" name="nume">

      <label for="e">Email:</label>
      <input type="email" id="e" name="email">

      <button type="submit">Trimite</button>
    </form>
    ```

### Exercițiu 2 — Validare
Pe formularul de la Exercițiul 1, fă câmpul **email obligatoriu** și câmpul **nume** cu minim 2 caractere.

??? success "Soluție"
    ```html
    <form>
      <label for="n">Nume:</label>
      <input type="text" id="n" name="nume" required minlength="2">

      <label for="e">Email:</label>
      <input type="email" id="e" name="email" required>

      <button type="submit">Trimite</button>
    </form>
    ```
    Încearcă să lași câmpurile goale — browser-ul va refuza trimiterea.

### Exercițiu 3 — Checkbox + radio
Adaugă un `<fieldset>` cu 4 checkbox-uri pentru hobby-uri și un `<fieldset>` cu 3 radio-uri pentru gen.

??? success "Soluție"
    ```html
    <fieldset>
      <legend>Hobby-uri</legend>
      <label><input type="checkbox" name="hobby" value="sport"> Sport</label>
      <label><input type="checkbox" name="hobby" value="citit"> Citit</label>
      <label><input type="checkbox" name="hobby" value="muzica"> Muzică</label>
      <label><input type="checkbox" name="hobby" value="calatorii"> Călătorii</label>
    </fieldset>

    <fieldset>
      <legend>Gen</legend>
      <label><input type="radio" name="gen" value="f"> Feminin</label>
      <label><input type="radio" name="gen" value="m"> Masculin</label>
      <label><input type="radio" name="gen" value="a"> Alt</label>
    </fieldset>
    ```

---

## Mini-proiect: „Formular de contact”

Fă un formular complet de contact cu:

- Nume (obligatoriu, minim 2 caractere)
- Email (obligatoriu, tip email)
- Telefon (opțional)
- Subiect (select: Feedback / Întrebare / Propunere)
- Mesaj (textarea, obligatoriu)
- Checkbox „Sunt de acord cu termenii” (obligatoriu)
- Butoane Trimite și Resetează

??? success "Soluție"
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Contact</title>
    </head>
    <body>
      <h1>Contactează-ne</h1>

      <form action="#" method="POST">
        <fieldset>
          <legend>Date de contact</legend>

          <p>
            <label for="nume">Nume *</label><br>
            <input type="text" id="nume" name="nume"
                   required minlength="2" maxlength="60">
          </p>

          <p>
            <label for="email">Email *</label><br>
            <input type="email" id="email" name="email" required>
          </p>

          <p>
            <label for="tel">Telefon</label><br>
            <input type="tel" id="tel" name="telefon"
                   placeholder="+40 712 345 678">
          </p>
        </fieldset>

        <fieldset>
          <legend>Mesajul tău</legend>

          <p>
            <label for="subiect">Subiect *</label><br>
            <select id="subiect" name="subiect" required>
              <option value="">— alege —</option>
              <option value="feedback">Feedback</option>
              <option value="intrebare">Întrebare</option>
              <option value="propunere">Propunere</option>
            </select>
          </p>

          <p>
            <label for="mesaj">Mesaj *</label><br>
            <textarea id="mesaj" name="mesaj"
                      rows="6" cols="50" required
                      placeholder="Scrie aici..."></textarea>
          </p>
        </fieldset>

        <p>
          <label>
            <input type="checkbox" name="acord" required>
            Sunt de acord cu termenii și condițiile *
          </label>
        </p>

        <p>
          <button type="submit">Trimite</button>
          <button type="reset">Resetează</button>
        </p>
      </form>
    </body>
    </html>
    ```

---

## Rezumat

- `<form action="..." method="POST">` înconjoară toate câmpurile.
- `<input type="...">` acoperă majoritatea tipurilor de date.
- **Fiecare input trebuie un `<label>`** — accesibilitate + UX.
- `required`, `minlength`, `pattern` = validare gratis din HTML.
- Radio-urile se grupează prin același `name`.
- `<fieldset>` + `<legend>` = secțiuni clare în formulare lungi.

---

**Pasul următor:** [→ Lecția 05: Site multi-pagină](05-html-multi-pagina.md)
