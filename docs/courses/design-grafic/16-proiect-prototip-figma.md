---
lesson: 16
tags: [proiect final, prototip, figma, interacțiune, smart animate, testare]
summary: Proiect final — un landing page interactiv în Figma, cu ecrane legate, stări, tranziții și o sesiune reală de testare cu utilizatori.
---

# Lecția 16 · Proiect: prototip interactiv de landing page

!!! tip "Ce vei construi"
    Un **landing page funcțional ca prototip**, pe care oricine îl poate deschide pe telefon și parcurge:

    - Ecranele pentru telefon și desktop, construite din biblioteca ta
    - Navigație reală: click pe meniu, scroll, deschidere de secțiuni
    - Stări interactive: hover, focus, apăsat
    - Un formular cu validare simulată și ecran de confirmare
    - Tranziții cu **Smart Animate**
    - O **sesiune de testare** cu trei persoane și lista de corecții rezultată

---

## Ce este un prototip și la ce folosește

Un prototip **nu este un site**. Nu are cod, nu salvează date, nu funcționează offline. Este o simulare — suficient de convingătoare încât cineva să o poată folosi și să îți spună unde se blochează.

De ce merită efortul:

| Beneficiu | Explicație |
|-----------|------------|
| **Testezi înainte să construiești** | O problemă de flux găsită în prototip costă 10 minute; găsită în cod, costă o zi |
| **Explici fără cuvinte** | Un link de prototip înlocuiește o discuție de 20 de minute |
| **Vezi ritmul real** | Un design static nu îți arată dacă un flux are prea mulți pași |
| **Primești feedback concret** | Oamenii comentează altfel când pot apăsa, nu doar privi |

---

## Pregătirea

### Ce trebuie să ai deja

- Biblioteca de componente din lecția 08, cu **toate stările** desenate (lecția 14).
- Identitatea vizuală din lecția 15.
- Fluxul scris în cuvinte.

### Fluxul pentru acest proiect

> 1. Vizitatorul deschide landing page-ul → vede secțiunea de întâmpinare
> 2. Derulează → vede ce face cercul, proiectele, programul
> 3. Apasă „Înscrie-te” (din meniu sau din pagină) → ajunge la formular
> 4. Completează câmpurile → apasă „Trimite”
> 5. Vede ecranul de confirmare
> 6. (alternativ) Trimite cu un câmp gol → vede starea de eroare

Șase pași, iar pasul 6 este cel pe care majoritatea îl uită.

### Ecranele necesare

| # | Ecran | De ce |
|---|-------|-------|
| 1 | Landing complet (scroll) | Pagina principală |
| 2 | Landing cu meniu mobil deschis | Starea navigației |
| 3 | Formular gol | Punctul de intrare |
| 4 | Formular cu eroare | Validare |
| 5 | Formular completat | Înainte de trimitere |
| 6 | Confirmare | Finalul fluxului |

Șase frame-uri pentru telefon. Pentru desktop, ecranele 2 și 3 se combină (meniul e mereu vizibil, formularul e o secțiune a paginii), deci patru frame-uri.

---

## Construirea ecranelor

### Secțiunile landing page-ului

| Secțiune | Conținut | Înălțime tipică (mobil) |
|----------|----------|-------------------------|
| **Navigație** | Logo + hamburger | 64 px, fixă sus |
| **Hero** | Titlu, o propoziție, buton principal | 480 px |
| **Ce facem** | 3 carduri cu pictogramă + text | 640 px |
| **Proiecte** | 3 carduri cu imagine | 900 px |
| **Program** | Ziua, ora, sala | 280 px |
| **Înscriere** | Buton mare către formular | 240 px |
| **Footer** | Logo, link-uri, contact | 320 px |

Totalul depășește înălțimea ecranului (844 px) — normal, pagina se derulează.

!!! tip "Cum faci scroll într-un prototip Figma"
    1. Frame-ul ecranului rămâne la **390 × 844** (dimensiunea telefonului).
    2. Conținutul din interior e mai înalt — de exemplu 3200 px.
    3. Selectează frame-ul → panoul din dreapta → **Clip content** bifat.
    4. Selectează conținutul interior → în tab-ul **Prototype**, setează **Overflow behavior: Vertical scrolling**.

    Acum, în modul de prezentare, pagina se derulează ca una reală.

