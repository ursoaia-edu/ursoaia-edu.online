---
lesson: 4
tags: [tipografie, fonturi, ierarhie, lizibilitate, google fonts]
summary: Anatomia literei, familii de fonturi, cum alegi o pereche care funcționează, corp, interlinie și lungimea rândului.
---

# Lecția 04 · Tipografia

!!! tip "Ce vei învăța"
    - **Anatomia literei** și de ce contează înălțimea x
    - Cele patru **familii de fonturi** și când se folosește fiecare
    - Diferența dintre **greutate**, **stil** și **corp**
    - **Interlinia**, **spațierea literelor** și **lungimea rândului**
    - Cum alegi o **pereche de fonturi** care funcționează
    - Cum instalezi Google Fonts și cum salvezi stiluri de text în Figma

---

## De ce tipografia e 90% din design

Deschide orice afiș, orice site, orice ambalaj. Elimină mental imaginile. Ce rămâne? Text. Majoritatea deciziilor tale de design vor fi, de fapt, decizii despre text: cât de mare, ce font, cât de departe de altceva.

Un design cu tipografie bună și fără imagini arată profesionist. Un design cu imagini excelente și tipografie proastă arată amatoricesc. Ordinea aceasta nu se inversează.

---

## Anatomia literei

```
      ┌─────────────────────────  linia ascendentelor
      │   h        ┌──           
  ┌───┼───────────┼──────────────  linia înălțimii x
  │   │  x  o  n  │
  └───┴───────────┴──────────────  linia de bază (baseline)
          │
          └──────────────────────  linia descendentelor (g, p, y)
```

| Termen | Ce este | De ce contează |
|--------|---------|----------------|
| **Linia de bază** | Linia pe care „stau” literele | Aliniază texte de mărimi diferite |
| **Înălțimea x** | Înălțimea literei `x` mici | Determină lizibilitatea reală |
| **Ascendente** | Partea care urcă peste x (`b`, `d`, `h`, `l`) | Ajută la recunoașterea cuvintelor |
| **Descendente** | Partea care coboară sub linia de bază (`g`, `p`, `y`) | Cere spațiu între rânduri |
| **Contra-formă** | Golul din interiorul literelor (`o`, `e`, `a`) | Dacă e mic, textul „se închide” la mărimi mici |

!!! note "Înălțimea x e mai importantă decât corpul"
    Două fonturi setate ambele la 16 px pot arăta complet diferit ca mărime. Un font cu înălțime x mare (Inter, Roboto) pare mult mai mare și se citește mai bine la dimensiuni mici decât unul cu înălțime x mică (Playfair Display, Garamond).

    Consecință practică: când schimbi fontul, **trebuie** să reverifici mărimile. Nu se transferă automat.

---

## Familiile de fonturi

### Serif

Au „picioare” — mici terminații la capetele liniilor. Georgia, Times New Roman, Playfair Display, Merriweather.

- **Asociere:** tradiție, autoritate, editorial, seriozitate.
- **Bun la:** text lung tipărit, titluri elegante, cărți, diplome.
- **Slab la:** ecrane mici, mărimi sub 14 px, interfețe.

### Sans-serif

Fără picioare. Inter, Helvetica, Roboto, Open Sans, Montserrat.

- **Asociere:** modern, curat, neutru, tehnologic.
- **Bun la:** ecrane, interfețe, titluri, text scurt, orice.
- **Slab la:** nimic major — de asta e alegerea implicită.

### Monospace

Toate literele au aceeași lățime. JetBrains Mono, Fira Code, Courier.

- **Asociere:** cod, date, tehnic, mașină.
- **Bun la:** cod, tabele cu numere, etichete tehnice, ceasuri.
- **Slab la:** text lung — se citește greu.

### Display / decorative

Fonturi cu personalitate puternică, desenate pentru dimensiuni mari. Lobster, Bebas Neue, Bangers.

- **Asociere:** depinde complet de font.
- **Bun la:** **doar** titluri foarte mari, logo-uri, afișe.
- **Slab la:** absolut orice altceva.

!!! warning "Regula fontului decorativ"
    Un font decorativ se folosește **o singură dată pe pagină**, la mărime mare. Dacă îl pui și pe titluri, și pe subtitluri, și pe butoane, designul devine obositor în 3 secunde.

---

## Greutate, stil, corp

### Greutatea (weight)

| Nume | Valoare numerică | Unde |
|------|------------------|------|
| Thin | 100 | Aproape niciodată |
| Light | 300 | Titluri foarte mari |
| Regular | 400 | Text curent |
| Medium | 500 | Etichete, subtitluri |
| Semi Bold | 600 | Titluri |
| Bold | 700 | Accente puternice, titluri mari |
| Black | 900 | Afișe, numere mari |

