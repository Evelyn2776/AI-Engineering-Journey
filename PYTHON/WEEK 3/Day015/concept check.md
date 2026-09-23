# Day 015 - Concept Check

## Question 1
### What is JSON?
(JavaScript Object Notation.) A lightweight text format for storing and transporting data.

## Question 2
### Why is JSON useful in software engineering?
It is human-readable and easy to write, virtually every programming language supports it natively.

## Question 3
### What does json.load() do?
Reads JSON data directly from a file object, converts that data into a Python dictionary or list.

## Question 4
### What does json.dump() do?
Takes a Python object (like a dictionary), writes it directly into a file as JSON text.

## Question 5
### What does json.loads() do?
Parses a JSON-formatted string (the "s" stands for string), converts that string into a Python dictionary.

## Question 6
### What does json.dumps() do?
Takes a Python object, converts (serializes) it into a JSON-formatted string.

## Question 7
### What is the relationship between JSON and Python dictionaries?
They share almost identical syntax (key-value pairs).When JSON is decoded, a JSON object maps to a Python dict, while a JSON array maps to a Python list. There are other mappings too, such as JSON numbers → Python int/float.

## Question 8
### Why is JSON important when working with APIs?
It serves as the universal standard language for web traffic. Servers and clients use it to exchange structured data easily.

## Question 9
### What is the difference between a JSON file and a JSON string?
A file is stored on a hard drive (e.g., profile.json). A string lives temporarily in memory as plain text data.

## Question 10
### What did you find interesting about JSON today?
It is fascinating how the omission of a single "s" (load vs loads) completely changes whether Python looks for a file or a text string.