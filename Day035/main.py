# Use next() to print all three values.
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Turn it into an iterator and print each character using next().
word = "Python"

words = iter(word)

print(next(words))
print(next(words))
print(next(words))
print(next(words))
print(next(words))
print(next(words))

# Use a for loop to print the values.
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Use try/except to handle the situation when next() is called after the iterator is exhausted.
try:
    numbers = [10, 20, 30]

    iterator = iter(numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator)) 
    print(next(iterator))

except StopIteration:
    print("Number exhausted!")

# Build Your Own Iterator
class count:

    def __init__(self, number):
        self.current = 1
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.current <= self.number:
            numbers = self.current
            self.current += 1
            return numbers

        raise StopIteration

numbers = count(5)

for number in numbers:
    print(number)
        
# AI Document Iterator
def document_iterator ():

    documents = [
        "Python basics",
        "Object oriented programming",
        "Regular expressions",
        "Type hints",
        "Decorators",
        "Generators"
    ]

    for document in documents:
        yield document

doc = document_iterator()

for document in doc:
    print(document)