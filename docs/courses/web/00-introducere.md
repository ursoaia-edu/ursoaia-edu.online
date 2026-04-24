---
lesson: 0
tags: [web, internet, http, browser, devtools, client-server]
summary: Cum funcționează web-ul, diferența dintre Internet și Web, rolul browser-ului și instrumentele pe care le vei folosi.
---

# Lecția 00 · Cum funcționează web-ul

!!! tip "Ce vei învăța"
    - Diferența dintre **Internet** și **Web**
    - Modelul **client–server** și ce se întâmplă când deschizi un site
    - Cele **3 limbaje** ale web-ului: HTML, CSS, JavaScript
    - Instrumentele de lucru: **VS Code**, **Live Server**, **DevTools**
    - Cum să inspectezi orice pagină web cu `F12`

---

## Internetul vs. Web-ul

Mulți folosesc cuvintele „Internet” și „Web” ca și cum ar fi același lucru. **Nu sunt.**

- **Internetul** este rețeaua fizică globală de cabluri, routere, antene și servere care conectează miliarde de calculatoare.
- **Web-ul** (World Wide Web) este **stratul de informație** construit deasupra Internetului — site-urile, paginile, imaginile, videoclipurile pe care le vezi în browser.

!!! note "Analogie"
    **Internetul = autostrada.** Cablurile și routerele sunt asfaltul și indicatoarele.

    **Web-ul = mașinile care circulă** pe ea. Pagina pe care o citești acum este o „mașină” care a ajuns la tine prin autostradă.

    Pe Internet mai circulă și altceva: e-mail, jocuri online, apeluri video, actualizări de aplicații. Web-ul este doar **un tip** de trafic.

---

## Modelul client–server

Orice pagină web pe care o deschizi presupune **două părți** care comunică:

```
[CLIENT]                            [SERVER]
Chrome / Firefox / Edge       Un calculator puternic
(calculatorul tău)            (ex: serverele Google)

      |   1. Cerere (request)            |
      |   GET /index.html                |
      |  ------------------------------> |
      |                                  |
      |   2. Răspuns (response)          |
      |   200 OK + cod HTML              |
      |  <------------------------------ |
      |                                  |
      v                                  v
   Afișează pagina            Trimite mai departe
```

- **Clientul** cere o resursă (o pagină, o imagine, un videoclip).
- **Serverul** răspunde cu acea resursă (sau cu o eroare, dacă nu există).

Browser-ul tău este un client. Google, YouTube, Wikipedia rulează pe servere.

---

## Cererea HTTP pe scurt

Limbajul prin care clientul și serverul vorbesc se numește **HTTP** (HyperText Transfer Protocol). Când scrii o adresă și apeși Enter, se întâmplă (simplificat):

1. Browser-ul construiește o **cerere**: „Dă-mi pagina `/` de pe `ursoaia-edu.online`”.
2. Serverul răspunde cu un **cod de stare** și conținutul paginii.

Coduri pe care le vei întâlni des:

| Cod | Ce înseamnă |
|-----|-------------|
| `200 OK` | Totul e bine, uite pagina |
| `301` / `302` | Redirectare — pagina s-a mutat |
| `404 Not Found` | Nu există pagina cerută |
| `500 Internal Server Error` | Serverul are o problemă |

!!! note "HTTPS"
    Versiunea **sigură** se numește **HTTPS** — comunicarea este criptată. În bara browser-ului vei vedea un **lacăt**. Toate site-urile moderne folosesc HTTPS.

---

## Ce face browser-ul?

Browser-ul are practic **3 joburi** atunci când primește o pagină:

1. **Citește HTML-ul** (parse) și construiește o structură de tip copac (DOM).
2. **Aplică CSS-ul** ca pagina să arate frumos (culori, fonturi, poziții).
3. **Execută JavaScript-ul** ca pagina să fie interactivă (butoane, animații, date dinamice).

Fără browser, HTML este doar un fișier text. Browser-ul este „motorul” care îl transformă în ceea ce vezi.

---

## Cele 3 limbaje ale web-ului

Orice site modern este construit pe trei piloni:

| Limbaj | Rol | Analogie |
|--------|-----|----------|
| **HTML** | Structura și conținutul paginii | Scheletul |
| **CSS**  | Aspectul: culori, fonturi, layout | Hainele |
| **JavaScript** | Comportamentul: interactivitate | Mișcările |

