class User:
    def __init__(self, name, career):
        self.name = name
        self.career = career

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am learning to become an {self.career}.")