"""
Unit 2: Dictionaries and Sets - Study Reference

This file contains syntax explanations, usage examples, and key insights for technical interview prep.
Topics covered:
- Type casting and numerical operations
- Enumerate, zip
- Dictionary methods
- Set operations
- Advanced concepts: sorted, lambda, dictionary comprehensions, ternary
- Tuples
"""

# -------------------------------
# Type Casting
# -------------------------------
x = int(2.5)           # 2 (rounded down)
y = int("5")           # 5

a = float(2)           # 2.0
b = float("5")         # 5.0
c = float("5.3")       # 5.3

s1 = str(2)            # '2'
s2 = str([1, 2, 3])    # '[1, 2, 3]'

# -------------------------------
# Infinity Handling
# -------------------------------
positive_inf = float('inf')
negative_inf = float('-inf')

def get_min(lst):
    minimum = float('inf')
    for num in lst:
        if num < minimum:
            minimum = num
    return minimum
print(get_min([4,3,53,3]))  # 3

def safe_divide(a, b):
    if b == 0:
        return float('inf') if a > 0 else float('-inf')
    return a / b
print(safe_divide(4,0))     #: inf
print(safe_divide(-4,4))    #: -1.0

# -------------------------------
# Numeric Helpers
# -------------------------------
print(round(3.14159, 2))  # 3.14
print(round(3.14159))     # 3

print(abs(-5))            # 5
print(abs(-3.14))         # 3.14

# -------------------------------
# Enumerate & Zip
# -------------------------------
for i, char in enumerate("code"):
    print(i, char)  # 0 c , 1 o , 2 d , 3 e

cereals = ['cheerios', 'pebbles', 'puffs']
for i, cereal in enumerate(cereals, start=1):
    print(i, cereal)   # 1 cheerios , 2 pebbles , 3 puffs

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
print(dict(zip(names, ages)))  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# -------------------------------
# Dictionary Syntax & Methods
# -------------------------------
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4         # Add
d['a'] = 100       # Update

print(d['b'])      # Access
print(d.get('z'))  # None (standard error message)
print(d.get('z', 'Not Found'))  # 'Not Found' for specific error message

d.pop('a', None)   # Safe removal
print(d.keys())    # dict_keys(['b', 'c', 'd'])
print(d.values())  # dict_values([2, 3, 4])
print(d.items())   # dict_items([('b', 2), ('c', 3), ('d', 4)])


# -------------------------------
# Sets
# -------------------------------
my_set = {1, 2, 3}
my_set.add(4)      # Adds 4 to end of set
my_set.discard(5)  # No error
my_set.discard(5)  # Throws error
print(my_set)      # {1, 2, 3, 4}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # Union  {1, 2, 3, 4, 5}
print(a & b)   # Intersection   {3}
print(a - b)   # Difference    {1, 2}
print(a ^ b)   # Symmetric Difference  {1, 2, 4, 5}

# -------------------------------
# Advanced Concepts
# -------------------------------

# sorted()
print(sorted([3, 1, 2]))  # Ascending [1, 2, 3]
print(sorted([3, 1, 2], reverse=True))  # Descending  [3, 2, 1]

words = ["apple", "banana", "cherry"]
print(sorted(words, key=len))  # By length  ['apple', 'banana', 'cherry']

# lambda functions
add_10 = lambda x: x + 10
print(add_10(5))  # 15

sum_two = lambda a, b: a + b
print(sum_two(3, 4))  # 7

# Lambda inside sorted
print(sorted(words, key=lambda x: x[-1]))   # ['banana', 'apple', 'cherry']

# Ternary Operator
x, y = 10, 20
max_val = x if x > y else y
print("Max:", max_val)  # Max: 20

# Dictionary Comprehensions
nums = [1, 2, 3]
squares = {x: x**2 for x in nums}
print(squares)      # {1: 1, 2: 4, 3: 9}

pairs = [('a', 1), ('b', 2)]
d_from_pairs = {k: v for k, v in pairs}
print(d_from_pairs)     # {'a': 1, 'b': 2}

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)         # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# -------------------------------
# Tuples
# -------------------------------
t = ("Mario", "Luigi")
print(t[0])  # Mario

# Tuples are immutable
# t[0] = "Peach"  # TypeError

# -------------------------------
# Bonus: Helpful Imports
# -------------------------------
from collections import defaultdict, Counter

# defaultdict example
dd = defaultdict(int)
dd["apple"] += 1
print(dd)  # defaultdict(<class 'int'>, {'apple': 1})

# Counter example
count = Counter("banana")
print(count)  # Counter({'a': 3, 'n': 2, 'b': 1})