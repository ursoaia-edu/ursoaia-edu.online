---
lesson: 6
tags: [ierarhie, contrast, atenție, scanare, design]
summary: Cum decizi ce vede cititorul primul — cele șase pârghii de contrast, traseul privirii și cum se repară o ierarhie greșită.
---

# Lecția 06 · Ierarhie vizuală

!!! tip "Ce vei învăța"
    - Ce este **ierarhia vizuală** și de ce e testul final al oricărui design
    - Cele **șase pârghii** prin care creezi contrast
    - **Traseul privirii**: Z, F și punctul de intrare
    - Regula celor **trei niveluri**
    - Cum diagnostichezi și repari o ierarhie greșită
    - Cum se aplică toate într-o interfață, nu doar într-un afiș

---

## Ce este ierarhia vizuală

**Ierarhia vizuală este ordinea în care cititorul observă lucrurile.** Ea există întotdeauna — întrebarea e doar dacă ai controlat-o tu sau s-a întâmplat de la sine.

Testul e simplu și crud: arată designul cuiva timp de 3 secunde, apoi întreabă ce a văzut primul. Dacă răspunsul nu e informația ta cea mai importantă, ierarhia e greșită. Nu „discutabilă” — greșită.

!!! note "Ierarhia nu e opțională"
    Un design fără ierarhie nu e „neutru”. Dacă toate elementele au aceeași greutate vizuală, cititorul trebuie să le proceseze pe toate ca să decidă ce contează. Majoritatea nu fac acest efort; pur și simplu pleacă.

---

## Cele șase pârghii de contrast

Ai exact șase moduri de a face un element mai important decât altul. Le poți combina, dar nu ai nevoie de toate.

### 1. Mărimea

Cea mai directă. Un element de două ori mai mare e citit primul.

**Regula:** pentru ca diferența să fie citită ca **intenționată**, saltul trebuie să fie de minimum **1.5×**. 18 px lângă 20 px arată ca o greșeală; 18 px lângă 32 px arată ca o decizie.

### 2. Greutatea

Bold vs. Regular, în cadrul aceluiași font. Discretă, foarte utilă în text curent, unde nu poți schimba mărimea.

**Limita:** dacă îngroși jumătate din text, nimic nu mai iese în evidență. Bold-ul funcționează doar cât timp e rar.

### 3. Culoarea

Un element colorat pe un fundal neutru sare imediat. Funcționează chiar și la mărime mică — de asta bulina roșie de notificări are 8 px și tot o vezi.

**Limita:** dacă ai patru culori de accent, nu mai ai niciun accent.

### 4. Spațiul

Un element izolat, cu gol mare în jur, pare important — chiar dacă e mic și gri. Este pârghia cea mai subtilă și cea mai subutilizată de începători.

### 5. Poziția

Ce e sus e citit înaintea a ce e jos. Ce e la stânga înaintea a ce e la dreapta (în culturile care citesc de la stânga la dreapta). Centrul optic al unei pagini se află puțin deasupra centrului geometric.

### 6. Forma și stilul

Un element care arată diferit de restul (rotunjit între dreptunghiuri, plin între contururi, o pictogramă între texte) atrage atenția prin simplu contrast de formă.

!!! warning "Nu folosi toate cele șase pe același element"
    Un buton care e simultan mai mare, bold, colorat, izolat, sus și rotunjit devine strident. **Două pârghii sunt de obicei suficiente.** Trei e maximul rezonabil.

    Exemplu bun: butonul principal = culoare + mărime. Restul butoanelor: doar contur.

---

## Regula celor trei niveluri

Orice compoziție ar trebui să aibă **exact trei niveluri** de importanță:

| Nivel | Rol | Cât ocupă | Exemple |
|-------|-----|-----------|---------|
| **Primar** | Ce trebuie reținut, chiar dacă cititorul pleacă imediat | Un singur element | Titlul evenimentului, numărul principal |
| **Secundar** | Ce completează mesajul | 2–4 elemente | Data, locul, subtitlul |
| **Terțiar** | Ce se citește doar dacă cineva e deja interesat | Restul | Detalii, note, contact, sursă |

