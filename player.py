from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("turtle")
        self.goto(0,-240)
        self.setheading(90)


    def move(self):
        self.forward(10)