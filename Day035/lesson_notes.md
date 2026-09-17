# Day 035 - Lesson Notes

## Iterators
An iterator is an object that produces values one at a time.

### Creating an Iterator
Python's `iter()` converts an iterable into an iterator.

```python
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
```

### `next()`
`next()` retrieves the next value from an iterator.

```python
print(next(iterator))
```
When there are no more values, Python raises:

```python
StopIteration
```

### Custom Iterators
A custom iterator uses:
```python
__iter__()
__next__()
```
Example:
```python
class Count:

    def __init__(self, number):
        self.current = 1
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.number:
            value = self.current
            self.current += 1
            return value

        raise StopIteration
```

### Generators and Iterators
Generators are a convenient way to create iterators using `yield`.
```python
def document_iterator():
    documents = ["Python", "AI", "RAG"]

    for document in documents:
        yield document
```

### AI Engineering Connection
Iterators are useful for processing data one item at a time.
They can be useful in:

* Large datasets
* Document processing
* RAG pipelines
* API pagination
* Batch processing
* Streaming data

### Key Takeaway
```text
iter() → create iterator
next() → get next value
yield  → produce values lazily
StopIteration → iteration is finished
```
