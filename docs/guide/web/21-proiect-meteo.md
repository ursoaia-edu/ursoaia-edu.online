---
lesson: 21
tags: [web, proiect, meteo, api, fetch, async, javascript]
summary: Proiect final — construiești o aplicație meteo care consumă un API public (Open-Meteo) cu fetch și async/await.
---

# Lecția 21 · Proiect: Aplicație Meteo

!!! tip "Ce vei exersa"
    - `fetch` și `async / await`
    - Lucrul cu JSON primit de la un API
    - Actualizarea DOM-ului cu date dinamice
    - Tratarea erorilor (conexiune pierdută, API indisponibil)
    - Stările de interfață: loading, succes, eroare

---

## Prezentarea proiectului

Vei construi o **aplicație meteo** care:

1. Permite alegerea unui oraș dintr-un dropdown (7 orașe preconfigurate)
2. La apăsarea butonului „Obține prognoza”, apelează un **API public**
3. Afișează temperatura, condiția meteo, viteza vântului și umiditatea
4. Arată iconuri (emoji) în funcție de cod meteo
5. Tratează elegant situațiile de eroare

**Exemplu de interfață:**

```
┌────────────────────────────────────┐
│  Meteo orașe                       │
│                                    │
│  Oraș: [ București ▼ ]             │
│        [ Obține prognoza ]         │
│                                    │
│  ─────── Rezultat ───────          │
│                                    │
│       🌤️                            │
│       21°C                         │
│     Parțial noros                  │
│                                    │
│  💨 Vânt:     12 km/h              │
│  💧 Umiditate: 65%                 │
└────────────────────────────────────┘
```

---

## De ce Open-Meteo?

Folosim **Open-Meteo** (<https://open-meteo.com>) pentru că:

- Este **gratuit** pentru uz educațional și personal
- **Nu are nevoie de API key** — te concentrezi pe cod, nu pe înregistrări
- Returnează **JSON curat** și bine documentat
- Endpoint-ul folosit: `https://api.open-meteo.com/v1/forecast`

**Exemplu URL:**

```
https://api.open-meteo.com/v1/forecast
  ?latitude=44.43
  &longitude=26.10
  &current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code
  &timezone=auto
```

!!! note "Parametrii"
    - `latitude`, `longitude` — coordonatele orașului
    - `current` — câmpurile care te interesează (separate prin virgulă)
    - `timezone=auto` — orele întoarse în timezone-ul orașului

---

## Pasul 1: Structura HTML

Creează `meteo/index.html`:

```html
<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meteo · Open-Meteo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="card">
    <h1>Meteo orașe</h1>

    <form id="form-meteo" class="form">
      <label for="oras">Oraș</label>
      <select id="oras" required>
        <option value="" disabled selected>Alege un oraș…</option>
      </select>

      <button type="submit" class="btn">Obține prognoza</button>
    </form>

    <p id="loading" class="mesaj ascuns">Se încarcă…</p>
    <p id="eroare" class="mesaj eroare ascuns" role="alert"></p>

    <section id="rezultat" class="rezultat ascuns" aria-live="polite"></section>
  </main>

  <script src="app.js"></script>
</body>
</html>
```

!!! warning "Accesibilitate"
    - `<label for="oras">` leagă eticheta de câmp: click pe text focalizează dropdown-ul.
    - `role="alert"` pe eroare anunță cititoarele de ecran automat.
    - `aria-live="polite"` pe rezultat anunță datele noi fără a întrerupe utilizatorul.

---

## Pasul 2: CSS — design modern

Creează `meteo/styles.css`:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --primara: #0ea5e9;
  --text: #f1f5f9;
  --text-moale: #cbd5e1;
  --eroare: #f87171;
  --radius: 14px;
}

body {
  min-height: 100vh;
  font-family: "Inter", system-ui, sans-serif;
  color: var(--text);
  background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0ea5e9 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.card {
  width: 100%;
  max-width: 460px;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  padding: 2.5rem 2rem;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.35);
}

