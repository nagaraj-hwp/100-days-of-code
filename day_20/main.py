# Snake game project
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Epic Snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()

