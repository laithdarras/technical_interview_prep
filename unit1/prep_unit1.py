# Unit 1 - Python Refresher

# ------------------
# Built-In Functions
# ------------------

# print(s): Prints the message s to the console
print("Welcome to TIP102!") # Output: Welcome to TIP102!

# len(s): Returns the length of a string or list
lst = ['a', 'b', 'c']
print(len(lst)) # Output: 3

s = "Laith Darras"
print(len(s)) # Output: 12

# range(start, stop, step): Generates a sequence of numbers
print(list(range(10))) # Output: [0, 1, 2, ..., 9]
print(list(range(5, 10))) # Output: [5, 6, 7, 8, 9]
print(list(range(2,11,2))) # Output: [2, 4, 6, 8, 10]

# sum(x): returns the sum of all numbers in a list
print(sum([1, 2, 3, 4])) # Output: 10

lst2 = [95, -5, 3]
print(sum(lst2)) # Output: 93

# min(x): Returns the smallest value
print(min([2,6,1,4,5,2])) # Output: 1
print(min(5,2,3)) # Output: 2

# max(x): Conversely, this returns the largest value
print(max([2,6,1,4,5,2])) # Output: 6
print(max(5,2,3)) # Output: 5

# ---------------------
# List Methods & Syntax
# ---------------------

# Append Method: Adds an item to the end of the list
lst3 = [1, 2, 4, 5]
print(lst3.append(8)) # Output: [1, 2, 4, 5, 8]

# Sort Method: Sorts the list in ascending order
unsorted_lst = [4, 3, 9, 1]
print(unsorted_lst.sort()) # Output: [1, 3, 4, 9]

# -----------------------
# String Methods & Syntax
# -----------------------

# lower(): Converts the string to lowercase
text = "San Jose, CA"
print(text.lower()) # Output: san jose, ca

# split(): Splits a string into a list based on a separator
sentence = "Python is fun"
print(sentence.split()) # Output: ['Python', 'is', 'fun']
hyphenated = "Python-is-fun"
print(hyphenated.split("-")) # Output: ['Python', 'is', 'fun']

# join(): Joins elements of an iterable into a string, using a specified separator
words = ['Python', 'is', 'fun']
print(' '.join(words)) # Output: Python is fun
print('-'.join(words)) # Output: Python-is-fun

# strip(): Removes whitespace or specified characters from both ends of the string
padded_string = "              Python is fun                 "
print(padded_string.strip()) # Output: Python is fun
questioned = "??????Python is fun???????"
print(questioned.strip("?")) # Output: Python is fun


# -------------
# Python Syntax
# -------------

# Variables: Python variables are dynamically types and typically use snake_case
var1 = 10 # Integer variable
var2 = "Python" # String variable
my_bool = True # Boolean variable
print(var1, var2, my_bool) # Output: 10 Python True

# Variables can change type dynamically
x = 10
print(x) # Output: 10
x = "Hello"
print(x) # Output: Hello


# Conditionals:
x = 3
if x > 1:
    print("x is greater than 1") # this line executes
if x > 5:
    print("x is greater than 5") # this line doesn't execute

# if-elif-else example:
x, y = 20, 20
if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
else:
    print("x and y are equal") # this line will execute only


# Functions:
def my_func():
    print("Python is fun")

my_func() # Output: Python is fun

def func_with_params(param1, param2):
    print(param1)
    print(param2)

func_with_params("Interview", "Prep") # Output: Interview 
                                      #         Prep

def add_nums(a, b):
    return a + b

print(add_nums(96,4)) # Output: 100


# Formatted Strings (f-strings):
name = "Laith"
print(f"Let's code, {name}!") # Output: Let's code, Laith!
a, b = 3, 5
print(f"The sum of {a} and {b} is {a+b}") # Output: The sum of 3 and 5 is 8

# Remainder Division:
print(5 % 2) # Output: 1
print(10 % 2) # Output: 0
print(3 % 11) # Output: 3

# -----------
# Loops
# -----------

# For Loop: Iterating over a list
fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
    print(fruit) # Output: apple
                 #         orange
                 #         banana

# For Loop with range:
for i in range(5):
    print(i) # Output: prints 0 through 4

