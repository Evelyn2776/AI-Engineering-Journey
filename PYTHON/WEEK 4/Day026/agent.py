class AIAgent:

    def __init__ (self, name, role):
        self.name = name
        self.role = role

    def introduce (self):
        print(f"Hello, I am {self.name}.")
        print(f"I am a {self.role}.")

    def respond (self):
        print("I can help with your request.")

class CodingAgent (AIAgent):

    def respond(self):
        print("I can help with your programming.")

class ResearchAgent (AIAgent):

    def respond(self):
        print("I can help with your research.")

class SupportAgent (AIAgent):

    def respond(self):
        print("I can help you with customer support.")