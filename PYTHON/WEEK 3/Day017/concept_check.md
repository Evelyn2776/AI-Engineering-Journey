# Day 017 - Concept Check

## Question 1
### What is a POST request?
An HTTP method used to send data to a server to create or update a resource.

## Question 2
### What is the difference between GET and POST?
GET retrieves data from a server; POST sends data to a server.

## Question 3
### What does requests.post() do?
A Python method that sends a POST request with data to a specific URL.

## Question 4
### What does the json= parameter do?
An argument that automatically converts a Python dictionary into a JSON string for transmission.More precisely, requests takes the Python object supplied through json= and serializes it as JSON for the HTTP request.

## Question 5
### Why might an API return status code 201?
A standard web code meaning a new resource was successfully created on the server.

## Question 6
### Why is JSON useful when sending data to an API?
It is lightweight, organized, and easily read by different programming languages.

## Question 7
### What does response.json() do?
A Python method that converts the server's raw text response back into a usable dictionary.

## Question 8
### Why should POST requests use error handling?
It ensures your app handles network drops, bad inputs, or server failures without crashing.

## Question 9
### What is the difference between data sent to an API and data received from an API?
Sent data contains inputs or parameters; received data contains the server's results or confirmation.

## Question 10
### How could POST requests be useful in an AI application?
It allows your application to submit user prompts, audio, or images to an AI model for processing.