### Elemente fixe la derulare

Navigația trebuie să rămână sus când derulezi.

1. Selectează frame-ul navigației.
2. În tab-ul **Prototype**, bifează **Fix position when scrolling**.

Același lucru pentru un buton flotant, dacă ai unul.

---

## Legarea ecranelor

### Conexiunile de bază

1. Comută în tab-ul **Prototype** (dreapta-sus).
2. Selectează elementul pe care se apasă (butonul, nu textul din el).
3. Trage de cerculețul albastru de pe marginea lui până pe frame-ul destinație.
4. În panoul care apare, setează declanșatorul și animația.

### Declanșatoarele

| Declanșator | Când se activează | Folosire |
|-------------|-------------------|----------|
| **On click / tap** | La apăsare | Butoane, link-uri |
| **While hovering** | Cât timp mouse-ul e deasupra | Stări hover pe desktop |
| **While pressing** | Cât timp e ținut apăsat | Starea active |
| **Key / gamepad** | La o tastă | Navigație cu tastatura |
| **After delay** | După un timp | Ecrane de încărcare, tranziții automate |

### Animațiile

| Animație | Efect | Când |
|----------|-------|------|
| **Instant** | Fără tranziție | Schimbări de stare rapide |
| **Dissolve** | Fade | Modale, confirmări |
| **Move in / out** | Intră peste ecranul curent | Meniuri laterale, panouri |
| **Push** | Împinge ecranul curent | Navigație între pagini |
| **Slide in / out** | Alunecă peste | Foi de jos (bottom sheets) |
| **Smart animate** | Interpolează automat elementele cu **același nume** | Tranziții fluide |

!!! warning "Durata contează mai mult decât tipul"
    | Durată | Senzație |
    |--------|----------|
    | < 100 ms | Pare instantaneu |
    | **150–300 ms** | Intervalul corect pentru majoritatea tranzițiilor |
    | 400–600 ms | Se simte lent |
    | > 700 ms | Enervant; utilizatorul apasă din nou crezând că nu a mers |

    Implicit, Figma pune 300 ms. Pentru schimbări mici (hover, apăsare), coboară la **150 ms**.

---

## Smart Animate

Este singura animație care necesită explicație.

**Cum funcționează:** Figma compară elementele din cele două frame-uri și interpolează automat tot ce are **exact același nume de strat**. Poziție, mărime, culoare, opacitate, rotație.

### Condiția obligatorie

Straturile trebuie să aibă **numele identice** în ambele frame-uri. Dacă în primul frame butonul se numește `cta-button` și în al doilea `Rectangle 43`, Smart Animate nu le va lega — va face un fade.

!!! tip "Fluxul corect de lucru"
    Nu construi al doilea ecran de la zero. **Duplică primul** (++ctrl+d++), apoi modifică ce trebuie. Astfel numele straturilor rămân identice automat.

### Ce poți face cu el

| Efect | Cum |
|-------|-----|
| Card care se extinde | Același card, mărime diferită în al doilea frame |
| Meniu care alunecă | Același panou, poziție X diferită |
| Buton care își schimbă culoarea | Același buton, Fill diferit |
| Element care se mută între secțiuni | Același nume, poziție diferită |

!!! note "Curbele de accelerație"
    Lângă durată, Figma are un meniu de easing:

    - **Ease out** — rapid la început, încetinește la final. Cea mai naturală pentru elemente care **apar**.
    - **Ease in** — invers. Pentru elemente care **dispar**.
    - **Ease in and out** — pentru mișcări între două poziții.
    - **Linear** — viteză constantă. Arată mecanic; evită-l, cu excepția indicatorilor de progres.

---

## Interacțiuni în componente

Un buton cu variante (lecția 08) poate avea interacțiunile **înăuntrul componentei**, nu pe fiecare instanță.

