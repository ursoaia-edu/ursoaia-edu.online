---
lesson: 16
tags: [capstone, prototype, figma, interaction, smart animate, testing]
summary: Capstone project — an interactive landing page in Figma, with linked screens, states, transitions and a real user testing session.
---

# Lesson 16 · Project: an interactive landing page prototype

!!! tip "What you will build"
    A **landing page that works as a prototype**, which anyone can open on a phone and walk through:

    - Phone and desktop screens, built from your library
    - Real navigation: menu clicks, scrolling, opening sections
    - Interactive states: hover, focus, pressed
    - A form with simulated validation and a confirmation screen
    - Transitions with **Smart Animate**
    - A **testing session** with three people and the resulting fix list

---

## What a prototype is and what it is for

A prototype **is not a website**. It has no code, saves no data, does not work offline. It is a simulation — convincing enough that someone can use it and tell you where they get stuck.

Why it is worth the effort:

| Benefit | Explanation |
|---------|-------------|
| **You test before building** | A flow problem found in the prototype costs 10 minutes; found in code, it costs a day |
| **You explain without words** | A prototype link replaces a 20-minute conversation |
| **You see the real rhythm** | A static design does not tell you whether a flow has too many steps |
| **You get concrete feedback** | People comment differently when they can press, not just look |

---

## Preparation

### What you should already have

- The component library from lesson 08, with **every state** drawn (lesson 14).
- The visual identity from lesson 15.
- The flow written in words.

### The flow for this project

> 1. The visitor opens the landing page → sees the welcome section
> 2. Scrolls → sees what the club does, the projects, the schedule
> 3. Presses "Join" (from the menu or the page) → reaches the form
> 4. Fills in the fields → presses "Submit"
> 5. Sees the confirmation screen
> 6. (alternatively) Submits with an empty field → sees the error state

Six steps, and step 6 is the one most people forget.

### The screens needed

| # | Screen | Why |
|---|--------|-----|
| 1 | Full landing (scrolling) | The main page |
| 2 | Landing with the mobile menu open | The navigation state |
| 3 | Empty form | The entry point |
| 4 | Form with an error | Validation |
| 5 | Filled form | Before submitting |
| 6 | Confirmation | The end of the flow |

Six phone frames. For desktop, screens 2 and 3 merge (the menu is always visible, the form is a page section), so four frames.

---

## Building the screens

### The landing page sections

| Section | Content | Typical height (mobile) |
|---------|---------|-------------------------|
| **Navigation** | Logo + hamburger | 64 px, pinned to the top |
| **Hero** | Title, one sentence, main button | 480 px |
| **What we do** | 3 cards with icon + text | 640 px |
| **Projects** | 3 cards with images | 900 px |
| **Schedule** | Day, time, room | 280 px |
| **Join** | A large button to the form | 240 px |
| **Footer** | Logo, links, contact | 320 px |

The total exceeds the screen height (844 px) — as it should; the page scrolls.

