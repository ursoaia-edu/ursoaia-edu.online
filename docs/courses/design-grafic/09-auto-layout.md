---
lesson: 9
tags: [figma, auto layout, flexbox, spațiere, responsive]
summary: Aranjare automată, direcție, spațiere și padding, comportamentul de redimensionare și cum se leagă Auto Layout de CSS Flexbox.
---

# Lecția 09 · Auto Layout

!!! tip "Ce vei învăța"
    - Ce este **Auto Layout** și ce problemă rezolvă
    - **Direcție**, **gap** și **padding**
    - **Alinierea** în interiorul containerului și `Space between`
    - **Hug**, **Fill** și **Fixed** — cele trei comportamente de redimensionare
    - Auto Layout **imbricat**, cel mai important concept al lecției
    - Cum se traduce totul în **CSS Flexbox**

---

## Problema

Ai un buton cu textul „Salvează”. Îl faci frumos: text centrat, 16 px spațiu în jur. Apoi schimbi textul în „Salvează modificările”.

Fără Auto Layout: textul iese din buton. Redimensionezi butonul manual, recentrezi textul, verifici spațiile. Apoi mai schimbi textul o dată.

Cu Auto Layout: butonul crește singur. Spațiul rămâne exact 16 px.

Aceeași problemă apare la orice listă la care adaugi elemente, la orice card cu text de lungime variabilă, la orice meniu. **Auto Layout este ce transformă un desen static într-o structură.**

---

## Bazele

### Cum îl aplici

Selectează unul sau mai multe elemente și apasă ++shift+a++. Se creează un frame cu Auto Layout în jurul lor.

Ca să-l scoți: ++shift+alt+a++.

### Cele patru setări de bază

În panoul din dreapta apare o secțiune nouă, **Auto layout**:

| Setare | Ce face | Valori |
|--------|---------|--------|
| **Direction** | Orientarea | Vertical ↓, Orizontal →, Wrap |
| **Gap** | Spațiul dintre elemente | Număr, sau `Auto` |
| **Padding** | Spațiul interior, față de margini | Un număr, sau 4 separate |
| **Alignment** | Cum se așază elementele în container | O grilă de 9 puncte |

```
┌─────────────────────────────┐
│  padding-top                │
│  ┌───────┐ gap ┌───────┐    │  padding-right
│  │  el 1 │─────│  el 2 │    │
│  └───────┘     └───────┘    │
│  padding-bottom             │
└─────────────────────────────┘
   padding-left
```

!!! tip "Padding-uri separate"
    Click pe iconița cu patru laturi de lângă câmpul de padding → se desfac în patru câmpuri: sus, dreapta, jos, stânga. Un buton are de obicei padding orizontal mai mare decât cel vertical (de ex. 24 pe orizontală, 12 pe verticală) — arată mai echilibrat.

### Space between

Dacă setezi **Gap** la `Auto` (iconița cu săgeți opuse), elementele se împing la marginile containerului și spațiul se distribuie între ele. Este exact ce ai nevoie pentru o bară de navigație: logo la stânga, meniu la dreapta.

```
┌────────────────────────────────────────┐
│ [logo]                    [meniu] [cta]│
└────────────────────────────────────────┘
   gap = Auto
```

---

## Comportamentul de redimensionare

Aceasta e partea care confundă pe toată lumea la început. Fiecare element dintr-un Auto Layout are două setări independente — una pentru lățime, una pentru înălțime.

| Comportament | Iconița | Ce face |
|--------------|---------|---------|
| **Hug contents** | Săgeți spre interior | Containerul se strânge exact pe conținut |
| **Fill container** | Săgeți spre exterior | Elementul se întinde pe tot spațiul disponibil |
| **Fixed** | Număr | Dimensiune fixă, nu se schimbă |

### Regulile practice

| Element | Lățime | Înălțime | De ce |
|---------|--------|----------|-------|
| Buton | Hug | Hug | Crește cu textul |
| Buton pe toată lățimea | Fill | Hug | Ocupă cardul, înălțimea urmează textul |
| Card într-o grilă | Fill | Hug | Lățimea vine de la grilă, înălțimea de la conținut |
| Text într-un card | Fill | Hug | Se rupe pe rânduri, crește în jos |
| Pictogramă | Fixed | Fixed | 24 × 24, mereu |
| Ecran / pagină | Fixed | Fixed sau Hug | Formatul e dat |

