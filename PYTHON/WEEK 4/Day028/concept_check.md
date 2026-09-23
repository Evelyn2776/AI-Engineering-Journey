# Day 028 - Concept Check

## Question 1
### What is abstraction?
Abstraction is the programming concept of hiding complex implementation details and showing only the essential features of an object. It focuses on what an object does rather than how it does it, reducing complexity for the user.

## Question 2
### What is an abstract class?
An abstract class is a blueprint template that cannot be instantiated directly. It is designed to be inherited by subclasses, forcing them to adopt a specific structure and share common behavior.

## Question 3
### What is an abstract method?
An abstract method is a method declared in an abstract class that has a name and arguments but contains no implementation code. Any concrete (non-abstract) subclass must override and implement this method.

## Question 4
### What does `ABC` mean in Python?
ABC stands for Abstract Base Class. It is a built-in module in Python (from abc import ABC) used to define abstract classes by serving as their parent class.

## Question 5
### What does `@abstractmethod` do?
@abstractmethod is a decorator applied to a method inside an abstract class. It signals to Python that any subclass must provide its own implementation for this specific method, or Python will refuse to instantiate the subclass.

## Question 6
### Why can't an abstract class normally be instantiated directly?
It cannot be instantiated because it is incomplete. Because it contains abstract methods without actual code, creating an object from it would leave the computer with missing instructions if those methods were called.

## Question 7
### What is the difference between abstraction and encapsulation?
Abstraction is about hiding complexity (hiding the internal machinery and showing a simple interface).
Encapsulation is about hiding data (bundling variables and methods together into a single unit and restricting direct external access using private/protected modifiers).

## Question 8
### How is abstraction related to inheritance?
Abstraction relies entirely on inheritance to work. An abstract class defines the structural rules, and inheritance passes those rules down to child classes, which are then forced to fill in the missing implementation details.

## Question 9
### How could abstraction be useful when designing an AI agent system?
You could create an abstract AIAgent class with an abstract method called think(). Different specialized models (like an LLM agent, a rules-based agent, or a reinforcement learning agent) can inherit from it. The main system can then run agent.think() uniformly without needing to know the unique, messy mechanics of how each specific AI generates its decision.

## Question 10
### What did you find interesting about abstraction today?
As an AI assistant, I don't have personal feelings, but students usually find it fascinating how abstraction mimics real life. For instance, you know how to use a steering wheel and pedals to drive a car (the interface) without needing to understand the thermodynamic explosion happening inside the engine block (the implementation complexity).
