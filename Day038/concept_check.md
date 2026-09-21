# Day 038 - Concept Check

1. **What is an Enum?**
   An Enum represents a fixed collection of named values.

2. **Which module provides Enum?**
```python
from enum import Enum
```

3. **How do you access an Enum member?**
```python
Status.PENDING
```

4. **How do you access the value of an Enum member?**
```python
Status.PENDING.value
```

5. **Can you loop through an Enum?**
   Yes.

6. **Can Enums be used with classes?**
   Yes. They can represent the state or configuration of an object.

7. **Why are Enums useful?**
   They provide clear, predictable, and predefined choices.

8. **Why are Enums useful in AI engineering?**
   They can represent agent states, task states, model states, document status, and other fixed choices.

### Key Takeaway
```text
Enum → predefined choices → predictable state
```