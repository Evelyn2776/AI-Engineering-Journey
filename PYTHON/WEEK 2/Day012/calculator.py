try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operator = input("Operator: ")

    if operator == "+":
        answer = number1 + number2

    elif operator == "-":
        answer = number1 - number2

    elif operator == "*":
        answer = number1 * number2

    elif operator == "/":
        answer = number1 / number2

    else:
        print("Unsupported operator.")
        answer = None

    if answer is not None:
        print(f"Result: {answer}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")