# Day 040 - Concept Check

1. What is Poetry?
   Poetry is a Python dependency and project-management tool.

2. What file does Poetry use for project configuration?
   `pyproject.toml`

3. How do you add a dependency?
```bash
poetry add package_name
```

4. How do you add a development dependency?
```bash
poetry add --group dev package_name
```

5. What is `poetry.lock`?
   It records resolved dependency versions and helps make environments reproducible.

6. How do you install project dependencies?
```bash
poetry install
```

7. How do you run a Python program through Poetry?
```bash
poetry run python main.py
```

8. How do you inspect the Poetry environment?
```bash
poetry env info
```

9. Why are development dependencies useful?
   They contain tools needed during development, such as testing tools.

10. Why is Poetry useful for AI engineering?
    AI projects often contain many dependencies, and Poetry helps manage them in a structured and reproducible way.

## Key Takeaway
Poetry → dependency management → reproducible projects