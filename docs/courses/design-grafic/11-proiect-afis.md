---
lesson: 11
tags: [proiect, afiș, print, a3, tipar, compoziție]
summary: Proiect complet — un afiș A3 pentru un eveniment școlar, de la brief la fișierul PDF pregătit pentru tipar.
---

# Lecția 11 · Afiș pentru un eveniment școlar

!!! tip "Ce vei construi"
    Un **afiș A3 complet**, pornind de la brief și ajungând la un PDF pregătit pentru tipar:

    - Brief completat și conținut ierarhizat
    - Două direcții vizuale diferite, pentru feedback
    - Varianta finală, cu grilă, paletă și tipografie coerente
    - Verificări de contrast, margini și rezoluție
    - Export PDF cu bleed, plus o variantă digitală pentru afișare pe ecrane

---

## Pasul 1 — Brief-ul

Folosim brief-ul din lecția 00. Iată-l completat pentru proiectul nostru:

| Întrebare | Răspuns |
|-----------|---------|
| **Ce** | Afiș A3 portret, tipar color, 15 exemplare |
| **Pentru cine** | Elevi de clasele V–XII care trec pe holuri în pauză |
| **Mesaj** | „Sâmbătă poți vedea proiectele construite de colegii tăi.” |
| **Acțiune** | Să vină sâmbătă, 12 aprilie, între 10:00 și 14:00, în sala de sport |
| **Unde** | Trei holuri, la nivelul ochilor, lângă scări |
| **Constrângeri** | Logo-ul școlii obligatoriu, fără poze cu elevi, gata în 7 zile |

!!! note "Distanța de citire schimbă tot"
    Un afiș pe hol se citește de la **2–4 metri**. La A3 (29.7 × 42 cm), asta înseamnă:

    - Titlul trebuie citit de la 4 m → minimum **90 pt**
    - Informația principală (data) de la 3 m → minimum **50 pt**
    - Detaliile de la 1 m → minimum **16 pt**

    Regula empirică: **1 cm înălțime de literă ≈ 3 metri distanță de citire**.

---

## Pasul 2 — Conținutul ierarhizat

Scrie tot textul înainte să desenezi ceva. Apoi numerotează.

```
1. TÂRGUL DE PROIECTE
2. Sâmbătă, 12 aprilie · 10:00 – 14:00
3. Sala de sport, etaj 1
4. Roboți, senzori, jocuri și site-uri construite
   de elevii cercului de informatică.
5. Intrarea liberă
6. Cercul de informatică Ursoaia · ursoaia-edu.online
```

**Gruparea:** `[1]`, `[2 + 3]`, `[4]`, `[5 + 6]` → patru grupuri. Exact în intervalul 3–5 din lecția 05.

!!! warning "Taie textul înainte să-l pui pe afiș"
    Prima variantă a punctului 4 suna așa: „Vino să descoperi proiectele fascinante realizate de colegii tăi de-a lungul întregului an școlar, într-un eveniment care promite să fie memorabil.” 27 de cuvinte, zero informație.

    Varianta finală: „Roboți, senzori, jocuri și site-uri construite de elevii cercului de informatică.” 12 cuvinte, patru substantive concrete. Un afiș nu e un text, e o listă de fapte.

---

## Pasul 3 — Configurarea fișierului

1. Frame nou: ++f++ → categoria **Paper** → **A3**. Rezultă 842 × 1191 pt (punctele Figma = 1/72 inch; A3 = 29.7 × 42 cm).
2. Redenumește-l `afis-targ-proiecte`.
3. **Grilă:** Layout grid → Columns → Count **6**, Type `Stretch`, Margin **60**, Gutter **24**.
4. **A doua grilă:** Rows → Count `Auto`, Height **24** — grila de linii de bază.
5. **Marginea de siguranță:** desenează un dreptunghi la 60 pt de toate marginile, fără umplere, cu contur roșu 1 pt. Blochează-l (++ctrl+shift+l++). Nimic important nu iese în afara lui.

!!! note "De ce 6 coloane și nu 12"
    Un afiș are mult mai puține elemente decât o pagină web. 6 coloane dau suficientă flexibilitate (1/2, 1/3, 2/3) fără să te tenteze să fragmentezi conținutul.

### Stilurile

Importă sau recreează stilurile din lecțiile 03 și 04. Pentru acest afiș:

