# Day 040 - Journal

## Today I Learned
Today I learned about Poetry and how it can be used to manage Python projects and dependencies. I practiced:
* Creating a Poetry project
* Understanding `pyproject.toml`
* Adding dependencies
* Adding development dependencies
* Using `poetry.lock`
* Checking the Poetry environment
* Running Python through Poetry

## Problems I Faced
When I first ran:
```bash
poetry env info
```
Poetry could not find a `pyproject.toml` file.

## How I Solved It
I learned that Poetry commands need to be run from the project directory containing `pyproject.toml`.
After moving into the Poetry project directory, Poetry could recognize the project.

## AI Engineering Connection
AI projects often depend on many libraries.
Poetry can help manage these dependencies and make project environments more reproducible.

## Key Takeaway
Poetry provides a structured way to manage Python projects, dependencies, and environments.

## Tomorrow's Goal
Continue with the next Python engineering concept.
