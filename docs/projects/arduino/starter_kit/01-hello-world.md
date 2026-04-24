---
category: Arduino
tags: [Arduino, Serial, Începători, Uno]
summary: Primul proiect — trimiți "Hello World!" de la Arduino către PC prin portul serial și confirmi că totul funcționează.
---

# Proiect 01 — Hello World

Acesta este primul pas în lumea Arduino. Nu ai nevoie de nicio componentă în afară de placă și cablul USB. Vei învăța cum se face comunicarea serială între Arduino și calculator și vei folosi pentru prima dată **Serial Monitor**-ul din Arduino IDE.

## Componente necesare

| Componentă | Cantitate |
|------------|-----------|
| Arduino Uno R3 (CH340) | 1 |
| Cablu USB A–B | 1 |

## Cum funcționează

Arduino poate comunica cu calculatorul prin intermediul cablului USB, folosind un protocol numit **UART** (comunicare serială asincronă). În Arduino IDE există o fereastră specială — **Serial Monitor** — care îți afișează mesajele primite de la placă și îți permite să trimiți date către ea.

În acest proiect vei face exact asta: când apeși litera `A` și trimiți prin Serial Monitor, Arduino va clipi LED-ul de pe pinul 13 (LED-ul încorporat pe placă) și îți va răspunde cu textul `Hello World!`.

Viteza de comunicare (**baud rate**) trebuie să fie aceeași și pe Arduino, și în Serial Monitor — folosim `9600` ca valoare standard pentru proiecte simple.

## Conectare

Nu este nevoie de conexiuni suplimentare. Folosești **LED-ul integrat** pe pinul 13 și comunicarea serială de pe pinii `0 (RX)` și `1 (TX)`, rutată prin USB.

```board
    [ Arduino Uno ]  ──USB──  [ PC / Laptop ]
           │
           └── LED 13 (integrat, clipește când primește 'A')
```

## Cod

```cpp
/*
 * Proiect 1 — Hello World
 * Trimite "Hello World!" când primește caracterul 'A' prin Serial.
 */

int ledPin = 13;            // LED-ul integrat pe placa Arduino
int serialData = 0;         // Variabilă pentru datele primite

void setup() {
  Serial.begin(9600);       // Pornim comunicarea serială la 9600 baud
  pinMode(ledPin, OUTPUT);  // Pinul 13 este ieșire (output)
}

void loop() {
  // Dacă s-a primit un caracter prin portul serial
  if (Serial.available()) {
    serialData = Serial.read();

    // Dacă este litera 'A' (majusculă)
    if (serialData == 'A') {
      digitalWrite(ledPin, HIGH);
      delay(500);
      digitalWrite(ledPin, LOW);
      delay(500);
      Serial.println("Hello World!");
    }
  }
}
```

## Ce să încerci

- Schimbă mesajul în `Salut, lume!` și vezi cum apare în Serial Monitor.
- Fă LED-ul să clipească de 3 ori în loc de 1 — folosește `for`.
- Adaugă o a doua comandă: la litera `B`, Arduino să răspundă cu numele tău.
- Schimbă `baud rate`-ul la `115200` (trebuie schimbat și în Serial Monitor).

## Note

- După upload, apasă butonul **Serial Monitor** (pictograma lupei, dreapta-sus în IDE).
- Asigură-te că **baud rate**-ul selectat în partea de jos a Serial Monitor-ului este `9600`.
- Dacă nu vezi niciun răspuns, verifică din **Tools → Port** că portul COM este cel corect.

---

**Vezi și:** [Toate proiectele kit-ului](kits.md)
