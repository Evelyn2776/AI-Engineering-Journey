from agent import AIAgent
from model import Model
from memory import Memory


model = Model()

memory = Memory()

agent = AIAgent("StudyBot", model, memory)

agent.ask("Explain Python classes")

print()

agent.ask("What is inheritance?")

print()

agent.memory.show()