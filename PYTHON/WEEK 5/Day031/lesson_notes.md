# Day 031 - Lesson Notes

## Regular Expressions (Regex)

Regex is used to search, extract, and replace patterns in text.
Python uses the `re` module:
```python
import re
```
### Main Functions

```python
re.findall()  # Find all matches
re.search()   # Find the first match
re.sub()      # Replace matches
```
### Common Patterns

```text
\d    → digit
\d+   → one or more digits
\w    → word character
[A-Z] → uppercase letter
^     → beginning
$     → end
(...)  → capturing group
```
### Capturing Groups

```python
result = re.search(r"Name: (\w+), Age: (\d+)", text)

result.group(1)
result.group(2)
```
Groups allow us to extract specific information from text.

### AI Engineering Connection
Regex can help with text cleaning, validation, pattern detection, and extracting information before processing data with AI systems.
