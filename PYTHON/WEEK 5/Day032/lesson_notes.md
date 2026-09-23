# Day 032 - Lesson Notes

## Type Hints
Type hints specify the expected types of variables, function parameters, and return values.

### Basic Type Hints
```python
name: str = "Evelyn"
age: int = 23
height: float = 168.7
is_student: bool = False
```

### Function Type Hints
```python
def calculate_total(price: int, quantity: int) -> int:
    return price * quantity
```

### Collection Type Hints
```python
skills: list[str] = ["Python", "AI"]

scores: tuple[int, ...] = (50, 70, 30)

student: dict[str, int] = {
    "Age": 20,
    "Mark": 15
}
```

### Union Types
```python
name: str | list[str] = "Evelyn"
```
A union allows a value to have more than one possible type.

### AI Engineering Connection
Type hints make larger Python applications easier to understand, maintain, and debug. They are especially useful when building APIs, AI systems, and agents.
