---
title: ESP32
overview: true
tags: [ESP32, IoT, MicroPython, Wi-Fi]
summary: ESP32 projects with MicroPython — Wi-Fi, sensors, web servers, and IoT prototypes.
---

# ESP32 Projects

The ESP32 is a microcontroller with **built-in Wi-Fi and Bluetooth**, ideal for IoT projects, automation, and small web servers. It runs MicroPython natively — Python syntax applies directly, no compilation needed.

## Available projects

### [LED Blink](led_blink.md)

The "Hello World" of embedded systems — toggles the on-board LED (GPIO 2) using MicroPython. Includes a **LED chaser** example across consecutive pins.

- **Components:** ESP32, external LED (optional), 220 Ω resistor
- **Concepts:** GPIO, lifecycle of a MicroPython script
- **Difficulty:** beginner

---

### [Temperature & Humidity](temperature.md)

Reads a **DHT22** (or DHT11) sensor and prints values to the serial console every 2 seconds.

- **Components:** ESP32, DHT22/DHT11, 10 kΩ pull-up resistor
- **Concepts:** 1-wire communication, exception handling, output formatting
- **Difficulty:** beginner-intermediate

---

### [Temperature Web Server](temperature_web.md)

Combines ESP32's Wi-Fi with the DHT22 sensor — serves a **styled HTML page** with live readings, accessible from any browser on the same network.

- **Components:** ESP32, DHT22, Wi-Fi connection
- **Concepts:** TCP socket, basic HTTP, HTML string formatting
- **Difficulty:** intermediate

---

## Why ESP32?

| Feature | Detail |
|---------|--------|
| **CPU** | Dual-core 240 MHz (much faster than Arduino Uno) |
| **Memory** | 520 KB RAM, 4 MB Flash |
| **Wi-Fi** | 802.11 b/g/n built-in |
| **Bluetooth** | Classic + BLE |
| **I/O pins** | 30+ GPIO, ADC, DAC, PWM |
| **Price** | ~5–10 € per board |

## Tools

- **[Thonny](https://thonny.org/)** — recommended IDE for MicroPython (ESP32 support built-in)
- **[esptool.py](https://github.com/espressif/esptool)** — flash MicroPython firmware to ESP32
- **[MicroPython firmware](https://micropython.org/download/esp32/)** — get the generic ESP32 build

## Where to start

1. **Flash MicroPython** onto your ESP32 with `esptool.py`
2. Connect via Thonny (pick "MicroPython (ESP32)" interpreter)
3. Run [LED Blink](led_blink.md) first to verify your setup
4. Continue with the temperature sensor, then the web server

!!! tip "Coming from Arduino?"
    Syntax is different — Python instead of C++ — but the concepts are the same (GPIO, sleep, interrupt, communication). The MicroPython advantage: **no compile step** on every change; code runs directly.

!!! note "ESP32 vs ESP8266"
    ESP8266 is older and more limited (only Wi-Fi, less RAM). For new projects we recommend ESP32.