!!! warning "`Fill` funcționează doar în interiorul unui Auto Layout"
    Dacă opțiunea `Fill container` e gri, înseamnă că elementul **nu** e într-un frame cu Auto Layout. Aplică Auto Layout pe părinte întâi.

!!! note "Hug + text = cel mai util cuplu"
    Un card cu lățime `Fill` și înălțime `Hug`, conținând un text cu lățime `Fill` și înălțime `Hug`: dacă textul are 2 rânduri, cardul e scund; dacă are 6 rânduri, cardul crește. Nu atingi nimic.

---

## Auto Layout imbricat

Aici stă toată puterea. Un frame cu Auto Layout poate conține alte frame-uri cu Auto Layout.

Un card de proiect real:

```
card/project                    ← Auto Layout vertical, gap 16, padding 24
├── header                      ← Auto Layout orizontal, gap 12, Fill
│   ├── ◇ icon (24×24)          ← Fixed
│   └── title                   ← Fill
├── description                 ← Fill / Hug
└── footer                      ← Auto Layout orizontal, gap Auto, Fill
    ├── tags                    ← Auto Layout orizontal, gap 8, Hug
    │   ├── badge
    │   └── badge
    └── button                  ← Hug
```

Patru niveluri de Auto Layout. Rezultatul: schimbi titlul, descrierea, numărul de badge-uri sau textul butonului, iar cardul se rearanjează corect de fiecare dată, fără să atingi nimic.

!!! tip "Construiește de la interior spre exterior"
    Nu încerca să faci structura de sus în jos. Fă întâi grupurile mici (badge-urile, apoi rândul de badge-uri), aplică-le Auto Layout, apoi grupează-le în rânduri mai mari, apoi în card.

    ++shift+a++ pe grupul mic, ++shift+a++ pe grupul mai mare, și tot așa.

### Redenumește frame-urile

Un Auto Layout imbricat cu straturi numite `Frame 12`, `Frame 13`, `Frame 14` devine imposibil de întreținut. Numește-le după rol: `header`, `content`, `footer`, `tags`, `actions`.

---

## Setări avansate

### Absolute position

Uneori vrei un element **în interiorul** unui Auto Layout, dar care să nu participe la aranjare — de exemplu o bulină de notificare peste un avatar, sau o etichetă „Nou” în colțul unui card.

Selectează elementul → în panoul din dreapta apare iconița cu un pătrat și un punct în colț → **Absolute position**. Elementul iese din flux și îl poziționezi liber, dar rămâne copil al containerului.

### Canvas stacking

Când elementele se suprapun (de exemplu avataruri în cascadă cu gap negativ), setarea **Canvas stacking** decide care e deasupra: primul sau ultimul.

### Strokes: included / excluded in layout

Implicit, Figma **nu** numără grosimea conturului în calculul spațierii. Dacă lucrezi cu butoane cu contur și vrei alinierea perfectă cu cele fără contur, comută la `Strokes: included in layout`.

### Wrap

Direcția a treia, **Wrap**, face ca elementele să treacă pe rândul următor când nu mai încap. Util pentru liste de etichete sau galerii care trebuie să se adapteze la lățimi diferite.

---

## Legătura cu CSS

Auto Layout este, practic, **CSS Flexbox** cu altă interfață. Dacă ai făcut cursul Web, îți e familiar.

| Figma | CSS |
|-------|-----|
| Auto layout | `display: flex` |
| Direction: Horizontal | `flex-direction: row` |
| Direction: Vertical | `flex-direction: column` |
| Direction: Wrap | `flex-wrap: wrap` |
| Gap | `gap` |
| Padding | `padding` |
| Gap: Auto | `justify-content: space-between` |
| Alignment (grila de 9) | `justify-content` + `align-items` |
| Fill container | `flex: 1` |
| Hug contents | `width: fit-content` / dimensiune implicită |
| Fixed | `width: 320px` |
| Absolute position | `position: absolute` |

!!! note "De ce contează"
    Când predai un design unui programator (sau îl construiești tu, la lecția 14), un layout făcut cu Auto Layout se traduce **direct** în CSS. Un layout făcut cu elemente poziționate manual trebuie reinterpretat, iar reinterpretarea introduce diferențe.

    Vezi [lecția 08 din cursul Web](../web/08-css-flexbox-grid.md) pentru partea de CSS.

---

## Erori frecvente

