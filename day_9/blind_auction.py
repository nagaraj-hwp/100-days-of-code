# Day 9 Final challenge
from art import logo
from os import system
print(logo)
print("Welcome to the blind auction!, bid more to win the auction :p")
auction_list = []
auction_continue = True

while auction_continue:
    auction_member = {}

    bidder_name = input("Enter your name: \n")
    bidder_amount = int(input(f"Hi {bidder_name}, How much you wanna bet? $\n"))
    more_bidders = input(
        "Is there any more bidders available to bet? 'Yes' or 'No' \n").lower()

    auction_member["name"] = bidder_name
    auction_member["amount"] = bidder_amount
    auction_list.append(auction_member)

    if more_bidders == "yes":
        system('cls')
        continue
    else:
        auction_continue = False


max_bid = 0
max_bidder = ""
for item in auction_list:
    if item["amount"] > max_bid:
        max_bid = item["amount"]
        max_bidder = item["name"]

print(
    f"Today the auction winner is {max_bidder} with maximum bid of ${max_bid}")
