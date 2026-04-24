---
lesson: 21
tags: [web, project, weather, api, fetch, async, javascript]
summary: Final project — build a weather application that consumes a public API (Open-Meteo) using fetch and async/await.
---

# Lesson 21 · Project: Weather Application

!!! tip "What you'll practice"
    - `fetch` and `async / await`
    - Working with JSON received from an API
    - Updating the DOM with dynamic data
    - Error handling (lost connection, API unavailable)
    - Interface states: loading, success, error

---

## Project overview

You will build a **weather application** that:

1. Lets the user pick a city from a dropdown (7 preconfigured cities)
2. On clicking the "Get forecast" button, calls a **public API**
3. Displays the temperature, weather condition, wind speed and humidity
4. Shows icons (emoji) based on the weather code
5. Handles error situations elegantly

**Sample interface:**

```
┌────────────────────────────────────┐
│  City weather                      │
│                                    │
│  City: [ București ▼ ]             │
│        [ Get forecast ]            │
│                                    │
│  ─────── Result ───────            │
│                                    │
│       🌤️                            │
│       21°C                         │
│     Partly cloudy                  │
│                                    │
│  💨 Wind:     12 km/h              │
│  💧 Humidity: 65%                  │
└────────────────────────────────────┘
```

---

## Why Open-Meteo?

