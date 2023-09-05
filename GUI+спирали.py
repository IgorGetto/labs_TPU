import tkinter as tk
import random
import math
from random import randint, random, choice
import time
import turtle
from turtle import Turtle, Screen
from math import pi, sin, cos
from scipy import integrate

window = tk.Tk()
window.geometry("300x300")
window.title("Спирали")

RADIUS = 180
screen = Screen()
WIDTH, HEIGHT = screen.window_width(), screen.window_height()
turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.up()




def draw_spiral():
    x = WIDTH//2 - RADIUS
    y = RADIUS - HEIGHT//2
    turtle.up()
    turtle.goto(x, y)

    turtle.color(random(), random(), random())
    turtle.down()

    for i in range(200):
        t = i / 20 * pi
        dx = (1 + 5 * t) * cos(t)
        dy = (1 + 5 * t) * sin(t)

        turtle.goto(x + dx, y + dy)

    turtle.up()
    screen.exitonclick()

def drawLogarithmicSpiral():
    x = -200
    y = 150
    a = 0.3
    b = 0.3

    turtle.up()
    turtle.goto(x, y)
    turtle.color(random(), random(), random())
    turtle.down()

    for i in range(0, 1200, 10):
        # Draw a spiral
        t = math.radians(i)
        dx = a*math.exp(b*t)*math.cos(t)
        dy = a*math.exp(b*t)*math.sin(t)
        turtle.goto(x + dx, y + dy)

    turtle.up()
    screen.exitonclick()


def draw_spiral_parabolic():
    x = -200
    y = -150
    a = 300
    turtle.up()
    turtle.goto(x, y)
    turtle.color(random(), random(), random())
    turtle.down()

    for i in range(1, 200):
        t = i / 20 * pi
        dx = (a * cos(t)) / t
        dy = (a * sin(t)) / t
        if i == 1:
            turtle.up()
        else:
            turtle.down()
        turtle.goto(x + dx, y + dy)

    turtle.up()
    screen.exitonclick()


def Cornu():
    x = -200
    y = 150

    turtle.up()
    turtle.goto(x, y)
    turtle.color(random(), random(), random())
    turtle.down()

    for i in range(0, 1200, 10):
        # Draw a spiral
        # t = math.radians(i)
        t = i / 20 * pi

        f = lambda x: math.cos(x*x)
        f1 = lambda x: math.sin(x*x)

        (dx, err) = integrate.quad(f, 0, t)
        (dy, err) = integrate.quad(f1, 0, t)
        turtle.goto(x + dx, y + dy)
    turtle.up()
    screen.exitonclick()


button1 = tk.Button(window, width=37, text="Нарисовать архимедову спираль", command=draw_spiral)
button1.place(x=10, y=20)

button2 = tk.Button(window, width=37, text="Нарисовать логарифмическую спираль", command=drawLogarithmicSpiral)
button2.place(x=10, y=50)

button3 = tk.Button(window, width=37, text="Нарисовать параболическую спираль", command=draw_spiral_parabolic)
button3.place(x=10, y=80)

# button4 = tk.Button(window, width=37, text="Нарисовать спираль Корню", command=Cornu)
# button4.place(x=10, y=110)

window.mainloop()

