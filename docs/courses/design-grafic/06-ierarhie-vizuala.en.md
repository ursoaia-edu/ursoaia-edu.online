---
lesson: 6
tags: [hierarchy, contrast, attention, scanning, design]
summary: How you decide what the reader sees first — the six contrast levers, the reading path and how to repair a broken hierarchy.
---

# Lesson 06 · Visual hierarchy

!!! tip "What you will learn"
    - What **visual hierarchy** is and why it is the final test of any design
    - The **six levers** you use to create contrast
    - The **reading path**: Z, F and the entry point
    - The **three levels** rule
    - How to diagnose and repair a broken hierarchy
    - How all of it applies in an interface, not just on a poster

---

## What visual hierarchy is

**Visual hierarchy is the order in which the reader notices things.** It always exists — the only question is whether you controlled it or it happened by itself.

The test is simple and brutal: show the design to someone for 3 seconds, then ask what they saw first. If the answer is not your most important piece of information, the hierarchy is wrong. Not "debatable" — wrong.

!!! note "Hierarchy is not optional"
    A design without hierarchy is not "neutral". If every element has the same visual weight, the reader has to process all of them to work out what matters. Most people do not make that effort; they simply leave.

---

## The six contrast levers

You have exactly six ways to make one element more important than another. You can combine them, but you do not need all of them.

### 1. Size

The most direct one. An element twice as large gets read first.

**The rule:** for the difference to read as **intentional**, the jump must be at least **1.5×**. 18 px next to 20 px looks like a mistake; 18 px next to 32 px looks like a decision.

### 2. Weight

Bold vs. Regular, within the same font. Discreet, very useful in body text where you cannot change the size.

**The limit:** if you bold half the text, nothing stands out any more. Bold only works while it stays rare.

### 3. Colour

A coloured element on a neutral background jumps out immediately. It works even at small sizes — that is why the red notification dot is 8 px and you still see it.

**The limit:** with four accent colours you no longer have an accent.

### 4. Space

An isolated element with a lot of emptiness around it looks important — even if it is small and grey. It is the subtlest lever and the one beginners underuse the most.

### 5. Position

What is at the top is read before what is at the bottom. What is on the left before what is on the right (in cultures that read left to right). The optical centre of a page sits slightly above the geometric centre.

### 6. Shape and style

An element that looks different from the rest (rounded among rectangles, filled among outlines, an icon among texts) draws attention through shape contrast alone.

!!! warning "Do not use all six on the same element"
    A button that is at once bigger, bold, coloured, isolated, at the top and rounded becomes shrill. **Two levers are usually enough.** Three is the reasonable maximum.

    A good example: the primary button = colour + size. All other buttons: outline only.

---

## The three levels rule

Any composition should have **exactly three levels** of importance:

| Level | Role | How much it takes | Examples |
|-------|------|-------------------|----------|
| **Primary** | What must be remembered, even if the reader leaves immediately | A single element | The event title, the main number |
| **Secondary** | What completes the message | 2–4 elements | Date, place, subheading |
| **Tertiary** | What is read only if someone is already interested | Everything else | Details, notes, contact, source |

!!! note "One single primary element"
    This is the hard part. If the title and the date are both 80 px, you do not have a primary level — you have two, and they cancel each other out.

    Ask yourself: **if the reader remembers one thing, what is it?** That gets the primary level. Everything else steps down.

---

## The reading path

### The entry point

The eye enters the page at the element with the highest contrast, wherever it sits. The path starts from there.

Consequence: **you can control where reading begins**, regardless of the order in which you placed things.

### The Z path

For pages with little content (posters, simple landing pages), the eye travels:

```
①─────────────────②
                 ╱
               ╱
             ╱
           ╱
③─────────────────④
```

Top-left corner, then top-right, the diagonal down to bottom-left, then bottom-right. You put the logo at ①, the title at ② and the action ("sign up") at ④.

### The F path

For pages with a lot of text (articles, content sites), the eye scans:

