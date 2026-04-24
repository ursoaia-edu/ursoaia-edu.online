<div align="center">

<img src="docs/assets/logo.png" alt="Ursoaia Edu Online" width="120" />

# Ursoaia Edu Online

**Cerc de informatică open-source — cursuri, proiecte și electronică pentru elevi curioși.**

[![Live site](https://img.shields.io/badge/site-ursoaia--edu.online-f97316?style=flat-square&logo=googlechrome&logoColor=white)](https://ursoaia-edu.online)
[![License](https://img.shields.io/badge/license-MIT_+_CC_BY_4.0-3b82f6?style=flat-square)](LICENSE)
[![Languages](https://img.shields.io/badge/limbi-RO_%7C_EN-22c55e?style=flat-square)](https://ursoaia-edu.online)
[![MkDocs](https://img.shields.io/badge/built%20with-MkDocs-526CFE?style=flat-square)](https://www.mkdocs.org/)
[![Python](https://img.shields.io/badge/python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)

[**Site live**](https://ursoaia-edu.online) · [Cursuri](https://ursoaia-edu.online/guide/) · [Proiecte](https://ursoaia-edu.online/projects/) · [Issues](https://github.com/ursoaia-edu/ursoaia-edu.online/issues)

</div>

<br />

<p align="center">
  <img src="docs/assets/images/projects/arduino/3x3x3_led_cube.jpg" alt="Cub LED 3x3x3 — proiect Arduino" width="720" />
</p>

<br />

## Despre

Suntem un **cerc de informatică condus de elevi** care explorează dezvoltarea web, Python și electronică/IoT prin proiecte concrete. Tot conținutul site-ului — lecții, scheme de cablare, cod sursă, tutoriale pas cu pas — este open-source și disponibil în limba română și engleză.

> Construit pentru elevi de gimnaziu și liceu (11–18 ani), folosit săptămânal în cercul de informatică.

---

## Ce conține

<table>
<tr>
<td width="50%" valign="top">

### Cursuri

| Curs | Lecții | Subiecte cheie |
|------|:------:|----------------|
| [Dezvoltare Web](docs/guide/web/) | **22** | HTML, CSS, JavaScript, Fetch, API |
| [Python](docs/guide/python/) | **12** | Variabile, bucle, funcții, fișiere, Turtle |

</td>
<td width="50%" valign="top">

### Proiecte hardware

| Platformă | Proiecte | Tehnologii |
|-----------|:--------:|-----------|
| [Arduino](docs/projects/arduino/) | 2 | C/C++, multiplexare LED |
| [ESP32](docs/projects/esp32/) | 3 | MicroPython, Wi-Fi, DHT |
| [LoPy](docs/projects/lopy/) | 1 | LoRaWAN, ABP |
| [Raspberry Pi](docs/projects/raspberry_pi/) | — | Pi Pico, C, MicroPython |

</td>
</tr>
</table>

### Statistici

|  |  |
|---|---|
| **35** lecții complete | **6+** proiecte hardware |
| **2** limbi (RO + EN) | **4** platforme hardware |
| **3** proiecte capstone web | **100%** open-source |

---

## Rulează site-ul local

Cerințe: **Python 3.12+** și [`uv`](https://docs.astral.sh/uv/) pentru gestionarea dependențelor.

```bash
# Clonează repo-ul
git clone git@github.com:ursoaia-edu/ursoaia-edu.online.git
cd ursoaia-edu.online

# Instalează dependențele (creează .venv automat)
uv sync

# Pornește serverul de dezvoltare cu live-reload
uv run serve
# → http://127.0.0.1:8000

# Sau construiește site-ul static în ./site
uv run build

# Build strict (eșuează la avertismente — folosit în CI)
uv run build --strict
```

---

## Tehnologii

- **[MkDocs](https://www.mkdocs.org/)** — generator de site static
- **[mkdocs-static-i18n](https://github.com/ultrabug/mkdocs-static-i18n)** — internaționalizare RO + EN
- **[Tailwind CSS](https://tailwindcss.com/)** + **[Lucide icons](https://lucide.dev/)** — styling și iconițe (via CDN)
- **Custom theme** — Jinja2 templates în `custom_theme/`, fără temă MkDocs preconstruită
- **[uv](https://docs.astral.sh/uv/)** — toolchain Python rapid

---

## Structura repo-ului

```
.
├── docs/                        # tot conținutul site-ului
│   ├── index.md / index.en.md   # homepage (RO / EN)
│   ├── assets/
│   │   ├── logo.png             # logo, favicons
│   │   └── images/              # imagini lecții, scheme, foto proiecte
│   ├── guide/                   # cursuri
│   │   ├── index.md             # pagina overview
│   │   ├── web/                 # 22 lecții HTML+CSS+JS
│   │   └── python/              # 12 lecții
│   └── projects/                # proiecte hardware
│       ├── index.md             # pagina overview
│       ├── arduino/
│       ├── esp32/
│       ├── lopy/
│       └── raspberry_pi/
├── custom_theme/                # template MkDocs custom
│   ├── base.html                # shell HTML, nav, language switcher
│   └── main.html                # homepage + inner page layouts
├── mkdocs.yml                   # configurație principală
├── pyproject.toml               # dependențe Python (uv)
├── LICENSE                      # MIT + CC BY 4.0
└── README.md
```

---

## Cum contribui

Contribuțiile sunt binevenite! Idei concrete:

- **Corecții** la lecții, erori de tipar, exemple greșite
- **Proiecte noi** — Arduino, ESP32, LoPy, Raspberry Pi, alte platforme
- **Lecții noi** — îmbunătățiri sau extinderi la cursurile existente
- **Traduceri** — îmbunătățiri la versiunea EN sau alte limbi
- **Design** — sugestii UI/UX pentru site

```bash
# Fork → branch → commit → PR
git checkout -b feature/numele-tau
# fă modificările
uv run build --strict   # verifică că totul construiește
git commit -m "feat: scurtă descriere"
git push origin feature/numele-tau
# deschide Pull Request pe GitHub
```

Sau deschide un [issue](https://github.com/ursoaia-edu/ursoaia-edu.online/issues) cu o idee.

---

## Licență

Proiect **dual-licențiat** — vezi [`LICENSE`](LICENSE) pentru detalii.

| Material | Licență |
|----------|---------|
| Cod (template, scripts, exemple) | **[MIT](LICENSE)** |
| Conținut educațional (lecții, scheme, exerciții) | **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** |

Poți folosi, modifica și redistribui liber, cu atribuire.

---

## Mulțumiri

- **[Arduino](https://arduino.cc)**, **[Espressif](https://espressif.com)**, **[Pycom](https://pycom.io)**, **[Raspberry Pi Foundation](https://raspberrypi.com)** — hardware accesibil
- **[Open-Meteo](https://open-meteo.com)** — API meteo gratuit folosit în cursul Web
- **[Thonny](https://thonny.org)** — IDE Python ideal pentru începători
- **Comunitatea MkDocs** și toți contribuitorii la i18n și theme tooling
- **Toți elevii și mentorii** care contribuie la cerc

---

<div align="center">

Construit de cercul de informatică **Ursoaia** &middot; Site live: [ursoaia-edu.online](https://ursoaia-edu.online)

</div>
