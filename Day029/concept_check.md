# Day 029 - Concept Check

## Question 1
### What is composition?
Composition is an Object-Oriented Programming design principle where one class is built using one or more objects of other classes as its parts. Instead of inheriting features from a parent, a class delegates tasks to internal component objects.

## Question 2
### What does a "has-a" relationship mean?
A "has-a" relationship means that one complex object owns or contains another distinct object as part of its state. For example, a Chatbot has a MemoryManager, or an AI_Model has a Tokenizer.

## Question 3
### What is the difference between "is-a" and "has-a"?
"Is-a" represents inheritance, meaning a child class is a specialized version of a parent class (e.g., a CodingAgent is an Agent). "Has-a" represents composition, meaning a class contains an instance of another class to add functionality (e.g., an Agent has an LLMClient).

## Question 4
### Why would a Car contain an Engine instead of inheriting from Engine?
A car shouldn't inherit from an engine because a car is not a specialized type of engine. If it inherited, the car would structurally expose internal engine mechanics (like pistons or spark plugs) as its own top-level features, which breaks logical boundaries and creates messy, fragile code.

## Question 5
### How does a class contain an object from another class?
A class contains another object by instantiating the component class and assigning it to an instance variable, usually inside its __init__() constructor method.

class Agent:
    def __init__(self):
        self.memory = MemoryManager()

## Question 6
### Why can composition make software easier to maintain?
It keeps classes loosely coupled, highly isolated, and focused on a single responsibility. If you need to fix a bug or rewrite the code inside a sub-component, you can change that component's file without risking breaking the parent class that wraps it.

## Question 7
### When would you choose composition instead of inheritance?
You should favor composition when you want to assemble diverse, independent features dynamically, or when a clear "is-a" relationship doesn't exist. There is a famous software engineering maxim: "Favor object composition over class inheritance" because it avoids rigid hierarchical entanglements.

## Question 8
### How can components be replaced when using composition?
Components can be easily swapped out by passing a different object instance into the class constructor (Dependency Injection). Because the parent class interacts with the component via a standard interface, you can swap one part for another without changing the parent class code.

## Question 9
### How could composition be used in an AI application?
You can build a comprehensive AIAgent class entirely through composition. Instead of writing one massive script, the agent has a TokenTracker component, has a VectorDBClient component, and has a PromptFormatter component. The agent acts as an assembly line coordinator directing these pieces.

## Question 10
### What did you find interesting about composition today?
The most compelling realization is how composition mirrors real-world engineering. Instead of forcing code into rigid evolutionary family trees like inheritance, composition lets you snap self-contained modules together like Lego blocks, allowing you to build highly complex AI architectures out of tiny, simple parts.
