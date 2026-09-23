try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    div = num1 / num2

    print(f"Answer: {div}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("You cannot divide by zero.")