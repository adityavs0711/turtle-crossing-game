from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.level = 1
        self.write_score()

    def increase_level(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Level : {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)
