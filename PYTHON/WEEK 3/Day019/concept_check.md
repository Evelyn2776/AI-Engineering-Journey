# Day 019 - Concept Check

## Question 1
### What is a Python package?
A Python package is a directory containing multiple Python modules (scripts) and a special file, usually __init__.py. It allows you to organize complex code into reusable, hierarchical folder structures that others can easily import.

## Question 2
### What is pip?
pip is the official package manager for Python. It allows you to download, install, update, and uninstall third-party libraries and dependencies from the Python Package Index (PyPI).

## Question 3
### What is a dependency?
A dependency is an external library or software package that your project relies on to function properly. For example, if your script uses pandas to analyze data, pandas is a dependency of your project.

## Question 4
### What is a virtual environment?
A virtual environment is an isolated directory that contains its own Python installation and independent set of packages. It acts as a sandbox, preventing your project's dependencies from interfering with other projects or the global system settings.

## Question 5
### Why are virtual environments useful?
They prevent dependency conflicts between different projects on the same machine. For instance, if Project A requires Django 3.2 and Project B requires Django 5.0, virtual environments allow both to run on the same computer without breaking each other.

## Question 6
### What command creates a virtual environment?
The standard command is python -m venv .venv. This uses Python's built-in venv module to create a hidden environment folder named .venv in your current working directory.

## Question 7
### How do you activate a virtual environment on Linux?
You activate it by running source .venv/bin/activate in your terminal. Once activated, your terminal prompt will change to show the environment's name, indicating that any Python or pip commands will now run inside that isolated space.

## Question 8
### What does requirements.txt contain?
It contains a plain-text list of all external packages and their specific versions used by the project. It allows other developers to instantly replicate your project setup by running the command pip install -r requirements.txt.

## Question 9
### Why shouldn't .venv normally be committed to Git?
The .venv folder is system-specific, massive in file size, and easily recreated. Committing it clutters your repository with thousands of unnecessary files that might not even work on another developer's operating system; sharing the requirements.txt file is the correct alternative.

## Question 10
### What did you find interesting about virtual environments?
What makes them fascinating is how lightweight they are despite providing total isolation. Instead of duplicating the entire Python codebase like a heavy Virtual Machine (VM), a virtual environment simply uses clever file pointers and environment variables to redirect where Python looks for packages.