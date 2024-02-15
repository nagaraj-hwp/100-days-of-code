# drawing different shapes with turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.color("red")
for i in range(3):
    tim.forward(100)
    tim.right(120)
for i in range(4):
    tim.forward(100)
    tim.right(90)
for i in range(5):
    tim.forward(100)
    tim.right(72)
for i in range(6):
    tim.forward(100)
    tim.right(60)
for i in range(7):
    tim.forward(100)
    tim.right(51.42)
for i in range(8):
    tim.forward(100)
    tim.right(45)
for i in range(9):
    tim.forward(100)
    tim.right(40)
for i in range(10):
    tim.forward(100)
    tim.right(36)

screen = Screen()
screen.exitonclick()
