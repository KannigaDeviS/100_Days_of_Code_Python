from turtle import Screen, Turtle
import time

class Snake:
    def __init__(self):
        self.x_axis = 20
        self.snake = []
        for s in range(3):
            segment = Turtle(shape='square')
            segment.width(20)
            segment.color('white')
            self.x_axis -= 20
            segment.penup()
            segment.goto(self.x_axis, 0)
            self.snake.append(segment)
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

