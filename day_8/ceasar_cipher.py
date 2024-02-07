# Final project day-8
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    list_text = list(text)
    word_length = len(list_text)
    for i in range(word_length):
        print("Text[i] is", text[i])
        list_text[i] = alphabet[alphabet.index(text[i])+shift]
        print(list_text)
    print(f"Final text output {''.join(list_text)}")

encrypt(text, shift)
