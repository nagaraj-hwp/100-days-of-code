# Decorators in python


def outer():
    print("Outer function call")

    def inner():
        print("Inner function call")
    inner()


outer()
