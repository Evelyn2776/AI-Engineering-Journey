# Day 033 - Lesson Notes

## Decorators
A decorator is a function that adds or changes the behavior of another function without changing its original code.

### Basic Decorator
```python
def decorator(function):

    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper
```

Use it with:
```python
@decorator
def hello():
    print("Hello")
```

### Decorators With Arguments
```python
def decorator(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
```
`*args` and `**kwargs` allow decorators to work with different function arguments.

### Key Concepts
```text
function       → can be stored and passed around
nested function → function inside another function
decorator      → modifies function behavior
@decorator     → applies a decorator
```

### AI Engineering Connection
Decorators are useful for logging, authentication, timing, error handling, and tracking AI/API calls.
