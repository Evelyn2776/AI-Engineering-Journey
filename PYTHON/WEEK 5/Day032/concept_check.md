# Day 032 - Concept Check

1. **What are type hints?**
   They specify the expected types of data.

2. **How do you type a variable?**

```python
name: str = "Evelyn"
```

3. **How do you type a function parameter?**

```python
def greet(name: str):
```

4. **How do you specify a return type?**

```python
def add(a: int, b: int) -> int:
```

5. **What does `list[str]` mean?**
   A list containing strings.

6. **What does `tuple[int, ...]` mean?**
   A tuple containing any number of integers.

7. **What does `str | None` mean?**
   The value can be a string or `None`.

8. **Why are type hints useful in AI engineering?**
   They make code clearer, easier to maintain, and easier to debug.

### Key Takeaway
```text
variable: type
parameter: type
function(...) -> return_type
```
