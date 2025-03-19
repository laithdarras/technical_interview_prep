# Big O, Time & Space Complexity + Optimization

Understanding how efficient your code is in terms of **time (speed)** and **space (memory)**, is a core skill every software engineer needs. 
This guide includes my understanding of **Big O Notation**, code analysis, and optimizing solutions.

---

## What is Big O?
Big O notation describes **how efficiently a function performs** in terms of time and space as the input size grows.

### Time Complexity
How long your code takes to run.

### Space Complexity
How much memory your code uses.

---

## Common Complexities (Fastest to Slowest)

| Time/Space | Big O | Example |
|------------|-------|---------|
| Constant   | O(1)  | Access element by index, add to hash table |
| Logarithmic | O(log n) | Binary search in sorted array |
| Linear     | O(n)  | Iterate through a list |
| Log-linear | O(n log n) | Merge sort |
| Quadratic  | O(n^2) | Nested loops over an array |
| Exponential | O(2^n) | Brute force recursion like subsets |
| Factorial | O(n!) | Generating permutations like BOGO SORT WOOHOO |

---

## Code Examples

### 1. **Constant Time Example**
```python
def get_element_at_index(lst, idx):
    if idx < 0 or idx >= len(lst):
        return None
    return lst[idx]
```
- Time Complexity: **O(1)** - Direct access by index.
- Space Complexity: **O(1)** - Only a couple of variables used.

---

### 2. **Linear Time Example**
```python
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```
- Time: **O(n)** - Loop runs once per element.
- Space: **O(1)** - Only simple variables used.

---

### 3. **HashMap Example (Word Frequencies)**
```python
def count_word_frequencies(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
```
- Time: **O(n)** - Loop through all words once.
- Space: **O(n)** - One entry per unique word.

---

### 4. **Fixed Loop Count = Constant Time**
```python
def sum_top_100(arr):
    total = 0
    for i in range(100):
        total += arr[i]
    return total
```
- Time: **O(1)** — Loop always runs 100 times.
- Space: **O(1)**

---

## Optimization

### Use Efficient Data Structures
- **Hash Tables** (dict/set) for O(1) lookup
- **Two Pointers** to avoid nested loops

### Match the Pattern to the Right Tool
- **Sorted arrays?** -> Use **binary search**, **two pointers**
- **Dupes & counts?** -> Use **hash tables**

### Review Your Code
- Test edge cases
- Look for nested loops
- Reuse calculations

### Evaluate the Results
- Does it handle all cases?
- Could we modify in place?
- Any unneeded memory usage?

---

## Brute Force vs Optimized Example

### Brute Force (Nested Loops)
```python
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if arr[i] not in duplicates:
                    duplicates.append(arr[i])
    return duplicates
```
- Time: **O(n^2)**
- Space: **O(n)** (for result list)

---

### Optimized Version (Using Set)
```python
def find_duplicates_optimized(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.add(num)
    return duplicates
```
- Time: **O(n)** - One pass, all lookups are O(1)
- Space: **O(n)** - `seen` + `duplicates`

---

## UMPIRE

- **U - Understand**: What's the input/output? Any edge cases?
- **M - Match**: Choose right approach: Brute-force? Hash table? Sorting?
- **P - Plan**: Pseudocode and test ideas.
- **I - Implement**: Write clean and simple code.
- **R - Review**: Think through logic, check off-by-one errors.
- **E - Evaluate**: Does it work on big/small inputs? What's the time/space complexity?

---

### My Takeaways
- Big O is essential for making scalable apps
- Optimize only when necessary, don’t overcomplicate it. Simple > Complex as many Engineers told me
- Matching problem types to known patterns saves a lot of time
- Build the habit of evaluating code even if it "works"

---

> "Write code that not only works, but works **efficiently**."