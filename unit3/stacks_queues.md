# Unit 3 – Stacks & Queues

---

## Stacks

- **Stacks follow LIFO (Last In, First Out)**.
- Common use cases:
  - Backtracking (e.g. DFS)
  - Reversing data
  - Expression evaluation
  - Recursive problem solving
- Python implementation: `list` + `append()` / `pop()`
  
```python
stack = []
stack.append("data")  # Push
stack.pop()           # Pop from top
```

Arrays and stacks are not the same.
- Stack: focus on the last index (top of stack).
- List: general-purpose storage.

Think of a stack of books – you remove from the top.

---

## Queues

- **Queues follow FIFO (First In, First Out)**.
- Common use cases:
    - Task scheduling
    - Breadth-First Search (BFS)
    - Implemented using collections.deque:

```python
from collections import deque

queue = deque()
queue.append("data")     # Enqueue
queue.popleft()          # Dequeue from front
```

---

## Stack vs Queue – Use Case Example

Valid Parentheses Problem:

Use a stack:
- You must check the most recent opening bracket against the next closing bracket.
- Stack gives you direct access to the last opened symbol.

A queue would not work:
- A queue processes in order of arrival.
- You can't match the last opened bracket with the next closing one using FIFO.