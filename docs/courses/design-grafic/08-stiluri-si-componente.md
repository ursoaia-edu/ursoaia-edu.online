---
lesson: 8
tags: [figma, componente, stiluri, variante, design system]
summary: Stiluri de culoare și text, componente și instanțe, proprietăți și variante — cum construiești o bibliotecă reutilizabilă.
---

# Lecția 08 · Stiluri și componente

!!! tip "Ce vei învăța"
    - Ce sunt **stilurile** și de ce nu mai alegi niciodată o culoare „de mână”
    - Diferența dintre **componentă** și **instanță**
    - Ce se poate suprascrie într-o instanță și ce nu
    - **Proprietăți** și **variante** — un singur buton în 12 stări
    - **Slot-uri** (instance swap) pentru componente flexibile
    - Cum organizezi o bibliotecă pe care o poți folosi peste șase luni

---

## Problema pe care o rezolvă

Ai un afiș cu 20 de elemente portocalii. Profesorul îți spune: „schimbă portocaliul în verde”.

- **Fără stiluri:** selectezi fiecare element, schimbi culoarea, cauți pe cele pe care le-ai ratat, mai găsești două a doua zi. 15 minute și o greșeală.
- **Cu stiluri:** schimbi stilul `brand/primary`. Toate cele 20 se actualizează. 3 secunde, zero greșeli.

Diferența crește exponențial cu mărimea proiectului. Într-un design de aplicație cu 40 de ecrane, fără stiluri nu se poate lucra deloc.

---

## Stiluri

Un **stil** este o valoare salvată cu un nume, pe care o aplici în multe locuri. Figma are patru tipuri:

| Tip | Ce salvează |
|-----|-------------|
| **Color** | O culoare sau un gradient |
| **Text** | Font + greutate + mărime + interlinie + tracking |
| **Effect** | Umbre, blur |
| **Grid** | Configurația grilei de layout |

### Cum creezi un stil

1. Selectează un element care are deja valoarea dorită.
2. În panoul din dreapta, la secțiunea respectivă (Fill / Text / Effects / Layout grid), apasă pe **cele patru puncte**.
3. Apasă **+** și dă-i un nume.

### Cum numești stilurile

Deja am stabilit regula în lecția 03: **după rol, nu după aspect**. Acum adaugă și structura de foldere, prin `/`:

```
brand/
  primary
  primary-hover
  secondary
surface/
  base
  raised
  overlay
text/
  strong
  base
  muted
  inverse
feedback/
  success
  warning
  error
```

```
heading/
  h1
  h2
  h3
body/
  large
  base
  small
label/
  caps
  mono
```

!!! tip "Trei niveluri maximum"
    `brand/primary` e bun. `design/colors/brand/main/primary-500` e o structură pe care o vei urî în două săptămâni. Două niveluri sunt suficiente pentru un proiect de curs.

!!! warning "Un stil neaplicat nu ajută la nimic"
    Greșeala clasică: creezi 12 stiluri frumos numite, apoi desenezi în continuare alegând culorile din selector. Verificarea: selectează orice element din designul tău — în panoul din dreapta, **Fill** trebuie să arate numele unui stil, nu un cod HEX.

---

## Componente

Un **stil** salvează o valoare. O **componentă** salvează o structură întreagă: forme, texte, spațiere, toate împreună.

### Componentă vs. instanță

- **Componenta principală** (main component) — originalul. Are un romb violet ◆ în panoul Layers.
- **Instanța** — o copie legată de original. Are un romb gol ◇.

**Modificările din componenta principală se propagă în toate instanțele.** Modificările dintr-o instanță rămân locale.

### Cum creezi o componentă

1. Selectează elementele (de obicei un frame cu tot ce trebuie înăuntru).
2. ++ctrl+alt+k++ (Windows) / ++cmd+option+k++ (Mac), sau butonul ◆ din bara de sus.
3. Dă-i un nume descriptiv, cu structură de foldere: `button/primary`, `card/project`, `icon/wifi`.

Apoi o plasezi cu ++ctrl+d++ sau din panoul **Assets** (stânga), unde apar toate componentele fișierului.

### Ce se poate suprascrie într-o instanță

