---
lesson: 3
tags: [web, html, liste, tabele, ul, ol, thead, accesibilitate]
summary: Cum structurezi date cu liste neordonate, liste ordonate și tabele semantice — thead, tbody, colspan, rowspan, caption.
---

# Lecția 03 · Liste și tabele

!!! tip "Ce vei învăța"
    - Liste **neordonate** (`<ul>`) și **ordonate** (`<ol>`)
    - Liste imbricate și liste de descriere (`<dl>`)
    - Tabele: `<table>`, `<tr>`, `<td>`, `<th>`
    - Structura semantică: `<thead>`, `<tbody>`, `<tfoot>`
    - `colspan` și `rowspan` pentru celule mai mari
    - Când **să NU** folosești tabele (pentru layout)

---

## Liste neordonate

`<ul>` = *unordered list*. Fiecare rând e un `<li>` (*list item*).

```html
<h2>Ingrediente pentru sarmale</h2>
<ul>
  <li>Varză murată</li>
  <li>Carne tocată</li>
  <li>Orez</li>
  <li>Ceapă</li>
  <li>Condimente</li>
</ul>
```

Browser-ul afișează puncte (`•`) în fața fiecărui element.

---

## Liste ordonate

`<ol>` = *ordered list*. Se afișează cu numere `1. 2. 3.`

```html
<h2>Pași pentru a porni motorul</h2>
<ol>
  <li>Introdu cheia în contact.</li>
  <li>Rotește cheia la poziția „ON”.</li>
  <li>Apasă ambreiajul.</li>
  <li>Pornește motorul.</li>
</ol>
```

### Atribute utile

```html
<!-- Numerotează cu litere mari: A, B, C -->
<ol type="A">
  <li>Prima opțiune</li>
  <li>A doua opțiune</li>
</ol>

<!-- Începe de la 5: 5, 6, 7... -->
<ol start="5">
  <li>Punctul cinci</li>
  <li>Punctul șase</li>
</ol>

<!-- Ordine inversă: 3, 2, 1 -->
<ol reversed>
  <li>Bronz</li>
  <li>Argint</li>
  <li>Aur</li>
</ol>
```

Valori pentru `type`: `1` (implicit), `A`, `a`, `I`, `i`.

---

## Liste imbricate

O listă poate conține alte liste:

```html
<h2>Cursurile mele</h2>
<ul>
  <li>Matematică
    <ul>
      <li>Algebră</li>
      <li>Geometrie</li>
      <li>Analiză</li>
    </ul>
  </li>
  <li>Informatică
    <ul>
      <li>HTML / CSS</li>
      <li>Python</li>
      <li>Arduino</li>
    </ul>
  </li>
  <li>Limba română</li>
</ul>
```

!!! warning "Pune sub-lista ÎN interiorul `<li>`"
    Listele imbricate trebuie să fie **copii ale unui `<li>`**, nu între `<li>`-uri. Uite greșeala clasică:

    ```html
    <!-- GREȘIT -->
    <ul>
      <li>Matematică</li>
      <ul>
        <li>Algebră</li>
      </ul>
      <li>Informatică</li>
    </ul>
    ```

---

## Liste de descriere (`<dl>`)

Mai puțin folosite, dar perfecte pentru **glosare** și **perechi termen-definiție**:

```html
<dl>
  <dt>HTML</dt>
  <dd>Limbaj de marcare pentru structura paginilor.</dd>

  <dt>CSS</dt>
  <dd>Limbaj pentru stilizarea paginilor HTML.</dd>

  <dt>JavaScript</dt>
  <dd>Limbaj pentru interactivitatea paginilor.</dd>
</dl>
```

- `<dl>` = *description list*
- `<dt>` = *description term* (termenul)
- `<dd>` = *description details* (definiția)

---

## Tabele — structura de bază

Un tabel este o matrice: **rânduri** cu **celule**.

```html
<table>
  <tr>
    <th>Nume</th>
    <th>Vârstă</th>
    <th>Oraș</th>
  </tr>
  <tr>
    <td>Ana</td>
    <td>13</td>
    <td>Cluj</td>
  </tr>
  <tr>
    <td>Mihai</td>
    <td>14</td>
    <td>București</td>
  </tr>
</table>
```

