# Day 034 - Concept Check

1. **What is a generator?**
   A function that produces values one at a time.

2. **What keyword creates a generator?**
   `yield`

3. **What does `next()` do?**
   Gets the next value from a generator.

4. **What happens when `yield` runs?**
   The function pauses and can continue later.

5. **What is a generator expression?**
```python
(x * x for x in range(5))
```

6. **Why are generators useful?**
   They save memory by producing values when needed.

### Key Takeaway
```text
yield → produce → pause → resume
```
