import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)

game_is_on = True

cars = []

for car in range(20):
    newCar = CarManager()
    cars.append(newCar)

turtle = Player()
newCar = CarManager()

while game_is_on:
    newCar.move()
    cars[0].move()

    screen.update()
    screen.update()
    screen.update()

    screen.listen()
    screen.onkey(turtle.move,"Up")