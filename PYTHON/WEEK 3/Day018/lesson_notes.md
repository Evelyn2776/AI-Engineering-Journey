# Lesson Notes - Day 018

## __name__
A built-in Python variable that automatically tracks how the current script is being executed.

## __main__
The specific value assigned to __name__ when a script is executed directly by the user.

## Running a Python file
Executing a script directly, which tells Python to set __name__ to "__main__" and run all code inside it.

## Importing a Python file
Loading a script's functions or classes into another file, which sets its __name__ to the file's actual name instead of "__main__".

## if __name__ == "__main__"
A code guard that ensures the block below it only runs when the file is executed directly, preventing it from running during imports.

## Why this matters in software engineering
It prevents code chaos by allowing you to test, share, and reuse scripts across large applications without accidentally triggering unwanted code or side effects.