!!! tip "How to make a Figma prototype scroll"
    1. The screen frame stays at **390 × 844** (the phone's size).
    2. The content inside is taller — 3200 px, for example.
    3. Select the frame → right panel → tick **Clip content**.
    4. Select the inner content → in the **Prototype** tab, set **Overflow behavior: Vertical scrolling**.

    Now, in presentation mode, the page scrolls like a real one.

### Elements fixed while scrolling

The navigation must stay at the top while you scroll.

1. Select the navigation frame.
2. In the **Prototype** tab, tick **Fix position when scrolling**.

The same applies to a floating button, if you have one.

---

## Linking the screens

### The basic connections

1. Switch to the **Prototype** tab (top right).
2. Select the element being pressed (the button, not the text inside it).
3. Drag the blue circle on its edge onto the destination frame.
4. In the panel that appears, set the trigger and the animation.

### The triggers

| Trigger | When it fires | Use |
|---------|---------------|-----|
| **On click / tap** | On press | Buttons, links |
| **While hovering** | While the mouse is over it | Hover states on desktop |
| **While pressing** | While held down | The active state |
| **Key / gamepad** | On a key | Keyboard navigation |
| **After delay** | After a period | Loading screens, automatic transitions |

### The animations

| Animation | Effect | When |
|-----------|--------|------|
| **Instant** | No transition | Quick state changes |
| **Dissolve** | Fade | Modals, confirmations |
| **Move in / out** | Comes in over the current screen | Side menus, panels |
| **Push** | Pushes the current screen aside | Navigation between pages |
| **Slide in / out** | Slides over | Bottom sheets |
| **Smart animate** | Automatically interpolates elements with the **same name** | Fluid transitions |

!!! warning "Duration matters more than type"
    | Duration | Feeling |
    |----------|---------|
    | < 100 ms | Feels instant |
    | **150–300 ms** | The right range for most transitions |
    | 400–600 ms | Feels slow |
    | > 700 ms | Annoying; the user presses again thinking it did not register |

    By default Figma sets 300 ms. For small changes (hover, press), drop to **150 ms**.

---

## Smart Animate

It is the only animation that needs explaining.

**How it works:** Figma compares the elements in the two frames and automatically interpolates anything that has **exactly the same layer name**. Position, size, colour, opacity, rotation.

### The mandatory condition

The layers must have **identical names** in both frames. If in the first frame the button is called `cta-button` and in the second `Rectangle 43`, Smart Animate will not link them — it will fade instead.

!!! tip "The right workflow"
    Do not build the second screen from scratch. **Duplicate the first** (++ctrl+d++), then change what needs changing. That way the layer names stay identical automatically.

### What you can do with it

| Effect | How |
|--------|-----|
| A card that expands | The same card, a different size in the second frame |
| A menu that slides | The same panel, a different X position |
| A button that changes colour | The same button, a different Fill |
| An element that moves between sections | The same name, a different position |

!!! note "Easing curves"
    Next to the duration, Figma has an easing menu:

    - **Ease out** — fast at the start, slowing at the end. The most natural for elements that **appear**.
    - **Ease in** — the reverse. For elements that **disappear**.
    - **Ease in and out** — for movement between two positions.
    - **Linear** — constant speed. It looks mechanical; avoid it except for progress indicators.

---

## Interactions inside components

A button with variants (lesson 08) can carry its interactions **inside the component**, rather than on each instance.

1. Enter the variant set.
2. Select the `State: default` variant.
3. In the Prototype tab, drag a connection to the `State: hover` variant.
4. Trigger: **While hovering**. Animation: Instant or Dissolve 100 ms.
5. Add the reverse connection (hover back to default is created automatically).

The result: **every instance of the button** across the whole prototype reacts to hover. You never have to wire anything by hand.

!!! tip "Do the same for form fields"
    The `default` → `focus` variant on the **On click** trigger. Your prototype will then correctly simulate filling in a form.

---

## Testing with users

This is the part everyone skips, and the one that gives the most back.

### Preparing

1. **Share → can view → Copy link**, then append `&scaling=scale-down` to the link so it fits the person's screen.
2. Prepare **one single task**, phrased as a goal, not as an instruction.

| Good phrasing | Bad phrasing |
|---------------|--------------|
| "You want to join the club. Show me how you would do it." | "Press the Join button in the menu." |
| "Find out when the meetings are." | "Scroll to the Schedule section." |

### During the test

| Rule | Why |
|------|-----|
| **Do not help** | The moment the person gets stuck is exactly the information you need |
| **Do not explain the design** | Real users will not have a designer sitting next to them |
| **Ask them to think out loud** | "Tell me what you are looking at and what you are looking for" |
| **Take notes, do not discuss** | The discussion comes afterwards |
| **Time them** | How many seconds until they find the join button? |

!!! warning "Three people are enough"
    You do not need a statistical sample. Usability research shows that **3–5 people** uncover most major problems. If all three get stuck in the same place, you have found a real problem, not a preference.

### What you note

| Column | Example |
|--------|---------|
| What they did | "Scrolled up and down three times before finding the button" |
| Where they got stuck | "Did not see the Join link in the menu" |
| What they said | "I thought I had to send an email" |
| How long it took | "38 seconds to reach the form" |

### From observations to fixes

| Observation | Diagnosis | Fix |
|-------------|-----------|-----|
| All three missed the hero button | Insufficient contrast or position | Move it higher, make it the only coloured element |
| Two tried to press the cards | The cards look interactive | Either make them interactive or remove the hover effect |
| One filled the class field wrongly | The label is ambiguous | Change "Class" to "Class (e.g. 9B)" |
| All hesitated at the "Submit" button | It is unclear what happens next | Add below the button: "You will get a confirmation by email" |

---

## Exercises

### Exercise 1 — A mobile menu with Smart Animate
Build two frames — the landing with the menu closed and with the menu open — and link them with Smart Animate so the panel slides down from the top.

??? success "Solution"
    1. Build the `landing-mobile` frame.
    2. ++ctrl+d++ → rename the copy `landing-mobile-menu`.
    3. In the copy, add a `menu-panel` frame of 390 × 480, positioned at Y = 64 (below the navigation), with the 4 links.
    4. In the **original frame**, add the **same** `menu-panel`, with an identical name, but positioned at **Y = −480** (off-screen, above) and with 0 opacity.
    5. Link the hamburger in screen 1 → screen 2. Animation: **Smart animate**, **Ease out**, **250 ms**.
    6. Link the X button in screen 2 → screen 1, with the same settings.

    **Why it works:** `menu-panel` has the same name in both frames, so Smart Animate interpolates the Y position from −480 to 64 and the opacity from 0 to 1. The result is a fluid slide.

    **If it does not work:** check the names. In 9 cases out of 10, one of the frames has `Frame 27` instead of `menu-panel`.

### Exercise 2 — A form with simulated validation
Build the complete form flow: empty → field focused → filled → error → confirmation.

??? success "Solution"
    **The frames needed:**

    | Frame | State |
    |-------|-------|
    | `form-empty` | All fields empty, the button active |
    | `form-focus` | The first field in the focus state |
    | `form-filled` | All fields filled in |
    | `form-error` | The email field empty + red border + message |
    | `form-success` | A confirmation screen with an icon and text |

    **The connections:**

    | From | Element | Trigger | To | Animation |
    |------|---------|---------|----|-----------|
    | `form-empty` | name field | On click | `form-focus` | Instant |
    | `form-focus` | name field | On click | `form-filled` | Instant |
    | `form-filled` | Submit button | On click | `form-success` | Dissolve 200 ms |
    | `form-empty` | Submit button | On click | `form-error` | Instant |
    | `form-error` | email field | On click | `form-filled` | Instant |
    | `form-success` | Close button | On click | `landing-mobile` | Push 250 ms |

    **The important observation:** the connection from `form-empty` straight to `form-error` simulates a user pressing Submit without filling anything in. That is the case most prototypes omit — and exactly the one that occurs most often in reality.

### Exercise 3 — A testing session
Test the prototype with three people who have not seen the project. Record the observations in the table above and produce a prioritised fix list.

??? success "Solution"
    **An example report:**

    | Person | Task | Time | Where they got stuck |
    |--------|------|------|----------------------|
    | A | Join | 42 s | Looked for the button in the footer |
    | B | Join | 28 s | Missed the hero button, found it in the menu |
    | C | Join | 51 s | Scrolled the whole page twice |

    **The diagnosis:** all three struggled with the same thing — the main join button in the hero is not visible. An average of 40 seconds for the page's primary action is very poor; the target is under 10 seconds.

    **The prioritised fix list:**

    | # | Fix | Impact | Effort |
    |---|-----|--------|--------|
    | 1 | Make the hero button the only coloured element on the first screen | High | Low |
    | 2 | Move the button 80 px higher so it is visible without scrolling | High | Low |
    | 3 | Add a fixed bottom button, visible while scrolling | Medium | Medium |
    | 4 | Change the label from "Join" to "Come Thursday at 15:00" | Medium | Low |
    | 5 | Remove the hover effect from the cards (it misleads) | Low | Low |

    **After the fixes, retest with three different people.** If the average time drops below 15 seconds, the fixes worked.

    !!! note "Why you retest with different people"
        Anyone who has already seen the prototype knows where the button is. A second attempt by the same person tells you nothing about the design, it tells you about their memory.

---

## Mini-project: a complete landing page, tested and fixed

Build the full prototype for your club, test it with three people and deliver the corrected version together with the testing report.

??? success "Deliverables and criteria"
    **The deliverables:**

    | Deliverable | Content |
    |-------------|---------|
    | The mobile prototype link | 6 linked screens, working scroll |
    | The desktop prototype link | 4 linked screens |
    | The testing report | The 3-person table + the prioritised fix list |
    | Version v2 | The prototype after the fixes |
    | The Figma file | With separate pages: `v1`, `Testing notes`, `v2` |

    **The evaluation criteria:**

    | # | Criterion | Check |
    |---|-----------|-------|
    | 1 | Scrolling works | Open it on a phone and scroll |
    | 2 | The navigation stays fixed while scrolling | Same |
    | 3 | Every button leads somewhere | Press each one; none is "dead" |
    | 4 | Hover and focus states live in the components | Check any instance |
    | 5 | The error flow exists | Submit the empty form |
    | 6 | You can go back from any screen | There is a back or close button |
    | 7 | Transitions are 150–300 ms | Check every connection |
    | 8 | Smart Animate works | The menu slides, it does not fade |
    | 9 | A testing report with 3 people | The full table |
    | 10 | v2 resolves at least the first 3 fixes | Compare v1 with v2 |

    **The "dead button" test:** walk the prototype as an ordinary user and press **every** element that looks interactive. Any button that goes nowhere is a problem — either wire it up or make it stop looking pressable.

    **The real phone test:** open the link on your actual phone, not in a browser on a laptop. Touch targets, text size and scroll smoothness feel completely different.

---

## You have finished the course

You have walked the whole road: from what a design decision is (lesson 00), through the visual language and Figma's tools, to a complete visual identity and a prototype tested with real users.

**What you now have:**

- A vocabulary: hierarchy, contrast, grid, component, state, breakpoint.
- A process: brief → content → structure → appearance → checks → testing.
- A portfolio: poster, logo, visual identity, prototype.
- Checking habits: blur, contrast, black and white, 3 seconds, user testing.

**Where to go next:**

| Direction | The first step |
|-----------|----------------|
| **Build what you designed** | [The web development course](../web/index.md) — HTML, CSS, JavaScript |
| **Design for physical projects** | [The electronics projects](../../projects/index.md) — interfaces for ESP32, labels, panels |
| **Go deeper into typography** | Design 10 posters using **one single font** |
| **Go deeper into UI** | Rebuild the interface of an app you use every day |

!!! tip "One last piece of advice"
    Design is not learned by reading, but by making and receiving feedback. The most useful thing you can do from here on: **publish**. Put the posters up in the corridor, post on the club's page, give the prototype to your classmates.

    One design seen by 100 people teaches you more than ten designs nobody sees.

---

## Summary

- A **prototype** is a simulation, not a website — but it is enough to test the flow.
- Scrolling: a frame at screen size + `Clip content` + `Vertical scrolling` on the content.
- `Fix position when scrolling` for navigation and floating buttons.
- Triggers: **on click, while hovering, while pressing, after delay**.
- The right transition duration: **150–300 ms**. Above 700 ms it becomes annoying.
- **Smart Animate** requires **identical layer names** in both frames — duplicate, do not rebuild.
- Put the interactions **inside the components**, not on each instance.
- **Three people** uncover most usability problems.
- Phrase tasks as **goals**, not instructions; do not help during the test.
- Retest **with different people**, not the same ones.

---

**Back to:** [the course map](index.md)
