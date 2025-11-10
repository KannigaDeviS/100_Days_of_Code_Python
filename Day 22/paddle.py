from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, X_COR):
        super().__init__()
        self.XCOR = X_COR
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(5,1)
        self.goto(X_COR,0)

    def move_up(self):
        y_axis = self.ycor() + 20
        print(y_axis)
        self.goto(self.XCOR, y_axis)

    def move_down(self):
        y_axis = self.ycor() - 20
        print(y_axis)
        self.goto(self.XCOR, y_axis)