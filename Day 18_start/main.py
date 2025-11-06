from turtle import Turtle, Screen
tim = Turtle()
tim.shape("circle")
tim.color("CornFlowerBlue")

for i in range(4):
    tim.forward(100)
    tim.right(90)


screen = Screen()
screen.exitonclick()
