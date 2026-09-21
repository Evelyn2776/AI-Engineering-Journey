# Day 037 - Lesson Notes

## Dataclasses
A dataclass is a special type of Python class designed to make storing structured data easier.

Dataclasses are created using the `@dataclass` decorator.
```python
from dataclasses import dataclass
```

### Basic Dataclass
```python
@dataclass
class Student:
    name: str
    age: int
    course: str
```
Python automatically creates an `__init__()` method.

```python
student = Student("Evelyn", 20, "Engineering")
```

### Default Values
Fields can have default values:

```python
@dataclass
class User:
    name: str
    age: int
    level: str = "Beginner"
```
Fields without defaults should come before fields with defaults.

### Dataclass Methods
Dataclasses can contain normal methods.

```python
@dataclass
class Student:
    name: str
    score: int

    def passed(self):
        return self.score >= 50
```

### Generated Features
Dataclasses can automatically provide useful methods such as:

```text
__init__()
__repr__()
__eq__()
```

### AI Engineering Connection
Dataclasses are useful for representing structured information such as:
* Users
* Documents
* Study records
* Model configurations
* API data
* AI agent state
* Evaluation results

### Key Takeaway
```text
@dataclass
      ↓
Less boilerplate
      ↓
Structured data
      ↓
Cleaner Python classes
```