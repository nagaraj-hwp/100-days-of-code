from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calculator():
    print(logo)
    num1 = float(input("Enter first number to operate: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter second number to operate: "))
        calculation_symbol = operations[operation_symbol]
        answer = calculation_symbol(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        proceed = input(f"Type 'y' to continue calculating with asnwer or type 'n' to start a new calculation or done to exit calculator: ").lower()
        if proceed == "y":
            num1 = answer
        elif proceed == "done":
            exit()
        else:
            should_continue = False
            calculator()


calculator()

