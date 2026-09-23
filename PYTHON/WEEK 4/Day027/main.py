from agent import CodingAgent, ResearchAgent, SupportAgent

agents = [
    CodingAgent("CodingBot", "Coding"),
    ResearchAgent("ResearchBot", "Research"),
    SupportAgent("SupportBot", "Support")
]

for agent in agents:
    agent.respond()