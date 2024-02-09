# Understanding Scopes in Python
# count = 1

# def increase_count():
#     count = 2
#     print(f"Count inside function: {count}")

# increase_count()
# print(f"Count Outside function: {count}")


# Local Scope
# def count_function():
#     count = 2 # local to function
#     print(f"Count inside function: {count}")

# count_function()
# print(f"Count Outside function: {count}")

# Block Scope
# in python unlike c, c++, Java there is nothing called block scope
# eg:
fill = "Red"
if fill == "Red":
    color = "Blue"

print(color) # Variable insode if block works outside as well.
