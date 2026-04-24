---
lesson: 12
tags: [javascript, variabile, tipuri, string, number, boolean, template-literals]
summary: Variabile cu let și const, tipuri primitive, template literals și metode utile pentru string și number.
---

# Lecția 12 · Variabile și tipuri de date

!!! tip "Ce vei învăța"
    - Diferența dintre `let`, `const` și `var`
    - Tipurile primitive: number, string, boolean, null, undefined
    - Cum folosești **template literals** (string-uri cu backticks)
    - Operatori aritmetici și capcanele cu string-uri
    - Metode utile pentru string și number

---

## Declararea variabilelor

În JavaScript modern folosim **`let`** și **`const`** pentru a declara variabile:

```js
let nume = "Ana";       // valoare care se poate schimba
const PI = 3.14;        // valoare fixă (nu se poate reasigna)

nume = "Maria";         // OK
// PI = 3.14159;        // Eroare! "Assignment to constant variable"
```

**Regula de aur:** preferă `const`. Folosește `let` doar când știi că valoarea se va schimba.

```js
const maxIncercari = 3;        // constantă
let incercari = 0;              // contor — crește în timp
incercari = incercari + 1;
```

### Ce este `var`?

`var` este varianta **veche**, dinainte de 2015. Are reguli ciudate de scope (vom vedea în lecția de funcții). **Nu îl folosi în cod nou** — folosește `let` / `const`.

### Convenții de denumire

| Stil | Când se folosește | Exemplu |
|------|-------------------|---------|
| `camelCase` | variabile și funcții | `numeleElevului`, `calculeazaMedia` |
| `PascalCase` | clase și componente | `Utilizator`, `CardProdus` |
| `UPPER_SNAKE` | constante „de sistem” | `MAX_SCOR`, `API_URL` |

### Reguli pentru nume

- Pot începe cu literă, `_` sau `$`.
- Pot conține cifre, dar **nu la început**.
- **Sunt case-sensitive:** `nume` și `Nume` sunt variabile diferite.
- Nu poți folosi cuvinte rezervate: `let`, `const`, `if`, `function`, `class`, etc.

---

## Tipuri primitive

JavaScript are câteva tipuri de bază numite **primitive**:

```js
const varsta = 14;              // Number
const pret = 3.14;              // Number (nu există tip separat pentru float)
const nume = "Ana";             // String
const esteMajor = false;        // Boolean
const nimic = null;             // null — „intenționat gol”
let neinitializat;              // undefined — „nu i-am dat valoare”
```

### `null` vs `undefined`

- **`undefined`** — valoarea pe care o are o variabilă **declarată dar fără valoare**.
- **`null`** — valoarea pe care o pui **intenționat** când vrei să spui „niciun obiect”.

```js
let x;                  // undefined (nu i-am dat valoare)
let y = null;           // null (eu am zis: e gol)
```

---

## Template literals

Cel mai elegant mod de a construi string-uri în JS modern: **backticks** `` ` ``.

```js
const nume = "Mihai";
const varsta = 14;

// Varianta veche — concatenare cu +
const vechi = "Salut, " + nume + "! Ai " + varsta + " ani.";

// Varianta modernă — template literal
const nou = `Salut, ${nume}! Ai ${varsta} ani.`;
```

Avantaje:

- `${expresie}` interpolează orice expresie JS.
- Funcționează pe **mai multe linii** fără `\n`:

```js
const mesaj = `Linia 1
Linia 2
Linia 3`;
```

!!! tip "Când folosești backticks?"
    Aproape mereu în JS modern. Chiar dacă nu ai interpolare, e lizibil și flexibil.

---

## Operatori aritmetici

```js
const a = 10;
const b = 3;

console.log(a + b);    // 13
console.log(a - b);    // 7
console.log(a * b);    // 30
console.log(a / b);    // 3.3333...
console.log(a % b);    // 1 — restul împărțirii (modulo)
console.log(a ** b);   // 1000 — ridicare la putere (10³)
```

### Capcana cu string-uri

`+` are două sensuri în JS:

```js
console.log(2 + 2);        // 4   — adunare numerică
console.log("2" + 2);      // "22" — concatenare string!
console.log("2" + "2");    // "22"
```

Dar operatorii `-`, `*`, `/` convertesc automat string la number:

```js
console.log("10" - 2);     // 8
console.log("5" * "3");    // 15
```

!!! warning "Conversia implicită e o sursă clasică de bug-uri"
    Dacă citești un număr dintr-un input HTML, acesta vine ca **string**. Convertește-l explicit înainte de calcule (vezi mai jos).

---

## Metode utile pentru string

```js
const text = "  Salut, Ana!  ";

text.length              // 15 — numărul de caractere (cu spații)
text.toUpperCase()       // "  SALUT, ANA!  "
text.toLowerCase()       // "  salut, ana!  "
text.trim()              // "Salut, Ana!" — elimină spațiile de la capete
text.includes("Ana")     // true
text.slice(2, 7)         // "Salut" — substring de la index 2 la 7 (exclusiv)
text.replace("Ana", "Maria")  // "  Salut, Maria!  "
text.split(",")          // ["  Salut", " Ana!  "] — împarte după virgulă
```

Metodele **nu modifică** string-ul original (string-urile sunt imutabile) — returnează unul nou.

---

## Metode utile pentru number

```js
const pret = 19.9876;

