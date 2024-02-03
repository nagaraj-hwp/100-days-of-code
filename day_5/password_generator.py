# Password Generator project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # easy method
# random_letters = random.sample(letters, nr_letters)
# random_numbers = random.sample(numbers, nr_numbers)
# random_symbols = random.sample(symbols, nr_symbols)

# print(random_letters)
# print(random_numbers)
# print(random_symbols)

# # password = str(random_letters) + str(random_symbols) + str(random_numbers)
# password= ""
# for i in random_letters:
#     password+=i
# for i in random_numbers:
#     password+=i
# for i in random_symbols:
#     password+=i

# print(password)

# Easy level 2
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
# print(password)

# Hard level
password_list = []
password = ""
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
# print(password_list)

random.shuffle(password_list)
for char in password_list:
    password += char

print("Your password is:", password)