!!! note "Un singur element primar"
    Aceasta e partea grea. Dacă titlul și data au amândouă 80 px, nu ai un nivel primar — ai doi și se anulează reciproc.

    Întreabă-te: **dacă cititorul reține un singur lucru, care e acela?** Acela primește nivelul primar. Totul altceva coboară.

---

## Traseul privirii

### Punctul de intrare

Ochiul intră în pagină pe elementul cu cel mai mare contrast, indiferent unde se află. De acolo pornește traseul.

Consecință: **poți controla unde începe lectura**, indiferent de ordinea în care ai așezat lucrurile.

### Traseul în Z

Pentru pagini cu puțin conținut (afișe, landing page-uri simple), ochiul parcurge:

```
①─────────────────②
                 ╱
               ╱
             ╱
           ╱
③─────────────────④
```

Colțul stânga-sus, apoi dreapta-sus, diagonala spre stânga-jos, apoi dreapta-jos. Pui logo-ul în ①, titlul în ② și acțiunea („înscrie-te”) în ④.

### Traseul în F

Pentru pagini cu mult text (articole, site-uri de conținut), ochiul scanează:

```
①━━━━━━━━━━━━━━━━━━
│
②━━━━━━━━━━━
│
③━━━━━
│
④
```

Rândul de sus complet, apoi tot mai puțin la fiecare coborâre. Consecință practică: **primele 2–3 cuvinte din fiecare titlu contează cel mai mult**. „Cum să configurezi ESP32” e scanabil; „Un ghid despre cum să configurezi ESP32” nu.

!!! tip "Care traseu se aplică?"
    Numără blocurile de conținut. **Sub 5** → Z. **Peste 5** → F. Nu încerca să forțezi un Z pe o pagină cu 12 secțiuni; nu funcționează.

---

## Cum diagnostichezi o ierarhie greșită

Patru teste, în ordinea rapidității.

### Testul 1 — Blur

Aplică blur puternic. Cea mai întunecată / mai mare pată trebuie să fie elementul primar. Dacă nu e, ai găsit problema.

### Testul 2 — Mijirea ochilor

Mijește ochii până vezi doar forme. Același principiu, fără unelte.

### Testul 3 — Cele 3 secunde

Arată designul unui coleg exact 3 secunde. Întreabă-l ce a reținut. Repetă cu 3 persoane; dacă răspunsurile diferă, ierarhia e ambiguă.

### Testul 4 — Lista inversă

Notează ce observi, în ordinea în care observi. Compară cu lista ta de priorități din brief. Diferențele sunt exact lucrurile de reparat.

---

## Erori frecvente și cum se repară

| Simptom | Cauză | Reparație |
|---------|-------|-----------|
| „Totul pare la fel de important” | Contrast insuficient între niveluri | Mărește saltul: primar 2–3× față de terțiar |
| „Nu știu unde să mă uit întâi” | Două sau mai multe elemente primare | Alege unul; coboară celelalte cu o treaptă |
| „E obositor” | Prea multe pârghii de contrast simultan | Păstrează 2 pârghii, elimină restul |
| „Pare gol / plictisitor” | Un singur nivel, fără accent | Adaugă contrast de mărime sau culoare pe elementul primar |
| „Imaginea fură atenția” | Fotografia are contrast mai mare decât textul | Overlay întunecat peste imagine, sau text pe zonă plată |
| „Butonul nu se vede” | Butonul are aceeași culoare cu restul | Un singur buton colorat, restul doar contur |

!!! warning "Capcana: „important” ≠ „mare”"
    Nu tot ce e important trebuie să fie mare. Un buton de „Cumpără” de 300 px arată disperat. Un buton de 48 px, singurul colorat de pe pagină, e imposibil de ratat și arată încrezător.

    Izolarea și culoarea bat mărimea aproape întotdeauna.

---

## Ierarhia într-o interfață

