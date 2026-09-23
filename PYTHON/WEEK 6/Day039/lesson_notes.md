# Day 039 - Lesson Notes

## Logging
Logging is the process of recording events that happen inside a program.
Python provides logging through the built-in `logging` module.

## Why Logging?
Logging is useful for:
- Debugging
- Tracking application activity
- Detecting errors
- Monitoring applications
- Understanding what happened in production

## Basic Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Application started")
```

## Log Levels
Python provides several important logging levels:
```python 
DEBUG — detailed information for debugging
INFO — normal application events
WARNING — something unexpected
ERROR — an operation failed
CRITICAL — a serious failure
```

## Exception Logging
Logging can be used together with exception handling.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("An error occurred")
```
logging.exception() is especially useful inside an except block because it records the exception information.

## Logging AI Systems
AI applications can log events such as:
- Model loading
- Prompt received
- Model request
- Tool execution
- Response generation
- Errors

Example:
```python
logging.info("Received prompt")
logging.info("Generating AI response")
logging.info("Response generated")
```

## AI Engineering Connection
Logging becomes important when building:
- AI agents
- RAG systems
- APIs
- Automation systems
- Production AI applications
Logs help developers understand what an application is doing and diagnose failures.

## Key Takeaway
Logging
    ↓
Application events
    ↓
Debugging + Monitoring
    ↓
Reliable software