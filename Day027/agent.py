class AIAgent:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def respond(self):
        print("I am an AI Agent")

class CodingAgent (AIAgent):

    def respond(self):
        print(f"{self.name}:")
        print(f"I can help with {self.role}.\n")

class ResearchAgent (AIAgent):

    def respond(self):
        print(f"{self.name}:")
        print(f"I can help with {self.role}.\n")

class SupportAgent (AIAgent):

    def respond(self):
        print(f"{self.name}:")
        print(f"I can help with {self.role}.")