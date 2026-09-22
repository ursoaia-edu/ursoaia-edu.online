---
lesson: 5
tags: [compoziție, grilă, aliniere, spațiere, layout]
summary: Aliniere, proximitate, grila de 12 coloane, sistemul de spațiere de 8 px, regula treimilor și cum se configurează toate în Figma.
---

# Lecția 05 · Compoziție și grilă

!!! tip "Ce vei învăța"
    - De ce **alinierea** este diferența vizibilă între amator și profesionist
    - **Proximitatea**: cum grupezi informația fără să desenezi nimic
    - **Sistemul de spațiere de 8 px** și de ce toate numerele tale trebuie să fie multipli
    - **Grila de 12 coloane** și cum se configurează în Figma
    - **Regula treimilor** și secțiunea de aur, cu rezervele de rigoare
    - Cum se aranjează un afiș de la zero, pas cu pas

---

## Alinierea

Regula: **fiecare element trebuie să aibă o legătură vizuală cu altul de pe pagină.** Nimic nu stă „pe unde a nimerit”.

```
   PROST                        BINE
┌──────────────┐            ┌──────────────┐
│  Titlu       │            │ Titlu        │
│      Subtitlu│            │ Subtitlu     │
│   Text text  │            │ Text text    │
│        text  │            │ text         │
│ Buton        │            │ Buton        │
└──────────────┘            └──────────────┘
  4 margini diferite          1 margine comună
```

În varianta din stânga, ochiul caută de fiecare dată unde începe rândul următor. În dreapta, există o **linie invizibilă** pe care stau toate — și ochiul o urmează fără efort.

### Ce tip de aliniere alegi

| Aliniere | Când | De evitat |
|----------|------|-----------|
| **La stânga** | Aproape întotdeauna. Text, liste, formulare | — |
| **Centrată** | Titluri scurte (1–2 rânduri), invitații, diplome | Paragrafe lungi |
| **La dreapta** | Cifre, prețuri, date în tabele | Text de citit |
| **Justified** | Ziare, cărți cu coloane late | Coloane înguste (creează „râuri”) |

!!! warning "Centrarea e capcana începătorului"
    Centrarea pare „echilibrată” și „sigură”. De fapt, un afiș complet centrat e cel mai rapid mod de a arăta amatoricesc: nicio margine comună, nicio structură, totul plutește.

    **Regula:** centrează **cel mult un bloc** pe pagină, de obicei titlul. Restul aliniat la stânga.

### Cum aliniezi în Figma

Selectează două sau mai multe elemente. În panoul din dreapta, sus, apar 6 butoane: aliniere la stânga / centru orizontal / dreapta, sus / centru vertical / jos.

Butonul **Tidy up** (apare când selectezi 3+ elemente) le aliniază **și** le distanțează egal, într-o singură apăsare.

!!! tip "Aliniere optică vs. aliniere matematică"
    Uneori un element aliniat perfect matematic **pare** dezaliniat. Se întâmplă la forme rotunde și la triunghiuri: un cerc aliniat la aceeași coordonată X cu un pătrat pare puțin mai la dreapta, pentru că marginea lui se curbează.

    La fel, un buton de „play” (triunghi) într-un cerc trebuie mutat cu 1–2 px la dreapta ca să **pară** centrat. Ochiul are dreptate, nu rigla.

---

## Proximitatea

Elementele apropiate formează un grup. Consecința practică: **spațiul dintre lucrurile legate trebuie să fie mai mic decât spațiul față de restul**.

```
PROST                         BINE

Nume                          Nume
                              Ana Popescu
Ana Popescu
                              Clasa
Clasa                         a IX-a B

a IX-a B
```

În stânga, fiecare etichetă e mai aproape de valoarea *altcuiva* decât de valoarea ei. Cititorul trebuie să ghicească ce cu ce merge.

!!! note "Regula 1:2"
    Spațiul **în interiorul** unui grup trebuie să fie de aproximativ **jumătate** din spațiul **dintre** grupuri.

    Exemplu: dacă între etichetă și valoare pui 8 px, între două perechi etichetă-valoare pui 16–24 px. Diferența e mică, dar face gruparea evidentă fără nicio linie.

