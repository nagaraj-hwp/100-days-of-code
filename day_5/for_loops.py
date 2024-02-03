# understanding for loops
# for item in list_of_items:
#     Do this action


fruits = ["Apple", "Peach", "Cherry"]

for fruit in fruits:
    print(fruit)


# write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# tot = 0
# for i in student_heights:
#     tot += i
# student = len(student_heights)
# print("total height = ", tot)
# print("number of students = ", student)
# print("average height = ", round(tot/student))


# write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

# Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# max_grade = 0
# for grade in student_scores:
#     if max_grade < grade:
#         max_grade = grade
# print("The highest score in the class is:", max_grade)

# write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

# target = int(input())  # Enter a number between 0 and 1000
# total = 0
# for num in range(target+1):
#     if num % 2 == 0:
#         total += num
# print(total)

# total = 0
# for num in range(2, target+1, 2):
#     total += num
# print(total)
