# Creating Higher lower game using Python

from art import logo, versus2
from game_data import data
import random
from os import system

game_over = False
repetition = []
user_points = 0
system('cls')
print(logo)
print("Welcome to higher lower!\nLet's examine your intelligence and prediction skills together!!!")
defend = random.choice(data)
# print(defend)
repetition.append(defend)


# def pick_data():
#     defend = random.choice(data)
#     print(defend)
#     repetition.append(defend)
#     opponent = random.choice(data)
#     print(opponent)
#     while opponent != defend and opponent not in repetition:
#         repetition.append(opponent)
#         break
#     return defend, opponent


while not game_over:
    # defend, opponent = pick_data()
    check = True
    while check:
        opponent = random.choice(data)
        # print(opponent)
        if opponent not in repetition:
            repetition.append(opponent)
            check = False
    # print(f"\nPrinting repetion here , {repetition}\n")
    # system('cls')
    # print(logo)
    print("*******************************************************************************************")
    print(
        f"Compare A: {defend['name']}, a {defend['description']}, from {defend['country']}")
    print("*******************************************************************************************")
    print(versus2)
    print("*******************************************************************************************")
    print(
        f"Compare B: {opponent['name']}, a {opponent['description']}, from {opponent['country']}")
    print("*******************************************************************************************")

    user_choice = input(
        "Enter Who has more follower count Type either 'A' or 'B'\n").lower()
    # print(user_choice)
    system('cls')
    print(logo)
    if user_choice != 'a' and user_choice != 'b':
        print(
            "You predicted something from out of syllabus! Haha\nRestart your game ;[")
        exit()
    if (user_choice == 'a' and defend['follower_count'] > opponent['follower_count']):
        print(".................................................................................")
        print(
            f"You guessed right, {defend['name']} has {defend['follower_count']} million followers and  {opponent['name']} has {opponent['follower_count']} million followers!")
        user_points += 1
        print(f"You scored {user_points} points, keep going")
        print(".................................................................................\n")

    elif (user_choice == 'b' and defend['follower_count'] < opponent['follower_count']):
        print(
            f"You guessed right, {defend['name']} has {defend['follower_count']} million followers and {opponent['name']} has {opponent['follower_count']} million followers!")
        user_points += 1
        print("........................................")
        print(f"You scored {user_points} points, keep going!")
        print("........................................\n")
        defend = opponent
    else:
        print(
            f"You guessed wrong, {defend['name']} has {defend['follower_count']} million followers and {opponent['name']} has {opponent['follower_count']} million followers!")
        print("\n\n\n---------------------------------------------------")
        print(
            f"| You scored {user_points} points in this higher lower game! |")
        print("---------------------------------------------------\n\n\n")
        game_over = True
