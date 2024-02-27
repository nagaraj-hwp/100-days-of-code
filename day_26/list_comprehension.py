# understanding and learning list comprehension using python

# numbers = [i for i in range(0, 5)]
#
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# new_numbers = [i+1 for i in numbers]
# print(new_numbers)

# name = "NAGARAJ"
# new_list = [letter for letter in name]
# print(new_list)

# num = [n*2 for n in range(1, 5)]
# print(num)

names = ["Nagaraj", "Ashok", "Santhanam", "Rishi", "Mani", "Rajalingam", "Ponmuthu", "Ajith"]
short_names = [name for name in names if len(name) < 8]
print(short_names)
capital_big_names = [name.upper() for name in names if len(name) >= 8]
print(capital_big_names)


# Interactive coding exercise LESSON 28 DAY 26 - SQUARING NUMBERS
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)


# Interactive coding exercise LESSON 29 DAY 26 - FILTERING EVEN NUMBERS
list_of_strings = input().split(',')
# sample input 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
result = [int(num.strip()) for num in list_of_strings if int(num) % 2 == 0]
print(result)
