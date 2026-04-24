---
lesson: 14
tags: [javascript, functii, arrow, callback, scope, parametri]
summary: Funcții declarative, expresii de funcție și arrow functions — blocul de construcție al codului reutilizabil.
---

# Lecția 14 · Funcții

!!! tip "Ce vei învăța"
    - De ce avem nevoie de funcții (evitarea repetării, organizare)
    - Trei moduri de a defini o funcție: declaration, expression, arrow
    - Parametri cu valori default, parametri rest
    - `return` și multiple return-uri
    - Ce este **scope**-ul: global, function, block
    - Ce sunt **callback**-urile (preview pentru DOM events)

---

## De ce funcții?

O **funcție** e un bloc de cod pe care îl poți **reutiliza** dându-i un nume. Îl apelezi oriunde ai nevoie, cu date diferite.

Fără funcții:

```js
// Calculează aria pentru trei dreptunghiuri — cod repetitiv
const arie1 = 5 * 3;
console.log(`Dreptunghi 1: ${arie1}`);

const arie2 = 10 * 4;
console.log(`Dreptunghi 2: ${arie2}`);

const arie3 = 7 * 2;
console.log(`Dreptunghi 3: ${arie3}`);
```

Cu funcții:

```js
function arie(lungime, latime) {
  return lungime * latime;
}

console.log(`Dreptunghi 1: ${arie(5, 3)}`);
console.log(`Dreptunghi 2: ${arie(10, 4)}`);
console.log(`Dreptunghi 3: ${arie(7, 2)}`);
```

Câștigi: **mai puțin cod, mai puține greșeli, ușor de modificat**.

---

## Function declaration

Stilul „clasic”:

```js
function salut(nume) {
  return `Salut, ${nume}!`;
}

console.log(salut("Ana"));    // "Salut, Ana!"
console.log(salut("Mihai"));  // "Salut, Mihai!"
```

Părți:

- `function` — cuvânt cheie.
- `salut` — numele funcției.
- `(nume)` — lista de parametri.
- `{ ... }` — corpul funcției.
- `return` — ce „returnează” (trimite înapoi) funcția.

---

## Function expression

O funcție poate fi **stocată într-o variabilă**:

```js
const salut = function(nume) {
  return `Salut, ${nume}!`;
};

console.log(salut("Ana"));
```

Observă:

- Funcția nu are nume după `function` (se numește **anonimă**).
- Linia se termină cu `;` (pentru că e o expresie asignată unei variabile).

---

## Arrow function (funcție săgeată)

Forma **modernă** și **compactă**, introdusă în ES6:

```js
// Versiunea lungă
const salut = (nume) => {
  return `Salut, ${nume}!`;
};

// Versiunea scurtă (implicit return)
const salut = (nume) => `Salut, ${nume}!`;

// Un singur parametru — parantezele sunt opționale
const salut = nume => `Salut, ${nume}!`;

// Fără parametri — parantezele sunt obligatorii
const ora = () => new Date().toLocaleTimeString();

// Doi sau mai mulți parametri
const suma = (a, b) => a + b;
```

Reguli:

- Un singur parametru: `()` opțional.
- Corp de o singură expresie: `{}` și `return` opționale (implicit return).
- Corp cu mai multe linii: `{}` și `return` explicit obligatorii.

---

## Arrow vs regular — ce să alegi?

| Aspect | `function` tradițional | Arrow `=>` |
|--------|------------------------|------------|
| Sintaxă | mai verboasă | mai compactă |
| `this` propriu | DA | NU (moștenit din contextul părinte) |
| Hoisting | DA (poți apela înainte de definire) | NU |
| Util pentru | metode de obiect, funcții lungi | callback-uri, funcții scurte |

!!! note "Despre `this`"
    `this` într-o arrow e moștenit din contextul părinte. Asta e adesea **ce vrei** când scrii callback-uri pentru events și pentru metode de array (`.map`, `.filter`). Detalii pe larg când ajungem la obiecte și clase.

Pentru acum: folosește **arrow** pentru callback-uri și funcții scurte, **function declaration** pentru funcții lungi de top-level.

---

## Parametri

### Multipli

```js
const suma = (a, b, c) => a + b + c;
console.log(suma(1, 2, 3));   // 6
```

### Default values

Dacă apelezi fără argument, parametrul ia valoarea default:

```js
const salut = (nume = "prieten") => `Salut, ${nume}!`;

console.log(salut());         // "Salut, prieten!"
console.log(salut("Ana"));    // "Salut, Ana!"
```

### Rest parameters

Pentru număr **variabil** de argumente:

```js
const suma = (...numere) => {
  let total = 0;
  for (const n of numere) {
    total += n;
  }
  return total;
};

console.log(suma(1, 2, 3));         // 6
console.log(suma(5, 10, 15, 20));   // 50
```

`...numere` strânge toate argumentele într-un array numit `numere`.

---

## `return`

- Fără `return`, funcția returnează `undefined`.
- `return` oprește execuția funcției imediat.

```js
const test = () => {
  console.log("înainte");
  return;
  console.log("după");   // nu se execută niciodată
};
```

### Early exit

Returnează devreme pentru a evita imbricarea profundă:

```js
// GREU de citit
const verificaVarsta = (v) => {
  if (v >= 0) {
    if (v >= 18) {
      return "major";
    } else {
      return "minor";
    }
  } else {
    return "valoare invalidă";
  }
};

// CURAT cu early return
const verificaVarsta = (v) => {
  if (v < 0) return "valoare invalidă";
  if (v >= 18) return "major";
  return "minor";
};
```

