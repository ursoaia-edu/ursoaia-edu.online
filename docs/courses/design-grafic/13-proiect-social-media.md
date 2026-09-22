---
lesson: 13
tags: [proiect, canva, social media, instagram, story, șabloane]
summary: Formate și zone de siguranță pentru rețele sociale, cum folosești Canva corect și cum construiești un set de șabloane refolosibile.
---

# Lecția 13 · Postare pentru rețele sociale

!!! tip "Ce vei construi"
    Un **set de șabloane** pentru comunicarea cercului de informatică:

    - Post pătrat, post vertical, story și copertă de eveniment
    - Un **kit de brand** în Canva, cu culorile și fonturile identității din lecția 12
    - **Zone de siguranță** respectate pe fiecare format
    - O **serie** de trei postări care se recunosc ca fiind din aceeași familie
    - Comparație practică: când folosești Canva și când Figma

---

## Formatele

Platformele își schimbă specificațiile des, dar raporturile rămân stabile. Reține **raporturile**, nu numerele.

| Format | Raport | Dimensiune recomandată | Unde |
|--------|--------|------------------------|------|
| **Pătrat** | 1:1 | 1080 × 1080 px | Feed Instagram, Facebook |
| **Vertical** | 4:5 | 1080 × 1350 px | Feed Instagram — ocupă cel mai mult ecran |
| **Story / Reels** | 9:16 | 1080 × 1920 px | Story Instagram, TikTok, YouTube Shorts |
| **Orizontal** | 16:9 | 1920 × 1080 px | YouTube, prezentări, ecrane de hol |
| **Copertă eveniment** | 1.91:1 | 1920 × 1005 px | Evenimente Facebook |

!!! tip "Verticalul 4:5 este formatul implicit pentru feed"
    La aceeași lățime de ecran, o postare 4:5 ocupă cu 25% mai multă înălțime decât una pătrată. Mai mult spațiu = mai mult timp de privire. Dacă ai de ales, fă 1080 × 1350.

### Zonele de siguranță

Interfața aplicației acoperă părți din imagine. Nu pune nimic important acolo.

**Story (1080 × 1920):**

```
┌──────────────────┐  ← 250 px: avatar, nume, ora
│ ~~~~~~~~~~~~~~~~ │
├──────────────────┤
│                  │
│   ZONĂ SIGURĂ    │  ← 1420 px utilizabili
│   1080 × 1420    │
│                  │
├──────────────────┤
│ ~~~~~~~~~~~~~~~~ │  ← 250 px: bara de răspuns, butoane
└──────────────────┘
```

**Post vertical (1080 × 1350):** în grilă de profil, apare **tăiat la pătrat**, centrat. Deci elementele esențiale trebuie să încapă în zona centrală de 1080 × 1080.

!!! warning "Testul grilei de profil"
    Pune un dreptunghi semi-transparent de 1080 × 1080 centrat peste postarea ta verticală. Ce rămâne în afara lui **nu se vede** în grila de profil. Dacă titlul e tăiat, mută-l.

---

## Canva: cum îl folosești corect

Canva e rapid, dar ușor de folosit prost. Trei reguli.

### Regula 1 — Configurează kitul de brand întâi

**Brand Hub → Brand Kit** (disponibil și pe planul gratuit, cu limitări):

1. **Culori:** adaugă paleta din lecția 03. Cu Canva for Education, poți salva palete complete.
2. **Fonturi:** setează fontul de titlu și cel de text din lecția 04.
3. **Logo:** încarcă variantele SVG din lecția 12.

Rezultatul: la fiecare element nou, culorile și fonturile tale apar primele în listă. Nu mai alegi „aproximativ portocaliu”.

!!! note "Dacă nu ai acces la Brand Kit"
    Pe planul gratuit fără Education, fă-ți o listă cu cele 5 coduri HEX într-un fișier text și copiază-le manual. În Canva, la selectorul de culoare, există un câmp pentru cod HEX și o secțiune „Culori folosite recent”.

### Regula 2 — Șablonul e structură, nu rezultat

Când pornești de la un șablon Canva:

