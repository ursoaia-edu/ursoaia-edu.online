---
lesson: 11
tags: [javascript, introducere, console, devtools, script]
summary: Primii pași în JavaScript — cum incluzi scripturi în pagină și cum folosești DevTools.
---

# Lecția 11 · JavaScript: introducere

!!! tip "Ce vei învăța"
    - Ce este JavaScript și unde rulează
    - Cele trei moduri de a include JS într-o pagină HTML
    - Cum folosești `console.log()` și DevTools Console
    - Funcții de bază: `alert`, `prompt`, `confirm`
    - Cum citești erorile din consolă

---

## Ce este JavaScript?

**JavaScript** (JS) este limbajul care **aduce la viață** paginile web. Dacă HTML-ul este „scheletul” și CSS-ul este „pielea”, JS-ul este „mușchiul” — el face paginile să reacționeze la clickuri, să valideze formulare, să încarce date din rețea și să se actualizeze fără reîncărcare.

A fost creat în **1995** de Brendan Eich (la Netscape) în doar **10 zile**. Numele „JavaScript” este pur marketing — **NU are nicio legătură cu limbajul Java**. E ca și cum ai compara „ham” (șuncă) cu „hamster”.

Astăzi, JS rulează pe **aproape orice browser modern** și este unul dintre cele mai populare limbaje din lume.

---

## Unde rulează JavaScript?

JS poate rula în două locuri principale:

- **În browser (client-side)** — ce învățăm aici. Codul rulează pe calculatorul vizitatorului.
- **Pe server (Node.js)** — vom discuta mai târziu. Codul rulează pe un server.

În această secțiune a ghidului ne concentrăm pe JS în browser.

---

## Trei moduri de a include JS

### 1. Inline, în atribut HTML (EVITĂ)

```html
<button onclick="alert('salut')">Apasă-mă</button>
```

Funcționează, dar amestecă logica cu structura și devine imposibil de menținut pentru pagini mari. **Nu folosi acest stil** în proiecte reale.

### 2. În HTML, cu tag `<script>`

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Salut!</h1>
    <script>
      console.log("Salut din script intern!");
    </script>
  </body>
</html>
```

Util pentru teste rapide, dar codul se amestecă cu HTML-ul.

### 3. Fișier JS extern (RECOMANDAT)

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Prima mea pagină cu JS</title>
    <script src="app.js" defer></script>
  </head>
  <body>
    <h1>Salut!</h1>
  </body>
</html>
```

Și fișierul `app.js`:

```js
// Primul meu cod JavaScript
console.log("Salut, lume!");
```

!!! tip "Ce face `defer`?"
    Fără `defer`, browserul descarcă și rulează scriptul **imediat**, oprind parsarea HTML. Cu `defer`, browserul **așteaptă** să termine de parsat HTML-ul, apoi rulează scriptul. Rezultat: pagina se încarcă mai rapid și scriptul găsește toate elementele deja create.

---

## Unde pui `<script>`?

Există două locuri bune:

- **În `<head>` cu `defer`** — curat, recomandat.
- **La sfârșitul `<body>`** — alternativă clasică (fără `defer`), tot funcționează pentru că HTML-ul de deasupra e deja parsat.

```html
<!-- Varianta 1: în head cu defer -->
<head>
  <script src="app.js" defer></script>
</head>

<!-- Varianta 2: la sfârșitul body -->
<body>
  <!-- ... conținut ... -->
  <script src="app.js"></script>
</body>
```

---

## Primul tău cod JS

Cea mai simplă instrucțiune: afișare în consolă.

```js
console.log("Salut, lume!");
console.log("Am învățat JavaScript!");
```

`console.log(...)` nu apare pe pagină — apare în **DevTools Console**.

---

## DevTools Console

Fiecare browser modern are un set de unelte pentru dezvoltatori numite **DevTools**. Le deschizi cu:

- **F12** (pe majoritatea browserelor)
- **Ctrl + Shift + I** (Windows / Linux)
- **Cmd + Option + I** (macOS)
- Click dreapta pe pagină → **Inspect** / **Inspectează**

Apoi dă click pe tab-ul **Console**.

În Console:

- Vezi tot ce ai scris cu `console.log(...)`.
- Poți tasta **direct comenzi JS** și apăsa Enter.

Încearcă să tastezi aceste comenzi în Console:

```js
2 + 2                    // 4
"Ana".toUpperCase()      // "ANA"
Math.random()            // un număr aleatoriu între 0 și 1
new Date()               // data și ora curentă
```

---

## Alte funcții utile

### `alert()` — popup informativ

```js
alert("Bună ziua!");
```

Deschide o fereastră popup cu un mesaj. Utilă pentru debug rapid, **iritantă pentru utilizator** — evit-o în aplicații reale.

