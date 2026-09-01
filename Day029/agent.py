class AIAgent:

    def __init__(self, name, model, memory):
        self.name = name
        self.model = model
        self.memory = memory

    def ask(self, message):
        print(f"{self.name}")

        response = self.model.generate(message)

        self.memory.save(message)

        print(response)