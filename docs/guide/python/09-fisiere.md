---
lesson: 9
tags: [python, fișiere, citire, scriere, csv, json]
summary: Citește și scrie date din fișiere text, CSV și JSON.
---

# Lecția 09 · Fișiere

!!! tip "Ce vei învăța"
    - Deschiderea și închiderea fișierelor cu `with open()`
    - Citirea: `read()`, `readline()`, `readlines()`
    - Scrierea: `write()`, `writelines()`
    - Lucrul cu fișiere CSV și JSON

---

## De ce fișiere?

Până acum, datele din programele noastre dispăreau când programul se închidea. Fișierele permit **persistența datelor** — le salvezi și le recitești mai târziu.

---

## Deschiderea unui fișier

```python
with open("date.txt", "r") as f:
    continut = f.read()
print(continut)
```

- `"date.txt"` — numele fișierului
- `"r"` — modul de deschidere (read = citire)
- `as f` — variabila prin care accesezi fișierul
- `with` — închide automat fișierul la ieșirea din bloc

### Modurile de deschidere

| Mod | Semnificație |
|-----|-------------|
| `"r"` | citire (fișierul trebuie să existe) |
| `"w"` | scriere (creează sau suprascrie fișierul) |
| `"a"` | adăugare la final (append) |
| `"r+"` | citire și scriere |

---

## Citirea

### `read()` — tot fișierul ca un șir

```python
with open("salut.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
```

### `readlines()` — o listă cu liniile

```python
with open("salut.txt", "r", encoding="utf-8") as f:
    linii = f.readlines()

for linie in linii:
    print(linie.strip())   # .strip() elimină \n de la final
```

### `readline()` — o linie pe rând

```python
with open("salut.txt", "r", encoding="utf-8") as f:
    prima = f.readline()
    a_doua = f.readline()
```

!!! tip "encoding='utf-8'"
    Adaugă întotdeauna `encoding="utf-8"` pentru a suporta diacriticele românești (ă, î, ș, ț, â).

---

## Scrierea

```python
with open("rezultate.txt", "w", encoding="utf-8") as f:
    f.write("Andrei: 95\n")
    f.write("Maria: 87\n")
    f.write("Radu: 91\n")
```

!!! warning "Modul `'w'` suprascrie!"
    Dacă fișierul există deja, `"w"` îl șterge și o ia de la capăt. Folosește `"a"` pentru a adăuga la final.

### Adăugare la fișier existent

```python
with open("rezultate.txt", "a", encoding="utf-8") as f:
    f.write("Elena: 99\n")
```

---

## Fișiere CSV

CSV (Comma-Separated Values) = valori separate prin virgulă. Ideal pentru tabele simple.

```python
import csv

# Scriere CSV
with open("elevi.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nume", "Nota", "Clasa"])   # header
    writer.writerow(["Ana", 9.5, "8A"])
    writer.writerow(["Mihai", 8.0, "8B"])

# Citire CSV
with open("elevi.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for rand in reader:
        print(rand)
# ['Nume', 'Nota', 'Clasa']
# ['Ana', '9.5', '8A']
# ['Mihai', '8.0', '8B']
```

---

## Fișiere JSON

JSON (JavaScript Object Notation) = format de date structurate. Ideal pentru dicționare și liste.

```python
import json

# Scriere JSON
date = {
    "elev": "Andrei",
    "note": [8, 9, 7, 10],
    "medie": 8.5
}

with open("elev.json", "w", encoding="utf-8") as f:
    json.dump(date, f, ensure_ascii=False, indent=2)

# Citire JSON
with open("elev.json", "r", encoding="utf-8") as f:
    date_citite = json.load(f)

print(date_citite["elev"])    # Andrei
print(date_citite["note"])    # [8, 9, 7, 10]
```

---

## Exerciții

### Exercițiu 1 — Scrie și citește
Scrie un program care salvează 3 propoziții într-un fișier, apoi le recitește și le afișează numerotate.

??? success "Soluție"
    ```python
    propozitii = [
        "Python este distractiv.",
        "Fișierele păstrează datele.",
        "Programarea deschide uși."
    ]

    with open("propozitii.txt", "w", encoding="utf-8") as f:
        for p in propozitii:
            f.write(p + "\n")

    with open("propozitii.txt", "r", encoding="utf-8") as f:
        for i, linie in enumerate(f, 1):
            print(f"{i}. {linie.strip()}")
    ```

### Exercițiu 2 — Numărare cuvinte
Citește un fișier text și afișează numărul de linii și de cuvinte.

??? success "Soluție"
    ```python
    with open("propozitii.txt", "r", encoding="utf-8") as f:
        linii = f.readlines()

    nr_linii = len(linii)
    nr_cuvinte = sum(len(linie.split()) for linie in linii)
    print(f"Linii: {nr_linii}, Cuvinte: {nr_cuvinte}")
    ```

---

## Mini-proiect: Scoreboard persistent

Creează un program care salvează și afișează un clasament de scoruri în format JSON.

**Funcționalitate:**
- Cere un nume și un scor
- Adaugă la clasament
- Afișează top-ul sortat
- Salvează între rulări

??? success "Soluție"
    ```python
    import json
    import os

    FISIER = "scoruri.json"

    def incarca_scoruri():
        if os.path.exists(FISIER):
            with open(FISIER, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def salveaza_scoruri(scoruri):
        with open(FISIER, "w", encoding="utf-8") as f:
            json.dump(scoruri, f, ensure_ascii=False, indent=2)

    scoruri = incarca_scoruri()

    nume = input("Numele tău: ")
    scor = int(input("Scorul tău: "))
    scoruri.append({"nume": nume, "scor": scor})

    scoruri.sort(key=lambda x: x["scor"], reverse=True)
    salveaza_scoruri(scoruri)

    print("\n=== CLASAMENT ===")
    for i, intrare in enumerate(scoruri[:5], 1):
        print(f"#{i}: {intrare['nume']} — {intrare['scor']}")
    ```

---

## Rezumat

- `with open("fișier", "mod", encoding="utf-8") as f:` — deschide fișierul sigur
- Moduri: `"r"` citire, `"w"` scriere, `"a"` adăugare
- `f.read()` — tot ca șir; `f.readlines()` — lista liniilor
- Modulul `csv` pentru tabele; modulul `json` pentru date structurate
- `encoding="utf-8"` — obligatoriu pentru caractere românești

---

**Pasul următor:** [→ Proiect: Joc de aventură text](10-proiect-joc-aventura.md)
