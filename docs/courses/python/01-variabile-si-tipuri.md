---
lesson: 1
tags: [python, variabile, tipuri-de-date, int, float, str, bool]
summary: Înțelege variabilele și cele patru tipuri de date de bază din Python.
---

# Lecția 01 · Variabile și tipuri de date

!!! tip "Ce vei învăța"
    - Ce este o variabilă și cum o creezi
    - Cele 4 tipuri de bază: `int`, `float`, `str`, `bool`
    - Cum afli tipul unei valori cu `type()`
    - Regulile de denumire a variabilelor

---

## Ce este o variabilă?

O variabilă este o **cutie cu etichetă** în care stochezi o valoare. Eticheta este **numele** variabilei, iar conținutul cutiei este **valoarea** ei.

```python
varsta = 14
nume = "Andrei"
este_premiant = True
```

De fiecare dată când scrii `varsta`, Python îți dă valoarea `14`.

### Crearea unei variabile

```python
# sintaxa: nume_variabila = valoare
scor = 100
oras = "București"
temperatura = 36.6
```

Semnul `=` este **operatorul de atribuire** — nu înseamnă "egal", ci "stochează valoarea din dreapta în variabila din stânga".

!!! note "Variabilele pot fi schimbate"
    ```python
    scor = 100
    print(scor)   # 100
    scor = 250
    print(scor)   # 250
    ```

---

## Cele 4 tipuri de bază

### 1. `int` — numere întregi

```python
varsta = 14
numar_elevi = 32
temperatura_minima = -5
```

Fără virgulă, fără ghilimele.

### 2. `float` — numere zecimale

```python
inaltime = 1.75
nota = 9.5
pi = 3.14159
```

!!! note "Punct, nu virgulă"
    Python folosește **punctul** ca separator zecimal: `9.5` ✓, nu `9,5` ✗

### 3. `str` — șiruri de caractere (text)

```python
prenume = "Ana"
mesaj = 'Bun venit!'
fraza = "Am 14 ani și locuiesc în Cluj."
```

Ghilimelele simple `'...'` și duble `"..."` funcționează la fel.

### 4. `bool` — valori logice

```python
este_major = False
a_luat_nota_mare = True
```

Doar două valori posibile: `True` sau `False` (cu majusculă obligatorie!).

---

## Funcția `type()`

```python
print(type(14))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("salut"))   # <class 'str'>
print(type(True))      # <class 'bool'>
```

---

## Regulile de denumire

| Regulă | Corect | Greșit |
|--------|--------|--------|
| Literă sau `_` la început | `varsta`, `_x` | `1varsta`, `@scor` |
| Fără spații | `numar_elevi` | `numar elevi` |
| Litere, cifre, `_` | `scor_joc2` | `scor-joc` |
| Sensibil la majuscule | `Varsta ≠ varsta` | — |
| Fără cuvinte rezervate | — | `if`, `for`, `while` |

### Convenții de scriere

```python
# snake_case — recomandat pentru variabile
numar_de_elevi = 32
temperatura_maxima = 37.5

# MAJUSCULE — pentru constante (valori care nu se schimbă)
PI = 3.14159
VITEZA_LUMINII = 299792458
```

---

## Afișarea variabilelor

```python
nume = "Elena"
varsta = 15

print(nume)           # Elena
print(varsta)         # 15
print(nume, varsta)   # Elena 15
```

---

## Exerciții

### Exercițiu 1 — Definește variabile
Creează variabile pentru: numele tău (`str`), vârsta ta (`int`), media ta la matematică (`float`) și dacă ești în clasa a 9-a (`bool`).

??? success "Soluție"
    ```python
    nume = "Mihai"
    varsta = 15
    medie_matematica = 9.25
    este_clasa_9 = True
    ```

### Exercițiu 2 — Ce tip?
Ce tip are fiecare valoare?

```python
x = 42
y = "42"
z = 42.0
w = False
```

??? success "Răspuns"
    - `x = 42` → `int`
    - `y = "42"` → `str` (ghilimelele fac diferența!)
    - `z = 42.0` → `float` (punctul zecimal contează)
    - `w = False` → `bool`

### Exercițiu 3 — Urmărește valoarea
Ce afișează programul următor?

```python
puncte = 10
puncte = puncte + 5
puncte = puncte * 2
print(puncte)
```

??? success "Răspuns"
    ```
    30
    ```
    `10 + 5 = 15`, apoi `15 × 2 = 30`.

### Exercițiu 4 — Găsește erorile
Ce este greșit?

```python
numar elevi = 30
2scor = 100
if = "cuvânt"
```

??? success "Răspuns"
    - `numar elevi` → spațiu interzis → `numar_elevi`
    - `2scor` → nu poate începe cu cifră → `scor2`
    - `if` → cuvânt rezervat Python → alege alt nume, ex: `cuvant`

---

## Mini-proiect: Fișa personală

Creează variabile pentru o persoană și afișează-le formatat.

**Output așteptat:**
```
=== Fișa personală ===
Nume: Radu Popescu
Vârsta: 13
Clasa: 7
Medie generală: 9.8
Este premiant: True
```

??? success "Soluție"
    ```python
    nume = "Radu Popescu"
    varsta = 13
    clasa = 7
    medie = 9.8
    este_premiant = True

    print("=== Fișa personală ===")
    print("Nume:", nume)
    print("Vârsta:", varsta)
    print("Clasa:", clasa)
    print("Medie generală:", medie)
    print("Este premiant:", este_premiant)
    ```

---

## Rezumat

- O **variabilă** stochează o valoare sub un nume ales de tine
- Tipuri de bază: `int`, `float`, `str`, `bool`
- `type(x)` îți spune tipul valorii `x`
- Folosește `snake_case` pentru denumirea variabilelor

---

**Pasul următor:** [→ Lecția 02: Operații și expresii](02-operatii-expresii.md)
