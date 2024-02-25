# main.py
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=tim.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()

    # DETECT WHEN TURTLE REACHES OTHER SIDE OF THE ROAD
    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

# Just a small comment added

