---
description: Add or edit a course/project page on ursoaia-edu.online. Bilingual RO+EN mandatory. Asks for preview image if missing. Updates mkdocs nav and runs strict build.
argument-hint: "[free-text brief, e.g. 'esp32 project: water level sensor']"
---

You are helping the user add or edit content for the MkDocs site at https://ursoaia-edu.online.

User brief: $ARGUMENTS

## Non-negotiable rules

1. **Bilingual or nothing.** Every content page exists as a pair:
   - Romanian (canonical): `<slug>.md`
   - English: `<slug>.en.md`
   Generate both. Never commit only one. RO is the source of truth — write it first, then translate to EN keeping section structure 1:1.

2. **Preview image is required for project pages.** If the user did not include one in the brief, **STOP and ask** for it before generating files. Accept either a local path or a URL. If a URL, download it into the project. Do not invent or generate a placeholder.

3. **`mkdocs.yml` nav must be updated.** New pages must be added to the `nav:` tree. If the English title differs from the canonical Romanian display name, add a `nav_translations:` entry under the `ro` locale so the Romanian site shows the right name.

4. **Strict build must pass.** Always end with `uv run build --strict`. If it warns or errors, fix and retry. Don't claim done until the build is green.

## Workflow

### Step 1 — Clarify intent

From the brief, determine:
- **Type:** project page / course lesson / overview revision / index card update
- **Target directory:** `docs/projects/<platform>/` or `docs/courses/<track>/`
- **Slug:** filename without extension (kebab-case, no spaces, ASCII)

If anything is ambiguous, ask one focused question — don't guess platform or track.

### Step 2 — Read a sibling page

Before writing anything, `Read` an existing page in the same directory (e.g. for a new ESP32 project, read `docs/projects/esp32/led_blink.md` and its `.en.md`). Mirror:
- Frontmatter fields and order
- Section heading style (e.g. `Descriere` / `Cod` / `Materiale` / `Schemă` for projects; `Obiective` / lesson body / `Exerciții` for course pages)
- Image embedding pattern with relative `../../assets/images/...` paths
- Tone and terminology

### Step 3 — Gather missing inputs

Ask the user for anything missing in one consolidated message:
- Title (RO; EN if you can't translate confidently)
- One-sentence summary
- Tags (3–5)
- Body content (or bullet points to expand)
- **Preview image** (path or URL) — required for projects, optional for course lessons
- Wiring diagram / extra images, if applicable
- Source code (paste it, or point to a file)

### Step 4 — Place the preview image

Save to `docs/assets/images/<section>/preview-<slug>.<ext>` (or for course assets, `docs/assets/images/courses/<track>/<filename>`). Reference it:
- In frontmatter: `image: assets/images/<section>/preview-<slug>.<ext>` (path relative to `docs/`)
- Inside the markdown body (if you embed it): `../../assets/images/<section>/preview-<slug>.<ext>` (relative to the page file)

If the user provided a URL, use `Bash` with `curl -L -o` to fetch it.

### Step 5 — Generate the Romanian page

Frontmatter shape for **project pages**:

```yaml
---
category: <Platform name, e.g. ESP32>
tags: [Tag1, Tag2, MicroPython]
summary: "Propoziție scurtă în română care descrie proiectul."
image: assets/images/projects/<platform>/preview-<slug>.jpg
---
```

Add `featured: true` only if the user explicitly asks for homepage hero placement.

Frontmatter shape for **course lesson pages**:

```yaml
---
tags: [python, începători]
summary: "Ce acoperă lecția."
---
```

Body conventions:
- Open with one paragraph framing what the reader will build/learn.
- Embed the preview image right after that paragraph.
- Use the section headings the sibling page uses, in the same order.
- Code blocks: tag with the right language (`python`, `cpp`, `bash`, `html`, `css`, `javascript`).
- Use admonitions (`!!! tip "..."`, `!!! warning "..."`) for callouts when neighbors do.

### Step 6 — Generate the English page

Same structure, translate body and frontmatter strings. Keep the `image:` path identical to the RO file (the asset is shared). Update `tags:` to English equivalents.

### Step 7 — Update `mkdocs.yml`

- Insert the new `- "Title": <path>.md` line under the correct section in `nav:`.
- If the English nav title differs from a Romanian display name, add a mapping under `plugins.i18n.languages[ro].nav_translations` (e.g. `"Water Level Sensor": "Senzor nivel apă"`).
- Preserve existing indentation and order.

### Step 8 — Strict build

Run `uv run build --strict` and read the output. Fix any warnings (broken nav entries, missing files, broken links). Don't suppress warnings — fix them.

### Step 9 — Report

List created and modified files. Mention anything you couldn't translate confidently or that needs the user's eyes. Do **not** commit unless the user says so.

## Style guardrails

- Romanian is the canonical voice. Match the existing tone of `docs/projects/esp32/led_blink.md` and `docs/courses/python/00-pregatire.md` for projects and lessons respectively.
- Concrete examples beat generic ones. Use real numbers, real GPIO pins, real names students recognize (Cluj, Chișinău, București).
- No emoji unless explicitly requested.
- No marketing fluff. No "in this exciting tutorial we will explore…".
- Keep `summary` to one sentence.
- Tags lowercase except proper nouns.

## When NOT to use this command

- Single typo fix → use `Edit` directly.
- Pure template/CSS work → edit `custom_theme/` directly.
- Cross-cutting refactors (rename a section, restructure many files) → use a planning + bulk-edit approach instead.

## Quick examples

```
/content esp32 project: water level sensor with float switch on GPIO 14
```
→ Asks for preview image. Reads `docs/projects/esp32/led_blink.md`. Generates `docs/projects/esp32/water_level.md` + `.en.md` with `category: ESP32`, wiring, code. Updates nav. Builds strict.

```
/content edit projects/arduino/led_cube: tighten summary and add a "common pitfalls" section
```
→ Reads existing RO + EN. Edits both in lockstep. Rebuilds.

```
/content course lesson: python turtle shapes — a deeper dive after lesson 11
```
→ Asks slug + position in nav. Generates RO `.md` + EN `.en.md` matching the existing `docs/courses/python/` lesson shape. Updates nav. Builds strict.
