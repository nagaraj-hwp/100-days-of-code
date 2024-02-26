# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
########################################################################################
# with open("./Input/Letters/starting_letter.txt") as letter:
#     letter_content = letter.read()
#
# with open("./Input/Names/invited_names.txt") as names:
#     name_list = names.readlines()
#
# for name in name_list:
#     guest_name = name.strip()
#     with open(f"./Output/ReadyToSend/letter_to_{guest_name}", "w") as guest_letter:
#         for line in letter_content:
#             if "[name]" in line:
#                 line = line.replace("[name]", guest_name)
#                 guest_letter.write(line)
#             else:
#                 guest_letter.write(line)

###########################################################################3

# Angela version

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", "w") as letter:
            letter.write(new_letter)
