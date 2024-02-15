# Random walk program using python turtle

from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "magenta", "brown", "violet", "azure",
           "bisque1", "burlywood1"]

directions = [0, 90, 180, 270]

for _ in range(100):
    tim.speed("fastest")
    tim.color(random.choice(colours))
    tim.pensize(10)
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
