# ============================================
# PYTHON ALGORITHMS TUTORIAL
# ============================================
# This file covers different types of algorithms in Python
# with examples, implementations, and performance analysis

print("=" * 60)
print("PYTHON ALGORITHMS TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO ALGORITHMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO ALGORITHMS")
print("=" * 60)

print("\n1.1 What are Algorithms?")
print("-" * 30)
print(
    """
An algorithm is a step-by-step procedure to solve a problem.
It's like a recipe that tells you exactly what to do to achieve a goal.

Key characteristics:
- Input: Data the algorithm works with
- Output: Result the algorithm produces
- Definiteness: Each step is clear and unambiguous
- Finiteness: Algorithm must terminate
- Effectiveness: Each step must be doable

Types of algorithms:
1. Searching algorithms
2. Sorting algorithms
3. Recursive algorithms
4. Dynamic programming
5. Greedy algorithms
6. Divide and conquer
7. Backtracking algorithms
"""
)

print("\n1.2 Algorithm Complexity")
print("-" * 30)
print(
    """
Time Complexity: How long an algorithm takes to run
Space Complexity: How much memory an algorithm uses

Big O Notation:
- O(1): Constant time
- O(log n): Logarithmic time
- O(n): Linear time
- O(n log n): Linearithmic time
- O(n²): Quadratic time
- O(2ⁿ): Exponential time
- O(n!): Factorial time
"""
)

# ============================================
# SECTION 2: SEARCHING ALGORITHMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: SEARCHING ALGORITHMS")
print("=" * 60)

print("\n2.1 Linear Search")
print("-" * 30)


def linear_search(arr, target):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


# Test linear search
numbers = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(numbers, target)
print(f"Array: {numbers}")
print(f"Searching for: {target}")
print(f"Linear search result: {result}")

print("\n2.2 Binary Search")
print("-" * 30)


def binary_search(arr, target):
    """
    Binary Search Algorithm (requires sorted array)
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test binary search
sorted_numbers = sorted(numbers)
target = 34
result = binary_search(sorted_numbers, target)
print(f"Sorted array: {sorted_numbers}")
print(f"Searching for: {target}")
print(f"Binary search result: {result}")

print("\n2.3 Recursive Binary Search")
print("-" * 30)


def recursive_binary_search(arr, target, left=0, right=None):
    """
    Recursive Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)


# Test recursive binary search
result = recursive_binary_search(sorted_numbers, target)
print(f"Recursive binary search result: {result}")

# ============================================
# SECTION 3: SORTING ALGORITHMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: SORTING ALGORITHMS")
print("=" * 60)

print("\n3.1 Bubble Sort")
print("-" * 30)


def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Test bubble sort
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {unsorted}")
sorted_arr = bubble_sort(unsorted.copy())
print(f"Bubble sorted: {sorted_arr}")

print("\n3.2 Selection Sort")
print("-" * 30)


def selection_sort(arr):
    """
    Selection Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Test selection sort
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {unsorted}")
sorted_arr = selection_sort(unsorted.copy())
print(f"Selection sorted: {sorted_arr}")

print("\n3.3 Insertion Sort")
print("-" * 30)


def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Test insertion sort
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {unsorted}")
sorted_arr = insertion_sort(unsorted.copy())
print(f"Insertion sorted: {sorted_arr}")

print("\n3.4 Merge Sort")
print("-" * 30)


def merge_sort(arr):
    """
    Merge Sort Algorithm (Divide and Conquer)
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Test merge sort
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {unsorted}")
sorted_arr = merge_sort(unsorted.copy())
print(f"Merge sorted: {sorted_arr}")

print("\n3.5 Quick Sort")
print("-" * 30)


def quick_sort(arr):
    """
    Quick Sort Algorithm (Divide and Conquer)
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Test quick sort
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {unsorted}")
sorted_arr = quick_sort(unsorted.copy())
print(f"Quick sorted: {sorted_arr}")

# ============================================
# SECTION 4: RECURSIVE ALGORITHMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: RECURSIVE ALGORITHMS")
print("=" * 60)

print("\n4.1 Factorial")
print("-" * 30)


def factorial(n):
    """
    Recursive Factorial
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Test factorial
n = 5
print(f"Factorial of {n}: {factorial(n)}")

print("\n4.2 Fibonacci Sequence")
print("-" * 30)


def fibonacci(n):
    """
    Recursive Fibonacci
    Time Complexity: O(2ⁿ)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n, memo={}):
    """
    Memoized Fibonacci (Dynamic Programming)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Test fibonacci
