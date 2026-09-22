---
lesson: 10
tags: [imagini, măști, export, png, jpg, svg, webp, rezoluție]
summary: Rezoluție și DPI, încadrarea imaginilor, măști, efecte, și ce format exporți pentru ecran și pentru tipar.
---

# Lecția 10 · Imagini, măști și export

!!! tip "Ce vei învăța"
    - **Rezoluție**, **DPI** și de ce o imagine bună pe ecran e proastă la tipar
    - Cele patru moduri de încadrare: **Fill, Fit, Crop, Tile**
    - **Măști** — cum pui o imagine într-o formă
    - Efecte: umbre, blur, overlay pentru text peste fotografii
    - Ce format alegi: **PNG, JPG, WebP, SVG, PDF**
    - **Exportul la scară** (1×, 2×, 3×) și de ce contează

---

## Rezoluție și DPI

Aici se împiedică aproape toți începătorii.

| Termen | Ce este |
|--------|---------|
| **Rezoluție** | Numărul total de pixeli: 1920 × 1080 |
| **PPI / DPI** | Câți pixeli intră într-un inch (2.54 cm) la tipar |

O imagine de 1920 × 1080 px:
- Pe un ecran: excelentă, e Full HD.
- Tipărită la 300 DPI: 1920 / 300 = **6.4 inch** = 16 cm lățime. Atât. Pe un A3 (42 cm) ar fi neclară.

### De câți pixeli ai nevoie

| Destinație | DPI necesar | Exemplu de calcul |
|------------|-------------|-------------------|
| Ecran, web | 72 (convențional) | Lățimea în px = lățimea afișată |
| Tipar de calitate | **300** | A4 (21 cm) → 21 / 2.54 × 300 = **2480 px** |
| Tipar mare (bannere) | 100–150 | Se privește de departe |
| Print de birou | 150–200 | Suficient pentru materiale interne |

!!! warning "Nu poți mări o imagine mică"
    O fotografie de 800 × 600 px mărită la 2480 px nu câștigă detalii — câștigă pixeli neclari. Informația care lipsește nu poate fi inventată.

    **Regula:** ia întotdeauna imaginea **mai mare decât ai nevoie** și micșoreaz-o. Micșorarea nu strică nimic; mărirea da.

!!! note "Cum verifici dacă o imagine ajunge"
    Ai nevoie de o imagine de 12 cm lățime pe un afiș A3 tipărit la 300 DPI?

    12 cm / 2.54 = 4.72 inch → 4.72 × 300 = **1417 px lățime minimum**.

    Dacă fotografia ta are 1200 px, nu ajunge. Caută alta.

---

## Imagini în Figma

### Cum inserezi

Trei moduri:
- **Trage fișierul** direct pe canvas.
- ++ctrl+shift+k++ → alegi fișierul.
- Selectezi o formă → panoul din dreapta, **Fill** → schimbi din `Solid` în **`Image`**.

Al treilea mod e cel corect în majoritatea cazurilor: imaginea devine **umplerea unei forme**, deci poți controla forma independent de imagine.

### Cele patru moduri de încadrare

Selectează o formă cu umplere de tip imagine. În panoul din dreapta, la Fill, apare un meniu:

| Mod | Ce face | Când |
|-----|---------|------|
| **Fill** | Acoperă toată forma, taie ce depășește | Implicit pentru fotografii în carduri |
| **Fit** | Încape întreagă, lasă spațiu gol | Logo-uri, când nu ai voie să tai |
| **Crop** | Îți dă mânere ca să alegi manual zona | Control fin |
| **Tile** | Repetă imaginea ca un model | Texturi, fundaluri |

!!! tip "Fill este aproape întotdeauna alegerea corectă"
    O fotografie cu `Fit` într-un card dreptunghiular lasă benzi goale sus și jos. Cu `Fill`, umple cardul și se taie ce e în plus. Singura grijă: verifică să nu tai capul cuiva.

    În modul `Crop`, poți repoziționa zona vizibilă fără să schimbi forma — dublu-click pe imagine și mută.

