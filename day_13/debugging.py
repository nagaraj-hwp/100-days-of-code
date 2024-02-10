# Learning to Debug the code in python

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   # for i in range(1, 20):
#   for i in range(1, 20+1):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# dice_num = randint(0, 5)
print(dice_num)
print(dice_imgs[dice_num])


