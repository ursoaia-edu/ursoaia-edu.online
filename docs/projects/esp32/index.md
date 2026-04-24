---
title: ESP32
overview: true
tags: [ESP32, IoT, MicroPython, Wi-Fi]
summary: Proiecte ESP32 cu MicroPython — Wi-Fi, senzori, servere web și prototipuri IoT.
---

# Proiecte ESP32

ESP32 este un microcontroller cu **Wi-Fi și Bluetooth integrate**, ideal pentru proiecte IoT, automatizări și mici servere web. Rulează nativ MicroPython — sintaxa Python se aplică direct, fără compilare.

## Proiecte disponibile

### [LED intermitent](led_blink.md)

„Hello World" al sistemelor integrate — aprinde și stinge LED-ul integrat (GPIO 2) cu MicroPython. Include și un exemplu **LED chaser** pe pini consecutivi.

- **Componente:** ESP32, LED extern (opțional), rezistență 220 Ω
- **Concepte:** GPIO, ciclu de viață al unui script MicroPython
- **Dificultate:** începător

---

### [Temperatură și umiditate](temperature.md)

Citește un senzor **DHT22** (sau DHT11) și afișează valorile pe consola serială la fiecare 2 secunde.

- **Componente:** ESP32, DHT22/DHT11, rezistență pull-up 10 kΩ
- **Concepte:** comunicare 1-wire, manipulare excepții, formatarea outputului
- **Dificultate:** începător-mediu

---

### [Server web pentru temperatură](temperature_web.md)

Combină Wi-Fi-ul ESP32 cu senzorul DHT22 — servește o **pagină HTML stilizată** cu citirile live, accesibilă din browser-ul oricărui dispozitiv din aceeași rețea.

- **Componente:** ESP32, DHT22, conexiune Wi-Fi
- **Concepte:** socket TCP, HTTP de bază, format string-uri HTML
- **Dificultate:** mediu

---

## De ce ESP32?

| Caracteristică | Detaliu |
|----------------|---------|
| **CPU** | Dual-core 240 MHz (mult mai rapid decât Arduino Uno) |
| **Memorie** | 520 KB RAM, 4 MB Flash |
| **Wi-Fi** | 802.11 b/g/n integrat |
| **Bluetooth** | Classic + BLE |
| **Pini I/O** | 30+ GPIO, ADC, DAC, PWM |
| **Preț** | ~5–10 € per placă |

## Instrumente

- **[Thonny](https://thonny.org/)** — IDE recomandat pentru MicroPython (vine cu suport ESP32)
- **[esptool.py](https://github.com/espressif/esptool)** — flash firmware MicroPython pe ESP32
- **[MicroPython firmware](https://micropython.org/download/esp32/)** — descarcă varianta ESP32 generic

## De unde să începi

1. **Flashează MicroPython** pe ESP32 cu `esptool.py`
2. Conectează cu Thonny (selectează interpreter „MicroPython (ESP32)")
3. Rulează prima dată [LED intermitent](led_blink.md) pentru a verifica setup-ul
4. Continuă cu senzorul de temperatură, apoi serverul web

!!! tip "Vii din lumea Arduino?"
    Sintaxa e diferită — Python în loc de C++ — dar conceptele sunt identice (GPIO, sleep, interrupt, comunicare). Avantajul MicroPython e că **nu trebuie să compilezi** la fiecare modificare; codul rulează direct.

!!! note "Diferența dintre ESP32 și ESP8266"
    ESP8266 e mai vechi și mai limitat (doar Wi-Fi, mai puțin RAM). Pentru proiecte noi recomandăm ESP32.