1. Intră în setul de variante.
2. Selectează varianta `State: default`.
3. În tab-ul Prototype, trage o conexiune către varianta `State: hover`.
4. Declanșator: **While hovering**. Animație: Instant sau Dissolve 100 ms.
5. Adaugă conexiunea inversă (de la hover la default se face automat).

Rezultat: **toate instanțele butonului** din tot prototipul reacționează la hover. Nu mai trebuie să legi nimic manual.

!!! tip "Fă la fel pentru câmpurile de formular"
    Varianta `default` → `focus` la declanșatorul **On click**. Prototipul tău va simula corect completarea unui formular.

---

## Testarea cu utilizatori

Aceasta e partea pe care o sar toți și care aduce cel mai mult.

### Pregătirea

1. **Share → can view → Copy link**, apoi adaugă `&scaling=scale-down` la link ca să se potrivească pe ecranul persoanei.
2. Pregătește **o singură sarcină**, formulată ca obiectiv, nu ca instrucțiune.

| Formulare bună | Formulare proastă |
|----------------|-------------------|
| „Vrei să te înscrii la cerc. Arată-mi cum ai face.” | „Apasă butonul Înscrie-te din meniu.” |
| „Află când se țin întâlnirile.” | „Derulează până la secțiunea Program.” |

### În timpul testului

| Regulă | De ce |
|--------|-------|
| **Nu ajuta** | Momentul în care persoana se blochează e exact informația de care ai nevoie |
| **Nu explica designul** | Utilizatorii reali nu vor avea un designer lângă ei |
| **Cere gândire cu voce tare** | „Spune-mi la ce te uiți și ce cauți” |
| **Notează, nu discuta** | Discuția vine după |
| **Cronometrează** | Câte secunde până găsește butonul de înscriere? |

!!! warning "Trei persoane sunt suficiente"
    Nu ai nevoie de un eșantion statistic. Cercetarea de uzabilitate arată că **3–5 persoane** descoperă majoritatea problemelor majore. Dacă toate trei se blochează în același loc, ai găsit o problemă reală, nu o preferință.

### Ce notezi

| Coloană | Exemplu |
|---------|---------|
| Ce a făcut | „A derulat de trei ori sus-jos înainte să găsească butonul” |
| Unde s-a blocat | „Nu a văzut link-ul Înscriere din meniu” |
| Ce a spus | „Credeam că trebuie să scriu un e-mail” |
| Cât a durat | „38 de secunde până la formular” |

### Din observații în corecții

| Observație | Diagnostic | Corecție |
|------------|-----------|----------|
| Toți trei au ratat butonul din hero | Contrast sau poziție insuficientă | Mută-l mai sus, fă-l singurul element colorat |
| Doi au încercat să apese pe carduri | Cardurile par interactive | Fie le faci interactive, fie scoți efectul de hover |
| Unul a completat greșit câmpul de clasă | Eticheta e ambiguă | Schimbă „Clasa” în „Clasa (ex: IX B)” |
| Toți au ezitat la butonul „Trimite” | Nu e clar ce se întâmplă după | Adaugă sub buton: „Primești confirmare pe e-mail” |

---

## Exerciții

### Exercițiu 1 — Meniu mobil cu Smart Animate
Construiește două frame-uri — landing cu meniu închis și landing cu meniu deschis — și leagă-le cu Smart Animate, astfel încât panoul să alunece de sus.

??? success "Soluție"
    1. Construiește frame-ul `landing-mobile`.
    2. ++ctrl+d++ → redenumește copia `landing-mobile-menu`.
    3. În copie, adaugă un frame `menu-panel` de 390 × 480, poziționat la Y = 64 (sub navigație), cu cele 4 link-uri.
    4. În **frame-ul original**, adaugă **același** `menu-panel`, cu numele identic, dar poziționat la **Y = −480** (în afara ecranului, deasupra) și cu opacitatea 0.
    5. Leagă hamburger-ul din ecranul 1 → ecranul 2. Animație: **Smart animate**, **Ease out**, **250 ms**.
    6. Leagă butonul X din ecranul 2 → ecranul 1, cu aceleași setări.

    **De ce funcționează:** `menu-panel` are același nume în ambele frame-uri, deci Smart Animate interpolează poziția Y de la −480 la 64 și opacitatea de la 0 la 1. Rezultă o alunecare fluidă.

    **Dacă nu funcționează:** verifică numele. În 9 cazuri din 10, unul dintre frame-uri are `Frame 27` în loc de `menu-panel`.

