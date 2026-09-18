# Day 036 - Lesson Notes

## Context Managers
A context manager controls what happens when entering and leaving a block of code.

The `with` statement is commonly used with context managers.

### Basic Structure
```python
with resource:
    # code
```
A context manager commonly uses:
```python
__enter__()
__exit__()
```

### `__enter__()`
`__enter__()` runs when entering the `with` block.

```python
def __enter__(self):
    print("Starting")
    return self
```

### `__exit__()`
`__exit__()` runs when leaving the `with` block.

```python
def __exit__(self, exc_type, exc_value, traceback):
    print("Cleanup")
```
It also runs when an exception occurs inside the `with` block.

### Exception Information
`__exit__()` receives:

```text
exc_type    → exception type
exc_value   → exception value
traceback   → traceback information
```
If there is no exception, these are generally `None`.

### Context Manager Flow
```text
with
 ↓
__enter__()
 ↓
Run code
 ↓
__exit__()
```

### AI Engineering Connection
Context managers are useful for managing resources such as:
* Database connections
* Network connections
* Files
* Model resources
* Temporary resources
* Locks
They help ensure resources are properly cleaned up.

### Key Takeaway
```text
with → enter → use resource → exit → cleanup
```
