# import colorgram
#
# # Extract some colors from an image.
# colors = colorgram.extract("image.jpg", 50)
# rgb_colors = []
# print(colors)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.goto(-300, -300)
tim.hideturtle()
# tim.setheading(225)
# tim.forward(320)
# tim.setheading(0)
number_of_dots = 100
divide_count = number_of_dots // 10

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % divide_count == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(number_of_dots * 5)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