n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}")
print(f"Memoized Fibonacci({n}) = {fibonacci_memo(n)}")

print("\n4.3 Tower of Hanoi")
print("-" * 30)


def tower_of_hanoi(n, source, auxiliary, target):
    """
    Tower of Hanoi Algorithm
    Time Complexity: O(2ⁿ)
    Space Complexity: O(n)
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Test tower of hanoi
print("Tower of Hanoi solution for 3 disks:")
tower_of_hanoi(3, "A", "B", "C")

print("\n4.4 Binary Tree Traversal")
print("-" * 30)


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def inorder_traversal(root):
    """Inorder traversal (Left -> Root -> Right)"""
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    """Preorder traversal (Root -> Left -> Right)"""
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    """Postorder traversal (Left -> Right -> Root)"""
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")


# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Binary Tree Traversals:")
print("Inorder:", end=" ")
inorder_traversal(root)
print("\nPreorder:", end=" ")
preorder_traversal(root)
print("\nPostorder:", end=" ")
postorder_traversal(root)
print()

# ============================================
# SECTION 5: DYNAMIC PROGRAMMING
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: DYNAMIC PROGRAMMING")
print("=" * 60)

print("\n5.1 Longest Common Subsequence")
print("-" * 30)


def longest_common_subsequence(text1, text2):
    """
    Longest Common Subsequence using Dynamic Programming
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Test LCS
text1 = "ABCDGH"
text2 = "AEDFHR"
result = longest_common_subsequence(text1, text2)
print(f"Text1: {text1}")
print(f"Text2: {text2}")
print(f"Longest Common Subsequence length: {result}")

print("\n5.2 Knapsack Problem")
print("-" * 30)


def knapsack(weights, values, capacity):
    """
    0/1 Knapsack Problem using Dynamic Programming
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Test knapsack
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 10
result = knapsack(weights, values, capacity)
print(f"Weights: {weights}")
print(f"Values: {values}")
print(f"Capacity: {capacity}")
print(f"Maximum value: {result}")

print("\n5.3 Coin Change Problem")
print("-" * 30)


def coin_change(coins, amount):
    """
    Coin Change Problem using Dynamic Programming
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


# Test coin change
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print(f"Coins: {coins}")
print(f"Amount: {amount}")
print(f"Minimum coins needed: {result}")

# ============================================
# SECTION 6: GREEDY ALGORITHMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: GREEDY ALGORITHMS")
print("=" * 60)

print("\n6.1 Activity Selection")
print("-" * 30)


def activity_selection(start, finish):
    """
    Activity Selection Problem (Greedy)
    Time Complexity: O(n log n) if not sorted
    Space Complexity: O(1)
    """
    n = len(start)
    selected = [0]  # First activity is always selected
    j = 0

    for i in range(1, n):
        if start[i] >= finish[j]:
            selected.append(i)
            j = i

    return selected


# Test activity selection
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
result = activity_selection(start, finish)
print(f"Start times: {start}")
print(f"Finish times: {finish}")
print(f"Selected activities: {result}")

print("\n6.2 Huffman Coding")
print("-" * 30)

import heapq


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(characters, frequencies):
    """
    Build Huffman Tree
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    heap = [HuffmanNode(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        internal = HuffmanNode(None, left.freq + right.freq)
        internal.left = left
        internal.right = right

        heapq.heappush(heap, internal)

    return heap[0]


def print_huffman_codes(root, code=""):
    """Print Huffman codes"""
    if root is None:
        return

    if root.char is not None:
        print(f"{root.char}: {code}")

    print_huffman_codes(root.left, code + "0")
    print_huffman_codes(root.right, code + "1")


# Test Huffman coding
characters = ["a", "b", "c", "d", "e"]
frequencies = [5, 9, 12, 13, 16]
print("Huffman Coding:")
print(f"Characters: {characters}")
print(f"Frequencies: {frequencies}")
root = build_huffman_tree(characters, frequencies)
print("Huffman Codes:")
print_huffman_codes(root)

# ============================================
# SECTION 7: GRAPH ALGORITHMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: GRAPH ALGORITHMS")
print("=" * 60)

print("\n7.1 Depth-First Search (DFS)")
print("-" * 30)


def dfs(graph, start, visited=None):
    """
    Depth-First Search
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Test DFS
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("DFS traversal starting from 'A':")
dfs(graph, "A")
print()

print("\n7.2 Breadth-First Search (BFS)")
print("-" * 30)

from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Test BFS
print("BFS traversal starting from 'A':")
bfs(graph, "A")
print()

