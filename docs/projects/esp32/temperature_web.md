---
category: ESP32
tags: [Sensor, Web Server, WiFi, MicroPython]
---

# Temperature and Humidity Web Server

Reads temperature and humidity from a DHT22 (or DHT11) sensor connected to an ESP32 and serves the values over a simple HTTP web page using MicroPython.

## Description

The project consists of a single `main.py` file that:
1. Connects the ESP32 to your Wi-Fi network.
2. Initialises the DHT11/DHT22 sensor.
3. Opens a TCP socket on port 80.
4. Waits for HTTP connections and responds with a styled HTML page showing current sensor readings.

## Code

```python
import network
import time
from machine import Pin
import dht
try:
  import usocket as socket
except:
  import socket

# Configuration
ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'

# Connect to Wi-Fi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
  print('Waiting for connection...')
  time.sleep(1)

print('Connection successful')
print(station.ifconfig())

# Sensor setup
sensor = dht.DHT11(Pin(4))
# sensor = dht.DHT22(Pin(4))

def read_sensor():
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return temp, hum
  except OSError as e:
    print('Failed to read sensor.')
    return 0, 0

def web_page(temp, hum):
  html = f"""<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css">
  <style>
    html {{ font-family: Arial; display: inline-block; margin: 0px auto; text-align: center; }}
    h2 {{ font-size: 3.0rem; }}
    p {{ font-size: 3.0rem; }}
    .units {{ font-size: 1.2rem; }}
    .dht-labels{{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }}
  </style>
</head>
<body>
  <h2>ESP DHT Server</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i>
    <span class="dht-labels">Temperature</span>
    <span>{temp}</span>
    <sup class="units">&deg;C</sup>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i>
    <span class="dht-labels">Humidity</span>
    <span>{hum}</span>
    <sup class="units">%</sup>
  </p>
</body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  temp, hum = read_sensor()
  response = web_page(temp, hum)
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
```

## Wiring

### DHT22 (or DHT11) to ESP32

```
DHT22 Pin  →  ESP32
---------     -----
VCC (1)    →  3.3V
DATA (2)   →  GPIO 4
GND (4)    →  GND
```

### Wiring Diagram

![ESP32 dht22 wifi](../../assets/images/projects/esp32/016-esp32-micropython-wifi-ap-techtotinker-diagram.png)

---

## Reference

- [016 - ESP32 MicroPython: Web Server | ESP32 Access Point](https://techtotinker.com/016-esp32-micropython-web-server-esp32-access-point-mode-in-micropython/)
