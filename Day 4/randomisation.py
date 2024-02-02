# understanding randomisation
import random
import my_module
random_integer = random.randint(1, 100)
print(random_integer)

# random float with random.random() produces between 0.00000000 to 0.99999999999999...
random_float = random.random()
print(random_float)

# random float with random.random() can be multiplied with 5 or 10 to produce within its range.
random_float = random.random() * 5
print(random_float)




# Accessing the other modules
# print(my_module.a)
# print(my_module.b)
# print(my_module.c)
# print(my_module.d)
# print(my_module.e)
