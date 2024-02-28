import pandas


nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic.iterrows()}
print(nato_phonetic_dict)


name = input("Enter a name: ").upper()
nato_phonetic_name = [nato_phonetic_dict[letter] for letter in name]
print(nato_phonetic_name)



