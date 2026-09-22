---
lesson: 7
tags: [figma, vectori, pen tool, bezier, svg, pictograme]
summary: Diferența dintre vector și raster, nodurile și mânerele Bézier, unealta Pen și operațiile booleene pentru construit pictograme.
---

# Lecția 07 · Vectori și Pen Tool

!!! tip "Ce vei învăța"
    - Diferența reală dintre **vector** și **raster**
    - Ce sunt **nodurile** și **mânerele Bézier**
    - Cum se folosește unealta **Pen** fără să înnebunești
    - **Stroke**: grosime, capete, colțuri și linii punctate
    - Cum construiești un set de **pictograme** coerent
    - Ce este **SVG** și de ce contează pentru web

---

## Vector vs. raster

| | Vector | Raster |
|---|--------|--------|
| **Cum e stocat** | Formule matematice: puncte, curbe, umpleri | O grilă de pixeli, fiecare cu culoarea lui |
| **La mărire** | Rămâne perfect clar la orice dimensiune | Se pixelează |
| **Mărime fișier** | Mică, crește cu complexitatea formelor | Mare, crește cu dimensiunea în pixeli |
| **Bun pentru** | Logo-uri, pictograme, ilustrații plate, text | Fotografii, texturi, efecte complexe |
| **Formate** | SVG, AI, EPS, PDF | PNG, JPG, WebP, GIF |

!!! note "De ce logo-ul trebuie să fie vector"
    Logo-ul școlii tale va apărea pe o carte de vizită (2 cm) și pe un banner de intrare (2 m). Un PNG bun pentru banner ar avea zeci de MB; unul bun pentru carte de vizită ar fi neclar pe banner.

    Un SVG de 4 KB arată perfect în ambele cazuri. De asta lecția 12 cere logo-ul obligatoriu în vector.

Figma este, în esență, un editor vectorial. Tot ce desenezi cu Rectangle, Ellipse sau Pen este vector. Doar imaginile importate sunt raster.

---

## Noduri și mânere

Orice formă vectorială e definită de **noduri** (puncte) legate prin **segmente**.

```
    ●────────────●        două noduri, segment drept

         ╭───╮
    ●───╯     ╰───●       două noduri, segment curb

    ●─ ─ ─○               nod (●) și mânerul lui (○)
```

### Tipurile de nod

| Tip | Cum arată | Efect |
|-----|-----------|-------|
| **Colț** (corner) | Fără mânere, sau mânere independente | Unghi ascuțit |
| **Neted** (mirrored) | Două mânere simetrice, pe aceeași linie | Curbă continuă, fără frângere |
| **Asimetric** (angle) | Două mânere pe aceeași linie, lungimi diferite | Curbă continuă, dar cu raze diferite |

În Figma, cu nodul selectat, panoul din dreapta îți arată tipul și îl poți schimba.

!!! tip "Mai puține noduri = curbă mai bună"
    Regula practică a ilustratorilor: **un nod la fiecare schimbare de direcție, niciunul în plus**. Un cerc perfect are 4 noduri, nu 12. O curbă cu 20 de noduri va arăta întotdeauna „ondulată”, oricât ai ajusta-o.

    Dacă o formă a ieșit prost, de obicei nu trebuie ajustată — trebuie refăcută cu mai puține noduri.

---

## Unealta Pen

Apasă ++p++. Apoi:

| Acțiune | Rezultat |
|---------|----------|
| **Click** | Adaugă un nod de colț — segment drept |
| **Click și trage** | Adaugă un nod neted — segment curb; lungimea tragerii dă raza curbei |
| **Click pe primul nod** | Închide forma |
| ++esc++ sau ++enter++ | Termină forma deschisă |
| ++alt++ + click pe un nod | Transformă nod neted în nod de colț |

### Editarea unei forme existente

Dublu-click pe formă → intri în **modul de editare vectorială**. Acum:

- ++v++ (Move) mută nodurile individual.
- ++p++ (Pen) adaugă noduri noi pe segmente.
- Tasta ++delete++ șterge un nod și unește segmentele vecine.
- **Bend tool** (++shift+b++) curbează un segment fără să adaugi noduri.

!!! warning "Pen-ul se învață în ore, nu în minute"
    Nimeni nu desenează bine cu Pen din prima. Este singura unealtă din Figma care cere exercițiu muscular, nu doar înțelegere. Exercițiul 2 de mai jos e făcut exact pentru asta — fă-l de trei ori, nu o dată.

    Vestea bună: pentru 90% din munca ta reală vei folosi dreptunghiuri, cercuri și operații booleene, nu Pen.

