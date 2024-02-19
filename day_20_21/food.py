# Food class methods and attributes
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_pos = random.randint(-280, 280)
        random_y_pos = random.randint(-280, 280)
        self.goto(x=random_x_pos, y=random_y_pos)

