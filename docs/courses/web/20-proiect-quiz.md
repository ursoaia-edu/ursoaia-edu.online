---
lesson: 20
tags: [web, proiect, quiz, javascript, dom, evenimente, state]
summary: Proiect complet — construiești o aplicație Quiz interactivă cu JavaScript, cu feedback instant și scor final.
---

# Lecția 20 · Proiect: Aplicație Quiz

!!! tip "Ce vei exersa"
    - Manipularea DOM (crearea dinamică de butoane, schimbarea textului)
    - Evenimente (click pe butoane)
    - Array-uri de obiecte (întrebările quiz-ului)
    - State management (indexul întrebării curente, scorul)
    - `setTimeout` pentru pauze scurte

---

## Prezentarea proiectului

Vei construi o **aplicație Quiz** de cultură generală cu 6 întrebări. Pentru fiecare:

- Se afișează enunțul și 4 opțiuni (ca butoane)
- La click: butonul corect devine **verde**, cel greșit **roșu**
- După 1 secundă, trecem la următoarea întrebare
- La final: scorul și un buton „Reîncepe”

**Exemplu de rulare:**

```
┌──────────────────────────────────────┐
│   Quiz cultura generală              │
├──────────────────────────────────────┤
│   Întrebarea 2 din 6                 │
│                                      │
│   Care este capitala României?       │
│                                      │
│   [ București  ]   ← apăsat (verde)  │
│   [ Cluj       ]                     │
│   [ Iași       ]                     │
│   [ Timișoara  ]                     │
└──────────────────────────────────────┘

... după 6 întrebări ...

┌──────────────────────────────────────┐
│   Ai răspuns corect la 5 / 6.        │
│   Felicitări!                        │
│                                      │
│          [ Reîncepe ]                │
└──────────────────────────────────────┘
```

---

## Pasul 1: Structura HTML

Creează `quiz/index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz · Cultura generală</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="quiz">
    <h1>Quiz cultura generală</h1>

    <p id="progres" class="progres">Întrebarea 1 din 6</p>
    <h2 id="intrebare" class="intrebare"></h2>

    <div id="optiuni" class="optiuni"></div>

    <section id="final" class="final ascuns">
      <p id="scor"></p>
      <p id="mesaj"></p>
      <button id="reincepe" class="btn">Reîncepe</button>
    </section>
  </main>

  <script src="quiz.js"></script>
</body>
</html>
```

!!! note "Strategia ID-urilor"
    Folosim `id` pentru elementele pe care JavaScript-ul trebuie să le actualizeze: `progres`, `intrebare`, `optiuni`, `final`, `scor`, `mesaj`, `reincepe`. Celelalte elemente sunt stilizate doar cu clase.

---

## Pasul 2: CSS

Creează `quiz/styles.css`:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --primara: #6366f1;
  --corect: #22c55e;
  --gresit: #ef4444;
  --fundal: #0f172a;
  --card: #1e293b;
  --text: #e2e8f0;
  --text-moale: #94a3b8;
  --radius: 12px;
}

