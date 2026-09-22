---
lesson: 1
tags: [figma, canva, tools, interface, getting started]
summary: A free Figma and Canva account, the interface of each, your first file, saving, sharing, and when to use which.
---

# Lesson 01 · Figma and Canva — first contact

!!! tip "What you will learn"
    - How to create a **free account** in Figma and Canva
    - What a **frame** is and why you never draw "on an empty canvas"
    - The Figma interface: left panel, canvas, right panel
    - The **keyboard shortcuts** you will use in every lesson
    - How to save, how to share and how to go back to an old version
    - **When to use Figma and when Canva**

---

## Two tools, two jobs

| | Figma | Canva |
|---|-------|-------|
| **Good for** | Drawing from scratch, with full control | Starting from a template and adapting it |
| **Graphics type** | Vector (scales to any size) | Mixed, template-oriented |
| **Strength** | Components, Auto Layout, prototypes | Speed, a huge library of elements |
| **Weakness** | Steeper learning curve | Limited fine control; many works look alike |
| **We use it for** | Logos, interfaces, prototypes (lessons 07–12, 14, 16) | Posts, stories, quick materials (lesson 13) |

!!! note "Why we start with Figma"
    Canva gives you good-looking results in 10 minutes, but it does not teach you *why* they look good — the decisions have already been made by the template. Figma forces you to make every decision yourself. We learn in Figma first, then use Canva as a speed tool.

---

## Account and installation

### Figma

