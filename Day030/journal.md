# Day 030

## Journal

### Imagine you are building an AI application that asks a user for information.

The user is expected to enter a number, but they might accidentally enter text instead.

### What could happen without exception handling?

Without exception handling, the program could crash when Python tries to convert invalid text into an integer.

For example:

```python
age = int("hello")
```

This would raise a `ValueError`.

### How could `try` and `except` improve the application?

I could place the conversion inside a `try` block and handle the `ValueError` with an `except` block.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
```

This allows the program to respond to invalid input instead of crashing immediately.

### Why is this important for AI applications?

AI applications often depend on external services such as APIs, databases, and AI models. These services can sometimes fail.

Exception handling allows the application to respond to errors in a controlled way and provide useful feedback to the user.

### Key takeaway

Exception handling makes programs more reliable.

I learned that:

```text
try     → attempt something
except  → handle an error
else    → run if successful
finally → always run
```

This is useful because real-world applications cannot assume that every operation will always succeed.