---

## Stroke — conturul

Orice formă vectorială poate avea **Fill** (umplere) și **Stroke** (contur), independent.

### Proprietățile stroke-ului

| Proprietate | Opțiuni | Când contează |
|-------------|---------|---------------|
| **Weight** | Grosimea în px | Consistența unui set de pictograme |
| **Align** | `Inside`, `Center`, `Outside` | Dimensiunea finală a formei |
| **Cap** | `None`, `Round`, `Square`, `Arrow` | Capetele liniilor deschise |
| **Join** | `Miter`, `Bevel`, `Round` | Aspectul colțurilor |
| **Dash** | Lungime linie / lungime gol | Linii punctate |

!!! note "Align schimbă dimensiunea reală"
    Un pătrat de 100 × 100 px cu stroke de 10 px:
    - `Inside` → ocupă exact 100 × 100 px
    - `Center` → ocupă 110 × 110 px (5 px în afară pe fiecare parte)
    - `Outside` → ocupă 120 × 120 px

    Dacă aliniezi elemente și unul are stroke `Outside`, va părea decalat. Pentru pictograme, folosește `Center` peste tot, consecvent.

### Convertirea stroke-ului în formă

Uneori ai nevoie ca un contur să devină o formă reală (de exemplu ca să-l scalezi fără să se îngroașe). Meniu: **Object → Outline stroke** (++ctrl+shift+o++).

!!! warning "Operația nu se poate anula ușor"
    După `Outline stroke`, nu mai poți schimba grosimea — ai acum un contur al conturului. Fă-o **la final**, și păstrează o copie a versiunii editabile.

---

## Operațiile booleene în profunzime

Le-am atins în lecția 02. Acum, detaliile care contează.

| Operație | Scurtătură | Rezultat |
|----------|-----------|----------|
| **Union** | ++ctrl+alt+u++ | Reuniunea tuturor formelor |
| **Subtract** | ++ctrl+alt+s++ | Prima formă minus toate cele de deasupra |
| **Intersect** | ++ctrl+alt+i++ | Doar zona comună |
| **Exclude** | ++ctrl+alt+x++ | Tot, mai puțin zona comună |

!!! tip "Operațiile rămân editabile"
    Spre deosebire de alte programe, în Figma un grup boolean **nu e distructiv**: poți intra în el (dublu-click) și muta formele componente oricând. Rezultatul se recalculează.

    Când vrei să-l „îngheți” definitiv: **Object → Flatten** (++ctrl+e++). Fă-o doar la export.

### Ordinea contează la Subtract

`Subtract` scade **formele de deasupra** din **cea de dedesubt**. Dacă rezultatul e invers decât te așteptai, selectează forma de deasupra și apasă ++ctrl+shift+bracket-left++ pentru a o trimite în spate (sau rearanjează în panoul Layers).

---

## Construiește un set de pictograme

Un set de pictograme coerent nu înseamnă „desene frumoase”. Înseamnă **reguli respectate identic** în fiecare desen.

### Regulile setului

1. **Grilă fixă.** Toate pictogramele se desenează într-un pătrat de aceeași mărime — standardul e **24 × 24 px**.
2. **Zonă de siguranță.** Desenul ocupă maximum **20 × 20 px** din cei 24; restul e margine. Astfel pictogramele nu se lipesc de text.
3. **Grosime unică.** Toate stroke-urile au aceeași grosime — de obicei **2 px** la o grilă de 24.
4. **Aceleași capete și colțuri.** `Cap: Round` și `Join: Round` peste tot, sau `Square` peste tot. Nu amestecat.
5. **Aceeași rază de colț.** Dacă un dreptunghi are 2 px rază, toate au 2 px.
6. **Aliniere la pixel.** Coordonatele sunt numere întregi. O linie de 2 px la X = 11.5 apare neclară.

!!! note "De ce 24 × 24 și stroke 2"
    24 se împarte la 2, 3, 4, 6, 8 și 12, deci poți centra ușor orice. Stroke-ul de 2 px rămâne clar și la 16 px (se scalează la 1.33) și la 48 px (4 px). Este standardul folosit de Lucide, Feather și majoritatea bibliotecilor moderne.

### Familia vizuală

| Stil | Aspect | Când |
|------|--------|------|
| **Outline** | Doar contur, fără umplere | Navigație, interfețe, stări inactive |
| **Filled** | Umplute solid | Stări active, accente |
| **Duotone** | Contur + umplere parțială cu opacitate | Ilustrații mici, dashboard-uri |