| Se poate | Nu se poate |
|----------|-------------|
| Textul | Adăugarea de straturi noi |
| Culorile (Fill, Stroke) | Ștergerea unui strat (doar ascunderea) |
| Imaginile | Schimbarea spațierii structurale |
| Vizibilitatea straturilor | Reordonarea straturilor |
| Instanțele imbricate (swap) | — |

!!! note "Resetarea unei instanțe"
    Dacă ai suprascris prea multe lucruri într-o instanță, click dreapta → **Reset all changes**. Revine la starea componentei principale.

!!! warning "Unde ții componentele principale"
    Nu le lăsa împrăștiate prin fișier. Creează o **pagină separată** numită `Components` (panoul din stânga, tab-ul Pages) și ține-le pe toate acolo, organizate în secțiuni. Când ștergi din greșeală o componentă principală, toate instanțele ei devin „detașate” și nu se mai actualizează.

---

## Proprietăți

O **proprietate** (component property) transformă o suprascriere manuală într-un câmp pe care îl completezi în panoul din dreapta. Patru tipuri:

| Tip | Ce controlează | Exemplu |
|-----|----------------|---------|
| **Text** | Conținutul unui text | Eticheta butonului |
| **Boolean** | Vizibilitatea unui strat | Afișează / ascunde pictograma |
| **Instance swap** | Care componentă stă într-un slot | Ce pictogramă anume |
| **Variant** | Care variantă e activă | Mărime, stare, tip |

### Cum adaugi o proprietate

1. Intră în componenta principală.
2. Selectează stratul pe care vrei să-l faci configurabil.
3. În panoul din dreapta, lângă proprietatea respectivă, apasă pe iconița cu romb mic.
4. **Create property** → nume + valoare implicită.

Acum, orice instanță arată în panoul din dreapta un câmp cu acel nume. Nu mai trebuie să intri în straturi ca să schimbi textul.

---

## Variante

O **variantă** grupează mai multe versiuni ale aceleiași componente într-una singură, cu un selector.

### Exemplu: un buton

Proprietăți:

| Proprietate | Valori | Câte |
|-------------|--------|------|
| `Type` | primary, secondary, ghost | 3 |
| `Size` | small, medium, large | 3 |
| `State` | default, hover, disabled | 3 |

3 × 3 × 3 = **27 de variante** dintr-o singură componentă. În panoul din dreapta al oricărei instanțe apar trei meniuri derulante.

### Cum construiești un set de variante

1. Creează prima componentă (`button`, tipul primary, mărimea medium, starea default).
2. Selecteaz-o și apasă **Create component set** (butonul cu patru pătrate din bara de sus).
3. Apare un chenar violet punctat. Înăuntru, apasă **+** pentru fiecare variantă nouă.
4. În panoul din dreapta, la **Properties**, redenumește proprietățile (`Property 1` → `Type`) și valorile.

!!! tip "Nu construi 27 de variante deodată"
    Începe cu 2 proprietăți și 4–6 variante. Adaugă a treia proprietate doar când chiar ai nevoie de ea. Un set de variante prea mare devine greu de întreținut: orice schimbare de spațiere trebuie făcută în 27 de locuri.

    Alternativa mai bună: folosește **Auto Layout** (lecția 09) astfel încât mărimea să se adapteze singură, și păstrează doar proprietățile `Type` și `State`.

---

## Instance swap — slot-uri

Cea mai utilă proprietate, și cea mai puțin cunoscută de începători.

**Problema:** ai un card de proiect care conține o pictogramă. Ai 8 pictograme diferite. Faci 8 componente de card?

**Soluția:** faci **o** componentă de card, în care pictograma este ea însăși o instanță. Apoi adaugi o proprietate de tip **Instance swap** pe ea. În fiecare instanță de card, alegi din meniu ce pictogramă vrei.

```
card/project  (componentă)
├── frame
│   ├── ◇ icon/wifi      ← slot: Instance swap
│   ├── text: Titlu      ← proprietate Text
│   └── text: Descriere  ← proprietate Text
```

!!! note "Regula slot-ului"
    Orice element care se schimbă de la o instanță la alta, **dar rămâne același tip de lucru**, trebuie să fie un slot. Pictograme, avataruri, badge-uri, butoane dintr-un card.

---

## Organizarea bibliotecii

Un fișier cu 60 de componente fără structură e mai rău decât niciuna. Structura minimă:

