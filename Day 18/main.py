import random
import turtle as t
import colorgram
from turtle import Screen
from random import Random
def draw_row(tut, colors_list):
    for r in range(10):
        tut.dot(20,random.choices(colors_list)[0])
        if r != 9:
            tut.penup()
            tut.forward(50)

def change_direction(tut):
    if tut.heading() == 0.0 or tut.heading == 270.0:
        tut.left(90)
        tut.forward(50)
        tut.left(90)
    else:
        tut.right(90)
        tut.forward(50)
        tut.right(90)

tim = t.Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.width(10)
t.colormode(255)
tim.hideturtle()
colors = colorgram.extract('spotpainting.jpg', 35)
colors_list = []
for c in colors:
    colors_list.append((c.rgb.r, c.rgb.g, c.rgb.b))

tim.home()
for r in range(10):
    draw_row(tim,colors_list)
    if r != 9:
        change_direction(tim)

screen = Screen()
screen.screensize(2500,2500)
screen.exitonclick()