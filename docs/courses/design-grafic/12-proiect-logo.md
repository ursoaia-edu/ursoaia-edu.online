---
lesson: 12
tags: [proiect, logo, identitate vizuală, branding, svg]
summary: Proiect complet — de la concept la logo vectorial, cu variante, versiune monocromă, zonă de protecție și reguli de folosire.
---

# Lecția 12 · Logo și identitate vizuală

!!! tip "Ce vei construi"
    Un **logo complet**, cu tot ce înseamnă asta în practică:

    - Concept pornit de la brief, nu din inspirație
    - Trei direcții schițate, una dezvoltată
    - Construcție vectorială pe grilă
    - **Variante:** principală, orizontală, pictogramă, monocromă, negativ
    - **Zonă de protecție** și dimensiune minimă
    - O pagină de **reguli de folosire**

---

## Ce este un logo (și ce nu este)

Un logo **nu** explică ce face organizația. Nu este o ilustrație, nu este o poveste, nu trebuie să conțină o metaforă genială.

Un logo este un **semn de identificare**: ceva ce recunoști rapid, la orice mărime, în orice context. Logo-ul unei companii de transport nu trebuie să conțină un camion; trebuie doar să fie recunoscut ca fiind al companiei respective.

!!! note "Testul de recunoaștere"
    Gândește-te la trei logo-uri pe care le recunoști instant. Aproape sigur sunt **simple**: o formă, una-două culori, uneori doar litere. Complexitatea nu ajută recunoașterea, o împiedică.

### Tipurile de logo

| Tip | Ce conține | Exemplu de structură |
|-----|-----------|----------------------|
| **Wordmark** | Doar numele, desenat cu grijă | Numele complet, tipografie personalizată |
| **Lettermark** | Doar inițialele | „CI” pentru Cercul de Informatică |
| **Pictogramă** | Un simbol abstract sau figurativ | Un semn geometric |
| **Combinat** | Pictogramă + text, folosibile împreună sau separat | Cel mai practic |
| **Emblemă** | Text închis într-o formă (insignă) | Greu de folosit la dimensiuni mici |

!!! tip "Pentru un cerc de școală, alege combinat"
    Ai nevoie de flexibilitate: pictograma singură pentru avatar și favicon, combinația pentru afișe și antet de site. Emblema arată bine pe un tricou și prost pe orice altceva.

---

## Cele cinci criterii ale unui logo bun

| Criteriu | Întrebarea de verificare |
|----------|--------------------------|
| **Simplu** | Îl poți desena din memorie după ce l-ai văzut de două ori? |
| **Memorabil** | Îl deosebești de altele din același domeniu? |
| **Atemporal** | Va arăta bine peste 10 ani, sau e legat de o modă? |
| **Versatil** | Funcționează la 16 px și la 2 metri, în color și alb-negru? |
| **Potrivit** | Tonul se potrivește cu organizația? |

!!! warning "Modele care îmbătrânesc prost"
    Umbre 3D, gradienturi complexe, reflexii „glossy”, fonturi la modă, efecte de lumină. Toate aceste elemente datează un logo la anul în care a fost făcut.

    Un logo desenat plat, cu forme geometrice simple, arăta bine în 1970 și arată bine acum.

---

## Pasul 1 — Brief-ul de identitate

Înainte de orice schiță, răspunde în scris:

1. **Cine suntem?** — o propoziție.
2. **Pentru cine?** — publicul real.
3. **Trei cuvinte** care descriu tonul dorit.
4. **Trei cuvinte** care descriu ce **nu** vrem să părem.
5. **Unde va apărea logo-ul?** — listează toate locurile concrete.
6. **Ce logo-uri similare există?** — ca să nu semeni cu ele.

!!! note "Brief completat — cercul de informatică"
    1. **Cine:** un cerc de elevi care construiesc proiecte de electronică și programare.
    2. **Pentru cine:** elevi de gimnaziu și liceu, plus părinți și profesori.
    3. **Ton dorit:** tehnic, accesibil, practic.
    4. **Ton nevrut:** corporativ, copilăros, elitist.
    5. **Unde:** avatar de Instagram (rotund, 110 px), favicon (32 px), antet de site, afișe A3, tricouri, autocolante, prezentări.
    6. **Similare:** majoritatea cercurilor folosesc o rotiță dințată sau un cip cu pini. Evităm ambele.

---

## Pasul 2 — Schițe

**Pe hârtie, nu în Figma.** Un creion desenează de zece ori mai repede decât mouse-ul, iar în această fază cantitatea contează mai mult decât calitatea.

Regula: **20 de schițe mici** (4 × 4 cm fiecare), în 30 de minute. Nu evalua în timp ce desenezi. Abia la final alegi trei.

