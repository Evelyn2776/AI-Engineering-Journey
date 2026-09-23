# Day 025 - Lesson Notes

## Inheritance

Inheritance is an Object-Oriented Programming concept that allows one class to reuse attributes and methods from another class.

The class being inherited from is called the parent class or base class.

The class that inherits from it is called the child class or derived class.

## Basic Example

class User:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(User):
    pass

Student inherits from User, so Student automatically has access to the name attribute and introduce() method.

## Why Inheritance Is Useful

Inheritance reduces duplicated code.

If several classes share the same attributes or behaviors, those common features can be placed in a parent class and reused by multiple child classes.

For example:

User
├── Student
├── Teacher
└── Developer

All of these classes may share:

- name
- country
- email
- introduce()

The child classes can then add their own specialized features.

## super()

super() allows a child class to call functionality from its parent class.

Example:

class User:

    def __init__(self, name, country):
        self.name = name
        self.country = country


class Student(User):

    def __init__(self, name, country, career):
        super().__init__(name, country)
        self.career = career

super().__init__(name, country) calls the parent User constructor.

This allows Student to reuse the parent's initialization instead of rewriting it.

## Inheritance and AI Engineering

Inheritance can help organize AI applications containing different types of agents.

For example:

AI Agent
├── CustomerSupportAgent
├── CodingAgent
└── ResearchAgent

The parent AI Agent class could contain common functionality such as model configuration, user information, or shared API behavior.

Each specialized agent could then add its own attributes and methods.

## Key Idea

Inheritance allows a child class to reuse functionality from a parent class while adding specialized behavior of its own.

super() provides a clean way for the child class to use functionality defined by its parent.