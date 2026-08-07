password = input("Password: ")
correct_password = "python123"

try:
    if password == correct_password:
        print("Access granted.")
    else:
        print("Incorrect password.")

except ValueError as error:
    print(f"Something went wrong: {error}")
    