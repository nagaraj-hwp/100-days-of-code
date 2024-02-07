# Understanding function with inputs

# Function with no inputs
def greet():
    print("Hi, Hello")
    print("This function greets everyone in general!")

# Function with one input


def greet_with_name(name="Ladies and Gentlemen"):
    print(f"Hi {name}")
    print(f"Hope you are doing well {name}")

# Function with more than one input


def greet_with_name_and_location(name, location):
    print(f"Hi {name}")
    print(f"How is the weather in {location}?")

# function with keyword arguments


def greet_with_positions(name, location):
    print(f"Hi {name}")
    print(f"How is the weather in {location}?")

# greet_with_positions(location="Madurai", name="Nagaraj P")

# LESSON 20 DAY 8 - PAINT AREA CALCULATOR
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# def paint_calc(height, width, cover):
#   total_cans = round((height * width) / coverage)
#   print(f"You'll need {total_cans} cans of paint.")

# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# LESSON 21 DAY 8 - PRIME NUMBERS
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            prime = False
            break
    if prime:
        print("It's a prime number.")
