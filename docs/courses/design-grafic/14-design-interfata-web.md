---
lesson: 14
tags: [ui, ux, wireframe, mockup, responsive, handoff]
summary: De la wireframe la mockup, componente de interfață, design responsive și ce predai mai departe către HTML și CSS.
---

# Lecția 14 · Design de interfață web

!!! tip "Ce vei învăța"
    - Diferența dintre **UX** și **UI**, fără jargon
    - **Wireframe** → **mockup** → **prototip**: ce se face în fiecare etapă
    - Componentele standard de interfață și **stările** lor
    - **Design responsive**: mobile-first, breakpoint-uri, ce se schimbă
    - Accesibilitate în interfețe: contrast, zonă de atingere, focus
    - **Handoff**: ce primește programatorul de la tine

---

## UX și UI

| | UX (User Experience) | UI (User Interface) |
|---|----------------------|---------------------|
| **Întrebarea** | Ce trebuie să poată face utilizatorul și în ce ordine? | Cum arată și cum se comportă fiecare element? |
| **Livrabile** | Fluxuri, hărți de ecrane, wireframe-uri | Mockup-uri, componente, stiluri, prototip |
| **Se greșește când** | Fluxul are 7 pași în loc de 3 | Butonul e frumos, dar nu se vede |

Ambele contează. Un UI perfect pe un UX prost dă o aplicație frumoasă pe care nimeni nu o folosește.

!!! note "Regula de start"
    Înainte să desenezi un singur ecran, scrie **fluxul** în cuvinte:

    > Un elev vrea să se înscrie la cerc.
    > 1. Intră pe site → vede pagina principală
    > 2. Apasă „Înscrie-te” → vede formularul
    > 3. Completează nume, clasă, e-mail → apasă „Trimite”
    > 4. Vede confirmarea

    Patru pași, patru ecrane. Acum știi exact ce ai de desenat.

---

## Wireframe, mockup, prototip

### Wireframe — structura

Gri, fără culori, fără fotografii, fără fonturi definitive. Doar dreptunghiuri și text de poziționare.

**Scopul:** decizi **ce** e pe ecran și **unde**, fără să te distragă aspectul.

| Convenție | Ce înseamnă |
|-----------|-------------|
| Dreptunghi cu X în diagonală | Imagine |
| Linii orizontale gri | Bloc de text |
| Dreptunghi cu rază + text centrat | Buton |
| Dreptunghi cu contur + text gri | Câmp de formular |

!!! tip "Wireframe-ul se face în 15 minute, nu în 2 ore"
    Dacă petreci mult timp pe un wireframe, îl faci prea detaliat. Scopul lui e să fie **aruncat** — dacă structura nu funcționează, refaci wireframe-ul în 10 minute, nu mockup-ul în 3 ore.

### Mockup — aspectul

Wireframe-ul + culori, tipografie, imagini, spațiere reală. Arată ca produsul final, dar nu face nimic.

### Prototip — comportamentul

Mockup-urile legate între ele, cu tranziții. Se poate apăsa și naviga. Îl construim în lecția 16.

---

## Grila și breakpoint-urile

### Mobile-first

Desenezi **întâi pentru telefon**, apoi extinzi. Motivele:

1. Peste 60% din traficul web e de pe telefon.
2. Telefonul e constrângerea cea mai dură — dacă încape acolo, încape oriunde.
3. Extinderea e mai ușoară decât comprimarea. Un design de desktop redus la telefon devine aproape întotdeauna aglomerat.

### Breakpoint-uri standard

| Dispozitiv | Lățime frame | Coloane | Margine | Gutter |
|------------|--------------|---------|---------|--------|
| **Telefon** | 390 px | 4 | 16 | 16 |
| **Tabletă** | 768 px | 8 | 32 | 24 |
| **Desktop** | 1440 px | 12 | 96 | 24 |

!!! note "Ce se schimbă la fiecare breakpoint"
    | Element | Telefon | Desktop |
    |---------|---------|---------|
    | Navigația | Meniu hamburger | Link-uri orizontale vizibile |
    | Coloanele de conținut | 1 | 2–3 |
    | Carduri | Una sub alta | Grilă de 3 |
    | Corpul textului | 16 px | 16–18 px |
    | Titlul principal | 32 px | 48–64 px |
    | Marginile | 16 px | 96 px |

---

## Componentele de interfață și stările lor

Un element de interfață **nu este o imagine**. Are stări, și fiecare trebuie desenată.

### Stările obligatorii

