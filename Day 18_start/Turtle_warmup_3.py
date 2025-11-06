import random
import turtle as t

from random import Random
tim = t.Turtle()
tim.width(10)
tim.shape('circle')
tim.speed('fastest')
action = ['forward','backward','left','right']
#colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta"]
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color
for _ in range(500):
    tim.color(random_color())
    random_action = random.choice(action)
    if random_action == 'forward':
        tim.forward(20)
    elif random_action == 'backward':
        tim.backward(20)
    elif random_action == 'left':
        tim.left(90)
    else:
        tim.right(90)