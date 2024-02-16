# Drawing a spirograph using python turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def get_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(get_colour())
        tim.circle(300)
        tim.setheading(tim.heading() + gap_size) 


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()

