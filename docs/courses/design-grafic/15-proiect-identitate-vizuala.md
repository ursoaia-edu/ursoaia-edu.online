---
lesson: 15
tags: [proiect final, identitate vizuală, brand book, design system, portofoliu]
summary: Proiect final — asamblarea tuturor lecțiilor într-o identitate vizuală completă, cu brand book și set de aplicații reale.
---

# Lecția 15 · Proiect: identitate vizuală completă

!!! tip "Ce vei construi"
    O **identitate vizuală completă** pentru cercul de informatică, adică tot ce ai nevoie ca oricine să poată produce materiale coerente fără să te întrebe nimic:

    - Platforma de brand: cine suntem, pentru cine, ce ton
    - Logo cu toate variantele (din lecția 12)
    - Sistem de culoare, tipografie și spațiere
    - Bibliotecă de componente în Figma
    - **Șase aplicații reale**: afiș, postare, prezentare, card de membru, tricou, antet de site
    - **Brand book** exportabil ca PDF

---

## Ce face diferența dintre un logo și o identitate

Un logo răspunde la întrebarea „cum ne recunoaște cineva”.

O identitate vizuală răspunde la o întrebare mult mai grea: **„cum arată *orice* material pe care îl producem, făcut de *oricine*, peste doi ani?”**

Testul practic: dacă un coleg nou trebuie să facă un afiș și îți trimite trei întrebări pe WhatsApp („ce font?”, „ce portocaliu?”, „cât de mare pun logo-ul?”), identitatea ta nu e completă. Răspunsurile trebuie să fie deja scrise.

---

## Structura proiectului

```
Fișier Figma: "Identitate vizuală — Cercul de informatică"
│
├── 01 · Brand platform      → cine suntem, ton, public
├── 02 · Logo                → construcție, variante, reguli
├── 03 · Foundations         → culoare, tipografie, spațiere, grilă
├── 04 · Components          → butoane, carduri, badge-uri, pictograme
├── 05 · Applications        → cele 6 aplicații reale
└── 06 · Brand book          → paginile pentru export PDF
```

---

## Pagina 01 — Platforma de brand

O pagină de text, dar cea care decide tot restul. Șase blocuri:

| Bloc | Conținut | Lungime |
|------|----------|---------|
| **Misiune** | Ce facem și de ce | 1 propoziție |
| **Public** | Cine ne vede materialele | 2–3 grupuri concrete |
| **Personalitate** | 3 adjective pe care le urmărim | 3 cuvinte |
| **Anti-personalitate** | 3 adjective pe care le evităm | 3 cuvinte |
| **Ton de comunicare** | Cum scriem: formal / direct / prietenos, cu exemple | 3 perechi „așa da / așa nu” |
| **Diferențiere** | Ce ne face să nu semănăm cu alte cercuri | 1–2 propoziții |

!!! note "Exemplu completat"
    **Misiune:** construim proiecte reale de electronică și programare și publicăm tot ce învățăm, gratuit.

    **Public:** elevi de gimnaziu care nu au mai programat; elevi de liceu care caută proiecte; profesori și părinți care vor să înțeleagă ce facem.

    **Personalitate:** tehnic, accesibil, practic.

    **Anti-personalitate:** corporativ, copilăros, elitist.

    **Ton:**

    | Așa da | Așa nu |
    |--------|--------|
    | „Aprinde un LED în 10 minute” | „Descoperă fascinanta lume a electronicii” |
    | „Ce nu merge: verifică polaritatea LED-ului” | „Pot apărea unele dificultăți tehnice” |
    | „Vino joi la 15:00 în laboratorul 2” | „Te așteptăm cu drag la întâlnirea noastră săptămânală” |

    **Diferențiere:** publicăm codul și schemele complete, nu doar poze cu rezultatul.

!!! tip "De ce contează tabelul „așa da / așa nu”"
    Este partea din brand book pe care o vor citi efectiv oamenii care scriu textele. Un principiu abstract („ton accesibil”) nu ajută pe nimeni; două exemple concrete alăturate schimbă imediat modul de scriere.

---

## Pagina 02 — Logo

Preia tot din lecția 12 și organizează-l pentru consultare rapidă:

1. Grila de construcție, cu modulele vizibile.
2. Cele cinci variante, fiecare cu numele fișierului dedesubt.
3. Zona de protecție, desenată cu unitatea marcată.
4. Dimensiunile minime, cu exemple la mărimea reală.
5. Testele pe fundaluri (cele cinci din lecția 12).
6. Capitolul „ce nu se face”, cu minimum șase exemple.

---

## Pagina 03 — Foundations

### Culoare

