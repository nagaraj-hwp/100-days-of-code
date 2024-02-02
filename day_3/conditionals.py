# Conditional statements
# simple if
# if condition:
#     do this
# else:
#     do this

# check height for rollercoaster ride

# print("Welcome to the rollercoaster ride!")
# height = int(input("What is your height in centimeter? "))

# if height > 120:
#     print("Enjoy your ride!")
# else:
#     print("You are too young for this ride!")

# # Odd or Even number check Which number do you want to check?
# number = int(input())

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Conditional statements
# Nested if

# if condition:
#    if another condition:
#       do This
#    else:
#       do this
# else:
#     do this

# ##########elif condition
# if condition1:
#    do This
# elif:
#     do this
# else:
#    do this
# check height for rollercoaster ride

# print("Welcome to the rollercoaster ride!")
# height = int(input("What is your height in centimeter? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#        print("Ride ride will cost $7.")
#     elif age <= 18:
#        print("Ride will cost $5.")
#     else:
#        print("Ride will cost $12.")
#     print("Enjoy your ride!")
# else:
#     print("You are too young for this ride!")


# BMI calculator 2.0
# Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# bmi = weight / (height * height)
# bmi_as_str = format(bmi, ".5f")
# print(bmi)
# print(bmi_as_str)
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.
# print(type(bmi))
# print(type(18.5))
# if bmi < 18.5:
#   print(f"Your BMI is {bmi_as_str}, you are underweight.")
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your BMI is {bmi_as_str}, you have a normal weight.")
# elif bmi >= 25 and bmi < 30:
#     print(f"Your BMI is {bmi_as_str}, you are slightly overweight.")
# elif bmi >= 30 and bmi < 35:
#     print(f"Your BMI is {bmi_as_str}, you are obese.")
# elif bmi >= 35:
#   print(f"Your BMI is {bmi_as_str}, you are clinically obese.")


# leap Year calculation

# Which year do you want to check?
# year = int(input())

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# else:
#     print("Not leap year")


# multiple if statements

# print("Welcome to the rollercoaster ride!")
# height = int(input("What is your height in centimeter? "))
# fare = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#        fare = 5
#        print(f"Ride ride will cost ${fare}.")
#     elif age <= 18:
#        fare = 7
#        print(f"Ride will cost ${fare}.")
#     else:
#        fare = 12
#        print(f"Ride will cost ${fare}.")
#     print("Enjoy your ride!")
#     wants_photo = input("Do you want your photo taken during ride Y or N ")
#     if wants_photo == "Y":
#        fare += 3
#     print(f"Your total fare will be ${fare}")
# else:
#     print("You are too young for this ride!")


# pizza order challenge
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N

# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill +=20
# elif size == "L":
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
# if extra_cheese == "Y":
#   bill+= 1

# print(f"Your final bill is: ${bill}.")