| Ce păstrezi | Ce schimbi **obligatoriu** |
|-------------|----------------------------|
| Structura compoziției | Toate culorile → paleta ta |
| Ierarhia mărimilor | Toate fonturile → fonturile tale |
| Poziționarea blocurilor | Toate imaginile → ale tale |
| — | Elementele decorative generice → scoase sau înlocuite |

!!! warning "Elementele Pro cu coroană"
    Filtrează întotdeauna după **Free** înainte să alegi un element. Altfel, exportul îți va cere plata sau va avea filigran. Filtrul e în partea de sus a panoului Elemente.

### Regula 3 — Verifică ce ai importat

Canva nu îți spune dacă textul tău are contrast suficient sau dacă imaginea e de rezoluție prea mică. Verificările din lecțiile 03 și 10 rămân valabile — doar că trebuie făcute manual.

---

## Canva vs. Figma

| Situație | Unealta |
|----------|---------|
| Ai nevoie de o postare în 10 minute | **Canva** |
| Faci un set de 20 de postări coerente | **Figma** (componente + variante) |
| Ai nevoie de forme și ilustrații gata făcute | **Canva** |
| Construiești identitatea vizuală | **Figma** |
| Lucrezi cu cineva care nu știe Figma | **Canva** |
| Ai nevoie de animație simplă | **Canva** (are timeline video) |
| Ai nevoie de control exact pe pixel | **Figma** |
| Faci un prototip interactiv | **Figma** |

!!! tip "Fluxul hibrid, cel mai practic"
    Construiește **șabloanele** în Figma, ca componente cu proprietăți de text și slot-uri de imagine. Exportă exemplele în Canva ca șabloane de brand, pentru colegii care postează săptămânal.

    Astfel, controlul rămâne la tine, iar oricine poate produce o postare corectă în 5 minute.

---

## Anatomia unei postări care funcționează

O postare de feed are ~1.5 secunde să oprească degetul de pe ecran.

### Cele cinci elemente

| Element | Rol | Cât ocupă |
|---------|-----|-----------|
| **Cârligul vizual** | Oprește derularea: o imagine puternică, un contrast mare, o culoare neașteptată | Toată suprafața, sau treimea de sus |
| **Titlul** | Spune despre ce e în maximum 6 cuvinte | 20–30% din înălțime |
| **Informația** | Data, locul, cifra importantă | 10–15% |
| **Marca** | Logo-ul sau culoarea de brand | 5% |
| **Apelul la acțiune** | „Link în bio”, „Vino sâmbătă”, „Detalii în comentarii” | 5% |

!!! note "Textul lung merge în caption, nu în imagine"
    Imaginea trebuie să oprească derularea. Explicația merge în textul postării, unde e și căutabilă, și copiabilă, și accesibilă pentru cititoarele de ecran.

    Regula: **maximum 15 cuvinte pe imagine**.

### Lizibilitatea pe telefon

O postare de 1080 px se afișează pe telefon la aproximativ 400 px lățime. Adică **se micșorează de 2.7 ori**.

| Mărime în fișier (1080 px) | Cum apare pe telefon |
|----------------------------|----------------------|
| 24 px | ~9 px — ilizibil |
| 40 px | ~15 px — minim absolut |
| 60 px | ~22 px — confortabil pentru detalii |
| 90 px | ~33 px — bun pentru informație |
| 140 px+ | ~52 px — titlu |

!!! warning "Testul obligatoriu"
    Înainte să publici, **trimite-ți imaginea pe telefon** și privește-o în feed, nu la zoom maxim. Jumătate din problemele de design la postări dispar dacă faci acest test.

---

## Seria: cum construiești coerență

O postare singură nu construiește o identitate. O **serie** de postări care se recunosc, da.

### Ce se repetă

| Element | Cât de strict |
|---------|---------------|
| Paleta | Identică, întotdeauna |
| Fonturile | Identice, întotdeauna |
| Poziția logo-ului | Același colț, aceeași mărime |
| Structura compoziției | Aceeași grilă, aceleași margini |
| Elementul de accent | Aceeași bară / formă / tratament |

### Ce variază

