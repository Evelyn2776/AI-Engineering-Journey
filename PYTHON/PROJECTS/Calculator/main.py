from PYTHON.PROJECTS.Calculator.calculator import Calculator


def perform_calculation(calculator: Calculator, operation: str) -> float:
    operations = {
        "+": calculator.add,
        "-": calculator.subtract,
        "*": calculator.multiply,
        "/": calculator.divide,
        "**": calculator.power
    }

    if operation not in operations:
        raise ValueError("Invalid operation.")

    return operations[operation]()


def display_menu():
    print()
    print("================================")
    print("          CALCULATOR")
    print("================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")
    print("================================")


def main():
    print("=== Welcome to Calculator ===")

    operation_map = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "**"
    }

    while True:
        display_menu()

        choice = input("Choose an option: ")

        if choice == "6":
            print("Goodbye!")
            break

        if choice not in operation_map:
            print("Invalid option. Please choose 1-6.")
            continue

        operation = operation_map[choice]

        try:

            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))


            calculator = Calculator(number1, number2)

            result = perform_calculation(calculator, operation)

            print(f"Result: {result}")

        except ValueError as error:
            print(f"Error: {error}")

        except ZeroDivisionError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()