!!! tip "Focus pe rând"
    În lecțiile 01–05 învățăm **HTML**, în 06–10 învățăm **CSS**, apoi trecem la **JavaScript**. Nu încerca să le înveți pe toate în același timp — fiecare are propriul mod de gândire.

---

## Instrumentele noastre

### 1. Editor de cod: VS Code

[Visual Studio Code](https://code.visualstudio.com/) este un editor gratuit, rapid și folosit în industrie. Descarcă-l și instalează-l.

După instalare, instalează **o singură extensie** esențială pentru început:

- **Live Server** (autor: Ritwick Dey) — pornește un mini-server local și îți **reîmprospătează automat** pagina când salvezi fișierul.

### 2. Browser: Chrome sau Firefox

Orice browser modern e bun. Recomandăm **Chrome** sau **Firefox** pentru că au DevTools puternice. Evită Internet Explorer — e oficial abandonat.

### 3. DevTools (uneltele developer-ului)

Cea mai importantă scurtătură din tot cursul:

```
F12
```

(sau `Ctrl+Shift+I` pe Windows / `Cmd+Opt+I` pe Mac)

Se va deschide un panou cu mai multe tab-uri. Cele care ne interesează acum:

- **Elements** — arborele HTML al paginii curente. Poți edita temporar orice element (doar la tine, nimeni altcineva nu vede schimbarea).
- **Console** — poți scrie comenzi JavaScript și vedea mesajele din pagină.
- **Network** — arată toate cererile HTTP (HTML, imagini, CSS, JS) pe care le face pagina.

!!! warning "Modificările din DevTools sunt locale"
    Orice schimbi în tab-ul Elements dispare la refresh. Nu modifici site-ul original — doar ce vezi **tu** în browser-ul tău.

---

## Primul tău experiment

1. Deschide **[google.com](https://www.google.com)**.
2. Apasă **F12**.
3. Mergi în tab-ul **Elements**.
4. Dă click pe săgeata/iconița „Inspect” din stânga-sus a panoului și apoi click pe bara de căutare Google.
5. În panou vei vedea codul HTML al acelui element — un `<input>`.
6. Dublu-click pe un text vizibil din pagină (ex: „Google Search”) și schimbă-l cu numele tău. Apasă Enter. Pagina arată altfel **doar pentru tine**.

Bravo! Tocmai ai făcut primul „hack” al unei pagini web. (Nu e un hack real — e doar o modificare locală.)

---

## Exerciții

### Exercițiu 1 — Disecează un URL
Explică fiecare parte a adresei: `https://ursoaia-edu.online/courses/python/04-conditii/`

??? success "Soluție"
    - `https` — **protocolul**: cum comunicăm (HTTPS = HTTP securizat).
    - `ursoaia-edu.online` — **domeniul**: adresa serverului.
    - `/courses/python/04-conditii/` — **path-ul**: ce pagină anume de pe acel server vrem să vedem.

### Exercițiu 2 — Modifică temporar un titlu
Deschide Wikipedia, apasă `F12`, mergi în Elements, găsește tag-ul `<h1>` al articolului și schimbă textul. Ia un screenshot. După refresh, totul revine.

??? success "Soluție"
    - `F12` → Elements.
    - Click pe iconița „Inspect element” (săgeata mică din stânga-sus a panoului).
    - Click pe titlul articolului.
    - Dublu-click pe text în panou, scrie altceva, Enter.
    - Refresh (`F5`) — titlul original revine.

### Exercițiu 3 — Folosește Console
Deschide orice pagină și în tab-ul **Console** scrie:

```js
document.title
```

și apasă Enter. Ce afișează?

??? success "Soluție"
    Afișează **textul din tab-ul browser-ului** (titlul paginii curente) — același lucru pe care îl vezi în bara de file. E primul tău contact cu JavaScript: `document` este pagina, `.title` este proprietatea cu titlul ei.

---

## Rezumat

- **Internet ≠ Web.** Internetul e infrastructura; Web-ul e stratul de site-uri.
- Paginile merg pe modelul **client–server** prin protocolul **HTTP/HTTPS**.
- Browser-ul face 3 lucruri: parsează HTML, aplică CSS, execută JS.
- Cele 3 limbaje: **HTML** (structură), **CSS** (aspect), **JavaScript** (comportament).
- Instrumentele tale: **VS Code + Live Server + browser modern + F12**.
- `F12` îți deschide DevTools — tab-urile **Elements**, **Console**, **Network** sunt prietenii tăi.

---

**Pasul următor:** [→ Lecția 01: Prima ta pagină](01-prima-pagina.md)
