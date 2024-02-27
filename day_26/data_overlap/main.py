with open("file1.txt") as file1:
    file1_contents = file1.readlines()
with open("file2.txt") as file2:
    file2_contents = file2.readlines()

# file1_list = []
# file2_list = []
# result = []
# for item in file1_contents:
#     file1_list.append(int(item.strip()))
# for item in file2_contents:
#     file2_list.append(int(item.strip()))
# for n in file1_list:
#     if n in file2_list:
#         result.append(n)

result = [int(num) for num in file2_contents if num in file1_contents]
print(result)