.card h1 {
  font-size: 1.6rem;
  text-align: center;
  margin-bottom: 1.75rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.form label {
  color: var(--text-moale);
  font-size: 0.9rem;
}

.form select {
  padding: 0.75rem 1rem;
  background: rgba(255, 255, 255, 0.1);
  color: var(--text);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius);
  font-family: inherit;
  font-size: 1rem;
}

.form select:focus {
  outline: 2px solid var(--primara);
  outline-offset: 2px;
}

.btn {
  margin-top: 0.5rem;
  padding: 0.85rem 1.25rem;
  background: var(--primara);
  color: white;
  border: none;
  border-radius: var(--radius);
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease, filter 0.2s ease;
}
.btn:hover    { transform: translateY(-2px); filter: brightness(1.1); }
.btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; }

.mesaj {
  margin-top: 1.25rem;
  text-align: center;
  color: var(--text-moale);
}
.mesaj.eroare { color: var(--eroare); }

.rezultat {
  margin-top: 2rem;
  text-align: center;
  animation: aparitie 0.4s ease;
}

@keyframes aparitie {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.rezultat h2      { font-size: 1.1rem; color: var(--text-moale); font-weight: 500; margin-bottom: 0.5rem; }
.rezultat .icon   { font-size: 4.5rem; line-height: 1; margin: 0.5rem 0; }
.rezultat .temp   { font-size: 3.5rem; font-weight: 700; }
.rezultat .desc   { font-size: 1.15rem; color: var(--text-moale); margin-bottom: 1.25rem; }

.rezultat .detalii {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--text-moale);
  font-size: 0.95rem;
}

.ascuns { display: none; }
```

---

## Pasul 3: Datele orașelor

În `meteo/app.js`, definim lista de orașe cu coordonatele lor:

```js
const orase = {
  "Chișinău":    { lat: 47.00, lon: 28.86 },
  "București":   { lat: 44.43, lon: 26.10 },
  "Cluj-Napoca": { lat: 46.77, lon: 23.60 },
  "Iași":        { lat: 47.16, lon: 27.58 },
  "Timișoara":   { lat: 45.76, lon: 21.22 },
  "Constanța":   { lat: 44.18, lon: 28.65 },
  "Brașov":      { lat: 45.66, lon: 25.61 }
};
```

Populăm dropdown-ul la pornire:

```js
const selectOras = document.getElementById("oras");

for (const nume of Object.keys(orase)) {
  const opt = document.createElement("option");
  opt.value = nume;
  opt.textContent = nume;
  selectOras.appendChild(opt);
}
```

---

## Pasul 4: Maparea codurilor meteo la emoji

Open-Meteo returnează câmpul `weather_code` (WMO). Îl traducem în ceva prietenos:

```js
const codMeteo = {
  0:  { descriere: "Cer senin",          icon: "☀️" },
  1:  { descriere: "Aproape senin",      icon: "🌤️" },
  2:  { descriere: "Parțial noros",      icon: "⛅" },
  3:  { descriere: "Înnorat",            icon: "☁️" },
  45: { descriere: "Ceață",              icon: "🌫️" },
  48: { descriere: "Ceață cu chiciură",  icon: "🌫️" },
  51: { descriere: "Burniță ușoară",     icon: "🌦️" },
  53: { descriere: "Burniță moderată",   icon: "🌦️" },
  55: { descriere: "Burniță densă",      icon: "🌧️" },
  61: { descriere: "Ploaie ușoară",      icon: "🌧️" },
  63: { descriere: "Ploaie moderată",    icon: "🌧️" },
  65: { descriere: "Ploaie intensă",     icon: "🌧️" },
  71: { descriere: "Zăpadă ușoară",      icon: "🌨️" },
  73: { descriere: "Zăpadă moderată",    icon: "🌨️" },
  75: { descriere: "Zăpadă intensă",     icon: "❄️" },
  80: { descriere: "Averse de ploaie",   icon: "🌦️" },
  81: { descriere: "Averse puternice",   icon: "🌧️" },
  95: { descriere: "Furtună",            icon: "⛈️" },
  96: { descriere: "Furtună cu grindină", icon: "⛈️" }
};
```

!!! note "Căutare cu valoare implicită"
    Dacă serverul întoarce un cod pe care nu-l cunoaștem, vom folosi un obiect fallback: `codMeteo[x] || { descriere: "Necunoscut", icon: "❓" }`.

---

## Pasul 5: Funcția `fetch` cu `async / await`

Aceasta face apelul propriu-zis la API:

```js
async function obținePrognoza(lat, lon) {
  const url = `https://api.open-meteo.com/v1/forecast`
            + `?latitude=${lat}&longitude=${lon}`
            + `&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code`
            + `&timezone=auto`;

  const raspuns = await fetch(url);

  if (!raspuns.ok) {
    throw new Error(`API a returnat HTTP ${raspuns.status}`);
  }

  const date = await raspuns.json();
  return date.current;  // ex.: { temperature_2m: 21.4, wind_speed_10m: 12, ... }
}
```

!!! tip "`async / await` vs `.then()`"
    `await` face codul să se citească ca și cum ar fi sincron, dar rulează tot asincron. `try / catch` în jurul lui tratează natural erorile — spre deosebire de lanțul `.then().catch()`.

---

## Pasul 6: Afișarea datelor în DOM

```js
const rezultatEl = document.getElementById("rezultat");

