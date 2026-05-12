---
title: Pregătire Windows
category: Setup
tags: [Windows, driver, CH340, Arduino, ESP32]
summary: Pașii necesari pe un calculator cu Windows înainte de a începe proiectele Arduino, ESP32 și LoPy — driver CH340, Arduino IDE, suport ESP32.
---

Înainte de a deschide primul proiect, calculatorul tău cu Windows are nevoie de câteva piese de software: un driver ca să „vadă" placa prin USB, Arduino IDE pentru a compila și încărca cod, și suportul pentru ESP32 dacă vrei să lucrezi și cu acea platformă. Toți pașii de mai jos se fac o singură dată.

!!! tip "Cui i se adresează"
    Acest ghid e pentru utilizatorii **Windows 10 / 11**. Pe macOS și Linux pașii sunt diferiți (în general, driverul CH340 nu e necesar) — întreabă-ne dacă lucrezi pe alt sistem.

## 1. Instalează driverul CH340 (pentru Arduino UNO)

Placa noastră de Arduino UNO folosește chip-ul **CH340** pentru comunicarea USB-Serial. Windows-ul nu îl recunoaște din start, așa că trebuie instalat un driver oficial.

1. Descarcă arhiva: [**CH34x_Install_Windows_v3_4.zip**](https://www.dropbox.com/scl/fi/acgidpsfj2461kk19dncx/CH34x_Install_Windows_v3_4.zip?rlkey=5gptifm6eh24i327e4395iq0u&st=4vpiwcyd&dl=0)
2. Dezarhivează (click dreapta → **Extract All**).
3. Rulează `CH34x_Install_Windows_v3_4.exe` (dublu-click; aprobă fereastra UAC).
4. Apasă **Install** și așteaptă mesajul „Driver install success".
5. Conectează placa Arduino prin USB.

### Verifică instalarea

1. Deschide **Device Manager** (`Win + X` → *Device Manager*).
2. Extinde secțiunea **Ports (COM & LPT)**.
3. Trebuie să vezi o intrare de forma `USB-SERIAL CH340 (COMx)` — `COMx` este numărul portului (ex. `COM3`, `COM7`). Ține minte acest număr, îl vei selecta în Arduino IDE.

!!! warning "Placa nu apare?"
    Vezi secțiunea [Probleme frecvente](#probleme-frecvente) de mai jos.

## 2. Instalează Arduino IDE

Arduino IDE este editorul în care scrii cod, compilezi și încarci programe pe placă.

1. Mergi pe [arduino.cc/en/software](https://www.arduino.cc/en/software).
2. Descarcă **Arduino IDE 2.x** pentru Windows (varianta *Installer*).
3. Rulează instalatorul cu setările implicite.
4. La primă pornire, lasă Windows-ul să instaleze driverele suplimentare propuse.

Verifică instalarea:

1. Deschide Arduino IDE.
2. **Tools → Board → Arduino AVR Boards → Arduino Uno**.
3. **Tools → Port → COMx** (portul detectat la pasul anterior).

Dacă placa e conectată și driverul e instalat corect, vei vedea portul în listă.

## 3. Adaugă suportul pentru ESP32

ESP32 nu vine preinstalat în Arduino IDE — trebuie adăugat prin **Boards Manager**.

1. Deschide Arduino IDE.
2. **File → Preferences**.
3. La câmpul **Additional Boards Manager URLs** lipește:
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
   Dacă există deja alte URL-uri, separă-le cu virgulă.
4. Apasă **OK**.
5. **Tools → Board → Boards Manager…**
6. Caută `esp32` și instalează pachetul **esp32 by Espressif Systems** (poate dura câteva minute).

După instalare:

- **Tools → Board → esp32** va lista zeci de variante (ex. `ESP32 Dev Module`, `WEMOS LOLIN32`). Alege-o pe a ta.
- Driverul CH340 instalat la pasul 1 e suficient pentru majoritatea plăcilor ESP32 dev-kit. Unele plăci folosesc chip-ul **CP2102** — dacă portul nu apare, instalează separat [driverul Silicon Labs CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).

## 4. (Opțional) Instalează Thonny pentru MicroPython

Dacă vrei să programezi ESP32 sau **LoPy** în **MicroPython** (sintaxă Python, fără compilare), instalează Thonny:

1. Mergi pe [thonny.org](https://thonny.org).
2. Descarcă varianta pentru Windows și instaleaz-o.
3. Deschide Thonny → **Tools → Options → Interpreter** → alege *MicroPython (ESP32)* și portul COM al plăcii.

Thonny e mai prietenos decât Arduino IDE pentru începătorii care vin de la cursul de [Python](../courses/python/index.md).

## Probleme frecvente

??? question "Portul COM nu apare în Arduino IDE / Device Manager"
    - Verifică **cablul USB**. Multe cabluri ieftine sunt „doar alimentare" și nu transmit date. Încearcă alt cablu — preferabil cel care a venit cu placa.
    - Încearcă **alt port USB** pe calculator (de preferat un port direct pe placa de bază, nu printr-un hub).
    - **Reinstalează driverul CH340** (pasul 1).
    - Deschide Device Manager cu placa conectată — dacă vezi un dispozitiv cu semn de exclamare galben, click dreapta → *Update driver* → *Browse my computer* și indică folderul în care ai dezarhivat `CH34x_Install_Windows_v3_4`.

??? question "„Access is denied" sau „Port busy" la upload"
    - Închide orice altă aplicație care folosește portul (alt Arduino IDE, Serial Monitor extern, Thonny etc.).
    - Verifică în Device Manager că nu e altă instanță a portului blocată.

??? question "Upload eșuează cu „A fatal error occurred: Failed to connect to ESP32" "
    - Apasă și ține apăsat butonul **BOOT** de pe placa ESP32 în timp ce Arduino IDE începe upload-ul. Eliberează-l când vezi „Connecting…".
    - Pe unele plăci e nevoie să apeși și **EN/RST** scurt, apoi să eliberezi.

## Următorul pas

Acum că PC-ul e gata, alege o platformă din [pagina Proiecte](index.md) și începe cu primul tutorial — de regulă [Hello World pe Arduino](arduino/starter_kit/01-hello-world.md).