!!! tip "Folosește maximum 3 greutăți"
    Regular pentru text, Semi Bold pentru titluri, Medium pentru etichete. Atât. Un design cu 6 greutăți din același font arată la fel de dezordonat ca unul cu 6 fonturi diferite.

### Stilul

**Italic** se folosește pentru: titluri de cărți și lucrări, cuvinte în altă limbă, accent subtil. **Nu** se folosește pentru paragrafe întregi — obosește.

!!! warning "Italic fals"
    Unele programe „înclină” fontul artificial dacă nu are variantă italic reală. Rezultatul arată strâmb. În Figma, verifică dacă `Italic` apare în lista de stiluri a fontului; dacă nu apare, fontul nu are italic și nu trebuie forțat.

### Corpul (font size)

O scară tipografică este un set de mărimi cu un raport constant între ele. Nu alegi mărimile la întâmplare.

**Scara 1.25 (Major Third)** — potrivită pentru interfețe:

| Rol | Mărime |
|-----|--------|
| Text mic | 13 px |
| Text curent | 16 px |
| Subtitlu | 20 px |
| Titlu secțiune | 25 px |
| Titlu pagină | 31 px |
| Titlu mare | 39 px |

**Scara 1.5** — potrivită pentru afișe, unde vrei contrast dramatic:

| Rol | Mărime |
|-----|--------|
| Detalii | 16 px |
| Informație | 24 px |
| Subtitlu | 36 px |
| Titlu | 54 px |
| Titlu dominant | 81 px |

!!! note "De ce o scară și nu mărimi la întâmplare"
    Mărimile 14, 15, 17, 18 arată ca o greșeală — diferențele sunt prea mici ca să pară intenționate, dar prea mari ca să fie identice. Ochiul citește asta drept „neglijent”. O scară garantează că fiecare salt e vizibil și deliberat.

---

## Spațiere

### Interlinia (line height)

Distanța dintre liniile de bază a două rânduri consecutive.

| Tip de text | Interlinie |
|-------------|------------|
| Titluri mari (peste 32 px) | 1.1 – 1.2 |
| Subtitluri | 1.3 |
| Text curent | 1.5 – 1.6 |
| Text mic, dens | 1.4 |

!!! warning "Interlinia implicită e aproape întotdeauna greșită"
    Figma pune `Auto`, care înseamnă aproximativ 1.2. Pentru un titlu e bine. Pentru un paragraf e prea strâns — rândurile se lipesc și ochiul sare pe rândul greșit când revine la capătul liniei.

    **Regula inversă:** cu cât textul e mai mare, cu atât interlinia e mai mică. Un titlu de 60 px la interlinie 1.5 are găuri uriașe între rânduri.

### Spațierea literelor (letter spacing / tracking)

| Situație | Valoare |
|----------|---------|
| Text curent | 0 (lasă fontul în pace) |
| Titluri foarte mari | −1% până la −3% (le strânge, arată mai compact) |
| MAJUSCULE | +5% până la +10% (obligatoriu) |
| Etichete mici cu majuscule | +10% până la +15% |

!!! tip "Majusculele au nevoie de aer"
    `CERCUL DE INFORMATICĂ` scris fără spațiere suplimentară arată înghesuit, pentru că literele majuscule au toate aceeași înălțime și nu lasă goluri naturale. Adaugă întotdeauna 5–10% tracking la text integral cu majuscule.

### Lungimea rândului (measure)

**45–75 de caractere pe rând**, ideal ~66. Include spațiile.

- **Prea scurt** (sub 45): ochiul sare prea des la rândul următor, ritmul se rupe.
- **Prea lung** (peste 75): la capăt de rând, ochiul nu mai găsește începutul rândului următor.

Practic, într-un afiș A4, o coloană de text nu ar trebui să depășească ~12 cm lățime la corp 12 pt.

---

## Cum alegi o pereche de fonturi

### Regula: contrast, nu conflict

Două fonturi trebuie să fie **clar diferite**. Două sans-serif asemănătoare (Helvetica + Arial) arată ca o greșeală, nu ca o alegere.

| Combinație | Funcționează? | De ce |
|------------|---------------|-------|
| Serif titlu + sans-serif text | Da | Contrast clar de familie |
| Sans-serif titlu + serif text | Da | Clasic editorial inversat |
| Același font, greutăți diferite | Da | Cea mai sigură opțiune |
| Două sans-serif diferite | Riscant | Doar dacă sunt foarte diferite ca personalitate |
| Două serif diferite | Nu | Aproape imposibil de făcut să arate intenționat |
| Două fonturi decorative | Nu | Niciodată |

!!! tip "Cea mai sigură pereche: un singur font"
    Ia **Inter** și folosește Bold 40 pentru titlu, Medium 18 pentru subtitlu, Regular 16 pentru text. Ai contrast clar și zero risc. Multe branduri mari fac exact asta.

