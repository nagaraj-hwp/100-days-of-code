# understanding inheritance in OOPS

class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_of_fins = 3

    def swim(self):
        print("Moving in water! Yay")

    def breathe(self):
        super().__init__()
        print("Breathe_under_water")


nemo = Fish()
nemo.swim()
print(nemo.num_of_eyes)
nemo.breathe()
