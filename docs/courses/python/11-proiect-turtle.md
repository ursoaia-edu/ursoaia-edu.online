---
lesson: 11
tags: [python, turtle, grafice, desen, animație]
summary: Proiect final — desenează forme geometrice și spirale cu modulul turtle.
---

# Lecția 11 · Proiect: Grafice cu Turtle

!!! tip "Ce vei exersa"
    - Modulul `turtle` pentru grafică vectorială
    - Bucle `for` pentru a desena forme repetitive
    - Funcții pentru forme reutilizabile
    - Creativitate — îți creezi propria artă cu cod

---

## Ce este modulul `turtle`?

`turtle` este un modul Python care simulează o "broască țestoasă" ce desenează pe ecran. O controlezi cu comenzi simple: `forward()`, `left()`, `right()`. Este instalat implicit cu Python.

```python
import turtle

t = turtle.Turtle()   # creează broasca
t.forward(100)        # merge 100 pixeli înainte
t.left(90)            # se întoarce 90° la stânga
t.forward(100)        # merge 100 pixeli înainte

turtle.done()         # menține fereastra deschisă
```

---

## Comenzile principale

### Mișcare

```python
t.forward(n)    # merge n pixeli înainte
t.backward(n)   # merge n pixeli înapoi
t.right(grade)  # se întoarce la dreapta
t.left(grade)   # se întoarce la stânga
t.goto(x, y)    # sare la coordonatele (x, y)
t.home()        # revine la origine (0, 0)
```

### Controlul creionului

```python
t.penup()               # ridică creionul (nu desenează la mișcare)
t.pendown()             # coboară creionul (desenează)
t.pensize(3)            # grosimea liniei
t.pencolor("red")       # culoarea liniei
t.fillcolor("yellow")   # culoarea de umplere
t.begin_fill()          # start umplere
t.end_fill()            # stop umplere
```

### Viteza și aspectul

```python
t.speed(0)              # 0 = maxim, 1 = lent, 10 = rapid
t.hideturtle()          # ascunde broasca (imagine mai curată)
turtle.bgcolor("black") # culoarea fundalului
```

---

## Forme de bază

### Pătrat

```python
import turtle
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### Triunghi echilateral

```python
for _ in range(3):
    t.forward(100)
    t.left(120)
```

### Cerc

```python
t.circle(50)   # cerc cu raza 50
```

### Poligon regulat

```python
def poligon(t, n, latura):
    unghi = 360 / n
    for _ in range(n):
        t.forward(latura)
        t.right(unghi)

poligon(t, 6, 80)   # hexagon cu latura 80
```

---

## Spirale

```python
import turtle
t = turtle.Turtle()
t.speed(0)

for i in range(200):
    t.forward(i * 2)
    t.right(91)

turtle.done()
```

---

## Steaua

```python
import turtle
t = turtle.Turtle()

t.fillcolor("gold")
t.begin_fill()
for _ in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

turtle.done()
```

---

## Proiect: Floare de culori

```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

culori = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    t.pencolor(culori[i % len(culori)])
    t.circle(80)
    t.right(10)

turtle.done()
```

---

## Proiect: Pânza de păianjen colorată

```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

culori = ["red", "yellow", "cyan", "magenta", "white"]

for i in range(200):
    t.pencolor(culori[i % 5])
    t.forward(i * 1.5)
    t.left(123)

turtle.done()
```

---

## Proiect complet: Galerie de forme

Creează un program care desenează mai multe forme la poziții diferite:

```python
import turtle

def patrat(t, x, y, latura, culoare):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(culoare)
    t.begin_fill()
    for _ in range(4):
        t.forward(latura)
        t.right(90)
    t.end_fill()

def cerc(t, x, y, raza, culoare):
    t.penup()
    t.goto(x, y - raza)
    t.pendown()
    t.fillcolor(culoare)
    t.begin_fill()
    t.circle(raza)
    t.end_fill()

ecran = turtle.Screen()
ecran.bgcolor("lightgray")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

patrat(t, -200, 50, 80, "blue")
patrat(t, -50, 50, 80, "red")
patrat(t, 100, 50, 80, "green")

cerc(t, -160, -80, 40, "yellow")
cerc(t, -10, -80, 40, "orange")
cerc(t, 140, -80, 40, "purple")

turtle.done()
```

---

## Idei de extindere

- Desenează un peisaj (soare, nori, munți, copaci)
- Creează un sistem solar animat cu planete care orbitează
- Desenează literele numelui tău
- Implementează un fractal (ex: Triunghiul lui Sierpinski)
- Creează un joc simplu cu turtle (bila care ricoșează)

---

## Rezumat al cursului

Felicitări! Ai parcurs toate lecțiile cursului de Python pentru începători:

| Lecție | Ce ai învățat |
|--------|--------------|
| 00–03 | Bazele: variabile, operații, input/output |
| 04–05 | Controlul fluxului: condiții și bucle |
| 06–07 | Colecții: liste și dicționare |
| 08 | Funcții: organizarea codului |
| 09 | Fișiere: persistența datelor |
| 10–11 | Proiecte: joc text și grafice |

**Unde mergi mai departe?**

- Încearcă să extinzi jocul de aventură cu mai multe camere
- Explorează modulele `random`, `math`, `datetime`
- Încearcă `pygame` pentru jocuri 2D cu grafică
- Explorează `matplotlib` pentru grafice de date
