# main.py
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

tim = Player()
car = CarManager()

screen.listen()
screen.onkey(key="Up", fun=tim.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