| Stare | Când apare | Ce se schimbă tipic |
|-------|------------|---------------------|
| **Default** | Normal | — |
| **Hover** | Mouse-ul deasupra (doar pe desktop) | Fundal mai închis / mai deschis |
| **Focus** | Selectat cu ++tab++ | **Contur vizibil** de 2–3 px |
| **Active / pressed** | În timpul apăsării | Puțin mai închis, uneori ușor micșorat |
| **Disabled** | Indisponibil | Opacitate redusă, fără cursor de mână |
| **Loading** | Așteaptă răspuns | Indicator, text schimbat |

!!! warning "Starea de focus nu este opțională"
    Mulți oameni navighează cu tastatura — din obișnuință, din viteză, sau pentru că nu pot folosi un mouse. Dacă ștergi conturul de focus („arată urât”), aceste persoane nu mai pot folosi site-ul deloc.

    Conturul de focus se **desenează deliberat**, în culoarea de brand, cu 2–3 px grosime și 2 px offset. Nu se șterge.

### Componentele de bază

| Componentă | Ce trebuie desenat |
|------------|--------------------|
| **Buton** | 3 tipuri (primar, secundar, ghost) × 5 stări |
| **Câmp de text** | default, focus, completat, eroare, dezactivat + etichetă + mesaj de eroare |
| **Card** | Cu și fără imagine, cu și fără acțiune |
| **Navigație** | Desktop și mobil, cu starea „pagina curentă” |
| **Mesaj de sistem** | Succes, avertisment, eroare, informație |

### Zona de atingere

Pe telefon, orice element pe care se apasă trebuie să aibă minimum **44 × 44 px** de zonă activă — indiferent cât de mică e pictograma din el.

```
    ┌──────────────┐
    │   ┌──────┐   │   ← zona activă: 44 × 44
    │   │ icon │   │   ← pictograma: 24 × 24
    │   │24×24 │   │
    │   └──────┘   │
    └──────────────┘
```

!!! warning "Greșeala clasică"
    Un buton de „închide” desenat ca un X de 16 px, fără padding. Pe telefon e aproape imposibil de apăsat. Adaugă padding până la 44 × 44, chiar dacă zona în plus e transparentă.

---

## Accesibilitate în interfețe

Pe lângă contrastul din lecția 03:

| Cerință | Regula |
|---------|--------|
| Contrast text | 4.5:1 normal, 3:1 pentru text ≥ 24 px |
| Contrast elemente interactive | **3:1** pentru contururi de câmpuri, pictograme funcționale |
| Zonă de atingere | Minimum 44 × 44 px |
| Focus vizibil | Contur de minimum 2 px, contrast 3:1 față de fundal |
| Etichete de formular | **Deasupra** câmpului, niciodată doar placeholder |
| Erori | Text explicit, nu doar contur roșu |
| Corp text | Minimum 16 px pe mobil (sub 16 px, iOS dă zoom automat) |

!!! note "De ce placeholder-ul nu ține loc de etichetă"
    Dacă singura indicație „Nume” e placeholder-ul din câmp, ea **dispare** când utilizatorul începe să scrie. Cine se întrerupe și revine nu mai știe ce completa. Eticheta stă deasupra și rămâne.

---

## Handoff — ce predai programatorului

Un design predat prost costă mai mult timp decât ar fi durat să fie făcut bine.

### Ce primește programatorul

| Livrabil | Conținut |
|----------|----------|
| **Link-ul Figma** cu drept de view | Nu capturi de ecran |
| **Pagina Foundations** | Culori cu nume de stil, scara tipografică, sistemul de spațiere |
| **Componentele** cu toate stările | Nu doar starea default |
| **Ecranele** la cele 3 breakpoint-uri | Telefon, tabletă, desktop |
| **Assets exportate** | SVG-uri pentru pictograme și logo, imagini la 2× |
| **Note** | Ce se întâmplă la click, ce texte sunt dinamice, ce se întâmplă dacă lista e goală |

### Modul Dev Mode

Figma are un mod dedicat (comutatorul din dreapta-sus). Un dezvoltator cu acces vede:

- Dimensiuni, spațieri și culori în CSS, direct copiabile
- Numele stilurilor și componentelor
- Distanțele dintre elemente, măsurate automat
- Assets de descărcat

!!! tip "Auto Layout face jumătate din handoff"
    Un design construit cu Auto Layout (lecția 09) îi arată dezvoltatorului direct `display: flex; gap: 16px; padding: 24px`. Un design cu elemente poziționate manual îl obligă să măsoare și să ghicească.

### Cazurile pe care le uită toți

Desenează-le, chiar dacă par plictisitoare:

