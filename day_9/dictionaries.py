# Understanding Dictionaries in Python
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again."}

# programming_dictionary["Loop"] = "The action of doing something repeatedly"

# print(programming_dictionary)

# print(programming_dictionary["Bug"])

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
# -------------------------------------------------------------------

# Day 9 Grading program challenge
# LESSON 22 DAY 9 - GRADING PROGRAM
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for student in student_scores:
#   score = student_scores[student]
#   if score >= 91 :
#     student_grades[student] = "Outstanding"
#   elif score >= 81 :
#     student_grades[student] = "Exceeds Expectations"
#   elif score >= 71:
#     student_grades[student] = "Acceptable"
#   elif score <= 70:
#     student_grades[student] = "Fail"

# print(student_grades)


# -------------------------------------------------------------------

# Nesting in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hmburg", "Stuttgart"]
# }

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille"],
#         "cities_yet_to_visit": ["Dijon"]},
#     "Germany": {
#         "cities_visited": ["Berlin", "Hmburg"],
#         "cities_yet_to_visit": ["Stuttgart"]}
# }

# # Nesting Dictionary in a list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille"],
#         "cities_yet_to_visit": ["Dijon"]
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hmburg"],
#         "cities_yet_to_visit": ["Stuttgart"]
#     }
# ]


# print(travel_log)

# -------------------------------------------------------------------

# LESSON 23 DAY 9 - DICTIONARY IN LIST
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.
# Write a function that will work with the following line of code to add the entry for Brazil to the travel_log.
# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])

country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, list_of_cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = list_of_cities
    travel_log.append(new_dict)


add_new_country(country, visits, list_of_cities)
print(
    f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# -------------------------------------------------------------------
