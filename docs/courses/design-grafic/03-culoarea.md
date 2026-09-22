---
lesson: 3
tags: [culoare, hex, rgb, hsl, contrast, accesibilitate, paletă]
summary: Roata cromatică, sistemele HEX, RGB și HSL, cum construiești o paletă de 3–5 culori și cum verifici contrastul pentru accesibilitate.
---

# Lecția 03 · Culoarea

!!! tip "Ce vei învăța"
    - Cum se citește **roata cromatică** și ce sunt schemele de culoare
    - Sistemele **HEX**, **RGB** și **HSL** — și de ce HSL e cel mai util la lucru
    - Regula **60-30-10** pentru construit o paletă
    - Diferența dintre **RGB (ecran)** și **CMYK (tipar)**
    - Cum verifici **contrastul** și de ce contează pentru accesibilitate
    - Cum creezi o paletă în Figma și o salvezi ca stiluri

---

## Roata cromatică

Roata cromatică așază culorile în ordinea în care se amestecă. Din ea se citesc toate schemele de culoare.

```
                    ROȘU
         ROȘU-VIOLET    ROȘU-PORTOCALIU
    VIOLET                        PORTOCALIU
 ALBASTRU-VIOLET              GALBEN-PORTOCALIU
    ALBASTRU                       GALBEN
         ALBASTRU-VERDE   GALBEN-VERDE
                    VERDE
```

**Culori calde** (roșu → galben): avansează spre privitor, energie, urgență, apetit.
**Culori reci** (verde → violet): se retrag, calm, încredere, profesionalism, tehnologie.

### Schemele de culoare

| Schemă | Cum se alege | Efect | Când o folosești |
|--------|--------------|-------|------------------|
| **Monocromatică** | O singură culoare, mai multe luminozități | Foarte coerent, calm, sigur | Când nu ai încredere în alegerile tale |
| **Analogă** | 2–3 culori vecine pe roată | Armonios, natural, blând | Afișe, ilustrații, branduri „calde” |
| **Complementară** | 2 culori opuse pe roată | Contrast maxim, energic | Sport, promoții, atenționări |
| **Triadică** | 3 culori la 120° una de alta | Viu, echilibrat, jucăuș | Materiale pentru copii, evenimente |
| **Split-complementară** | O culoare + cele două vecine ale opusului ei | Contrast fără agresivitate | Cea mai sigură alegere pentru începători |

!!! tip "Începe monocromatic"
    Dacă ai dubii, ia **o singură culoare** și lucrează cu 5 luminozități diferite ale ei, plus un gri neutru și o singură culoare de accent. E aproape imposibil să greșești și rezultatul arată deliberat.

---

## HEX, RGB, HSL

Aceeași culoare, trei moduri de a o scrie.

### HEX — pentru copiat

`#F97316` — șase caractere hexazecimale: două pentru roșu, două pentru verde, două pentru albastru, fiecare de la `00` la `FF` (0–255).

```
#F9 73 16
 │  │  │
 │  │  └── albastru: 0x16 = 22
 │  └───── verde:    0x73 = 115
 └──────── roșu:     0xF9 = 249
```

Este formatul pe care îl copiezi între Figma, CSS și Canva. Nu e util pentru gândit.

### RGB — cum funcționează ecranul

`rgb(249, 115, 22)` — aceeași culoare. Ecranele **adună** lumină: roșu + verde + albastru la maximum dau alb. Se numește sinteză **aditivă**.

Varianta cu transparență: `rgba(249, 115, 22, 0.5)` — ultimul număr e opacitatea, de la 0 (invizibil) la 1 (opac).

### HSL — pentru gândit

`hsl(25, 95%, 53%)` — trei valori care corespund modului în care oamenii vorbesc despre culoare:

| Componentă | Interval | Ce înseamnă |
|------------|----------|-------------|
| **H** (hue, nuanță) | 0–360° | Poziția pe roata cromatică |
| **S** (saturation) | 0–100% | Cât de intensă e; 0% = gri |
| **L** (lightness) | 0–100% | Cât de deschisă; 0% = negru, 100% = alb |

!!! note "De ce HSL îți ușurează viața"
    Vrei o variantă mai închisă a portocaliului tău pentru starea `hover` a unui buton? În HEX trebuie să ghicești. În HSL scazi 10 la L: `hsl(25, 95%, 43%)`. Gata.

    O paletă întreagă se construiește păstrând H constant și variind L: `hsl(25, 95%, 95%)` pentru fundal foarte deschis, `hsl(25, 95%, 53%)` pentru culoarea principală, `hsl(25, 95%, 25%)` pentru text pe fundal deschis.