# While Loop: Iterates as long as a condition is True
i = 1
while i < 6:
    print(i)    # Output: prints 1 through 5
    i += 1


# ---------------------------
# Comparing Strings and Lists
# ---------------------------

# Both strings and lists are ordered and indexable
s = "hello"
print(s[0]) # Output: h
lst = list(s)
lst[0] = "H"
print(lst) # Output: ['H', 'e', 'l', 'l', 'o']


# ---------------------------
# Advanced Concepts
# ---------------------------

# Enumerate: Iterate over both indices and values
my_str = "code"
for index, char in enumerate(my_str):
    print(f"Index {index} has character '{char}'")
# Output:
# Index 0 has character 'c'
# Index 1 has character 'o'
# Index 2 has character 'd'
# Index 3 has character 'e'

# Enumerate with a custom start:
cereals = ['cheerios', 'ctc', 'frosted flakes']
for count, cereal in enumerate(cereals, start=1):
    print(f"{count}: {cereal}")
# Output:
# 1: cheerios
# 2: ctc
# 3: frosted flakes

# Zip: Combine elements from multiple iterables into tuples
names = ['Alice', 'Bob', 'Angela']
ages = [25, 22, 21, 43]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old
# Bob is 22 years old
# Angela is 21 years old


# Nested Lists and Nested Loops:
albums = [
    ["Kendrick Lamar", "Good Kid, Maad City"],
    ["Drake", "If You're Reading This It's Too Late"],
    ["Dr. Dre", "2001"]
]
# Access a nested list
print(albums[0])    # Output: ['Kendrick Lamar', 'Good Kid, Maad City']
# Nested loop to print all album details
for album in albums:
    for detail in album:
        print(detail, end=" | ")
    print()
# Output:
# Kendrick Lamar | Good Kid, Maad City |
# Drake | If You're Reading This It's Too Late |
# Dr. Dre | 2001 |

# Nested Loops: Example with for and while loops
nums = [5, 10, 15]
for num in nums:
    print(f"Counting down from {num}")
    temp = num
    while temp >= 0:
        print(temp, end=" ")
        temp -= 1
    print("\n---")
# Output:
# Counting down from 5
# 5 4 3 2 1 0
# ---
# Counting down from 10
# 10 9 8 7 6 5 4 3 2 1 0
# ---
# Counting down from 15
# 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
# ---


# List Comprehensions:
nums = [1, 2, 3, 4, 5]
doubled = [value * 2 for value in nums]
print(doubled)  # Output: [2, 4, 6, 8, 10]

# List Comprehension with condition
words = ['I', 'love', 'programming']
result = [word for word in words if len(word) > 5]
print(result)   # Output: ['programming']


# Two-Pointer Technique
# Ex// Reverse a list using two pointers
def reverse_list(lst):
    left, right = 0, len(lst) -1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

lst9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse_list(lst9.copy()))    # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Same direction pointers: Merging two sorted lists
# Output: [1, 2, 3, 4, 5, 9]
def merge_sorted_lists(lst7, lst8):
    lst7.sort()
    lst8.sort()
    merged = []
    p1, p2 = 0, 0
    while p1 < len(lst7) and p2 < len(lst8):
        if lst7[p1] < lst8[p2]:
            merged.append(lst7[p1])
            p1 += 1
        else:
            merged.append(lst8[p2])
            p2 += 1
    merged.extend(lst7[p1:])
    merged.extend(lst8[p2:])
    return merged

print(merge_sorted_lists([4, 1, 2], [9, 3, 5]))

"""
When to use Two-Pointer Technique:
- Data Structure: commonly applied to strings, arrays, and linked lists
- Reducing Nested Loops: improved solutions that can be 'brute forced' using multiple for loops
- Searching for Pairs or Triplets: find pairs or triplets within a sorted array that satisfy certain conditions. ex// Two Sum
- In Place Operations: performing operations on a sequence in place, without creating an extra data structure to hold the result. ex// Removing Duplicates from a Sorted Array
- Comparing Opposite Ends of a Sequence: a problem that involves comparing or processing elements from both ends of a sequence. ex// Valid Palindrome
- Partitioning Problems: a problem requires dividing or partitioning the data into multiple parts. ex// Partitioning Array According to a Given Pivot
"""