---

## Sistemul de spațiere

Toate valorile tale de spațiere trebuie să vină dintr-un set fix. Cel mai folosit sistem: **multipli de 8**.

| Treaptă | Valoare | Folosire |
|---------|---------|----------|
| 1 | 4 px | Între o pictogramă și textul ei |
| 2 | 8 px | Între etichetă și valoare |
| 3 | 16 px | Padding în butoane, între elemente înrudite |
| 4 | 24 px | Între grupuri mici |
| 5 | 32 px | Padding în carduri |
| 6 | 48 px | Între secțiuni |
| 7 | 64 px | Între blocuri mari |
| 8 | 96 px | Margini de pagină, separări majore |

!!! note "De ce 8 și nu 10"
    8 se împarte la 2 și la 4 fără zecimale, iar majoritatea ecranelor lucrează cu densități care sunt multipli de 2. Un padding de 15 px devine 15.5 px pe un ecran retina, iar Figma și browser-ul îl rotunjesc diferit — apar linii de 1 px care apar și dispar la zoom.

!!! warning "Numerele „aproape bune” sunt cel mai vizibil semn de amatorism"
    Padding 13 px într-un loc, 15 px în altul, 17 px în al treilea. Nimeni nu poate spune ce e greșit, dar toată lumea simte că e ceva. Rotunjește **tot** la multipli de 8 (sau de 4 pentru valori mici).

---

## Grila

O grilă este un set de coloane invizibile care dau structură paginii. Nu o vede nimeni în final, dar ea decide unde stau lucrurile.

### Grila de 12 coloane

12 este numărul standard pentru că se împarte frumos: 12 = 2×6 = 3×4 = 4×3 = 6×2. Poți face astfel layout-uri cu 2, 3, 4 sau 6 coloane egale folosind aceeași grilă.

```
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │

│      3 coloane       │      (4+4+4)          │
│         2 coloane (6+6)                      │
│  4 coloane (3+3+3+3)                         │
```

### Termenii

| Termen | Ce este | Valoare tipică |
|--------|---------|----------------|
| **Coloană** | Zona în care stă conținutul | Lățime variabilă |
| **Gutter** | Spațiul dintre coloane | 16–32 px |
| **Margin** | Spațiul de la marginea paginii | 24–96 px |

### Cum configurezi grila în Figma

1. Selectează frame-ul.
2. În panoul din dreapta, la **Layout grid**, apasă **+**.
3. Din meniul derulant schimbă din `Grid` în **`Columns`**.
4. Setează: **Count** 12, **Type** `Stretch`, **Margin** 64, **Gutter** 24.
5. Comută vizibilitatea grilei cu ++ctrl+shift+4++ (Windows) sau ++ctrl+g++ (macOS — tasta `control`, nu `cmd`).

!!! tip "Grile diferite pentru dispozitive diferite"
    - **Telefon** (390 px): 4 coloane, margin 16, gutter 16
    - **Tabletă** (768 px): 8 coloane, margin 32, gutter 24
    - **Desktop** (1440 px): 12 coloane, margin 96, gutter 24

    Le vei folosi în lecția 14, când desenezi interfețe.

### Grilă de linii de bază

Pentru print, se adaugă o a doua grilă, **orizontală**, cu pasul egal cu interlinia textului curent (de ex. 24 px). Toate liniile de text din toate coloanele se așază pe ea. Este ce face o revistă să arate îngrijită.

În Figma: mai adaugă un **Layout grid**, tip `Rows`, `Count: Auto`, `Height: 24`.

---

## Regula treimilor

Împarte pagina în 3 × 3 cu două linii verticale și două orizontale. Așază elementele importante **pe linii** sau **în punctele de intersecție**, nu în centrul exact.

```
┌───────┬───────┬───────┐
│       │       │       │
├───────●───────●───────┤   ● = puncte forte
│       │       │       │
├───────●───────●───────┤
│       │       │       │
└───────┴───────┴───────┘
```