Într-un afiș, ierarhia e statică. Într-o interfață, ea trebuie să răspundă la o întrebare suplimentară: **ce poate face utilizatorul aici?**

### Ierarhia acțiunilor

| Tip | Aspect | Câte pe ecran |
|-----|--------|---------------|
| **Primară** | Fundal plin, culoarea de brand | **Exact una** |
| **Secundară** | Doar contur, sau fundal neutru | 1–2 |
| **Terțiară** | Doar text, ca un link | Oricâte |
| **Distructivă** | Roșu, de obicei doar contur | Rar, niciodată lângă cea primară |

!!! note "De ce o singură acțiune primară"
    Dacă pe un ecran sunt două butoane portocalii pline, utilizatorul trebuie să citească ambele ca să decidă. Cu un buton plin și unul cu contur, decizia implicită e evidentă și rapidă — iar cel care vrea altceva tot găsește a doua opțiune.

### Ierarhia informației

- **Titlul ecranului** spune unde ești.
- **Conținutul** e ce ai venit să vezi — el primește cel mai mult spațiu.
- **Navigația** e mereu accesibilă, dar nu domină.
- **Metadatele** (date, autori, etichete) sunt terțiare: mici, gri.

!!! tip "Testul „de ce e asta aici”"
    Pentru fiecare element de pe ecran, întreabă: **ce se întâmplă dacă îl scot?** Dacă răspunsul e „nimic”, scoate-l. Cea mai bună îmbunătățire a ierarhiei e adesea o ștergere.

---

## Exerciții

### Exercițiu 1 — Trei niveluri dintr-o listă plată
Ia acest conținut și construiește-l într-un frame de 800 × 1000 px cu trei niveluri clare de ierarhie:

```
Târgul de proiecte
Sâmbătă, 12 aprilie
Sala de sport, etaj 1
10:00 – 14:00
Intrarea liberă
Organizat de cercul de informatică
Detalii: ursoaia-edu.online
```

??? success "Soluție"
    | Nivel | Text | Mărime | Greutate | Culoare |
    |-------|------|--------|----------|---------|
    | Primar | `Târgul de proiecte` | 72 | Bold | `#F8FAFC` |
    | Secundar | `Sâmbătă, 12 aprilie` | 32 | Semi Bold | `#F97316` |
    | Secundar | `10:00 – 14:00 · Sala de sport, etaj 1` | 24 | Regular | `#CBD5E1` |
    | Terțiar | `Intrarea liberă` | 16 | Medium | `#94A3B8` |
    | Terțiar | `Organizat de cercul de informatică` | 16 | Regular | `#64748B` |
    | Terțiar | `ursoaia-edu.online` | 16 | Regular | `#64748B` |

    Observă trei decizii:
    - Ora și locul au fost **unite pe un rând** — sunt aceeași informație („când și unde”), deci nu au nevoie de două niveluri.
    - Saltul 72 → 32 → 16 e de aproximativ 2× la fiecare treaptă. Vizibil, deliberat.
    - Data e singurul element colorat din nivelul secundar — e a doua informație ca importanță și culoarea o ridică fără să o facă mai mare decât titlul.

### Exercițiu 2 — Repară un ecran cu trei butoane primare
Desenează un ecran de aplicație cu trei butoane, toate cu fundal plin portocaliu: `Salvează`, `Anulează`, `Șterge`. Apoi corectează ierarhia acțiunilor.

??? success "Soluție"
    | Buton | Înainte | După | De ce |
    |-------|---------|------|-------|
    | `Salvează` | Fundal portocaliu | **Rămâne** fundal portocaliu | Acțiunea principală |
    | `Anulează` | Fundal portocaliu | Doar text, gri (`#94A3B8`) | Acțiune de ieșire, nu merită greutate |
    | `Șterge` | Fundal portocaliu | Contur roșu, text roșu | Distructivă: vizibilă, dar nu invitantă |

    În plus: mută `Șterge` **departe** de `Salvează`, de obicei în colțul opus sau într-un meniu. Un buton distructiv lipit de cel principal produce clicuri greșite.

    Rezultat: utilizatorul vede instant ce se așteaptă de la el, iar acțiunea periculoasă cere un pas conștient.

