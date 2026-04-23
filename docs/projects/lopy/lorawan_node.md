---
category: LoPy
tags: [LoRa, LoRaWAN, ABP, IoT]
summary: Configure a Pycom LoPy4 for the EU868 LoRaWAN network using ABP activation and send periodic payloads.
---

# LoPy LoRaWAN Node

Connecting a Pycom LoPy4 to a LoRaWAN network using ABP (Activation By Personalization) and sending data.

## Description

This project demonstrates how to configure the LoPy4 to join a LoRaWAN network in the EU868 region. It uses ABP for quick activation and sends a simple 4-byte payload periodically.

## Code

### boot.py

The `boot.py` file handles the network joining process.

```python
import os
import binascii
import time
import machine
import pycom
import struct
from network import LoRa

# Disable heartbeat LED
pycom.heartbeat(False)

# LoRaWAN Configuration
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# ABP Credentials (replace with your own)
dev_addr = struct.unpack(">l", binascii.unhexlify('26011346'))[0]
nwk_swkey = binascii.unhexlify('0619AB7D261950743D46D701AD9903DD')
app_swkey = binascii.unhexlify('8FBE002AA5008BCC52638CF2D33A6A10')

# Join network
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# Wait for join
pycom.rgbled(0xffff00) # Yellow
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')
pycom.rgbled(0x0000ff) # Blue
time.sleep(1)
pycom.rgbled(0x000000)
```

### main.py

The `main.py` file handles data transmission.

```python
import socket
import pycom
from time import sleep

# Create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# Set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

count = 0
while True:
    s.setblocking(True)
    # Send data (Example payload: 0x01, 0x67, 0x00, 0x96)
    s.send(bytes([0x01, 0x67, 0x00, 0x96]))
    s.setblocking(False)

    print(f"Sent packet #{count}")

    # Receive downlink data (optional)
    data = s.recv(64)
    if data:
        print(f"Received: {data}")

    count += 1
    sleep(10) # Wait before next transmission
```

## How it works

1. **LoRa Stack:** The `network.LoRa` module is used to initialize the LoRa radio in LoRaWAN mode.
2. **ABP Joining:** Unlike OTAA (Over-the-Air Activation), ABP uses hardcoded session keys. It doesn't require a handshake with the gateway, making it faster but less secure for production.
3. **Data Transmission:** A standard BSD-style socket is used to send data over the LoRa network.
4. **Payload:** The sample payload `[0x01, 0x67, 0x00, 0x96]` is typical for Cayenne LPP (Low Power Payload) format, where `0x67` represents temperature.

## Reference

- [Pycom Documentation: LoRaWAN](https://docs.pycom.io/tutorials/networks/lora/lorawan-abp/)
