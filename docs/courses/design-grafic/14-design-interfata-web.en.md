---
lesson: 14
tags: [ui, ux, wireframe, mockup, responsive, handoff]
summary: From wireframe to mockup, interface components, responsive design and what you hand over to HTML and CSS.
---

# Lesson 14 · Web interface design

!!! tip "What you will learn"
    - The difference between **UX** and **UI**, without jargon
    - **Wireframe** → **mockup** → **prototype**: what happens at each stage
    - The standard interface components and their **states**
    - **Responsive design**: mobile-first, breakpoints, what changes
    - Accessibility in interfaces: contrast, touch target, focus
    - **Handoff**: what the developer receives from you

---

## UX and UI

| | UX (User Experience) | UI (User Interface) |
|---|----------------------|---------------------|
| **The question** | What must the user be able to do, and in what order? | How does each element look and behave? |
| **Deliverables** | Flows, screen maps, wireframes | Mockups, components, styles, prototype |
| **It goes wrong when** | The flow has 7 steps instead of 3 | The button is beautiful but invisible |

Both matter. A perfect UI on a bad UX gives you a beautiful app nobody uses.

!!! note "The starting rule"
    Before you draw a single screen, write the **flow** in words:

    > A student wants to join the club.
    > 1. Lands on the site → sees the home page
    > 2. Presses "Join" → sees the form
    > 3. Fills in name, class, email → presses "Submit"
    > 4. Sees the confirmation

    Four steps, four screens. Now you know exactly what to draw.

---

## Wireframe, mockup, prototype

### Wireframe — the structure

Grey, no colours, no photos, no final fonts. Just rectangles and placeholder text.

**The purpose:** decide **what** is on screen and **where**, without being distracted by looks.

| Convention | What it means |
|------------|---------------|
| Rectangle with a diagonal X | An image |
| Grey horizontal lines | A block of text |
| Rounded rectangle + centred text | A button |
| Outlined rectangle + grey text | A form field |

!!! tip "A wireframe takes 15 minutes, not 2 hours"
    If you spend a long time on a wireframe, you are making it too detailed. Its purpose is to be **thrown away** — if the structure does not work, you redo the wireframe in 10 minutes, not the mockup in 3 hours.

### Mockup — the appearance

The wireframe + colours, typography, images, real spacing. It looks like the final product but does nothing.

### Prototype — the behaviour

The mockups linked together, with transitions. It can be clicked and navigated. We build it in lesson 16.

---

## The grid and breakpoints

### Mobile-first

You design **for the phone first**, then expand. The reasons:

1. Over 60% of web traffic comes from phones.
2. The phone is the harshest constraint — if it fits there, it fits anywhere.
3. Expanding is easier than compressing. A desktop design squeezed onto a phone almost always ends up cluttered.

### Standard breakpoints

| Device | Frame width | Columns | Margin | Gutter |
|--------|-------------|---------|--------|--------|
| **Phone** | 390 px | 4 | 16 | 16 |
| **Tablet** | 768 px | 8 | 32 | 24 |
| **Desktop** | 1440 px | 12 | 96 | 24 |

!!! note "What changes at each breakpoint"
    | Element | Phone | Desktop |
    |---------|-------|---------|
    | Navigation | Hamburger menu | Visible horizontal links |
    | Content columns | 1 | 2–3 |
    | Cards | Stacked | A grid of 3 |
    | Body text | 16 px | 16–18 px |
    | Main heading | 32 px | 48–64 px |
    | Margins | 16 px | 96 px |

---

## Interface components and their states

An interface element **is not an image**. It has states, and each one must be drawn.

### The mandatory states

| State | When it appears | What typically changes |
|-------|-----------------|------------------------|
| **Default** | Normal | — |
| **Hover** | Mouse over it (desktop only) | A darker / lighter fill |
| **Focus** | Selected with ++tab++ | **A visible outline** of 2–3 px |
| **Active / pressed** | While being pressed | Slightly darker, sometimes slightly smaller |
| **Disabled** | Unavailable | Reduced opacity, no pointer cursor |
| **Loading** | Waiting for a response | An indicator, a changed label |

!!! warning "The focus state is not optional"
    Many people navigate with the keyboard — out of habit, for speed, or because they cannot use a mouse. If you remove the focus outline ("it looks ugly"), those people can no longer use the site at all.

    The focus outline is **drawn deliberately**, in the brand colour, 2–3 px thick with a 2 px offset. It is not removed.

### The basic components

| Component | What must be drawn |
|-----------|--------------------|
| **Button** | 3 types (primary, secondary, ghost) × 5 states |
| **Text field** | default, focus, filled, error, disabled + label + error message |
| **Card** | With and without an image, with and without an action |
| **Navigation** | Desktop and mobile, with the "current page" state |
| **System message** | Success, warning, error, info |

### The touch target

On a phone, any element that gets pressed must have at least **44 × 44 px** of active area — no matter how small the icon inside it is.

