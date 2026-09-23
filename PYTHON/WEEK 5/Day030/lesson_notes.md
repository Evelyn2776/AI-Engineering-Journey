# Day 030 - Lesson Notes

## Exception Handling

Exception handling allows a Python program to handle errors that happen while the program is running instead of crashing.

## What Is an Exception?

An exception is an error that occurs during program execution.

For example:

```python
age = int(input("Enter your age: "))
```

If the user enters `"hello"`, Python raises a `ValueError` because `"hello"` cannot be converted into an integer.

## try

The `try` block contains code that might cause an exception.

```python
try:
    age = int(input("Enter your age: "))
```

## except

The `except` block handles an exception if one occurs.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
```

Using a specific exception such as `ValueError` is better than using a general `except` because it makes the program more precise.

## else

The `else` block runs when no exception occurs.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
else:
    print(f"You are {age} years old.")
```

## finally

The `finally` block runs whether an exception occurs or not.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
else:
    print(f"You are {age} years old.")
finally:
    print("Program finished.")
```

## Common Exceptions

Some common Python exceptions include:

* `ValueError` — an inappropriate value was provided.
* `TypeError` — an operation was performed on an inappropriate type.
* `IndexError` — a list or sequence index does not exist.
* `KeyError` — a dictionary key does not exist.
* `ZeroDivisionError` — a number was divided by zero.

## Why Exception Handling Is Useful

Exception handling prevents programs from crashing when users provide invalid input or when unexpected problems occur.

It also allows programs to display useful error messages and continue running when appropriate.

## AI Engineering Connection

AI applications depend on many external components that can fail.

For example:

```text
User Input
    ↓
AI Application
    ↓
AI Model / API
    ↓
Database
    ↓
Response
```

An API request could fail, a database operation could produce an error, or a user could provide invalid input.

Exception handling allows the application to handle these situations gracefully.

## Key Idea

`try` = attempt the operation.

`except` = handle the error.

`else` = run when there is no error.

`finally` = run regardless of whether an error occurred.