Este moștenită din fotografie și funcționează pentru că un element ușor decentrat creează tensiune și mișcare, în timp ce centrul perfect e static.

!!! note "Secțiunea de aur — cu rezerve"
    Vei auzi des despre raportul de aur (1:1.618) prezentat ca „legea secretă a frumuseții”. Adevărul e mai modest: este un raport plăcut, dar **nu** e o lege și nu explică de ce funcționează un design.

    Regula treimilor (1:2) e mai simplă, dă rezultate foarte apropiate și nu cere calcule. Folosește-o pe ea.

---

## Cum construiești o compoziție, pas cu pas

Nu începe desenând. Începe ordonând.

### Pasul 1 — Listează conținutul și ierarhizează-l

Scrie pe hârtie tot ce trebuie să apară și numerotează în ordinea importanței. Pentru un afiș de eveniment:

1. Titlul evenimentului
2. Data
3. Ora și locul
4. Descrierea scurtă
5. Cine organizează
6. Detalii (intrare, contact, site)

### Pasul 2 — Grupează

Câte grupuri rezultă? Ideal **3–5**. Dacă ai 9 grupuri, cititorul nu are de unde să știe de unde să înceapă.

Pentru exemplul de mai sus: `[titlu]`, `[data + ora + loc]`, `[descriere]`, `[organizator + detalii]`. Patru grupuri.

### Pasul 3 — Alege o structură

| Structură | Cum arată | Bună pentru |
|-----------|-----------|-------------|
| **Coloană unică** | Totul pe verticală, aliniat la stânga | Afișe simple, postări |
| **Două coloane** | Imagine / text, sau conținut / detalii | Pliante, pagini web |
| **În Z** | Ochiul merge stânga-sus → dreapta-sus → stânga-jos → dreapta-jos | Afișe cu puține elemente |
| **În F** | Scanare pe orizontală descrescătoare | Pagini web cu mult text |
| **Modulară** | Carduri într-o grilă | Portofolii, galerii, dashboard-uri |

### Pasul 4 — Așază pe grilă și verifică

- Toate elementele încep pe o coloană a grilei?
- Toate spațiile sunt multipli de 8?
- Spațiul din interiorul grupurilor e mai mic decât cel dintre grupuri?
- Elementul cel mai important e și cel mai vizibil?

### Pasul 5 — Testul de blur

Aplică blur puternic (lecția 02). Vezi 3–5 pete, cu cea mai puternică pe informația cea mai importantă? Dacă da, compoziția e gata.

---

## Exerciții

### Exercițiu 1 — Repară alinierea
Într-un frame de 600 × 800 px, așază intenționat 6 elemente de text în poziții ușor decalate (toate la coordonate X diferite: 40, 47, 52, 41, 58, 45). Apoi repar-o.

??? success "Soluție"
    Corecția are un singur pas real: selectezi toate cele 6 texte și apeși **Align left**. Toate trec la X = 40 (coordonata celui mai din stânga).

    Comparând înainte/după, diferența e uriașă, deși cea mai mare deplasare a fost de 18 px. Aceasta e proba că **alinierea e mai vizibilă decât crezi** — inclusiv atunci când e greșită cu foarte puțin.

    Verificare suplimentară: setează spațierea verticală dintre ele la multipli de 8 (8 în interiorul grupurilor, 24 între grupuri) folosind **Tidy up** sau Auto layout.

### Exercițiu 2 — Grupare prin proximitate
Într-un frame de 400 × 500 px, așază 8 rânduri de text — 4 perechi etichetă/valoare — fără să desenezi nicio linie și fără să folosești culori diferite. Cititorul trebuie să vadă instant 4 grupuri.

??? success "Soluție"
    Setările care rezolvă:

    - Etichetă: 13 px, Medium, culoare `#6B7280`, majuscule, tracking +8%.
    - Valoare: 18 px, Regular, culoare `#111827`.
    - Spațiu etichetă → valoare: **4 px**.
    - Spațiu între perechi: **24 px**.

    Raportul 4 : 24 = 1 : 6 face gruparea evidentă imediat. Chiar și 8 : 24 (1 : 3) funcționează.

    Ce **nu** funcționează: spațiu de 12 px peste tot. Atunci ai 8 rânduri egale, nu 4 grupuri, iar cititorul trebuie să citească atent ca să înțeleagă structura.