| Stil | Valoare |
|------|---------|
| `surface/base` | `#0F172A` |
| `brand/primary` | `#F97316` |
| `text/strong` | `#F8FAFC` |
| `text/base` | `#CBD5E1` |
| `text/muted` | `#64748B` |
| `poster/title` | Inter Bold, 104 pt, interlinie 1.05, tracking −2% |
| `poster/date` | Inter Semi Bold, 52 pt, interlinie 1.2 |
| `poster/body` | Inter Regular, 26 pt, interlinie 1.4 |
| `poster/label` | Inter Medium, 18 pt, majuscule, tracking +12% |
| `poster/detail` | Inter Regular, 16 pt, interlinie 1.4 |

---

## Pasul 4 — Două direcții

Regula din lecția 00: **nu arăta niciodată o singură variantă**. Construiește două, vizibil diferite.

### Direcția A — tipografică

Fără imagini. Titlul ocupă treimea de sus, pe trei rânduri. Sub el, o bară portocalie de 8 × 240 pt. Data mare, sub bară. Descrierea pe coloanele 1–4. Detaliile jos, pe un singur rând.

**Punct forte:** imposibil de ratat, se citește de la 5 metri, se tipărește perfect chiar și alb-negru.
**Punct slab:** nu comunică nimic despre *ce fel* de eveniment e.

### Direcția B — cu imagine

O fotografie a unui proiect (o placă ESP32 cu LED-uri aprinse, macro) ocupă treimea de sus, sângerând până la marginile frame-ului. Gradient de la opac jos la transparent sus. Titlul peste gradient. Restul conținutului pe fundal plat, dedesubt.

**Punct forte:** spune imediat despre ce e vorba; atrage privirea de la distanță.
**Punct slab:** depinde de calitatea fotografiei; la tipar alb-negru se pierde.

!!! tip "Cum ceri feedback pe cele două direcții"
    Nu întreba „care îți place”. Întreabă:

    - „Uită-te 3 secunde la fiecare. Ce ai reținut din fiecare?”
    - „Care te-ar face mai probabil să vii?”
    - „Din care ai înțeles mai repede ce fel de eveniment e?”

---

## Pasul 5 — Construirea variantei finale

Presupunem că feedback-ul a ales direcția B. Construcția, element cu element.

### 5.1 — Fundalul

1. Dreptunghi peste tot frame-ul, Fill `surface/base`. Redenumește `bg`.

### 5.2 — Fotografia

1. Dreptunghi de 842 × 480 pt, lipit de marginea de sus (X: 0, Y: 0).
2. Fill → `Image` → alege fotografia. Mod **Fill**.
3. Dublu-click și repoziționează astfel încât subiectul principal să fie în jumătatea dreaptă (titlul va sta în stânga).

!!! warning "Verifică rezoluția acum, nu la final"
    Afișul are 29.7 cm lățime. La 300 DPI: 29.7 / 2.54 × 300 = **3508 px**. Fotografia ta trebuie să aibă **minimum 3508 px lățime** dacă se întinde pe toată lățimea.

    Dacă are 1800 px, fie o folosești pe jumătate de lățime, fie cauți alta. Verifică în panoul din dreapta, la Fill → click pe imagine → Figma afișează dimensiunea originală.

### 5.3 — Gradientul

1. Dreptunghi de 842 × 480 pt, exact peste fotografie.
2. Fill → `Linear gradient`.
3. Punctul de jos: `#0F172A`, opacitate **100%**. Punctul de sus: `#0F172A`, opacitate **0%**.
4. Trage mânerul gradientului pe verticală, de jos în sus.

### 5.4 — Titlul

1. Text pe trei rânduri: `TÂRGUL / DE / PROIECTE`.
2. Stil `poster/title`, culoare `text/strong`.
3. Poziționat pe coloanele 1–4, cu linia de bază a ultimului rând la ~60 pt sub marginea de jos a fotografiei.

!!! note "De ce titlul intră peste fotografie"
    Suprapunerea leagă cele două zone. Dacă titlul ar sta complet sub fotografie, afișul s-ar rupe în două benzi orizontale independente. Suprapunerea de ~80 pt creează continuitate.

### 5.5 — Bara de accent

