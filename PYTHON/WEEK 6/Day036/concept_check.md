# Day 036 - Concept Check

1. **What is a context manager?**
   An object that manages entering and leaving a block of code.

2. **What keyword is commonly used with context managers?**
   `with`

3. **What does `__enter__()` do?**
   It runs when entering the context.

4. **What does `__exit__()` do?**
   It runs when leaving the context and handles cleanup.

5. **What happens to `__exit__()` when an exception occurs?**
   It is still called.

6. **What are the three parameters of `__exit__()`?**
```python
exc_type
exc_value
traceback
```

7. **Why does `__enter__()` sometimes return `self`?**
   So the object can be assigned with `as` and used inside the context.

8. **Why are context managers useful in AI engineering?**
   They help safely manage resources such as databases, network connections, files, and model resources.

### Key Takeaway
```text
with
 ↓
__enter__()
 ↓
code
 ↓
__exit__()
```
