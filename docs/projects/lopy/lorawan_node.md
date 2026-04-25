---
category: LoPy
tags: [LoRa, LoRaWAN, ABP, IoT]
summary: Configurează un Pycom LoPy4 pentru rețeaua LoRaWAN EU868 folosind activarea ABP și transmite payload-uri periodice.
image: assets/images/projects/lopy/preview-lorawan-node.jpg
---

# Nod LoRaWAN pe LoPy

Conectarea unui Pycom LoPy4 la o rețea LoRaWAN folosind ABP (Activation By Personalization) și trimiterea de date.

![Nod LoRaWAN — Pycom LoPy4 configurat pentru EU868](../../assets/images/projects/lopy/preview-lorawan-node.jpg)

## Descriere

Acest proiect demonstrează cum să configurezi LoPy4 pentru a se alătura unei rețele LoRaWAN în regiunea EU868. Folosește ABP pentru activare rapidă și trimite un payload simplu de 4 octeți periodic.

## Cod

### boot.py

Fișierul `boot.py` gestionează procesul de conectare la rețea.

```python
import os
import binascii
import time
import machine
import pycom
import struct
from network import LoRa

# Dezactivează LED-ul heartbeat
pycom.heartbeat(False)

# Configurare LoRaWAN
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# Credențiale ABP (înlocuiește cu ale tale)
dev_addr = struct.unpack(">l", binascii.unhexlify('26011346'))[0]
nwk_swkey = binascii.unhexlify('0619AB7D261950743D46D701AD9903DD')
app_swkey = binascii.unhexlify('8FBE002AA5008BCC52638CF2D33A6A10')

# Conectare la rețea
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# Asteaptă conectarea
pycom.rgbled(0xffff00) # Galben
while not lora.has_joined():
    time.sleep(2.5)
    print('Nu s-a conectat inca...')

print('Retea jonata!')
pycom.rgbled(0x0000ff) # Albastru
time.sleep(1)
pycom.rgbled(0x000000)
```

### main.py

Fișierul `main.py` gestionează transmisia de date.

```python
import socket
import pycom
from time import sleep

# Creează un socket LoRa
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# Setează rata de date LoRaWAN
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

count = 0
while True:
    s.setblocking(True)
    # Trimite date (Payload exemplu: 0x01, 0x67, 0x00, 0x96)
    s.send(bytes([0x01, 0x67, 0x00, 0x96]))
    s.setblocking(False)

    print(f"Pachet #{count} trimis")

    # Primește date downlink (opțional)
    data = s.recv(64)
    if data:
        print(f"Primit: {data}")

    count += 1
    sleep(10) # Asteaptă înainte de următoarea transmisie
```

## Cum funcționează

1. **Stiva LoRa:** Modulul `network.LoRa` este folosit pentru a inițializa radio-ul LoRa în modul LoRaWAN.
2. **Conectare ABP:** Spre deosebire de OTAA (Over-the-Air Activation), ABP folosește chei de sesiune hardcodate. Nu necesită un handshake cu gateway-ul, ceea ce îl face mai rapid, dar mai puțin sigur pentru producție.
3. **Transmisia datelor:** Un socket standard de tip BSD este folosit pentru a trimite date peste rețeaua LoRa.
4. **Payload:** Payload-ul exemplu `[0x01, 0x67, 0x00, 0x96]` este tipic pentru formatul Cayenne LPP (Low Power Payload), unde `0x67` reprezintă temperatura.

## Referințe

- [Documentația Pycom: LoRaWAN](https://docs.pycom.io/tutorials/networks/lora/lorawan-abp/)