body {
  font-family: "Inter", system-ui, sans-serif;
  background: var(--fundal);
  color: var(--text);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.quiz {
  max-width: 600px;
  width: 100%;
  background: var(--card);
  padding: 2.5rem 2rem;
  border-radius: 18px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
  animation: aparitie 0.4s ease;
}

@keyframes aparitie {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

.quiz h1 {
  font-size: 1.5rem;
  text-align: center;
  margin-bottom: 0.5rem;
}

.progres {
  text-align: center;
  color: var(--text-moale);
  font-size: 0.9rem;
  margin-bottom: 2rem;
}

.intrebare {
  font-size: 1.35rem;
  line-height: 1.4;
  margin-bottom: 1.75rem;
  min-height: 3.5em;
}

.optiuni {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.optiune {
  padding: 0.9rem 1.25rem;
  background: transparent;
  color: var(--text);
  border: 2px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius);
  font-size: 1rem;
  font-family: inherit;
  text-align: left;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}

.optiune:hover:not(:disabled) {
  border-color: var(--primara);
  transform: translateX(4px);
}

.optiune:disabled { cursor: not-allowed; opacity: 0.7; }
.optiune.corect   { background: var(--corect); border-color: var(--corect); color: white; }
.optiune.gresit   { background: var(--gresit); border-color: var(--gresit); color: white; }

.final { text-align: center; margin-top: 1rem; }
.final p { margin-bottom: 1rem; }
.final p:first-child { font-size: 1.5rem; font-weight: 700; }

.btn {
  padding: 0.75rem 2rem;
  background: var(--primara);
  color: white;
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn:hover { transform: translateY(-2px); }

.ascuns { display: none; }
```

---

## Pasul 3: Datele quiz-ului

În `quiz/quiz.js`, definim întrebările ca **array de obiecte**:

```js
const intrebari = [
  {
    text: "Care este capitala României?",
    optiuni: ["București", "Cluj-Napoca", "Iași", "Timișoara"],
    corect: 0
  },
  {
    text: "Cât face 7 × 8?",
    optiuni: ["54", "56", "58", "64"],
    corect: 1
  },
  {
    text: "Cine a scris „Luceafărul”?",
    optiuni: ["Ion Creangă", "George Coșbuc", "Mihai Eminescu", "Tudor Arghezi"],
    corect: 2
  },
  {
    text: "Care planetă este cea mai apropiată de Soare?",
    optiuni: ["Venus", "Pământ", "Marte", "Mercur"],
    corect: 3
  },
  {
    text: "În ce an a căzut comunismul în România?",
    optiuni: ["1989", "1991", "1985", "1993"],
    corect: 0
  },
  {
    text: "Ce limbaj rulează în browser?",
    optiuni: ["Python", "JavaScript", "Java", "C++"],
    corect: 1
  }
];
```

!!! tip "Indexare de la 0"
    În programare, primul element din `optiuni` are indexul `0`, al doilea `1` etc. Dacă răspunsul corect este a treia opțiune, `corect: 2`.

---

## Pasul 4: State-ul aplicației

State-ul este **datele care se schimbă în timp** pe măsură ce jucătorul progresează:

```js
let indexCurent = 0;  // ce întrebare arătăm (0..n-1)
let scor = 0;         // câte răspunsuri corecte are
```

Luăm și referințele la elementele din DOM o singură dată:

```js
const progresEl   = document.getElementById("progres");
const intrebareEl = document.getElementById("intrebare");
const optiuniEl   = document.getElementById("optiuni");
const finalEl     = document.getElementById("final");
const scorEl      = document.getElementById("scor");
const mesajEl     = document.getElementById("mesaj");
const reincepeEl  = document.getElementById("reincepe");
```

---

## Pasul 5: Funcția `afișeazăÎntrebarea()`

Afișează întrebarea curentă și creează butoanele pentru opțiuni:

```js
function afișeazăÎntrebarea() {
  const intrebare = intrebari[indexCurent];

  progresEl.textContent = `Întrebarea ${indexCurent + 1} din ${intrebari.length}`;
  intrebareEl.textContent = intrebare.text;

  optiuniEl.innerHTML = "";  // curățăm butoanele vechi

  intrebare.optiuni.forEach((opt, i) => {
    const btn = document.createElement("button");
    btn.className = "optiune";
    btn.textContent = opt;
    btn.addEventListener("click", () => verifică(i, btn));
    optiuniEl.appendChild(btn);
  });
}
```

!!! note "Închiderea (closure) pe `i`"
    Fiecare buton își „amintește” propriul `i` datorită funcției săgeată `() => verifică(i, btn)`. Când utilizatorul apasă butonul, se trimite exact indexul opțiunii apăsate.

---

## Pasul 6: Verificarea răspunsului

Comparăm indexul apăsat cu `corect` și colorăm butoanele:

```js
function verifică(indexApasat, butonApasat) {
  const intrebare = intrebari[indexCurent];
  const butoane = optiuniEl.querySelectorAll(".optiune");

  // Dezactivăm toate butoanele
  butoane.forEach(b => b.disabled = true);

  if (indexApasat === intrebare.corect) {
    butonApasat.classList.add("corect");
    scor++;
  } else {
    butonApasat.classList.add("gresit");
    // Arătăm și răspunsul corect
    butoane[intrebare.corect].classList.add("corect");
  }

  // După 1 secundă, trecem la următoarea
  setTimeout(urmează, 1000);
}
```

---

## Pasul 7: Finalul quiz-ului

Funcția `urmează()` decide dacă mai sunt întrebări sau arătăm scorul:

```js
function urmează() {
  indexCurent++;

  if (indexCurent < intrebari.length) {
    afișeazăÎntrebarea();
  } else {
    afișeazăScor();
  }
}

function afișeazăScor() {
  intrebareEl.classList.add("ascuns");
  optiuniEl.classList.add("ascuns");
  progresEl.classList.add("ascuns");

  finalEl.classList.remove("ascuns");
  scorEl.textContent = `Ai răspuns corect la ${scor} din ${intrebari.length}.`;

  const procent = (scor / intrebari.length) * 100;
  if (procent === 100)       mesajEl.textContent = "Perfect! Ești un expert.";
  else if (procent >= 75)    mesajEl.textContent = "Foarte bine! Mai ai de lucru la câteva detalii.";
  else if (procent >= 50)    mesajEl.textContent = "Bun început. Mai exersează!";
  else                       mesajEl.textContent = "Nu descuraja — încearcă din nou!";
}
```

---

## Pasul 8: Reîncepere

Butonul „Reîncepe” resetează state-ul și repornește quiz-ul:

```js
reincepeEl.addEventListener("click", () => {
  indexCurent = 0;
  scor = 0;

  intrebareEl.classList.remove("ascuns");
  optiuniEl.classList.remove("ascuns");
  progresEl.classList.remove("ascuns");
  finalEl.classList.add("ascuns");

  afișeazăÎntrebarea();
});
```

La final, pornim quiz-ul:

```js
afișeazăÎntrebarea();
```

---

## Codul complet

### `index.html`

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz · Cultura generală</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="quiz">
    <h1>Quiz cultura generală</h1>
    <p id="progres" class="progres">Întrebarea 1 din 6</p>
    <h2 id="intrebare" class="intrebare"></h2>
    <div id="optiuni" class="optiuni"></div>

    <section id="final" class="final ascuns">
      <p id="scor"></p>
      <p id="mesaj"></p>
      <button id="reincepe" class="btn">Reîncepe</button>
    </section>
  </main>

  <script src="quiz.js"></script>
</body>
</html>
```

### `styles.css`

(folosește CSS-ul integral din Pasul 2)

### `quiz.js`

```js
const intrebari = [
  { text: "Care este capitala României?",
    optiuni: ["București", "Cluj-Napoca", "Iași", "Timișoara"], corect: 0 },
  { text: "Cât face 7 × 8?",
    optiuni: ["54", "56", "58", "64"], corect: 1 },
  { text: "Cine a scris „Luceafărul”?",
    optiuni: ["Ion Creangă", "George Coșbuc", "Mihai Eminescu", "Tudor Arghezi"], corect: 2 },
  { text: "Care planetă este cea mai apropiată de Soare?",
    optiuni: ["Venus", "Pământ", "Marte", "Mercur"], corect: 3 },
  { text: "În ce an a căzut comunismul în România?",
    optiuni: ["1989", "1991", "1985", "1993"], corect: 0 },
  { text: "Ce limbaj rulează în browser?",
    optiuni: ["Python", "JavaScript", "Java", "C++"], corect: 1 }
];

let indexCurent = 0;
let scor = 0;

const progresEl   = document.getElementById("progres");
const intrebareEl = document.getElementById("intrebare");
const optiuniEl   = document.getElementById("optiuni");
const finalEl     = document.getElementById("final");
const scorEl      = document.getElementById("scor");
const mesajEl     = document.getElementById("mesaj");
const reincepeEl  = document.getElementById("reincepe");

function afișeazăÎntrebarea() {
  const intrebare = intrebari[indexCurent];
  progresEl.textContent = `Întrebarea ${indexCurent + 1} din ${intrebari.length}`;
  intrebareEl.textContent = intrebare.text;
  optiuniEl.innerHTML = "";

  intrebare.optiuni.forEach((opt, i) => {
    const btn = document.createElement("button");
    btn.className = "optiune";
    btn.textContent = opt;
    btn.addEventListener("click", () => verifică(i, btn));
    optiuniEl.appendChild(btn);
  });
}

function verifică(indexApasat, butonApasat) {
  const intrebare = intrebari[indexCurent];
  const butoane = optiuniEl.querySelectorAll(".optiune");
  butoane.forEach(b => b.disabled = true);

  if (indexApasat === intrebare.corect) {
    butonApasat.classList.add("corect");
    scor++;
  } else {
    butonApasat.classList.add("gresit");
    butoane[intrebare.corect].classList.add("corect");
  }

  setTimeout(urmează, 1000);
}

function urmează() {
  indexCurent++;
  if (indexCurent < intrebari.length) {
    afișeazăÎntrebarea();
  } else {
    afișeazăScor();
  }
}

function afișeazăScor() {
  intrebareEl.classList.add("ascuns");
  optiuniEl.classList.add("ascuns");
  progresEl.classList.add("ascuns");
  finalEl.classList.remove("ascuns");

  scorEl.textContent = `Ai răspuns corect la ${scor} din ${intrebari.length}.`;
  const procent = (scor / intrebari.length) * 100;

  if (procent === 100)    mesajEl.textContent = "Perfect! Ești un expert.";
  else if (procent >= 75) mesajEl.textContent = "Foarte bine! Mai ai de lucru la câteva detalii.";
  else if (procent >= 50) mesajEl.textContent = "Bun început. Mai exersează!";
  else                    mesajEl.textContent = "Nu descuraja — încearcă din nou!";
}

reincepeEl.addEventListener("click", () => {
  indexCurent = 0;
  scor = 0;
  intrebareEl.classList.remove("ascuns");
  optiuniEl.classList.remove("ascuns");
  progresEl.classList.remove("ascuns");
  finalEl.classList.add("ascuns");
  afișeazăÎntrebarea();
});

afișeazăÎntrebarea();
```

---

## Idei de extindere

1. **Amestecă întrebările și opțiunile** cu algoritmul Fisher–Yates pentru varietate la fiecare reluare.
2. **Timer per întrebare** — 10 secunde; dacă expiră, marchezi automat răspunsul ca greșit.
3. **Categorii** — un meniu inițial: „Geografie”, „Istorie”, „Matematică”, „Tehnologie”. Fiecare categorie are propriul array de întrebări.
4. **Scor salvat** — `localStorage.setItem("scorMaxim", scor)` ca să păstrezi cel mai bun rezultat între sesiuni.
5. **Leaderboard** — input pentru nume la final, scorurile celor mai buni jucători stocate în `localStorage`.
6. **Întrebări multi-răspuns** — adaugă `corecte: [0, 2]` pentru întrebări cu mai multe bile de răspuns.
7. **Sunet** — un scurt *ding* la răspuns corect, *buzz* la greșit (cu `new Audio()`).

---

## Rezumat

Ai învățat să:

- Modelezi datele unui quiz cu un **array de obiecte**
- Generezi butoane **dinamic** cu `createElement` și `appendChild`
- Gestionezi state-ul (întrebarea curentă, scorul) cu variabile la nivelul modulului
- Oferi feedback vizual prin clase CSS (`corect`, `gresit`)
- Folosești `setTimeout` pentru pauze între pași

---

**Pasul următor:** [→ Proiect: Aplicație Meteo](21-proiect-meteo.md)
