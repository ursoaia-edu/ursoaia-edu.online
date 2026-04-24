---
title: LoPy
overview: true
tags: [LoPy, Pycom, LoRa, LoRaWAN, IoT]
summary: Pycom LoPy projects with LoRa and LoRaWAN — long-range, low-power IoT sensors.
---

# LoPy Projects

**Pycom LoPy** is a development board with built-in **LoRa** radio, perfect for IoT projects that transmit small amounts of data over long distances (up to 10+ km in open field) with very low power consumption.

It runs MicroPython, has Wi-Fi and Bluetooth in addition to LoRa, and is programmed identically to ESP32.

## Available projects

### [LoRaWAN Node](lorawan_node.md)

Configure a **Pycom LoPy4** for the LoRaWAN EU868 network using **ABP** (Activation By Personalization) and transmit periodic payloads.

- **Components:** Pycom LoPy4, LoRa antenna, connection to a LoRaWAN gateway
- **Concepts:** LoRaWAN, ABP vs OTAA, Cayenne LPP format, radio sockets
- **Difficulty:** intermediate-advanced

---

## What's LoRa and LoRaWAN?

- **LoRa** = radio technology for long-range, low-power communication. Modulates at low rates (250 bps – 50 kbps) to maximize range.
- **LoRaWAN** = network protocol on top of LoRa with authentication, encryption, and roaming across gateways. The Things Network (TTN) is the largest public LoRaWAN network.

| Aspect | LoRa | Wi-Fi | Bluetooth |
|--------|------|-------|-----------|
| Range | 2-15 km | 50 m | 10 m |
| Power | very low | medium | low |
| Bandwidth | 250 bps - 50 kbps | mbps | mbps |
| Use case | distributed IoT sensors | local fast network | personal devices |

## Resources

- [Pycom documentation](https://docs.pycom.io/) — official guides and API reference
- [The Things Network](https://www.thethingsnetwork.org/) — free public LoRaWAN network
- [TTN Mapper](https://ttnmapper.org/) — check LoRaWAN coverage in your area
- [LoRa Calculator](https://avbentem.github.io/airtime-calculator/ttn/eu868) — compute transmission airtime

## Where to start

1. **Check TTN coverage** in your area with TTN Mapper
2. If a gateway is nearby: register on TTN and create an application
3. Connect LoPy to your PC, install **Pymakr** (VS Code extension) or **Pycom Firmware Updater**
4. Follow the [LoRaWAN Node](lorawan_node.md) lesson with your credentials

!!! warning "Antenna required"
    NEVER power on LoPy without the LoRa antenna connected — you risk burning the radio module. The antenna usually comes in the box with the board.

!!! tip "No gateway nearby?"
    If there's no TTN gateway in range, you can buy a small one (~100€) or use **point-to-point** mode between two LoPy boards for local experiments.
