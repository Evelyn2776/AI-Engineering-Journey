class Student:
    def __init__(self, name, country, career, *languages):
        self.name = name
        self.country = country
        self.career = career
        self.__languages = list(languages)

    def introduction (self):
        print(f"Hello, my name is {self.name}.") 
        print(f"I am from {self.country}.")
        print(f"I am learning to become {self.career}.")

    def languages (self):
        print("Programming Languages:")
        for lan in self.__languages:
            print(f" - {lan}")

    def language_count (self):
        length = len(self.__languages)
        print(f"You know {length} programming languages.")

    def has_language (self):

        search = input("Search language: ")

        if search in self.__languages:
            print(f"{search} is in your list.")
        else:
            print(f"{search} is not in your list.")

    def add_language (self): 
        new = input("Add a language: ")

        self.__languages.append(new)

        print("Updated Programming Languages: ")
        for language in self.__languages:
            print(f" - {language}")