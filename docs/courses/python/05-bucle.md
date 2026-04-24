---
lesson: 5
tags: [python, for, while, bucle, break, continue, range]
summary: Repetă acțiuni cu buclele for și while. Controlează fluxul cu break și continue.
---

# Lecția 05 · Bucle

!!! tip "Ce vei învăța"
    - Bucla `for` cu `range()`
    - Bucla `while`
    - Instrucțiunile `break` și `continue`
    - Bucle imbricate

---

## Bucla `for`

`for` repetă un bloc de cod pentru fiecare element dintr-o secvență:

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### Funcția `range()`

| Apel | Valori generate |
|------|----------------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, 8, ..., 1 |

```python
# Numără de la 1 la 10
for i in range(1, 11):
    print(i)

# Numere pare de la 2 la 20
for i in range(2, 21, 2):
    print(i)

# Numără invers
for i in range(5, 0, -1):
    print(i)
print("Start!")
```

### `for` peste un șir de caractere

```python
for litera in "Python":
    print(litera)
# P
# y
# t
# h
# o
# n
```

---

## Bucla `while`

`while` repetă un bloc **cât timp o condiție este adevărată**:

```python
numar = 1
while numar <= 5:
    print(numar)
    numar += 1   # numar = numar + 1
```

**Output:**
```
1
2
3
4
5
```

!!! warning "Bucla infinită"
    Dacă uiți să modifici variabila, bucla nu se mai oprește:
    ```python
    # GREȘIT — buclă infinită!
    x = 1
    while x <= 5:
        print(x)
        # am uitat x += 1
    ```
    Oprește programul cu `Ctrl+C`.

### `while` pentru validarea inputului

```python
raspuns = ""
while raspuns != "da" and raspuns != "nu":
    raspuns = input("Ai înțeles? (da/nu): ")
print("Mulțumesc!")
```

---

## `break` — ieșirea forțată din buclă

```python
for i in range(1, 100):
    if i == 5:
        break
    print(i)
# Afișează: 1, 2, 3, 4
```

---

## `continue` — sare la următoarea iterație

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue   # sare peste numerele pare
    print(i)
# Afișează: 1, 3, 5, 7, 9
```

---

## Bucle imbricate

O buclă înăuntrul altei bucle:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()
```

**Output:**
```
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3

2 × 1 = 2
...
```

---

## Exerciții

### Exercițiu 1 — Suma de la 1 la N
Cere un număr N și calculează suma 1 + 2 + ... + N.

??? success "Soluție"
    ```python
    n = int(input("N = "))
    suma = 0
    for i in range(1, n + 1):
        suma += i
    print(f"Suma = {suma}")
    ```

### Exercițiu 2 — Numere prime
Afișează toate numerele prime mai mici decât 50.

??? success "Soluție"
    ```python
    for n in range(2, 50):
        este_prim = True
        for d in range(2, n):
            if n % d == 0:
                este_prim = False
                break
        if este_prim:
            print(n)
    ```

### Exercițiu 3 — Ghicește numărul
Generează un număr "secret" (folosit hardcodat) și lasă utilizatorul să ghicească cu feedback.

??? success "Soluție"
    ```python
    secret = 42
    incercari = 0

    while True:
        ghicit = int(input("Ghicește numărul (1-100): "))
        incercari += 1
        if ghicit < secret:
            print("Prea mic!")
        elif ghicit > secret:
            print("Prea mare!")
        else:
            print(f"Corect! Ai ghicit în {incercari} încercări.")
            break
    ```

---

## Mini-proiect: Tabla înmulțirii

Afișează tabla înmulțirii pentru numerele 1–10 în format tabelar.

**Output (primele rânduri):**
```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
...
```

??? success "Soluție"
    ```python
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end="")
        print()
    ```
    `{i*j:4}` formatează numărul pe 4 caractere pentru aliniere.

---

## Rezumat

- `for i in range(n):` — repetă de `n` ori
- `range(start, stop, pas)` — generează secvențe de numere
- `while condiție:` — repetă cât timp condiția e adevărată
- `break` — ieșire forțată din buclă
- `continue` — sare la iterația următoare
- Indentarea este obligatorie!

---

**Pasul următor:** [→ Lecția 06: Liste](06-liste.md)
