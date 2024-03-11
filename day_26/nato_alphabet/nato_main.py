import pandas


nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic.iterrows()}
# print(nato_phonetic_dict)


def nato_create():
    name = input("Enter a name: ").upper()
    try:
        nato_phonetic_name = [nato_phonetic_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, Only letters are allowed in the alphabet please.")
        nato_create()
    else:
        print(f"{nato_phonetic_name}")


nato_create()