1. Go to [figma.com](https://www.figma.com/) and click **Sign up**.
2. Use an email address (ideally your school one — see below).
3. When asked about the plan, pick **Starter** (free). It is enough for the whole course.
4. You can work straight in the browser. The desktop app is optional and downloads from **Products → Desktop app**.

!!! tip "Free Education plan"
    With a school email address you can request the **Figma for Education** plan, which unlocks unlimited team projects and shared libraries. Apply at [figma.com/education](https://www.figma.com/education/). The course works fully on the regular Starter plan too.

### Canva

1. Go to [canva.com](https://www.canva.com/) and click **Sign up**.
2. Choose **Canva Free**.
3. If your school has an account, **Canva for Education** is free and unlocks the Pro elements.

!!! warning "The crown-marked elements"
    In Canva, elements marked with a **crown** are Pro. If you use them on a free account, the exported image will carry a watermark or you will be asked to pay. Always filter by **Free** before choosing.

---

## The Figma interface

Open Figma and create a new file: **+ Design file**. You will see three areas.

```
┌──────────────┬────────────────────────────┬──────────────┐
│              │                            │              │
│    LEFT      │                            │    RIGHT     │
│    PANEL     │         CANVAS             │    PANEL     │
│              │     (infinite surface)     │              │
│              │                            │              │
│  Layers      │    ┌──────────────┐        │  Position    │
│  Pages       │    │              │        │  Size        │
│  Assets      │    │    Frame     │        │  Fill        │
│              │    │              │        │  Stroke      │
│              │    └──────────────┘        │  Effects     │
│              │                            │              │
└──────────────┴────────────────────────────┴──────────────┘
```

**The left panel** — the list of layers (**Layers**). Everything you draw shows up here, newest at the top. This is where you select, rename, group and hide elements.

**The canvas** — the infinite surface. You move around it with the mouse wheel (or two fingers on a trackpad) and zoom with ++ctrl++ + wheel.

**The right panel** — the properties of the selected element: where it is, how big it is, what colour it has. With nothing selected, it shows the page properties.

---

## The frame: your real canvas

The Figma canvas is infinite, but a poster is not. The **frame** is the rectangle representing the final format: an A3 page, a phone screen, a square post.

Create a frame with the ++f++ key. The right panel shows a list of ready-made formats:

| Category | Useful formats |
|----------|----------------|
| **Phone** | iPhone 14 — 390 × 844 px |
| **Desktop** | Desktop — 1440 × 1024 px |
| **Paper** | A4 — 595 × 842 pt, A3 — 842 × 1191 pt |
| **Social media** | Instagram post — 1080 × 1080 px, Story — 1080 × 1920 px |

!!! note "The golden rule"
    **You always draw inside a frame**, never directly on the canvas. An element outside a frame cannot be exported properly and does not appear in a prototype.

A frame can contain other frames. You will use this constantly: a "Card" frame inside a "Page" frame.

---

## The basic tools

The top bar holds the tools. Each has a shortcut — learn them now, they save you hours.

| Tool | Key | What it does |
|------|-----|--------------|
| Move | ++v++ | Select and move |
| Frame | ++f++ | Create a frame |
| Rectangle | ++r++ | Rectangle |
| Ellipse | ++o++ | Circle / ellipse |
| Line | ++l++ | Line |
| Pen | ++p++ | Free vector shape (lesson 07) |
| Text | ++t++ | Text |
| Hand | ++h++ or ++space++ | Move the canvas |
| Comment | ++c++ | Add a comment |

### Shortcuts you will use daily

| Action | Windows / Linux | macOS |
|--------|-----------------|-------|
| Duplicate the selection | ++ctrl+d++ | ++cmd+d++ |
| Group | ++ctrl+g++ | ++cmd+g++ |
| Wrap in a frame | ++ctrl+alt+g++ | ++cmd+option+g++ |
| Zoom to selection | ++shift+2++ | ++shift+2++ |
| Zoom to fit all | ++shift+1++ | ++shift+1++ |
| Zoom 100% | ++shift+0++ | ++shift+0++ |
| Lock the element | ++ctrl+shift+l++ | ++cmd+shift+l++ |
| Undo | ++ctrl+z++ | ++cmd+z++ |

!!! tip "Three shortcuts that change everything"
    - ++shift++ while drawing a rectangle → a **perfect square**; on an ellipse → a **perfect circle**; on a line → 45° angles.
    - ++alt++ (++option++ on Mac) while dragging an element → **duplicates** it.
    - ++alt++ held with one element selected and the mouse over another → shows you the **distance** between them in pixels. You will use this in every lesson about spacing.

---

## Your first file: a name card

Let's make something concrete. A 400 × 250 px card with your name.

1. Press ++f++, then in the right panel type **W: 400**, **H: 250** by hand. The frame appears on the canvas.
2. Double-click its name in the left panel and rename it `Card`.
3. With the frame selected, in the right panel under **Fill** click the colour swatch and type the code `1F2937`. The background turns dark grey.
4. Press ++t++, drag a text box inside the card and type your name.
5. In the right panel set: font **Inter**, **Semi Bold**, size **28**, colour `FFFFFF`.
6. Press ++t++ again, type "computer club member" underneath, size **14**, colour `9CA3AF`.
7. Select both texts (++shift++ + click) and, in the right panel, press the **Align left** button.

!!! note "What you actually did"
    You applied three principles without naming them: **contrast** (28 pt vs. 14 pt, white vs. grey), **proximity** (the two texts sit close, so they read as one block) and **alignment** (the same left edge). These are lessons 05 and 06, you just did them on autopilot.

---

## Saving, versions, sharing

### Saving

**Figma saves by itself.** There is no ++ctrl+s++ for content — every change goes straight to the cloud. The file name is changed by double-clicking it at the top.

### Version history

Menu **Figma → File → Show version history**. You see every stage of the file and can return to any of them.

!!! tip "Mark the important stages"
    In the history panel press **+** and name the version: "version 1, before feedback". Two weeks from now you will know exactly what to go back to.

### Sharing

The **Share** button, top right. Choose:

| Option | Who can | When you use it |
|--------|---------|-----------------|
| **Anyone with the link → can view** | Anyone with the link, view and comment only | Sending it out for feedback |
| **Anyone with the link → can edit** | Anyone with the link can modify | Working on a project as a team |
| **Only invited people** | Only people invited by email | The default; the safest |

!!! warning "Careful with public 'can edit'"
    A public link with edit rights can be modified by anyone who has it. For feedback, always send **can view** — comments still work, with the ++c++ key.

---

## The Canva interface in short

Canva is simpler. Three things to know:

1. **Format search.** On the home page type "Instagram post" or "A3 poster" and Canva creates the canvas at the right size.
2. **The left panel.** Tabs: **Design** (templates), **Elements** (shapes, icons, illustrations), **Text**, **Uploads** (your files), **Projects**.
3. **The Share → Download button.** Formats: PNG (default), JPG, PDF Standard (screen), PDF Print (printing).

!!! tip "Start from a template, but change it seriously"
    If you use an untouched Canva template, your work will look like ten thousand others. The rule we use in lesson 13: **you must change the colours and the fonts** to the ones from your own visual identity. The template stays as structure only.

---

## Exercises

### Exercise 1 — Three frames, three formats
In a new Figma file, create three frames side by side: an **A4** (portrait), an **Instagram post** (1080 × 1080) and an **iPhone 14** (390 × 844). Rename them properly in the Layers panel.

??? success "Solution"
    - ++f++ → in the right panel, the **Paper** category → **A4**.
    - ++f++ → **Social media** → **Instagram post**.
    - ++f++ → **Phone** → **iPhone 14**.

    If the frames overlap, select them all (++ctrl+a++) and use the **Tidy up** button in the right panel — it aligns and spaces them evenly, automatically.

    Renaming is done by double-clicking the name in Layers. Names like "Frame 1, Frame 2, Frame 3" look harmless now, but in a file with 40 layers they become a nightmare.

### Exercise 2 — Perfect square and perfect circle
Draw a square of exactly 200 × 200 px and a circle of exactly 200 × 200 px, side by side, 40 px apart. Check the distance with ++alt++.

??? success "Solution"
    - ++r++, then hold ++shift++ while dragging → a square. Correct it to 200 × 200 in the right panel.
    - ++o++, ++shift++ held → a circle. Same, 200 × 200.
    - Select the square, hold ++alt++ and move the mouse over the circle: Figma shows the distance in red. Move the circle until you read **40**.

    Alternatively: select both shapes and, in the right panel, under **Auto layout** (++shift+a++) set the gap to 40. You will learn this in depth in lesson 09.

### Exercise 3 — Share for comments
Share the file from exercise 1 with a classmate, with **view** rights, and ask them to leave a comment with the ++c++ key on the A4 frame.

??? success "Solution"
    - **Share** → **Anyone with the link** → **can view** → **Copy link**.
    - Your classmate opens the link, presses ++c++, clicks the frame and writes the comment.
    - Comments appear as bubbles on the canvas and in the comments panel (the message icon, top right). You close them with **Resolve** once you have made the change.

    Notice that although your classmate cannot edit, they can comment. That is exactly what you want for feedback.

---

## Mini-project: your membership card

Build a computer club membership card, **400 × 250 px**, containing: your name, your class, your role in the club and one graphic element (a circle or a coloured rectangle) used as an accent.

??? success "Solution"
    A result that works:

    1. Frame `Member card`, 400 × 250, Fill `0F172A`.
    2. A 6 × 250 px rectangle on the left edge, Fill `F97316` — the accent bar. Made with ++r++, then X: 0, Y: 0, W: 6, H: 250.
    3. Text `Ana Popescu` — Inter Semi Bold 26, white, placed at X: 32, Y: 48.
    4. Text `Grade 9B` — Inter Regular 14, colour `94A3B8`, 8 px below the name.
    5. Text `ESP32 project lead` — Inter Medium 13, colour `F97316`, 20 px further down.
    6. All three texts aligned left, on the same X: 32 coordinate.

    **Why it works:** a single accent colour (the orange), used twice — the bar and the role — ties the card together visually. The three text sizes (26 / 14 / 13) create a clear hierarchy: the name first, the rest after. The 32 px left and 48 px top margins give the card air.

    **Common mistakes:** text glued to the frame edge (leave at least 24 px), three accent colours instead of one, texts aligned "approximately" instead of exactly on the same X coordinate.

---

## Summary

- **Figma** for control and construction; **Canva** for speed and templates.
- Both have **free** plans that cover the whole course; with a school email you can request **Education**.
- You always draw **inside a frame** (++f++), never on a bare canvas.
- Essential shortcuts: ++v++ ++f++ ++r++ ++o++ ++t++, ++shift++ for perfect shapes, ++alt++ for duplicating and for measuring distances.
- Figma **saves automatically**; important stages get marked in **version history**.
- For feedback, share with **can view** — comments work with ++c++.
- An unmodified Canva template looks like everyone else's; change its colours and fonts.

---

**Next step:** [→ Lesson 02: Shape, line, space](02-forma-linie-spatiu.md)
