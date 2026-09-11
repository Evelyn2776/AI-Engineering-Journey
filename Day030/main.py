try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
else:
    print(f"You are {age} years old.")
finally:
    print("Program finished.")