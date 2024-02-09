# Wrting code for black jack project
import random
from art import logo

print(logo)

print("Welcome to Black Jack, its going to be a good game!\n\n")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
game_finished = False


def add_player_card():
    player_cards.append(random.choice(cards))


def add_dealer_card():
    dealer_cards.append(random.choice(cards))


def pre_cards():
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))


def check_push():
    # return True if sum(player_cards) == sum(dealer_cards) else False
    if sum(player_cards) == sum(dealer_cards):
        print("Its a Push, 'DRAW'\n")


while not game_finished:
    pre_cards()
    print(
        f"You got the initial cards as {player_cards} amounts to {sum(player_cards)}")
    print(
        f"Dealer's first card is {dealer_cards} amounts to {sum(dealer_cards)}")
    while sum(player_cards) < 21:
        hit_or_stand = input(
            "Whether you wanna hit or stand? type 'H' for hit or 'S' for stand\n").lower()
        if hit_or_stand == 'h':
            add_player_card()
            print(
                f"You cards are {player_cards} amounts to {sum(player_cards)}")
            print(
                f"Dealer's cards are {dealer_cards} amounts to {sum(dealer_cards)}")
            # check_push()
            if sum(player_cards) > 21 and sum(dealer_cards) <= 21:
                print("You lose!")
                game_finished = True
            elif sum(player_cards) == 21 and sum(dealer_cards) != 21:
                print("You Win!")
                game_finished = True
        elif hit_or_stand == 's':
            add_dealer_card()
            print(
                f"You cards are {player_cards} amounts to {sum(player_cards)}")
            print(
                f"Dealer's cards are {dealer_cards} amounts to {sum(dealer_cards)}")
            if (sum(player_cards) < 21 and sum(dealer_cards) < 21 and 21 - sum(player_cards) < 21 - sum(dealer_cards)) or (sum(player_cards) <= 21 and sum(dealer_cards) > 21):
                print("You win!")
                game_finished = True
                break
            elif (sum(player_cards) < 21 and sum(dealer_cards) < 21 and 21 - sum(player_cards) > 21 - sum(dealer_cards)) or (sum(player_cards) > 21 and sum(dealer_cards) <= 21):
                print("You Lose")
                game_finished = True
                break