### Idei de pornire pentru cercul de informatică

| Direcție | Concept | Risc |
|----------|---------|------|
| Lettermark geometric | `CI` construite din segmente drepte, ca urmele de pe un circuit imprimat | Poate semăna cu alte inițiale |
| Nod de rețea | Trei-patru puncte legate prin linii, sugerând conexiune | Foarte folosit |
| Semnul „mai mic decât” | `</>` stilizat, semnul universal al codului | Prea literal |
| Formă modulară | Un pătrat compus din 4 module care se pot rearanja | Abstract, dar distinctiv |

!!! tip "Cum recunoști o schiță bună"
    Acoper-o cu degetul mare. Dacă silueta rămasă e încă distinctă, e o direcție bună. Dacă devine o pată fără formă, nu.

---

## Pasul 3 — Construcția vectorială

Alege o direcție și construiește-o corect, în Figma.

### Grila de construcție

1. Frame de **240 × 240 px**, numit `logo/construction`.
2. Layout grid: `Grid`, size **24** — deci 10 × 10 module.
3. Al doilea layout grid: `Grid`, size **8**, culoare mai discretă — pentru detalii fine.

Desenează folosind **doar** coordonate care cad pe grilă. Un logo construit pe grilă arată deliberat; unul desenat „la ochi” arată aproximativ.

### Regulile de construcție

| Regulă | De ce |
|--------|-------|
| Grosimi identice de linie | Un logo cu linii de 8 și 9 px arată neîngrijit |
| Unghiuri din setul 0° / 45° / 90° | Unghiurile arbitrare arată accidentale |
| Raze de colț identice | Aceeași rază peste tot, sau zero |
| Coordonate întregi | Jumătățile de pixel dau margini neclare |
| Simetrie unde e posibil | Ochiul o detectează și o citește ca ordine |

!!! warning "Corecția optică"
    Un cerc și un pătrat de aceeași înălțime **nu arată** de aceeași mărime — cercul pare mai mic. Regula: formele rotunde se desenează cu 2–4% mai mari decât cele drepte, ca să pară egale.

    La fel, un triunghi cu vârful în sus pare mai înalt decât un pătrat de aceeași înălțime. Ochiul are dreptate, rigla nu.

### Tipografia din logo

Dacă logo-ul conține text:

1. Alege un font care se potrivește tonului (lecția 04).
2. Ajustează **manual** spațierea dintre litere. Un logo nu folosește niciodată kerning-ul implicit.
3. La final, **convertește textul în vector**: click dreapta → **Outline stroke** pentru contururi, sau **Flatten** (++ctrl+e++) pentru text.

!!! warning "De ce textul din logo se convertește în forme"
    Dacă logo-ul rămâne text, oricine deschide fișierul fără fontul respectiv va vedea altceva. Un logo convertit în vector arată identic pe orice calculator, în orice program.

    **Păstrează două fișiere:** unul cu textul editabil (pentru viitor) și unul convertit (pentru livrare).

---

## Pasul 4 — Variantele

Un logo nu este un fișier. Este un **set**.

| Variantă | Când se folosește | Fișier |
|----------|-------------------|--------|
| **Principală** (verticală) | Afișe, prezentări, spații pătrate | `logo-primary.svg` |
| **Orizontală** | Antet de site, semnături, bannere late | `logo-horizontal.svg` |
| **Pictogramă** | Avatar, favicon, autocolante mici | `logo-mark.svg` |
| **Monocromă (negru)** | Fax, ștampile, tipar alb-negru | `logo-black.svg` |
| **Monocromă (alb)** | Pe fundaluri închise sau fotografii | `logo-white.svg` |

!!! note "Varianta orizontală nu este cea principală întinsă"
    Când treci de la vertical la orizontal, **recompui**: pictograma trece în stânga textului, mărimea relativă se ajustează, spațierea se recalculează. Nu scalezi neproporțional.

### Testul de reducere

Pune varianta pictogramă la **16 px**. Ce se întâmplă?

- Dacă detaliile se topesc într-o pată → simplifică. Scoate elementele mici.
- Dacă golurile interioare se închid → mărește-le sau subțiază liniile.
- Dacă încă se recunoaște → logo-ul trece testul.

!!! tip "Fă o versiune simplificată pentru dimensiuni mici"
    Multe logo-uri profesioniste au o variantă „compactă”, cu mai puține detalii, folosită sub 32 px. Nu e o înfrângere, e o practică normală.

---

## Pasul 5 — Zona de protecție și dimensiunea minimă

### Zona de protecție (clear space)

Spațiul gol minim din jurul logo-ului, în care nu are voie să intre nimic — nici text, nici alte logo-uri, nici marginea paginii.

**Se definește relativ**, nu în milimetri, ca să funcționeze la orice mărime:

