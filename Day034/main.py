# Create a generator called numbers() that yields: Use next() to retrieve each value.
def numbers ():
    yield 1
    yield 2
    yield 3

result = numbers()

print(next(result))
print(next(result))
print(next(result))

# Use a for loop to print the values from your generator.
for number in numbers():
    print(number)

# Countdown
def countdown(number):
    while number > 0:
        yield number 
        number -= 1

for numbers in countdown(5):
    print(numbers)

# Even Numbers
def even_numnber(number):
    count = 2
    while count <= number:
        yield count
        count += 2

for numbers in even_numnber(10):
    print(numbers)

# Generator Expression
collection = [0, 1, 2, 3, 4]

numbers = (x * x for x in collection) 

for p in numbers:
    print(p)    

# AI Data Stream
def ai_messages():
    messages = [
        "Loading model...",
        "Processing prompt...",
        "Generating response...",
        "Response complete."
    ]

    for message in messages:
        yield message

for message in ai_messages():
    print(message)