| Element | De ce |
|---------|-------|
| Imaginea | Altfel toate postările arată identic |
| Titlul | Evident |
| Culoarea de accent, dintr-un set de 3 | Diferențiază categoriile: `eveniment`, `proiect`, `anunț` |

!!! tip "Sistemul de categorii prin culoare"
    Dacă postările despre evenimente sunt portocalii, cele despre proiecte albastre și anunțurile verzi, cine urmărește pagina învață codul în două săptămâni și își dă seama din grilă ce e fiecare postare, fără să o deschidă.

    **Condiția:** toate cele trei culori trebuie să treacă testul de contrast cu textul alb.

---

## Exerciții

### Exercițiu 1 — Zone de siguranță
Construiește un story de 1080 × 1920 și marchează cu dreptunghiuri semi-transparente zonele acoperite de interfață. Apoi plasează conținutul astfel încât nimic important să nu iasă din zona sigură.

??? success "Soluție"
    **Construcția:**
    1. Frame 1080 × 1920.
    2. Dreptunghi 1080 × 250 sus, Fill roșu la 20% — zona interfeței de sus.
    3. Dreptunghi 1080 × 250 jos, Fill roșu la 20% — zona interfeței de jos.
    4. Grupează-le și blochează-le (++ctrl+shift+l++). Redenumește grupul `safe-zones — nu exporta`.
    5. Înainte de export, ascunde grupul.

    **Plasarea conținutului:**
    - Logo: Y = 300 (imediat sub zona de sus).
    - Titlu: centrat vertical în zona sigură, Y ≈ 800.
    - Informația: sub titlu.
    - Apelul la acțiune: Y ≈ 1550, adică la 120 px deasupra zonei de jos.

    **Greșeala frecventă:** apelul la acțiune pus la 1850, pentru că „acolo e jos”. Va fi acoperit complet de bara de răspuns. Nimeni nu îl va vedea.

### Exercițiu 2 — Testul grilei de profil
Ia o postare verticală de 1080 × 1350 și verifică ce se vede în grila de profil. Corectează dacă e nevoie.

??? success "Soluție"
    **Verificarea:**
    1. Peste postarea de 1080 × 1350, pune un dreptunghi de 1080 × 1080 centrat vertical (Y = 135).
    2. Tot ce cade în afara lui, sus și jos, dispare din grilă.

    **Ce se pierde de obicei:** logo-ul pus foarte sus și apelul la acțiune pus foarte jos.

    **Corecția:**
    - Mută logo-ul la Y ≥ 180 (în loc de 60).
    - Mută apelul la acțiune la Y ≤ 1120 (în loc de 1270).
    - Sau: acceptă pierderea lor și asigură-te că **titlul și imaginea** — singurele care contează în grilă — sunt complet în zona centrală.

    **Decizia corectă depinde de scop:** dacă postarea e pentru feed (unde se vede întreagă), zona centrală contează mai puțin. Dacă e pentru a construi aspectul grilei de profil, contează enorm.

### Exercițiu 3 — Trei postări dintr-o serie
Construiește trei postări pătrate care se recunosc instant ca fiind din aceeași familie, dar comunică lucruri diferite: un eveniment, un proiect, un anunț.

??? success "Soluție"
    **Structura comună (identică în toate trei):**
    - 1080 × 1080, fundal `#0F172A`, margini 80 px.
    - Logo-ul cercului, 64 px, colț stânga-sus, la 80 px de margini.
    - O bară de accent de 8 × 160 px sub titlu.
    - Eticheta de categorie, sus-dreapta, majuscule, 24 px, tracking +12%.
    - Titlul, Inter Bold, 88 px, alb, aliniat la stânga, maximum 3 rânduri.
    - Informația, Inter Regular, 32 px, `#CBD5E1`.

    **Ce variază:**

    | Postare | Etichetă | Culoare accent | Conținut |
    |---------|----------|----------------|----------|
    | Eveniment | `EVENIMENT` | `#F97316` portocaliu | `TÂRGUL DE PROIECTE` + data |
    | Proiect | `PROIECT` | `#38BDF8` albastru | `ROBOT CU ESP32` + o fotografie în treimea de jos |
    | Anunț | `ANUNȚ` | `#4ADE80` verde | `ÎNSCRIERI DESCHISE` + termenul |

    **Verificările de contrast pe fundalul `#0F172A`:**
    - `#F97316` → 5.9:1 — trece AA
    - `#38BDF8` → 8.4:1 — trece AAA
    - `#4ADE80` → 11.2:1 — trece AAA

    **Testul de coerență:** pune cele trei una lângă alta la 200 px lățime (cum apar în grila de profil). Trebuie să se vadă instant că sunt din aceeași familie, dar să se distingă categoriile. Dacă arată identic, variază prea puțin. Dacă nu par înrudite, ai variat prea mult.