---

## Măști

O **mască** face ca o formă să decupeze ce e deasupra ei.

### Cum funcționează

1. Desenează forma care va fi masca (un cerc, un text, o formă din Pen).
2. Așaz-o **sub** conținutul pe care vrei să-l decupezi (în panoul Layers, masca stă mai jos).
3. Selectează masca **și** conținutul.
4. ++ctrl+alt+m++ sau butonul de mască din bara de sus.

Rezultatul: conținutul se vede doar în interiorul formei-mască.

!!! note "Mască vs. umplere cu imagine"
    Pentru o fotografie într-un cerc, **nu ai nevoie de mască** — pune imaginea ca `Fill` pe un cerc și gata. Masca e utilă când decupezi **mai multe straturi deodată**, sau când forma-mască e complexă (de exemplu un text).

### Text ca mască

Efectul „imagine în interiorul literelor”:

1. Scrie textul, mare și bold (fonturile subțiri nu funcționează).
2. Pune fotografia deasupra textului în panoul Layers.
3. Selectează ambele → ++ctrl+alt+m++.

!!! warning "După mascare, textul rămâne editabil"
    Bine: poți schimba cuvântul. Atenție: dacă schimbi fontul într-unul subțire, efectul dispare — nu mai e destulă suprafață prin care să se vadă imaginea.

---

## Efecte

Panoul din dreapta, secțiunea **Effects**, butonul **+**:

| Efect | Ce face | Folosire |
|-------|---------|----------|
| **Drop shadow** | Umbră în afara formei | Ridică un card de pe fundal |
| **Inner shadow** | Umbră în interior | Câmpuri de formular „adâncite” |
| **Layer blur** | Blurează elementul | Fundaluri, testul de compoziție |
| **Background blur** | Blurează **ce e în spate** | Sticlă mată (glassmorphism) |

### Umbre care arată bine

Greșeala tipică: o umbră neagră, tare, la 50% opacitate. Arată ca Word 2003.

O umbră credibilă are:
- **Culoare** apropiată de fundal, nu negru pur. Pe un fundal albastru deschis, o umbră albastru-închis.
- **Opacitate mică**: 8–15%.
- **Blur mare** raportat la offset: `Y: 4, Blur: 16` arată mai bine decât `Y: 4, Blur: 4`.
- **Offset doar pe Y**, nu și pe X (lumina vine de sus).

```
Umbră proastă:  X:4  Y:4   Blur:4   #000000 50%
Umbră bună:     X:0  Y:4   Blur:16  #0F172A 12%
Umbră mare:     X:0  Y:12  Blur:32  #0F172A 16%
```

!!! tip "Două umbre suprapuse arată cel mai realist"
    Adaugă două `Drop shadow`: una mică și strânsă (`Y: 1, Blur: 2, 8%`) pentru contactul cu suprafața, și una mare și difuză (`Y: 8, Blur: 24, 10%`) pentru volum. Este ce fac toate sistemele de design moderne.

### Text peste fotografie

Problema: fotografia are zone deschise și zone închise, iar textul e ilizibil peste unele.

Patru soluții, de la cea mai simplă:

| Soluție | Cum | Când |
|---------|-----|------|
| **Overlay plat** | Dreptunghi de culoare peste toată imaginea, opacitate 40–65% | Cea mai sigură |
| **Gradient** | Dreptunghi cu gradient de la opac jos la transparent sus | Text doar în partea de jos |
| **Bandă** | Dreptunghi opac doar sub text | Text scurt |
| **Zonă plată** | Alegi o fotografie cu cer / perete uniform și pui textul acolo | Cea mai elegantă, dar depinde de imagine |

!!! warning "Verifică contrastul și aici"
    Un overlay de 40% poate să nu fie destul peste o zonă foarte deschisă. Aplică testul din lecția 03: pluginul Contrast, pe zona cea mai deschisă a imaginii.

