# Day 028 - Lesson Notes

## Abstraction
Abstraction is an Object-Oriented Programming concept that focuses on what an object should do while hiding unnecessary implementation details.

## Abstract Classes
An abstract class provides a structure or blueprint for child classes. Python provides the abc module for creating abstract classes. Example:

from abc import ABC, abstractmethod
class AIAgent(ABC):

    @abstractmethod
    def respond(self):
        pass

AIAgent is an abstract class.

## Abstract Methods
An abstract method defines a method that child classes are expected to implement. Example:

@abstractmethod
def respond(self):
    pass

The parent class defines the required method, but the child class provides the actual implementation.

## Child Classes
Example:
class CodingAgent(AIAgent):

    def respond(self):
        print("I can help with programming.")

The CodingAgent implements the respond() method required by AIAgent.

## Why Abstraction Is Useful
Abstraction creates a consistent structure for related classes.
It allows developers to define what functionality must exist without forcing every implementation to work in exactly the same way.

## Abstraction and Polymorphism
Abstraction and polymorphism can work together.
An abstract parent class can require every child to implement the same method.
Each child can then provide its own implementation.
For example:

AIAgent
├── CodingAgent
├── ResearchAgent
└── SupportAgent

All agents must implement respond(), but each agent can respond differently.

## AI Engineering Connection
A BaseAgent class could require every AI agent to implement methods such as:
respond()
process_input()
generate_output()

Different specialized agents could implement these methods according to their own requirements.
The rest of the application can interact with all agents through the common abstract interface.

## Key Idea
Abstraction defines what must exist.
The child classes define how it works.