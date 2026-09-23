import json

name = input("Enter your name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
career = input("Enter your career: ")

profile = {
    "Name": name,
    "Country": country,
    "Age": age,
    "Career": career
}

with open("student_profile.json", "w") as file:
    json.dump(profile,file,indent=4)

print("\n Student profile saved successfully.")