# Day 034 - Lesson Notes

## Generators
Generators produce values one at a time using `yield`.

### Basic Generator
```python
def numbers():
    yield 1
    yield 2
    yield 3
```
Use `next()` to retrieve values:

```python
result = numbers()

print(next(result))
```

### `yield` vs `return`
```text
return → returns a value and ends the function
yield  → produces a value and pauses the function
```

### Generator Expression
```python
numbers = (x * x for x in range(5))
```
Parentheses create a generator expression.

### AI Engineering Connection
Generators are useful for large datasets, data pipelines, streaming, API responses, and processing AI data one item at a time.

### Key Takeaway
Generators are memory-efficient because they produce values only when needed.
