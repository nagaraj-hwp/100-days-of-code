# Snake game project
from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Epic Snake game")
screen.tracer(0)

initial_turtles = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in initial_turtles:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# segment_1 = Turtle("Square")
# segment_1.color("white")
#
# segment_2 = Turtle("Square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("Square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()

