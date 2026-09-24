# Password Generator

A secure command-line password generator built with Python as part of my AI Engineering learning journey.

## Features

* Custom password length
* Uppercase letters
* Lowercase letters
* Numbers
* Symbols
* Secure random generation
* Input validation
* Error handling
* Automated testing

## Project Structure
```text
Project-02-Password-Generator/
├── password_generator.py
├── main.py
├── test_password_generator.py
└── README.md
```
* `password_generator.py` — Contains the password generation logic.
* `main.py` — Handles user input and the CLI interface.
* `test_password_generator.py` — Contains automated tests.
* `README.md` — Project documentation.

## Requirements
* Python 3.12+
* pytest

## Usage
Run the generator:

```bash
python main.py
```
Follow the prompts to choose the password length and character types.
Run the tests:

```bash
pytest
```

## Security
The project uses Python's `secrets` module for secure random password generation.

## What I Learned
This project helped me practice:
* Classes and methods
* Type hints
* Lists and strings
* List comprehensions
* Exception handling
* CLI application design
* Secure random generation
* Automated testing

## Future Improvements
* Password strength indicator
* Generate multiple passwords
* Copy password to clipboard
* Password history
* Improved CLI interface

## License
This project is part of my AI Engineering learning journey.
