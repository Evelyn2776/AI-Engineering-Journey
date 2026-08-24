class Student:
    def __init__(self, name, career, topic, *topics):

        self.name = name
        self.career = career
        self.topic = topic
        self.__topics = list(topics)

    def introduction (self):

        print(f"Hello, my name is {self.name}.")
        print(f"I am learning to become an {self.career}.")

    def show_topics (self):

        print("Topics Studied")

        for note in self.__topics: 
            print(f" - {note}")

    def topics_count (self):

        length = len(self.__topics)
        print(f"You have studied {length} topics.")

    def search_topic (self):

        search = input("Search topic: ")

        if search in self.__topics:
            print(f"{search} is in your study list.")
        else:
            print(f"{search} is not in your list.")

    def add_topic (self):

        new = input("Add a new topic: ")
        self.__topics.append(new)

        for notes in self.__topics:
            print(f" - {notes}")

    def change_topic (self):

        new_topic = input("New Study Topic: ")

        self.topic = new_topic

        print(f"Current topic studying is {self.topic}.")