Dreptunghi de 8 × 200 pt, Fill `brand/primary`, la 40 pt sub titlu, aliniat la stânga cu el.

### 5.6 — Data și locul

1. `Sâmbătă, 12 aprilie` — stil `poster/date`, culoare `brand/primary`.
2. `10:00 – 14:00 · Sala de sport, etaj 1` — stil `poster/body`, culoare `text/base`, la 12 pt sub dată.

Cele două formează un grup: spațiu de 12 pt între ele, 48 pt față de bara de deasupra.

### 5.7 — Descrierea

Text pe coloanele 1–4 (nu pe toate 6 — lungimea rândului!), stil `poster/body`, culoare `text/base`, la 48 pt sub grupul datei.

Verifică: **maximum 66 de caractere pe rând**. La 26 pt, asta înseamnă o lățime de aproximativ 460 pt.

### 5.8 — Zona de jos

Auto Layout orizontal, gap `Auto`, lățime `Fill`, ancorat la 60 pt de marginea de jos:

- Stânga: logo-ul școlii (SVG, înălțime 48 pt) + text `Cercul de informatică Ursoaia`, stil `poster/detail`.
- Dreapta: `Intrarea liberă` (stil `poster/label`, culoare `brand/primary`) + `ursoaia-edu.online` (stil `poster/detail`, culoare `text/muted`).

Deasupra zonei, o linie de separare de 1 pt, culoare `#1E293B`.

---

## Pasul 6 — Verificările

Parcurge lista înainte de export. Fiecare punct a apărut într-o lecție anterioară.

| # | Verificare | Cum | Lecția |
|---|-----------|-----|--------|
| 1 | Testul de blur | Layer blur 20 pe o copie — titlul e pata dominantă? | 02 |
| 2 | Testul celor 3 secunde | Arată-l la 3 colegi, întreabă ce au reținut | 00 |
| 3 | Contrastul titlului | Plugin Contrast, pe cel mai deschis punct de sub text | 03 |
| 4 | Contrastul detaliilor | `text/muted` pe `surface/base` ≥ 4.5:1 | 03 |
| 5 | Marginile | Nimic important sub 60 pt de margine | 02 |
| 6 | Lungimea rândului | Descrierea ≤ 66 caractere / rând | 04 |
| 7 | Alinierea | Toate elementele pornesc de pe o coloană a grilei | 05 |
| 8 | Spațierea | Toate valorile sunt multipli de 8 (sau 12 pt) | 05 |
| 9 | Rezoluția fotografiei | ≥ 3508 px pe lățimea afișată | 10 |
| 10 | Testul alb-negru | Saturation −100 — se mai înțelege? | 03 |

!!! warning "Testul 10 nu e opțional aici"
    Brief-ul spune tipar color, dar afișele se fotocopiază. Dacă la −100 saturație data devine invizibilă (pentru că era portocalie pe fundal închis, iar ambele devin gri asemănător), schimbă: fă data albă și lasă doar bara portocalie ca accent.

---

## Pasul 7 — Exportul

### Pentru tipar

1. **Bleed.** Dacă tipografia cere 3 mm bleed: mărește frame-ul cu 3 mm pe fiecare latură. 3 mm = 8.5 pt, deci frame-ul devine **859 × 1208 pt**. Extinde `bg` și fotografia până la noile margini. Conținutul rămâne unde e.
2. Selectează frame-ul → Export → **PDF** → Export.
3. Deschide PDF-ul și verifică: fonturile arată corect, imaginea nu e pixelată la 100% zoom.

!!! note "Dacă tipografia nu cere bleed"
    Multe copy-shop-uri tipăresc direct pe A3 fără tăiere. Atunci nu ai nevoie de bleed, dar **fundalul trebuie să ajungă exact la margine** și trebuie să știi că imprimanta poate lăsa o bandă albă de 3–5 mm. Întreabă înainte.

### Pentru ecrane

Multe școli au ecrane pe holuri sau conturi de rețele sociale.

| Variantă | Format | Dimensiune | Notă |
|----------|--------|------------|------|
| Ecran hol (orizontal) | PNG 2× | 1920 × 1080 | Recompune: afișul vertical nu încape |
| Instagram post | JPG | 1080 × 1080 | Recompune la pătrat |
| Instagram story | JPG | 1080 × 1920 | Aproape același raport ca A3 — cea mai ușoară adaptare |

