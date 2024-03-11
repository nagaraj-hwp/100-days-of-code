# Error handling in Python

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["no_key"])
    a_list = [1, 2, 3, 4]
    print(a_list[4])
    print(a_set)
    print(a_list[1] + "a")
except FileNotFoundError:
    print("File does not exist, let's create")
    file = open("a_file.txt", "w")
    file.write("Created this file\n")
    file.close()
except KeyError as error_message:
    print(f"Key {error_message} not exist")
except IndexError:
    print("No more index to access")
except NameError:
    print("Variable not defined")
except ValueError:
    print("Check your values")
else:
    content = file.read()
    print(content)
finally:
    print("I am a finally block")