### Exercițiu 3 — Grilă de 12 coloane
Configurează o grilă de 12 coloane pe un frame Desktop (1440 × 1024) și așază pe ea trei carduri egale, apoi rearanjează aceleași carduri în două coloane inegale (8 + 4).

??? success "Soluție"
    **Grila:** Layout grid → Columns → Count 12, Type `Stretch`, Margin 96, Gutter 24.
    Lățimea unei coloane rezultă automat: (1440 − 2×96 − 11×24) / 12 = **62 px**.

    **Trei carduri egale:** fiecare ocupă 4 coloane → lățime = 4×62 + 3×24 = **320 px**. Le așezi la X = 96, 440, 784.

    **Layout 8 + 4:** cardul principal ocupă 8 coloane → 8×62 + 7×24 = **664 px**. Cardul lateral ocupă 4 coloane → **320 px**, la X = 96 + 664 + 24 = 784.

    Observă că **nu ai calculat nimic „din ochi”**. Fiecare lățime rezultă din grilă. De asta o folosești: elimină deciziile arbitrare.

---

## Mini-proiect: același conținut, trei compoziții

Ia conținutul afișului tipografic din lecția 04 și construiește **trei compoziții diferite** cu exact același text: una în **coloană unică**, una în **Z**, una **modulară** (carduri). Aceeași paletă, aceleași fonturi, aceeași ierarhie.

??? success "Soluție"
    **Coloană unică (A3):** grilă de 12 coloane, tot conținutul pe coloanele 1–9, aliniat la stânga. Titlul sus, apoi data, apoi descrierea, apoi detaliile jos. Spațiere: 16 px în grupuri, 48 px între ele. **Cea mai sigură variantă** — greu de stricat, ușor de citit.

    **În Z (A3 landscape):** eticheta stânga-sus, titlul dreapta-sus, descrierea stânga-jos, data mare dreapta-jos. Ochiul parcurge natural un Z. Funcționează **doar** cu puțin conținut — maximum 4 blocuri. Cu 6 blocuri se destramă.

    **Modulară (A3):** grilă de 12 × 12; patru carduri cu fundal `#1E293B`, colțuri 16 px, padding 32 px. Cardul titlului ocupă 12 coloane × 4 rânduri; data 6 × 3; locul 6 × 3; detaliile 12 × 2. Arată ca un dashboard. Bună când informația e de tip „date”, slabă când vrei impact emoțional.

    **Concluzia:** conținutul identic produce trei impresii complet diferite. Compoziția nu e „aranjarea de la final” — e o decizie de comunicare, la fel ca alegerea culorii.

    **Verificare pe toate trei:** aplică blur. În toate cazurile, cea mai întunecată pată trebuie să fie titlul. Dacă într-una dintre variante data iese mai puternic decât titlul, ai schimbat ierarhia fără să vrei.

---

## Rezumat

- **Aliniere:** fiecare element se leagă vizual de altul. Implicit — la stânga.
- Centrarea se folosește pentru **cel mult un bloc** pe pagină.
- **Proximitate:** spațiul în interiorul grupului ≈ jumătate din spațiul dintre grupuri.
- Toate spațiile sunt **multipli de 8** (sau de 4 pentru valori mici).
- **Grila de 12 coloane** se împarte în 2, 3, 4 și 6 — de asta e standardul.
- Termenii grilei: **coloană, gutter, margin**.
- **Regula treimilor** > secțiunea de aur: mai simplă, rezultat similar.
- Construiești în 5 pași: **listezi → grupezi → alegi structura → așezi pe grilă → testezi cu blur**.
- Ideal **3–5 grupuri** vizuale pe o pagină.

---

**Pasul următor:** [→ Lecția 06: Ierarhie vizuală](06-ierarhie-vizuala.md)