!!! warning "Nu întinde afișul A3 la alt format"
    Raportul A3 este 1:1.41. Un post de Instagram e 1:1. Dacă scalezi neproporțional, tipografia se deformează și se vede imediat.

    **Fă un frame nou** pentru fiecare format și refolosește elementele. Cu stiluri și componente, asta durează 10 minute, nu o oră.

---

## Erori frecvente la afișe

| Eroare | De ce e problemă | Corecția |
|--------|------------------|----------|
| Prea mult text | Nimeni nu citește un afiș ca pe o carte | Maximum 6 blocuri, maximum 40 de cuvinte total |
| Titlu prea mic | Nu se citește de la distanța reală | 1 cm literă ≈ 3 m distanță |
| Text lipit de margine | Se taie la tipar | Minimum 10 mm, ideal 15–20 mm pe A3 |
| Fotografie de rezoluție mică | Pixelată la tipar | Verifică înainte de a începe, nu la final |
| Cinci culori | Ochiul nu știe unde să meargă | O primară, un accent, restul neutre |
| Data mai mică decât titlul decorativ | Informația vitală se pierde | Data e nivel secundar, dar niciodată terțiar |
| Font decorativ pe tot afișul | Obositor, ilizibil de departe | Font decorativ **doar** pe titlu |
| Fără informația de contact | Nimeni nu poate afla mai mult | Măcar un site sau o sală |

---

## Exerciții

### Exercițiu 1 — Taie textul
Ia următorul text de brief și redu-l la maximum 40 de cuvinte totale, păstrând toate informațiile esențiale:

> „Cercul de informatică al școlii noastre are deosebita plăcere de a vă invita la Târgul de Proiecte, un eveniment special care va avea loc în data de sâmbătă, 12 aprilie, începând cu ora 10:00 și până la ora 14:00, în sala de sport situată la etajul 1 al clădirii principale, unde veți putea admira o gamă variată de proiecte realizate de elevii noștri talentați pe parcursul întregului an școlar, incluzând roboți, senzori, jocuri și site-uri web. Intrarea este complet gratuită pentru toată lumea.”

??? success "Soluție"
    89 de cuvinte → 32 de cuvinte:

    ```
    TÂRGUL DE PROIECTE

    Sâmbătă, 12 aprilie · 10:00 – 14:00
    Sala de sport, etaj 1

    Roboți, senzori, jocuri și site-uri construite
    de elevii cercului de informatică.

    Intrarea liberă
    Cercul de informatică Ursoaia · ursoaia-edu.online
    ```

    **Ce s-a tăiat și de ce:**
    - „are deosebita plăcere de a vă invita” → politețe care ocupă spațiu; afișul *este* invitația.
    - „un eveniment special care va avea loc” → redundant, data spune deja asta.
    - „situată la etajul 1 al clădirii principale” → „etaj 1” e suficient într-o școală.
    - „o gamă variată de proiecte realizate de elevii noștri talentați pe parcursul întregului an școlar” → înlocuit cu cele patru substantive concrete. Concretul convinge, adjectivele nu.
    - „complet gratuită pentru toată lumea” → „liberă”.

    **Verificare:** citește varianta scurtă cu voce tare. Lipsește vreo informație de care are nevoie cineva ca să vină? Nu.

### Exercițiu 2 — Corectează un afiș
Construiește deliberat un afiș A3 cu cinci greșeli din tabelul de mai sus, apoi fă versiunea corectată. Notează fiecare corecție.

??? success "Soluție"
    Exemplu de afiș greșit și corecțiile:

    | Greșeala introdusă | Efectul | Corecția |
    |--------------------|---------|----------|
    | Titlu la 40 pt | Ilizibil de la 3 m (40 pt ≈ 1.4 cm ≈ 4 m teoretic, dar cu font subțire nu se vede) | 104 pt Bold |
    | Text la 15 pt de margine | Risc de tăiere | 60 pt (≈ 21 mm) |
    | 4 culori de accent | Nicio ierarhie de culoare | Doar `brand/primary` |
    | Descriere pe toată lățimea (842 pt) | ~120 caractere / rând | Pe 4 coloane, ~460 pt |
    | Titlu centrat pe 3 rânduri | Margine stângă zimțată | Aliniat la stânga |

    După corecții, aplică testul de blur pe ambele variante. Diferența trebuie să fie evidentă: în varianta greșită, petele sunt toate de aceeași intensitate; în cea corectă, titlul domină clar.

