# Day 026 - Lesson Notes

## Method Overriding
Method overriding occurs when a child class provides its own implementation of a method that already exists in its parent class.
The child class inherits from the parent but changes how that particular method behaves.

## Example
class User:

    def introduce(self):
        print("I am a user.")

class Student(User):

    def introduce(self):
        print("I am a student.")

The Student class overrides the introduce() method inherited from User.

## Why Method Overriding Is Useful
Different types of objects may need the same method but require different behavior. For example:
User
├── Student
├── Developer
└── AIEngineer

Each class could have its own introduce() method.

## Using super()
super() allows a child class to access functionality from its parent. Example:
class User:

    def introduce(self):
        print("Hello, I am a user.")

class Student(User):

    def introduce(self):
        super().introduce()
        print("I am a student.")

The parent method runs first, followed by the child's additional behavior.

## Inheritance vs Method Overriding
Inheritance allows a child class to reuse functionality from a parent class.
Method overriding allows a child class to customize or replace inherited behavior.

## AI Engineering Connection
AI applications can have different types of agents that share common functionality but behave differently. For example:
AIAgent
├── CodingAgent
├── ResearchAgent
└── SupportAgent

Each specialized agent could override a method such as respond() to provide behavior specific to its role.

## Key Idea
Inheritance means:
"Reuse functionality from the parent."

Method overriding means:
"Reuse the structure, but change specific behavior."