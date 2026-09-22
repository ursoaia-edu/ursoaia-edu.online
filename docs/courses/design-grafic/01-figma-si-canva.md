---
lesson: 1
tags: [figma, canva, instrumente, interfață, început]
summary: Cont gratuit în Figma și Canva, interfața fiecăruia, primul fișier, salvare, partajare și când folosești unul sau altul.
---

# Lecția 01 · Figma și Canva — primul contact

!!! tip "Ce vei învăța"
    - Cum îți faci **cont gratuit** în Figma și Canva
    - Ce este un **frame** și de ce nu desenezi niciodată „pe pânză goală”
    - Interfața Figma: panoul din stânga, canvas-ul, panoul din dreapta
    - **Scurtăturile** de tastatură pe care le vei folosi în fiecare lecție
    - Cum salvezi, cum partajezi și cum revii la o versiune veche
    - **Când folosești Figma și când Canva**

---

## Două instrumente, două meserii

| | Figma | Canva |
|---|-------|-------|
| **La ce e bun** | Desenezi de la zero, cu control total | Pornești de la un șablon și îl adaptezi |
| **Tip de grafică** | Vectorială (se scalează la orice mărime) | Mixtă, orientată pe șabloane |
| **Punctul forte** | Componente, Auto Layout, prototipuri | Viteză, bibliotecă uriașă de elemente |
| **Punctul slab** | Curbă de învățare mai abruptă | Control fin limitat; multe lucrări seamănă între ele |
| **Îl folosim pentru** | Logo, interfețe, prototipuri (lecțiile 07–12, 14, 16) | Postări, story-uri, materiale rapide (lecția 13) |

!!! note "De ce începem cu Figma"
    Canva îți dă rezultate frumoase în 10 minute, dar nu te învață *de ce* sunt frumoase — deciziile sunt deja luate de șablon. Figma te obligă să iei tu fiecare decizie. Învățăm întâi în Figma, apoi folosim Canva ca unealtă de viteză.

---

## Cont și instalare

### Figma

