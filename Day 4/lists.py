# understanding lists
a = []
b = [1, 2, 3]
c = ['a', 'b', 'c']
d = ["apple", "ball"]
e = [1, 'select', True]
# list can be any datatype collection

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


print(states_of_america[0])

# negative indexing
print(states_of_america[-1])

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

print(len(states_of_america))

states_of_america.insert(0, "Nagaland")
print(len(states_of_america))

# more list methods