> Zona de protecție = **înălțimea literei „C” din logo**, pe toate cele patru laturi.

Sau, pentru un logo fără text: jumătate din lățimea pictogramei.

### Dimensiunea minimă

Cea mai mică dimensiune la care logo-ul mai e lizibil. Se stabilește **prin testare**, nu prin calcul:

| Variantă | Minim tipic (ecran) | Minim tipic (tipar) |
|----------|---------------------|---------------------|
| Principală | 120 px lățime | 30 mm lățime |
| Orizontală | 160 px lățime | 40 mm lățime |
| Pictogramă | 24 px | 8 mm |

Tipărește-le la aceste dimensiuni și privește-le. Dacă ceva se pierde, mărește minimul.

---

## Pasul 6 — Regulile de folosire

O pagină, cu exemple vizuale. Este documentul care face diferența dintre un logo și o identitate vizuală.

### Ce conține

1. **Variantele** — toate cele cinci, cu numele fișierelor.
2. **Zona de protecție** — desenată, cu unitatea de măsură marcată.
3. **Dimensiunile minime** — pentru fiecare variantă.
4. **Culorile** — HEX, RGB, și echivalentul CMYK dacă se tipărește.
5. **Pe ce fundaluri** — exemple: pe alb, pe culoarea de brand, pe fotografie, pe negru.
6. **Ce nu se face** — cel mai util capitol.

### Lista „ce nu se face”

Desenează fiecare greșeală, cu un X roșu peste:

- Nu se întinde neproporțional
- Nu se rotește
- Nu se schimbă culorile
- Nu se adaugă umbre sau efecte
- Nu se rearanjează elementele
- Nu se pune pe fundaluri cu contrast insuficient
- Nu se pune într-un chenar care nu face parte din logo
- Nu se schimbă fontul

!!! note "De ce capitolul negativ e cel mai util"
    Oamenii care vor folosi logo-ul (profesori, colegi, tipografia) nu vor citi teoria. Se vor uita la imaginile cu X roșu și vor înțelege în 5 secunde. Investește efort acolo.

---

## Exerciții

### Exercițiu 1 — 20 de schițe
Pe hârtie, în 30 de minute, desenează 20 de schițe de logo pentru cercul de informatică. Nu evalua în timpul desenării. La final, alege trei și motivează alegerea într-o propoziție fiecare.

??? success "Soluție"
    Nu există un răspuns corect, dar procesul are indicatori clari:

    - **Dacă ai făcut sub 12 schițe**, ai evaluat în timp ce desenai. Următoarea dată, pune un cronometru de 90 de secunde per schiță.
    - **Dacă toate cele 20 seamănă între ele**, ai rămas blocat pe o idee. Forțează-te: fă 5 doar din litere, 5 doar din forme geometrice, 5 abstracte, 5 figurative.
    - **Dacă la final nu-ți place niciuna**, e normal. Alege cele trei cu silueta cea mai distinctă, nu cele mai „frumoase” — frumusețea vine la rafinare, silueta nu.

    **Motivațiile bune sună așa:** „Aceasta rămâne recunoscibilă când o acopăr pe jumătate.” „Aceasta nu seamănă cu nicio rotiță dințată.” „Aceasta se poate desena din 4 linii — merge la 16 px.”

    **Motivațiile slabe:** „Aceasta îmi place.” „Aceasta arată profesionist.”

### Exercițiu 2 — Construcție pe grilă
Ia una dintre cele trei schițe și construiește-o vectorial pe o grilă de 10 × 10 module. Toate coordonatele trebuie să cadă pe grilă.

??? success "Soluție"
    **Exemplu — lettermark `CI` geometric:**

    1. Frame 240 × 240, grilă de 24 px (10 module).
    2. Litera `C`: un cerc de 144 × 144 px (6 module), Fill `none`, Stroke 24 px (1 modul), `Align: Center`. Apoi scazi (Subtract) un dreptunghi de 72 × 48 px din partea dreaptă → rezultă deschiderea literei C.
    3. Litera `I`: un dreptunghi de 24 × 144 px (1 × 6 module), la 24 px distanță de C.
    4. Verifică: toate coordonatele sunt multipli de 24, toate grosimile sunt 24.

    **Corecția optică necesară:** cercul de 144 px pare mai mic decât bara verticală de 144 px. Mărește cercul la 150 px (Y: −3) ca să pară egale. **Acesta e singurul loc unde ai voie să ieși de pe grilă** — și notează de ce.

    **Verificarea finală:** copiază logo-ul la 16 px. Deschiderea literei C mai e vizibilă? Dacă nu, mărește-o de la 48 la 60 px în construcția originală.

