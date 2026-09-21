# Day 038 - Journal

## Today I Learned
Today I learned about Python Enums and how to use them to represent fixed choices and states.
I practiced:

```python
Enum
.value
```
I also learned how to compare Enum members, loop through them, and use them with classes.

## Problems I Faced
I initially passed the Enum class itself to my `check_status()` function instead of passing an individual Enum member.

## How I Solved It
I learned the difference between:
```python
TaskStatus
```
and:
```python
TaskStatus.DONE
```
I then passed individual Enum members to the function.

## AI Engineering Connection
Enums can represent the different states of AI agents, tasks, models, and document-processing workflows.

## Key Takeaway
Enums make fixed choices and application states clearer and more predictable.

## Tomorrow's Goal
Continue with the next Python engineering concept.