| Caz | Întrebarea |
|-----|-----------|
| **Stare goală** | Ce se vede când nu există niciun proiect încă? |
| **Text lung** | Ce se întâmplă cu un titlu de 15 cuvinte? Se rupe pe rânduri sau se taie cu `…`? |
| **Imagine lipsă** | Ce apare în locul ei? |
| **Eroare de rețea** | Ce vede utilizatorul? |
| **Încărcare** | Skeleton, spinner, sau nimic? |

---

## Exerciții

### Exercițiu 1 — Flux și wireframe
Scrie fluxul în cuvinte pentru „un vizitator vrea să vadă detaliile unui proiect al cercului”, apoi desenează wireframe-urile ecranelor, la 390 px lățime.

??? success "Soluție"
    **Fluxul:**
    > 1. Intră pe pagina principală → vede o listă de proiecte
    > 2. Apasă pe un proiect → vede pagina proiectului
    > 3. Derulează → vede descrierea, schema, codul
    > 4. (opțional) Apasă „Vezi pe GitHub” → pleacă de pe site

    Trei ecrane de desenat (al patrulea e extern).

    **Wireframe ecran 1 — lista:**
    ```
    ┌────────────────────┐
    │ ☰   Logo        🔍 │  ← header, 56 px
    ├────────────────────┤
    │ Proiecte           │  ← titlu pagină
    │                    │
    │ ┌────────────────┐ │
    │ │ ╲╱  Titlu      │ │  ← card: imagine + titlu + tag
    │ │ ╱╲  ▬▬▬▬ ▬▬    │ │
    │ └────────────────┘ │
    │ ┌────────────────┐ │
    │ │ ╲╱  Titlu      │ │
    │ │ ╱╲  ▬▬▬▬ ▬▬    │ │
    │ └────────────────┘ │
    └────────────────────┘
    ```

    **Ecran 2 — proiectul:** header cu buton „înapoi”, imagine mare, titlu, taguri, descriere, secțiune de cod, buton „Vezi pe GitHub”.

    **Ecran 3 = ecranul 2 derulat.** Nu e nevoie de un wireframe separat — notează doar „scroll”.

    **Verificarea:** poate cineva să parcurgă fluxul privind doar wireframe-urile, fără explicații de la tine? Dacă întreabă „și de aici unde ajung?”, lipsește un ecran sau un buton.

### Exercițiu 2 — Un câmp de formular, toate stările
Desenează un câmp de text cu etichetă, în toate cele șase stări obligatorii. Verifică contrastul la fiecare.

??? success "Soluție"
    Structura componentei (Auto Layout vertical, gap 6):
    - Etichetă: 13 px Medium, `text/base`
    - Câmp: înălțime 44 px, padding orizontal 16, rază 8, contur 1 px
    - Mesaj (opțional): 12 px Regular

    | Stare | Contur | Fundal | Text | Mesaj |
    |-------|--------|--------|------|-------|
    | Default | 1 px `#334155` | `#0F172A` | `text/muted` (placeholder) | — |
    | Hover | 1 px `#475569` | `#0F172A` | `text/muted` | — |
    | Focus | 2 px `brand/primary` + offset 2 px | `#0F172A` | `text/strong` | — |
    | Completat | 1 px `#334155` | `#0F172A` | `text/strong` | — |
    | Eroare | 2 px `feedback/error` | `#0F172A` | `text/strong` | `feedback/error`: „Adresa de e-mail nu este validă” |
    | Dezactivat | 1 px `#1E293B` | `#111827` | `text/muted` 50% | — |

    **Verificările:**
    - Conturul în starea default: `#334155` pe `#0F172A` → 2.1:1. **Cade** cerința de 3:1 pentru elemente interactive. Corecție: `#475569` → 3.4:1. Trece.
    - Textul de eroare: `#F87171` pe `#0F172A` → 6.8:1. Trece.
    - Înălțimea 44 px respectă zona minimă de atingere.

    **Greșeala pe care ai evitat-o:** starea de eroare marcată **doar** prin conturul roșu. Cu mesaj text, funcționează și pentru cine nu distinge roșul.

### Exercițiu 3 — Același ecran la trei lățimi
Ia ecranul de listă din exercițiul 1 și desenează-l la 390, 768 și 1440 px. Notează exact ce se schimbă la fiecare prag.