function afișeazăRezultat(numeOras, date) {
  const cod = codMeteo[date.weather_code] || { descriere: "Necunoscut", icon: "❓" };

  rezultatEl.innerHTML = `
    <h2>${numeOras}</h2>
    <div class="icon" aria-hidden="true">${cod.icon}</div>
    <div class="temp">${Math.round(date.temperature_2m)}°C</div>
    <div class="desc">${cod.descriere}</div>
    <div class="detalii">
      <div>💨 Vânt: ${date.wind_speed_10m} km/h</div>
      <div>💧 Umiditate: ${date.relative_humidity_2m}%</div>
    </div>
  `;
  rezultatEl.classList.remove("ascuns");
}
```

!!! warning "Nu insera string-uri nesigure în `innerHTML`"
    Aici e sigur pentru că vin de la Open-Meteo (numere), iar `numeOras` e dintr-o listă pe care o controlăm tu. Pentru input liber de la utilizator, folosește `textContent` în loc de `innerHTML`.

---

## Pasul 7: Conectarea formularului

Evenimentul `submit` apelează fetch-ul și afișează rezultatul:

```js
const formEl     = document.getElementById("form-meteo");
const loadingEl  = document.getElementById("loading");
const eroareEl   = document.getElementById("eroare");

formEl.addEventListener("submit", async e => {
  e.preventDefault();
  const numeOras = selectOras.value;
  if (!numeOras) return;

  const coord = orase[numeOras];

  // Resetăm interfața
  rezultatEl.classList.add("ascuns");
  eroareEl.classList.add("ascuns");
  loadingEl.classList.remove("ascuns");

  try {
    const date = await obținePrognoza(coord.lat, coord.lon);
    afișeazăRezultat(numeOras, date);
  } catch (err) {
    afișeazăEroare(err);
  } finally {
    loadingEl.classList.add("ascuns");
  }
});
```

---

## Pasul 8: Starea „Se încarcă”

Ascunsă implicit, `#loading` devine vizibilă între click și răspuns. Am inclus-o deja în Pasul 7 cu `classList.remove("ascuns")` înainte de fetch și `classList.add("ascuns")` în `finally`, ca să se închidă indiferent dacă reușește sau eșuează.

!!! tip "De ce `finally`?"
    Block-ul `finally` rulează mereu, fie că `try` se termină normal, fie că aruncă eroare. E locul perfect pentru curățare (oprire loading, resetare butoane, etc.).

---

## Pasul 9: Tratarea erorilor

Adăugăm funcția de eroare:

```js
function afișeazăEroare(err) {
  console.error(err);
  eroareEl.textContent =
    "Nu am putut obține prognoza. Verifică conexiunea la internet și încearcă din nou.";
  eroareEl.classList.remove("ascuns");
}
```