În Figma, la selectorul de culoare, butonul cu trei puncte îți permite să comuți între HEX, RGB, HSL și CSS.

---

## RGB vs. CMYK

Aceasta e diferența care strică cele mai multe afișe tipărite.

| | RGB | CMYK |
|---|-----|------|
| **Unde** | Ecrane | Tipar |
| **Cum funcționează** | Adună lumină | Scade lumină (cerneală pe hârtie) |
| **Componente** | Roșu, Verde, Albastru | Cyan, Magenta, Yellow, Key (negru) |
| **Gamă de culori** | Mai largă | Mai îngustă |
| **Alb** | Toate la maximum | Absența cernelii (hârtia) |

!!! warning "Culorile fluorescente nu se tipăresc"
    Un verde neon strălucitor pe ecran (`#39FF14`) va ieși la tipar ca un verde-măsliniu trist. Cernelurile CMYK nu pot reproduce culorile foarte saturate din RGB.

    **Ce faci:** dacă lucrarea merge la tipar, evită saturațiile peste ~85% și verifică o probă tipărită înainte de tirajul mare. Figma lucrează nativ în RGB — pentru CMYK real ai nevoie de un pas de conversie la tipografie.

---

## Regula 60-30-10

O paletă echilibrată distribuie culorile în proporții inegale:

- **60% — culoarea dominantă.** De obicei un neutru: alb, gri foarte deschis, sau un gri foarte închis. Este fundalul.
- **30% — culoarea secundară.** Susține structura: carduri, bare, secțiuni.
- **10% — culoarea de accent.** Doar pentru ce trebuie apăsat sau observat: butonul principal, un badge, o cifră importantă.

!!! note "Exemplu — paleta acestui site"
    - **60%** — fundal zinc foarte închis (`#0D0D10`) sau alb, după temă.
    - **30%** — grile de text și carduri (`#27272A`, `#A1A1AA`).
    - **10%** — portocaliu (`#F97316`), folosit **doar** pentru link-uri, butoane și accente.

    Observă că portocaliul apare rar. De asta funcționează: dacă ar fi peste tot, nu ar mai însemna „aici”.

### Structura unei palete complete

Pentru un proiect serios ai nevoie de mai mult decât trei culori:

| Rol | Câte | Exemplu |
|-----|------|---------|
| Primară | 1 | Culoarea identității |
| Neutre | 4–6 | De la aproape alb la aproape negru |
| Accent | 1 | Opusă sau complementară primarei |
| Semantice | 3 | Succes (verde), avertisment (galben), eroare (roșu) |

!!! warning "Nu folosi negru pur și alb pur"
    `#000000` pe `#FFFFFF` dă un contrast dur, obositor la citit lung. Folosește `#111827` pentru text și `#FAFAFA` pentru fundal. Diferența e mică, dar ochiul o simte după 5 minute de citit.

---

## Contrastul și accesibilitatea

Aproximativ **1 din 12 bărbați** și **1 din 200 de femei** au o formă de daltonism. Mult mai mulți citesc pe telefon, în soare, pe un ecran ieftin. Contrastul nu este o opțiune estetică.

### Raportul de contrast

Se măsoară ca raport între luminozitatea textului și cea a fundalului, de la 1:1 (identice) la 21:1 (negru pe alb). Standardul **WCAG** cere:

| Nivel | Text normal | Text mare (≥ 24 px sau ≥ 19 px bold) |
|-------|-------------|--------------------------------------|
| **AA** (minim obligatoriu) | 4.5:1 | 3:1 |
| **AAA** (ideal) | 7:1 | 4.5:1 |

### Cum verifici

- **În Figma:** pluginul gratuit **Contrast** sau **Stark**. Selectezi textul și îți arată raportul instant.
- **În browser:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — pui cele două coduri HEX și îți dă verdictul.

!!! warning "Combinațiile care cad mereu testul"
    - Galben pe alb (raport ~1.5:1) — ilizibil
    - Gri deschis pe alb (`#CCCCCC` pe `#FFFFFF`, ~1.6:1)
    - Text alb pe portocaliu deschis (~2:1)
    - Albastru pe roșu — contrast de luminozitate aproape zero, vibrează

### Culoarea nu poate fi singura informație

Dacă într-un grafic linia „vândut” e verde și „nevândut” e roșie, un daltonist vede două linii identice. **Adaugă întotdeauna un al doilea semnal**: o etichetă, o formă diferită, o linie punctată, o pictogramă.