```
①━━━━━━━━━━━━━━━━━━
│
②━━━━━━━━━━━
│
③━━━━━
│
④
```

The top line fully, then less and less on each descent. The practical consequence: **the first 2–3 words of every heading matter most**. "How to configure the ESP32" is scannable; "A guide on how to configure the ESP32" is not.

!!! tip "Which path applies?"
    Count the content blocks. **Under 5** → Z. **Over 5** → F. Do not try to force a Z onto a page with 12 sections; it does not work.

---

## How to diagnose a broken hierarchy

Four tests, in order of speed.

### Test 1 — Blur

Apply a strong blur. The darkest / largest blob must be the primary element. If it is not, you have found the problem.

### Test 2 — Squinting

Squint until you only see shapes. The same principle, no tools.

### Test 3 — The 3 seconds

Show the design to a classmate for exactly 3 seconds. Ask what they remember. Repeat with 3 people; if the answers differ, the hierarchy is ambiguous.

### Test 4 — The reverse list

Write down what you notice, in the order you notice it. Compare with your priority list from the brief. The differences are exactly what needs fixing.

---

## Common mistakes and how to fix them

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Everything looks equally important" | Insufficient contrast between levels | Increase the jump: primary 2–3× the tertiary |
| "I don't know where to look first" | Two or more primary elements | Pick one; step the others down |
| "It's tiring" | Too many contrast levers at once | Keep 2 levers, drop the rest |
| "It looks empty / boring" | A single level, no accent | Add size or colour contrast on the primary element |
| "The image steals attention" | The photo has more contrast than the text | Dark overlay on the image, or text on a flat area |
| "The button isn't visible" | The button is the same colour as everything else | One coloured button, the rest outlined |

!!! warning "The trap: 'important' ≠ 'big'"
    Not everything important has to be big. A 300 px "Buy" button looks desperate. A 48 px button, the only coloured thing on the page, is impossible to miss and looks confident.

    Isolation and colour beat size almost every time.

---

## Hierarchy in an interface

On a poster, hierarchy is static. In an interface it has to answer an extra question: **what can the user do here?**

### The hierarchy of actions

| Type | Appearance | How many per screen |
|------|-----------|---------------------|
| **Primary** | Solid fill, brand colour | **Exactly one** |
| **Secondary** | Outline only, or neutral fill | 1–2 |
| **Tertiary** | Text only, like a link | Any number |
| **Destructive** | Red, usually outline only | Rare, never next to the primary |

!!! note "Why only one primary action"
    If a screen has two solid orange buttons, the user has to read both to decide. With one filled and one outlined button, the default decision is obvious and fast — and anyone who wants the other option still finds it.

### The hierarchy of information

- **The screen title** tells you where you are.
- **The content** is what you came to see — it gets the most space.
- **Navigation** is always reachable, but does not dominate.
- **Metadata** (dates, authors, tags) is tertiary: small, grey.

!!! tip "The 'why is this here' test"
    For every element on the screen, ask: **what happens if I remove it?** If the answer is "nothing", remove it. The best hierarchy improvement is often a deletion.

---

## Exercises

### Exercise 1 — Three levels out of a flat list
Take this content and build it in an 800 × 1000 px frame with three clear hierarchy levels:

```
Project fair
Saturday, 12 April
Sports hall, floor 1
10:00 – 14:00
Free entry
Organised by the computer science club
Details: ursoaia-edu.online
```

??? success "Solution"
    | Level | Text | Size | Weight | Colour |
    |-------|------|------|--------|--------|
    | Primary | `Project fair` | 72 | Bold | `#F8FAFC` |
    | Secondary | `Saturday, 12 April` | 32 | Semi Bold | `#F97316` |
    | Secondary | `10:00 – 14:00 · Sports hall, floor 1` | 24 | Regular | `#CBD5E1` |
    | Tertiary | `Free entry` | 16 | Medium | `#94A3B8` |
    | Tertiary | `Organised by the computer science club` | 16 | Regular | `#64748B` |
    | Tertiary | `ursoaia-edu.online` | 16 | Regular | `#64748B` |

    Notice three decisions:
    - The time and place have been **merged onto one line** — they are the same piece of information ("when and where"), so they do not need two levels.
    - The jump 72 → 32 → 16 is roughly 2× at each step. Visible, deliberate.
    - The date is the only coloured element in the secondary level — it is the second most important piece of information and colour lifts it without making it bigger than the title.

