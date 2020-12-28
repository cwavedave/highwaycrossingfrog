from turtle import Turtle


class Background(Turtle):
    def __init__(self):
        super().__init__()
        background = Turtle()
        background.shapesize(stretch_wid=25, stretch_len=50)
        background.shape("square")
        background.color("grey")