### `prompt()` — cere input

```js
const nume = prompt("Cum te cheamă?");
console.log("Salut,", nume);
```

Returnează un **string** (sau `null` dacă utilizatorul apasă Cancel).

### `confirm()` — întreabă da / nu

```js
const sigur = confirm("Sigur vrei să continui?");
console.log(sigur);   // true sau false
```

### Variante de `console`

```js
console.log("mesaj normal");
console.warn("avertisment galben");
console.error("eroare roșie");
console.info("info");
```

Fiecare apare cu o culoare / iconiță diferită în Console.

---

## Citirea erorilor

Când ceva nu merge, Console-ul îți afișează **tipul erorii** și **linia** pe care a apărut:

```text
Uncaught ReferenceError: conzole is not defined
    at app.js:3
```

Tipuri frecvente:

- **`ReferenceError`** — ai folosit un nume care nu există (ex. `conzole` în loc de `console`).
- **`TypeError`** — ai încercat o operație nepermisă pe un tip (ex. `null.length`).
- **`SyntaxError`** — ai scris cod care nu respectă gramatica JS (paranteză lipsă, ghilimea nenchisă).

!!! warning "Citește mesajul de eroare!"
    Mulți începători ignoră mesajul și se uită direct în cod. Mesajul îți spune **unde** și **ce** s-a stricat — e primul loc unde trebuie să te uiți.

---

## Comentarii în JS

```js
// Acesta este un comentariu pe o singură linie

/*
   Acesta este un comentariu
   pe mai multe linii.
*/

const pi = 3.14;   // poți pune și la capăt de linie
```

Comentariile nu sunt executate — sunt doar pentru tine și pentru colegii care citesc codul.

---

## Exerciții

### Exercițiu 1 — Prima pagină cu JS
Creează un folder nou cu două fișiere: `index.html` și `app.js`. Leagă-le corect și afișează `"merge!"` în Console.

??? success "Soluție"
    `index.html`:

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <title>Test JS</title>
        <script src="app.js" defer></script>
      </head>
      <body>
        <h1>Verifică Console!</h1>
      </body>
    </html>
    ```

    `app.js`:

    ```js
    console.log("merge!");
    ```

    Deschide `index.html` în browser, apasă F12 → Console și ar trebui să vezi `merge!`.

### Exercițiu 2 — Experimente în Console
Deschide Console-ul pe orice pagină și tastează:

1. `5 + 5 * 2`
2. `"salut".length`
3. `prompt("Vârsta ta?")`

Ce observi?

??? success "Soluție"
    ```js
    5 + 5 * 2             // 15 — înmulțirea are prioritate
    "salut".length        // 5 — numărul de caractere
    prompt("Vârsta ta?")  // deschide popup, returnează string (ex: "14")
    ```

### Exercițiu 3 — Forțează o eroare
În `app.js`, scrie o linie greșită intenționat: `conzole.log("test")`. Reîncarcă pagina și citește mesajul din Console.

??? success "Soluție"
    Vei vedea ceva de genul:

    ```text
    Uncaught ReferenceError: conzole is not defined
        at app.js:1
    ```

    Browserul îți spune exact linia (`app.js:1`) și motivul (`conzole` nu există). Corectezi la `console` și eroarea dispare.

---

## Mini-proiect: Banner de salut

Pagina cere numele vizitatorului la încărcare și afișează un alert personalizat.

**Cerință:**

- Folosește `prompt()` pentru a cere numele.
- Folosește `alert()` pentru a afișa un salut personalizat.
- Loghează în consolă numele introdus.

??? success "Soluție"
    `index.html`:

    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <title>Banner de salut</title>
        <script src="app.js" defer></script>
      </head>
      <body>
        <h1>Bun venit pe site!</h1>
      </body>
    </html>
    ```

    `app.js`:

    ```js
    // Cere numele vizitatorului
    const nume = prompt("Cum te cheamă?");

    // Loghează în consolă pentru debug
    console.log("Nume introdus:", nume);

    // Afișează un salut personalizat
    alert("Salut, " + nume + "! Mă bucur să te văd.");
    ```

---

## Rezumat

- JavaScript rulează în browser și face paginile interactive.
- Include scripturile cu `<script src="app.js" defer></script>` în `<head>`.
- `console.log(...)` afișează mesaje în **DevTools Console** (F12).
- `alert`, `prompt`, `confirm` sunt popup-uri simple — utile pentru debug, nu pentru UI real.
- Citește **tipul** și **linia** erorii — sunt cel mai bun ghid când ceva nu merge.
- `//` și `/* */` sunt comentarii, ignorate de browser.

---

**Pasul următor:** [→ Lecția 12: Variabile și tipuri de date](12-js-variabile-tipuri.md)
