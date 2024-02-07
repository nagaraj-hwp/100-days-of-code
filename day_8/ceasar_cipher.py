# Final project day-8
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter == " ":
            cipher_text += " "
            continue
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position -= 25
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"Your encrypted text {cipher_text}")


def decrypt(encrypted_text, shift_amount):
    reverted_text = ""
    for letter in encrypted_text:
        if letter == " ":
            reverted_text += " "
            continue
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if new_position < 0:
            new_position += 25
        print("New position value", new_position)
        new_letter = alphabet[new_position]
        reverted_text += new_letter

    print(f"Your decrypted text {reverted_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)

elif direction == "decode":
    decrypt(encrypted_text=text, shift_amount=shift)
