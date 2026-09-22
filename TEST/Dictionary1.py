# 1. Create a dictionary
student = {
    "name": "John",
    "age": 18,
    "course": "Python"
}

print(student)

# 2. Access dictionary values
print(student["name"])
print(student["course"])

# 3. Add a new key
student["Grade"] = "A"
print(student)

# 4. Change a value
student["grade"] = "B"
print(student)

# 5. Delete a key
del student["age"]
print(student)

# 6. Dictionary containing a list
student["Subject"] = ["Math", "English", "Python"]
print(student)

# 7. Index a list inside a dictionary
student["Subject"].remove("Python")
print(student["Subject"][1])

# 8. Append to a list inside a dictionary
print(student)
student["Subject"].append("Python")

# 9. Delete from a list inside a dictionary
print(student)
student["Subject"].remove("English")

# 10. Modify an item using an index
student["Subject"][1] = "Science"
print(student)

# 11. Shopping cart
cart = {
    "items": ["rice", "beans", "milk"],
    "total": 5000
}

cart["items"].append("bread")
cart ["items"].remove("beans")
cart["total"] = 5500
print(cart)

# 12. Dictionary of students
student = {
    "John": [80, 75, 90],
    "Mary": [95, 88, 92],
    "Peter": [70, 65, 80]
}

print(student["John"][1])

# 13.Add a score
student["John"].append(85)
print(student)

# 14. Remove a score
student["Peter"].remove(70)
print(student)

# 15. Dictionary manipulation
person = {
    "name": "Alice",
    "age": 20,
    "hobbies": ["reading", "music"]
}

person["age"] = 21
person["hobbies"].append("coding")
person["hobbies"].remove("music")
person["country"] = "Nigeria"
print(person)

# 16. Create a dictionary from input
name = input("Name: ")
age = int(input("Age: "))
country = input("Country: ")

Dict = {
    "Name": name,
    "Age": age,
    "Country": country
}

print(Dict)

# 17. Input multiple items into a dictionary list
person = {
    "name": "David",
    "foods": []
}

favorite_food = input("Food 1: ")
favorite_food1 = input("Food 2: ")
favorite_food2 = input("Food 3: ")

person["foods"].append(favorite_food)
person["foods"].append(favorite_food1)
person["foods"].append(favorite_food2)

# 18. Input and convert to a list
print("Seperate numbers by space.")

Numbers = input("Numbers:")

Numbers = [int(number) for number in Numbers.split()]

Dict = {
    "Numbers": Numbers
}

print(Dict)

# 19. Student management system
name = input("Name: ")
age = input("Age: ")

subjects = input("Subjects: ")
subjetcs = subjects.split(" ")

Dict = {
    "Name": name,
    "Age": age,
    "Subjects": subjects
}

Add = input("Another subject: ")
Dict["Subjects"].append(Add)

Remove = input("Rmove a subject: ")
Dict["Subjects"].remove(Remove)

new_age = int(input("Change age: "))
Dict["Age"] = new_age

print(Dict["Subjects"][0])
print(Dict)

# 20. Mini contact book
Name = input("Contact Name: ")
Age = input("Contact Age: ")
Phone = input("Add Number: ")

Phone = Phone.split(",")    

Dictionary = {
    Name: {
        "Age": Age,
        "Phone": Phone
    }
}

new_contact = input("Another contact: ")
new_age = int(input("Enter age: "))
new_phone = int(input("Enter number: "))

Dictionary[new_contact] = {
    "Age": new_age,
    "Phone": new_phone
}

del Dictionary[new_contact]
