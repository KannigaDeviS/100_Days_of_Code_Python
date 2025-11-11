from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.goto(-280,260)
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.write(f'Level: {self.level}', move=False, align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over.', False, align="center", font=('Arial', 24, 'normal'))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()
