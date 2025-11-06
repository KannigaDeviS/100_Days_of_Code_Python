import random
import turtle as t
from turtle import Screen
tim = t.Turtle()
tim.shape('circle')
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color
tim.speed('fastest')
for r in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)

screen = Screen()
screen.exitonclick()

