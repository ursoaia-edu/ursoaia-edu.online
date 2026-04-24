---
lesson: 4
tags: [python, if, elif, else, condiții, operatori-logici]
summary: Controlează ce face programul în funcție de condiții cu if, elif și else.
---

# Lecția 04 · Condiții

!!! tip "Ce vei învăța"
    - Structura `if / elif / else`
    - Operatorii de comparație: `==`, `!=`, `<`, `>`, `<=`, `>=`
    - Operatorii logici: `and`, `or`, `not`
    - Condiții imbricate

---

## Instrucțiunea `if`

`if` îți permite să execuți cod **doar dacă o condiție este adevărată**:

```python
temperatura = 35

if temperatura > 30:
    print("Este cald afară!")
```

**Output:**
```
Este cald afară!
```

Dacă `temperatura` ar fi `20`, nu s-ar afișa nimic.

!!! warning "Indentarea este obligatorie"
    Codul din interiorul `if` trebuie indentat cu **4 spații** (sau un Tab). Python folosește indentarea pentru a ști ce face parte din bloc.
    ```python
    if True:
        print("Această linie face parte din if")
    print("Această linie rulează întotdeauna")
    ```

---

## `if / else`

```python
varsta = 16

if varsta >= 18:
    print("Ești major.")
else:
    print("Ești minor.")
```

`else` se execută când condiția din `if` este **falsă**.

---

## `if / elif / else`

`elif` (prescurtare de la "else if") verifică o condiție nouă dacă cea anterioară a fost falsă:

```python
nota = 8.5

if nota >= 9.5:
    print("Foarte bine — calificativ: Excelent")
elif nota >= 8.5:
    print("Bine — calificativ: Foarte bine")
elif nota >= 7:
    print("Satisfăcător — calificativ: Bine")
elif nota >= 5:
    print("Calificativ: Suficient")
else:
    print("Calificativ: Insuficient")
```

Python verifică condițiile **de sus în jos** și se oprește la prima condiție adevărată.

---

## Operatorii de comparație

| Operator | Semnificație | Exemplu | Rezultat |
|----------|-------------|---------|---------|
| `==` | egal cu | `5 == 5` | `True` |
| `!=` | diferit de | `5 != 3` | `True` |
| `<` | mai mic | `3 < 5` | `True` |
| `>` | mai mare | `5 > 3` | `True` |
| `<=` | mai mic sau egal | `5 <= 5` | `True` |
| `>=` | mai mare sau egal | `6 >= 5` | `True` |

!!! warning "= vs =="
    `=` atribuie valori. `==` compară valori.
    ```python
    x = 5      # atribuire
    x == 5     # comparație → True
    ```

---

## Operatorii logici

### `and` — ambele condiții trebuie să fie adevărate

```python
varsta = 16
are_permis = False

if varsta >= 18 and are_permis:
    print("Poate conduce.")
else:
    print("Nu poate conduce.")
```

### `or` — cel puțin una trebuie să fie adevărată

```python
este_weekend = True
este_sarbatoare = False

if este_weekend or este_sarbatoare:
    print("Nu e școală!")
```

### `not` — neagă condiția

```python
ploua = False

if not ploua:
    print("Putem ieși afară.")
```

---

## Condiții imbricate

Poți pune un `if` înăuntrul altui `if`:

```python
scor = 85
nivel = "avansat"

if scor >= 50:
    print("Ai trecut testul.")
    if nivel == "avansat":
        print("Ai obținut certificatul avansat!")
    else:
        print("Ai obținut certificatul de bază.")
else:
    print("Nu ai trecut testul.")
```

---

## Exerciții

### Exercițiu 1 — Pozitiv, negativ sau zero?
Cere un număr și afișează dacă este pozitiv, negativ sau zero.

??? success "Soluție"
    ```python
    numar = float(input("Introdu un număr: "))
    if numar > 0:
        print("Pozitiv")
    elif numar < 0:
        print("Negativ")
    else:
        print("Zero")
    ```

### Exercițiu 2 — Cel mai mare
Cere două numere și afișează cel mai mare.

??? success "Soluție"
    ```python
    a = float(input("Primul număr: "))
    b = float(input("Al doilea număr: "))
    if a > b:
        print(f"Cel mai mare este {a}")
    elif b > a:
        print(f"Cel mai mare este {b}")
    else:
        print("Numerele sunt egale")
    ```

### Exercițiu 3 — Divisibil?
Cere un număr și verifică dacă este divizibil cu 3 și cu 5 simultan.

??? success "Soluție"
    ```python
    n = int(input("Numărul: "))
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} este divizibil cu 3 și cu 5")
    else:
        print(f"{n} nu este divizibil cu ambele")
    ```

---

## Mini-proiect: Clasificator de note

Cere o notă (1–10) și afișează calificativul și un mesaj motivațional.

**Exemplu:**
```
Nota ta: 9.2
Calificativ: Foarte bine
Felicitări! Ești aproape de perfecțiune!
```

??? success "Soluție"
    ```python
    nota = float(input("Nota ta: "))

    if nota < 1 or nota > 10:
        print("Notă invalidă. Introdu o valoare între 1 și 10.")
    elif nota >= 9.5:
        print("Calificativ: Excelent")
        print("Extraordinar! Performanță de top!")
    elif nota >= 8.5:
        print("Calificativ: Foarte bine")
        print("Felicitări! Ești aproape de perfecțiune!")
    elif nota >= 7:
        print("Calificativ: Bine")
        print("Rezultat bun! Continuă să exersezi.")
    elif nota >= 5:
        print("Calificativ: Suficient")
        print("Ai trecut, dar ai potențial pentru mai mult.")
    else:
        print("Calificativ: Insuficient")
        print("Nu-ți pierde curajul! Repetă materia și încearcă din nou.")
    ```

---

## Rezumat

- `if condiție:` — execută bloc dacă condiția e adevărată
- `elif altă_condiție:` — verifică altă condiție dacă precedenta e falsă
- `else:` — se execută când nicio condiție anterioară nu e adevărată
- Operatori de comparație: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Operatori logici: `and`, `or`, `not`
- Indentarea (4 spații) este obligatorie!

---

**Pasul următor:** [→ Lecția 05: Bucle](05-bucle.md)