- `<table>` — tabelul.
- `<tr>` (*table row*) — un rând.
- `<th>` (*table header*) — o celulă de **antet** (bold + centrat implicit).
- `<td>` (*table data*) — o celulă normală.

---

## Structura semantică

Un tabel profesionist are **3 zone**:

```html
<table>
  <thead>
    <tr>
      <th>Produs</th>
      <th>Preț</th>
      <th>Cantitate</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Caiet</td>
      <td>5 lei</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Pix</td>
      <td>2 lei</td>
      <td>30</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <td>Total</td>
      <td>120 lei</td>
      <td>42</td>
    </tr>
  </tfoot>
</table>
```

- `<thead>` — antetul (coloane, titluri)
- `<tbody>` — conținutul (rândurile cu date)
- `<tfoot>` — totaluri, sumar

Browser-ele și cititoarele de ecran pot trata cele 3 zone diferit (ex: antetul rămâne vizibil la imprimare).

---

## `colspan` și `rowspan`

Uneori o celulă trebuie să ocupe **mai multe coloane** sau **mai multe rânduri**.

### colspan (celulă pe mai multe coloane)

```html
<table>
  <tr>
    <th colspan="2">Contact</th>
  </tr>
  <tr>
    <td>Email</td>
    <td>ana@exemplu.ro</td>
  </tr>
  <tr>
    <td>Telefon</td>
    <td>+40 712 345 678</td>
  </tr>
</table>
```

### rowspan (celulă pe mai multe rânduri)

```html
<table>
  <tr>
    <th>Oraș</th>
    <th>Sezon</th>
    <th>Temperatură</th>
  </tr>
  <tr>
    <td rowspan="2">Cluj</td>
    <td>Vară</td>
    <td>25°C</td>
  </tr>
  <tr>
    <td>Iarnă</td>
    <td>-5°C</td>
  </tr>
</table>
```

Celula „Cluj” se întinde pe 2 rânduri; nu o mai scrii a doua oară.

---

## Când să NU folosești tabele

În anii 2000, oamenii foloseau `<table>` pentru **întreg aspectul paginii** (coloane, sidebar, etc.). **Greșit!**

- Tabelele sunt pentru **date tabelare**: rânduri × coloane de informații legate.
- Pentru **aspectul paginii** (navigație sus, conținut la mijloc, sidebar) folosim **Flexbox** și **Grid** — vei învăța în Lecția 08.

!!! warning "Regulă simplă"
    Dacă datele ar avea sens și într-un Excel/Sheets — e tabel. Dacă e doar „vreau două coloane pe pagină” — **NU** e tabel.

---

## Accesibilitate pentru tabele

### `<caption>` — titlu pentru tabel

```html
<table>
  <caption>Orarul clasei a VIII-a A</caption>
  <thead>
    ...
  </thead>
</table>
```

Apare deasupra tabelului și e citit de screen reader-e.

### `scope` pentru antete

```html
<tr>
  <th scope="col">Luni</th>
  <th scope="col">Marți</th>
</tr>
<tr>
  <th scope="row">08:00</th>
  <td>Mate</td>
  <td>Româna</td>
</tr>
```

- `scope="col"` — antet de **coloană**.
- `scope="row"` — antet de **rând**.

Cititoarele de ecran folosesc `scope` ca să spună utilizatorului: „celula Mate este la intersecția rândului 08:00 cu coloana Luni”.

---

## Exerciții

### Exercițiu 1 — Programele tale TV
Fă o listă neordonată cu 5 programe / seriale preferate.

??? success "Soluție"
    ```html
    <h2>Programele mele preferate</h2>
    <ul>
      <li>Stranger Things</li>
      <li>Las Fierbinți</li>
      <li>MasterChef</li>
      <li>Pro TV Știri</li>
      <li>Vocea României</li>
    </ul>
    ```

### Exercițiu 2 — Liste imbricate
Fă o listă cu 3 materii, iar sub fiecare câte 3 subteme.