```
Pagina: Foundations
  ├── Paleta de culori (toate stilurile, vizual)
  ├── Scara tipografică
  └── Sistemul de spațiere

Pagina: Components
  ├── Secțiunea: Primitives     → button, input, badge, avatar
  ├── Secțiunea: Icons          → setul de 24 × 24
  └── Secțiunea: Composites     → card, header, nav, footer

Pagina: Screens / Designs
  └── Lucrul propriu-zis
```

### Convenția de nume

| Model | Exemplu | De ce |
|-------|---------|-------|
| `categorie/nume` | `button/primary` | Grupare automată în Assets |
| `icon/nume` | `icon/wifi` | Toate pictogramele împreună |
| `card/tip` | `card/project` | Ușor de găsit la swap |

!!! tip "Testul de peste șase luni"
    Deschide fișierul peste șase luni și încearcă să găsești componenta de buton secundar în sub 10 secunde. Dacă nu reușești, organizarea e prea complicată sau numele sunt prea vagi.

---

## Când NU folosești componente

Componentele au un cost: timp de construcție și complexitate. Nu merită pentru:

- Un element folosit **o singură dată**. Un titlu de afiș nu e componentă.
- Un afiș unic care nu va avea variante.
- Forme decorative care se schimbă de fiecare dată.

!!! note "Regula de trei"
    Dacă un element apare de **trei ori sau mai mult**, sau știi sigur că se va repeta, fă-l componentă. Sub trei, nu merită.

---

## Exerciții

### Exercițiu 1 — Sistem de stiluri complet
Creează, într-un fișier nou, setul complet de stiluri de culoare și text din lecțiile 03 și 04. Apoi construiește un card de proiect care folosește **exclusiv** stiluri — niciun HEX scris de mână.

??? success "Soluție"
    **Stiluri de culoare (9):**
    `brand/primary`, `brand/primary-hover`, `surface/base`, `surface/raised`, `text/strong`, `text/base`, `text/muted`, `feedback/success`, `feedback/error`.

    **Stiluri de text (6):**
    `heading/h1` (31/1.2 Semi Bold), `heading/h2` (25/1.3 Semi Bold), `body/base` (16/1.6 Regular), `body/small` (13/1.4 Regular), `label/caps` (13/1.4 Medium, majuscule, +10% tracking), `label/mono` (13/1.4 Regular, JetBrains Mono).

    **Cardul:** frame 360 × 280, `surface/raised`, rază 16, padding 32.
    - Etichetă: `label/caps` + `brand/primary`
    - Titlu: `heading/h2` + `text/strong`
    - Descriere: `body/base` + `text/muted`
    - Buton: fundal `brand/primary`, text `body/small` + `text/inverse`

    **Verificarea:** selectează pe rând fiecare element. În panoul din dreapta, la Fill și la Text, trebuie să apară un **nume de stil**, nu un cod. Dacă apare un cod, ai ratat unul.

### Exercițiu 2 — Buton cu variante
Construiește un set de variante pentru un buton cu proprietățile `Type` (primary, secondary, ghost) și `State` (default, hover, disabled). Nouă variante.

??? success "Soluție"
    | Type | State | Fundal | Text | Contur |
    |------|-------|--------|------|--------|
    | primary | default | `brand/primary` | `text/inverse` | — |
    | primary | hover | `brand/primary-hover` | `text/inverse` | — |
    | primary | disabled | `surface/raised` | `text/muted` | — |
    | secondary | default | transparent | `text/strong` | 1 px `text/muted` |
    | secondary | hover | `surface/raised` | `text/strong` | 1 px `text/base` |
    | secondary | disabled | transparent | `text/muted` | 1 px `surface/raised` |
    | ghost | default | transparent | `brand/primary` | — |
    | ghost | hover | `surface/raised` | `brand/primary` | — |
    | ghost | disabled | transparent | `text/muted` | — |

    **Adaugă și o proprietate Text** pe eticheta butonului, cu valoarea implicită `Butonul`. Acum orice instanță se configurează complet din panoul din dreapta: alegi tipul, starea și scrii textul.

    **Verificare:** plasează 3 instanțe și schimbă-le tipul din meniu. Dacă butonul își păstrează mărimea corectă la texte de lungimi diferite, ai folosit Auto Layout — bine. Dacă textul iese din buton, revino după lecția 09.

