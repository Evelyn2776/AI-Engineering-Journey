# Day 029 - Lesson Notes

## Composition
Composition is an Object-Oriented Programming design technique where one class contains objects of another class and uses them as components.
A simple way to remember composition is: "Has-a relationship."

## Inheritance vs Composition
Inheritance represents an "is-a" relationship. Examples:
Student IS A User.
CodingAgent IS AN AIAgent.

Composition represents a "has-a" relationship. Examples:
Car HAS AN Engine.
AIApplication HAS A Model.

## Simple Example
class Engine:

    def start(self):
        print("Engine started.")

class Car:

    def __init__(self):
        self.engine = Engine()

The Car class contains an Engine object. We can then use:
car = Car()
car.engine.start()

## Why Composition Is Useful
Composition allows a class to be built from smaller, specialized objects. Each object can have its own responsibility.
This can make programs easier to understand, test, replace, and maintain.

## Composition and Inheritance
Inheritance should be used when there is a genuine "is-a" relationship.
Composition should be considered when one object needs to use or contain another object.

## AI Engineering Connection
An AI application may contain several independent components. For example:

AIApplication
├── Model
├── Database
├── Memory
└── ToolManager

The AIApplication can contain instances of these components instead of inheriting from them.
This allows components to be replaced independently.
For example, an application could use different model implementations without changing the main application structure.

## Key Idea
Inheritance: "IS-A"
Composition: "HAS-A"