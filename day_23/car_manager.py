# car managing for the Turtle racing
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color(random.choice(COLORS))

    def move_car(self):
        pass