### Perechi care funcționează garantat

| Titlu | Text | Ton |
|-------|------|-----|
| Playfair Display | Source Sans 3 | Elegant, editorial |
| Montserrat | Merriweather | Modern + lizibil |
| Bebas Neue | Inter | Afiș, impact |
| Inter Bold | Inter Regular | Tehnic, curat, sigur |
| Space Grotesk | IBM Plex Sans | Tech, contemporan |
| Lora | Lato | Cald, prietenos |

---

## Google Fonts în Figma

1. Figma are deja **toate fonturile Google** disponibile în versiunea web. Le cauți direct în lista de fonturi.
2. Pentru aplicația desktop, ai nevoie de **Figma Font Helper** (se instalează o dată) sau instalezi fontul în sistem.
3. Pentru a folosi fontul pe un site: [fonts.google.com](https://fonts.google.com/) → alegi stilurile → copiezi codul `<link>` în `<head>`.

!!! warning "Nu încărca 8 stiluri de font pe un site"
    Fiecare greutate și fiecare stil italic este un fișier separat de descărcat. Un site care încarcă Inter în 9 greutăți transferă peste 1 MB doar pentru text. Alege **3 greutăți** și atât.

### Stiluri de text în Figma

Ca la culori, salvezi combinațiile ca stiluri reutilizabile:

1. Selectezi un text formatat corect.
2. În panoul din dreapta, la secțiunea **Text**, apeși pe cele patru puncte → **+**.
3. Îi dai un nume **după rol**: `heading/h1`, `heading/h2`, `body/base`, `body/small`, `label/caps`.

Când schimbi stilul, **tot textul care îl folosește se actualizează**. Într-un afiș cu 20 de texte, asta e diferența dintre 2 secunde și 10 minute.

---

## Erori frecvente

| Eroare | De ce e problemă | Corecția |
|--------|------------------|----------|
| Text centrat pe mai multe rânduri | Marginea stângă zimțată; ochiul caută începutul fiecărui rând | Aliniere la stânga pentru orice peste 3 rânduri |
| Justified cu coloană îngustă | „Râuri” de spațiu alb vertical prin text | Aliniere la stânga |
| Text pe fotografie fără tratament | Contrast imprevizibil, ilizibil în zonele aglomerate | Overlay întunecat, blur pe zona textului, sau bandă de culoare |
| Tot textul cu majuscule | Cuvintele își pierd forma, se citesc literă cu literă | Majuscule doar la etichete scurte |
| 5 fonturi pe o pagină | Nu există ierarhie, doar zgomot | Maximum 2 fonturi |
| Corp sub 12 px la print | Ilizibil pentru mulți cititori | Minimum 9 pt la print, 14 px pe web |

!!! note "Orfani și văduve"
    Un **orfan** este un singur cuvânt rămas pe ultimul rând al unui paragraf. Arată neîngrijit. Se repară forțând o întrerupere de rând mai devreme sau ajustând ușor lățimea coloanei. La un afiș, cu 3 rânduri de text, contează.

---

## Exerciții

### Exercițiu 1 — Aceeași frază, patru familii
Scrie fraza „Cercul de informatică primește membri noi” de patru ori, într-un frame de 800 × 600 px, la 32 px, folosind un serif, un sans-serif, un monospace și un display. Notează sub fiecare ce ton transmite.

??? success "Soluție"
    - **Playfair Display** — solemn, ca o invitație oficială. Potrivit dacă evenimentul e formal.
    - **Inter** — neutru, clar, modern. Merge în orice context; e alegerea implicită corectă.
    - **JetBrains Mono** — tehnic, „de programator”. Aici chiar are sens, fiind vorba de informatică — dar devine obositor peste 2 rânduri.
    - **Bebas Neue** — strigă. Bun pentru un afiș văzut de departe, prost pentru orice text de citit.

    Observație importantă: toate patru sunt la **același corp (32 px)**, dar arată de mărimi diferite. Bebas Neue pare mai mare, Playfair mai mic. Aceasta e înălțimea x în acțiune.

### Exercițiu 2 — Repară un paragraf
Într-un frame de 600 × 400 px, pune un paragraf de ~60 de cuvinte cu setările implicite Figma (16 px, interlinie Auto, lățime 580 px, centrat). Apoi corectează-l.

??? success "Soluție"
    Problemele din varianta inițială:
    - Lățime 580 px la 16 px ≈ **95 de caractere pe rând** — prea lung.
    - Interlinie Auto ≈ 1.2 — prea strâns pentru un paragraf.
    - Centrat — marginea stângă zimțată face citirea grea.

    Corecția:
    - Lățime **440 px** → ~66 de caractere pe rând.
    - Interlinie **1.6** (adică 25.6 px la corp 16).
    - Aliniere **la stânga**.
    - Culoare text `#374151` în loc de negru pur.

    Citește ambele variante cu voce tare. A doua se citește vizibil mai fluent, deși ai schimbat doar patru setări și niciun cuvânt.

### Exercițiu 3 — Scară tipografică
Construiește o scară cu raportul 1.25 pornind de la 16 px, pe 6 trepte, și aplic-o pe o pagină cu: titlu, subtitlu, două titluri de secțiune, text curent și o notă de subsol.

??? success "Soluție"
    Scara (fiecare valoare × 1.25, rotunjită):

    | Treaptă | Mărime | Rol | Greutate | Interlinie |
    |---------|--------|-----|----------|------------|
    | −1 | 13 px | Notă de subsol | Regular | 1.4 |
    | 0 | 16 px | Text curent | Regular | 1.6 |
    | 1 | 20 px | Subtitlu | Medium | 1.4 |
    | 2 | 25 px | Titlu secțiune | Semi Bold | 1.3 |
    | 3 | 31 px | Titlu pagină | Semi Bold | 1.2 |
    | 4 | 39 px | Titlu dominant | Bold | 1.1 |

    Salvează fiecare treaptă ca stil de text în Figma: `body/small`, `body/base`, `heading/h4` … `heading/h1`.

    Verificare: dacă schimbi acum fontul din Inter în Source Sans 3 modificând doar stilurile, întreaga pagină se actualizează coerent. Dacă a trebuit să corectezi manual vreun text, înseamnă că acel text nu folosea un stil.

---

## Mini-proiect: afiș tipografic

Construiește un afiș A3 pentru un eveniment școlar folosind **exclusiv text** — fără imagini, fără pictograme, maximum o formă geometrică simplă. Un singur font, maximum 3 greutăți.

??? success "Soluție"
    Exemplu — „Noaptea Cercetătorilor” la cercul de informatică:

    **Setări:** frame A3 (842 × 1191 pt), fundal `#0F172A`, font Inter, margini 60 pt.

    | Element | Text | Mărime | Greutate | Culoare | Tracking |
    |---------|------|--------|----------|---------|----------|
    | Etichetă | `CERCUL DE INFORMATICĂ` | 18 | Medium | `#F97316` | +12% |
    | Titlu | `NOAPTEA CERCETĂTORILOR` | 96 | Bold | `#F8FAFC` | −2% |
    | Data | `27 SEPTEMBRIE` | 54 | Semi Bold | `#F97316` | 0 |
    | Ora și locul | `18:00 · Laboratorul 2` | 28 | Regular | `#94A3B8` | 0 |
    | Descriere | 2 rânduri, max 60 caractere | 20 | Regular | `#CBD5E1` | 0 |
    | Detalii | `Intrarea liberă · ursoaia-edu.online` | 16 | Medium | `#64748B` | 0 |

    Plus **o singură formă:** o bară de 8 × 200 pt în portocaliu, sub titlu, ca separator.

    **De ce funcționează:**
    - Un singur font, trei greutăți → coerență totală.
    - Saltul de la 96 la 54 la 28 e mare și deliberat → ierarhie citibilă din mers.
    - Portocaliul apare de exact trei ori (etichetă, dată, bară) → accentul rămâne accent.
    - Titlul cu tracking negativ (−2%) arată compact și intenționat la 96 pt.
    - Eticheta cu majuscule are +12% tracking → respiră.

    **Greșeli de evitat:**
    - Titlul centrat pe 3 rânduri → marginea stângă zimțată.
    - Data la aceeași mărime cu titlul → cititorul nu știe ce e mai important.
    - Mai mult de 6 blocuri de text → nimeni nu citește un afiș ca pe o carte.

---

## Rezumat

- **Înălțimea x** determină lizibilitatea reală, nu corpul declarat.
- Patru familii: **serif** (tradiție), **sans-serif** (implicit), **monospace** (tehnic), **display** (o singură dată, mare).
- Maximum **2 fonturi** și **3 greutăți** pe proiect.
- Mărimile vin dintr-o **scară** (1.25 pentru interfețe, 1.5 pentru afișe), nu la întâmplare.
- Interlinie: **1.5–1.6** pentru text curent, **1.1–1.2** pentru titluri mari.
- Majusculele cer **+5% până la +15% tracking**.
- Lungime de rând: **45–75 de caractere**, ideal 66.
- Aliniere **la stânga** pentru orice paragraf de peste 3 rânduri.
- Salvează stilurile de text în Figma, numite **după rol**, nu după aspect.

---

**Pasul următor:** [→ Lecția 05: Compoziție și grilă](05-compozitie-si-grila.md)