Documentează vizual, nu doar ca stiluri invizibile:

| Ce arăți | Cum |
|----------|-----|
| Fiecare culoare | Pătrat 96 × 96, nume de stil, HEX, HSL |
| Perechile verificate | Tabel cu raportul de contrast pentru fiecare combinație text/fundal |
| Proporțiile 60-30-10 | O bară vizuală care arată distribuția |
| Culorile semantice | Succes, avertisment, eroare, cu exemplu de utilizare |

!!! warning "Documentează și ce e interzis"
    Adaugă explicit: „portocaliul nu se folosește ca fundal pentru blocuri mari de text” sau „verdele se folosește **doar** pentru confirmări, niciodată decorativ”.

    Fără aceste reguli, în șase luni cineva va face un afiș complet verde și va avea dreptate să spună că nu scria nicăieri că nu se poate.

### Tipografie

| Ce arăți | Cum |
|----------|-----|
| Fonturile alese | Alfabetul complet, cifre, diacritice românești (ă â î ș ț) |
| Scara tipografică | Cele 6 trepte, aplicate pe text real, cu specificațiile |
| Perechile de greutăți | Ce se combină cu ce |
| Regulile de aliniere | Când se centrează, când nu |

!!! warning "Verifică diacriticele"
    Multe fonturi gratuite au `ș` și `ț` desenate cu **sedilă** (ş, ţ) în loc de **virgulă dedesubt** (ș, ț). Este forma greșită pentru limba română.

    Verifică înainte să alegi fontul: scrie `Știință și țară` și privește cu atenție. Inter, Source Sans 3, Lato și IBM Plex Sans au formele corecte.

### Spațiere și grilă

- Scara de spațiere (4, 8, 16, 24, 32, 48, 64, 96), desenată vizual.
- Grilele pentru cele trei breakpoint-uri.
- Grila pentru print (A4 și A3).

---

## Pagina 04 — Components

Biblioteca din lecția 08, completată:

| Grup | Componente |
|------|-----------|
| **Primitive** | `button` (9 variante), `input` (6 stări), `badge` (4 tipuri), `avatar` (3 mărimi) |
| **Pictograme** | Setul de 8+ din lecția 07, ca instanțe |
| **Compuse** | `card/project`, `card/feature`, `nav/mobile`, `nav/desktop`, `footer` |
| **Șabloane sociale** | Cele 4 din lecția 13 |

Toate trebuie să folosească **exclusiv** stilurile din pagina 03.

---

## Pagina 05 — Aplicații

Aici se vede dacă identitatea funcționează cu adevărat. Șase materiale reale, construite doar din ce e definit mai sus.

| # | Aplicație | Format | Ce demonstrează |
|---|-----------|--------|-----------------|
| 1 | **Afiș de eveniment** | A3, 842 × 1191 pt | Tipografie la scară mare, ierarhie, print |
| 2 | **Postare + story** | 1080 × 1350 și 1080 × 1920 | Adaptare între formate |
| 3 | **Slide de prezentare** | 1920 × 1080, 3 slide-uri | Tipar de layout repetabil |
| 4 | **Card de membru** | 85 × 54 mm (format card bancar) | Logo la dimensiune mică, print |
| 5 | **Tricou** | Mockup, print 25 × 30 cm | Logo monocrom, aplicare pe textil |
| 6 | **Antet de site** | 1440 × 800 px | Componente, grilă, responsive |

!!! tip "Cardul de membru e cel mai bun test"
    La 85 × 54 mm, logo-ul ajunge la ~20 mm lățime și textul la 7–8 pt. Dacă identitatea ta funcționează pe un card de membru, funcționează aproape oriunde.

    Dacă la această dimensiune logo-ul devine o pată, întoarce-te la lecția 12 și fă varianta compactă.

### Mockup-uri

