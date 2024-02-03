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
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

tot = 0
for i in student_heights:
    tot += i
student = len(student_heights)
print("total height = ", tot)
print("number of students = ", student)
print("average height = ", round(tot/student))


# write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# The highest score in the class is: x

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_grade = 0
for grade in student_scores:
    if max_grade < grade:
        max_grade = grade
print("The highest score in the class is:", max_grade)
