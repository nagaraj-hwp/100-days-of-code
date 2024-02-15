# drawing different shapes with turtle
from turtle import Turtle, Screen
from random import choice
tim = Turtle()

tim.color("red")
# for i in range(3):
#     tim.forward(100)
#     tim.right(120)
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
# for i in range(5):
#     tim.forward(100)
#     tim.right(72)
# for i in range(6):
#     tim.forward(100)
#     tim.right(60)
# for i in range(7):
#     tim.forward(100)
#     tim.right(51.42)
# for i in range(8):
#     tim.forward(100)
#     tim.right(45)
# for i in range(9):
#     tim.forward(100)
#     tim.right(40)
# for i in range(10):
#     tim.forward(100)
#     tim.right(36)

colours = ["steel blue", "dark red", "magenta", "yellow", "green", "cyan", "brown"]


def draw_shapes(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for shape_n in range(3, 11):
    tim.color(choice(colours))
    tim.speed(0.001)
    draw_shapes(shape_n)


screen = Screen()
screen.exitonclick()
