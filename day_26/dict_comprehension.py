# Dictionary comprehension
import random

# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test_condition}


# names = ["Nagaraj", "Ashok", "Santhanam", "Rishi", "Mani", "Rajalingam", "Ponmuthu", "Ajith"]
#
# students_scores = {student: random.randint(1, 100) for student in names}
#
# print(students_scores)

# for value in students_scores:
#     print(value)

# passed_students = {student: score for student, score in students_scores.items() if score >= 50}
# print(passed_students)

# LESSON 31 DAY 26 - DICTIONARY COMPREHENSION 1
sentence = input()
# word_list = sentence.split()
# print(word_list)
# result = {word: len(word) for word in word_list}
result = {word: len(word) for word in sentence.split()}
print(result)












