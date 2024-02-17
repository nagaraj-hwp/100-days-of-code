import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    # tim.left(10)
    current_direction = tim.heading()
    tim.setheading(current_direction + 10)


def turn_right():
    # tim.right(10)
    current_direction = tim.heading()
    tim.setheading(current_direction - 10)


def clear_screen():
    # screen.clear()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