### Exercițiu 3 — Diagnostic pe un design existent
Ia un afiș sau o postare pe care ai făcut-o în lecțiile anterioare și aplică toate cele patru teste de diagnostic. Notează ce ai găsit și ce ai schimbat.

??? success "Soluție"
    Exemplu de raport de diagnostic:

    > **Testul blur:** cea mai întunecată pată e fotografia, nu titlul. → Problema 1.
    > **Mijirea ochilor:** data și ora se topesc într-o singură pată cu descrierea. → Problema 2.
    > **3 secunde (3 persoane):** doi au reținut titlul, unul a reținut data. → Ambiguitate ușoară, acceptabilă.
    > **Lista inversă:** am observat, în ordine: imaginea, titlul, data, logo-ul, descrierea. Brief-ul cerea: titlul, data, locul.

    **Reparațiile:**
    1. Overlay `rgba(15, 23, 42, 0.65)` peste fotografie → titlul devine punctul de intrare.
    2. Spațiu între blocul dată/oră și descriere mărit de la 12 la 40 px → se separă clar.
    3. Locul urcat lângă dată, la aceeași mărime → cele trei informații obligatorii stau împreună.

    După reparații, testul de 3 secunde dă același răspuns la toate cele trei persoane. Asta e ținta.

---

## Mini-proiect: același afiș, ierarhie inversată

Ia afișul tipografic din lecția 04 și fă o **a doua versiune** în care ierarhia e deliberat mutată: **data** devine elementul primar, iar titlul coboară la secundar. Nu schimba nimic altceva — aceeași paletă, același font, aceeași compoziție.

??? success "Soluție"
    | Element | Versiunea 1 | Versiunea 2 |
    |---------|-------------|-------------|
    | Titlu | 96 Bold, alb | 36 Semi Bold, `#CBD5E1` |
    | Data | 54 Semi Bold, portocaliu | 120 Bold, alb |
    | Restul | neschimbat | neschimbat |

    **Ce observi:**

    - Versiunea 1 spune „**vino la Noaptea Cercetătorilor**”. Funcționează pentru cineva care nu a auzit de eveniment.
    - Versiunea 2 spune „**27 septembrie se întâmplă ceva**”. Funcționează pentru cineva care deja știe despre eveniment și trebuie doar să rețină data — de exemplu un afiș pus cu o săptămână înainte, după o campanie de anunțuri.

    Ambele sunt corecte. **Corectitudinea ierarhiei depinde de brief**, nu de reguli abstracte. De asta lecția 00 începe cu brief-ul și nu cu instrumentele.

    **Extensie:** fă și o a treia versiune în care elementul primar e locul (`LABORATORUL 2`). Când ar fi utilă? Răspuns: dacă evenimentul e cunoscut și singura întrebare rămasă e „unde se ține anul ăsta”.

---

## Rezumat

- **Ierarhia vizuală** este ordinea în care cititorul observă lucrurile — și ea există oricum.
- Șase pârghii: **mărime, greutate, culoare, spațiu, poziție, formă**. Folosește 2, maximum 3.
- Saltul de mărime trebuie să fie de minimum **1.5×** ca să pară intenționat.
- **Trei niveluri**: un singur element primar, 2–4 secundare, restul terțiar.
- Traseul privirii: **Z** sub 5 blocuri, **F** peste 5.
- Într-o interfață: **exact un buton primar** pe ecran.
- Diagnostic: **blur, mijire, 3 secunde, listă inversă**.
- Cea mai bună îmbunătățire a ierarhiei este de multe ori o **ștergere**.
- Ce e „corect” depinde de **brief**, nu de reguli abstracte.

---

**Pasul următor:** [→ Lecția 07: Vectori și Pen Tool](07-vectori-pen-tool.md)
