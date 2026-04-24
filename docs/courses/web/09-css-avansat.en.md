---
lesson: 9
tags: [web, css, pseudo-classes, transitions, animations, transform, hover]
summary: Interactive effects and animations using only CSS — no JavaScript.
---

# Lesson 09 · Advanced CSS: pseudo-classes, transitions, and animations

!!! tip "What you will learn"
    - **Pseudo-classes** (`:hover`, `:focus`, `:nth-child`) and pseudo-elements (`::before`, `::after`)
    - **Transitions** smoothly between two states
    - **Transform**: rotation, scaling, translation
    - **@keyframes** — full animations
    - Popular modern effects you use on any site

---

## Pseudo-classes

A pseudo-class attaches to a selector with `:` and selects the element in a particular **state**.

### Interaction pseudo-classes

```css
/* The mouse is over the element */
.button:hover {
  background-color: #4338ca;
}

/* The element is focused (tab in a form) */
input:focus {
  border-color: #4f46e5;
  outline: 2px solid #c7d2fe;
}

/* At the moment of the click (pressed) */
.button:active {
  transform: translateY(1px);
}

/* Already visited link */
a:visited {
  color: #7c3aed;
}
```

!!! warning "Don't remove `:focus` visually"
    `outline: none` without putting something else in its place **breaks accessibility**. Keyboard users (including those with disabilities) no longer know where they are. Always leave a visible border at `:focus`.

### Structural pseudo-classes

```css
/* The first child of the parent */
li:first-child {
  font-weight: 700;
}

/* The last child */
li:last-child {
  border-bottom: none;
}

/* Even rows in a table */
tr:nth-child(even) {
  background-color: #f9fafb;
}

/* Odd rows */
tr:nth-child(odd) {
  background-color: white;
}

/* Every third element */
.card:nth-child(3n) {
  background-color: #ede9fe;
}

/* All, EXCEPT .active */
.tab:not(.active) {
  opacity: 0.6;
}
```

### Pseudo-classes for forms

```css
input:disabled {
  background-color: #f3f4f6;
  cursor: not-allowed;
}

input:checked + label {
  font-weight: 700;
}

input:required {
  border-left: 3px solid red;
}

input:valid {
  border-color: green;
}

input:invalid {
  border-color: red;
}
```

---

## Pseudo-elements

Two colons (`::`) instead of one. Creates **virtual** content that doesn't exist in the HTML.

```css
.quote::before {
  content: "“";
  color: #9ca3af;
  font-size: 2rem;
}

.quote::after {
  content: "”";
  color: #9ca3af;
  font-size: 2rem;
}
```

Common uses:

- Decorative quotation marks
- Icons before a link
- Separator between links (`::after { content: " · "; }`)
- Overlays over images

```css
/* Breadcrumb with automatic separator */
.breadcrumb li + li::before {
  content: " › ";
  color: #9ca3af;
  padding: 0 0.5rem;
}
```

---

## Transitions

A transition animates the change of a property from one value to another.

### Syntax

```css
.button {
  background-color: #4f46e5;
  transition: background-color 0.3s ease;
  /*          ^prop          ^duration ^curve */
}

.button:hover {
  background-color: #4338ca;   /* smoothly transitions from one color to another */
}
```

### Multiple properties

```css
.card {
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
```

### `all` — all properties

```css
.button {
  transition: all 0.2s ease;   /* convenient, but less performant */
}
```

### Timing functions (animation curves)

| Value | Character |
|---------|----------|
| `linear` | constant speed (robotic) |
| `ease` (default) | starts slow, accelerates, slows down |
| `ease-in` | starts slow, ends fast |
| `ease-out` | starts fast, ends smooth |
| `ease-in-out` | slow at the ends, fast in the middle |
| `cubic-bezier(...)` | custom curve |

!!! tip "`ease-out` for UI"
    Effects that appear to the user (hover, fade-in) feel most natural with `ease-out` — they move quickly, then slow down.

---

## Transform — rotation, scaling, translation

`transform` applies **geometric transformations** without affecting the layout. Other elements **don't move** when an element is transformed.

```css
.element {
  /* Translation — movement on X / Y */
  transform: translate(10px, -5px);
  transform: translateX(20px);
  transform: translateY(-10px);

  /* Scaling */
  transform: scale(1.1);         /* 110% */
  transform: scaleX(2);          /* 2 times wider */

  /* Rotation */
  transform: rotate(45deg);
  transform: rotate(-90deg);

  /* Skew */
  transform: skew(10deg, 0);

  /* Combined — applied right to left */
  transform: translateY(-4px) scale(1.05) rotate(2deg);
}
```

!!! note "Why `transform` is so powerful"
    The browser runs `transform` and `opacity` on the **GPU**, using compositing. Animations are smooth even on old phones — unlike `margin` or `top`, which trigger layout reflow (slow).

---

## Animations with `@keyframes`

For complex animations (multiple steps) you use `@keyframes` + `animation`.

### Syntax

```css
@keyframes pulse {
  0%   { transform: scale(1); }
  50%  { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.pulsing {
  animation: pulse 2s ease-in-out infinite;
  /*         ^name ^duration ^curve ^repeat */
}
```

### Detailed syntax