### Exercițiu 2 — Formular cu validare simulată
Construiește fluxul complet al formularului: gol → focus pe câmp → completat → eroare → confirmare.

??? success "Soluție"
    **Frame-urile necesare:**

    | Frame | Stare |
    |-------|-------|
    | `form-empty` | Toate câmpurile goale, butonul activ |
    | `form-focus` | Primul câmp în starea focus |
    | `form-filled` | Toate câmpurile completate |
    | `form-error` | Câmpul de e-mail gol + contur roșu + mesaj |
    | `form-success` | Ecran de confirmare cu pictogramă și text |

    **Conexiunile:**

    | De la | Element | Declanșator | Către | Animație |
    |-------|---------|-------------|-------|----------|
    | `form-empty` | câmp nume | On click | `form-focus` | Instant |
    | `form-focus` | câmp nume | On click | `form-filled` | Instant |
    | `form-filled` | buton Trimite | On click | `form-success` | Dissolve 200 ms |
    | `form-empty` | buton Trimite | On click | `form-error` | Instant |
    | `form-error` | câmp e-mail | On click | `form-filled` | Instant |
    | `form-success` | buton Închide | On click | `landing-mobile` | Push 250 ms |

    **Observația importantă:** conexiunea de la `form-empty` direct la `form-error` simulează utilizatorul care apasă Trimite fără să completeze nimic. Acesta e cazul pe care majoritatea prototipurilor îl omit — și exact cel care apare cel mai des în realitate.

### Exercițiu 3 — Sesiune de testare
Testează prototipul cu trei persoane care nu au văzut proiectul. Notează observațiile în tabelul de mai sus și produ o listă de corecții prioritizate.

??? success "Soluție"
    **Exemplu de raport:**

    | Persoană | Sarcina | Timp | Unde s-a blocat |
    |----------|---------|------|-----------------|
    | A | Înscriere | 42 s | A căutat butonul în footer |
    | B | Înscriere | 28 s | A ratat butonul din hero, l-a găsit în meniu |
    | C | Înscriere | 51 s | A derulat toată pagina de două ori |

    **Diagnosticul:** toate trei au avut dificultăți cu același lucru — butonul principal de înscriere din hero nu se vede. Media de 40 de secunde pentru acțiunea principală a paginii este foarte proastă; ținta e sub 10 secunde.

    **Lista de corecții, prioritizată:**

    | # | Corecție | Impact | Efort |
    |---|----------|--------|-------|
    | 1 | Butonul din hero devine singurul element colorat de pe primul ecran | Mare | Mic |
    | 2 | Mută butonul cu 80 px mai sus, ca să fie vizibil fără derulare | Mare | Mic |
    | 3 | Adaugă un buton fix jos, vizibil la derulare | Mediu | Mediu |
    | 4 | Schimbă textul din „Înscrie-te” în „Vino joi la 15:00” | Mediu | Mic |
    | 5 | Scoate efectul de hover de pe carduri (induce în eroare) | Mic | Mic |

    **După corecții, retestează cu alte trei persoane.** Dacă timpul mediu scade sub 15 secunde, corecțiile au funcționat.

    !!! note "De ce se retestează cu alte persoane"
        Cine a văzut deja prototipul știe unde e butonul. A doua încercare a aceleiași persoane nu îți spune nimic despre design, îți spune despre memoria ei.

---

## Mini-proiect: landing page complet, testat și corectat

Construiește prototipul complet pentru cercul tău, testează-l cu trei persoane și livrează versiunea corectată, împreună cu raportul de testare.

