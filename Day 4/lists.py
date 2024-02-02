# understanding lists
a = []
b = [1, 2, 3]
c = ['a', 'b', 'c']
d = ["apple", "ball"]
e = [1, 'select', True]
# list can be any datatype collection

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# print(states_of_america[0])

# negative indexing
# print(states_of_america[-1])

# modify any element of the list with the index
# states_of_america[1] = "Nagaland"
# print(states_of_america)
# print()
# states_of_america[1] = "Pennsylvania"
# print(states_of_america)
# print()
# states_of_america.append("Nagaland")
# print(states_of_america)
# print()

# states_of_america.extend(["Nagaland", "Manland"])
# print(states_of_america)

# print(len(states_of_america))

# states_of_america.insert(0, "Nagaland")
# print(len(states_of_america))

# more list methods
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4
print(fruits.reverse())
print(fruits)
print(fruits.append('grape'))
print(fruits)
print(fruits.sort())
print(fruits)
print(fruits.pop())

# nested lists
veg_foods = ["greens", "carrot", "milk", "fruits"]
non_veg_foods = ["chicken", "mutton", "steaks", "pork"]

combined_foods = [veg_foods, non_veg_foods]


# You are going to write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# if position[1] == "1":
#   if position[0] == 'A':
#     line1[0] = 'X'
#   elif position[0] == 'B':
#     line1[1] = 'X'
#   elif position[0] == 'C':
#     line1[2] = 'X'
# elif position[1] == "2":
#   if position[0] == 'A':
#     line2[0] = 'X'
#   elif position[0] == 'B':
#     line2[1] = 'X'
#   elif position[0] == 'C':
#     line2[2] = 'X'
# elif position[1] == "3":
#   if position[0] == 'A':
#     line3[0] = 'X'
#   elif position[0] == 'B':
#     line3[1] = 'X'
#   elif position[0] == 'C':
#     line3[2] = 'X'

column = position[0].lower()
row = position[1]
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']
map[numbers.index(row)][letters.index(column)] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
