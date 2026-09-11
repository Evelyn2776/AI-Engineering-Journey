# Day 030 - Concept Check

## Question 1

### What is an exception?

An exception is an error that occurs while a Python program is running.

## Question 2

### Why is exception handling useful?

Exception handling allows a program to handle errors gracefully instead of crashing. It can provide useful feedback to the user and allow the program to continue when appropriate.

## Question 3

### What does `try` do?

The `try` block contains code that might cause an exception.

## Question 4

### What does `except` do?

The `except` block catches and handles an exception that occurs inside the `try` block.

## Question 5

### What is `ValueError`?

`ValueError` occurs when a function receives a value of the correct general type but the value is not appropriate.

For example:

```python
int("hello")
```

causes a `ValueError`.

## Question 6

### What does `else` do in exception handling?

The `else` block runs only when the code inside the `try` block completes successfully without raising an exception.

## Question 7

### What does `finally` do?

The `finally` block runs whether an exception occurs or not. It is useful for code that should always execute.

## Question 8

### Why is catching a specific exception better than using a general `except`?

Catching a specific exception makes the program more predictable and helps avoid accidentally hiding unrelated programming errors.

## Question 9

### How could exception handling be useful in an AI application?

It could handle problems such as invalid user input, failed API requests, database errors, or unavailable services without causing the entire application to crash.

## Question 10

### What did you learn from exception handling?

I learned that programs can anticipate certain errors and handle them using `try`, `except`, `else`, and `finally`. This makes applications more reliable and user-friendly.
