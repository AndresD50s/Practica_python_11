import turtle
import math


screen = turtle.Turtle()
screen.bgcolor("black")
screen.title("planeta con dos lunas")


planeta = turtle.Turtle()
planeta.color("blue")
planeta.pensize(50)
planeta.shape("circle")
planeta.penup()
planeta.goto(0, 0)


luna1 = turtle.Turtle()
luna1.color("gray")
luna1.shape("circle")
luna1.penup()
luna1.goto(100, 0)


luna2 = turtle.Turtle()
luna2.color("lightgray")
luna2.shape("circle")
luna2.penup()
luna2.goto(-100, 0)


angulo_luna1 = 0
angulo_luna2 = 0
velocidad_luna1 = 2
velocidad_luna2 = 4

while True:
    angulo_luna1 += velocidad_luna1
    x1 = 100 * math.cos(math.radians(angulo_luna1))
    y2 = 100 * math.sin(math.radians(angulo_luna2))
    luna1.goto(x1, y1)
    
    screen.update()

turtle.done()