??? success "Soluție"
    | Element | 390 px | 768 px | 1440 px |
    |---------|--------|--------|---------|
    | Navigația | Hamburger | Hamburger | 4 link-uri orizontale + buton |
    | Marginea | 16 | 32 | 96 |
    | Coloane grilă | 4 | 8 | 12 |
    | Carduri pe rând | 1 | 2 | 3 |
    | Lățime card | Fill (358 px) | 4 coloane | 4 coloane |
    | Titlu pagină | 32 px | 40 px | 48 px |
    | Corp text | 16 px | 16 px | 16 px |
    | Imaginea din card | 16:9 | 16:9 | 16:9 |

    **Ce NU se schimbă:** paleta, fonturile, razele de colț, raportul imaginilor, înălțimea zonelor de atingere.

    **Observația importantă:** corpul textului rămâne 16 px la toate lățimile. Un text de 20 px pe desktop pare „prea mare” pentru majoritatea cititorilor. Ce se schimbă e **lungimea rândului**, controlată prin lățimea coloanei, nu prin mărimea literei.

    **Verificarea cu Auto Layout:** dacă ai construit cardurile pe `Fill` într-un container cu `Wrap`, trecerea de la 1 la 2 la 3 carduri pe rând se întâmplă **singură** când schimbi lățimea ecranului. Dacă a trebuit să le muți manual, structura nu e completă.

---

## Mini-proiect: pagina de proiect a cercului

Proiectează **trei ecrane** ale unei pagini web pentru cercul de informatică — pagina principală, lista de proiecte și pagina unui proiect — la toate cele trei breakpoint-uri, folosind identitatea vizuală din lecția 12.

??? success "Livrabilele și criteriile"
    **Structura fișierului Figma:**

    | Pagina | Conținut |
    |--------|----------|
    | `Flows` | Fluxul scris + harta ecranelor |
    | `Wireframes` | Cele 3 ecrane × 390 px, în gri |
    | `Components` | Buton, câmp, card, navigație, badge — toate cu stările lor |
    | `Screens` | 3 ecrane × 3 breakpoint-uri = 9 frame-uri |
    | `Handoff` | Note pentru dezvoltator, stări goale, cazuri limită |

    **Componentele minime, cu toate stările:**

    | Componentă | Stări / variante |
    |------------|------------------|
    | `button` | 3 tipuri × 5 stări |
    | `input` | 6 stări |
    | `card/project` | cu imagine / fără imagine |
    | `nav` | mobil (închis / deschis) + desktop |
    | `badge` | 3 categorii |

    **Cazurile limită de desenat:**
    - Lista de proiecte **goală** („Niciun proiect încă. Revino în curând.”)
    - Un titlu de proiect de 12 cuvinte
    - Un card fără imagine
    - Ecranul de eroare 404

    **Criteriile de evaluare:**

    | # | Criteriu | Verificare |
    |---|----------|-----------|
    | 1 | Fluxul e scris înainte de desen | Pagina `Flows` există |
    | 2 | Mobile-first | Wireframe-urile sunt la 390 px |
    | 3 | Toate stările desenate | Inclusiv focus și disabled |
    | 4 | Zone de atingere ≥ 44 px | Măsoară butoanele mici |
    | 5 | Contrast text ≥ 4.5:1, interactiv ≥ 3:1 | Plugin Contrast |
    | 6 | Etichete deasupra câmpurilor | Nu doar placeholder |
    | 7 | Tot e Auto Layout | Schimbă lățimea unui ecran — se adaptează? |
    | 8 | Un singur buton primar pe ecran | Numără |
    | 9 | Cazurile limită desenate | Cele 4 de mai sus |
    | 10 | Doar stiluri, zero HEX scris de mână | Verifică 10 elemente la întâmplare |

    **Legătura cu cursul Web:** ecranele pe care le-ai desenat aici se construiesc efectiv în HTML și CSS. Vezi [Flexbox și Grid](../web/08-css-flexbox-grid.md) pentru structură și [Responsive design](../web/10-css-responsive.md) pentru breakpoint-uri. Auto Layout-ul tău se traduce aproape rând cu rând.

---

## Rezumat

- **UX** = ce poate face utilizatorul; **UI** = cum arată și cum se comportă.
- Scrie **fluxul în cuvinte** înainte să desenezi un ecran.
- **Wireframe** (structură, gri, 15 minute) → **mockup** (aspect) → **prototip** (comportament).
- **Mobile-first**: 390 → 768 → 1440 px; 4 → 8 → 12 coloane.
- Fiecare componentă are **6 stări**: default, hover, focus, active, disabled, loading.
- **Conturul de focus nu se șterge niciodată.**
- Zona de atingere minimă: **44 × 44 px**.
- Contrast: **4.5:1** text, **3:1** elemente interactive.
- Eticheta stă **deasupra** câmpului; placeholder-ul nu ține loc de etichetă.
- Handoff = link Figma + componente cu stări + 3 breakpoint-uri + assets + **cazurile limită**.

---

**Pasul următor:** [→ Lecția 15: Identitate vizuală pentru cercul de informatică](15-proiect-identitate-vizuala.md)
