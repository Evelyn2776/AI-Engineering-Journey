# Day 022 - Concept Check

## Question 1
### What is a pytest fixture?
A fixture is a special baseline function that sets up a fixed state or data context before a test runs. It provides a dependable, predictable environment or object that your test functions can consistently pull from. 

## Question 2
### What does @pytest.fixture do?
It is a Python decorator that flags an ordinary function as a reusable testing asset. When pytest scans your code, this decorator tells it to register the function's return value so it can be passed into individual test scripts on demand.

## Question 3
### Why are fixtures useful?
They eliminate repetitive setup code across your test files. Instead of manually instantiating objects, opening files, or cleaning data inside every single test function, you write that setup logic once inside a fixture and share it everywhere.

## Question 4
### How does a test receive a fixture?
A test receives a fixture by accepting the fixture's function name as an input argument. pytest automatically detects this argument matching, runs the fixture first, and passes the output directly into your test function.

## Question 5
### Why is reusable test data useful?
It ensures consistency across your test suite and reduces code maintenance. If your test data structure changes later, you only have to update it in one central location rather than hunting down and editing dozens of individual tests. 

## Question 6
### How could fixtures help when testing an AI application?
AI tests often require large, complex objects like mock LLM prompt templates, heavy text cleaning configurations, or sample JSON API payloads. Fixtures let you package these static datasets or mock API clients cleanly so your tests can instantly use them without cluttering the testing assertions. 

## Question 7
### What happens if a fixture is changed?
Any modification to a fixture instantly applies to every test that references it. This is highly efficient for updating shared structures, but you must be careful, as a breaking change in a core fixture can cause dozens of tests to fail simultaneously.

## Question 8
### What is the advantage of keeping test data separate from test logic?
It makes your test files significantly easier to read and scan. Your test functions can focus purely on verifying outcomes (the assertions) without being buried under hundreds of lines of raw text, sample dictionaries, or initialization boilerplate

## Question 9
### How are fixtures different from ordinary Python functions?
You never call a fixture explicitly using parentheses (like my_fixture()) in your code. Instead, pytest manages their execution lifecycle automatically behind the scenes, handling when they are built, injected, and torn down.

## Question 10
### What did you find interesting about today's lesson?
The most interesting part is dependency injectionâ€”how pytest dynamically links functions together based entirely on argument names. It turns test files into neat, modular Lego blocks where data flows smoothly into assertions without messy import strings or manual wiring.