print("\n7.3 Dijkstra's Shortest Path")
print("-" * 30)


def dijkstra(graph, start):
    """
    Dijkstra's Shortest Path Algorithm
    Time Complexity: O(V²) for simple implementation
    Space Complexity: O(V)
    """
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current)

        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


# Test Dijkstra
weighted_graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2},
}

print("Dijkstra's shortest paths from 'A':")
distances = dijkstra(weighted_graph, "A")
for vertex, distance in distances.items():
    print(f"To {vertex}: {distance}")

# ============================================
# SECTION 8: PERFORMANCE ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("SECTION 8: PERFORMANCE ANALYSIS")
print("=" * 60)

print("\n8.1 Algorithm Comparison")
print("-" * 30)

import time
import random


def measure_time(func, *args, iterations=1000):
    """Measure execution time of a function"""
    start_time = time.time()
    for _ in range(iterations):
        func(*args)
    end_time = time.time()
    return (end_time - start_time) / iterations


# Test sorting algorithms performance
sizes = [100, 500, 1000]
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
]

print("Sorting Algorithm Performance (seconds per operation):")
print(
    f"{'Size':<6} {'Bubble':<10} {'Selection':<10} {'Insertion':<10} {'Merge':<10} {'Quick':<10}"
)
print("-" * 60)

for size in sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    times = []

    for name, algorithm in algorithms:
        if size <= 1000 or name in ["Merge Sort", "Quick Sort"]:
            time_taken = measure_time(algorithm, arr.copy())
            times.append(f"{time_taken:.6f}")
        else:
            times.append("N/A")

    print(
        f"{size:<6} {times[0]:<10} {times[1]:<10} {times[2]:<10} {times[3]:<10} {times[4]:<10}"
    )

print("\n8.2 Space Complexity Analysis")
print("-" * 30)
print(
    """
Algorithm Space Complexity Analysis:

Sorting Algorithms:
- Bubble Sort: O(1) - In-place sorting
- Selection Sort: O(1) - In-place sorting
- Insertion Sort: O(1) - In-place sorting
- Merge Sort: O(n) - Requires extra space
- Quick Sort: O(log n) - Recursion stack

Searching Algorithms:
- Linear Search: O(1) - No extra space
- Binary Search: O(1) - No extra space
- Recursive Binary Search: O(log n) - Recursion stack

Dynamic Programming:
- Fibonacci (memoized): O(n) - Memoization table
- LCS: O(m * n) - DP table
- Knapsack: O(n * W) - DP table
"""
)

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    """
🎯 WHAT YOU'VE LEARNED:

1. SEARCHING ALGORITHMS
   - Linear Search: O(n) - Simple but slow for large datasets
   - Binary Search: O(log n) - Fast but requires sorted data
   - Recursive Binary Search: O(log n) - Elegant recursive approach

2. SORTING ALGORITHMS
   - Bubble Sort: O(n²) - Simple but inefficient
   - Selection Sort: O(n²) - Better than bubble sort
   - Insertion Sort: O(n²) - Good for small datasets
   - Merge Sort: O(n log n) - Stable and predictable
   - Quick Sort: O(n log n) - Fast in practice

3. RECURSIVE ALGORITHMS
   - Factorial: Simple recursion example
   - Fibonacci: Classic recursion with memoization
   - Tower of Hanoi: Complex recursive problem
   - Tree Traversals: Inorder, preorder, postorder

4. DYNAMIC PROGRAMMING
   - Longest Common Subsequence: String matching
   - Knapsack Problem: Optimization problem
   - Coin Change: Minimum coins problem
   - Memoization: Caching recursive results

5. GREEDY ALGORITHMS
   - Activity Selection: Scheduling problems
   - Huffman Coding: Data compression
   - Always choose locally optimal solution

6. GRAPH ALGORITHMS
   - DFS: Depth-first traversal
   - BFS: Breadth-first traversal
   - Dijkstra: Shortest path algorithm

7. PERFORMANCE ANALYSIS
   - Time complexity measurement
   - Space complexity analysis
   - Algorithm comparison

🚀 KEY TAKEAWAYS:
- Choose the right algorithm for your problem
- Understand time and space complexity
- Use recursion when it simplifies the solution
- Apply dynamic programming for overlapping subproblems
- Consider greedy approaches for optimization
- Always analyze performance for large datasets

To run this tutorial: python python_algorithms.py
"""
)

print("\nHappy coding with Python algorithms! 🐍⚡")
print("Remember: The right algorithm can make all the difference!")