### Exercițiu 3 — Adaptare la trei formate
Ia afișul final și adaptează-l la: Instagram post (1080 × 1080), story (1080 × 1920) și ecran orizontal (1920 × 1080). Nu scala — recompune.

??? success "Soluție"
    | Format | Ce se schimbă |
    |--------|---------------|
    | **Story 1080 × 1920** | Raport 1:1.78 vs. A3 1:1.41. Fotografia crește proporțional mai mult, textul rămâne la fel. Cea mai ușoară adaptare: mărește zona foto la 45% din înălțime și lasă restul identic ca structură. |
    | **Post 1080 × 1080** | Pătrat — nu încape structura verticală. Soluție: fotografie pe jumătatea de sus, conținut pe jumătatea de jos; **scoate** descrierea (o pui în caption-ul postării). Rămân titlu, dată, loc, logo. |
    | **Ecran 1920 × 1080** | Orizontal — inversează structura: fotografie pe 45% din lățime în dreapta, tot textul aliniat stânga pe 55%. Titlul poate scădea la 72 pt, fiindcă ecranul se privește de la 3–5 m dar are luminozitate proprie. |

    **Ce rămâne identic în toate patru:** paleta, fontul, raportul dintre nivelurile ierarhiei, bara portocalie de accent, poziția logo-ului.

    **Acesta e testul unei identități vizuale reale:** patru formate complet diferite, dar recunoscute instant ca fiind același eveniment. Exact ce vei construi sistematic în lecția 12.

---

## Mini-proiect: afișul tău

Alege un eveniment **real** din școala ta și parcurge toți cei șapte pași: brief, conținut ierarhizat, configurare fișier, două direcții, variantă finală, cele 10 verificări, export PDF + o variantă digitală.

??? success "Criteriile de evaluare"
    Un afiș reușit trece toate cele nouă puncte:

    | # | Criteriu | Cum se verifică |
    |---|----------|-----------------|
    | 1 | Brief complet, scris | Cele 6 întrebări au răspuns |
    | 2 | Maximum 40 de cuvinte | Numără-le |
    | 3 | 3–5 grupuri vizuale | Testul de blur |
    | 4 | Ierarhie clară | 3 persoane × 3 secunde dau același răspuns |
    | 5 | Titlu citibil de la 3 m | Tipărește-l și du-te 3 metri înapoi |
    | 6 | Contrast ≥ 4.5:1 peste tot | Plugin Contrast |
    | 7 | Margini ≥ 15 mm | Dreptunghiul de siguranță |
    | 8 | O primară + un accent | Numără culorile |
    | 9 | PDF care se deschide corect | Deschide-l pe alt calculator |

    **Livrabilele:**
    - `afis-<eveniment>.pdf` — pentru tipar
    - `afis-<eveniment>-story.jpg` — 1080 × 1920
    - Fișierul Figma cu **ambele direcții** păstrate (nu șterge varianta neselectată — e dovada procesului)

    **Bonus real:** tipărește-l și pune-l efectiv pe hol. Apoi întreabă trei colegi care nu știu nimic despre eveniment ce au înțeles. Acesta e singurul test care contează cu adevărat.

---

## Rezumat

- Începi cu **brief-ul**, nu cu Figma.
- **1 cm înălțime de literă ≈ 3 metri** distanță de citire.
- Maximum **40 de cuvinte** și **6 blocuri** pe un afiș.
- Taie politețea și adjectivele; păstrează **substantivele concrete**.
- Construiește **două direcții** vizibil diferite înainte de a cere feedback.
- Grilă de **6 coloane** pentru afișe, margine minimă **60 pt** pe A3.
- Suprapunerea titlului peste fotografie **leagă** zonele; fără ea, afișul se rupe în benzi.
- Verifică **rezoluția fotografiei la început**: A3 la 300 DPI = 3508 px lățime.
- Cele **10 verificări** înainte de export, inclusiv testul alb-negru.
- Adaptarea la alt format înseamnă **recompunere**, nu scalare.

---

**Pasul următor:** [→ Lecția 12: Logo și identitate vizuală](12-proiect-logo.md)