Un set profesionist are **outline pentru toate** și, opțional, o variantă filled pentru starea „selectat”.

---

## SVG și exportul

**SVG** (Scalable Vector Graphics) este format text — se poate deschide într-un editor și citi.

```xml
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <circle cx="12" cy="12" r="10"/>
  <path d="M12 8v4l3 3"/>
</svg>
```

Aceasta e o pictogramă de ceas: un cerc și două linii (acele). 150 de octeți.

### De ce contează `currentColor`

Dacă atributul `stroke` este `currentColor`, pictograma **preia culoarea textului din jur** prin CSS. O singură pictogramă funcționează și pe fundal deschis, și pe fundal închis, fără să exporți două fișiere.

### Export din Figma

1. Selectează pictograma (frame-ul de 24 × 24, nu forma dinăuntru).
2. În panoul din dreapta, jos, la **Export**, apasă **+**.
3. Alege formatul **SVG**.
4. Bifează **Include "id" attribute** doar dacă ai nevoie; de obicei nu.
5. **Export**.

!!! tip "Curăță SVG-ul"
    Figma exportă SVG cu atribute în plus (`width`, `height`, culori fixe). Pentru web, trece fișierul prin [SVGOMG](https://jakearchibald.github.io/svgomg/) — reduce mărimea cu 30–60% și scoate gunoiul.

    Apoi înlocuiește manual culoarea fixă cu `currentColor`.

---

## Exerciții

### Exercițiu 1 — Trei pictograme pe grilă
Construiește, pe o grilă de 24 × 24 px cu stroke 2 px, `Cap: Round`, `Join: Round`: o pictogramă de **casă**, una de **utilizator** și una de **setări** (rotiță sau trei cursoare). Folosește doar forme primare și operații booleene — fără Pen.

??? success "Soluție"
    **Casa:** un triunghi (Polygon cu 3 laturi) de 20 × 10 px pentru acoperiș, sus; un dreptunghi de 14 × 10 px dedesubt pentru pereți; un dreptunghi mic de 5 × 6 px pentru ușă, centrat jos. Toate cu Fill `none`, Stroke 2.

    **Utilizatorul:** un cerc de 8 × 8 px pentru cap, centrat la X = 12, Y = 8; dedesubt, o formă de umeri făcută dintr-un cerc mare de 18 × 18 px din care scazi (Subtract) un dreptunghi care acoperă jumătatea de jos. Rezultă un arc.

    **Setările:** varianta simplă cu trei cursoare — trei linii orizontale de 18 px la Y = 7, 12, 17, plus trei cercuri mici de 4 px așezate pe ele la poziții X diferite (8, 15, 10). Este mai ușor de făcut și mai lizibil la 16 px decât o rotiță dințată.

    **Verificare de consecvență:** pune toate trei una lângă alta la 24 px și apoi la 16 px. Dacă una pare mai groasă sau mai plină decât celelalte, ai încălcat una dintre cele șase reguli.

### Exercițiu 2 — Pen Tool: trasează o literă
Importă în Figma o captură cu litera `S` dintr-un font serif, la 400 px înălțime. Blochează imaginea (++ctrl+shift+l++), scade-i opacitatea la 30% și trasează conturul literei cu Pen.

??? success "Soluție"
    Metoda care funcționează:

    1. Începe cu nodurile de la **extremele curbelor** — punctele cele mai de sus, de jos, stânga și dreapta. Pentru un `S` sunt aproximativ 8 astfel de puncte.
    2. La fiecare, **click și trage** pe direcția tangentei (orizontal la extremele de sus/jos, vertical la cele de stânga/dreapta). Mânerele trebuie să fie **orizontale sau verticale**, nu oblice.
    3. Nu adăuga noduri „ca să iasă mai bine”. Dacă o curbă nu e corectă, ajustează **mânerele** nodurilor existente.
    4. Închide forma pe primul nod.

    **Verificare:** ascunde imaginea de fundal. Litera ta trebuie să arate ca o literă și fără referință. Dacă are „umflături”, ai prea multe noduri sau mânere oblice.

    Fă exercițiul de trei ori, la zile diferite. Diferența dintre prima și a treia încercare va fi mai mare decât te aștepți.

### Exercițiu 3 — Trei forme din operații booleene
Construiește, folosind doar dreptunghiuri și cercuri plus operații booleene: un **semn de vorbire** (bulă de dialog cu coadă), o **pictogramă de descărcare** (săgeată în jos peste o linie) și un **marcaj de locație** (picătura de hartă).

??? success "Soluție"
    **Bula de dialog:** dreptunghi 20 × 14 px cu rază 4, plus un triunghi mic de 5 × 5 px lipit de marginea de jos-stânga. **Union**.

    **Descărcarea:** o linie verticală de 2 × 10 px, plus un triunghi de 10 × 6 px dedesubt (Union pentru săgeată), plus o linie orizontală separată de 16 × 2 px jos — aceasta rămâne separată, nu se unește.

    **Marcajul de locație:** un cerc de 14 × 14 px sus, plus un triunghi de 14 × 10 px cu vârful în jos, suprapuse cu ~4 px. **Union** → rezultă picătura. Apoi un cerc mic de 5 × 5 px în centrul părții rotunde, selectat împreună cu forma → **Subtract** → rezultă gaura.

    **Observație:** niciuna dintre cele trei nu a cerut Pen. Aceasta este regula generală — încearcă întâi cu forme primare, folosește Pen doar când chiar nu se poate altfel.

---

## Mini-proiect: set de 8 pictograme pentru cercul de informatică

Construiește un set coerent de **8 pictograme** de 24 × 24 px pe teme legate de cerc: `cod`, `placă de dezvoltare`, `senzor`, `wifi`, `baterie`, `ciocan de lipit`, `calendar`, `utilizator`. Exportă-le în SVG.

??? success "Soluție"
    **Configurarea:**
    1. Creează un frame de 24 × 24 px, redenumește-l `icon/cod`.
    2. Adaugă-i o grilă de layout: `Grid`, size 1, culoare foarte discretă — te ajută la alinierea pe pixel.
    3. Desenează în interiorul zonei de siguranță de 20 × 20 px (margine 2 px pe fiecare parte).
    4. Duplică frame-ul (++ctrl+d++) pentru fiecare pictogramă nouă și redenumește.

    **Reguli aplicate identic:** Stroke 2 px, `Align: Center`, `Cap: Round`, `Join: Round`, rază de colț 2 px, coordonate întregi.

    **Câteva construcții:**

    | Pictogramă | Construcție |
    |------------|-------------|
    | `cod` | Două perechi de linii formând `<` și `>`, plus o linie oblică la mijloc |
    | `placă` | Dreptunghi 16 × 16 rază 2, plus 3 linii scurte pe fiecare latură (pinii), plus un pătrat mic 6 × 6 în centru (cipul) |
    | `wifi` | Trei arce concentrice (cercuri din care scazi un dreptunghi pentru jumătatea de jos), plus un punct de 2 px |
    | `baterie` | Dreptunghi 18 × 10 rază 2, plus un dreptunghi 2 × 4 lipit la dreapta (borna) |
    | `calendar` | Dreptunghi 18 × 16 rază 2, o linie orizontală la 4 px de sus, două linii verticale scurte deasupra |

    **Exportul:**
    - Selectează toate cele 8 frame-uri.
    - **Export → SVG → Export 8 layers**. Figma le salvează cu numele frame-urilor.
    - Trece fișierele prin SVGOMG și înlocuiește culoarea cu `currentColor`.

    **Testul final de coerență:** pune toate cele 8 pe un rând la 24 px, apoi fă o copie la 16 px și una la 48 px. Într-un set bun, toate cele opt par să aibă aceeași „densitate” la fiecare dimensiune. Dacă una pare mai grea, are prea multe detalii — simplific-o.

---

## Rezumat

- **Vector** = formule, se scalează perfect; **raster** = pixeli, se pixelează.
- Logo-urile și pictogramele sunt **întotdeauna** vector.
- O formă = **noduri** + **segmente**; nodurile pot fi de colț, netede sau asimetrice.
- **Mai puține noduri dau curbe mai bune.** Un cerc are 4 noduri.
- Pen: **click** = colț, **click și trage** = curbă. Se învață prin repetiție.
- `Stroke Align` schimbă **dimensiunea reală** a formei — folosește `Center` consecvent.
- Booleene: **Union, Subtract, Intersect, Exclude** — rămân editabile până la `Flatten`.
- Pictograme: grilă **24 × 24**, zonă de siguranță **20 × 20**, stroke **2 px**, capete și colțuri identice.
- **SVG** cu `currentColor` funcționează pe orice fundal; curăță-l cu SVGOMG.

---

**Pasul următor:** [→ Lecția 08: Stiluri și componente](08-stiluri-si-componente.md)
