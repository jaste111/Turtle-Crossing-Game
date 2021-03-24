import random
import time
from turtle import Screen

from Scoreboard import Scoreboard
from car import Car
from player import Player

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_NUMBER_OF_CARS = 10

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(n=0)
screen.colormode(255)

player = Player()
screen.listen()
screen.onkey(fun=player.move_up, key="Up")


def main():
    level = Scoreboard()
    cars = []
    game_is_on = True
    while game_is_on:
        if random.randint(0, 30) == 15 and len(cars) < MAX_NUMBER_OF_CARS:
            cars.append(Car())
        for car in cars:
            if player.hit_car(car):
                game_is_on = False
                break
            car.move_left()
            if car.xcor() < -300:
                car.hideturtle()
                cars.remove(car)
        screen.update()
        player.crossed_street(level=level)
        time.sleep(0.01)
    screen.exitonclick()


if __name__ == '__main__':
    main()