!!! tip "Testul alb-negru"
    Fă o captură a lucrării tale și transform-o în alb-negru (în Figma: efect **Saturation → -100** peste tot frame-ul). Dacă informația încă se înțelege, designul e robust. Dacă se pierde, te bazezi prea mult pe culoare.

---

## Cum construiești o paletă în Figma

1. Alege culoarea primară. Nu o inventa din senin — pornește de la ceva: culorile școlii, o fotografie care îți place, un logo existent.
2. Deschide [coolors.co](https://coolors.co/), fixează culoarea primară (tasta `space` generează variante) și alege încă 2–4 care merg cu ea.
3. Generează neutrele: ia primara, du saturația la 5–10% și variază luminozitatea de la 98% la 10%. Vei avea griuri care „au” culoarea ta, nu griuri moarte.
4. Verifică fiecare pereche text/fundal cu pluginul Contrast.
5. **Salvează-le ca stiluri** în Figma: selectezi un element cu acea culoare, în panoul din dreapta la **Fill** apeși pe cele patru puncte → **+** → dai un nume.

### Cum numești culorile

!!! warning "Nu le numi după cum arată"
    `Albastru` este un nume prost. Când peste o lună schimbi albastrul în verde, stilul se va numi „Albastru” dar va fi verde.

    Numește-le **după rol**:

    | Nume bun | Nume prost |
    |----------|------------|
    | `brand/primary` | `Portocaliu` |
    | `brand/primary-hover` | `Portocaliu închis` |
    | `text/strong` | `Negru` |
    | `text/muted` | `Gri` |
    | `surface/base` | `Alb` |
    | `feedback/error` | `Roșu` |

Slash-ul din nume creează automat foldere în panoul de stiluri din Figma.

---

## Psihologia culorii, pe scurt și cu rezerve

Asocierile sunt reale, dar **culturale și contextuale**, nu universale.

| Culoare | Asociere frecventă în Europa | Folosită de |
|---------|------------------------------|-------------|
| Roșu | Urgență, pasiune, pericol, apetit | Promoții, fast-food, atenționări |
| Portocaliu | Energie, accesibil, prietenos | Butoane de acțiune, educație |
| Galben | Optimism, atenție, ieftin | Avertismente, reduceri |
| Verde | Natură, siguranță, „mergi”, sănătate | Confirmări, ecologie, farmacii |
| Albastru | Încredere, calm, tehnologie, corporativ | Bănci, rețele sociale, software |
| Violet | Creativitate, lux, mister | Branduri premium, cosmetice |
| Negru | Eleganță, autoritate, scump | Modă, tehnologie premium |

!!! note "Atenție la context cultural"
    Albul înseamnă puritate în Europa și doliu în mai multe țări din Asia. Roșul e noroc în China și pericol în Europa. Dacă lucrarea ta se adresează unui public internațional, verifică.

---

## Exerciții

### Exercițiu 1 — Aceeași culoare în trei sisteme
Ia culoarea `#2563EB` și scrie-o în RGB și HSL. Apoi creează o variantă cu 15% mai închisă, folosind HSL.

??? success "Soluție"
    - **HEX:** `#2563EB`
    - **RGB:** `rgb(37, 99, 235)` — `0x25 = 37`, `0x63 = 99`, `0xEB = 235`
    - **HSL:** `hsl(221, 83%, 53%)`

    Varianta mai închisă: scazi 15 din L → `hsl(221, 83%, 38%)`, adică `#1D4ED8`.

    În Figma: selectezi elementul, deschizi selectorul de culoare, apeși pe eticheta formatului (scrie `HEX`) și comuți la `HSL`. Modifici doar a treia valoare.

### Exercițiu 2 — Paletă 60-30-10
Construiește o paletă pentru un afiș al cercului de informatică: o primară, patru neutre și un accent. Aplic-o pe un frame A4 în proporțiile 60-30-10.

??? success "Soluție"
    O paletă care funcționează:

    | Rol | HEX | HSL | Unde |
    |-----|-----|-----|------|
    | `surface/base` | `#0F172A` | `hsl(222, 47%, 11%)` | Fundal — 60% |
    | `surface/raised` | `#1E293B` | `hsl(217, 33%, 17%)` | Carduri — 30% |
    | `text/strong` | `#F1F5F9` | `hsl(210, 40%, 96%)` | Titluri |
    | `text/muted` | `#94A3B8` | `hsl(215, 20%, 65%)` | Text secundar |
    | `brand/primary` | `#F97316` | `hsl(25, 95%, 53%)` | Accent — 10% |

    Verificări de contrast:
    - `text/strong` pe `surface/base` → **15.8:1** — trece AAA
    - `text/muted` pe `surface/base` → **6.4:1** — trece AA, nu AAA. Acceptabil pentru text secundar.
    - `brand/primary` pe `surface/base` → **5.9:1** — trece AA pentru text normal.

    Greșeala tipică: folosirea accentului la 40% din suprafață. Atunci nu mai e accent, e a doua culoare dominantă, și nimic nu mai iese în evidență.

### Exercițiu 3 — Repară trei combinații
Următoarele perechi cad testul de contrast. Corectează fiecare, păstrând nuanța (H) neschimbată.

1. Text `#FFD700` pe fundal `#FFFFFF`
2. Text `#FFFFFF` pe fundal `#FB923C`
3. Text `#9CA3AF` pe fundal `#F3F4F6`

??? success "Soluție"
    **1.** `#FFD700` pe alb = **1.6:1**. Galbenul nu poate fi text pe alb, punct. Păstrezi H = 51° și cobori L de la 50% la 30%: `hsl(51, 100%, 30%)` = `#997A00`, raport **5.3:1**. Trece AA.

    **2.** Alb pe `#FB923C` = **2.1:1**. Fie închizi fundalul: `hsl(27, 96%, 40%)` = `#C2560A`, raport **4.7:1**. Fie păstrezi portocaliul deschis și pui text închis: `#431407` pe `#FB923C` = **7.9:1**. A doua variantă e mai plăcută vizual.

    **3.** `#9CA3AF` pe `#F3F4F6` = **2.4:1**. Cobori L-ul textului: `#4B5563`, raport **7.3:1**. Trece AAA.

    Observă tiparul: în toate cele trei cazuri soluția a fost să **mărești diferența de luminozitate (L)**, nu de nuanță. Contrastul de culoare fără contrast de luminozitate nu ajută pe nimeni.

---

## Mini-proiect: același afiș, trei palete

Ia mini-proiectul din lecția 02 (afișul „mișcare”) și fă trei variante identice ca formă, diferite doar prin paletă: una **monocromatică**, una **complementară** și una **analogă**. Verifică contrastul la fiecare.

??? success "Soluție"
    **Monocromatică — albastru:**
    fundal `hsl(217, 91%, 96%)`, linii `hsl(217, 91%, 25%)`, cerc `hsl(217, 91%, 53%)`.
    Efect: calm, tehnic, coerent. Contrast linii/fundal: 11.2:1.

    **Complementară — albastru și portocaliu:**
    fundal `hsl(217, 30%, 12%)`, linii `hsl(217, 60%, 70%)`, cerc `hsl(25, 95%, 53%)`.
    Efect: energic, cercul sare imediat. E cea mai „afiș de eveniment” dintre cele trei.

    **Analogă — albastru, albastru-verde, verde:**
    fundal `hsl(190, 40%, 95%)`, linii `hsl(200, 70%, 30%)`, cerc `hsl(160, 70%, 40%)`.
    Efect: armonios dar moale — cercul nu iese suficient. Aceasta e limita schemei analoge: e frumoasă, dar are contrast intern mic.

    **Concluzia exercițiului:** paleta nu decorează compoziția, o **schimbă**. Aceeași formă comunică „tehnic”, „energic” sau „calm” doar prin culoare. Iar dacă ai nevoie ca un element să sară în ochi, schema analogă îți va da bătăi de cap.

---

## Rezumat

- Roata cromatică dă schemele: **monocromatică, analogă, complementară, triadică, split-complementară**.
- **HEX** pentru copiat, **RGB** pentru ecran, **HSL** pentru gândit și pentru generat variante.
- **RGB pe ecran, CMYK la tipar.** Saturațiile mari nu se tipăresc.
- **60-30-10**: dominant neutru, secundar de structură, accent rar.
- Nu folosi `#000000` pe `#FFFFFF` — obosește ochiul.
- Contrast minim **4.5:1** pentru text normal, **3:1** pentru text mare (WCAG AA).
- **Culoarea nu poate fi singura informație** — adaugă etichetă, formă sau pictogramă.
- Numește stilurile **după rol** (`brand/primary`), nu după aspect (`Portocaliu`).
- Testul alb-negru îți spune dacă designul rezistă fără culoare.

---

**Pasul următor:** [→ Lecția 04: Tipografia](04-tipografia.md)
