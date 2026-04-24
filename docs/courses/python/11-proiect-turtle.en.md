---
lesson: 11
tags: [python, turtle, graphics, drawing, animation]
summary: Final project — draw geometric shapes and spirals with the turtle module.
---

# Lesson 11 · Project: Turtle Graphics

!!! tip "What you'll practice"
    - The `turtle` module for vector graphics
    - `for` loops to draw repeating shapes
    - Functions for reusable shapes
    - Creativity — making your own art with code

---

## What is the `turtle` module?

`turtle` is a Python module that simulates a "turtle" drawing on the screen. You control it with simple commands: `forward()`, `left()`, `right()`. It comes installed with Python by default.

```python
import turtle

t = turtle.Turtle()   # create the turtle
t.forward(100)        # move 100 pixels forward
t.left(90)            # turn 90° left
t.forward(100)        # move 100 pixels forward

turtle.done()         # keep the window open
```

---

## Main commands

### Movement

```python
t.forward(n)    # move n pixels forward
t.backward(n)   # move n pixels backward
t.right(deg)    # turn right
t.left(deg)     # turn left
t.goto(x, y)    # jump to coordinates (x, y)
t.home()        # return to the origin (0, 0)
```

### Pen control

```python
t.penup()               # lift the pen (no drawing while moving)
t.pendown()             # put the pen down (draws)
t.pensize(3)            # line thickness
t.pencolor("red")       # line color
t.fillcolor("yellow")   # fill color
t.begin_fill()          # start filling
t.end_fill()            # stop filling
```

### Speed and appearance

```python
t.speed(0)              # 0 = max, 1 = slow, 10 = fast
t.hideturtle()          # hide the turtle (cleaner image)
turtle.bgcolor("black") # background color
```

---

## Basic shapes

### Square

```python
import turtle
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### Equilateral triangle

```python
for _ in range(3):
    t.forward(100)
    t.left(120)
```

### Circle

```python
t.circle(50)   # circle with radius 50
```

### Regular polygon

```python
def polygon(t, n, side):
    angle = 360 / n
    for _ in range(n):
        t.forward(side)
        t.right(angle)

polygon(t, 6, 80)   # hexagon with side 80
```

---

## Spirals

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

## Star

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

## Project: Colorful flower

```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.circle(80)
    t.right(10)

turtle.done()
```

---

## Project: Colorful spider web

```python
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

colors = ["red", "yellow", "cyan", "magenta", "white"]

for i in range(200):
    t.pencolor(colors[i % 5])
    t.forward(i * 1.5)
    t.left(123)

turtle.done()
```

---

## Complete project: Shape gallery

Build a program that draws several shapes at different positions:

```python
import turtle

def square(t, x, y, side, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()

def circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

screen = turtle.Screen()
screen.bgcolor("lightgray")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

square(t, -200, 50, 80, "blue")
square(t, -50, 50, 80, "red")
square(t, 100, 50, 80, "green")

circle(t, -160, -80, 40, "yellow")
circle(t, -10, -80, 40, "orange")
circle(t, 140, -80, 40, "purple")

turtle.done()
```

---

## Ideas for extending the project

- Draw a landscape (sun, clouds, mountains, trees)
- Build an animated solar system with orbiting planets
- Draw the letters of your name
- Implement a fractal (e.g., Sierpinski triangle)
- Create a simple game with turtle (a bouncing ball)

---

## Course summary

Congratulations! You've completed all the lessons of the Python course for beginners:

| Lesson | What you learned |
|--------|------------------|
| 00–03 | Basics: variables, operations, input/output |
| 04–05 | Flow control: conditions and loops |
| 06–07 | Collections: lists and dictionaries |
| 08 | Functions: organizing code |
| 09 | Files: data persistence |
| 10–11 | Projects: text game and graphics |

**Where to go next?**

- Try extending the adventure game with more rooms
- Explore the `random`, `math`, `datetime` modules
- Try `pygame` for 2D games with graphics
- Explore `matplotlib` for data charts
