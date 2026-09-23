from student import Student

name = input("Name: ")
country = input("Country: ")
career = input("Career: ")
languages = input("Programming languages: ")
langs = languages.split()

Info = Student(name, country, career, *langs)

print()
print("==============================")
print("STUDENT PROFILE")
print("==============================\n")
Info.introduction()
print()
Info.languages()
print()
Info.language_count()
print()
Info.has_language()
print()
Info.add_language()