---

## Formatele de export

| Format | Tip | Transparență | Când îl folosești |
|--------|-----|--------------|-------------------|
| **PNG** | Raster | Da | Capturi, grafice cu text, orice are nevoie de fundal transparent |
| **JPG** | Raster | Nu | Fotografii; fișier mult mai mic decât PNG |
| **WebP** | Raster | Da | Web modern; ~30% mai mic decât JPG la aceeași calitate |
| **SVG** | Vector | Da | Logo-uri, pictograme, ilustrații plate |
| **PDF** | Mixt | Da | Tipar, documente multi-pagină |

!!! note "Regula scurtă"
    - Are text sau linii clare și trebuie să fie vector? → **SVG**
    - E fotografie? → **JPG** (sau WebP pe web)
    - Are nevoie de fundal transparent și nu e vector? → **PNG**
    - Merge la tipar? → **PDF**

### Scara exportului

Ecranele moderne au densitate dublă sau triplă. O imagine exportată la 1× va arăta neclară pe un telefon.

| Scară | Pentru | Un frame de 400 × 300 devine |
|-------|--------|------------------------------|
| **1×** | Referință, mockup-uri | 400 × 300 px |
| **2×** | Ecrane retina (majoritatea telefoanelor și laptopurilor) | 800 × 600 px |
| **3×** | Ecrane de telefon foarte dense | 1200 × 900 px |

În panoul de Export poți adăuga mai multe rânduri, fiecare cu scara și sufixul lui (`@2x`, `@3x`).

!!! tip "Pentru web, exportă la 2× și micșorează în CSS"
    Exporți un `card@2x.jpg` de 800 px și îl afișezi la 400 px. Arată clar pe orice ecran. Pentru SVG nu se pune problema — se scalează perfect oricum.

### Export pentru tipar

1. Setează frame-ul la dimensiunea fizică reală. În Figma, pentru A4 folosește **595 × 842** (puncte, adică 72 DPI) sau **2480 × 3508** (pixeli la 300 DPI).
2. Exportă **PDF**.
3. Dacă tipografia cere **bleed** (zonă de siguranță pentru tăiere), fă frame-ul cu 3 mm mai mare pe fiecare latură și extinde fundalul până la margine.
4. Textul rămâne text în PDF-ul din Figma — bine pentru claritate. Dacă tipografia nu are fontul, cere-le să folosească PDF-ul așa cum e, nu să reeditează.

!!! warning "Figma nu face CMYK"
    Figma exportă în RGB. Conversia la CMYK o face tipografia. Consecința practică: **cere o probă tipărită** înainte de tirajul mare, mai ales dacă ai culori saturate.

---

## Optimizarea pentru web

O pagină cu imagini neoptimizate se încarcă lent, iar vizitatorii pleacă.