**Ce fel de erori pot apărea?**

- **Conexiune pierdută** — `fetch` aruncă `TypeError: Failed to fetch`.
- **API indisponibil** — `fetch` reușește dar întoarce HTTP 5xx — `response.ok` este `false` și noi aruncăm manual.
- **Răspuns invalid** — `response.json()` aruncă dacă body-ul nu e JSON valid.

Toate cele 3 ajung în același `catch`, ceea ce face codul simplu.

---

## Codul complet

### `index.html`

(Codul integral de la Pasul 1)

### `styles.css`

(Codul integral de la Pasul 2)

### `app.js`

```js
// === Date orașe ===
const orase = {
  "Chișinău":    { lat: 47.00, lon: 28.86 },
  "București":   { lat: 44.43, lon: 26.10 },
  "Cluj-Napoca": { lat: 46.77, lon: 23.60 },
  "Iași":        { lat: 47.16, lon: 27.58 },
  "Timișoara":   { lat: 45.76, lon: 21.22 },
  "Constanța":   { lat: 44.18, lon: 28.65 },
  "Brașov":      { lat: 45.66, lon: 25.61 }
};

// === Mapare coduri WMO → iconuri / descrieri ===
const codMeteo = {
  0: { descriere: "Cer senin", icon: "☀️" },
  1: { descriere: "Aproape senin", icon: "🌤️" },
  2: { descriere: "Parțial noros", icon: "⛅" },
  3: { descriere: "Înnorat", icon: "☁️" },
  45: { descriere: "Ceață", icon: "🌫️" },
  48: { descriere: "Ceață cu chiciură", icon: "🌫️" },
  51: { descriere: "Burniță ușoară", icon: "🌦️" },
  53: { descriere: "Burniță moderată", icon: "🌦️" },
  55: { descriere: "Burniță densă", icon: "🌧️" },
  61: { descriere: "Ploaie ușoară", icon: "🌧️" },
  63: { descriere: "Ploaie moderată", icon: "🌧️" },
  65: { descriere: "Ploaie intensă", icon: "🌧️" },
  71: { descriere: "Zăpadă ușoară", icon: "🌨️" },
  73: { descriere: "Zăpadă moderată", icon: "🌨️" },
  75: { descriere: "Zăpadă intensă", icon: "❄️" },
  80: { descriere: "Averse de ploaie", icon: "🌦️" },
  81: { descriere: "Averse puternice", icon: "🌧️" },
  95: { descriere: "Furtună", icon: "⛈️" },
  96: { descriere: "Furtună cu grindină", icon: "⛈️" }
};

// === Referințe DOM ===
const formEl     = document.getElementById("form-meteo");
const selectOras = document.getElementById("oras");
const loadingEl  = document.getElementById("loading");
const eroareEl   = document.getElementById("eroare");
const rezultatEl = document.getElementById("rezultat");

// === Populare dropdown ===
for (const nume of Object.keys(orase)) {
  const opt = document.createElement("option");
  opt.value = nume;
  opt.textContent = nume;
  selectOras.appendChild(opt);
}

// === Fetch ===
async function obținePrognoza(lat, lon) {
  const url = `https://api.open-meteo.com/v1/forecast`
            + `?latitude=${lat}&longitude=${lon}`
            + `&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code`
            + `&timezone=auto`;

  const raspuns = await fetch(url);
  if (!raspuns.ok) throw new Error(`API a returnat HTTP ${raspuns.status}`);
  const date = await raspuns.json();
  return date.current;
}

// === Afișare ===
function afișeazăRezultat(numeOras, date) {
  const cod = codMeteo[date.weather_code] || { descriere: "Necunoscut", icon: "❓" };
  rezultatEl.innerHTML = `
    <h2>${numeOras}</h2>
    <div class="icon" aria-hidden="true">${cod.icon}</div>
    <div class="temp">${Math.round(date.temperature_2m)}°C</div>
    <div class="desc">${cod.descriere}</div>
    <div class="detalii">
      <div>💨 Vânt: ${date.wind_speed_10m} km/h</div>
      <div>💧 Umiditate: ${date.relative_humidity_2m}%</div>
    </div>
  `;
  rezultatEl.classList.remove("ascuns");
}