We use **Open-Meteo** (<https://open-meteo.com>) because:

- It is **free** for educational and personal use
- It **does not require an API key** — you focus on the code, not on registrations
- It returns **clean, well-documented JSON**
- The endpoint we use: `https://api.open-meteo.com/v1/forecast`

**Sample URL:**

```
https://api.open-meteo.com/v1/forecast
  ?latitude=44.43
  &longitude=26.10
  &current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code
  &timezone=auto
```

!!! note "Parameters"
    - `latitude`, `longitude` — the city coordinates
    - `current` — the fields you care about (comma-separated)
    - `timezone=auto` — times returned in the city's timezone

---

## Step 1: HTML structure

Create `weather/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weather · Open-Meteo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="card">
    <h1>City weather</h1>

    <form id="weather-form" class="form">
      <label for="city">City</label>
      <select id="city" required>
        <option value="" disabled selected>Choose a city…</option>
      </select>

      <button type="submit" class="btn">Get forecast</button>
    </form>

    <p id="loading" class="message hidden">Loading…</p>
    <p id="error" class="message error hidden" role="alert"></p>

    <section id="result" class="result hidden" aria-live="polite"></section>
  </main>

  <script src="app.js"></script>
</body>
</html>
```

!!! warning "Accessibility"
    - `<label for="city">` ties the label to the field: clicking the text focuses the dropdown.
    - `role="alert"` on the error announces it to screen readers automatically.
    - `aria-live="polite"` on the result announces new data without interrupting the user.

---

## Step 2: CSS — modern design

Create `weather/styles.css`:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --primary: #0ea5e9;
  --text: #f1f5f9;
  --text-soft: #cbd5e1;
  --error: #f87171;
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
  color: var(--text-soft);
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
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

.btn {
  margin-top: 0.5rem;
  padding: 0.85rem 1.25rem;
  background: var(--primary);
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

.message {
  margin-top: 1.25rem;
  text-align: center;
  color: var(--text-soft);
}
.message.error { color: var(--error); }

.result {
  margin-top: 2rem;
  text-align: center;
  animation: appear 0.4s ease;
}

@keyframes appear {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.result h2      { font-size: 1.1rem; color: var(--text-soft); font-weight: 500; margin-bottom: 0.5rem; }
.result .icon   { font-size: 4.5rem; line-height: 1; margin: 0.5rem 0; }
.result .temp   { font-size: 3.5rem; font-weight: 700; }
.result .desc   { font-size: 1.15rem; color: var(--text-soft); margin-bottom: 1.25rem; }

.result .details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--text-soft);
  font-size: 0.95rem;
}

.hidden { display: none; }
```

---

## Step 3: City data

In `weather/app.js`, we define the list of cities with their coordinates:

```js
const cities = {
  "Chișinău":    { lat: 47.00, lon: 28.86 },
  "București":   { lat: 44.43, lon: 26.10 },
  "Cluj-Napoca": { lat: 46.77, lon: 23.60 },
  "Iași":        { lat: 47.16, lon: 27.58 },
  "Timișoara":   { lat: 45.76, lon: 21.22 },
  "Constanța":   { lat: 44.18, lon: 28.65 },
  "Brașov":      { lat: 45.66, lon: 25.61 }
};
```

We populate the dropdown at startup:

```js
const selectCity = document.getElementById("city");

for (const name of Object.keys(cities)) {
  const opt = document.createElement("option");
  opt.value = name;
  opt.textContent = name;
  selectCity.appendChild(opt);
}
```

---

## Step 4: Mapping weather codes to emoji

Open-Meteo returns a `weather_code` field (WMO). We translate it into something friendly:

```js
const weatherCode = {
  0:  { description: "Clear sky",          icon: "☀️" },
  1:  { description: "Mainly clear",       icon: "🌤️" },
  2:  { description: "Partly cloudy",      icon: "⛅" },
  3:  { description: "Overcast",           icon: "☁️" },
  45: { description: "Fog",                icon: "🌫️" },
  48: { description: "Depositing rime fog", icon: "🌫️" },
  51: { description: "Light drizzle",      icon: "🌦️" },
  53: { description: "Moderate drizzle",   icon: "🌦️" },
  55: { description: "Dense drizzle",      icon: "🌧️" },
  61: { description: "Light rain",         icon: "🌧️" },
  63: { description: "Moderate rain",      icon: "🌧️" },
  65: { description: "Heavy rain",         icon: "🌧️" },
  71: { description: "Light snow",         icon: "🌨️" },
  73: { description: "Moderate snow",      icon: "🌨️" },
  75: { description: "Heavy snow",         icon: "❄️" },
  80: { description: "Rain showers",       icon: "🌦️" },
  81: { description: "Heavy showers",      icon: "🌧️" },
  95: { description: "Thunderstorm",       icon: "⛈️" },
  96: { description: "Thunderstorm with hail", icon: "⛈️" }
};
```

!!! note "Lookup with default value"
    If the server returns a code we don't know, we'll use a fallback object: `weatherCode[x] || { description: "Unknown", icon: "❓" }`.

---

## Step 5: The `fetch` function with `async / await`

This makes the actual API call:

```js
async function getForecast(lat, lon) {
  const url = `https://api.open-meteo.com/v1/forecast`
            + `?latitude=${lat}&longitude=${lon}`
            + `&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code`
            + `&timezone=auto`;

  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`API returned HTTP ${response.status}`);
  }

  const data = await response.json();
  return data.current;  // e.g.: { temperature_2m: 21.4, wind_speed_10m: 12, ... }
}
```

!!! tip "`async / await` vs `.then()`"
    `await` makes the code read as if it were synchronous, but it still runs asynchronously. `try / catch` around it handles errors naturally — unlike the `.then().catch()` chain.

---

## Step 6: Displaying the data in the DOM

```js
const resultEl = document.getElementById("result");

function showResult(cityName, data) {
  const code = weatherCode[data.weather_code] || { description: "Unknown", icon: "❓" };

  resultEl.innerHTML = `
    <h2>${cityName}</h2>
    <div class="icon" aria-hidden="true">${code.icon}</div>
    <div class="temp">${Math.round(data.temperature_2m)}°C</div>
    <div class="desc">${code.description}</div>
    <div class="details">
      <div>💨 Wind: ${data.wind_speed_10m} km/h</div>
      <div>💧 Humidity: ${data.relative_humidity_2m}%</div>
    </div>
  `;
  resultEl.classList.remove("hidden");
}
```

!!! warning "Don't insert untrusted strings into `innerHTML`"
    Here it's safe because they come from Open-Meteo (numbers), and `cityName` is from a list we control. For free user input, use `textContent` instead of `innerHTML`.

---

## Step 7: Wiring up the form

The `submit` event calls the fetch and displays the result:

```js
const formEl    = document.getElementById("weather-form");
const loadingEl = document.getElementById("loading");
const errorEl   = document.getElementById("error");