| Pas | Unealtă | Câștig tipic |
|-----|---------|--------------|
| Dimensiune corectă | Export la exact ce ai nevoie, ×2 | Cel mai mare câștig |
| Compresie JPG | [Squoosh](https://squoosh.app/), calitate 75–85 | 40–60% |
| Conversie WebP | Squoosh | încă 25–35% |
| Curățare SVG | [SVGOMG](https://jakearchibald.github.io/svgomg/) | 30–60% |

!!! note "Exemplu real — acest site"
    Site-ul pe care citești acum generează automat variante `.webp` pentru fiecare `.jpg` și `.png`, iar browserul o alege pe cea mai mică pe care o suportă. Rezultatul: încărcarea imaginilor a scăzut de la 15.4 MB la 3.2 MB — aproximativ **80% mai puțin**, fără diferență vizibilă.

---

## Exerciții

### Exercițiu 1 — Calcule de rezoluție
Răspunde, cu calculul scris:

1. Ce rezoluție minimă are nevoie o imagine care ocupă 15 cm lățime pe un afiș A3 tipărit la 300 DPI?
2. O fotografie de 4000 × 3000 px, tipărită la 300 DPI, ce dimensiune fizică maximă are?
3. Ai nevoie de un banner de 2 m lățime privit de la 5 metri. Ce rezoluție e suficientă?

??? success "Soluție"
    **1.** 15 cm / 2.54 = 5.9 inch → 5.9 × 300 = **1772 px lățime**.

    **2.** 4000 / 300 = 13.3 inch → 13.3 × 2.54 = **33.8 cm lățime**; 3000 / 300 = 10 inch → **25.4 cm înălțime**. Deci puțin mai mare decât un A4, mai mic decât un A3.

    **3.** La 5 metri distanță, ochiul nu distinge detalii fine. 100 DPI e suficient: 200 cm / 2.54 = 78.7 inch → 78.7 × 100 = **7870 px lățime**. La 300 DPI ar fi 23 600 px — un fișier uriaș, complet inutil.

    **Concluzia:** DPI-ul necesar scade cu distanța de privire. 300 DPI e pentru ce ții în mână.

### Exercițiu 2 — Text lizibil peste fotografie
Ia o fotografie cu contrast neuniform (de exemplu un peisaj cu cer luminos și pământ întunecat) și pune peste ea un titlu alb, în patru variante: fără tratament, cu overlay plat, cu gradient, cu bandă. Verifică contrastul la fiecare.

??? success "Soluție"
    | Variantă | Construcție | Contrast minim măsurat |
    |----------|-------------|------------------------|
    | Fără tratament | Text alb direct pe foto | ~1.8:1 peste cer — **cade** |
    | Overlay plat | Dreptunghi `#0F172A` la 55% peste toată imaginea | ~7.2:1 — **trece AAA** |
    | Gradient | Dreptunghi cu gradient liniar de la `#0F172A` 85% (jos) la 0% (sus), text jos | ~9.1:1 în zona textului |
    | Bandă | Dreptunghi `#0F172A` opac, înălțime cât textul + 32 px padding | ~15:1 |

    **Care e cea mai bună?** Depinde:
    - **Overlay plat** — cel mai sigur, dar întunecă toată fotografia.
    - **Gradient** — cel mai elegant; păstrează fotografia curată sus și garantează lizibilitatea jos. Alegerea implicită pentru afișe și carduri.
    - **Bandă** — cel mai puternic contrast, dar acoperă mult din imagine.

    **Verificarea obligatorie:** măsoară contrastul în zona **cea mai deschisă** de sub text, nu în medie.

### Exercițiu 3 — Set complet de exporturi
Ia cardul de proiect construit în lecția 09 și exportă-l în toate formatele potrivite: pentru web (2×), pentru o prezentare (1×), pentru tipar. Compară mărimile fișierelor.

??? success "Soluție"
    | Destinație | Format | Scară | Mărime tipică |
    |------------|--------|-------|---------------|
    | Web, cu fotografie | JPG, calitate 80 | 2× | 60–120 KB |
    | Web, optimizat | WebP, calitate 80 | 2× | 40–80 KB |
    | Prezentare / document | PNG | 1× | 150–400 KB |
    | Tipar | PDF | — | 200 KB – 2 MB |
    | Doar pictograma din card | SVG | — | 0.5–2 KB |

    **Ce observi:**
    - PNG-ul e mai mare decât JPG-ul deși are aceeași dimensiune — PNG e fără pierderi, JPG comprimă.
    - WebP e vizibil mai mic decât JPG la aceeași calitate percepută.
    - SVG-ul e cu trei ordine de mărime mai mic decât orice raster — și arată perfect la orice dimensiune.

    **Configurarea în Figma:** selectează frame-ul, la Export apasă **+** de trei ori și setează: `JPG 2× sufix @2x`, `PNG 1×`, `PDF`. Un singur click exportă toate trei.

---

## Mini-proiect: card de eveniment cu fotografie

Construiește un card de eveniment de **1080 × 1350 px** (format vertical pentru rețele sociale) care conține o fotografie de fundal, un gradient, un titlu, data și logo-ul cercului. Exportă-l în trei variante: WebP pentru web, JPG pentru trimis pe WhatsApp, PDF pentru tipărit A5.

??? success "Soluție"
    **Construcția:**

    1. Frame `event-card`, 1080 × 1350 px.
    2. **Fotografia:** caută pe Unsplash una de minimum 2000 px lățime. Pune-o ca `Fill` pe un dreptunghi care acoperă tot frame-ul, mod `Fill`, repoziționată cu `Crop` astfel încât zona interesantă să fie în treimea de sus.
    3. **Gradientul:** dreptunghi peste toată suprafața, umplere `Linear gradient`, de la `#0F172A` cu opacitate 95% jos la `#0F172A` cu opacitate 0% la 55% din înălțime.
    4. **Conținutul** (Auto Layout vertical, gap 16, padding 64, ancorat jos):
        - Etichetă: `CERCUL DE INFORMATICĂ`, 24 px, Medium, `#F97316`, tracking +12%
        - Titlu: 88 px, Bold, alb, tracking −2%, maximum 3 rânduri
        - Data și locul: 32 px, Regular, `#CBD5E1`
    5. **Logo-ul:** SVG, 64 px, colț stânga-sus, cu 48 px margine. Adaugă-i o umbră discretă (`Y: 2, Blur: 8, 25%`) ca să se vadă și peste zone deschise.

    **Verificările înainte de export:**

    | Verificare | Cum |
    |-----------|-----|
    | Contrastul titlului | Plugin Contrast, pe cel mai deschis punct de sub text — minimum 4.5:1 |
    | Rezoluția fotografiei | Trebuie să fie ≥ 1080 px pe latura scurtă **înainte** de încadrare |
    | Textul nu atinge marginile | Minimum 54 px (5% din 1080) peste tot |
    | Testul de blur | Titlul trebuie să fie pata dominantă |

    **Exporturile:**

    | Variantă | Setare | De ce |
    |----------|--------|-------|
    | Web | WebP, 1× (1080 px e deja suficient) | Format nativ pentru rețele |
    | WhatsApp | JPG, 1×, calitate 85 | WhatsApp recomprimă oricum; nu trimite PNG |
    | Tipar A5 | PDF | A5 la 300 DPI = 1748 × 2480 px; cardul tău de 1080 px dă ~150 DPI, acceptabil pentru print de birou dar nu pentru tipografie |

    **Observația importantă:** dacă vrei tipar profesional, trebuie să reconstruiești cardul la 1748 × 2480 px de la început, cu o fotografie de minimum 2500 px. Nu poți mări la final. Aceasta e exact greșeala pe care lecția a încercat să o prevină.

---

## Rezumat

- **Rezoluție** = pixeli totali; **DPI** = pixeli pe inch la tipar.
- Pentru tipar de calitate: **300 DPI**. A4 = 2480 px lățime.
- **Nu poți mări o imagine mică.** Ia mereu mai mare și micșorează.
- DPI-ul necesar **scade cu distanța de privire**: un banner are nevoie de 100, nu de 300.
- Încadrare: **Fill** (implicit), Fit, Crop, Tile.
- Masca decupează ce e deasupra ei; pentru o singură imagine într-o formă, folosește `Fill` în loc de mască.
- Umbre bune: **offset doar pe Y**, blur mare, opacitate 8–15%, culoare apropiată de fundal.
- Text peste fotografie: **gradient** este cea mai bună soluție implicită.
- Formate: **SVG** vector, **JPG/WebP** fotografii, **PNG** transparență, **PDF** tipar.
- Exportă la **2×** pentru web; optimizează cu Squoosh și SVGOMG.

---

**Pasul următor:** [→ Lecția 11: Afiș pentru un eveniment școlar](11-proiect-afis.md)
