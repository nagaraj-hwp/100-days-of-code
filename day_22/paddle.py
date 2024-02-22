# paddle control file for pong game
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position, paddle_color="white", paddle_width=7):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(paddle_color)
        self.shapesize(stretch_wid=paddle_width, stretch_len=1)
        self.goto(position)

    def go_up(self):
        current_y = self.ycor()
        if current_y < 250:
            new_y = current_y + 20
            self.setposition(self.xcor(), new_y)

    def go_down(self):
        current_y = self.ycor()
        if current_y > -250:
            new_y = current_y - 20
            self.setposition(self.xcor(), new_y)
