# Snake game project
from turtle import Screen
import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_level = t.textinput("Choose Game Level", "easy or hard").lower()
# print(game_level)

if game_level == "easy":
    time_interval = 0.25
    screen_width = 800
    screen_height = 800
    screen_min_distance = -380
    screen_max_distance = 380
else:
    time_interval = 0.1
    screen_width = 600
    screen_height = 600
    screen_min_distance = -380
    screen_max_distance = 380

walls_enabled = t.textinput("Walls around (Your snake may lost without walls)", "Yes for walls or no").lower()
# print(walls_enabled)

if walls_enabled == "no":
    walls = False
else:
    walls = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=screen_width, height=screen_height)
screen.title("Epic Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(time_interval)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if (snake.head.xcor() > screen_max_distance or snake.head.xcor() < screen_min_distance or snake.head.ycor() > screen_max_distance or snake.head.ycor() < screen_min_distance) and walls:
        scoreboard.reset()
        snake.reset()
    elif not walls:
        pass

    # Detect collision with the snakes tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