---

## Scope (domeniu de vizibilitate)

**Scope** = unde e **vizibilă** o variabilă.

### Global scope

Declarată în afara oricărei funcții — accesibilă de oriunde:

```js
const numeSit = "Cercul de Informatică";

function afisare() {
  console.log(numeSit);   // OK, o vede
}
```

### Function scope

Declarată **în** funcție — accesibilă doar în funcție:

```js
function calcul() {
  const secret = 42;
  console.log(secret);   // OK
}

calcul();
console.log(secret);   // ReferenceError!
```

### Block scope (`let` / `const`)

`let` și `const` sunt **block-scoped** — limitate la cea mai apropiată pereche de `{}`:

```js
if (true) {
  const x = 10;
  console.log(x);   // 10
}

console.log(x);   // ReferenceError!
```

!!! warning "`var` e function-scoped, nu block-scoped"
    Asta înseamnă că `var` declarată într-un `if` e accesibilă în afara lui — exact opusul a ce te-ai aștepta. Încă un motiv să folosești `let`/`const`.

---

## Callback functions

Un **callback** e o funcție pe care o **pasezi** altei funcții ca argument, pentru a fi apelată mai târziu:

```js
const cuIntarziere = (callback) => {
  setTimeout(callback, 1000);   // rulează callback după 1 secundă
};

cuIntarziere(() => console.log("A trecut o secundă!"));
```

Callback-urile sunt peste tot în JS — le vei folosi intens pentru evenimente (lecția 16) și pentru fetch (lecția 18).

---

## Exerciții

### Exercițiu 1 — Funcția `patrat`
Scrie o funcție `patrat(n)` care returnează `n²`.

??? success "Soluție"
    ```js
    function patrat(n) {
      return n * n;
    }

    console.log(patrat(5));   // 25

    // Sau ca arrow:
    const patrat = (n) => n * n;
    ```

### Exercițiu 2 — Salut cu default
Scrie `salut(nume = "prieten")` care afișează `"Salut, <nume>!"`.

??? success "Soluție"
    ```js
    const salut = (nume = "prieten") => `Salut, ${nume}!`;

    console.log(salut());         // "Salut, prieten!"
    console.log(salut("Maria"));  // "Salut, Maria!"
    ```

### Exercițiu 3 — Cel mai mare din trei
Funcția `celMaiMare(a, b, c)` returnează cel mai mare din trei numere.

??? success "Soluție"
    ```js
    const celMaiMare = (a, b, c) => {
      if (a >= b && a >= c) return a;
      if (b >= c) return b;
      return c;
    };

    console.log(celMaiMare(3, 9, 5));   // 9

    // Sau foarte scurt:
    const celMaiMare2 = (a, b, c) => Math.max(a, b, c);
    ```

### Exercițiu 4 — Rescriere ca arrow
Rescrie `patrat` și `salut` de mai sus folosind **arrow functions**, în formele cele mai scurte posibil.

??? success "Soluție"
    ```js
    const patrat = n => n * n;
    const salut = (nume = "prieten") => `Salut, ${nume}!`;
    ```

    Pentru `patrat`, un singur parametru → fără paranteze. O singură expresie → fără `{}` și fără `return`.

---

## Mini-proiect: Convertor de temperatură

Scrie două funcții care convertesc temperaturi între Celsius și Fahrenheit.

**Formule:**

- Celsius → Fahrenheit: `F = C * 9/5 + 32`
- Fahrenheit → Celsius: `C = (F - 32) * 5/9`

**Cerințe:**

- Două funcții: `celsiusInFahrenheit(c)` și `fahrenheitInCelsius(f)`.
- Apelează-le cu câteva valori.
- Afișează cu template literal: `"0 °C = 32 °F"`.

??? success "Soluție"
    ```js
    // Formule de conversie
    const celsiusInFahrenheit = (c) => c * 9 / 5 + 32;
    const fahrenheitInCelsius = (f) => (f - 32) * 5 / 9;

    // Câteva teste
    console.log(`0 °C = ${celsiusInFahrenheit(0)} °F`);      // 0 °C = 32 °F
    console.log(`100 °C = ${celsiusInFahrenheit(100)} °F`);  // 100 °C = 212 °F
    console.log(`32 °F = ${fahrenheitInCelsius(32)} °C`);    // 32 °F = 0 °C
    console.log(`212 °F = ${fahrenheitInCelsius(212)} °C`);  // 212 °F = 100 °C
    ```

    **Bonus:** cere temperatura de la utilizator:

    ```js
    const c = Number(prompt("Temperatura în °C:"));
    const f = celsiusInFahrenheit(c);
    alert(`${c} °C = ${f.toFixed(1)} °F`);
    ```

---

## Rezumat

- Funcțiile îți permit să **reutilizezi cod** cu input-uri diferite.
- Trei forme: **declaration** (`function nume() {}`), **expression** (`const f = function() {}`), **arrow** (`const f = () => {}`).
- Arrow e compactă și preferată pentru callback-uri scurte.
- Parametrii pot avea **default values** și **rest** (`...`).
- `return` oprește funcția și trimite înapoi o valoare. Folosește **early return** ca să eviți imbricarea.
- **Scope-ul** `let`/`const` e block-scoped (`{}`), `var` e function-scoped (evit-o).
- **Callback**-urile sunt funcții pasate ca argumente — le vei folosi mult la events.

---

**Pasul următor:** [→ Lecția 15: DOM — Manipulare HTML](15-js-dom.md)
