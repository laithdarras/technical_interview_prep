"""
This script contains well-documented examples of:
- Stacks (LIFO) and their usage in reversing strings and checking valid parentheses.
- Queues (FIFO) using collections.deque, with examples like BFS traversal and task scheduling.
- Two-pointer technique (opposite direction and same direction pointers) with string reversal and merging sorted lists.
- Helper functions and Python syntax features, such as inner functions and multiple variable unpacking for swapping.

Each section includes functions with docstrings explaining the concepts and usage.
"""

# --- Stacks ---
# Stacks follow Last-In-First-Out (LIFO) order. In Python, a list can be used as a stack 
# by using append() to push and pop() to remove the last element.
# Common uses of stacks include backtracking algorithms, managing function calls (call stack),
# evaluating expressions (e.g., postfix notation), and balancing symbols (like parentheses).

def reverse_string_using_stack(s: str) -> str:
    """
    Reverses a given string using a stack.
    
    We push all characters of the string onto a stack, then pop them off.
    This returns the characters in reverse order due to LIFO behavior of stack.
    
    Args:
        s: The input string to reverse.
    Returns:
        The reversed string.
    """
    stack = []
    # Push all characters onto the stack
    for char in s:
        stack.append(char)
    # Pop all characters from the stack to get them in reverse order
    reversed_chars = []
    while stack:
        reversed_chars.append(stack.pop())
    return "".join(reversed_chars)

print(reverse_string_using_stack("Laith"))  # htiaL


def is_valid_parentheses(s: str) -> bool:
    """
    Checks if a string of brackets (parentheses, curly braces, square brackets) is valid.
    
    A string is valid if every opening bracket has a corresponding closing bracket in the correct order.
    This is solved using a stack:
    - Push opening brackets onto the stack.
    - When a closing bracket is encountered, check if it matches the top of stack.
    - If not, or if stack is empty when encountering a closing bracket, the string is invalid.
    - In the end, the stack should be empty for the string to be valid.
    
    Args:
        s: String consisting of characters '()', '[]', '{}'.
    Returns:
        True if the parentheses/brackets are balanced and properly nested, False otherwise.
    """
    stack = []
    # Mapping of closing to opening brackets
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in brackets:
            # char is a closing bracket
            if stack and stack[-1] == brackets[char]:
                stack.pop()  # pop the matching opening bracket
            else:
                return False  # not matching or stack is empty when a closing bracket appears
        else:
            # char is an opening bracket
            stack.append(char)
    return len(stack) == 0  # stack is empty so string must be valid

print(is_valid_parentheses("([{}])"))   # True

# Common applications of stacks include:
# - Backtracking (e.g., solving puzzles, DFS algorithm uses an implicit or explicit stack).
# - Recursion (the call stack behind the scenes).
# - Undo mechanisms in software (pushing states onto stack).
# - Parsing and evaluating expressions (using stacks to hold values/operators).

# --- Queues ---
# Queues follow First-In-First-Out (FIFO) order: the first element added is the first one removed.
# In Python, collections.deque is preferred for queue implementation because popleft() is O(1).
# Lists can function as queues with append() and pop(0), but popping from the start is O(n) and thus inefficient for large queues.
# Common uses of queues include breadth-first search (BFS) algorithms, scheduling tasks, and buffering data (like in breadth-first traversal of trees/graphs or task scheduling in operating systems).

from collections import deque

def bfs_traverse(graph: dict, start):
    """
    Performs Breadth-First Search (BFS) traversal on a graph from a starting node.
    
    BFS uses a queue to traverse nodes in layers:
    - Visit the starting node, then all of its neighbors, then neighbors of those neighbors, and so on.
    - We mark nodes as visited to avoid processing a node more than once.
    
    Args:
        graph: A dictionary representing an adjacency list of the graph (mapping node -> list of neighbors).
        start: The starting node for BFS traversal.
    Returns:
        A list of nodes in the order they were visited using BFS.
    
    Example:
        >>> graph = {
        ...    'A': ['B', 'C'],
        ...    'B': ['D', 'E'],
        ...    'C': ['F'],
        ...    'D': [],
        ...    'E': ['F'],
        ...    'F': []
        ... }
        >>> bfs_traverse(graph, 'A')
        ['A', 'B', 'C', 'D', 'E', 'F']
    """
    visited = set([start])      # keep track of visited nodes to avoid repeats
    queue = deque([start])      # initialize queue with the start node
    bfs_order = []              # return a list to store the order of traversal
    while queue:
        node = queue.popleft()  # dequeue the next node
        bfs_order.append(node)
        # enqueue all unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return bfs_order
