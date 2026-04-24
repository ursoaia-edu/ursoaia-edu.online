---
lesson: 1
tags: [web, html, vscode, live-server, doctype, utf-8]
summary: Creează prima ta pagină HTML, înțelege structura minimă a unui document HTML5 și stabilește un flux de lucru save→refresh.
---

# Lecția 01 · Prima ta pagină

!!! tip "Ce vei învăța"
    - Cum creezi un fișier `.html` și un folder pentru proiect
    - **Structura minimă** a unui document HTML5
    - La ce servește fiecare linie din `<head>` și `<body>`
    - Fluxul de lucru: **editor → salvează → browser**
    - Erori frecvente la început (diacritice, taguri neînchise)

---

## Crearea fișierului

Orice site pornește de la un **folder** în care pui fișierele tale. Pe calculator:

1. Creează un folder nou, de exemplu `site-meu` pe Desktop.
2. Deschide **VS Code** → `File` → `Open Folder...` → alege `site-meu`.
3. În VS Code, dă click dreapta în panoul din stânga → `New File` → numește-l **`index.html`**.

!!! warning "Extensia `.html` este obligatorie"
    Dacă salvezi fișierul ca `index.txt`, browser-ul nu va ști că e o pagină web — îl va afișa ca text simplu. Numele `index` este o convenție: browser-ul încarcă automat `index.html` când deschizi un folder.

---

## Structura minimă HTML5

Scrie (sau copiază) în `index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prima mea pagină</title>
</head>
<body>
  <h1>Salut, lume!</h1>
  <p>Aceasta este prima mea pagină web.</p>
</body>
</html>
```

Salvează (`Ctrl+S`). Hai să înțelegem fiecare linie.

### Linie cu linie

| Linia | La ce servește |
|-------|---------------|
| `<!DOCTYPE html>` | Spune browser-ului: „folosim HTML5” (standardul modern). |
| `<html lang="ro">` | Rădăcina documentului. `lang="ro"` anunță că pagina e în română (util pentru motoare de căutare și cititoare de ecran). |
| `<head>` | Informații **despre** pagină (metadate). Nu apar vizual. |
| `<meta charset="UTF-8">` | Codificarea caracterelor. **Obligatoriu** pentru diacritice: `ă î ș ț â`. |
| `<meta name="viewport" ...>` | Face pagina să se afișeze corect pe telefoane. |
| `<title>` | Textul care apare în **tab-ul browser-ului** și în rezultatele Google. |
| `<body>` | **Conținutul vizibil** al paginii. |
| `<h1>` | Titlu principal (nivel 1). |
| `<p>` | Paragraf de text. |

!!! note "Head vs. Body"
    **Head = culisele.** Titlu, codificare, legături către CSS, setări pentru motoare de căutare.

    **Body = scena.** Tot ce vede utilizatorul: texte, imagini, butoane, formulare.

---

## Deschiderea în browser

Ai două variante:

### Varianta simplă (fără extensii)
Dublu-click pe `index.html` în File Explorer / Finder. Se deschide în browser-ul implicit.

**Dezavantaj:** la fiecare modificare trebuie să apeși `F5` (refresh) manual.

### Varianta recomandată: Live Server

1. În VS Code, instalează extensia **Live Server** (autor: Ritwick Dey).
2. Dă click dreapta pe `index.html` → `Open with Live Server`.
3. Se deschide automat browser-ul la `http://127.0.0.1:5500/index.html`.
4. Acum, **de fiecare dată când salvezi**, pagina se reîmprospătează singură.

!!! tip "Ce înseamnă 127.0.0.1"
    `127.0.0.1` este **calculatorul tău**. Live Server pornește un mini-server local pe calculatorul tău — doar tu îl poți accesa.

---

## Fluxul de lucru

```
┌──────────┐      Ctrl+S      ┌──────────┐     reload    ┌──────────┐
│  Editor  │ ───────────────> │  Fișier  │ ────────────> │ Browser  │
│ (VS Code)│                  │.html     │  (Live Server)│          │
└──────────┘                  └──────────┘               └──────────┘
     ^                                                        │
     │                  „hmm, mai schimb ceva”                │
     └────────────────────────────────────────────────────────┘
```

Regula de aur: **modifică → salvează → uită-te în browser**. Dacă nu vezi schimbarea, ai uitat să salvezi.

---

