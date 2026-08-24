# Day 025 - Concept Check

## Question 1
### What is inheritance in Python?
Inheritance is an Object-Oriented Programming (OOP) mechanism that allows a new class to adopt the attributes and methods of an existing class. It establishes a hierarchical relationship between classes, enabling code reuse and customization.

## Question 2
### What is a parent class?
A parent class (also called a base class or superclass) is the original class whose properties and functionalities are passed down. It contains the shared, common logic that multiple related classes will use.

## Question 3
### What is a child class?
A child class (also called a derived class or subclass) is the new class that inherits from the parent class. It automatically receives all data and behavior from the parent, while retaining the ability to add unique features or override existing ones.

## Question 4
### What does `class Student(User):` mean?
This syntax means that a new class named Student is being created as a child class that inherits directly from the User parent class. The Student class automatically gains access to everything defined inside User.

## Question 5
### What happens when a child class inherits from a parent class?
The child class automatically copies all attributes and methods of the parent without physical duplication. You can immediately call the parentâ€™s methods on an object instance of the child class.

## Question 6
### Why is inheritance useful for avoiding duplicated code?
It groups all shared functionality into one central location. Instead of writing identical code for an Admin, a Teacher, and a Student, you write common code once in a User parent class, drastically reducing code bloat and maintenance layout.

## Question 7
### What does `super()` do?
super() is a built-in Python function that returns a temporary object of the parent class, allowing the child class to call its methods. It is most commonly used inside a child's constructor to execute the parent's initialization logic first.

## Question 8
### Why might a child class need its own `__init__()` method?
A child class needs its own constructor when it must accept and track unique inputs that the generic parent class does not care about. For example, a Student needs all User information plus a unique student_id.

## Question 9
### How could inheritance be useful when building different AI agents?
You can create a generic BaseAgent parent class that handles core tasks like API connections and token counting. Then, you can build specialized child classes like CodingAgent or SupportAgent that inherit that core setup but implement their own custom system prompts and specialized tools.

## Question 10
### What did you find interesting about inheritance today?
The most interesting part is method overridingâ€”how a child class can silently rewrite a parent's method to change its behavior. It offers the perfect balance of structural uniformity and creative freedom when writing complex multi-agent AI workflows.
