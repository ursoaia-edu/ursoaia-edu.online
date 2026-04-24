---
lesson: 10
tags: [python, proiect, joc, aventură-text, funcții, dicționare, fișiere]
summary: Proiect final — construiești un joc de aventură text complet, pas cu pas.
---

# Lecția 10 · Proiect: Joc de aventură text

!!! tip "Ce vei exersa"
    - Variabile, condiții, bucle
    - Funcții și organizarea codului
    - Dicționare pentru date structurate
    - Fișiere pentru salvarea progresului

---

## Prezentarea proiectului

Vei construi un **joc de aventură text** simplu în care jucătorul explorează camere, culege obiecte și trebuie să ajungă la ieșire.

**Exemplu de rulare:**
```
=== AVENTURA ÎN CASTELUL MISTERIOS ===

Ești în: Intrare
Descriere: O sală mare cu podea de piatră. Simți un curent rece.
Obiecte: ['torță']
Ieșiri: ['nord']

Ce faci? (du-te [direcție] / ia [obiect] / inventar / ieși): ia torță
Ai luat: torță

Ce faci?: du-te nord

Ești în: Coridor
Descriere: Un coridor îngust. La capăt vezi o ușă masivă.
Obiecte: ['cheie']
Ieșiri: ['sud', 'nord']
```

---

## Pasul 1: Structura lumii

Mai întâi definim camerele ca dicționar:

```python
lume = {
    "intrare": {
        "nume": "Intrare",
        "descriere": "O sală mare cu podea de piatră. Simți un curent rece.",
        "obiecte": ["torță"],
        "iesiri": {"nord": "coridor"}
    },
    "coridor": {
        "nume": "Coridor",
        "descriere": "Un coridor îngust. La capăt vezi o ușă masivă.",
        "obiecte": ["cheie"],
        "iesiri": {"sud": "intrare", "nord": "sala_tezaur"}
    },
    "sala_tezaur": {
        "nume": "Sala Tezaurului",
        "descriere": "O cameră plină de aur! Dar ușa de ieșire e încuiată...",
        "obiecte": ["tezaur"],
        "iesiri": {"sud": "coridor", "est": "iesire"}
    },
    "iesire": {
        "nume": "Ieșire",
        "descriere": "Ai ieșit din castel! Felicitări, aventurier!",
        "obiecte": [],
        "iesiri": {}
    }
}
```

## Pasul 2: Starea jucătorului

```python
jucator = {
    "camera_curenta": "intrare",
    "inventar": [],
    "pasi": 0
}
```

## Pasul 3: Funcțiile de bază

```python
def afiseaza_camera(lume, jucator):
    camera = lume[jucator["camera_curenta"]]
    print(f"\nEști în: {camera['nume']}")
    print(f"Descriere: {camera['descriere']}")
    if camera["obiecte"]:
        print(f"Obiecte: {camera['obiecte']}")
    print(f"Ieșiri: {list(camera['iesiri'].keys())}")

def deplaseaza(lume, jucator, directie):
    camera = lume[jucator["camera_curenta"]]
    if directie in camera["iesiri"]:
        jucator["camera_curenta"] = camera["iesiri"][directie]
        jucator["pasi"] += 1
        print(f"Te deplasezi spre {directie}...")
    else:
        print("Nu poți merge în acea direcție.")

def ia_obiect(lume, jucator, obiect):
    camera = lume[jucator["camera_curenta"]]
    if obiect in camera["obiecte"]:
        camera["obiecte"].remove(obiect)
        jucator["inventar"].append(obiect)
        print(f"Ai luat: {obiect}")
    else:
        print(f"Nu există '{obiect}' în această cameră.")

def afiseaza_inventar(jucator):
    if jucator["inventar"]:
        print(f"Inventar: {jucator['inventar']}")
    else:
        print("Inventarul tău este gol.")
```

## Pasul 4: Bucla principală a jocului