### Exercise 2 — Fix a screen with three primary buttons
Draw an app screen with three buttons, all with a solid orange fill: `Save`, `Cancel`, `Delete`. Then fix the action hierarchy.

??? success "Solution"
    | Button | Before | After | Why |
    |--------|--------|-------|-----|
    | `Save` | Orange fill | **Stays** orange fill | The main action |
    | `Cancel` | Orange fill | Text only, grey (`#94A3B8`) | An exit action, not worth weight |
    | `Delete` | Orange fill | Red outline, red text | Destructive: visible, but not inviting |

    On top of that: move `Delete` **away** from `Save`, usually to the opposite corner or into a menu. A destructive button glued to the main one produces misclicks.

    Result: the user instantly sees what is expected of them, and the dangerous action requires a conscious step.

### Exercise 3 — Diagnose an existing design
Take a poster or post you made in an earlier lesson and run all four diagnostic tests on it. Write down what you found and what you changed.

??? success "Solution"
    An example diagnostic report:

    > **Blur test:** the darkest blob is the photo, not the title. → Problem 1.
    > **Squinting:** the date and time melt into a single blob with the description. → Problem 2.
    > **3 seconds (3 people):** two remembered the title, one remembered the date. → Slight ambiguity, acceptable.
    > **Reverse list:** I noticed, in order: the image, the title, the date, the logo, the description. The brief asked for: title, date, place.

    **The fixes:**
    1. An `rgba(15, 23, 42, 0.65)` overlay on the photo → the title becomes the entry point.
    2. The space between the date/time block and the description increased from 12 to 40 px → they separate clearly.
    3. The place moved up next to the date, at the same size → the three mandatory pieces of information sit together.

    After the fixes, the 3-second test gives the same answer from all three people. That is the target.

---

## Mini-project: the same poster, inverted hierarchy

Take the typographic poster from lesson 04 and make a **second version** in which the hierarchy is deliberately shifted: the **date** becomes the primary element and the title steps down to secondary. Change nothing else — same palette, same font, same composition.

??? success "Solution"
    | Element | Version 1 | Version 2 |
    |---------|-----------|-----------|
    | Title | 96 Bold, white | 36 Semi Bold, `#CBD5E1` |
    | Date | 54 Semi Bold, orange | 120 Bold, white |
    | Everything else | unchanged | unchanged |

    **What you notice:**

    - Version 1 says "**come to Researchers' Night**". It works for someone who has never heard of the event.
    - Version 2 says "**on 27 September something happens**". It works for someone who already knows about the event and only needs to retain the date — for example a poster put up a week ahead, after an announcement campaign.

    Both are correct. **Whether a hierarchy is right depends on the brief**, not on abstract rules. That is why lesson 00 starts with the brief and not with the tools.

    **Extension:** make a third version where the primary element is the place (`LAB 2`). When would that be useful? Answer: when the event is well known and the only remaining question is "where is it held this year".

---

## Summary

- **Visual hierarchy** is the order in which the reader notices things — and it exists either way.
- Six levers: **size, weight, colour, space, position, shape**. Use 2, at most 3.
- The size jump must be at least **1.5×** to look intentional.
- **Three levels**: a single primary element, 2–4 secondary, everything else tertiary.
- Reading path: **Z** under 5 blocks, **F** over 5.
- In an interface: **exactly one primary button** per screen.
- Diagnosis: **blur, squint, 3 seconds, reverse list**.
- The best hierarchy improvement is often a **deletion**.
- What is "correct" depends on the **brief**, not on abstract rules.

---

**Next step:** [→ Lesson 07: Vectors and the Pen Tool](07-vectori-pen-tool.md)
