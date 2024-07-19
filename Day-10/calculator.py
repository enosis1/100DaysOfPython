import art


def add(num1, num2):
    """Adds two numbers together."""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts two numbers together."""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies two numbers together."""
    return num1 * num2


def divide(num1, num2):
    """Divides two numbers together."""
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    calculator_off = False

    while not calculator_off:
        operator = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operator]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        continue_calculating = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )

        if continue_calculating == "n":
            calculator()
        elif continue_calculating == "y":
            num1 = answer
        else:
            calculator_off = True
            print("Exiting program...")


calculator()
