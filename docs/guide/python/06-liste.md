---
lesson: 6
tags: [python, liste, indexare, slice, metode-liste]
summary: Stochează și manipulează colecții de valori cu listele Python.
---

# Lecția 06 · Liste

!!! tip "Ce vei învăța"
    - Cum creezi și accesezi o listă
    - Indexare și slice
    - Metodele principale ale listelor
    - Iterarea peste liste cu `for`

---

## Ce este o listă?

O **listă** stochează mai multe valori într-o singură variabilă, în ordine:

```python
note = [8, 9, 7, 10, 6]
fructe = ["măr", "pară", "cireașă"]
mixt = [42, "salut", True, 3.14]   # poate conține tipuri diferite
goala = []                          # lista goală
```

---

## Indexarea

Fiecare element are un **index** (poziție), care începe de la `0`:

```python
fructe = ["măr", "pară", "cireașă", "coacăz"]
#           0       1        2          3

print(fructe[0])   # măr
print(fructe[2])   # cireașă
print(fructe[-1])  # coacăz — ultimul element
print(fructe[-2])  # cireașă — penultimul
```

!!! note "Indexarea negativă"
    `-1` este ultimul element, `-2` penultimul, etc.

---

## Slice — sub-liste

```python
note = [5, 7, 8, 9, 10]
#        0  1  2  3   4

print(note[1:3])    # [7, 8]      — de la index 1 la 3 (exclusiv)
print(note[:3])     # [5, 7, 8]  — de la început la 3
print(note[2:])     # [8, 9, 10] — de la 2 până la final
print(note[::2])    # [5, 8, 10] — fiecare al doilea element
print(note[::-1])   # [10, 9, 8, 7, 5] — lista inversată
```

---

## Modificarea listelor

```python
culori = ["roșu", "verde", "albastru"]

culori[1] = "galben"
print(culori)   # ["roșu", "galben", "albastru"]
```

---

## Metodele principale

```python
note = [8, 6, 9, 7]

note.append(10)         # adaugă la final: [8, 6, 9, 7, 10]
note.insert(0, 5)       # inserează la poziția 0: [5, 8, 6, 9, 7, 10]
note.remove(6)          # elimină prima apariție a lui 6
nota_scoasa = note.pop()     # scoate și returnează ultimul element
nota_scoasa = note.pop(0)    # scoate și returnează elementul de la index 0
note.sort()             # sortează crescător (modifică lista originală)
note.sort(reverse=True) # sortează descrescător
note.reverse()          # inversează lista
print(len(note))        # numărul de elemente
print(note.count(9))    # de câte ori apare 9
print(note.index(9))    # indexul primei apariții a lui 9
```

---

## Iterarea cu `for`

```python
fructe = ["măr", "pară", "cireașă"]

for fruct in fructe:
    print(fruct)
```

### `enumerate()` — index și valoare

```python
for i, fruct in enumerate(fructe):
    print(f"{i}: {fruct}")
# 0: măr
# 1: pară
# 2: cireașă
```

---

## Funcții utile

```python
note = [8, 6, 9, 7, 10]

print(len(note))    # 5
print(sum(note))    # 40
print(max(note))    # 10
print(min(note))    # 6
print(sorted(note)) # [6, 7, 8, 9, 10] — nu modifică originala
```

---

## Verificarea apartenenței cu `in`

```python
fructe = ["măr", "pară", "cireașă"]

print("pară" in fructe)       # True
print("ananas" in fructe)     # False
print("ananas" not in fructe) # True
```

---

## Exerciții

### Exercițiu 1 — Accesare
Ai lista `planete = ["Mercur", "Venus", "Pământ", "Marte"]`. Afișează prima și ultima planetă.

??? success "Soluție"
    ```python
    planete = ["Mercur", "Venus", "Pământ", "Marte"]
    print(planete[0])    # Mercur
    print(planete[-1])   # Marte
    ```

### Exercițiu 2 — Suma notelor
Cere 5 note de la utilizator, stochează-le într-o listă și afișează suma și media.

??? success "Soluție"
    ```python
    note = []
    for i in range(5):
        nota = float(input(f"Nota {i + 1}: "))
        note.append(nota)
    print(f"Suma: {sum(note)}")
    print(f"Media: {sum(note) / len(note):.2f}")
    ```

### Exercițiu 3 — Filtrare
Din lista `[3, 7, 2, 9, 4, 6, 1, 8, 5]`, creează o nouă listă doar cu numerele mai mari decât 5.

??? success "Soluție"
    ```python
    numere = [3, 7, 2, 9, 4, 6, 1, 8, 5]
    mari = []
    for n in numere:
        if n > 5:
            mari.append(n)
    print(mari)   # [7, 9, 6, 8]
    ```

---

## Mini-proiect: Top 5 scoruri

Cere 5 scoruri de la utilizator, sortează-le descrescător și afișează clasamentul.

**Exemplu:**
```
Scor 1: 850
Scor 2: 1200
Scor 3: 450
Scor 4: 990
Scor 5: 750

=== TOP 5 SCORURI ===
#1: 1200
#2: 990
#3: 850
#4: 750
#5: 450
```

??? success "Soluție"
    ```python
    scoruri = []
    for i in range(5):
        scor = int(input(f"Scor {i + 1}: "))
        scoruri.append(scor)

    scoruri.sort(reverse=True)

    print()
    print("=== TOP 5 SCORURI ===")
    for i, scor in enumerate(scoruri):
        print(f"#{i + 1}: {scor}")
    ```

---

## Rezumat

- Listele stochează mai multe valori: `[val1, val2, val3]`
- Indexarea începe de la `0`; indexele negative numără de la final
- Slice: `lista[start:stop:pas]`
- Metode cheie: `append()`, `remove()`, `sort()`, `pop()`, `len()`
- `for elem in lista:` iterează peste toate elementele
- `x in lista` verifică dacă `x` există în listă

---

**Pasul următor:** [→ Lecția 07: Dicționare](07-dictionare.md)