my_graph = {
    'L': ['R', 'Z'],
    'R': ['Z'],
    'Z': []
}
print(bfs_traverse(my_graph, 'L'))      # ['L', 'R', 'Z']

def round_robin_schedule(tasks: list, time_slice: int):
    """
    Simulates a round-robin task scheduling in an operating system.
    
    Round-robin scheduling uses a queue to give each task a fixed time slice in order, cycling through tasks until all are complete.
    Each task is represented as a tuple (task_name, remaining_time).
    In each step, the task at front of the queue gets executed for 'time_slice' units or until completion.
    If the task finishes, it is not requeued; if it doesn't finish, it is enqueued again with updated remaining time.
    
    Args:
        tasks: List of tuples, where each tuple is (task_name, remaining_time).
        time_slice: An integer representing time units each task can use per round.
    Returns:
        A list representing the order in which tasks were executed. Completed tasks are marked as finished in the output.
    """
    queue = deque(tasks)
    execution_order = []
    while queue:
        task_name, remaining = queue.popleft()
        if remaining > time_slice:
            # Execute for one time slice and requeue the task with remaining time reduced
            execution_order.append(task_name)
            queue.append((task_name, remaining - time_slice))
        else:
            # Task can finish in this time slice
            execution_order.append(f"{task_name} (finished)")
            # (Do not requeue since it's finished)
    return execution_order
tasks = [("A", 5), ("B", 7), ("C", 4)]
print(round_robin_schedule(tasks, 3))       # ['A', 'B', 'C', 'A (finished)', B'', 'C (finished)', 'B (finished)']

# Explanation of FIFO:
# For a queue, the first element enqueued is the first one to be dequeued.
# Think of a line of people: the first person in line is served first. 
# BFS and round-robin scheduling both utilize this principle by processing items in the order they were added.

# --- Two-Pointer Technique ---
# The two-pointer technique involves using two indices (or pointers) to traverse a structure (like an array or list).
# This approach can be used in two main ways:
# 1. Opposite direction pointers (start from both ends and move towards the center).
#    - Useful for problems like checking palindromes, reversing sequences in place, or two-sum in sorted arrays.
# 2. Same direction pointers (one or both move from start to end, sometimes at different speeds).
#    - Useful for merging sorted lists, removing duplicates in-place, or detecting certain patterns (e.g., fast/slow pointer for cycle detection).

def reverse_list_in_place(lst: list) -> None:
    """
    Reverses a list in place using opposite-direction two-pointer technique.
    
    One pointer starts at the beginning (left index) and another at the end (right index).
    They move towards each other, swapping elements until they meet or cross.
    This operates in-place, modifying the original list.
    
    Args:
        lst: The list of elements to reverse. The list is modified in place.
    Returns:
        None. (The list `lst` is modified to be in reversed order.)
    
    Example:
        >>> data = [1, 2, 3, 4, 5]
        >>> reverse_list_in_place(data)
        >>> data
        [5, 4, 3, 2, 1]
    """
    left = 0
    right = len(lst) - 1
    while left < right:
        # swap the elements at left and right pointers
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    # Note: The function doesn't return anything because it modifies the list in place.

