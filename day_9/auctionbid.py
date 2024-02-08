# Day 9 Final challenge
from art import logo
from os import system
print(logo)
print("Welcome to the blind auction!, bid more to win the auction :p")
auction_completed = False
bids = {}


def find_highest_bidder(bidding_record):
    max_bid = 0
    max_bidder = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > max_bid:
            max_bid = bidding_record[bidder]
            max_bidder = bidder
    print(
        f"Today's auction winner is {max_bidder} with maximum bid of ${max_bid}")


while not auction_completed:
    bidder_name = input("Enter your name: \n")
    bidder_amount = int(
        input(f"Hi {bidder_name}, How much you wanna bet? $\n"))
    bids[bidder_name] = bidder_amount
    more_bidders = input(
        "Is there any more bidders available to bet? 'Yes' or 'No' \n").lower()

    if more_bidders == "no":
        auction_completed = True
        find_highest_bidder(bidding_record=bids)
    else:
        system('cls')
