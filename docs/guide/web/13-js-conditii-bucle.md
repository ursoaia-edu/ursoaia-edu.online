---
lesson: 13
tags: [javascript, conditii, if, else, for, while, bucle, operatori]
summary: Controlează fluxul programului cu if/else, switch și bucle for/while.
---

# Lecția 13 · Condiții și bucle

!!! tip "Ce vei învăța"
    - Cum iei decizii cu `if / else if / else`
    - Diferența între `==` și `===` (spoiler: folosește `===`)
    - Operatori logici `&&`, `||`, `!` și operatorul ternar
    - Buclele `for`, `while`, `do...while`, `for...of`
    - Cum controlezi execuția cu `break` și `continue`

---

## `if / else if / else`

Cea mai simplă decizie:

```js
const varsta = 16;

if (varsta >= 18) {
  console.log("Poate vota.");
} else if (varsta >= 16) {
  console.log("Poate obține permis categoria AM.");
} else {
  console.log("Încă prea tânăr pentru permis.");
}
```

Structura:

- `if (condiție) { ... }` — dacă `condiție` e `true`, rulează blocul.
- `else if (altaCondiție) { ... }` — verificată doar dacă precedenta e `false`.
- `else { ... }` — se rulează dacă nimic de mai sus nu s-a potrivit.

Acoladele sunt opționale pentru o singură linie, dar **pune-le oricum** — e mai sigur și mai clar.

---

## Operatori de comparație

| Operator | Semnificație | Exemplu | Rezultat |
|----------|--------------|---------|----------|
| `===` | strict egal | `5 === 5` | `true` |
| `!==` | strict diferit | `"5" !== 5` | `true` |
| `==` | egal cu coerce | `"5" == 5` | `true` |
| `!=` | diferit cu coerce | `"5" != 5` | `false` |
| `<`, `>`, `<=`, `>=` | comparație numerică | `3 < 5` | `true` |

### `==` vs `===` — capcana clasică

`==` face **coerce de tip** înainte să compare — încearcă să facă valorile „compatibile”:

```js
console.log("2" == 2);      // true  — string e convertit la number
console.log("2" === 2);     // false — tipuri diferite, gata

console.log(0 == false);    // true  — coerce la boolean
console.log(null == undefined);  // true — caz special

console.log(0 === false);   // false
```

!!! warning "Folosește întotdeauna `===` și `!==`"
    `==` are reguli de coerce complicate care duc la bug-uri subtile. `===` compară tipul + valoarea — simplu și previzibil.

---

## Operatori logici

```js
const a = true;
const b = false;

console.log(a && b);   // false — AND: true doar dacă ambele true
console.log(a || b);   // true  — OR: true dacă cel puțin unul e true
console.log(!a);       // false — NOT: inversează
```

Exemplu practic:

```js
const varsta = 17;
const areCarnet = false;

if (varsta >= 18 && areCarnet) {
  console.log("Poate conduce.");
} else {
  console.log("Nu încă.");
}
```

### Short-circuit (evaluare leneșă)

- `&&` se oprește la **primul `false`**.
- `||` se oprește la **primul `true`**.

```js
// b() nu va fi apelată, pentru că a() a returnat false
a() && b();

// b() nu va fi apelată, pentru că a() a returnat true
a() || b();
```

Util pentru valori default:

```js
const nume = inputUtilizator || "Necunoscut";
// dacă inputUtilizator e "" / null / undefined, folosește "Necunoscut"
```

---

## Operatorul ternar

Formă scurtă pentru `if / else` care returnează o valoare:

```js
// condiție ? valoareDacaTrue : valoareDacaFalse
const varsta = 16;
const eticheta = varsta >= 18 ? "major" : "minor";

console.log(eticheta);   // "minor"
```

Poate fi util, dar **nu-l îngropa** în expresii imbricate — devine ilizibil.

---

## `switch / case`

Când ai multe ramuri bazate pe aceeași variabilă:

```js
const zi = "luni";

switch (zi) {
  case "luni":
  case "marți":
  case "miercuri":
  case "joi":
  case "vineri":
    console.log("Zi lucrătoare");
    break;
  case "sâmbătă":
  case "duminică":
    console.log("Weekend!");
    break;
  default:
    console.log("Zi necunoscută");
}
```

!!! note "Nu uita `break`!"
    Fără `break`, execuția „cade” în case-ul următor (fall-through). Util intenționat (ca mai sus, unde mai multe zile rulează același cod), dar periculos dacă uiți.

---

## Bucla `for`

```js
for (let i = 0; i < 5; i++) {
  console.log(`Iterația ${i}`);
}
// Iterația 0
// Iterația 1
// Iterația 2
// Iterația 3
// Iterația 4
```

Trei părți în paranteze:

1. **Inițializare** — `let i = 0` (rulează o dată, la început).
2. **Condiție** — `i < 5` (verificată înainte de fiecare iterație).
3. **Pas** — `i++` (rulează după fiecare iterație).

`i++` e prescurtare pentru `i = i + 1`. Similar: `i--`, `i += 2`, `i *= 3`.

---

## Bucla `while`

```js
let n = 0;

while (n < 5) {
  console.log(n);
  n++;
}
```

