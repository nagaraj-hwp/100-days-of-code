import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
              "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game 🏓")
screen.tracer(0)

# Enhancement code for easy hard level adjustment
# difficulty = turtle.textinput(title="Game Difficulty", prompt="Easy or hard").lower()
# paddle_color = turtle.textinput(title="Paddle color (Choose lighter one)", prompt="Enter preferred color").lower()
#
# if difficulty == "easy":
#     width = 8
#     ball_paddle_dist = 70
# else:
#     width = 5
#     ball_paddle_dist = 50
#
# if paddle_color not in color_list:
#     color = "white"
# else:
#     color = paddle_color
#

# r_paddle = Paddle(paddle_color=color, paddle_width=width, position=(380, 0))
# l_paddle = Paddle(paddle_color=color, paddle_width=width, position=(-380, 0))
r_paddle = Paddle(position=(380, 0))
l_paddle = Paddle(position=(-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect ball miss from paddle right
    if ball.xcor() > 390:
        ball.reset_ball()
        ball.bounce_x()
        scoreboard.l_point()

    # Detect ball miss from paddle right
    if ball.xcor() < -390:
        ball.reset_ball()
        ball.bounce_y()
        scoreboard.r_point()


screen.exitonclick()