```
    ┌──────────────┐
    │   ┌──────┐   │   ← active area: 44 × 44
    │   │ icon │   │   ← the icon: 24 × 24
    │   │24×24 │   │
    │   └──────┘   │
    └──────────────┘
```

!!! warning "The classic mistake"
    A "close" button drawn as a 16 px X with no padding. On a phone it is almost impossible to hit. Add padding up to 44 × 44, even if the extra area is transparent.

---

## Accessibility in interfaces

On top of the contrast from lesson 03:

| Requirement | The rule |
|-------------|----------|
| Text contrast | 4.5:1 normal, 3:1 for text ≥ 24 px |
| Interactive element contrast | **3:1** for field outlines and functional icons |
| Touch target | At least 44 × 44 px |
| Visible focus | An outline of at least 2 px, 3:1 contrast against the background |
| Form labels | **Above** the field, never placeholder only |
| Errors | Explicit text, not just a red outline |
| Body text | At least 16 px on mobile (below 16 px, iOS zooms automatically) |

!!! note "Why a placeholder is not a label"
    If the only "Name" hint is the placeholder inside the field, it **disappears** the moment the user starts typing. Anyone who is interrupted and comes back no longer knows what they were filling in. The label sits above and stays.

---

## Handoff — what you give the developer

A badly handed-over design costs more time than doing it properly would have taken.

### What the developer receives

| Deliverable | Content |
|-------------|---------|
| **The Figma link** with view rights | Not screenshots |
| **The Foundations page** | Colours with style names, the type scale, the spacing system |
| **The components** with every state | Not just the default state |
| **The screens** at all 3 breakpoints | Phone, tablet, desktop |
| **Exported assets** | SVGs for icons and the logo, images at 2× |
| **Notes** | What happens on click, which texts are dynamic, what happens when the list is empty |

### Dev Mode

Figma has a dedicated mode (the toggle at the top right). A developer with access sees:

- Dimensions, spacing and colours as CSS, directly copyable
- Style and component names
- Distances between elements, measured automatically
- Assets to download

!!! tip "Auto Layout does half the handoff"
    A design built with Auto Layout (lesson 09) shows the developer `display: flex; gap: 16px; padding: 24px` directly. A design with manually positioned elements forces them to measure and guess.

### The cases everyone forgets

Draw them, even if they look boring:

| Case | The question |
|------|--------------|
| **Empty state** | What is shown when there are no projects yet? |
| **Long text** | What happens with a 15-word title? Does it wrap or truncate with `…`? |
| **Missing image** | What appears in its place? |
| **Network error** | What does the user see? |
| **Loading** | A skeleton, a spinner, or nothing? |

---

## Exercises

### Exercise 1 — Flow and wireframe
Write the flow in words for "a visitor wants to see the details of a club project", then draw the wireframes of the screens, at 390 px wide.

??? success "Solution"
    **The flow:**
    > 1. Lands on the home page → sees a list of projects
    > 2. Presses a project → sees the project page
    > 3. Scrolls → sees the description, the schematic, the code
    > 4. (optional) Presses "View on GitHub" → leaves the site

    Three screens to draw (the fourth is external).

    **Wireframe screen 1 — the list:**
    ```
    ┌────────────────────┐
    │ ☰   Logo        🔍 │  ← header, 56 px
    ├────────────────────┤
    │ Projects           │  ← page title
    │                    │
    │ ┌────────────────┐ │
    │ │ ╲╱  Title      │ │  ← card: image + title + tag
    │ │ ╱╲  ▬▬▬▬ ▬▬    │ │
    │ └────────────────┘ │
    │ ┌────────────────┐ │
    │ │ ╲╱  Title      │ │
    │ │ ╱╲  ▬▬▬▬ ▬▬    │ │
    │ └────────────────┘ │
    └────────────────────┘
    ```

    **Screen 2 — the project:** a header with a "back" button, a large image, the title, tags, the description, a code section, a "View on GitHub" button.

    **Screen 3 = screen 2 scrolled.** No separate wireframe needed — just note "scroll".

    **The check:** can someone walk the flow looking only at the wireframes, with no explanation from you? If they ask "and where do I go from here?", a screen or a button is missing.

### Exercise 2 — One form field, every state
Draw a labelled text field in all six mandatory states. Check the contrast of each.

