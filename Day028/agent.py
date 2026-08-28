from abc import ABC, abstractmethod

class AIAgent:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def respond (self):
        print(f"I am {self.name} and I will be helping with {self.role}.")

class BaseAgent (AIAgent, ABC):

    @abstractmethod
    def respond (self):
        pass

class CodingAgent (BaseAgent):

    def respond (self):
        print(f"I am {self.name} and I will be helping with {self.role}.")

class ResearchAgent (BaseAgent):

    def respond (self):
        print(f"I am {self.name} and I will be helping with {self.role}.")

class SupportAgent (BaseAgent):

    def respond (self):
        print(f"I am {self.name} and I will be helping with {self.role}.")