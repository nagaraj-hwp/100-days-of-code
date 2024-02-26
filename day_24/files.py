# Understanding how to handle files using python

# file = open("text_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("text_file.txt", mode="a+") as file1:
    file1.write("Let me write to it\n")
    contents = file1.read()
    print(contents)


with open("../day_23/sample.txt", mode="w+") as file2:
    file2.write("Let me write to it\n")
    contents = file2.read()
    print(contents)