---

## Mini-proiect: kit complet de comunicare

Construiește un set de **patru șabloane** în Figma (post pătrat, post vertical, story, copertă de eveniment), transformă-le în componente cu proprietăți, și replică-le ca șabloane în Canva.

??? success "Livrabilele și criteriile"
    **În Figma — componentele:**

    | Componentă | Proprietăți | Slot-uri |
    |------------|-------------|----------|
    | `social/post-square` | Category (variant: event/project/news), Title (text), Info (text) | Image |
    | `social/post-vertical` | aceleași | Image |
    | `social/story` | aceleași + CTA (text) | Image |
    | `social/event-cover` | Title, Date | Image |

    Toate patru folosesc **aceleași stiluri** de culoare și text. Schimbarea unui stil actualizează toate șabloanele.

    **În Canva — șabloanele:**
    1. Creează câte un design pentru fiecare format.
    2. Aplică paleta și fonturile din Brand Kit.
    3. Salvează fiecare ca **Șablon de brand** (Share → Template link), ca să poată fi refolosit de colegi fără să strice originalul.

    **Criteriile de evaluare:**

    | # | Criteriu | Verificare |
    |---|----------|-----------|
    | 1 | Zone de siguranță respectate | Suprapune dreptunghiurile de test |
    | 2 | Maximum 15 cuvinte pe imagine | Numără |
    | 3 | Text lizibil pe telefon | Trimite-ți imaginea și privește-o în feed |
    | 4 | Contrast ≥ 4.5:1 | Plugin Contrast pe fiecare culoare de accent |
    | 5 | Logo prezent și lizibil | Minimum 48 px pe 1080 |
    | 6 | Seria se recunoaște | Cele 4 formate una lângă alta |
    | 7 | Schimbarea unui stil actualizează tot | Testul din lecția 08 |
    | 8 | Șabloanele Canva sunt partajabile | Deschide link-ul într-un browser în care nu ești logat |

    **Testul final, cel practic:** cere unui coleg care nu a lucrat la proiect să facă o postare pentru un eveniment real, folosind șablonul tău din Canva. Cronometrează-l. Dacă durează peste 10 minute sau dacă rezultatul nu mai arată ca seria ta, șablonul e prea complicat sau prea permisiv — simplifică-l.

---

## Rezumat

- Reține **raporturile**, nu numerele: 1:1, 4:5, 9:16, 16:9.
- **4:5 (1080 × 1350)** este formatul implicit pentru feed — ocupă cel mai mult ecran.
- **Zone de siguranță:** 250 px sus și jos la story; zona centrală de 1080 × 1080 la postările verticale.
- În Canva, configurează **Brand Kit-ul întâi**; un șablon e structură, nu rezultat.
- Filtrează după **Free** ca să eviți elementele Pro cu filigran.
- Figma pentru sisteme și control, Canva pentru viteză; fluxul hibrid le combină.
- **Maximum 15 cuvinte** pe imagine — restul merge în caption.
- O postare de 1080 px se vede la ~400 px pe telefon: minimum **40 px** pentru orice text.
- **Seria** construiește identitatea: repeți paleta, fonturile și structura; variezi imaginea și titlul.
- Codul de culori pe categorii se învață de urmăritori în două săptămâni.

---

**Pasul următor:** [→ Lecția 14: Design de interfață web](14-design-interfata-web.md)