formEl.addEventListener("submit", async e => {
  e.preventDefault();
  const cityName = selectCity.value;
  if (!cityName) return;

  const coord = cities[cityName];

  // Reset the interface
  resultEl.classList.add("hidden");
  errorEl.classList.add("hidden");
  loadingEl.classList.remove("hidden");

  try {
    const data = await getForecast(coord.lat, coord.lon);
    showResult(cityName, data);
  } catch (err) {
    showError(err);
  } finally {
    loadingEl.classList.add("hidden");
  }
});
```

---

## Step 8: The "Loading" state

Hidden by default, `#loading` becomes visible between the click and the response. We've already included it in Step 7 with `classList.remove("hidden")` before the fetch and `classList.add("hidden")` in `finally`, so it closes whether it succeeds or fails.

!!! tip "Why `finally`?"
    The `finally` block always runs, whether `try` ends normally or throws an error. It's the perfect place for cleanup (turning off loading, resetting buttons, etc.).

---

## Step 9: Error handling

We add the error function:

```js
function showError(err) {
  console.error(err);
  errorEl.textContent =
    "Could not get the forecast. Check your internet connection and try again.";
  errorEl.classList.remove("hidden");
}
```

**What kinds of errors can occur?**

- **Lost connection** — `fetch` throws `TypeError: Failed to fetch`.
- **API unavailable** — `fetch` succeeds but returns HTTP 5xx — `response.ok` is `false` and we throw manually.
- **Invalid response** — `response.json()` throws if the body isn't valid JSON.

All 3 end up in the same `catch`, which makes the code simple.

---

## Complete code

### `index.html`

(The full code from Step 1)

### `styles.css`

(The full code from Step 2)

### `app.js`

```js
// === City data ===
const cities = {
  "Chișinău":    { lat: 47.00, lon: 28.86 },
  "București":   { lat: 44.43, lon: 26.10 },
  "Cluj-Napoca": { lat: 46.77, lon: 23.60 },
  "Iași":        { lat: 47.16, lon: 27.58 },
  "Timișoara":   { lat: 45.76, lon: 21.22 },
  "Constanța":   { lat: 44.18, lon: 28.65 },
  "Brașov":      { lat: 45.66, lon: 25.61 }
};

// === WMO code mapping → icons / descriptions ===
const weatherCode = {
  0: { description: "Clear sky", icon: "☀️" },
  1: { description: "Mainly clear", icon: "🌤️" },
  2: { description: "Partly cloudy", icon: "⛅" },
  3: { description: "Overcast", icon: "☁️" },
  45: { description: "Fog", icon: "🌫️" },
  48: { description: "Depositing rime fog", icon: "🌫️" },
  51: { description: "Light drizzle", icon: "🌦️" },
  53: { description: "Moderate drizzle", icon: "🌦️" },
  55: { description: "Dense drizzle", icon: "🌧️" },
  61: { description: "Light rain", icon: "🌧️" },
  63: { description: "Moderate rain", icon: "🌧️" },
  65: { description: "Heavy rain", icon: "🌧️" },
  71: { description: "Light snow", icon: "🌨️" },
  73: { description: "Moderate snow", icon: "🌨️" },
  75: { description: "Heavy snow", icon: "❄️" },
  80: { description: "Rain showers", icon: "🌦️" },
  81: { description: "Heavy showers", icon: "🌧️" },
  95: { description: "Thunderstorm", icon: "⛈️" },
  96: { description: "Thunderstorm with hail", icon: "⛈️" }
};

// === DOM references ===
const formEl     = document.getElementById("weather-form");
const selectCity = document.getElementById("city");
const loadingEl  = document.getElementById("loading");
const errorEl    = document.getElementById("error");
const resultEl   = document.getElementById("result");

// === Populate the dropdown ===
for (const name of Object.keys(cities)) {
  const opt = document.createElement("option");
  opt.value = name;
  opt.textContent = name;
  selectCity.appendChild(opt);
}

// === Fetch ===
async function getForecast(lat, lon) {
  const url = `https://api.open-meteo.com/v1/forecast`
            + `?latitude=${lat}&longitude=${lon}`
            + `&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code`
            + `&timezone=auto`;

  const response = await fetch(url);
  if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
  const data = await response.json();
  return data.current;
}

