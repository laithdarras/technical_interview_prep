# Unit 2 - Dictionaries

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