### Exercițiu 3 — Card cu slot de pictogramă
Construiește o componentă `card/feature` cu: o pictogramă (slot), un titlu (proprietate Text) și o descriere (proprietate Text). Plasează 4 instanțe cu pictograme diferite din setul făcut în lecția 07.

??? success "Soluție"
    **Construcția componentei:**
    1. Frame 280 × 200, `surface/raised`, rază 16, padding 24.
    2. Înăuntru, pune o instanță a componentei `icon/wifi` — **trebuie** să fie o instanță, nu o copie desenată.
    3. Sub ea, un text `heading/h3` și un text `body/small`.
    4. Selectează tot → ++ctrl+alt+k++ → nume `card/feature`.

    **Proprietățile:**
    - Selectează pictograma → panoul din dreapta arată `Instance` → apasă rombul mic → **Create property** → tip `Instance swap`, nume `Icon`.
    - Selectează titlul → rombul de lângă conținut → **Create property** → tip `Text`, nume `Title`.
    - La fel pentru descriere → `Description`.

    **Utilizarea:** plasezi 4 instanțe. În panoul din dreapta al fiecăreia apar trei câmpuri: un meniu cu toate pictogramele tale și două casete de text. Nu mai intri niciodată în straturi.

    **Testul real:** schimbă acum padding-ul componentei principale de la 24 la 32. Toate cele 4 instanțe se actualizează. Asta e tot rostul exercițiului.

---

## Mini-proiect: bibliotecă de bază pentru cercul de informatică

Construiește un fișier `Design System` cu trei pagini (`Foundations`, `Components`, `Playground`) care conține: setul complet de stiluri, setul de 8 pictograme din lecția 07, și patru componente — `button` (cu variante), `badge`, `card/project` și `input`.

??? success "Soluție"
    **Pagina Foundations** — documentație vizuală, nu doar stiluri invizibile:
    - Un rând de pătrate de 80 × 80 px, câte unul pentru fiecare stil de culoare, cu numele stilului și codul HEX dedesubt.
    - O coloană cu cele 6 stiluri de text, fiecare aplicat pe textul „Cercul de informatică Ursoaia”, cu specificația (mărime / interlinie / greutate) alături.
    - O scară vizuală a spațierii: 8 dreptunghiuri de înălțime 4, 8, 16, 24, 32, 48, 64, 96 px, etichetate.

    **Pagina Components:**

    | Componentă | Proprietăți | Variante |
    |------------|-------------|----------|
    | `button` | Type, State, Label (Text) | 9 |
    | `badge` | Type (info/success/warning/error), Label | 4 |
    | `card/project` | Icon (swap), Title, Description, Tag | 1 |
    | `input` | State (default/focus/error), Placeholder, Label | 3 |

    Plus secțiunea `Icons` cu cele 8 pictograme ca instanțe.

    **Pagina Playground:** construiește un ecran simplu folosind **doar** instanțe și stiluri din bibliotecă — un antet cu logo și navigație, trei carduri de proiect, un formular de înscriere cu două câmpuri și un buton.

    **Criteriul de succes:** schimbă `brand/primary` din portocaliu în albastru, într-un singur loc. Dacă întregul ecran din Playground se actualizează coerent — inclusiv butoanele, badge-urile, stările de focus și pictogramele — biblioteca e construită corect.

    **Dacă ceva nu s-a schimbat:** acel element folosește o culoare scrisă de mână. Găsește-l și înlocuiește-o cu stilul.

---

## Rezumat

- **Stilurile** salvează valori (culoare, text, efect, grilă); le numești **după rol**, cu `/` pentru foldere.
- Un element corect făcut arată în panoul din dreapta un **nume de stil**, nu un cod HEX.
- **Componenta** ◆ e originalul, **instanța** ◇ e copia legată. Modificările curg de sus în jos.
- Într-o instanță poți schimba text, culori, imagini și vizibilitate — **nu** structura.
- **Proprietățile** (Text, Boolean, Instance swap, Variant) transformă suprascrierile în câmpuri.
- **Variantele** grupează versiuni; nu construi 27 dintr-o dată.
- **Instance swap** = slot; orice element care variază, dar rămâne același tip, e slot.
- Ține componentele principale pe o **pagină separată**.
- **Regula de trei:** sub trei utilizări, componenta nu merită.

---

**Pasul următor:** [→ Lecția 09: Auto Layout](09-auto-layout.md)
