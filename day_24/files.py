# Understanding how to handle files using python

# file = open("text_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("text_file.txt", mode="r+") as file:
    contents = file.read()
    print(contents)
    file.write("Let me write to it\n")
    print(contents)


