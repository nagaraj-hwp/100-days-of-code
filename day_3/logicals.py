# # Logical operators on Python

# # combined mid life category
# print("Welcome to the rollercoaster ride!")
# height = int(input("What is your height in centimeter? "))
# fare = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         fare = 5
#         print(f"Ride ride will cost ${fare}.")
#     elif age <= 18:
#         fare = 7
#         print(f"Ride will cost ${fare}.")
#     elif age >= 45 and age <= 55:
#         fare = 0
#         print(f"Enjoy your free ride your ride will cost ${fare}. Yay!")
#     else:
#         fare = 12
#         print(f"Ride will cost ${fare}.")
#     print("Enjoy your ride!")
#     wants_photo = input("Do you want your photo taken during ride Y or N ")
#     if wants_photo == "Y":
#         fare += 3
#     print(f"Your total fare will be ${fare}")
# else:
#     print("You are too young for this ride!")


# Lova calculator Haha
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

total = str(first_digit) + str(second_digit)
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
