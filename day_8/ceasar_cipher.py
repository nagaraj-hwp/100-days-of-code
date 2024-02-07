# Final project day-8
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
            continue
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d result is '{end_text}'\n")


go_again = True
while go_again:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    yes_no = input(
        "Type 'yes', if you want to go again. Otherwise type 'no'\n").lower()
    if yes_no == "yes":
        continue
    else:
        print("Bye, Take care\n")
        go_again = False
