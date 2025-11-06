from turtle import Turtle, Screen
tim = Turtle()

def backwards():
    tim.backward(10)

def forwards():
    tim.forward(10)

def clockwise():
    tim.right(10)

def counter_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()

screen.onkey(forwards, 'w')
screen.onkey(backwards, 's')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clockwise, 'd')
screen.onkey(clear, 'c')

screen.listen()
screen.exitonclick()

