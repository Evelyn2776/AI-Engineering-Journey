# Day 026

## Journal

### Imagine you are building an AI application with three different AI agents:
- Coding Agent
- Research Agent
- Customer Support Agent

### How could inheritance and method overriding allow all three agents to share common functionality while behaving differently?

### What could belong in the parent AI Agent class?

### What could each child agent override?

### Explain how this could make the application easier to maintain.

Inheritance and method overriding allow you to build a highly scalable multi-agent system. Instead of writing separate, redundant scripts for every single agent, you can establish a parent class to handle predictable infrastructure and use method overriding in the child classes to define their unique logic.
Here is how you can cleanly architecture this AI application:
1. The Parent Class: BaseAgent
This class houses the core operational framework that every AI agent needs to exist, connect, and log data.
Shared Information (Attributes):
agent_name: A string identifier for logging.
client: The authenticated LLM API client instance (e.g., OpenAI or Anthropic).
token_counter: An integer tracking operational costs.
Shared Behavior (Methods):
.calculate_cost(): Standard mathematical formula to calculate API bills based on token counts.
.log_interaction(): A function that saves inputs and outputs to a local file or database for auditing.
2. What Each Child Agent Overrides
You establish a core method in the parent class called .generate_response(user_input). By default, it does a plain API call. Each child agent overrides this exact method to inject its specialized workflow.
CodingAgent
What it overrides: The .generate_response() method.
Unique Behavior inside the override:
It injects a strict system persona forcing the output to be purely raw, syntax-highlighted code blocks.
It passes the code through a local syntax checker (like a linter) to verify the code compiles before returning it to the user.
ResearchAgent
What it overrides: The .generate_response() method.
Unique Behavior inside the override:
It intercepts the user prompt and runs a web-search function to grab fresh real-time articles.
It formats those search results into a detailed context block and wraps it in a citation enforcement prompt before making the final LLM call.
CustomerSupportAgent
What it overrides: The .generate_response() method.
Unique Behavior inside the override:
It checks the user's text against a local vector database of company FAQs.
It filters the final LLM output through a strict safety guardrail to ensure no toxic language or internal company secrets leak out.