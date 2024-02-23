# player file
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color("brown3")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        current_y = self.ycor()
        if current_y < 280:
            new_y = current_y + 20
            self.setposition(self.xcor(), new_y)
