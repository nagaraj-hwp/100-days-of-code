# Random walk program using python turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
colours = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "magenta", "brown", "violet", "azure",
           "bisque1", "burlywood1"]

directions = [0, 90, 180, 270]


def get_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    rgb = (red, green, blue)
    return rgb


for _ in range(200):
    tim.speed("fastest")
    # tim.color(random.choice(colours))
    tim.pencolor(get_colour())
    tim.pensize(10)
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()

