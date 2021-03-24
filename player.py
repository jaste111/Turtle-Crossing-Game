from turtle import Turtle

import Scoreboard
import car
from car import Car

START_X = 0
START_Y = -280
STEP_SIZE = 20


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=START_X, y=START_Y)

    def move_up(self) -> None:
        self.goto(x=self.xcor(), y=self.ycor() + STEP_SIZE)

    def hit_car(self, current_car: Car) -> bool:
        return self.distance(current_car) < 25

    def crossed_street(self, level: Scoreboard) -> None:
        if self.ycor() > 300:
            level.increase_level()
            self.goto(x=START_X, y=START_Y)
            car.STEP_SIZE += 1