Pentru tricou și card, prezintă-le în context, nu ca fișiere plate. Surse gratuite de mockup-uri: [Mockey](https://mockey.ai/), sau construiește-ți singur în Figma un mockup simplu (o fotografie de tricou + logo-ul cu `Multiply` blend mode și o ușoară distorsiune).

---

## Pagina 06 — Brand book

Documentul pe care îl dai altora. **Maximum 20 de pagini**, format A4 landscape (1123 × 794 pt) sau 16:9 pentru citit pe ecran.

### Structura

| Pagini | Conținut |
|--------|----------|
| 1 | Copertă: logo mare, numele organizației, anul |
| 2 | Cuprins |
| 3–4 | Platforma de brand (misiune, public, ton) |
| 5–8 | Logo: variante, zonă de protecție, dimensiuni minime, ce nu se face |
| 9–11 | Culoare: paleta, proporții, contrast |
| 12–13 | Tipografie: fonturi, scară, exemple |
| 14 | Spațiere și grilă |
| 15–18 | Aplicații: câte o pagină pentru fiecare material |
| 19 | Unde se găsesc fișierele (link către folderul cu assets) |
| 20 | Contact: cine răspunde la întrebări |

!!! note "Un brand book nu se citește, se consultă"
    Nimeni nu va citi 20 de pagini din scoarță în scoarță. Oamenii vor deschide documentul cu o întrebare precisă („ce cod are portocaliul?”) și vor căuta răspunsul.

    Consecințe de design:
    - **Cuprins cu numere de pagină**, obligatoriu.
    - Titluri mari și clare pe fiecare pagină.
    - Informația critică (coduri de culoare, nume de fonturi) în **tabele**, nu în proză.
    - Exemple vizuale lângă fiecare regulă.

---

## Exerciții

### Exercițiu 1 — Platforma de brand
Completează cele șase blocuri ale platformei de brand pentru cercul tău. Tabelul „așa da / așa nu” trebuie să aibă minimum trei perechi, luate din texte reale ale organizației tale.

??? success "Soluție"
    Indicatorii unei platforme bune:

    - **Misiunea** e o propoziție care conține un **verb concret**. „Construim și publicăm” e bine; „promovăm pasiunea pentru tehnologie” nu spune nimic.
    - **Publicul** are grupuri numite, nu „toată lumea”. Dacă ai scris „toți elevii”, subîmparte: cine nu a programat niciodată vs. cine caută proiecte avansate — au nevoie de mesaje diferite.
    - **Anti-personalitatea** e la fel de importantă ca personalitatea. Fără ea, orice direcție pare acceptabilă.
    - **Perechile de ton** trebuie luate din texte **reale** pe care le-ai scris. Dacă le inventezi, nu te vor ajuta când vei scrie următorul afiș.

    **Test:** dă platforma unui coleg și cere-i să scrie titlul unei postări. Dacă tonul rezultat seamănă cu al tău, platforma funcționează.

### Exercițiu 2 — Auditul de contrast
Construiește tabelul complet de contrast pentru paleta ta: fiecare culoare de text pe fiecare culoare de fundal. Marchează cu verde ce trece AA, cu galben ce trece doar pentru text mare, cu roșu ce cade.

??? success "Soluție"
    Exemplu de tabel, pentru o paletă de 5 culori:

    | Text pe fundal → | `#0F172A` | `#1E293B` | `#F8FAFC` | `#F97316` |
    |---------------|-----------|-----------|-----------|-----------|
    | `#F8FAFC` | 15.8 ✅ | 13.1 ✅ | 1.0 ❌ | 2.7 ❌ |
    | `#CBD5E1` | 11.2 ✅ | 9.3 ✅ | 1.4 ❌ | 1.9 ❌ |
    | `#94A3B8` | 6.4 ✅ | 5.3 ✅ | 2.5 ❌ | 1.1 ❌ |
    | `#64748B` | 3.8 ⚠️ | 3.1 ⚠️ | 4.2 ⚠️ | 1.5 ❌ |
    | `#0F172A` | 1.0 ❌ | 1.2 ❌ | 15.8 ✅ | 5.9 ✅ |
    | `#F97316` | 5.9 ✅ | 4.9 ✅ | 2.7 ❌ | 1.0 ❌ |

    **Ce înveți din tabel:**
    - `#64748B` nu trece AA nicăieri pentru text normal. Îl folosești **doar** pentru text ≥ 24 px, sau pentru elemente decorative. Documentează asta.
    - Pe fundal portocaliu, singura culoare de text sigură este `#0F172A`. Deci **butoanele portocalii au text închis**, nu alb. Aceasta e o decizie de design luată de tabel, nu de gust.
    - `#F8FAFC` pe `#F97316` dă 2.7 — combinația pe care majoritatea o folosește instinctiv și care cade testul.

    **Adaugă tabelul în brand book.** E una dintre cele mai consultate pagini.

### Exercițiu 3 — Testul de coerență
Pune cele șase aplicații una lângă alta, la scară mică, și aplică testul de blur. Apoi arată-le cuiva care nu a lucrat la proiect.

??? success "Soluție"
    **Testul de blur pe set:** la blur 15, toate cele șase trebuie să prezinte **aceleași tipare** — aceeași distribuție de pete închise/deschise, aceeași poziție a accentului de culoare, aceeași densitate.

    Dacă una arată complet diferit, verifică:
    - Folosește alte proporții de culoare? (60-30-10 încălcat)
    - Are alte margini? (grila ignorată)
    - Are alt raport de ierarhie? (scara tipografică ignorată)

    **Testul cu o persoană nouă**, trei întrebări:
    1. „Sunt acestea ale aceleiași organizații?” — răspunsul trebuie să fie da, instantaneu.
    2. „Care e culoarea lor?” — trebuie să numească una singură.
    3. „Cum ai descrie tonul?” — răspunsul trebuie să conțină cel puțin unul dintre cele trei adjective din platforma ta.

    Dacă la întrebarea 3 primești un adjectiv din lista **anti-personalitate**, identitatea comunică altceva decât ai intenționat. Cel mai des vinovat: fontul sau raza colțurilor.

---

## Mini-proiect: identitatea completă

Parcurge toate cele șase pagini și livrează setul complet.

??? success "Livrabilele și criteriile"
    **Livrabilele:**

    ```
    identitate-vizuala/
    ├── brand-book.pdf                  (20 pagini)
    ├── logo/
    │   ├── logo-primary.svg
    │   ├── logo-horizontal.svg
    │   ├── logo-mark.svg
    │   ├── logo-black.svg
    │   ├── logo-white.svg
    │   ├── logo-mark-32.png
    │   └── logo-mark-512.png
    ├── fonts/
    │   └── link-uri-google-fonts.txt
    ├── templates/
    │   ├── afis-a3.pdf
    │   ├── post-1080x1350.png
    │   ├── story-1080x1920.png
    │   └── slide-16x9.pdf
    └── README.txt                      (cum se folosesc fișierele)
    ```

    Plus **link-ul Figma** cu drept de view către fișierul cu cele șase pagini.

    **Criteriile de evaluare:**

    | # | Criteriu | Verificare |
    |---|----------|-----------|
    | 1 | Platforma de brand completă | Cele 6 blocuri, cu 3 perechi de ton |
    | 2 | Logo în 5 variante, vectorial | Deschide SVG-urile fără fontul original |
    | 3 | Paleta documentată cu tabel de contrast | Tabelul complet, colorat |
    | 4 | Fonturile au diacritice românești corecte | Scrie `Știință și țară` |
    | 5 | Componente care folosesc doar stiluri | Schimbă `brand/primary` — se actualizează tot? |
    | 6 | Șase aplicații reale | Toate prezente și construite din bibliotecă |
    | 7 | Cardul de membru e lizibil | Tipărește-l la 85 × 54 mm |
    | 8 | Brand book ≤ 20 pagini, cu cuprins | Numără paginile |
    | 9 | Capitolul „ce nu se face” ≥ 6 exemple | Numără |
    | 10 | Testul cu persoană nouă | Cele 3 întrebări din exercițiul 3 |

    **Testul final — cel care contează cu adevărat:**

    Dă **doar** `brand-book.pdf` și folderul de fișiere unui coleg care nu a participat la proiect. Cere-i să facă un afiș A3 pentru un eveniment real. Cronometrează și numără întrebările pe care ți le pune.

    | Rezultat | Interpretare |
    |----------|--------------|
    | 0 întrebări, afiș coerent | Identitate completă |
    | 1–2 întrebări | Aproape; adaugă răspunsurile în brand book |
    | 3+ întrebări | Ghidul are lacune structurale |
    | Afiș incoerent, fără întrebări | Mai rău decât întrebările: regulile există dar nu sunt găsibile. Reorganizează cuprinsul |

    **Ce faci după:** adaugă în brand book răspunsurile la fiecare întrebare primită. Un brand book bun crește prin întrebările la care a trebuit să răspundă autorul.

---

## Rezumat

- Un logo răspunde „cum ne recunoști”; o identitate răspunde **„cum arată orice material, făcut de oricine, peste doi ani”**.
- **Platforma de brand** (misiune, public, personalitate, anti-personalitate, ton, diferențiere) decide toate deciziile vizuale.
- Tabelul **„așa da / așa nu”** este partea cel mai des folosită din tot documentul.
- Documentează și **ce e interzis**, nu doar ce e permis.
- Verifică **diacriticele românești** (ș, ț cu virgulă, nu cu sedilă) înainte să alegi fontul.
- **Tabelul complet de contrast** ia decizii de design în locul gustului.
- **Șase aplicații reale** demonstrează că sistemul funcționează; cardul de membru e cel mai dur test.
- Brand book: **maximum 20 de pagini**, cu cuprins, tabele și exemple vizuale.
- Testul final: un coleg produce un material corect **fără să te întrebe nimic**.

---

**Pasul următor:** [→ Lecția 16: Prototip interactiv de landing page](16-proiect-prototip-figma.md)
