# Day 039 - Journal

## Today I Learned
Today I learned how to use Python's `logging` module.
I practiced:
- `logging.basicConfig()`
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL
- `logging.exception()`
I also learned how logging can be used to track AI application activity.

## Problems I Faced
Initially, I used `logging.basicConfig()` multiple times and expected each call to change the logging configuration.
I also initially tried to catch an `AssertionError` without actually raising one.

## How I Solved Them
I learned that the logging configuration should be set once at the beginning of the program.
I also learned that an exception must actually occur for an `except` block to execute.
I changed the example to deliberately trigger a `ZeroDivisionError` and used `logging.exception()` to record it.

## AI Engineering Connection
Logging can track events inside AI systems such as:
- Receiving prompts
- Loading models
- Generating responses
- Calling tools
- Handling errors
This will become especially useful when building AI agents and production applications.

## Key Takeaway
Logging helps developers understand what their applications are doing and makes debugging easier.

## Tomorrow's Goal
Continue with the next Python engineering concept.