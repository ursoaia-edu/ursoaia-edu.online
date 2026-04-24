---
lesson: 3
tags: [python, input, output, interactivitate]
summary: Fă programele interactive cu input() și formatează output-ul cu print().
---

# Lecția 03 · Input și Output

!!! tip "Ce vei învăța"
    - Cum citești date de la utilizator cu `input()`
    - De ce `input()` returnează întotdeauna `str`
    - Cum convertești inputul în numere
    - Formatarea avansată a output-ului

---

## Funcția `input()`

`input()` oprește programul și așteaptă ca utilizatorul să tasteze ceva și să apese Enter:

```python
nume = input("Cum te numești? ")
print("Salut,", nume)
```

**Rulare:**
```
Cum te numești? Andrei
Salut, Andrei
```

Textul din paranteze este **promptul** — mesajul afișat utilizatorului.

---

## `input()` returnează ÎNTOTDEAUNA `str`

Aceasta este cea mai frecventă sursă de erori pentru începători:

```python
varsta = input("Vârsta ta: ")
print(type(varsta))   # <class 'str'>
```

Chiar dacă utilizatorul tastează `14`, Python primește șirul `"14"`, nu numărul `14`.

### Conversia inputului

```python
varsta = int(input("Vârsta ta: "))
print(type(varsta))   # <class 'int'>
print(varsta + 1)     # funcționează!
```

```python
inaltime = float(input("Înălțimea ta (m): "))
print(f"Înălțimea în cm: {inaltime * 100}")
```

!!! warning "Dacă utilizatorul tastează altceva"
    `int(input(...))` va genera o eroare dacă utilizatorul tastează text în loc de număr. Vom rezolva asta în lecția despre condiții și excepții.

---

## Funcția `print()` — detalii

### Separatorul `sep`

```python
print("luni", "marți", "miercuri")           # luni marți miercuri
print("luni", "marți", "miercuri", sep=", ") # luni, marți, miercuri
print("luni", "marți", "miercuri", sep="\n") # fiecare pe linie nouă
```

### Terminatorul `end`

```python
print("Unu", end=" ")
print("Doi", end=" ")
print("Trei")
# Unu Doi Trei — toate pe aceeași linie
```

### Linie goală

```python
print()   # afișează o linie goală
```

---

## Exemple combinate

### Program simplu de salut

```python
prenume = input("Prenumele tău: ")
varsta = int(input("Vârsta ta: "))

print()
print(f"Salut, {prenume}!")
print(f"Anul viitor vei avea {varsta + 1} ani.")
```

### Citire mai multor valori

```python
a = float(input("Primul număr: "))
b = float(input("Al doilea număr: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} × {b} = {a * b}")
```

---

## Exerciții

### Exercițiu 1 — Salut personalizat
Scrie un program care cere numele și vârsta, apoi afișează: `"Bună, [nume]! Ai [vârstă] ani."`

??? success "Soluție"
    ```python
    nume = input("Numele tău: ")
    varsta = int(input("Vârsta ta: "))
    print(f"Bună, {nume}! Ai {varsta} ani.")
    ```

### Exercițiu 2 — Aria dreptunghiului
Cere lungimea și lățimea unui dreptunghi, calculează aria și perimetrul.

??? success "Soluție"
    ```python
    lungime = float(input("Lungimea (m): "))
    latime = float(input("Lățimea (m): "))
    aria = lungime * latime
    perimetru = 2 * (lungime + latime)
    print(f"Aria: {aria} m²")
    print(f"Perimetrul: {perimetru} m")
    ```

### Exercițiu 3 — Câte secunde?
Cere ore și minute, afișează totalul în secunde.

??? success "Soluție"
    ```python
    ore = int(input("Ore: "))
    minute = int(input("Minute: "))
    secunde = ore * 3600 + minute * 60
    print(f"{ore}h {minute}min = {secunde} secunde")
    ```

---

## Mini-proiect: Calculator interactiv

Scrie un program care cere două numere și afișează toate operațiile de bază.

**Exemplu de rulare:**
```
Primul număr: 10
Al doilea număr: 3

10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 × 3.0 = 30.0
10.0 / 3.0 = 3.3333333333333335
10.0 // 3.0 = 3.0
10.0 % 3.0 = 1.0
10.0 ^ 3.0 = 1000.0
```

??? success "Soluție"
    ```python
    a = float(input("Primul număr: "))
    b = float(input("Al doilea număr: "))

    print()
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} × {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ^ {b} = {a ** b}")
    ```

---

## Rezumat

- `input("mesaj")` citește text de la tastatură — returnează ÎNTOTDEAUNA `str`
- Convertește cu `int(input(...))` sau `float(input(...))`
- `print(a, b, sep=", ")` controlează separatorul
- `print("text", end="")` controlează ce vine după linie

---

**Pasul următor:** [→ Lecția 04: Condiții](04-conditii.md)