| Simptom | Cauză | Reparație |
|---------|-------|-----------|
| Textul iese din buton | Butonul e `Fixed` pe lățime | Setează lățimea pe `Hug` |
| Cardul nu crește cu textul | Înălțimea e `Fixed` | Setează înălțimea pe `Hug` |
| `Fill` e gri și nu se poate alege | Părintele nu are Auto Layout | ++shift+a++ pe părinte |
| Spațiile arată inegale | Unele elemente au margini proprii | Șterge marginile, folosește gap |
| Un element „sare” la redimensionare | Are `Absolute position` fără constrângeri | Setează constrângerile în panoul din dreapta |
| Totul se strânge într-o coloană subțire | Containerul e `Hug` pe lățime, dar ar trebui `Fixed` | Setează lățimea containerului |

!!! warning "Nu amesteca Auto Layout cu poziționare manuală"
    Dacă jumătate din card e aranjată cu Auto Layout și jumătate cu elemente mutate cu mâna, la prima schimbare de conținut se strică jumătatea manuală. **Ori tot, ori nimic**, pe fiecare nivel.

---

## Exerciții

### Exercițiu 1 — Buton care crește
Construiește un buton cu Auto Layout: padding 12 vertical / 24 orizontal, gap 8, cu o pictogramă de 16 px și text. Testează cu textele `OK`, `Salvează` și `Salvează toate modificările`.

??? success "Soluție"
    1. Scrie textul, pune pictograma lângă el.
    2. Selectează ambele → ++shift+a++.
    3. Direction: **Horizontal**, Gap: **8**, Padding: **12 / 24**.
    4. Alignment: **centru-stânga** (punctul din mijloc-stânga al grilei de 9).
    5. Lățime și înălțime: ambele pe **Hug**.
    6. Adaugă Fill `brand/primary` și rază 8.

    Acum schimbă textul de trei ori. Butonul își schimbă lățimea, pictograma rămâne la 8 px de text, padding-ul rămâne 24. Nu ai atins nimic.

    **Greșeala de verificat:** dacă ai lăsat pictograma pe `Fill` în loc de `Fixed`, ea se va întinde urât la texte scurte. Pictogramele sunt întotdeauna `Fixed`.

### Exercițiu 2 — Bară de navigație
Construiește o bară de navigație de 1440 px lățime cu: logo la stânga, patru link-uri la mijloc-dreapta și un buton la extrema dreaptă. Trebuie să funcționeze corect și la 1024 px.

??? success "Soluție"
    **Structura:**

    ```
    navbar                  ← Auto Layout orizontal, gap Auto,
    │                          padding 0/32, lățime Fixed 1440, înălțime Hug
    ├── logo                ← Hug
    └── right               ← Auto Layout orizontal, gap 32, Hug
        ├── links           ← Auto Layout orizontal, gap 24, Hug
        │   ├── link × 4
        └── ◇ button        ← Hug
    ```

    **Pașii:**
    1. Fă cele 4 link-uri, selectează-le → ++shift+a++ → orizontal, gap 24. Redenumește `links`.
    2. Selectează `links` + butonul → ++shift+a++ → orizontal, gap 32. Redenumește `right`.
    3. Selectează logo + `right` → ++shift+a++ → orizontal, **gap Auto**. Redenumește `navbar`.
    4. Setează lățimea `navbar` la 1440, padding orizontal 32, alignment vertical centrat.

    **Testul:** schimbă lățimea `navbar` la 1024. Logo-ul rămâne lipit de stânga, grupul din dreapta de dreapta, iar spațiul dintre ele se micșorează. Exact cum trebuie.

    **Fără gap Auto:** ar fi trebuit să muți manual grupul din dreapta la fiecare schimbare de lățime.

### Exercițiu 3 — Card cu Auto Layout imbricat
Construiește cardul de proiect din schema de mai sus (patru niveluri). Testează cu un titlu de 2 cuvinte și unul de 8 cuvinte, cu 1 badge și cu 4 badge-uri.

