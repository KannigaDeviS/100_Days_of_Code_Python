import random
from turtle import Turtle, Screen
from random import Random
colors = ['red', 'blue', 'yellow', 'orange', 'green', 'pink']
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = 'What is your bet?', prompt = 'Which turtle will win')
print(user_bet)
turtles = []
index_y = 100
is_race_on = False

for r in range(6):
    tim = Turtle(shape='turtle')
    tim.color(colors[r])
    tim.penup()
    tim.goto(x=-240, y=index_y)
    index_y -= 40
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        t.forward(random.randint(0,10))
        if t.xcor() > 225:
            is_race_on = False
            winning_turtle = t.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won! {winning_turtle} turtle won the race")
            else:
                print(f"You've lost! {winning_turtle} turtle won the race")

screen.exitonclick()