def merge_sorted_lists(a: list, b: list) -> list:
    """
    Merges two sorted lists into one sorted list using two pointers moving in the same direction.
    
    Both input lists `a` and `b` are assumed to be sorted. We use two indices (pointers) i and j for lists `a` and `b`:
    - Compare elements at these pointers and append the smaller one to the result list, then move that pointer forward.
    - Continue until one list is empty, then append the remainder of the other list.
    This runs in O(n+m) time, where n and m are lengths of `a` and `b`, respectively.
    
    Args:
        a: First sorted list.
        b: Second sorted list.
    Returns:
        A new list containing all elements from `a` and `b` in sorted order.
    
    Example:
        >>> merge_sorted_lists([1,3,5], [2,4,6])
        [1, 2, 3, 4, 5, 6]
    """
    i, j = 0, 0
    merged = []
    # Traverse both lists with two pointers
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # Append any remaining elements from list a or b (only one of these will have elements left)
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])
    return merged

list1 = [2, 4, 6]
list2 = [2, 3, 8]
print(merge_sorted_lists(list1, list2))     # [2, 2, 3, 4, 6, 8]

# Indicators for using two-pointer approach:
# - The problem involves searching for pairs or segments (e.g., two numbers in a sorted array that add up to a target which is TwoSum).
# - The problem can be simplified by moving pointers inward or forward instead of nested loops.
# - You need to perform in-place operations that look at elements from both ends or track a current and next element.
# Examples include: finding a pair with a given sum in a sorted array, partitioning arrays (like quicksort), and checking palindrome strings.

# --- Helper Functions & Python Syntax ---
# Inner functions (nested functions):
# In Python, you can define a function inside another function. These inner functions are useful for:
# - Encapsulating helper logic that is only relevant inside the outer function (keeping the global namespace clean).
# - Creating closures (functions that retain access to the outer function's variables even after the outer function has finished execution).
# Inner functions can improve modularity and readability by logically grouping functionality.

def factorial_with_inner_function(n: int) -> int:
    """
    Calculates the factorial of n using an inner recursive function.
    
    An inner function `inner_factorial` is defined to perform the recursion. This inner function is not accessible outside `factorial_with_inner_function`, 
    which helps encapsulate the recursion logic. This demonstrates how inner functions support modular programming by keeping helper logic self-contained.
    
    Args:
        n: Non-negative integer to calculate factorial of.
    Returns:
        The factorial of n.
    
    Example:
        >>> factorial_with_inner_function(5)
        120
    """
    def inner_factorial(x: int) -> int:
        # Inner recursive function for factorial.
        if x <= 1:
            return 1
        return x * inner_factorial(x - 1)
    
    return inner_factorial(n)
print(factorial_with_inner_function(6))     # 720


def make_multiplier(factor: int):
    """
    Returns a function that multiplies its input by a given factor.
    
    This is an example of a closure using an inner function. The inner function `multiply` captures the `factor` from the enclosing scope.
    When we call `make_multiplier`, it returns the inner `multiply` function which remembers the factor provided.
    This can be used to create specialized functions (e.g., double = make_multiplier(2) creates a function to double numbers).
    
    Args:
        factor: The multiplication factor to use in the returned function.
    Returns:
        A function that takes one argument and returns that argument multiplied by `factor`.
    
    Example:
        >>> double = make_multiplier(2)
        >>> double(5)
        10
    """
    def multiply(x: int) -> int:
        return x * factor
    return multiply

double = make_multiplier(2)
print(double(10))   # 20

# Unpacking multiple variables:
# Python allows swapping variables without a temporary variable using tuple unpacking.
# This makes code more concise and is a Pythonic way to swap values or assign multiple variables at once.
# Example:
#    a = 1
#    b = 2
#    a, b = b, a    # Now a is 2, b is 1

def swap_values(a, b):
    """
    Swaps two values using Python's multiple assignment (tuple unpacking).
    
    In Python, you can swap two variables in one line without using a temporary variable:
    a, b = b, a
    This works by packing the right-hand side into a tuple and then unpacking it into the left-hand side variables.
    
    Args:
        a: First value.
        b: Second value.
    Returns:
        A tuple (new_a, new_b) where new_a is the original b and new_b is the original a.
    """
    a, b = b, a
    return a, b

a, b = 4, 5
print(swap_values(a, b))    # (5, 4)