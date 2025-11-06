from turtle import Turtle, Screen
tom = Turtle()
sides = 3
colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta"]

for j in range(6):
    tom.color(colors[j])
    for i in range(sides):
        tom.right(360/sides)
        tom.forward(100)
    sides += 1
screen = Screen()
screen.exitonclick()