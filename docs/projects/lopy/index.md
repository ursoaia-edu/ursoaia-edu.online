---
title: LoPy
overview: true
tags: [LoPy, Pycom, LoRa, LoRaWAN, IoT]
summary: Proiecte Pycom LoPy cu LoRa și LoRaWAN — senzori IoT pe rază lungă cu consum redus.
---

# Proiecte LoPy

**Pycom LoPy** este o placă de dezvoltare cu radio **LoRa** integrat, perfectă pentru proiecte IoT care trimit cantități mici de date pe distanțe lungi (până la 10+ km în câmp deschis) cu consum foarte redus de energie.

Rulează MicroPython, are Wi-Fi și Bluetooth în plus față de LoRa, și se programează identic cu ESP32-ul.

## Proiecte disponibile

### [Nod LoRaWAN](lorawan_node.md)

Configurează un **Pycom LoPy4** pentru rețeaua LoRaWAN EU868 folosind activarea **ABP** (Activation By Personalization) și transmite payload-uri periodice.

- **Componente:** Pycom LoPy4, antenă LoRa, conexiune la un gateway LoRaWAN
- **Concepte:** LoRaWAN, ABP vs OTAA, format Cayenne LPP, socket-uri pe radio
- **Dificultate:** mediu-avansat

---

## Ce e LoRa și LoRaWAN?

- **LoRa** = tehnologie radio pentru comunicare pe distanțe lungi cu consum mic. Modulează la rate joase (250 bps – 50 kbps) pentru a maximiza raza de acțiune.
- **LoRaWAN** = protocol de rețea peste LoRa, cu autentificare, criptare și roaming între gateway-uri. The Things Network (TTN) e cea mai mare rețea publică LoRaWAN.

| Aspect | LoRa | Wi-Fi | Bluetooth |
|--------|------|-------|-----------|
| Rază | 2-15 km | 50 m | 10 m |
| Consum | foarte mic | mediu | mic |
| Bandwidth | 250 bps - 50 kbps | mbps | mbps |
| Use case | senzori IoT distribuiți | rețea locală rapidă | dispozitive personale |

## Resurse

- [Documentația Pycom](https://docs.pycom.io/) — ghiduri oficiale și API reference
- [The Things Network](https://www.thethingsnetwork.org/) — rețea LoRaWAN publică gratuită
- [TTN Mapper](https://ttnmapper.org/) — verifică acoperirea LoRaWAN în zona ta
- [LoRa Calculator](https://avbentem.github.io/airtime-calculator/ttn/eu868) — calculează durata transmisiei

## De unde să începi

1. **Verifică acoperirea TTN** în zona ta cu TTN Mapper
2. Dacă există un gateway aproape: înregistrează-te pe TTN și creează o aplicație
3. Conectează LoPy la PC, instalează **Pymakr** (extensie VS Code) sau **Pycom Firmware Updater**
4. Urmează lecția [Nod LoRaWAN](lorawan_node.md) cu credențialele tale

!!! warning "Antenă obligatorie"
    NU pornești niciodată LoPy fără antenă LoRa conectată — riști să arzi modulul radio. Antena vine de obicei în pachet cu placa.

!!! tip "Alternativă fără gateway"
    Dacă nu ai un gateway TTN aproape, poți cumpăra unul mic (~100€) sau folosi modul **point-to-point** între două LoPy-uri pentru experimente locale.
