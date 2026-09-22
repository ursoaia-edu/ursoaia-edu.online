---
lesson: 8
tags: [figma, components, styles, variants, design system]
summary: Colour and text styles, components and instances, properties and variants — how you build a reusable library.
---

# Lesson 08 · Styles and components

!!! tip "What you will learn"
    - What **styles** are and why you never pick a colour "by hand" again
    - The difference between a **component** and an **instance**
    - What can be overridden in an instance and what cannot
    - **Properties** and **variants** — one button in 12 states
    - **Slots** (instance swap) for flexible components
    - How to organise a library you can still use six months from now

---

## The problem it solves

You have a poster with 20 orange elements. Your teacher says: "change the orange to green".

- **Without styles:** you select each element, change the colour, hunt for the ones you missed, find two more the next day. 15 minutes and one mistake.
- **With styles:** you change the `brand/primary` style. All 20 update. 3 seconds, zero mistakes.

The difference grows exponentially with project size. In an app design with 40 screens, working without styles is simply impossible.

---

## Styles

A **style** is a value saved under a name, which you apply in many places. Figma has four types:

| Type | What it saves |
|------|---------------|
| **Color** | A colour or a gradient |
| **Text** | Font + weight + size + line height + tracking |
| **Effect** | Shadows, blur |
| **Grid** | The layout grid configuration |

### How to create a style

1. Select an element that already has the value you want.
2. In the right panel, in the relevant section (Fill / Text / Effects / Layout grid), click **the four dots**.
3. Press **+** and give it a name.

### How to name styles

We settled the rule in lesson 03: **by role, not by appearance**. Now add a folder structure through `/`:

```
brand/
  primary
  primary-hover
  secondary
surface/
  base
  raised
  overlay
text/
  strong
  base
  muted
  inverse
feedback/
  success
  warning
  error
```

```
heading/
  h1
  h2
  h3
body/
  large
  base
  small
label/
  caps
  mono
```

!!! tip "Three levels maximum"
    `brand/primary` is good. `design/colors/brand/main/primary-500` is a structure you will hate within two weeks. Two levels are enough for a course project.

!!! warning "An unapplied style helps nobody"
    The classic mistake: you create 12 beautifully named styles, then keep drawing by picking colours from the picker. The check: select any element in your design — in the right panel, **Fill** must show a style name, not a HEX code.

---

## Components

A **style** saves a value. A **component** saves a whole structure: shapes, text, spacing, all together.

### Component vs. instance

- **The main component** — the original. It has a purple diamond ◆ in the Layers panel.
- **The instance** — a copy linked to the original. It has a hollow diamond ◇.

**Changes in the main component propagate to every instance.** Changes in an instance stay local.

### How to create a component

1. Select the elements (usually a frame with everything inside).
2. ++ctrl+alt+k++ (Windows) / ++cmd+option+k++ (Mac), or the ◆ button in the top bar.
3. Give it a descriptive name with a folder structure: `button/primary`, `card/project`, `icon/wifi`.

Then you place it with ++ctrl+d++ or from the **Assets** panel (left), where all the file's components appear.

### What can be overridden in an instance

| You can | You cannot |
|---------|-----------|
| The text | Add new layers |
| The colours (Fill, Stroke) | Delete a layer (only hide it) |
| The images | Change structural spacing |
| Layer visibility | Reorder layers |
| Nested instances (swap) | — |

!!! note "Resetting an instance"
    If you have overridden too much in an instance, right-click → **Reset all changes**. It returns to the main component's state.

!!! warning "Where you keep the main components"
    Do not leave them scattered across the file. Create a **separate page** called `Components` (left panel, Pages tab) and keep them all there, organised into sections. If you accidentally delete a main component, all its instances become "detached" and stop updating.

---

## Properties

A **component property** turns a manual override into a field you fill in from the right panel. Four types:

| Type | What it controls | Example |
|------|------------------|---------|
| **Text** | The content of a text layer | The button label |
| **Boolean** | The visibility of a layer | Show / hide the icon |
| **Instance swap** | Which component sits in a slot | Which specific icon |
| **Variant** | Which variant is active | Size, state, type |

### How to add a property

1. Enter the main component.
2. Select the layer you want to make configurable.
3. In the right panel, next to that property, click the small diamond icon.
4. **Create property** → name + default value.

Now every instance shows a field with that name in the right panel. You never have to dig into layers to change the text again.

