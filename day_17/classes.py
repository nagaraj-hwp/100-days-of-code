# understanding and creating classes

class User:
    def __init__(self, id, username):
        print("Constructor been called")
        self.id = id
        self.username = username

user_1 = User("001", "nagaraj_hwp")
print(user_1)
user_2 = User("002", "common_man_says")
print(user_2)


