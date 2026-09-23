# Lesson Notes - Day 019

## Python Packages
A structured directory containing multiple Python modules (scripts) and an __init__.py file. It organizes complex, multi-file codebases into reusable, hierarchical sub-folders.

## pip
The official package installer for Python. It connects to the Python Package Index (PyPI) to download and manage third-party libraries.

## Dependencies
: Third-party libraries that your primary application code relies on to work correctly. If Package A requires Package B to function, Package B is a dependency. pip automatically tracks and downloads these chained dependencies when you install a top-level package.

## Virtual Environments
An isolated directory containing its own independent copy of a Python interpreter and libraries. It acts as a sandbox to prevent code conflicts between different projects.

## Creating a Virtual Environment
: Handled by Python's built-in venv module. python -m venv .venv creates a hidden directory named .venv in your project folder. Generates local bin/ (or Scripts/ on Windows) and site-packages/ directories to store isolated tools.

## Activating a Virtual Environment
A terminal command that redirects your shell's focus to your private project folder. The name of your environment (.venv) will appear as a prefix at the start of your terminal line.
Linux/macOS Command: source .venv/bin/activate
Windows Command: .venv\Scripts\activate

## Installing Packages
Always activate your virtual environment first to avoid corrupting your global computer settings. Run pip install <package_name>.

## requirements.txt
A plain text blueprint containing a list of all your project's external packages and versions. Generated instantly using the command pip freeze > requirements.txt.

## .gitignore
A configuration file instructing Git which files and folders to completely ignore during version control. You must add .venv/ (or venv/) to this file. Virtual environments are massive, machine specific directories that break on other computers and should never be pushed to GitHub.

## Why Virtual Environments Matter in AI Engineering
Massive Library Chains: AI tools like transformers, torch, or tensorflow have hundreds of strict, complex sub-dependencies.
Hardware Configurations: Different machine learning models require highly specific, hyper-sensitive versions of CUDA or deep learning libraries.
Production Stability: A single mismatched library version can instantly break matrix calculations or GPU utilization in an AI system.
Portability: Virtual environments ensure your LLM application runs identically in your local terminal, a cloud Docker container, or an enterprise server.