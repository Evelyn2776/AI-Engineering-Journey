# What is a class?
A class is a blueprint, template, or structural roadmap used to create objects. It defines the characteristics (data) and behaviors (actions) that any object created from it will possess, acting as a custom user-defined data type.

# What is an object?
An object is a concrete, real-world instance created from a class blueprint. While a class is just a design on paper, an object is the actual entity that occupies memory and holds live data you can interact with.

# What does __init__() do?
The __init__() method is Python's constructor function, which runs automatically every time a new object is instantiated. Its job is to initialize the objectâ€™s starting state by assigning initial values to its internal variables.

# What does self represent?
The self keyword represents the specific, individual instance of the object currently being created or modified. It acts as an internal pointer, allowing an object to access its own attributes and methods without confusing them with other objects of the same class.

# What is an attribute?
An attribute is a variable stored inside an object that holds data or state characteristics. For example, if you have a User class, its attributes might be username, email_address, and account_age.

# What is a method?
A method is a function defined inside a class that dictates what actions an object can perform. Methods look and act like normal functions, but they are explicitly bound to an object and always require self as their first parameter.

# How do you create an object?
You create an object by calling the class name followed by parentheses, assigning it directly to a variable name.

# Can one class create multiple objects?
Yes, a single class can spawn an infinite number of unique objects. Just as an architectural blueprint can be used to build hundreds of distinct houses on a street, a single class can generate countless independent object instances in memory.

# Why is OOP useful in larger applications?
OOP provides structure, maintainability, and code reusability (modular design). As codebases grow, OOP allows developers to compartmentalize complex systems into isolated, self-contained objects, preventing a bug in one section from causing an uncontrollable chain reaction across the entire app.

# How could classes be useful in an AI application?
In AI engineering, classes are perfect for packaging complex states like conversation histories and API configurations. You can build an Agent class that maintains its own message thread history, tracks total token consumption, holds a private OpenAI client key, and exposes a .respond() method to run prompts seamlessly.