function afișeazăEroare(err) {
  console.error(err);
  eroareEl.textContent =
    "Nu am putut obține prognoza. Verifică conexiunea la internet și încearcă din nou.";
  eroareEl.classList.remove("ascuns");
}

// === Submit ===
formEl.addEventListener("submit", async e => {
  e.preventDefault();
  const numeOras = selectOras.value;
  if (!numeOras) return;
  const coord = orase[numeOras];

  rezultatEl.classList.add("ascuns");
  eroareEl.classList.add("ascuns");
  loadingEl.classList.remove("ascuns");

  try {
    const date = await obținePrognoza(coord.lat, coord.lon);
    afișeazăRezultat(numeOras, date);
  } catch (err) {
    afișeazăEroare(err);
  } finally {
    loadingEl.classList.add("ascuns");
  }
});
```

---

## Idei de extindere

1. **Input liber de oraș** — înlocuiește dropdown-ul cu un `<input>` și folosește **Nominatim** (OpenStreetMap) pentru geocoding.
2. **Prognoza pe 7 zile** — folosește parametrul `daily=temperature_2m_max,temperature_2m_min,weather_code` și randează 7 carduri.
3. **Detectarea automată a locației** — `navigator.geolocation.getCurrentPosition()` la prima încărcare.
4. **Grafic cu temperaturile pe 24h** — `hourly=temperature_2m` + o bibliotecă ușoară (Chart.js) sau pur SVG.
5. **Oraș preferat salvat** — `localStorage.setItem("orasPreferat", numeOras)` ca la reîncărcare să pornești de acolo.
6. **Modul offline** — `Service Worker` care cache-uiește ultima prognoză și o arată când nu ai internet.
7. **Unități imperiale** — toggle °C / °F folosind parametrul `temperature_unit=fahrenheit` în URL.

---

## Felicitări — ai terminat cursul!

Dacă ai ajuns până aici, felicitări. Ai învățat **de la zero**:

- **HTML** — structură semantică, formulare, multi-pagină
- **CSS** — variabile, Box Model, Flexbox, Grid, responsive design, animații
- **JavaScript** — variabile, funcții, DOM, evenimente, `fetch`, `async/await`
- **3 proiecte complete** — portofoliu, quiz, aplicație meteo

### Unde mergi mai departe?

- **Frameworks moderne** — învață [React](https://react.dev), [Vue](https://vuejs.org) sau [Svelte](https://svelte.dev) după ce stăpânești bine vanilla JS.
- **Backend** — [Node.js](https://nodejs.org) + Express sau [Python Flask](https://flask.palletsprojects.com) ca să construiești propriul API.
- **Bază de date** — începe cu [SQLite](https://www.sqlite.org) sau [PostgreSQL](https://www.postgresql.org).
- **Deploy gratuit** — publică proiectele pe [GitHub Pages](https://pages.github.com), [Netlify](https://www.netlify.com) sau [Vercel](https://vercel.com).
- **Git și GitHub** — versionează tot ce scrii; orice angajator verifică profilul tău GitHub.
- **Accesibilitate (a11y)** — citește [WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) și [WebAIM](https://webaim.org).

### Continuă să construiești

Cel mai bun mod de a învăța web development este să **construiești lucruri reale**:

1. Alege o problemă de-a ta (o notă de școală, un orar, o colecție)
2. Schițează interfața pe hârtie sau în [Figma](https://www.figma.com)
3. Construiește prototipul cu HTML + CSS + JS
4. Publică-l online și arată-l prietenilor

**Mult succes pe mai departe!** Web-ul este plin de posibilități — ai acum toate uneltele să contribui la el.

---

**Pasul următor:** [← Înapoi la prezentarea cursului](index.md)
