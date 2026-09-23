name = input("Name: ")
country = input("Country: ")
career = input("Career: ")

with open("profile.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Country: {country}\n")
    file.write(f"Career: {career}\n")