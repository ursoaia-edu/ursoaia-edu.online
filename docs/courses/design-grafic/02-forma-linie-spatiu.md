---
lesson: 2
tags: [design, formă, linie, spațiu alb, gestalt]
summary: Elementele de bază ale oricărei compoziții — linia, forma și spațiul gol — plus legile Gestalt care explică de ce ochiul grupează lucrurile.
---

# Lecția 02 · Formă, linie, spațiu

!!! tip "Ce vei învăța"
    - Ce comunică o **linie** și cum se folosește corect
    - Cele trei **forme primare** și ce asociere are fiecare
    - De ce **spațiul gol** este cel mai subestimat element de design
    - **Greutatea vizuală**: de ce un element mic poate cântări mai mult decât unul mare
    - Legile **Gestalt** — cum grupează ochiul automat
    - Cum construiești forme complexe din forme simple în Figma

---

## Linia

O linie face trei lucruri: **separă**, **leagă** sau **ghidează privirea**. Nimic altceva. Dacă o linie din compoziția ta nu face niciunul dintre aceste trei lucruri, scoate-o.

### Ce comunică direcția

| Direcție | Senzație | Unde o folosești |
|----------|----------|------------------|
| Orizontală | Calm, stabilitate, odihnă | Separatoare între secțiuni |
| Verticală | Forță, formalitate, înălțime | Bare de accent, coloane |
| Diagonală | Mișcare, energie, tensiune | Afișe de sport, elemente dinamice |
| Curbă | Blândețe, natural, organic | Ilustrații, branduri „calde” |

### Grosimea contează

O linie de 1 px spune „aici se termină o secțiune”. O linie de 8 px spune „uită-te aici”. Regula practică:

- **Separatoare:** 1 px, culoare foarte discretă (gri deschis pe alb, `rgba(255,255,255,0.08)` pe fundal închis).
- **Accente:** 4–8 px, culoarea principală a identității.
- **Sublinieri de titlu:** 3–4 px, lățime egală cu 40–60 px, nu cu tot titlul.

!!! warning "Greșeala separatorului prea vizibil"
    Un începător desenează separatoarele cu negru de 2 px. Rezultatul: liniile țipă mai tare decât conținutul. Un separator bun **abia se vede** — ochiul îl simte, nu îl observă.

!!! note "Linia invizibilă"
    Cea mai puternică linie dintr-un design este de multe ori **cea pe care nu o desenezi**: marginea comună pe care sunt aliniate mai multe elemente. Ochiul o completează singur. Mai multe în lecția 05.

---

## Forma

Trei forme primare, trei asocieri. Sunt învățate de la vârste mici și funcționează în aproape toate culturile.

| Formă | Asociere | Exemple reale |
|-------|----------|---------------|
| **Pătrat / dreptunghi** | Stabilitate, ordine, încredere, seriozitate | Bănci, instituții, ferestre de aplicație |
| **Cerc** | Unitate, comunitate, mișcare, prietenie | Rețele sociale, avataruri, butoane de play |
| **Triunghi** | Direcție, tensiune, ierarhie, atenție | Indicatoare de pericol, butoane de redare, săgeți |

!!! note "De ce indicatorul de pericol e triunghi"
    Triunghiul are un vârf. Vârful este o direcție, iar direcția forțează atenția. Un cerc nu are direcție — de aceea nu vei vedea niciodată un semn de avertizare rotund cu vârful în sus.

### Colțurile rotunjite

Raza colțului (`corner radius` în Figma) schimbă tonul fără să schimbe forma:

| Rază | Ton | Folosire tipică |
|------|-----|-----------------|
| 0 px | Sever, tehnic, precis | Tabele, interfețe de date, print |
| 4–8 px | Neutru, modern | Butoane, câmpuri de formular, carduri |
| 16–24 px | Prietenos, moale | Aplicații pentru copii, branduri „calde” |
| 50% (pilulă) | Foarte prietenos, jucăuș | Etichete, badge-uri, butoane de acțiune |

!!! tip "Consistența razei"
    Alege **maximum două raze** pentru tot proiectul: una pentru elemente mici (8 px) și una pentru containere mari (16 px). Un design cu cinci raze diferite arată neîngrijit, chiar dacă nimeni nu poate spune exact de ce.

### Forme complexe din forme simple

Aproape orice pictogramă se construiește din dreptunghiuri și cercuri, folosind **operații booleene**. În Figma, cu două forme selectate, butonul din bara de sus îți dă:

| Operație | Rezultat |
|----------|----------|
| **Union** | Lipește formele într-una singură |
| **Subtract** | Scade forma de deasupra din cea de dedesubt |
| **Intersect** | Păstrează doar zona comună |
| **Exclude** | Păstrează tot, mai puțin zona comună |

Exemplu: o **lună în creștere** = un cerc din care scazi alt cerc, decalat. O **săgeată** = un dreptunghi plus un triunghi, unite.

---

## Spațiul gol