```python
def joc():
    print("=== AVENTURA ÎN CASTELUL MISTERIOS ===\n")
    print("Comenzi: du-te [direcție] | ia [obiect] | inventar | ieși\n")

    while True:
        afiseaza_camera(lume, jucator)

        # Verifică dacă a ajuns la ieșire
        if jucator["camera_curenta"] == "iesire":
            print(f"\nAi terminat jocul în {jucator['pasi']} pași!")
            print(f"Inventar final: {jucator['inventar']}")
            break

        comanda = input("\nCe faci? ").strip().lower()

        if comanda.startswith("du-te "):
            directie = comanda[6:]
            deplaseaza(lume, jucator, directie)

        elif comanda.startswith("ia "):
            obiect = comanda[3:]
            ia_obiect(lume, jucator, obiect)

        elif comanda == "inventar":
            afiseaza_inventar(jucator)

        elif comanda == "ieși":
            print("Ai abandonat aventura.")
            break

        else:
            print("Comandă necunoscută. Încearcă: du-te [direcție], ia [obiect], inventar, ieși")

joc()
```

## Codul complet

Iată jocul complet, combinând toți pașii:

```python
# === Joc de aventură text ===

lume = {
    "intrare": {
        "nume": "Intrare",
        "descriere": "O sală mare cu podea de piatră. Simți un curent rece.",
        "obiecte": ["torță"],
        "iesiri": {"nord": "coridor"}
    },
    "coridor": {
        "nume": "Coridor",
        "descriere": "Un coridor îngust. La capăt vezi o ușă masivă.",
        "obiecte": ["cheie"],
        "iesiri": {"sud": "intrare", "nord": "sala_tezaur"}
    },
    "sala_tezaur": {
        "nume": "Sala Tezaurului",
        "descriere": "O cameră plină de aur! Dar ușa de ieșire e încuiată...",
        "obiecte": ["tezaur"],
        "iesiri": {"sud": "coridor", "est": "iesire"}
    },
    "iesire": {
        "nume": "Ieșire",
        "descriere": "Ai ieșit din castel! Felicitări, aventurier!",
        "obiecte": [],
        "iesiri": {}
    }
}

jucator = {
    "camera_curenta": "intrare",
    "inventar": [],
    "pasi": 0
}

def afiseaza_camera(lume, jucator):
    camera = lume[jucator["camera_curenta"]]
    print(f"\nEști în: {camera['nume']}")
    print(f"Descriere: {camera['descriere']}")
    if camera["obiecte"]:
        print(f"Obiecte: {camera['obiecte']}")
    print(f"Ieșiri: {list(camera['iesiri'].keys())}")

def deplaseaza(lume, jucator, directie):
    camera = lume[jucator["camera_curenta"]]
    if directie in camera["iesiri"]:
        jucator["camera_curenta"] = camera["iesiri"][directie]
        jucator["pasi"] += 1
    else:
        print("Nu poți merge în acea direcție.")

def ia_obiect(lume, jucator, obiect):
    camera = lume[jucator["camera_curenta"]]
    if obiect in camera["obiecte"]:
        camera["obiecte"].remove(obiect)
        jucator["inventar"].append(obiect)
        print(f"Ai luat: {obiect}")
    else:
        print(f"Nu există '{obiect}' în această cameră.")

def joc():
    print("=== AVENTURA ÎN CASTELUL MISTERIOS ===\n")
    print("Comenzi: du-te [direcție] | ia [obiect] | inventar | ieși\n")

    while True:
        afiseaza_camera(lume, jucator)

        if jucator["camera_curenta"] == "iesire":
            print(f"\nFelicitări! Ai terminat în {jucator['pasi']} pași.")
            print(f"Inventar final: {jucator['inventar']}")
            break

        comanda = input("\nCe faci? ").strip().lower()

        if comanda.startswith("du-te "):
            deplaseaza(lume, jucator, comanda[6:])
        elif comanda.startswith("ia "):
            ia_obiect(lume, jucator, comanda[3:])
        elif comanda == "inventar":
            if jucator["inventar"]:
                print(f"Inventar: {jucator['inventar']}")
            else:
                print("Inventarul tău este gol.")
        elif comanda == "ieși":
            print("Ai abandonat aventura.")
            break
        else:
            print("Comandă necunoscută.")

joc()
```

---

## Idei de extindere

- Adaugă mai multe camere și obiecte
- Implementează o ușă care se deschide doar dacă ai cheia
- Salvează progresul în JSON (din Lecția 09)
- Adaugă un sistem de puncte sau viață
- Creează un monstru care blochează un coridor

---

**Pasul următor:** [→ Proiect: Grafice cu Turtle](11-proiect-turtle.md)
