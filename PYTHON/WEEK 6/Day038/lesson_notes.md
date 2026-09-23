# Day 038 - Lesson Notes

## Enums
Enum stands for enumeration.
An Enum represents a fixed collection of named values.
Python provides Enums through the `enum` module:

```python
from enum import Enum
```

### Creating an Enum
```python
class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
```

### Accessing Enum Members
```python
Status.PENDING
```
To access the value:
```python
Status.PENDING.value
```

### Comparing Enum Members
Enum members can be compared directly:
```python
if status == TaskStatus.DONE:
    print("Task completed!")
```

### Looping Through an Enum
```python
for status in TaskStatus:
    print(status, status.value)
```

### Enums With Classes
Enums can represent the state of an object.
```python
class AgentStatus(Enum):
    IDLE = "idle"
    THINKING = "thinking"
    USING_TOOL = "using_tool"
    RESPONDING = "responding"
    ERROR = "error"
```
An AI agent can then change its state.

### AI Engineering Connection
Enums are useful for representing fixed choices and states such as:
* Agent states
* Task status
* Model status
* User roles
* Document status
* Message types

### Key Takeaway
```text
Enum
 ↓
Fixed named choices
 ↓
Predictable application state
```