1. Intră pe [figma.com](https://www.figma.com/) și apasă **Sign up**.
2. Folosește o adresă de e-mail (ideal cea de școală — vezi mai jos).
3. La întrebarea despre plan, alege **Starter** (gratuit). Îți ajunge pentru tot cursul.
4. Poți lucra direct în browser. Aplicația de desktop este opțională și se descarcă de la **Products → Desktop app**.

!!! tip "Plan Education gratuit"
    Cu o adresă de e-mail de școală poți cere planul **Figma for Education**, care deblochează proiecte de echipă nelimitate și biblioteci partajate. Se cere de la [figma.com/education](https://www.figma.com/education/). Cursul funcționează complet și pe planul Starter obișnuit.

### Canva

1. Intră pe [canva.com](https://www.canva.com/) și apasă **Înregistrare**.
2. Alege **Canva Free**.
3. Dacă școala ta are cont, **Canva for Education** este gratuit și deblochează elementele Pro.

!!! warning "Elementele cu coroană"
    În Canva, elementele marcate cu o **coroană** sunt Pro. Dacă le folosești pe cont gratuit, imaginea exportată va avea o filigranare sau ți se va cere plata. Filtrează întotdeauna după **Free** înainte să alegi.

---

## Interfața Figma

Deschide Figma și creează un fișier nou: **+ Design file**. Vei vedea trei zone.

```
┌──────────────┬────────────────────────────┬──────────────┐
│              │                            │              │
│   PANOUL     │                            │   PANOUL     │
│   DIN        │        CANVAS              │   DIN        │
│   STÂNGA     │      (pânza infinită)      │   DREAPTA    │
│              │                            │              │
│  Layers      │    ┌──────────────┐        │  Poziție     │
│  Pages       │    │              │        │  Mărime      │
│  Assets      │    │    Frame     │        │  Umplere     │
│              │    │              │        │  Contur      │
│              │    └──────────────┘        │  Efecte      │
│              │                            │              │
└──────────────┴────────────────────────────┴──────────────┘
```

**Panoul din stânga** — lista straturilor (**Layers**). Tot ce desenezi apare aici, cel mai nou sus. Aici selectezi, redenumești, grupezi și ascunzi elemente.

**Canvas-ul** — pânza infinită. Te miști pe ea cu rotița mouse-ului (sau două degete pe trackpad) și dai zoom cu ++ctrl++ + rotiță.

**Panoul din dreapta** — proprietățile elementului selectat: unde e, cât e de mare, ce culoare are. Când nu ai nimic selectat, îți arată proprietățile paginii.

---

## Frame-ul: pânza ta reală

Canvas-ul Figma e infinit, dar un afiș nu e infinit. **Frame-ul** este dreptunghiul care reprezintă formatul final: o pagină A3, un ecran de telefon, o postare pătrată.

Creează un frame cu tasta ++f++. În panoul din dreapta apare o listă de formate gata definite:

| Categorie | Formate utile |
|-----------|---------------|
| **Phone** | iPhone 14 — 390 × 844 px |
| **Desktop** | Desktop — 1440 × 1024 px |
| **Paper** | A4 — 595 × 842 pt, A3 — 842 × 1191 pt |
| **Social media** | Instagram post — 1080 × 1080 px, Story — 1080 × 1920 px |

!!! note "Regula de aur"
    **Desenezi întotdeauna în interiorul unui frame**, niciodată direct pe canvas. Un element din afara frame-ului nu poate fi exportat corect și nu apare în prototip.

Un frame poate conține alte frame-uri. Vei folosi asta constant: un frame „Card” în interiorul unui frame „Pagină”.

---

## Uneltele de bază

Bara de sus ține uneltele. Fiecare are o scurtătură — învață-le acum, îți salvează ore.

| Unealtă | Tastă | Ce face |
|---------|-------|---------|
| Move | ++v++ | Selectează și mută |
| Frame | ++f++ | Creează un frame |
| Rectangle | ++r++ | Dreptunghi |
| Ellipse | ++o++ | Cerc / elipsă |
| Line | ++l++ | Linie |
| Pen | ++p++ | Formă vectorială liberă (lecția 07) |
| Text | ++t++ | Text |
| Hand | ++h++ sau ++space++ | Mută pânza |
| Comment | ++c++ | Adaugă un comentariu |

### Scurtături pe care le vei folosi zilnic

| Acțiune | Windows / Linux | macOS |
|---------|-----------------|-------|
| Duplică selecția | ++ctrl+d++ | ++cmd+d++ |
| Grupează | ++ctrl+g++ | ++cmd+g++ |
| Pune într-un frame | ++ctrl+alt+g++ | ++cmd+option+g++ |
| Zoom la selecție | ++shift+2++ | ++shift+2++ |
| Zoom la tot | ++shift+1++ | ++shift+1++ |
| Zoom 100% | ++shift+0++ | ++shift+0++ |
| Blochează elementul | ++ctrl+shift+l++ | ++cmd+shift+l++ |
| Anulează | ++ctrl+z++ | ++cmd+z++ |

!!! tip "Trei scurtături care schimbă tot"
    - ++shift++ în timp ce desenezi un dreptunghi → **pătrat perfect**; pe elipsă → **cerc perfect**; pe linie → unghiuri de 45°.
    - ++alt++ (++option++ pe Mac) în timp ce tragi un element → îl **duplică**.
    - ++alt++ apăsat cu un element selectat și mouse-ul peste altul → îți arată **distanța** dintre ele în pixeli. Îl vei folosi în fiecare lecție despre spațiere.

---

## Primul tău fișier: un card de prezentare

Hai să facem ceva concret. Un card 400 × 250 px cu numele tău.

1. Apasă ++f++, iar în panoul din dreapta scrie manual **W: 400**, **H: 250**. Frame-ul apare pe canvas.
2. Dublu-click pe numele lui în panoul din stânga și redenumește-l `Card`.
3. Cu frame-ul selectat, în panoul din dreapta la **Fill** apasă pe pătratul de culoare și scrie codul `1F2937`. Fundalul devine gri închis.
4. Apasă ++t++, trage o casetă de text în interiorul cardului și scrie numele tău.
5. În panoul din dreapta setează: font **Inter**, **Semi Bold**, mărime **28**, culoare `FFFFFF`.
6. Apasă din nou ++t++, scrie dedesubt „elev, cercul de informatică”, mărime **14**, culoare `9CA3AF`.
7. Selectează ambele texte (++shift++ + click) și, în panoul din dreapta, apasă butonul de aliniere **Align left**.

!!! note "Ce ai făcut de fapt"
    Ai aplicat trei principii fără să le numești: **contrast** (28 pt vs. 14 pt, alb vs. gri), **proximitate** (cele două texte stau aproape, deci se citesc ca un bloc) și **aliniere** (aceeași margine stângă). Acestea sunt lecțiile 05 și 06, doar că le-ai făcut pe pilot automat.

---

## Salvare, versiuni, partajare

### Salvarea

**Figma salvează singur.** Nu există ++ctrl+s++ pentru conținut — fiecare modificare ajunge imediat în cloud. Numele fișierului se schimbă cu dublu-click pe el, sus.

### Istoricul versiunilor

Meniul **Figma → File → Show version history**. Vezi toate etapele fișierului și poți reveni la oricare.

!!! tip "Marchează etapele importante"
    În panoul de istoric apasă **+** și dă un nume versiunii: „varianta 1, înainte de feedback”. Peste două săptămâni vei ști exact la ce să te întorci.

### Partajarea

Butonul **Share**, sus-dreapta. Alege:

| Opțiune | Cine poate | Când o folosești |
|---------|-----------|------------------|
| **Anyone with the link → can view** | Oricine are link-ul, doar privește și comentează | Trimiți spre feedback |
| **Anyone with the link → can edit** | Oricine are link-ul poate modifica | Lucrezi în echipă la un proiect |
| **Only invited people** | Doar cine e invitat pe e-mail | Implicit; cel mai sigur |

!!! warning "Atenție la „can edit” public"
    Un link public cu drept de editare poate fi modificat de oricine îl are. Pentru feedback, trimite mereu **can view** — comentariile funcționează și așa, cu tasta ++c++.

---

## Interfața Canva pe scurt

Canva e mai simplu. Trei lucruri de știut:

1. **Căutarea de format.** Pe pagina principală scrii „Postare Instagram” sau „Afiș A3” și Canva creează pânza cu dimensiunea corectă.
2. **Panoul din stânga.** Tab-urile **Design** (șabloane), **Elemente** (forme, iconițe, ilustrații), **Text**, **Încărcări** (fișierele tale), **Proiecte**.
3. **Butonul Partajare → Descărcare.** Formatele: PNG (implicit), JPG, PDF Standard (ecran), PDF Print (tipar).

!!! tip "Pornește de la un șablon, dar schimbă-l serios"
    Dacă folosești un șablon Canva neatins, lucrarea ta va arăta ca alte zece mii. Regula pe care o folosim în lecția 13: **schimbă obligatoriu culorile și fonturile** cu cele din identitatea ta vizuală. Șablonul rămâne doar structură.

---

## Exerciții

### Exercițiu 1 — Trei frame-uri, trei formate
Într-un fișier Figma nou, creează trei frame-uri alăturate: un **A4** (portret), un **Instagram post** (1080 × 1080) și un **iPhone 14** (390 × 844). Redenumește-le corect în panoul Layers.

??? success "Soluție"
    - ++f++ → în panoul din dreapta, categoria **Paper** → **A4**.
    - ++f++ → **Social media** → **Instagram post**.
    - ++f++ → **Phone** → **iPhone 14**.

    Dacă frame-urile se suprapun, selectează-le pe toate (++ctrl+a++) și folosește butonul **Tidy up** din panoul din dreapta — le aliniază și le distanțează egal automat.

    Redenumirea se face cu dublu-click pe nume în Layers. Nume ca „Frame 1, Frame 2, Frame 3” par inofensive acum, dar într-un fișier cu 40 de straturi devin un coșmar.

### Exercițiu 2 — Pătrat perfect și cerc perfect
Desenează un pătrat de exact 200 × 200 px și un cerc de exact 200 × 200 px, unul lângă altul, la 40 px distanță. Verifică distanța cu ++alt++.

??? success "Soluție"
    - ++r++, apoi ține ++shift++ apăsat în timp ce tragi → pătrat. Corectează la 200 × 200 în panoul din dreapta.
    - ++o++, ++shift++ apăsat → cerc. La fel, 200 × 200.
    - Selectează pătratul, ține ++alt++ apăsat și plimbă mouse-ul peste cerc: Figma îți arată distanța cu roșu. Mută cercul până citești **40**.

    Alternativ: selectează ambele forme și, în panoul din dreapta, la **Auto layout** (++shift+a++) setează gap-ul la 40. Vei învăța asta pe larg în lecția 09.

### Exercițiu 3 — Partajează pentru comentarii
Partajează fișierul din exercițiul 1 cu un coleg, cu drept de **view**, și cere-i să lase un comentariu cu tasta ++c++ pe frame-ul A4.

??? success "Soluție"
    - **Share** → **Anyone with the link** → **can view** → **Copy link**.
    - Colegul deschide link-ul, apasă ++c++, dă click pe frame și scrie comentariul.
    - Comentariile apar ca bule pe canvas și în panoul de comentarii (iconița de mesaj, sus-dreapta). Le rezolvi cu **Resolve** după ce ai făcut modificarea.

    Observă că, deși colegul nu poate edita, poate comenta. Asta e exact ce vrei la feedback.

---

## Mini-proiect: cardul tău de membru

Construiește un card de membru al cercului de informatică, **400 × 250 px**, care să conțină: numele tău, clasa, rolul în cerc și un element grafic (un cerc sau un dreptunghi colorat) folosit ca accent.

??? success "Soluție"
    Un rezultat care funcționează:

    1. Frame `Card membru`, 400 × 250, Fill `0F172A`.
    2. Un dreptunghi de 6 × 250 px pe marginea stângă, Fill `F97316` — bara de accent. Se face cu ++r++, apoi X: 0, Y: 0, W: 6, H: 250.
    3. Text `Ana Popescu` — Inter Semi Bold 26, alb, poziționat la X: 32, Y: 48.
    4. Text `Clasa a IX-a B` — Inter Regular 14, culoare `94A3B8`, la 8 px sub nume.
    5. Text `Coordonator proiecte ESP32` — Inter Medium 13, culoare `F97316`, la 20 px mai jos.
    6. Toate cele trei texte aliniate la stânga, pe aceeași coordonată X: 32.

    **De ce funcționează:** un singur accent de culoare (portocaliul), folosit de două ori — bara și rolul — leagă vizual cardul. Cele trei mărimi de text (26 / 14 / 13) creează ierarhie clară: numele primul, restul după. Marginea de 32 px pe stânga și 48 px sus dă cardului aer.

    **Greșeli frecvente:** text lipit de marginea frame-ului (lasă minimum 24 px), trei culori de accent în loc de una, texte aliniate „aproximativ” în loc de exact pe aceeași coordonată X.

---

## Rezumat

- **Figma** pentru control și construcție; **Canva** pentru viteză și șabloane.
- Ambele au planuri **gratuite** suficiente pentru curs; cu e-mail de școală poți cere **Education**.
- Desenezi **întotdeauna într-un frame** (++f++), niciodată pe canvas gol.
- Scurtături esențiale: ++v++ ++f++ ++r++ ++o++ ++t++, ++shift++ pentru forme perfecte, ++alt++ pentru duplicare și pentru măsurarea distanțelor.
- Figma **salvează automat**; etapele importante se marchează în **version history**.
- Pentru feedback, partajezi cu **can view** — comentariile funcționează cu ++c++.
- Un șablon Canva nemodificat arată ca al tuturor; schimbă-i culorile și fonturile.

---

**Pasul următor:** [→ Lecția 02: Formă, linie, spațiu](02-forma-linie-spatiu.md)
