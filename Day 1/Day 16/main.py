from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')

myScreen = Screen()
print(myScreen.canvheight)
timmy.forward(100)
myScreen.exitonclick()

