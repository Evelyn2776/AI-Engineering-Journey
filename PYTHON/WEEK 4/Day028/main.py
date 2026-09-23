from agent import CodingAgent, ResearchAgent, SupportAgent

agents = [
    CodingAgent("CodeBot", "programming"),
    ResearchAgent("ResearchBot", "research"),
    SupportAgent("SupportBot", "customer service")
]

for agent in agents:
    agent.respond()
