# Day 018 - Concept Check

## Question 1
### What does `if __name__ == "__main__":` do?
A script guard that ensures specific code only runs when the file is executed directly, not when imported.

## Question 2
### What is `__name__` in Python?
A built-in Python variable that holds the name of the current module or evaluates to "__main__".

## Question 3
### What happens when you run a Python file directly?
Python sets __name__ to "__main__" and executes every line of code in the file from top to bottom.

## Question 4
### What happens when you import that Python file into another file?
Python loads the module and sets its `__name__` to the module's name, such as `"greetings"`. The code inside `if __name__ == "__main__":` does not run because the module was imported rather than executed directly.

## Question 5
### Why is `if __name__ == "__main__":` useful?
It allows a file to serve dual purposes: it can be run as a standalone program or cleanly reused as an import.

## Question 6
### What is the difference between running a file and importing a file?
Running executes the script as the main entry point; importing loads its tools into another script without auto-running them.

## Question 7
### Why is this important when building larger applications?
It prevents code chaos by stopping imported files from accidentally running side effects, setups, or tests automatically.

## Question 8
### What did you find interesting about today's lesson?
It reveals Python's under-the-hood mechanics, turning scripts from simple one-off tools into clean, professional, reusable modules.
