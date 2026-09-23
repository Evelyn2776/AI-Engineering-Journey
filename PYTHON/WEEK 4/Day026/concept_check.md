# Day 026 - Concept Check

## Question 1
### What is method overriding?
Method overriding is an Object-Oriented Programming feature that allows a child class to provide a specific implementation of a method that is already defined in its parent class. It lets the child class change how a parent action behaves.

## Question 2
### Why would a child class override a method from its parent?
A child class overrides a method when the default behavior provided by the parent is too generic or incorrect for the child's specific role. It allows the child class to handle the same action in its own unique way.

## Question 3
### What happens when a child class defines a method with the same name as a parent method?
The child's method completely masks, intercepts, and takes precedence over the parent's method. When you call that method name on a child object instance, Python runs the child's custom code instead of the parent's code.

## Question 4
### What is the difference between inheritance and method overriding?
Inheritance is the act of a child class gaining and reusing a parent class's attributes and methods. Method overriding is the act of a child class modifying or completely replacing an inherited method to change its specific behavior.

## Question 5
### What does super() allow a child class to do?
It allows the child class to call and execute the parent class's version of an overridden method. This is useful when you want to extend or add to the parent's logic rather than completely discarding it.

## Question 6
### Can multiple child classes override the same parent method?
Yes, absolutely. Multiple child classes can inherit from the same parent and each override the same method in completely different ways, a foundational programming concept known as polymorphism.

## Question 7
### Why is method overriding useful in larger applications?
It creates an identical, reliable interface across different objects. Larger applications can run a single standard command (like .process_payment()) across hundreds of distinct objects without caring about the unique, internal overriding logic of each specific subclass.

## Question 8
### What is the difference between adding a new method and overriding a method?
Adding a new method introduces a completely new action name unique to that specific child class. Overriding a method retains an existing action name from the parent class but fundamentally changes what happens when that name is called.

## Question 9
### How could method overriding be useful when building different AI agents?
You can create a parent BaseAgent with a default .respond() method that simply calls a basic LLM API. Then, a child ResearchAgent can override .respond() to execute a web search before answering, while a child GuardrailAgent can override it to check for safety flags before returning text.

## Question 10
### What did you find interesting about method overriding today?
The most fascinating aspect is how it enables code to adapt dynamically without breaking templates. You can define a rigid, predictable architectural blueprint in your parent class, yet your child classes retain total creative freedom to reimplement specific rules exactly when they need to.