Spațiul gol (**white space** — se numește așa chiar dacă fundalul e negru) nu este spațiu „nefolosit”. Este elementul care face restul lizibil.

### Ce face spațiul gol

1. **Separă** grupurile de informație fără să ai nevoie de linii.
2. **Creează ierarhie** — ce are spațiu în jur pare important.
3. **Odihnește ochiul** — un design dens obosește și se abandonează.
4. **Semnalizează calitate.** Nu întâmplător reclamele la produse scumpe au foarte mult gol; densitatea mare e asociată cu reducerile și cu urgența.

!!! note "Testul mijirii ochilor"
    Mijește ochii până când textul devine ilizibil. Ce rămâne sunt **pete de gri** — blocurile de conținut. Dacă petele sunt lipite una de alta, ai prea puțin spațiu. Dacă vezi clar grupuri separate, spațierea e bună.

### Micro-spațiu și macro-spațiu

- **Micro-spațiu:** între litere, între rânduri, între un buton și textul lui. Afectează lizibilitatea.
- **Macro-spațiu:** între secțiuni, în jurul paginii, între coloane. Afectează structura.

Un design poate avea macro-spațiu generos și micro-spațiu prost (text înghesuit în butoane) și tot va arăta neprofesionist.

### Marginea paginii

Regula minimă pentru un afiș: **marginea nu coboară niciodată sub 5% din latura scurtă**.

| Format | Latura scurtă | Marginea minimă |
|--------|---------------|-----------------|
| A4 (210 × 297 mm) | 210 mm | ~10 mm |
| A3 (297 × 420 mm) | 297 mm | ~15 mm |
| Instagram post (1080 px) | 1080 px | ~54 px |

!!! warning "Zona de tăiere la tipar"
    Când trimiți un afiș la tipografie, hârtia se taie cu o toleranță de 2–3 mm. Dacă textul e la 5 mm de margine, riști să fie tăiat. Ține textul la **minimum 10 mm** de marginea fizică.

---

## Greutatea vizuală

Fiecare element „cântărește” pe pagină. Greutatea nu e dată doar de mărime:

| Factor | Crește greutatea |
|--------|------------------|
| Mărime | Element mai mare |
| Culoare | Culori saturate, calde (roșu, portocaliu) |
| Contrast | Diferență mare față de fundal |
| Izolare | Element singur, cu mult gol în jur |
| Complexitate | O fotografie cântărește mai mult decât un dreptunghi plat |
| Poziție | Partea de sus și dreapta par mai „grele” |

!!! note "De ce un punct roșu mic bate un dreptunghi gri mare"
    Un cerc roșu de 20 px pe un fundal alb atrage privirea înaintea unui dreptunghi gri de 400 px. Contrastul și saturația bat mărimea. Exact de asta funcționează bulina de notificări de pe iconițele aplicațiilor.

### Echilibru

- **Simetric** — aceeași greutate stânga-dreapta. Formal, calm, uneori plictisitor. Potrivit pentru diplome, invitații oficiale.
- **Asimetric** — greutăți diferite, echilibrate prin poziție și spațiu. Dinamic, modern. Un element mare în stânga se echilibrează cu unul mic, dar intens colorat, în dreapta-jos.

---

## Legile Gestalt

Gestalt este un set de observații despre cum grupează creierul uman elementele vizuale, **automat, înainte de gândire conștientă**. Cinci dintre ele îți sunt utile zilnic.

### 1. Proximitate

Elementele apropiate par că formează un grup. Este cel mai puternic instrument de organizare pe care îl ai.

```
●  ●        ●  ●          ●  ●  ●  ●  ●  ●

două grupuri              un singur grup
```

### 2. Similaritate

Elementele care arată la fel (aceeași culoare, formă, mărime) par că aparțin aceleiași categorii — chiar dacă sunt departe unul de altul.

### 3. Închidere

Creierul completează formele incomplete. De aceea un logo format din trei arcuri este citit ca un cerc.

### 4. Continuitate

Ochiul urmează linii și curbe. Elemente aliniate pe o direcție sunt citite ca o secvență, nu ca lucruri separate.

### 5. Figură și fond

Ochiul separă automat „obiectul” de „fundal”. Unele imagini exploatează ambiguitatea: în logo-ul WWF, spațiul alb dintre petele negre formează ursul.

!!! tip "Cum folosești Gestalt practic"
    Când un design pare dezordonat, întreabă-te: **ce grupuri ar trebui să vadă cititorul?** Apoi apropie elementele din același grup și îndepărtează grupurile între ele. De obicei asta rezolvă 80% din problemă, fără să adaugi nimic.

---

## Exerciții

### Exercițiu 1 — Trei separatoare
Într-un frame de 800 × 400 px pe fundal alb, desenează trei separatoare orizontale: unul corect (discret), unul prea gros și unul prea colorat. Privește-le de la 2 metri distanță.

