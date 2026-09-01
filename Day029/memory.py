class Memory:

    def __init__(self):
        self.messages = []

    def save(self, message):
        self.messages.append(message)

    def show(self):
        print("Memory:")
        
        for message in self.messages:
            print(f" - {message}")