## Comentarii HTML

Un comentariu este o notă pentru tine — **nu apare** în browser:

```html
<!-- Aceasta este o notă, browser-ul o ignoră -->
<h1>Salut!</h1>
<!-- TODO: adaugă o poză aici -->
```

Folosește comentariile pentru a-ți explica secțiunile sau pentru a lăsa reminder-e.

---

## Indentare

Indentarea (spațiile la începutul liniei) **nu schimbă** modul în care browser-ul afișează pagina, dar face codul **mult mai ușor de citit** pentru tine și pentru cine îl va citi după tine.

Folosește **2 sau 4 spații** pentru fiecare nivel de imbricare. VS Code adaugă automat.

```html
<body>
  <main>
    <section>
      <h2>Titlu secțiune</h2>
      <p>Conținut...</p>
    </section>
  </main>
</body>
```

---

## Erori frecvente la început

### 1. Taguri neînchise

```html
<!-- Greșit: -->
<h1>Titlu
<p>Paragraf</p>

<!-- Corect: -->
<h1>Titlu</h1>
<p>Paragraf</p>
```

### 2. Ghilimele lipsă în atribute

```html
<!-- Greșit: -->
<html lang=ro>

<!-- Corect: -->
<html lang="ro">
```

### 3. Diacritice care apar ca `???` sau `Ã®`

Ai uitat `<meta charset="UTF-8">` în `<head>`. Adaugă-l **prima linie din head** și salvează.

### 4. „Nu se întâmplă nimic la refresh”

Ai salvat fișierul? `Ctrl+S`. În VS Code, titlul tab-ului are un `●` când există modificări nesalvate.

---

## Exerciții

### Exercițiu 1 — Pagina ta personală
Creează `index.html` cu titlul „Prima mea pagină” și un `<h1>` care conține numele tău.

??? success "Soluție"
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Prima mea pagină</title>
    </head>
    <body>
      <h1>Ana Popescu</h1>
    </body>
    </html>
    ```

### Exercițiu 2 — Adaugă conținut
Adaugă sub `<h1>` încă un titlu (ex: „Elev în clasa a VIII-a”) și un paragraf descriptiv de 2–3 fraze.

??? success "Soluție"
    ```html
    <body>
      <h1>Ana Popescu</h1>
      <h2>Elevă în clasa a VIII-a, Cluj-Napoca</h2>
      <p>Îmi place matematica, cărțile și să desenez. Învăț acum HTML
         pentru că vreau să-mi fac propriul site.</p>
    </body>
    ```

### Exercițiu 3 — Spargere intenționată
Închide `<h1>` cu `</h2>` (greșit, pe scop). Salvează. Ce observi în browser? Apoi reparează.

??? success "Soluție"
    Browser-ul este **indulgent**: probabil va afișa titlul totuși, dar structura paginii va fi coruptă. Dacă ai mai multe elemente, pot apărea în poziții stranii sau cu stiluri greșite. **Morala:** închide taguri corect; validatoarele și instrumentele automate se vor plânge.

---

## Mini-proiect: „Pagina Despre mine”

Fă o pagină completă despre tine care conține:

- `<title>` cu numele tău
- Un `<h1>` cu numele
- Un `<p>` cu vârsta și orașul
- Un `<h2>` „Hobby-uri”
- Un `<p>` cu 2–3 hobby-uri

??? success "Soluție"
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Mihai Ionescu – Despre mine</title>
    </head>
    <body>
      <h1>Mihai Ionescu</h1>
      <p>Am 14 ani și sunt din Chișinău.</p>

      <h2>Hobby-uri</h2>
      <p>Îmi place fotbalul, programarea și să construiesc chestii
         din Lego. Recent am început să experimentez cu Arduino.</p>
    </body>
    </html>
    ```

---

## Rezumat

- Orice pagină HTML5 începe cu `<!DOCTYPE html>`.
- `<head>` = metadate (invizibile), `<body>` = conținut vizibil.
- `<meta charset="UTF-8">` este **obligatoriu** pentru diacritice.
- `<title>` apare în tab-ul browser-ului.
- Flux de lucru: **editor → salvează → browser** (cu Live Server reload-ul e automat).
- Închide mereu tagurile și folosește indentare consistentă.

---

**Pasul următor:** [→ Lecția 02: HTML – tagurile de bază](02-html-bazele.md)