```css
.element {
  animation-name: pulse;
  animation-duration: 2s;
  animation-timing-function: ease-in-out;
  animation-delay: 0s;
  animation-iteration-count: infinite;   /* or a number: 3, 1, ... */
  animation-direction: normal;           /* normal | reverse | alternate */
  animation-fill-mode: forwards;         /* keeps the final state */
}
```

### Examples

```css
/* Fade-in on page load */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero {
  animation: fadeIn 0.6s ease-out;
}

/* Spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.loader {
  animation: spin 1s linear infinite;
}

/* Shake (for form errors) */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25%      { transform: translateX(-8px); }
  75%      { transform: translateX(8px); }
}

.input-error {
  animation: shake 0.3s ease;
}
```

!!! warning "Respect `prefers-reduced-motion`"
    Some users disable animations for medical reasons (motion sickness, epilepsy). Provide a simplified variant:
    ```css
    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
      }
    }
    ```

---

## Popular effects

### Button with "lift" on hover

```css
.button {
  background: #4f46e5;
  color: white;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(79, 70, 229, 0.3);
}
```

### Card that grows on hover

```css
.card {
  transition: transform 0.3s ease;
}

.card:hover {
  transform: scale(1.03);
}
```

### Animated underline

```css
.link {
  position: relative;
  text-decoration: none;
  color: #1f2937;
}

.link::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: #4f46e5;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.link:hover::after {
  transform: scaleX(1);
}
```

---

## Exercises

### Exercise 1 — Button with colored hover

The button changes its background color smoothly (0.3s) on hover.

??? success "Solution"
    ```html
    <button class="cta">Subscribe</button>
    ```
    ```css
    .cta {
      background-color: #10b981;
      color: white;
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 8px;
      font-size: 1rem;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .cta:hover {
      background-color: #059669;
    }
    ```

### Exercise 2 — First element with different style

The first `<li>` in a list has a different color.

??? success "Solution"
    ```css
    li:first-child {
      color: #4f46e5;
      font-weight: 700;
    }
    ```

### Exercise 3 — Even rows in a table

The even rows have a light gray background (zebra effect).

??? success "Solution"
    ```css
    tr:nth-child(even) {
      background-color: #f9fafb;
    }

    tr:hover {
      background-color: #e0e7ff;
    }
    ```

### Exercise 4 — Beating heart

A heart that pulses in a loop, like a heartbeat.

??? success "Solution"
    ```html
    <div class="heart">&#9829;</div>
    ```
    ```css
    .heart {
      font-size: 4rem;
      color: #e11d48;
      display: inline-block;
      animation: heartbeat 1.2s ease-in-out infinite;
    }

    @keyframes heartbeat {
      0%, 100% { transform: scale(1); }
      25%      { transform: scale(1.2); }
      50%      { transform: scale(1); }
      75%      { transform: scale(1.15); }
    }

    /* Respect user preferences */
    @media (prefers-reduced-motion: reduce) {
      .heart { animation: none; }
    }
    ```

---

## Mini-project: Modern "premium" button

A button with hover: lift, shadow, gradient shift, and smooth transition.

??? success "Solution"
    **index.html**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Premium button</title>
      <link rel="stylesheet" href="styles.css">
    </head>
    <body>
      <main>
        <button class="premium-button">
          Get started
        </button>
      </main>
    </body>
    </html>
    ```

    **styles.css**
    ```css
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: "Inter", sans-serif;
      background: #f9fafb;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }

    .premium-button {
      position: relative;
      padding: 1rem 2.5rem;
      font-size: 1.1rem;
      font-weight: 600;
      color: white;
      border: none;
      border-radius: 12px;
      cursor: pointer;

      /* Background gradient */
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      background-size: 200% 200%;
      background-position: 0% 50%;

      /* Initial shadow */
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.3);

      /* Transition covers all properties changed on hover */
      transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background-position 0.6s ease;
    }

    .premium-button:hover {
      /* Lift effect */
      transform: translateY(-3px);
      /* Larger and more diffuse shadow */
      box-shadow: 0 10px 28px rgba(99, 102, 241, 0.45);
      /* The gradient shifts subtly */
      background-position: 100% 50%;
    }

    .premium-button:active {
      /* Slight press on click */
      transform: translateY(-1px);
    }

    /* Visible focus for accessibility */
    .premium-button:focus-visible {
      outline: 3px solid #c7d2fe;
      outline-offset: 2px;
    }

    /* Respect user preferences */
    @media (prefers-reduced-motion: reduce) {
      .premium-button { transition: none; }
      .premium-button:hover { transform: none; }
    }
    ```

    **How it works:**

    - `background-size: 200%` makes the gradient larger than the button
    - `background-position` shifts the "window" that shows part of the gradient
    - On hover, the position changes from `0%` to `100%` → color flow effect
    - `translateY(-3px)` + larger shadow → impression of floating
    - `:focus-visible` ensures accessibility for keyboard users

---

## Summary

- **Pseudo-classes** (`:hover`, `:focus`, `:nth-child`) select the element in a state
- **Pseudo-elements** (`::before`, `::after`) create decorative content without HTML
- `transition` animates changes between states — minimum for modern UI
- `transform` (translate, scale, rotate) is **fast** — runs on the GPU
- `@keyframes` + `animation` for animations with multiple steps
- Respect `prefers-reduced-motion` for accessibility
- Keep a visual indicator at `:focus`

---

**Next step:** [→ Lesson 10: Responsive design](10-css-responsive.md)
