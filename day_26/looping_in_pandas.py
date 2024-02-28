import pandas

student_dict = {
    "student": ["Nagaraj", "Raj", "NP"],
    "score": [100, 99, 100]
}

# Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key, value)


pandas.DataFrame(student_dict)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data
for (index, row) in student_data_frame.iterrows():
    if row.student == "NP":
        print(row.student)
        print(row.score)



