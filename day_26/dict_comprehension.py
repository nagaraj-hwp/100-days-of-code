# Dictionary comprehension
import random

# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test_condition}


names = ["Nagaraj", "Ashok", "Santhanam", "Rishi", "Mani", "Rajalingam", "Ponmuthu", "Ajith"]

students_scores = {student: random.randint(90, 100) for student in names}

print(students_scores)







