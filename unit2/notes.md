# Unit 2 - Dictionaries & Sets

# Time Management Reflection

## Challenge:
Balancing academics and other responsibilities can lead to neglecting certain tasks due to lack of time.

## Solution:
- Prioritize tasks
- Use a calendar to schedule time blocks
- Maintain a running to-do list
- Minimize distractions during focus time
- Review and adjust  routine weekly

# Dictionaries (Hash Maps)

Dictionaries store **key-value pairs** and offer **O(1)** average lookup and update times.

## Use Cases:
- Fast lookups and updates
- Frequency maps (counting items)
- Data mapping (phonebooks, config settings)
- Associating lists or other structures to keys

## Dictionary Properties:
- Keys must be unique
- Values can be any data type (strings, numbers, lists, dictionaries, etc.)
- Dictionaries are not meant for sorting — use `.items()` and `sorted()` when needed

---

## Example: Word Frequency Counter

### Problem:
Write a function that takes a list of words and returns a dictionary of word counts.

### Input:
```python
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'Apple']
```

### Output:
```python
{'apple': 3, 'banana': 2, 'orange': 1}
```

### Understanding Phase: 
- Is it case sensitive? → No, treat 'apple' and 'Apple' the same

### Planning Phase:
- Convert words to lowercase
- Initialize an empty dictionary
- Loop through the list
- Use .get() or if-else to track word 

### Inplemetation:
```python
def frequency(words):
    hashMap = {}
    for word in words:
        word = word.lower()
        hashMap[word] = hashMap.get(word, 0) + 1
    return hashMap
```

```python
# Alternative version using if-else
def frequency(words):
    hashMap = {}
    for word in words:
        word = word.lower()
        if word in hashMap:
            hashMap[word] += 1
        else:
            hashMap[word] = 1
    return hashMap
```

#### Both solutions have O(n) time complexity


---

# Sets

Sets are **unordered collections of unique elements**. They are powerful for fast lookup times and set operations.

## Use Cases:
- Removing duplicates
- Checking existence of a value
- Performing set math (union, intersection, difference, symmetric difference)

## Properties:
- Unordered
- Mutable
- No duplicates
- Fast access: **O(1)** average lookup time

---

## When to Use:

| Goal                                | Best Structure |
|-------------------------------------|----------------|
| Maintain order                      | List           |
| Key-value mapping                   | Dictionary     |
| Enforce uniqueness + fast lookup    | Set            |

---

# Using AI Tools (Intelligently)

AI is a great companion when used as a **thinking partner**, not a crutch.

---

## Ways I Use AI:
- Start with a **brute-force solution**, then use AI to suggest optimizations
- Use it to **unblock myself**, not to hand me full answers
- Generate **mock interview questions** (technical + behavioral)
- Break down logic or improve clarity
- Help evaluate **time/space complexity**

---

## Example Workflow:
1. Solve on your own → explain your logic
2. Ask AI: "How can I optimize this?"
3. Use AI's feedback to build intuition, not just copy it

---

## Be Careful:
- AI can give wrong answers at times
- Always verify logic and edge cases
- Think critically before accepting suggestions

Use it like an interviewer — someone who nudges you, not someone who codes for you.