---

## Variants

A **variant** groups several versions of the same component into one, with a selector.

### Example: a button

Properties:

| Property | Values | How many |
|----------|--------|----------|
| `Type` | primary, secondary, ghost | 3 |
| `Size` | small, medium, large | 3 |
| `State` | default, hover, disabled | 3 |

3 × 3 × 3 = **27 variants** from a single component. The right panel of any instance shows three dropdowns.

### How to build a variant set

1. Create the first component (`button`, type primary, size medium, state default).
2. Select it and press **Create component set** (the four-squares button in the top bar).
3. A dashed purple frame appears. Inside it, press **+** for each new variant.
4. In the right panel, under **Properties**, rename the properties (`Property 1` → `Type`) and the values.

!!! tip "Do not build 27 variants at once"
    Start with 2 properties and 4–6 variants. Add the third property only when you actually need it. A variant set that grows too large becomes hard to maintain: any spacing change has to be made in 27 places.

    The better alternative: use **Auto Layout** (lesson 09) so the size adapts by itself, and keep only the `Type` and `State` properties.

---

## Instance swap — slots

The most useful property, and the one beginners know least.

**The problem:** you have a project card containing an icon. You have 8 different icons. Do you make 8 card components?

**The solution:** you make **one** card component in which the icon is itself an instance. Then you add an **Instance swap** property to it. In each card instance, you pick the icon you want from a menu.

```
card/project  (component)
├── frame
│   ├── ◇ icon/wifi        ← slot: Instance swap
│   ├── text: Title        ← Text property
│   └── text: Description  ← Text property
```

!!! note "The slot rule"
    Any element that changes from one instance to another **but stays the same kind of thing** should be a slot. Icons, avatars, badges, the button inside a card.

---

## Organising the library

A file with 60 components and no structure is worse than none. The minimum structure:

```
Page: Foundations
  ├── The colour palette (all styles, visually)
  ├── The type scale
  └── The spacing system

Page: Components
  ├── Section: Primitives     → button, input, badge, avatar
  ├── Section: Icons          → the 24 × 24 set
  └── Section: Composites     → card, header, nav, footer

Page: Screens / Designs
  └── The actual work
```

### The naming convention

| Pattern | Example | Why |
|---------|---------|-----|
| `category/name` | `button/primary` | Automatic grouping in Assets |
| `icon/name` | `icon/wifi` | All icons together |
| `card/type` | `card/project` | Easy to find when swapping |

!!! tip "The six-months test"
    Open the file six months from now and try to find the secondary button component in under 10 seconds. If you cannot, the organisation is too complicated or the names are too vague.

---

## When NOT to use components

Components have a cost: build time and complexity. They are not worth it for:

- An element used **once**. A poster headline is not a component.
- A one-off poster that will never have variants.
- Decorative shapes that change every time.

!!! note "The rule of three"
    If an element appears **three times or more**, or you know it will repeat, make it a component. Below three, it is not worth it.

---

## Exercises

### Exercise 1 — A complete style system
In a new file, create the full set of colour and text styles from lessons 03 and 04. Then build a project card that uses **only** styles — no hand-typed HEX.

??? success "Solution"
    **Colour styles (9):**
    `brand/primary`, `brand/primary-hover`, `surface/base`, `surface/raised`, `text/strong`, `text/base`, `text/muted`, `feedback/success`, `feedback/error`.

    **Text styles (6):**
    `heading/h1` (31/1.2 Semi Bold), `heading/h2` (25/1.3 Semi Bold), `body/base` (16/1.6 Regular), `body/small` (13/1.4 Regular), `label/caps` (13/1.4 Medium, all caps, +10% tracking), `label/mono` (13/1.4 Regular, JetBrains Mono).

    **The card:** a 360 × 280 frame, `surface/raised`, 16 radius, 32 padding.
    - Label: `label/caps` + `brand/primary`
    - Title: `heading/h2` + `text/strong`
    - Description: `body/base` + `text/muted`
    - Button: `brand/primary` fill, `body/small` + `text/inverse` text

    **The check:** select each element in turn. In the right panel, Fill and Text must show a **style name**, not a code. If a code appears, you missed one.

### Exercise 2 — A button with variants
Build a variant set for a button with the properties `Type` (primary, secondary, ghost) and `State` (default, hover, disabled). Nine variants.

