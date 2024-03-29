# This is a project for hangman using
# while loop
# for loop
# range function
# if else
# lists, etc
# random module

import random
from hangman_Art import logo, stages
from hangman_words import word_list
from os import system

system('cls')
print(logo)
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
display = ["_" for i in range(word_length)]

end_of_game = False
lives = 6

while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in display:
        print(
            f"You guessed letter {guessed_letter}, You already guessed this letter! you lost a life.\n")
        continue
    correct_guess = False
    for i in range(0, word_length):
        if chosen_word[i] == guessed_letter:
            display[i] = guessed_letter
            correct_guess = True
    if not correct_guess:
        print(
            f"You guessed letter {guessed_letter}, letter not in the word! you lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lost! \nThe chosen word was {chosen_word}.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win.")

    print(stages[lives])
