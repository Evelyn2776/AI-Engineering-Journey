# Day 035 - Concept Check

1. **What is an iterator?**
   An object that produces values one at a time.

2. **What does `iter()` do?**
   It creates an iterator from an iterable.

3. **What does `next()` do?**
   It retrieves the next value from an iterator.

4. **What happens when an iterator has no more values?**
   Python raises `StopIteration`.

5. **What methods are required for a custom iterator?**
```python
__iter__()
__next__()
```

6. **What does `__iter__()` return in a custom iterator?**
   Usually `self`.

7. **How can a generator create an iterator?**
   By using the `yield` keyword.

8. **Why are iterators useful in AI engineering?**
   They allow data to be processed one item at a time, which is useful for large datasets, documents, RAG pipelines, and streaming data.

### Key Takeaway
```text
Iterable → Iterator → next() → Value
                         ↓
                  StopIteration
```
