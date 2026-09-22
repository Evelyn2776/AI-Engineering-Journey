# Day 040 - Lesson Notes

## Poetry
Poetry is a Python dependency and project-management tool. It helps manage:
* Project configuration
* Dependencies
* Development dependencies
* Virtual environments
* Dependency versions
* Project metadata

## pyproject.toml
Poetry uses `pyproject.toml` to store project configuration and dependency information.
Example:
```toml
[tool.poetry]
name = "poetry-ai-demo"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.34.2"

[tool.poetry.group.dev.dependencies]
pytest = "^9.1.1"
```

## Adding Dependencies
A project dependency can be added with:
```bash
poetry add requests
```
Development dependencies can be added with:
```bash
poetry add --group dev pytest
```

## poetry.lock
Poetry creates a `poetry.lock` file containing resolved dependency versions.
This helps make project environments reproducible.

## Installing Dependencies
```bash
poetry install
```
This installs the project's dependencies.

## Running Code
Python programs can be run through the Poetry environment:
```bash
poetry run python main.py
```

## Environment Information
Poetry can show information about the project's environment:
```bash
poetry env info
```
This command should be run from a directory containing `pyproject.toml`.

## AI Engineering Connection
Poetry is useful for AI projects because AI applications often have many dependencies.
For example:
* FastAPI
* Requests
* Pydantic
* AI SDKs
* Database libraries
* Testing tools
Poetry helps organize and reproduce these environments.

## Key Takeaway
Poetry
    ↓
Project configuration
    ↓
Dependencies
    ↓
Locked versions
    ↓
Reproducible Python projects