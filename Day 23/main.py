import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car = CarManager()
screen = Screen()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up,'Up')

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter % 6 == 0:
        car.create_car()
    counter += 1

    car.move_left()

    # detect collision with any car
    if car.collide(player):
        game_is_on = False
        scoreboard.game_over()

    # player reached finish line
    if player.reached_finishline():
        car.update_increment()
        player.restart()
        scoreboard.increase_level()
        scoreboard.update_level()

screen.exitonclick()