// === Display ===
function showResult(cityName, data) {
  const code = weatherCode[data.weather_code] || { description: "Unknown", icon: "❓" };
  resultEl.innerHTML = `
    <h2>${cityName}</h2>
    <div class="icon" aria-hidden="true">${code.icon}</div>
    <div class="temp">${Math.round(data.temperature_2m)}°C</div>
    <div class="desc">${code.description}</div>
    <div class="details">
      <div>💨 Wind: ${data.wind_speed_10m} km/h</div>
      <div>💧 Humidity: ${data.relative_humidity_2m}%</div>
    </div>
  `;
  resultEl.classList.remove("hidden");
}

function showError(err) {
  console.error(err);
  errorEl.textContent =
    "Could not get the forecast. Check your internet connection and try again.";
  errorEl.classList.remove("hidden");
}

// === Submit ===
formEl.addEventListener("submit", async e => {
  e.preventDefault();
  const cityName = selectCity.value;
  if (!cityName) return;
  const coord = cities[cityName];

  resultEl.classList.add("hidden");
  errorEl.classList.add("hidden");
  loadingEl.classList.remove("hidden");

  try {
    const data = await getForecast(coord.lat, coord.lon);
    showResult(cityName, data);
  } catch (err) {
    showError(err);
  } finally {
    loadingEl.classList.add("hidden");
  }
});
```

---

## Ideas to extend

1. **Free city input** — replace the dropdown with an `<input>` and use **Nominatim** (OpenStreetMap) for geocoding.
2. **7-day forecast** — use the `daily=temperature_2m_max,temperature_2m_min,weather_code` parameter and render 7 cards.
3. **Automatic location detection** — `navigator.geolocation.getCurrentPosition()` on the first load.
4. **Chart with 24h temperatures** — `hourly=temperature_2m` + a lightweight library (Chart.js) or pure SVG.
5. **Saved favorite city** — `localStorage.setItem("favoriteCity", cityName)` so on reload you start from there.
6. **Offline mode** — `Service Worker` that caches the latest forecast and shows it when you have no internet.
7. **Imperial units** — toggle °C / °F using the `temperature_unit=fahrenheit` parameter in the URL.

---

## Congratulations — you've finished the course!

If you've made it this far, congratulations. You've learned **from scratch**:

- **HTML** — semantic structure, forms, multi-page
- **CSS** — variables, Box Model, Flexbox, Grid, responsive design, animations
- **JavaScript** — variables, functions, DOM, events, `fetch`, `async/await`
- **3 complete projects** — portfolio, quiz, weather application

### Where do you go next?

- **Modern frameworks** — learn [React](https://react.dev), [Vue](https://vuejs.org) or [Svelte](https://svelte.dev) after you master vanilla JS well.
- **Backend** — [Node.js](https://nodejs.org) + Express or [Python Flask](https://flask.palletsprojects.com) to build your own API.
- **Database** — start with [SQLite](https://www.sqlite.org) or [PostgreSQL](https://www.postgresql.org).
- **Free deploy** — publish your projects on [GitHub Pages](https://pages.github.com), [Netlify](https://www.netlify.com) or [Vercel](https://vercel.com).
- **Git and GitHub** — version everything you write; any employer checks your GitHub profile.
- **Accessibility (a11y)** — read [WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/) and [WebAIM](https://webaim.org).

### Keep building

The best way to learn web development is to **build real things**:

1. Pick a problem of your own (a school grade, a schedule, a collection)
2. Sketch the interface on paper or in [Figma](https://www.figma.com)
3. Build the prototype with HTML + CSS + JS
4. Publish it online and show it to friends

**Good luck moving forward!** The web is full of possibilities — you now have all the tools to contribute to it.

---

**Next step:** [← Back to the course overview](index.md)
