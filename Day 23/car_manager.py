import random
from turtle import Turtle
from random import Random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.increment = 0

    def create_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(1,2)
        new_car.speed('fastest')
        new_car.color(random.choice(COLORS))
        new_car.goto(250, random.randint(-250, 250))
        self.cars.append(new_car)

    def move_left(self):
        for c in self.cars:
            new_xaxis = c.xcor() - (STARTING_MOVE_DISTANCE + (self.increment * MOVE_INCREMENT))
            new_yaxis = c.ycor()
            c.goto(new_xaxis, new_yaxis)


    def collide(self, player):
        for c in self.cars:
            if c.distance(player) < 20:
                return True

        return False

    def update_increment(self):
        self.increment += 1