??? success "Solution"
    | Type | State | Fill | Text | Border |
    |------|-------|------|------|--------|
    | primary | default | `brand/primary` | `text/inverse` | — |
    | primary | hover | `brand/primary-hover` | `text/inverse` | — |
    | primary | disabled | `surface/raised` | `text/muted` | — |
    | secondary | default | transparent | `text/strong` | 1 px `text/muted` |
    | secondary | hover | `surface/raised` | `text/strong` | 1 px `text/base` |
    | secondary | disabled | transparent | `text/muted` | 1 px `surface/raised` |
    | ghost | default | transparent | `brand/primary` | — |
    | ghost | hover | `surface/raised` | `brand/primary` | — |
    | ghost | disabled | transparent | `text/muted` | — |

    **Also add a Text property** on the button label, with the default value `Button`. Now every instance is configured entirely from the right panel: you pick the type, the state and type the text.

    **Check:** place 3 instances and change their type from the menu. If the button keeps a correct size across labels of different lengths, you used Auto Layout — good. If the text overflows the button, come back after lesson 09.

### Exercise 3 — A card with an icon slot
Build a `card/feature` component with: an icon (slot), a title (Text property) and a description (Text property). Place 4 instances with different icons from the set you made in lesson 07.

??? success "Solution"
    **Building the component:**
    1. A 280 × 200 frame, `surface/raised`, 16 radius, 24 padding.
    2. Inside it, place an instance of the `icon/wifi` component — it **must** be an instance, not a redrawn copy.
    3. Below it, a `heading/h3` text and a `body/small` text.
    4. Select everything → ++ctrl+alt+k++ → name it `card/feature`.

    **The properties:**
    - Select the icon → the right panel shows `Instance` → click the small diamond → **Create property** → type `Instance swap`, name `Icon`.
    - Select the title → the diamond next to the content → **Create property** → type `Text`, name `Title`.
    - Same for the description → `Description`.

    **Using it:** place 4 instances. The right panel of each shows three fields: a menu with all your icons and two text boxes. You never dig into layers again.

    **The real test:** now change the main component's padding from 24 to 32. All 4 instances update. That is the whole point of the exercise.

---

## Mini-project: a base library for the computer science club

Build a `Design System` file with three pages (`Foundations`, `Components`, `Playground`) containing: the full style set, the 8-icon set from lesson 07, and four components — `button` (with variants), `badge`, `card/project` and `input`.

??? success "Solution"
    **The Foundations page** — visual documentation, not just invisible styles:
    - A row of 80 × 80 px squares, one per colour style, with the style name and HEX code underneath.
    - A column with the 6 text styles, each applied to the text "Ursoaia computer science club", with the spec (size / line height / weight) alongside.
    - A visual spacing scale: 8 rectangles of height 4, 8, 16, 24, 32, 48, 64, 96 px, labelled.

    **The Components page:**

    | Component | Properties | Variants |
    |-----------|------------|----------|
    | `button` | Type, State, Label (Text) | 9 |
    | `badge` | Type (info/success/warning/error), Label | 4 |
    | `card/project` | Icon (swap), Title, Description, Tag | 1 |
    | `input` | State (default/focus/error), Placeholder, Label | 3 |

    Plus an `Icons` section with the 8 icons as instances.

    **The Playground page:** build a simple screen using **only** instances and styles from the library — a header with logo and navigation, three project cards, a sign-up form with two fields and a button.

    **The success criterion:** change `brand/primary` from orange to blue, in one single place. If the entire Playground screen updates coherently — buttons, badges, focus states and icons included — the library is built correctly.

    **If something did not change:** that element uses a hand-typed colour. Find it and replace it with the style.

---

## Summary

- **Styles** save values (colour, text, effect, grid); you name them **by role**, with `/` for folders.
- A correctly built element shows a **style name** in the right panel, not a HEX code.
- The **component** ◆ is the original, the **instance** ◇ is the linked copy. Changes flow top-down.
- In an instance you can change text, colours, images and visibility — **not** the structure.
- **Properties** (Text, Boolean, Instance swap, Variant) turn overrides into fields.
- **Variants** group versions; do not build 27 at once.
- **Instance swap** = slot; any element that varies but stays the same kind of thing is a slot.
- Keep main components on a **separate page**.
- **The rule of three:** below three uses, a component is not worth it.

---

**Next step:** [→ Lesson 09: Auto Layout](09-auto-layout.md)
