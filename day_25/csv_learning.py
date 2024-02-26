# Working with csv files using Python

# with open("./weather_data.csv", "r") as data:
#     weather_data = data.readlines()
#     print(weather_data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["day"])  # both are same
# print(data.day)  # both are same

#
# data_dict = data.to_dict()
# print(data_dict)
#
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
#
# print(max_temp)

# Get data in a row
# row = data[data.temp == 14]
# print(row)

max_temp_row = data[data.temp == data.temp.max()]
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
# print(max_temp_row)
# print(monday)
print(monday_temp)

monday_temp_f = monday_temp * 9 / 5 + 32
print(monday_temp_f)

# Create a dataframe from scratch

data_dict = {
    "students": ["Nagaraj", "NP", "Raj"],
    "scores": [99, 100, 98],
    "age": [24, 25, 23]
}

panda_data = pandas.DataFrame(data_dict)
print(panda_data)
panda_data.to_csv("student_data.csv")

