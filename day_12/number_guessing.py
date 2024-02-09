from art import logo, win
import random
from os import system


def choose_diffculty():
    difficulty_level = input(
        "Choose Difficulty level. Type 'Easy' or 'Hard':  ").lower()
    if difficulty_level == "hard":
        attempts = 5
    else:
        attempts = 10
    print("You will be having {attempts} to guess the number.\n")
    return attempts


def guess_number(attempts, number):
    while attempts > 0:
        print(f"You still have {attempts} attempts left to guess this number.")
        predict = int(input("Make a guess.\n"))
        if predict > number:
            print("Too High.\nGuess Again.")
        elif predict < number:
            print("Too Low.\nGuess Again.")
        else:
            print(win)
            print(f"You guessed it right!!!, the number is {number}.\n")
            return
        attempts -= 1
    if attempts == 0:
        print(f"You ran out of attempts to guess, the number is {number}.\n")


def play_game():
    game_done = False
    while not game_done:
        system('cls')
        print(logo)
        print("Welcome to the number guessing game! Be Sharp.\n")
        number = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100.\n")
        attempts = choose_diffculty()
        guess_number(attempts=attempts, number=number)
        another_game = input(
            "Play another game? Type 'y' for Yes or 'n' for No.\n").lower()
        if another_game != "y":
            print("Good luck with your daily chores!!\n")
            game_done = True


play_game()