??? success "Livrabilele și criteriile"
    **Livrabilele:**

    | Livrabil | Conținut |
    |----------|----------|
    | Link-ul prototipului mobil | 6 ecrane legate, scroll funcțional |
    | Link-ul prototipului desktop | 4 ecrane legate |
    | Raportul de testare | Tabelul cu 3 persoane + lista de corecții prioritizate |
    | Versiunea v2 | Prototipul după corecții |
    | Fișierul Figma | Cu pagini separate: `v1`, `Testing notes`, `v2` |

    **Criteriile de evaluare:**

    | # | Criteriu | Verificare |
    |---|----------|-----------|
    | 1 | Scroll funcțional | Deschide pe telefon și derulează |
    | 2 | Navigația rămâne fixă la derulare | Idem |
    | 3 | Toate butoanele duc undeva | Apasă pe fiecare; niciunul nu e „mort” |
    | 4 | Stările hover și focus sunt în componente | Verifică o instanță oarecare |
    | 5 | Fluxul de eroare există | Trimite formularul gol |
    | 6 | Se poate reveni din orice ecran | Există buton de înapoi sau închide |
    | 7 | Tranzițiile sunt 150–300 ms | Verifică fiecare conexiune |
    | 8 | Smart Animate funcționează | Meniul alunecă, nu face fade |
    | 9 | Raport de testare cu 3 persoane | Tabelul complet |
    | 10 | v2 rezolvă cel puțin primele 3 corecții | Compară v1 cu v2 |

    **Testul „butonului mort”:** parcurge prototipul ca un utilizator obișnuit și apasă pe **fiecare** element care pare interactiv. Orice buton care nu duce nicăieri e o problemă — fie îl legi, fie îl faci să nu mai arate apăsabil.

    **Testul telefonului real:** deschide link-ul pe telefonul tău, nu în browser pe laptop. Zonele de atingere, mărimea textului și fluiditatea derulării se simt complet diferit.

---

## Ai terminat cursul

Ai parcurs drumul complet: de la ce înseamnă o decizie de design (lecția 00), prin limbajul vizual și instrumentele Figma, până la o identitate vizuală completă și un prototip testat cu utilizatori reali.

**Ce ai acum:**

- Un vocabular: ierarhie, contrast, grilă, componentă, stare, breakpoint.
- Un proces: brief → conținut → structură → aspect → verificare → testare.
- Un portofoliu: afiș, logo, identitate vizuală, prototip.
- Obiceiuri de verificare: blur, contrast, alb-negru, 3 secunde, test cu utilizatori.

**Unde continui:**

| Direcție | Primul pas |
|----------|-----------|
| **Construiește ce ai desenat** | [Cursul de dezvoltare web](../web/index.md) — HTML, CSS, JavaScript |
| **Design pentru proiecte fizice** | [Proiectele de electronică](../../projects/index.md) — interfețe pentru ESP32, etichete, panouri |
| **Aprofundează tipografia** | Desenează 10 afișe folosind **un singur font** |
| **Aprofundează UI** | Reconstruiește interfața unei aplicații pe care o folosești zilnic |

!!! tip "Ultimul sfat"
    Designul nu se învață citind, ci făcând și primind feedback. Cel mai util lucru pe care îl poți face de acum înainte: **publică**. Pune afișele pe hol, postează pe pagina cercului, dă prototipul colegilor.

    Un design văzut de 100 de oameni te învață mai mult decât zece designuri pe care nu le vede nimeni.

---

## Rezumat

- Un **prototip** e o simulare, nu un site — dar e suficient ca să testezi fluxul.
- Scroll: frame la dimensiunea ecranului + `Clip content` + `Vertical scrolling` pe conținut.
- `Fix position when scrolling` pentru navigație și butoane flotante.
- Declanșatoare: **on click, while hovering, while pressing, after delay**.
- Durata corectă a tranzițiilor: **150–300 ms**. Peste 700 ms devine enervant.
- **Smart Animate** cere **nume de straturi identice** în ambele frame-uri — duplică, nu reconstrui.
- Pune interacțiunile **în componente**, nu pe fiecare instanță.
- **Trei persoane** descoperă majoritatea problemelor de uzabilitate.
- Formulează sarcini ca **obiective**, nu ca instrucțiuni; nu ajuta în timpul testului.
- Retestează **cu alte persoane**, nu cu aceleași.

---

**Înapoi la:** [harta cursului](index.md)
