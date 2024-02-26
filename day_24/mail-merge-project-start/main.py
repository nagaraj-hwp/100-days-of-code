# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.readlines()
print(letter_content)

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
print(name_list)


for line in letter_content:
    if line != '\n':
        print(line)

for name in name_list:
    guest_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_to_{guest_name}", "w") as guest_letter:
        for line in letter_content:
            if "[name]" in line:
                line = line.replace("[name]", guest_name)
                guest_letter.write(line)
            else:
                guest_letter.write(line)

