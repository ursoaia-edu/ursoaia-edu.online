---
lesson: 0
tags: [python, instalare, thonny, primul-program]
summary: Instalează Thonny, înțelege ce este Python și scrie primul tău program.
---

# Lecția 00 · Pregătire

!!! tip "Ce vei învăța"
    - Ce este Python și la ce se folosește
    - Cum instalezi și folosești Thonny IDE
    - Cum scrii și rulezi primul program Python
    - Cum citești un mesaj de eroare

---

## Ce este Python?

**Python** este un limbaj de programare creat în 1991 de Guido van Rossum. Astăzi este unul dintre cele mai populare limbaje din lume — și din motive bune:

- Se citește aproape ca engleza obișnuită
- Funcționează pe Windows, macOS și Linux
- Este folosit pentru **jocuri**, **inteligență artificială**, **site-uri web**, **analize de date**, **robotică**

!!! note "Python este gratuit"
    Python este open-source. Poți să îl descarci, folosești și distribui fără nicio restricție.

---

## Instrumentul nostru: Thonny

**Thonny** este un editor de cod creat special pentru a învăța Python. Este simplu, are un depanator vizual și vine cu Python deja inclus.

### Instalare

1. Mergi la [https://thonny.org](https://thonny.org)
2. Descarcă varianta pentru sistemul tău (Windows / macOS / Linux)
3. Rulează installerul — toate setările implicite sunt bune
4. Deschide Thonny

!!! tip "Alternativă online"
    Dacă nu poți instala programe, folosește [repl.it](https://repl.it) — creează un cont gratuit și rulezi Python direct în browser.

### Cum arată Thonny

```
┌─────────────────────────────────────────────────┐
│  [Editor] — scrii codul aici                    │
│                                                 │
│  print("Salut, lume!")                          │
│                                                 │
├─────────────────────────────────────────────────┤
│  [Shell] — vezi rezultatele când rulezi         │
│                                                 │
│  Salut, lume!                                   │
└─────────────────────────────────────────────────┘
```

- **Editorul** (sus) — unde scrii programele
- **Shell-ul** (jos) — unde apar rezultatele

---

## Primul program

### 1. Scrie codul

În editorul Thonny, scrie exact:

```python
print("Salut, lume!")
```

### 2. Rulează

Apasă butonul **▶ Run** sau tasta `F5`.

### 3. Privește rezultatul

```
Salut, lume!
```

Felicitări — ai scris primul tău program Python!

---

## Funcția `print()`

`print()` este o **funcție** — un bloc de cod gata făcut care face ceva. În cazul acesta, afișează text pe ecran.

Textul se pune între **ghilimele** (simple `'` sau duble `"`) și **între paranteze**:

```python
print("Python este distractiv!")
print('Și eu pot programa.')
print("Ursoaia Edu Online")
```

Fiecare `print()` afișează o linie nouă.

---

## Citirea erorilor

Greșelile sunt normale și inevitabile. Iată un exemplu:

```python
print("Salut, lume!"
```

Python va afișa:

```
SyntaxError: '(' was never closed
```

**Traducere:** paranteza `(` nu a fost niciodată închisă.

**Soluție:** adaugă `)` la final.

!!! warning "Erorile sunt prietenii tăi"
    Fiecare eroare îți spune exact ce nu a mers și pe ce linie. Citește mesajul cu atenție înainte de a modifica codul.

---

## Shell-ul interactiv

În zona de jos din Thonny poți testa comenzi Python direct, fără să salvezi un fișier:

```python
>>> 2 + 3
5
>>> "Ana" + " are " + "mere"
'Ana are mere'
```

`>>>` înseamnă că Python așteaptă o comandă. Ideal pentru a testa rapid idei.

---

## Exerciții

### Exercițiu 1 — Trei lucruri despre tine
Scrie un program care afișează numele tău, vârsta și orașul natal, fiecare pe o linie separată.

??? success "Soluție"
    ```python
    print("Maria")
    print(14)
    print("Timișoara")
    ```

### Exercițiu 2 — Câte linii?
Câte linii va afișa programul următor?

```python
print("Unu")
print("Doi")
print("Trei")
```

??? success "Răspuns"
    **3 linii.** Fiecare `print()` produce o linie nouă.

### Exercițiu 3 — Găsește eroarea
Ce este greșit?

```python
print("Bună ziua!
```

??? success "Răspuns"
    Lipsesc ghilimelele de închidere `"` și paraneza de închidere `)`.
    ```python
    print("Bună ziua!")
    ```

---

## Mini-proiect: Cartea ta de vizită

Scrie un program care afișează o carte de vizită cu informații despre tine.

**Exemplu de output:**
```
==============================
  Numele meu: Maria Ionescu
  Vârsta: 14 ani
  Școala: Liceul Teoretic X
  Hobby: programare, fotbal
==============================
```

??? success "Soluție"
    ```python
    print("==============================")
    print("  Numele meu: Maria Ionescu")
    print("  Vârsta: 14 ani")
    print("  Școala: Liceul Teoretic X")
    print("  Hobby: programare, fotbal")
    print("==============================")
    ```
    Modifică cu datele tale reale!

---

## Rezumat

- Python este un limbaj de programare simplu și puternic
- Thonny este editorul nostru recomandat pentru a scrie cod
- `print()` afișează text pe ecran
- Erorile sunt normale — citește mesajul și corectează

---

**Pasul următor:** [→ Lecția 01: Variabile și tipuri de date](01-variabile-si-tipuri.md)
