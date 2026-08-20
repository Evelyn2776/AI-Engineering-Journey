# Day 024 - Concept Check

## Question 1
### What is encapsulation?
Encapsulation is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class), while simultaneously restricting direct access to some of the object's internal components. It hides the internal complexity of an object and only exposes what is absolutely necessary.

## Question 2
### What is a public attribute?
A public attribute is a variable inside a class that can be accessed, modified, or deleted from anywhere outside the class. In Python, all attributes are public by default (e.g., self.name = "Bot"). 

## Question 3
### What does a single underscore before an attribute mean?
A single underscore (e.g., self._history) is a convention signaling a "protected" attribute. It tells other developers: "This is internal data; do not modify it directly outside this class." However, Python does not enforce this restriction structurally; it operates purely on an honor system. 

## Question 4
### What does a double underscore before an attribute mean?
A double underscore (e.g., self.__api_key) triggers name mangling, where Python structurally alters the attribute's internal name to _ClassName__attribute. This makes it much harder to accidentally access or overwrite the variable from outside the class, acting as a stricter "private" marker.

## Question 5
### Why is encapsulation useful?
It protects the internal state of an object from accidental corruption and creates cleaner boundaries in your code. By forcing developers to use dedicated methods (getters and setters) to change data, you can add validation checks to ensure bad data never breaks your application logic.

## Question 6
### What is the difference between an attribute and a method?
An attribute is a variable that holds data or state (e.g., self.token_count = 10), while a method is a function that executes actions or behaviors using that data (e.g., def calculate_cost(self):).

## Question 7
### Why might an AI application need to control access to its internal data?
AI applications manage highly sensitive and structural data, like raw API keys, chat message arrays, and token usage budgets. If external code directly modifies the chat history array out of order, it can corrupt the context window sent to the LLM, causing the model to hallucinate or crash.

## Question 8
### Is a double underscore a replacement for proper security?
No, absolutely not. Name mangling is simply a defensive programming tool to prevent developer accidents. Anyone can still bypass it if they know the mangled name formula (e.g., obj._MyClass__private_var). It does not encrypt data or protect it from malicious hackers.

## Question 9
### How could encapsulation be used in an AI chatbot?
You can encapsulate the __conversation_history list. Instead of allowing outside files to directly wipe or overwrite the list, you make it private. Outside files are forced to use a public method like .add_message(), which can automatically validate token limits before appending data.

## Question 10
### What did you find interesting about today's lesson?
The most interesting part is Python's community philosophy of "we are all consenting adults here." Instead of hard-locking private variables with rigid syntax keywords like Java or C++, Python uses visual cues like underscores to trust developers to respect data boundaries, keeping the language flexible yet clean. 
