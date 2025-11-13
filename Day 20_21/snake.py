from turtle import  Turtle

class Snake:
    def __init__(self):
        self.x_axis = 20
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for s in range(3):
            self.x_axis -= 20
            self.add_segment(self.x_axis, 0)

    def add_segment(self, x_axis, y_axis):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(x_axis, y_axis)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].xcor(), self.snake[-1].ycor())

    def reset(self):
        for s in self.snake:
            s.goto (100,100)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
