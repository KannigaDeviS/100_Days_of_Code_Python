from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as highscore:
            self.highscore = int(highscore.read())
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        with open("data.txt", mode="w") as highscore:
            highscore.write(str(self.highscore))


    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, align="center", font=('Arial', 24, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over.', False, align="center", font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
