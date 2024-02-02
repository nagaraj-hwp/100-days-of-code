# This is a simple rock paper scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_images = [rock, paper, scissors]

user_choice = int(input(
    "What do you wanna Choose? Rock, paper or scissors Enter \n1 for Rock\n2 for Paper\n3 for scissors\n"))
computer = random.randint(0, 2)
if user_choice < 0 and user_choice > 2:
    print("Wrong choice, you lose")
    # exit()
else:
    print()
    print(f"You chose\n{game_images[user_choice]}\nComputer Chose\n {game_images[computer]}")
    # if user_choice == 0:
    #     print("You chose Rock\n")
    #     print(rock)
    # elif user_choice == 1:
    #     print("You chose Paper\n")
    #     print(paper)
    # elif user_choice == 2:
    #     print("You chose Scissors\n")
    #     print(scissors)
    # else:
    #     print("Wrong Choice, you lose")
    #     exit()

    # if computer == 0:
    #     print("Computer chose Rock\n")
    #     print(rock)
    # elif computer == 1:
    #     print("Computer chose Paper\n")
    #     print(paper)
    # elif computer == 2:
    #     print("Computer chose Scissors\n")
    #     print(scissors)

    if (user_choice == computer):
        print("\nThe game is draw")
    elif (user_choice == 0 and computer == 1) or (user_choice == 2 and computer == 0) or (user_choice == 1 and computer == 2):
        print("\nYou lose!")
    elif (user_choice == 0 and computer == 2) or (user_choice == 1 and computer == 0) or (user_choice == 2 and computer == 1):
        print("\n You won !!!!\n\n")