??? success "Soluție"
    **Construcția, de la interior spre exterior:**

    1. **Badge:** text + Auto Layout, padding 4/10, rază 4, Hug/Hug.
    2. **Tags:** selectează 2 badge-uri → ++shift+a++ → orizontal, gap 8, Hug.
    3. **Footer:** selectează `tags` + buton → ++shift+a++ → orizontal, **gap Auto**, lățime **Fill**.
    4. **Header:** pictogramă (Fixed 24×24) + titlu (Fill) → ++shift+a++ → orizontal, gap 12, lățime Fill, alignment centrat vertical.
    5. **Card:** selectează `header` + descriere + `footer` → ++shift+a++ → vertical, gap 16, padding 24, lățime **Fill**, înălțime **Hug**.

    **Testele:**
    - Titlu de 8 cuvinte → se rupe pe 2 rânduri, header-ul crește, cardul crește, footer-ul coboară. Corect.
    - 4 badge-uri → rândul de tags se lățește; dacă depășește spațiul, comută `tags` pe direcția **Wrap**.
    - Card pus într-o grilă de 3 coloane cu lățimi diferite → fiecare card își ajustează înălțimea la conținut.

    **Verificare finală:** pune trei carduri într-un Auto Layout orizontal cu gap 24, fiecare pe `Fill`. Toate trei au aceeași lățime automat. Dacă schimbi lățimea containerului, cele trei se adaptează împreună.

---

## Mini-proiect: ecran de aplicație complet cu Auto Layout

Construiește un ecran de **390 × 844 px** (iPhone 14) pentru o aplicație a cercului de informatică: antet cu titlu și avatar, o listă de 5 proiecte (carduri), și o bară de navigație jos cu 4 pictograme. **Totul** trebuie să fie Auto Layout — zero elemente poziționate manual.

??? success "Soluție"
    **Structura:**

    ```
    screen                        ← Fixed 390 × 844, Auto Layout vertical, gap 0
    ├── header                    ← orizontal, gap Auto, padding 16/20, Fill
    │   ├── title                 ← Hug
    │   └── ◇ avatar (40×40)      ← Fixed
    ├── content                   ← vertical, gap 12, padding 20, Fill / Fill
    │   └── ◇ card/project × 5    ← fiecare Fill / Hug
    └── tabbar                    ← orizontal, gap Auto, padding 12/24, Fill
        └── ◇ tab-item × 4        ← fiecare Hug
    ```

    **Detaliile care contează:**

    - `content` are înălțimea pe **Fill** — ocupă tot spațiul rămas între header și tabbar. Aceasta e singura setare care face ca bara de jos să stea lipită de marginea ecranului indiferent de câte carduri ai.
    - Fiecare `tab-item` este un Auto Layout vertical cu pictogramă 24 px + etichetă 10 px, gap 4, alignment centrat.
    - `tabbar` folosește gap **Auto** — cele 4 elemente se distribuie egal pe lățime.
    - Cardurile sunt instanțe ale componentei din exercițiul 3.

    **Testele finale:**

    | Test | Rezultat corect |
    |------|-----------------|
    | Șterge 2 carduri | Cele 3 rămase urcă; tabbar rămâne jos |
    | Adaugă 3 carduri | Lista crește; conținutul depășește ecranul (normal — se va scrolla) |
    | Schimbă lățimea ecranului la 320 | Toate cardurile se îngustează; nimic nu iese în afară |
    | Schimbă titlul unui card în unul lung | Cardul crește în înălțime, cele de dedesubt coboară |
    | Schimbă padding-ul din `content` de la 20 la 24 | Toate cardurile se îngustează cu 8 px, uniform |

    **Criteriul de trecere:** dacă la oricare dintre cele cinci teste a trebuit să muți manual ceva, undeva în structură există un element care nu e în Auto Layout sau are dimensiune `Fixed` unde ar trebui `Fill`.

---

## Rezumat

- **Auto Layout** (++shift+a++) transformă un desen în structură care se adaptează la conținut.
- Patru setări de bază: **direction, gap, padding, alignment**.
- **Gap: Auto** = `space-between` — elementele se împing la margini.
- Trei comportamente: **Hug** (strânge pe conținut), **Fill** (ocupă spațiul), **Fixed** (dimensiune fixă).
- Pictogramele sunt **întotdeauna Fixed**; textele sunt de obicei **Fill / Hug**.
- **Auto Layout imbricat** e ce face un card real să funcționeze; construiește **de la interior spre exterior**.
- **Absolute position** scoate un element din flux fără să-l scoată din container.
- Auto Layout ≈ **CSS Flexbox**; un design făcut așa se traduce direct în cod.
- Nu amesteca Auto Layout cu poziționare manuală pe același nivel.

---

**Pasul următor:** [→ Lecția 10: Imagini, măști și export](10-imagini-masti-export.md)