### Exercițiu 3 — Setul de variante
Generează toate cele cinci variante din logo-ul construit la exercițiul 2 și testează-le pe cinci fundaluri diferite.

??? success "Soluție"
    **Variantele:**

    | Fișier | Construcție |
    |--------|-------------|
    | `logo-primary.svg` | Pictograma sus, numele dedesubt, centrat. Raport: numele are lățimea pictogramei × 1.6 |
    | `logo-horizontal.svg` | Pictograma stânga, numele dreapta, aliniat vertical pe centru optic. Gap = jumătate din lățimea pictogramei |
    | `logo-mark.svg` | Doar pictograma, în frame pătrat cu margine egală cu 1 modul |
    | `logo-black.svg` | Tot pe `#111827`, zero culori |
    | `logo-white.svg` | Tot pe `#FFFFFF`, zero culori |

    **Testele pe fundaluri:**

    | Fundal | Ce variantă | Rezultat așteptat |
    |--------|-------------|-------------------|
    | Alb | primary color | Trece |
    | `brand/primary` portocaliu | `logo-white` | Trece |
    | `#0F172A` închis | `logo-white` | Trece |
    | Fotografie luminoasă | `logo-black` + umbră discretă | Trece cu umbră |
    | Fotografie aglomerată | Niciuna | **Cade** — aici nu se pune logo direct; pune-l pe o bandă plată |

    **Ultimul rând e cel mai important de reținut:** un logo nu funcționează peste orice. Regulile de folosire trebuie să spună explicit „pe fotografii cu detaliu mare, logo-ul se așază pe o bandă de culoare plată”.

---

## Mini-proiect: identitatea vizuală a cercului tău

Construiește setul complet pentru cercul tău de informatică (sau pentru o altă organizație reală din școală): logo cu toate variantele, paletă, fonturi și o pagină de reguli de folosire.

??? success "Livrabilele și criteriile"
    **Fișierul Figma** cu trei pagini:

    | Pagina | Conținut |
    |--------|----------|
    | `Explorations` | Cele 20 de schițe scanate + cele 3 direcții digitalizate |
    | `Logo` | Grila de construcție, cele 5 variante, testele de reducere, testele pe fundaluri |
    | `Guidelines` | Pagina de reguli, gata de exportat ca PDF |

    **Fișierele exportate:**

    ```
    logo/
      logo-primary.svg
      logo-horizontal.svg
      logo-mark.svg
      logo-black.svg
      logo-white.svg
      logo-mark-32.png      (favicon)
      logo-mark-512.png     (avatar rețele sociale)
    guidelines.pdf
    ```

    **Criteriile de evaluare:**

    | # | Criteriu | Verificare |
    |---|----------|-----------|
    | 1 | Logo-ul se desenează din memorie | Arată-l unui coleg 10 secunde, cere-i să-l deseneze |
    | 2 | Funcționează la 16 px | Exportă și privește pe telefon |
    | 3 | Funcționează monocrom | Varianta black pe alb, la 3 metri |
    | 4 | Construit pe grilă | Toate coordonatele pe module, cu excepțiile documentate |
    | 5 | Textul e convertit în vector | Deschide SVG-ul pe un calculator fără fontul respectiv |
    | 6 | Zona de protecție definită relativ | Nu în mm, ci raportat la o parte a logo-ului |
    | 7 | Capitolul „ce nu se face” are ≥ 6 exemple desenate | Numără-le |
    | 8 | Paleta trece testele de contrast | Plugin Contrast pe fiecare pereche |

    **Testul final, cel care contează:** dă setul de fișiere unui coleg care nu a participat la proiect și cere-i să facă un afiș simplu folosind doar ghidul. Dacă reușește fără să te întrebe nimic, identitatea vizuală e completă. Dacă te întreabă „ce culoare pun aici?”, ghidul are o lipsă — completeaz-o.

---

## Rezumat

- Un logo este un **semn de identificare**, nu o explicație și nu o ilustrație.
- Cinci tipuri: wordmark, lettermark, pictogramă, **combinat** (cel mai practic), emblemă.
- Cinci criterii: **simplu, memorabil, atemporal, versatil, potrivit**.
- Începi cu un **brief de identitate**, apoi **20 de schițe pe hârtie**, apoi trei direcții.
- Construiești **pe grilă**, cu grosimi identice și unghiuri din setul 0/45/90.
- **Corecția optică** e permisă și necesară — documentează-o.
- Textul din logo se **convertește în vector** la livrare.
- Un logo este un **set de 5 variante**, nu un fișier.
- **Zona de protecție** se definește relativ la logo, nu în milimetri.
- Capitolul **„ce nu se face”** este cel mai citit din tot ghidul.

---

**Pasul următor:** [→ Lecția 13: Postare pentru rețele sociale](13-proiect-social-media.md)