Rulează **atâta timp cât** condiția e `true`. Folosește-o când **nu știi dinainte** câte iterații vei face.

---

## Bucla `do...while`

Similară cu `while`, dar **rulează cel puțin o dată** (verifică condiția la final):

```js
let raspuns;

do {
  raspuns = prompt("Spune „ieși” ca să termini:");
} while (raspuns !== "ieși");
```

---

## `break` și `continue`

- **`break`** iese complet din buclă.
- **`continue`** sare la următoarea iterație.

```js
for (let i = 0; i < 10; i++) {
  if (i === 5) break;       // se oprește când i e 5
  if (i % 2 === 0) continue; // sare peste pare
  console.log(i);           // 1, 3
}
```

---

## `for...of` — pentru iterare peste array

Varianta modernă, **preferată** pentru a parcurge un array:

```js
const culori = ["roșu", "verde", "albastru"];

for (const culoare of culori) {
  console.log(culoare);
}
// roșu
// verde
// albastru
```

Simplu și curat. Nu mai ai nevoie de index `i`.

!!! note "`for...in` există, dar evit-o pentru array-uri"
    `for...in` iterează peste **chei** (inclusiv moștenite) și e concepută pentru obiecte. Pentru array-uri, folosește `for...of` sau `.forEach()`.

---

## Erori frecvente

### Buclă infinită

Uiți să incrementezi contorul:

```js
// GREȘIT: n nu crește niciodată!
let n = 0;
while (n < 5) {
  console.log(n);
  // lipsește n++
}
```

Browserul se va bloca. Deschide DevTools și oprește fila.

### `=` vs `==` vs `===`

```js
if (x = 5) { ... }    // atribuire! nu comparație. Aproape mereu greșit.
if (x == 5) { ... }   // comparație cu coerce. Evită.
if (x === 5) { ... }  // strict equal. Corect.
```

---

## Exerciții

### Exercițiu 1 — Par sau impar
Scrie un program care citește un număr și afișează dacă e par sau impar.

??? success "Soluție"
    ```js
    const n = Number(prompt("Un număr:"));

    if (n % 2 === 0) {
      console.log(`${n} e par.`);
    } else {
      console.log(`${n} e impar.`);
    }
    ```

    `% 2` dă 0 pentru numere pare, 1 pentru impare.

### Exercițiu 2 — Numere de la 1 la 10
Afișează în consolă numerele de la 1 la 10 cu `for`.

??? success "Soluție"
    ```js
    for (let i = 1; i <= 10; i++) {
      console.log(i);
    }
    ```

### Exercițiu 3 — Cel mai mare din trei
Primești 3 numere și afișezi pe cel mai mare.

??? success "Soluție"
    ```js
    const a = 12;
    const b = 47;
    const c = 8;

    let max = a;
    if (b > max) max = b;
    if (c > max) max = c;

    console.log(`Cel mai mare: ${max}`);   // 47

    // Variantă scurtă, cu Math.max:
    console.log(Math.max(a, b, c));         // 47
    ```

### Exercițiu 4 — Suma de la 1 la 100
Calculează suma numerelor de la 1 la 100.

??? success "Soluție"
    ```js
    let suma = 0;
    for (let i = 1; i <= 100; i++) {
      suma += i;
    }
    console.log(suma);   // 5050
    ```

---

## Mini-proiect: Ghicește numărul

Un joc clasic: calculatorul alege un număr random între 1 și 100, tu ai câte încercări îți trebuie să-l ghicești.

**Cerințe:**

- Generează un număr random între 1 și 100.
- Într-o buclă, cere utilizatorului să ghicească.
- Dă feedback: **prea mic** / **prea mare** / **corect**.
- La sfârșit, afișează câte încercări au fost necesare.

??? success "Soluție"
    ```js
    // Număr random între 1 și 100
    const tinta = Math.floor(Math.random() * 100) + 1;

    let incercari = 0;
    let ghicit = false;

    while (!ghicit) {
      const raspuns = Number(prompt("Ghicește un număr între 1 și 100:"));
      incercari++;

      if (raspuns === tinta) {
        ghicit = true;
        alert(`Felicitări! Ai ghicit în ${incercari} încercări.`);
      } else if (raspuns < tinta) {
        alert("Prea mic. Mai încearcă!");
      } else {
        alert("Prea mare. Mai încearcă!");
      }
    }
    ```

    `Math.random()` returnează `[0, 1)`. Înmulțit cu 100 și rotunjit în jos cu `Math.floor`, apoi `+1`, dă întreg `[1, 100]`.

---

## Rezumat

- `if / else if / else` — decizii ramificate.
- Folosește **`===`**, nu `==`. Așa eviți coerce-ul implicit de tip.
- Operatori logici: `&&` (și), `||` (sau), `!` (nu). Folosesc evaluare leneșă.
- Ternar `condiție ? a : b` — util pentru atribuiri simple.
- `for` când știi câte iterații; `while` când nu știi.
- `for...of` pentru parcurgerea elementelor unui array.
- `break` iese, `continue` sare la iterația următoare.

---

**Pasul următor:** [→ Lecția 14: Funcții](14-js-functii.md)
