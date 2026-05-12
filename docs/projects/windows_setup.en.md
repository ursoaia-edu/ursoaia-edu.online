---
title: Windows setup
category: Setup
tags: [Windows, driver, CH340, Arduino, ESP32]
summary: What you need on a Windows PC before starting Arduino, ESP32, and LoPy projects — CH340 driver, Arduino IDE, ESP32 support.
---

Before you open the first project, your Windows PC needs a few pieces of software: a driver so the OS can "see" the board over USB, the Arduino IDE to compile and upload code, and ESP32 support if you also want to work with that platform. The steps below are a one-time setup.

!!! tip "Who this is for"
    This guide targets **Windows 10 / 11** users. On macOS and Linux the steps differ (usually no CH340 driver is needed) — ask us if you are on another OS.

## 1. Install the CH340 driver (for Arduino UNO)

Our Arduino UNO board uses the **CH340** chip for USB-Serial communication. Windows does not recognize it out of the box, so an official driver has to be installed.

1. Download the archive: [**CH34x_Install_Windows_v3_4.zip**](https://www.dropbox.com/scl/fi/acgidpsfj2461kk19dncx/CH34x_Install_Windows_v3_4.zip?rlkey=5gptifm6eh24i327e4395iq0u&st=4vpiwcyd&dl=0)
2. Extract it (right-click → **Extract All**).
3. Run `CH34x_Install_Windows_v3_4.exe` (double-click; approve the UAC prompt).
4. Click **Install** and wait for the "Driver install success" message.
5. Plug the Arduino board into a USB port.

### Verify the install

1. Open **Device Manager** (`Win + X` → *Device Manager*).
2. Expand **Ports (COM & LPT)**.
3. You should see an entry like `USB-SERIAL CH340 (COMx)` — `COMx` is the port number (e.g. `COM3`, `COM7`). Remember this number; you will pick it in the Arduino IDE.

!!! warning "Board not showing up?"
    See the [Troubleshooting](#troubleshooting) section below.

## 2. Install the Arduino IDE

The Arduino IDE is the editor where you write code, compile it, and upload it to the board.

1. Go to [arduino.cc/en/software](https://www.arduino.cc/en/software).
2. Download **Arduino IDE 2.x** for Windows (the *Installer* build).
3. Run the installer with the default settings.
4. On first launch, allow Windows to install any additional drivers it prompts for.

Verify the install:

1. Open the Arduino IDE.
2. **Tools → Board → Arduino AVR Boards → Arduino Uno**.
3. **Tools → Port → COMx** (the port from the previous step).

If the board is plugged in and the driver is correct, the port appears in the list.

## 3. Add ESP32 support

ESP32 is not bundled with the Arduino IDE — you add it through **Boards Manager**.

1. Open the Arduino IDE.
2. **File → Preferences**.
3. In **Additional Boards Manager URLs** paste:
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
   If other URLs are already there, separate them with a comma.
4. Click **OK**.
5. **Tools → Board → Boards Manager…**
6. Search for `esp32` and install **esp32 by Espressif Systems** (this may take a few minutes).

After install:

- **Tools → Board → esp32** lists dozens of variants (e.g. `ESP32 Dev Module`, `WEMOS LOLIN32`). Pick yours.
- The CH340 driver from step 1 is enough for most ESP32 dev kits. Some boards use the **CP2102** chip — if the port does not appear, install the [Silicon Labs CP210x driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) separately.

## 4. (Optional) Install Thonny for MicroPython

If you want to program the ESP32 or **LoPy** in **MicroPython** (Python syntax, no compile step), install Thonny:

1. Go to [thonny.org](https://thonny.org).
2. Download the Windows build and install it.
3. Open Thonny → **Tools → Options → Interpreter** → choose *MicroPython (ESP32)* and the board's COM port.

Thonny is friendlier than the Arduino IDE for beginners coming from the [Python course](../courses/python/index.md).

## Troubleshooting

??? question "The COM port does not show up in Arduino IDE / Device Manager"
    - Check the **USB cable**. Many cheap cables are "power only" and carry no data. Try another cable — preferably the one that shipped with the board.
    - Try **another USB port** on the computer (preferably one directly on the motherboard, not through a hub).
    - **Reinstall the CH340 driver** (step 1).
    - Open Device Manager with the board plugged in — if you see a device with a yellow exclamation mark, right-click → *Update driver* → *Browse my computer* and point to the folder where you extracted `CH34x_Install_Windows_v3_4`.

??? question "'Access is denied' or 'Port busy' on upload"
    - Close any other app using the port (another Arduino IDE window, an external Serial Monitor, Thonny, etc.).
    - In Device Manager, check that there is no other locked instance of the port.

??? question "Upload fails with 'A fatal error occurred: Failed to connect to ESP32'"
    - Press and hold the **BOOT** button on the ESP32 board while the Arduino IDE starts uploading. Release it when you see "Connecting…".
    - On some boards you also need to briefly press **EN/RST** and release.

## Next step

Now that the PC is ready, pick a platform from the [Projects page](index.md) and start with the first tutorial — typically [Hello World on Arduino](arduino/starter_kit/01-hello-world.md).
