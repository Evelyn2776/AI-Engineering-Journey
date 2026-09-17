# Day 035 - Journal

## Today I Learned
Today I learned how Python iterators work.

I practiced:

```python
iter()
next()
StopIteration
__iter__()
__next__()
```

I also built my own custom iterator and created a document iterator using `yield`.

## Problems I Faced

I initially created the AI document iterator as a normal function and tried to iterate over the function itself.

## How I Solved It

I used `yield` to make the function produce each document one at a time.

## AI Engineering Connection

Iterators can process large amounts of data one item at a time.

This is useful for document processing, RAG pipelines, API pagination, batch processing, and streaming data.

## Key Takeaway

Iterators allow Python programs to process values one at a time instead of requiring all values to be processed at once.

## Tomorrow's Goal

Learn Context Managers.