pret.toFixed(2);            // "19.99" — rotunjire la 2 zecimale (ATENȚIE: returnează string!)

Number.parseInt("42");      // 42
Number.parseFloat("3.14");  // 3.14
Number("3.14");             // 3.14 — conversie directă

Math.round(3.6);     // 4
Math.floor(3.9);     // 3
Math.ceil(3.1);      // 4
Math.abs(-5);        // 5
Math.max(2, 9, 4);   // 9
Math.min(2, 9, 4);   // 2
Math.random();       // 0.7231... — număr aleatoriu în [0, 1)
```

### Conversie string → number

Când citești dintr-un input:

```js
const textVarsta = "14";               // a venit ca string
const varsta = Number(textVarsta);      // 14 ca number
const total = varsta + 1;               // 15 (corect!)
```

---

## Operatorul `typeof`

Află tipul unei valori:

```js
typeof 42          // "number"
typeof "ana"       // "string"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object" — bug istoric în JS!
typeof [1, 2, 3]   // "object"
typeof { a: 1 }    // "object"
```

!!! note "`typeof null` este `\"object\"`"
    Este un bug vechi din JavaScript care nu mai poate fi reparat fără să strice internetul. Reține că e o excepție.

---

## Arrays — pe scurt

Un **array** stochează o listă ordonată de valori. Detalii în lecțiile următoare; pentru moment:

```js
const culori = ["roșu", "verde", "albastru"];

console.log(culori[0]);       // "roșu"
console.log(culori.length);   // 3

culori.push("galben");        // adaugă la final
console.log(culori);           // ["roșu", "verde", "albastru", "galben"]

const ultim = culori.pop();   // scoate ultimul element
console.log(ultim);            // "galben"
```

---

## Obiecte — pe scurt

Un **obiect** stochează perechi cheie-valoare:

```js
const persoana = {
  nume: "Ana",
  varsta: 14,
  clasa: "8A"
};

console.log(persoana.nume);     // "Ana"
console.log(persoana["varsta"]); // 14
```

Vom reveni pe larg.

---

## Exerciții

### Exercițiu 1 — Prezentare personală
Creează variabilele `nume`, `varsta` și `student` (boolean). Afișează-le cu un template literal.

??? success "Soluție"
    ```js
    const nume = "Mihai";
    const varsta = 14;
    const student = true;

    console.log(`Numele meu e ${nume}, am ${varsta} ani, student: ${student}.`);
    // Numele meu e Mihai, am 14 ani, student: true.
    ```

### Exercițiu 2 — Curățare string
Pornind de la `"  Ana Pop  "`, obține varianta fără spații la capete și în majuscule.

??? success "Soluție"
    ```js
    const original = "  Ana Pop  ";
    const curatat = original.trim().toUpperCase();
    console.log(curatat);   // "ANA POP"
    ```

    Poți înlănțui metode: `trim()` returnează un string, pe care apelezi apoi `toUpperCase()`.

### Exercițiu 3 — Conversie și adunare
Convertește string-ul `"42"` la număr și adună-i `8`. Afișează rezultatul.

??? success "Soluție"
    ```js
    const text = "42";
    const numar = Number(text);      // sau Number.parseInt(text)
    const rezultat = numar + 8;
    console.log(rezultat);            // 50
    ```

    Dacă uiți conversia: `"42" + 8` → `"428"` (concatenare). Clasic!

### Exercițiu 4 — Verifică tipuri
Ce afișează fiecare din aceste `console.log`?

```js
console.log(typeof "14");
console.log(typeof 14);
console.log(typeof (14 > 10));
console.log(typeof undefined);
```

??? success "Soluție"
    ```text
    "string"
    "number"
    "boolean"   — comparația returnează true/false
    "undefined"
    ```

---

## Mini-proiect: Calculator de arie

Scrie un program care calculează aria unui dreptunghi și afișează rezultatul frumos.

**Cerință:**

- Definește `lungime` și `latime` cu `let` / `const`.
- Calculează aria.
- Afișează cu template literal: `"Aria dreptunghiului de 5x3 este 15 m²"`.

??? success "Soluție"
    ```js
    const lungime = 5;
    const latime = 3;
    const arie = lungime * latime;

    console.log(`Aria dreptunghiului de ${lungime}x${latime} este ${arie} m².`);
    // Aria dreptunghiului de 5x3 este 15 m².
    ```

    **Bonus:** cere valorile de la utilizator cu `prompt()` și convertește-le cu `Number()`.

    ```js
    const lungime = Number(prompt("Lungime:"));
    const latime = Number(prompt("Lățime:"));
    const arie = lungime * latime;

    alert(`Aria e ${arie} m².`);
    ```

---

## Rezumat

- Preferă **`const`**; folosește **`let`** doar când reasignezi; **nu folosi `var`**.
- Tipuri primitive: `number`, `string`, `boolean`, `null`, `undefined`.
- Template literals cu `` ` `` și `${}` sunt modul modern de a construi string-uri.
- `"2" + 2` este `"22"` (concatenare) — ai grijă la conversiile implicite.
- `Number(x)`, `Number.parseInt(x)`, `Number.parseFloat(x)` convertesc string la number.
- `typeof` îți spune tipul unei valori.

---

**Pasul următor:** [→ Lecția 13: Condiții și bucle](13-js-conditii-bucle.md)