??? success "Soluție"
    ```html
    <ul>
      <li>Matematică
        <ul>
          <li>Ecuații</li>
          <li>Geometrie</li>
          <li>Probabilități</li>
        </ul>
      </li>
      <li>Fizică
        <ul>
          <li>Mecanică</li>
          <li>Optică</li>
          <li>Electricitate</li>
        </ul>
      </li>
      <li>Chimie
        <ul>
          <li>Elemente</li>
          <li>Reacții</li>
          <li>Substanțe organice</li>
        </ul>
      </li>
    </ul>
    ```

### Exercițiu 3 — Tabel cu 4 coloane
Fă un tabel cu coloanele Nume, Vârstă, Oraș, Clasa și 3 rânduri de elevi.

??? success "Soluție"
    ```html
    <table>
      <caption>Elevii din echipa de informatică</caption>
      <thead>
        <tr>
          <th scope="col">Nume</th>
          <th scope="col">Vârstă</th>
          <th scope="col">Oraș</th>
          <th scope="col">Clasa</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Ana Pop</td>
          <td>13</td>
          <td>Cluj</td>
          <td>VII-a B</td>
        </tr>
        <tr>
          <td>Mihai Radu</td>
          <td>14</td>
          <td>București</td>
          <td>VIII-a A</td>
        </tr>
        <tr>
          <td>Elena Ionescu</td>
          <td>12</td>
          <td>Chișinău</td>
          <td>VI-a C</td>
        </tr>
      </tbody>
    </table>
    ```

---

## Mini-proiect: „Orar școlar”

Construiește un tabel cu orarul săptămânal: **coloane** = zilele (Luni–Vineri), **rânduri** = orele (08:00, 09:00, 10:00, ...).

- Folosește `<thead>` pentru zilele săptămânii.
- Folosește `<tbody>` pentru orele și materiile.
- Adaugă `<caption>` cu titlul „Orar clasa a VIII-a A”.
- Folosește `scope="col"` și `scope="row"` corect.
- Pentru o pauză mai lungă (ex: 12:00–13:00), folosește `colspan="5"` pe celula „Pauză de masă”.

??? success "Soluție"
    ```html
    <!DOCTYPE html>
    <html lang="ro">
    <head>
      <meta charset="UTF-8">
      <title>Orar școlar</title>
    </head>
    <body>
      <h1>Orarul săptămânii</h1>

      <table>
        <caption>Orar clasa a VIII-a A</caption>

        <thead>
          <tr>
            <th scope="col">Ora</th>
            <th scope="col">Luni</th>
            <th scope="col">Marți</th>
            <th scope="col">Miercuri</th>
            <th scope="col">Joi</th>
            <th scope="col">Vineri</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <th scope="row">08:00</th>
            <td>Matematică</td>
            <td>Română</td>
            <td>Fizică</td>
            <td>Engleză</td>
            <td>Informatică</td>
          </tr>
          <tr>
            <th scope="row">09:00</th>
            <td>Română</td>
            <td>Matematică</td>
            <td>Chimie</td>
            <td>Istorie</td>
            <td>Mate</td>
          </tr>
          <tr>
            <th scope="row">10:00</th>
            <td>Engleză</td>
            <td>Informatică</td>
            <td>Biologie</td>
            <td>Mate</td>
            <td>Română</td>
          </tr>
          <tr>
            <th scope="row">11:00</th>
            <td>Sport</td>
            <td>Geografie</td>
            <td>Română</td>
            <td>Fizică</td>
            <td>Desen</td>
          </tr>
          <tr>
            <th scope="row">12:00</th>
            <td colspan="5">Pauză de masă</td>
          </tr>
          <tr>
            <th scope="row">13:00</th>
            <td>Desen</td>
            <td>Muzică</td>
            <td>Cerc IT</td>
            <td>—</td>
            <td>—</td>
          </tr>
        </tbody>
      </table>
    </body>
    </html>
    ```

---

## Rezumat

- `<ul>` pentru liste fără ordine; `<ol>` când ordinea contează.
- Imbricări: pune sub-lista **în interiorul** unui `<li>`.
- Tabele = date tabelare, **nu** pentru layout.
- Folosește `<thead>`, `<tbody>`, `<tfoot>` pentru tabele serioase.
- `colspan` / `rowspan` pentru celule mai mari.
- `<caption>` + `scope` = tabel accesibil.

---

**Pasul următor:** [→ Lecția 04: Formulare](04-html-formulare.md)
