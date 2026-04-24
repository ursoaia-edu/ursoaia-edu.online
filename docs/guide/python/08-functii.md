---
lesson: 8
tags: [python, funcții, def, parametri, return, scope]
summary: Organizează codul în blocuri reutilizabile cu funcțiile Python.
---

# Lecția 08 · Funcții

!!! tip "Ce vei învăța"
    - Cum definești și apelezi o funcție cu `def`
    - Parametri și argumente
    - Valoarea returnată cu `return`
    - Domeniul de vizibilitate (scope): local vs global
    - Parametri cu valori implicite

---

## De ce funcții?

Fără funcții, dacă vrei să calculezi aria unui dreptunghi de trei ori, scrii codul de trei ori. Cu funcții, îl scrii o dată și îl **apelezi** de câte ori ai nevoie:

```python
def aria_dreptunghi(lungime, latime):
    return lungime * latime

print(aria_dreptunghi(4, 5))    # 20
print(aria_dreptunghi(10, 3))   # 30
print(aria_dreptunghi(7, 7))    # 49
```

---

## Sintaxa de bază

```python
def salut():
    print("Bună ziua!")

salut()   # apelul funcției → Bună ziua!
```

### Anatomia unei funcții

```python
def calculeaza_medie(note):     # 'note' este parametrul
    suma = sum(note)
    medie = suma / len(note)
    return medie                # valoarea returnată

rezultat = calculeaza_medie([8, 9, 7, 10])
print(rezultat)   # 8.5
```

- `def` — cuvântul cheie pentru definirea funcției
- `calculeaza_medie` — numele funcției
- `note` — parametrul (datele de intrare)
- `return` — trimite înapoi o valoare

---

## Parametri și argumente

```python
def prezinta(nume, varsta):
    print(f"Mă numesc {nume} și am {varsta} ani.")

prezinta("Ana", 14)       # Ana, 14
prezinta("Mihai", 16)     # Mihai, 16
```

### Argumente cu cuvânt cheie

```python
prezinta(varsta=15, nume="Elena")   # ordinea nu contează
```

### Parametri cu valori implicite

```python
def salut(nume, mesaj="Bună ziua"):
    print(f"{mesaj}, {nume}!")

salut("Ana")              # Bună ziua, Ana!
salut("Mihai", "Salut")   # Salut, Mihai!
```

---

## Funcții fără `return`

O funcție fără `return` returnează implicit `None`:

```python
def afiseaza_titlu(text):
    print("=" * len(text))
    print(text)
    print("=" * len(text))

afiseaza_titlu("Clasament")
# ===========
# Clasament
# ===========
```

---

## Domeniul de vizibilitate (Scope)

Variabilele create **în interiorul** unei funcții sunt **locale** — nu există în afara ei:

```python
def calcul():
    x = 10   # variabilă locală
    print(x)

calcul()
print(x)   # NameError — x nu există aici!
```

Variabilele definite **în afara** oricărei funcții sunt **globale**:

```python
nume = "Global"   # variabilă globală

def afiseaza():
    print(nume)   # poate fi citită

afiseaza()   # Global
```

!!! warning "Evită modificarea variabilelor globale din funcții"
    Modificarea variabilelor globale din funcții face codul greu de urmărit. Preferă să transmiți valorile ca parametri și să le returnezi.

---

## Valori returnate multiple

Python poate returna mai multe valori simultan (ca un tuplu):

```python
def min_max(lista):
    return min(lista), max(lista)

minim, maxim = min_max([3, 7, 1, 9, 4])
print(minim)   # 1
print(maxim)   # 9
```

---

## Exerciții

### Exercițiu 1 — Funcție simplă
Scrie o funcție `patrat(n)` care returnează pătratul lui `n`.

??? success "Soluție"
    ```python
    def patrat(n):
        return n ** 2

    print(patrat(5))    # 25
    print(patrat(12))   # 144
    ```

### Exercițiu 2 — Celsius la Fahrenheit
Scrie o funcție `celsius_in_fahrenheit(c)` care convertește temperatura.

??? success "Soluție"
    ```python
    def celsius_in_fahrenheit(c):
        return c * 9 / 5 + 32

    print(celsius_in_fahrenheit(0))    # 32.0
    print(celsius_in_fahrenheit(100))  # 212.0
    ```

### Exercițiu 3 — Validare
Scrie o funcție `este_par(n)` care returnează `True` dacă `n` este par, `False` altfel.

??? success "Soluție"
    ```python
    def este_par(n):
        return n % 2 == 0

    print(este_par(4))   # True
    print(este_par(7))   # False
    ```

---

## Mini-proiect: Generator de parole

Scrie o funcție care generează o parolă aleatorie din litere mari, mici și cifre.

```python
import random
import string

def genereaza_parola(lungime=8):
    caractere = string.ascii_letters + string.digits
    parola = ""
    for _ in range(lungime):
        parola += random.choice(caractere)
    return parola

print(genereaza_parola())      # ex: "aB3xKp9Q"
print(genereaza_parola(12))    # ex: "kR7mNq2xPa5L"
```

??? note "Ce sunt `string.ascii_letters` și `random.choice`?"
    - `string.ascii_letters` = toate literele mici și mari: `abcde...XYZ`
    - `string.digits` = cifrele: `0123456789`
    - `random.choice(s)` = alege un caracter aleatoriu din șirul `s`

---

## Rezumat

- `def nume(param):` definește o funcție
- `return valoare` trimite înapoi rezultatul
- Parametrii cu valori implicite: `def f(x, y=0):`
- Variabilele locale există doar în interiorul funcției
- Funcțiile pot returna mai multe valori: `return a, b`

---

**Pasul următor:** [→ Lecția 09: Fișiere](09-fisiere.md)
