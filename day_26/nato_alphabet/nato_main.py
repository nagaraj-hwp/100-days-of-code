import pandas


nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic.iterrows()}
# print(nato_phonetic_dict)

nato_created = False
while not nato_created:
    name = input("Enter a name: ").upper()
    try:
        nato_phonetic_name = [nato_phonetic_dict[letter] for letter in name]
    except KeyError:
        print("\nSorry, Only letters are allowed in the alphabet please.")
    else:
        print(f"\n{nato_phonetic_name}")
        nato_created = True