??? success "Soluție"
    - **Corect:** linie de 1 px, culoare `E5E7EB`, lățime 100% din conținut.
    - **Prea gros:** 4 px, negru — devine element principal, deși e doar un separator.
    - **Prea colorat:** 2 px roșu — ochiul merge la el înaintea textului.

    De la 2 metri, primul dispare (exact ce vrei: îl simți ca structură), celelalte două sar în ochi. Un separator care se vede mai tare decât conținutul e o greșeală de ierarhie.

### Exercițiu 2 — Trei pictograme din forme simple
Construiește, doar din dreptunghiuri și cercuri plus operații booleene: o **lună în creștere**, o **săgeată spre dreapta** și un **semn de „interzis”** (cerc cu bară diagonală).

??? success "Soluție"
    **Luna:** două cercuri de 100 × 100 px suprapuse, al doilea decalat cu 25 px la dreapta. Selectezi ambele → **Subtract**. Cercul de deasupra îl scade pe cel de dedesubt.

    **Săgeata:** un dreptunghi de 80 × 12 px (corpul) plus un triunghi de 32 × 32 px lipit de capătul drept. Triunghiul se face cu unealta Polygon (setată la 3 laturi) rotit la 90°. Selectezi ambele → **Union**.

    **Semnul de interzis:** un cerc de 100 × 100 px cu **Fill: none** și **Stroke: 10 px roșu**, plus un dreptunghi de 100 × 10 px roșu, rotit la 45° și centrat. Le grupezi cu ++ctrl+g++.

    Observație: în toate cele trei cazuri ai lucrat cu forme primare. Aproape toate pictogramele pe care le vezi zilnic se construiesc așa.

### Exercițiu 3 — Testul mijirii ochilor
Ia un afiș sau o postare făcută de altcineva, fă-i o captură, pune-o în Figma și aplică peste ea un blur puternic (**Effects → Layer blur → 12**). Câte grupuri distincte vezi?

??? success "Soluție"
    După blur ar trebui să distingi **3–5 pete**: titlu, informația principală, detaliile, eventual imaginea și logo-ul.

    - Dacă vezi **o singură pată mare**, spațierea e insuficientă — grupurile nu se separă.
    - Dacă vezi **peste 8 pete**, designul e fragmentat; cititorul nu știe de unde să înceapă.
    - Dacă cea mai întunecată pată **nu este** informația cea mai importantă, ierarhia e greșită.

    Trucul cu blur-ul este cel mai rapid test de compoziție pe care îl ai. Îl vei refolosi la fiecare proiect.

---

## Mini-proiect: afiș fără text

Construiește un frame A4 în care comunici ideea „**mișcare**” folosind **exclusiv** linii și forme geometrice. Fără text, fără imagini, maximum două culori plus fundalul.

??? success "Soluție"
    O direcție care funcționează:

    1. Frame A4, Fill `FFFFFF`.
    2. Șapte linii diagonale paralele, la 45°, grosime crescătoare de la 2 px la 14 px, distanțate la 24 px. Culoare `1F2937`.
    3. Un cerc de 120 px, Fill `F97316`, plasat în partea dreaptă-sus, exact peste liniile groase.
    4. Marginile: minimum 30 px de la marginea paginii, peste tot.

    **De ce comunică mișcare:** diagonala e direcția care sugerează deplasare; grosimea crescătoare creează accelerație (ochiul citește de la subțire la gros ca de la lent la rapid); cercul portocaliu e „obiectul” care se mișcă, iar poziția lui în dreapta-sus îi dă unde să ajungă.

    **Variante care nu funcționează:**
    - Toate liniile de aceeași grosime → repetiție, nu mișcare.
    - Linii orizontale → calm, exact opusul.
    - Cinci culori → ochiul nu mai știe ce e obiectul și ce e fundalul.

    **Extensie:** fă a doua variantă cu aceleași elemente, dar comunicând „**calm**”. Vei vedea că schimbi doar direcția liniilor și saturația culorii — restul poate rămâne identic.

---

## Rezumat

- O linie **separă, leagă sau ghidează**. Altfel, scoate-o.
- Separatoarele bune abia se văd; accentele sunt groase și colorate.
- **Pătrat** = stabilitate, **cerc** = unitate, **triunghi** = direcție.
- Maximum **două raze de colț** pe tot proiectul.
- Formele complexe se construiesc din forme simple cu **Union, Subtract, Intersect, Exclude**.
- **Spațiul gol** nu e spațiu pierdut — el creează grupuri, ierarhie și impresia de calitate.
- Marginea minimă: **5% din latura scurtă**; la tipar, minimum 10 mm.
- Greutatea vizuală vine din mărime, **culoare, contrast, izolare, complexitate și poziție**.
- Gestalt: **proximitate, similaritate, închidere, continuitate, figură-fond**.
- Testul cel mai rapid de compoziție: **blur puternic** și numără petele.

---

**Pasul următor:** [→ Lecția 03: Culoarea](03-culoarea.md)
