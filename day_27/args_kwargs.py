
# def fun(a=1, b=2, c=3):
#     print(a, b, c)
#
#
# fun()  # 1 2 3
# fun(4, 5)  # 4 5 3
# fun(4, c=9)  # 4 2 9
# fun(b=10)  # 1 10 3

# variable arguments
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=10, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make_year = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(color="blue", make=2000)

print(my_car.model)
print(my_car.color)


