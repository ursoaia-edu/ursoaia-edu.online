---
lesson: 7
tags: [python, dicționare, dict, chei, valori]
summary: Stochează date structurate cu dicționarele Python — perechi cheie-valoare.
---

# Lecția 07 · Dicționare

!!! tip "Ce vei învăța"
    - Ce este un dicționar și când îl folosești
    - Cum creezi, accesezi și modifici un dicționar
    - Metodele principale: `.keys()`, `.values()`, `.items()`
    - Iterarea peste dicționar

---

## Ce este un dicționar?

Un **dicționar** stochează perechi **cheie → valoare**, ca un dicționar real unde cuvântul este cheia și definiția este valoarea:

```python
elev = {
    "nume": "Andrei",
    "varsta": 14,
    "medie": 9.5,
    "este_premiant": True
}
```

Spre deosebire de liste (unde accesezi prin index numeric), dicționarele se accesează prin **chei**:

```python
print(elev["nume"])    # Andrei
print(elev["medie"])   # 9.5
```

---

## Crearea unui dicționar

```python
# Dicționar gol
date = {}

# Dicționar cu valori inițiale
masina = {
    "marca": "Dacia",
    "model": "Logan",
    "an": 2020,
    "km": 45000
}
```

Cheile pot fi `str`, `int` sau `float`. Valorile pot fi orice tip.

---

## Accesarea valorilor

### Cu `[]`

```python
print(masina["marca"])   # Dacia
```

Dacă cheia nu există, primești `KeyError`.

### Cu `.get()` — mai sigur

```python
print(masina.get("culoare"))                   # None (fără eroare)
print(masina.get("culoare", "necunoscut"))      # necunoscut
```

---

## Adăugarea și modificarea

```python
masina["culoare"] = "alb"    # adaugă cheie nouă
masina["km"] = 46000          # modifică valoare existentă
print(masina)
```

---

## Ștergerea cheilor

```python
del masina["km"]              # șterge cheia
km = masina.pop("an", None)   # șterge și returnează valoarea
```

---

## Verificarea existenței cheii

```python
if "marca" in masina:
    print("Avem marca:", masina["marca"])
```

---

## Metodele principale

```python
persoana = {"nume": "Elena", "varsta": 16, "oras": "Cluj"}

print(persoana.keys())    # dict_keys(['nume', 'varsta', 'oras'])
print(persoana.values())  # dict_values(['Elena', 16, 'Cluj'])
print(persoana.items())   # dict_items([('nume', 'Elena'), ...])
print(len(persoana))      # 3
```

---

## Iterarea

### Doar chei

```python
for cheie in persoana:
    print(cheie)
# nume
# varsta
# oras
```

### Chei și valori cu `.items()`

```python
for cheie, valoare in persoana.items():
    print(f"{cheie}: {valoare}")
# nume: Elena
# varsta: 16
# oras: Cluj
```

---

## Dicționare imbricate

```python
clasa = {
    "Andrei": {"nota_ro": 9, "nota_mat": 8},
    "Maria": {"nota_ro": 10, "nota_mat": 9},
}

print(clasa["Maria"]["nota_mat"])   # 9
```

---

## Exerciții

### Exercițiu 1 — Capitala
Creează un dicționar cu 5 perechi țară-capitală. Cere o țară de la utilizator și afișează capitala (sau "Necunoscut" dacă nu există).

??? success "Soluție"
    ```python
    capitale = {
        "România": "București",
        "Franța": "Paris",
        "Germania": "Berlin",
        "Italia": "Roma",
        "Spania": "Madrid"
    }
    tara = input("Țara: ")
    print(capitale.get(tara, "Necunoscut"))
    ```

### Exercițiu 2 — Numărarea aparițiilor
Numără de câte ori apare fiecare literă din cuvântul `"programare"`.

??? success "Soluție"
    ```python
    cuvant = "programare"
    frecventa = {}
    for litera in cuvant:
        if litera in frecventa:
            frecventa[litera] += 1
        else:
            frecventa[litera] = 1
    for litera, count in frecventa.items():
        print(f"{litera}: {count}")
    ```

### Exercițiu 3 — Actualizare
Pornind de la `{"mere": 5, "pere": 3}`, adaugă `"cireșe": 10`, modifică merele la `8` și șterge perele.

??? success "Soluție"
    ```python
    cos = {"mere": 5, "pere": 3}
    cos["cireșe"] = 10
    cos["mere"] = 8
    del cos["pere"]
    print(cos)   # {'mere': 8, 'cireșe': 10}
    ```

---

## Mini-proiect: Carnet de contacte

Creează un mic program de gestiune a contactelor care permite adăugarea, căutarea și listarea contactelor.

**Exemplu de rulare:**
```
1. Adaugă contact
2. Caută contact
3. Listează toate
4. Ieșire
Alegerea ta: 1
Nume: Ana
Telefon: 0722123456
Contact adăugat!
```

??? success "Soluție"
    ```python
    contacte = {}

    while True:
        print("\n1. Adaugă contact")
        print("2. Caută contact")
        print("3. Listează toate")
        print("4. Ieșire")
        alegere = input("Alegerea ta: ")

        if alegere == "1":
            nume = input("Nume: ")
            telefon = input("Telefon: ")
            contacte[nume] = telefon
            print("Contact adăugat!")
        elif alegere == "2":
            nume = input("Caută după nume: ")
            print(contacte.get(nume, "Contact negăsit."))
        elif alegere == "3":
            if contacte:
                for nume, tel in contacte.items():
                    print(f"{nume}: {tel}")
            else:
                print("Niciun contact salvat.")
        elif alegere == "4":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.")
    ```

---

## Rezumat

- Dicționarele stochează perechi cheie-valoare: `{"cheie": valoare}`
- Accesare: `dict["cheie"]` sau `dict.get("cheie", implicit)`
- Adăugare/modificare: `dict["cheie"] = valoare`
- Ștergere: `del dict["cheie"]` sau `dict.pop("cheie")`
- Iterare cu `.items()` pentru chei și valori simultan
- Verificare: `"cheie" in dict`

---

**Pasul următor:** [→ Lecția 08: Funcții](08-functii.md)
