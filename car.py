import random
from turtle import Turtle

STEP_SIZE = 1


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(x=320, y=random.randint(-300, 300))
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        self.color(r, b, g)

    def move_left(self) -> None:
        self.goto(x=self.xcor() - STEP_SIZE, y=self.ycor())
