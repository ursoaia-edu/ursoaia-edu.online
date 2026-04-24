---
title: Arduino
overview: true
tags: [Arduino, electronics, microcontroller, C++]
summary: Arduino projects with schematics, code, and bills of materials — from first LED to multiplexed cubes and starter kits.
---

# Arduino Projects

Arduino boards are the perfect entry point into electronics. With a simplified C/C++ dialect and a friendly IDE, they're ideal for first hardware projects. All projects here ship with full wiring diagrams, source code, and component lists.

## Available projects

### [3x3x3 LED Cube](led_cube.md)

Build a 27-LED cube driven via **layer multiplexing** with POV animations. 9 columns wire directly to GPIO; 3 layers are switched through NPN transistors.

- **Components:** Arduino Uno, 27× LED, resistors, 2N2222 transistors, breadboard
- **Concepts:** multiplexing, POV (persistence of vision), GPIO control
- **Difficulty:** medium

---

### [Arduino Starter Kits](starter_kit/kits.md)

All **25 projects** from the Super Starter Kit for Arduino UNO (CH340) — from "Hello World" up to stepper motors controlled by IR remote. Each project comes with description, wiring diagram, and ready-to-flash code.

- **Audience:** absolute beginners and intermediate
- **Components:** complete LA036 kit
- **Concepts:** GPIO, PWM, I2C, ADC, serial communication, sensors, actuators

---

## Resources

- [Official Arduino site](https://www.arduino.cc/)
- [Arduino IDE — download](https://www.arduino.cc/en/software)
- [Arduino language reference](https://www.arduino.cc/reference/en/)
- [Tinkercad Circuits](https://www.tinkercad.com/circuits) — free online simulator

## Where to start

If you're a complete beginner:

1. Install **Arduino IDE** and connect your board
2. Start with [Hello World](starter_kit/01-hello-world.md) from the Starter Kit
3. Continue with LEDs, buttons, sensors — in the kit's project order
4. Tackle the [3x3x3 LED Cube](led_cube.md) as a more challenging project

!!! tip "First time with C++?"
    Arduino uses a simplified C/C++ dialect. The key functions are `setup()` (runs once on boot) and `loop()` (runs forever in a loop). You'll pick up the rest from the projects.
