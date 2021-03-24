from turtle import Turtle

FONT = ("Arial", 20, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.level = 0
        self.increase_level()

    def increase_level(self) -> None:
        self.level += 1
        self.clear()
        self.write(self.level, font=FONT, align=ALIGNMENT)
