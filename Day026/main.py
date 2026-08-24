from agent import CodingAgent, ResearchAgent, SupportAgent

agent1 = CodingAgent("CodeBot", "Coding Agent")
agent2 = ResearchAgent("ResearchBot", "Research Agent")
agent3 = SupportAgent("SupportBot", "Support Agent")

agent1.introduce()
agent1.respond()
print()
agent2.introduce()
agent2.respond()
print()
agent3.introduce()
agent3.respond()