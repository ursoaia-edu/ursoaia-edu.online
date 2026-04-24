---
lesson: 2
tags: [python, operatori, aritmetică, f-strings, conversii]
summary: Lucrează cu numere și text — operații aritmetice, f-strings și conversii de tip.
---

# Lecția 02 · Operații și expresii

!!! tip "Ce vei învăța"
    - Operatorii aritmetici și ordinea operațiilor
    - Operații cu șiruri de caractere
    - F-strings — modul modern de a formata text
    - Conversia între tipuri: `int()`, `float()`, `str()`

---

## Operatori aritmetici

| Operator | Operație | Exemplu | Rezultat |
|----------|----------|---------|---------|
| `+` | adunare | `3 + 4` | `7` |
| `-` | scădere | `10 - 3` | `7` |
| `*` | înmulțire | `3 * 4` | `12` |
| `/` | împărțire (rezultat float) | `7 / 2` | `3.5` |
| `//` | împărțire întreagă | `7 // 2` | `3` |
| `%` | rest (modulo) | `7 % 2` | `1` |
| `**` | ridicare la putere | `2 ** 8` | `256` |

```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.3333...
print(10 // 3)  # 3
print(10 % 3)   # 1
print(2 ** 10)  # 1024
```

### Ordinea operațiilor

Python respectă regulile matematice: `**` → `* / // %` → `+ -`

```python
print(2 + 3 * 4)    # 14 (nu 20!)
print((2 + 3) * 4)  # 20 — parantezele schimbă ordinea
```

### Operatorul `%` — la ce folosește?

`%` returnează **restul** împărțirii. Util pentru a verifica paritatea:

```python
print(10 % 2)   # 0 — par
print(11 % 2)   # 1 — impar
print(15 % 5)   # 0 — divizibil cu 5
```

---

## Operații cu șiruri de caractere

### Concatenare cu `+`

```python
prenume = "Ana"
nume = "Pop"
print(prenume + " " + nume)   # Ana Pop
```

### Repetare cu `*`

```python
print("Ha" * 3)    # HaHaHa
print("-" * 30)    # ------------------------------
```

### Funcții utile

```python
mesaj = "  Bun venit!  "
print(len(mesaj))           # 14
print(mesaj.upper())        # "  BUN VENIT!  "
print(mesaj.lower())        # "  bun venit!  "
print(mesaj.strip())        # "Bun venit!"
print(mesaj.strip().upper()) # "BUN VENIT!"
```

---

## F-strings

F-strings îți permit să inserezi variabile direct în text:

```python
nume = "Mihai"
varsta = 14
print(f"Mă numesc {nume} și am {varsta} ani.")
# Mă numesc Mihai și am 14 ani.
```

### Formatarea numerelor

```python
pi = 3.14159265
print(f"Pi ≈ {pi:.2f}")   # Pi ≈ 3.14
print(f"Pi ≈ {pi:.4f}")   # Pi ≈ 3.1416
```

### Calcule în f-strings

```python
latime = 4
lungime = 7
print(f"Aria dreptunghiului: {latime * lungime} m²")
# Aria dreptunghiului: 28 m²
```

---

## Conversii de tip

| Funcție | Ce face |
|---------|---------|
| `int(x)` | transformă în număr întreg |
| `float(x)` | transformă în număr zecimal |
| `str(x)` | transformă în text |

```python
print(int(3.9))      # 3  (taie zecimalele, nu rotunjește!)
print(int("42"))     # 42
print(float(5))      # 5.0
print(float("3.14")) # 3.14
print(str(100))      # "100"
```

!!! warning "Conversii invalide"
    ```python
    int("salut")    # ValueError
    int("3.14")     # ValueError — folosește int(float("3.14"))
    ```

---

## Exerciții

### Exercițiu 1 — Calculează
Fără a rula codul, calculează:

```python
print(17 % 5)
print(2 ** 3 + 1)
print(15 // 4)
```

??? success "Răspuns"
    - `17 % 5` → `2`
    - `2 ** 3 + 1` → `9`
    - `15 // 4` → `3`

### Exercițiu 2 — F-string
```python
produs = "caiet"
pret = 3.5
cantitate = 4
```
Afișează: `4 caiete costă 14.0 lei.`

??? success "Soluție"
    ```python
    print(f"{cantitate} {produs}e costă {pret * cantitate} lei.")
    ```

### Exercițiu 3 — Par sau impar?
Afișează restul împărțirii lui 47 la 2.

??? success "Soluție"
    ```python
    print(47 % 2)   # 1 — deci impar
    ```

---

## Mini-proiect: Convertor de temperaturi

Convertește 100 °C în Fahrenheit și Kelvin.

**Formule:** `F = C × 9/5 + 32` și `K = C + 273.15`

**Output:**
```
Temperatura: 100 °C
În Fahrenheit: 212.0 °F
În Kelvin: 373.15 K
```

??? success "Soluție"
    ```python
    celsius = 100
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    print(f"Temperatura: {celsius} °C")
    print(f"În Fahrenheit: {fahrenheit} °F")
    print(f"În Kelvin: {kelvin} K")
    ```

---

## Rezumat

- Operatori aritmetici: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- `%` returnează restul — util pentru paritate
- F-strings `f"text {variabila}"` — formatare modernă
- Conversii: `int()`, `float()`, `str()`

---

**Pasul următor:** [→ Lecția 03: Input și Output](03-input-output.md)
