# # understanding Datatypes

# # string

# m = 123_123
# n = 12

# print(m+n)

# # typecasting

# name = input("Enter your age: ")
# name_char_len = len(name)
# print(type(name))
# name_char_len_str = str(name_char_len)
# print("Your name has " + name_char_len_str + " letters.")

# ###############
# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input()
# ####################################
# print(int(two_digit_number[0]) + int(two_digit_number[1]))


# # BMI calculation

# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()

# weight_int = int(weight)
# height_int = float(height)
# bmi = (weight_int / (height_int * height_int))

# print(int(bmi))
##########################################################################################
# Day 2 Final project

print("Welcome to the tip Calculator!")
total_bill = float(input("what was the total bill? $"))
tip_percent = float(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_persons = int(input("How many people to split the bill? "))
total_pay = total_bill + (total_bill * (tip_percent/100))
pay_per_person = round(total_pay / number_of_persons, 2)
pay_per_person = "{:.2f}".format(pay_per_person)
# pay_per_person = round((total_bill / number_of_persons) * (1 + tip_percent/100), 2)
print(f"Each person should pay ${pay_per_person}")
print()
print()
