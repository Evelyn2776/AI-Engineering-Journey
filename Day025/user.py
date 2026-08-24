class User:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def introduce (self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am from {self.country}.")

class Student (User):

    def __init__(self, name, country, career):
        super().__init__(name, country)
        self.career = career

    def study (self):
        print(f"I am studying to become an {self.career}.")
        