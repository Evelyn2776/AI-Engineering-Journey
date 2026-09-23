# Day 037 - Concept Check

1. **What is a dataclass?**
   A Python class designed to make storing structured data easier.

2. **What decorator creates a dataclass?**
```python
@dataclass
```

3. **What module provides `dataclass`?**
```python
from dataclasses import dataclass
```

4. **What does a dataclass automatically generate?**
   It can automatically generate methods such as `__init__()`, `__repr__()`, and `__eq__()`.

5. **Can dataclasses contain methods?**
   Yes.

6. **Can dataclass fields have default values?**
   Yes.

7. **What should you remember about fields with defaults?**
   Fields without defaults should come before fields with defaults.

8. **Why are dataclasses useful in AI engineering?**
   They provide a clean way to represent structured data such as documents, users, model configurations, and AI agent state.

### Key Takeaway
```text
@dataclass → structured data + less boilerplate
```