# Decorators in python


def outer():
    print("Outer function call")

    def inner():
        print("Inner function call")
    inner()


# outer()


def decorator_function(function):
    def wrapper_function():
        print("wrapper function call")
        result = function()
        print("result: ", result)
    return wrapper_function


@decorator_function
def say_hi(name="Nagaraj"):
    return name


say_hi()

# Speed calculator function
import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()

# Speed calculator function complete