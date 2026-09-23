# Day 036 - Journal

## Today I Learned
Today I learned about Python context managers and the `with` statement.
I practiced:

```python
with
__enter__()
__exit__()
```
I also built custom context managers and learned how `__exit__()` runs even when an exception occurs.

## Problems I Faced
I initially created the AI model manager with a `generate()` method that did not accept the prompt I passed to it.

## How I Solved It
I updated the method to accept a `prompt` parameter and cleaned up the duplicate class definition.

## AI Engineering Connection
Context managers can help AI applications safely manage resources such as model resources, databases, files, and network connections.

## Key Takeaway
Context managers provide a structured way to enter a resource, use it, and ensure cleanup when leaving the context.

## Tomorrow's Goal
Continue with the next Python engineering concept.
