# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(170)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
# screen = Screen()
# screen.exitonclick()


from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
for _ in range(5):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()

