# Day 021 - Concept Check

## Question 1
### What is software testing?
Software testing is the programmatic process of verifying that an application works exactly as expected. It involves passing specific inputs into a piece of code and checking if the resulting output matches a predefined, correct result.

## Question 2
### Why is testing important?
It prevents bugs from reaching production, saves development time, and ensures code stability. When you modify or upgrade your application later, tests act as a safety net, instantly alerting you if your new changes accidentally broke existing features

## Question 3
### What does assert do in Python?
The assert keyword is a sanity check that verifies if a condition is True. If the expression following assert evaluates to True, Python quietly moves to the next line of code without doing anything.

## Question 4
### What happens when an assertion fails?
Python immediately halts program execution and raises an AssertionError exception. You can optionally append a custom error message after the condition (e.g., assert x == 5, "x should be 5"), which will print directly to the terminal when the crash occurs. 

## Question 5
### What is pytest?
pytest is a popular, third-party testing framework for Python. It simplifies writing, organizing, and running test suites, offering clean terminal readouts and advanced features like test discovery, fixtures, and detailed failure reports. 

## Question 6
### Why do test files often start with test_?
Frameworks like pytest rely on automatic test discovery rules. They scan your directories and automatically execute any file starting with test_ (or ending with _test), saving you from manually pointing the framework to each testing script.

## Question 7
### What is the difference between manually testing a program and automated testing?
Manually testing requires a human to repeatedly open the app, type inputs, and click buttons to see if it works, which is slow and prone to human error. Automated testing uses dedicated scripts to instantly run hundreds of checks in seconds, making it fast, precise, and infinitely repeatable.

## Question 8
### Why are automated tests useful in AI Engineering?
AI systems are inherently unpredictable due to probabilistic LLM outputs and data drift. Automated tests allow AI engineers to validate data preprocessing pipelines, check token limits, enforce strict JSON schema outputs, and run evaluation benchmarks to ensure model changes do not degrade application safety.

## Question 9
### What is a unit test?
A unit test is a highly focused test that checks the smallest isolated piece of code in an application, typically a single function or method. It isolates that function from external factors (like databases or APIs) to verify its logical accuracy independently. 

## Question 10
### What did you find interesting about testing today?
The most compelling aspect of testing is how it shifts your mindset from defensive coding to offensive verification. Writing code to intentionally break your own application highlights hidden edge casesâ€”like handling empty strings or None valuesâ€”before your users ever encounter them.