??? success "Solution"
    The component structure (vertical Auto Layout, gap 6):
    - Label: 13 px Medium, `text/base`
    - Field: 44 px tall, 16 horizontal padding, 8 radius, 1 px border
    - Message (optional): 12 px Regular

    | State | Border | Fill | Text | Message |
    |-------|--------|------|------|---------|
    | Default | 1 px `#334155` | `#0F172A` | `text/muted` (placeholder) | — |
    | Hover | 1 px `#475569` | `#0F172A` | `text/muted` | — |
    | Focus | 2 px `brand/primary` + 2 px offset | `#0F172A` | `text/strong` | — |
    | Filled | 1 px `#334155` | `#0F172A` | `text/strong` | — |
    | Error | 2 px `feedback/error` | `#0F172A` | `text/strong` | `feedback/error`: "That email address is not valid" |
    | Disabled | 1 px `#1E293B` | `#111827` | `text/muted` 50% | — |

    **The checks:**
    - The default border: `#334155` on `#0F172A` → 2.1:1. It **fails** the 3:1 requirement for interactive elements. Fix: `#475569` → 3.4:1. Passes.
    - The error text: `#F87171` on `#0F172A` → 6.8:1. Passes.
    - The 44 px height meets the minimum touch target.

    **The mistake you avoided:** marking the error state with the red border **alone**. With a text message it also works for anyone who cannot distinguish red.

### Exercise 3 — The same screen at three widths
Take the list screen from exercise 1 and draw it at 390, 768 and 1440 px. Note exactly what changes at each threshold.

??? success "Solution"
    | Element | 390 px | 768 px | 1440 px |
    |---------|--------|--------|---------|
    | Navigation | Hamburger | Hamburger | 4 horizontal links + a button |
    | Margin | 16 | 32 | 96 |
    | Grid columns | 4 | 8 | 12 |
    | Cards per row | 1 | 2 | 3 |
    | Card width | Fill (358 px) | 4 columns | 4 columns |
    | Page title | 32 px | 40 px | 48 px |
    | Body text | 16 px | 16 px | 16 px |
    | Card image | 16:9 | 16:9 | 16:9 |

    **What does NOT change:** the palette, the fonts, the corner radii, the image ratios, the touch target heights.

    **The important observation:** body text stays 16 px at every width. 20 px text on desktop looks "too big" to most readers. What changes is the **line length**, controlled through column width, not through letter size.

    **The Auto Layout check:** if you built the cards on `Fill` inside a container with `Wrap`, the shift from 1 to 2 to 3 cards per row happens **by itself** when you change the screen width. If you had to move them by hand, the structure is incomplete.

---

## Mini-project: the club's project page

Design **three screens** of a website for the computer science club — the home page, the project list and a single project page — at all three breakpoints, using the visual identity from lesson 12.

??? success "Deliverables and criteria"
    **The Figma file structure:**

    | Page | Content |
    |------|---------|
    | `Flows` | The written flow + the screen map |
    | `Wireframes` | The 3 screens × 390 px, in grey |
    | `Components` | Button, field, card, navigation, badge — all with their states |
    | `Screens` | 3 screens × 3 breakpoints = 9 frames |
    | `Handoff` | Notes for the developer, empty states, edge cases |

    **The minimum components, with all their states:**

    | Component | States / variants |
    |-----------|-------------------|
    | `button` | 3 types × 5 states |
    | `input` | 6 states |
    | `card/project` | with image / without image |
    | `nav` | mobile (closed / open) + desktop |
    | `badge` | 3 categories |

    **The edge cases to draw:**
    - The **empty** project list ("No projects yet. Check back soon.")
    - A 12-word project title
    - A card with no image
    - The 404 error screen

    **The evaluation criteria:**

    | # | Criterion | Check |
    |---|-----------|-------|
    | 1 | The flow is written before drawing | The `Flows` page exists |
    | 2 | Mobile-first | The wireframes are at 390 px |
    | 3 | Every state drawn | Focus and disabled included |
    | 4 | Touch targets ≥ 44 px | Measure the small buttons |
    | 5 | Text contrast ≥ 4.5:1, interactive ≥ 3:1 | The Contrast plugin |
    | 6 | Labels above the fields | Not placeholder only |
    | 7 | Everything is Auto Layout | Change a screen's width — does it adapt? |
    | 8 | One primary button per screen | Count them |
    | 9 | Edge cases drawn | The 4 above |
    | 10 | Only styles, zero hand-typed HEX | Check 10 random elements |

    **The link to the Web course:** the screens you designed here get actually built in HTML and CSS. See [Flexbox and Grid](../web/08-css-flexbox-grid.md) for the structure and [Responsive design](../web/10-css-responsive.md) for the breakpoints. Your Auto Layout translates almost line for line.

---

## Summary

- **UX** = what the user can do; **UI** = how it looks and behaves.
- Write the **flow in words** before drawing a screen.
- **Wireframe** (structure, grey, 15 minutes) → **mockup** (appearance) → **prototype** (behaviour).
- **Mobile-first**: 390 → 768 → 1440 px; 4 → 8 → 12 columns.
- Every component has **6 states**: default, hover, focus, active, disabled, loading.
- **The focus outline is never removed.**
- Minimum touch target: **44 × 44 px**.
- Contrast: **4.5:1** text, **3:1** interactive elements.
- The label sits **above** the field; a placeholder is not a label.
- Handoff = a Figma link + components with states + 3 breakpoints + assets + **the edge cases**.

---

**Next step:** [→ Lesson 15: Visual identity for the computer science club](15-proiect-identitate-vizuala.md)
