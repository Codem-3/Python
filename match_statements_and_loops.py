# Match Statements and Loops in Python
# This file demonstrates match statements (Python 3.10+) and various loop types

print("=== MATCH STATEMENTS AND LOOPS EXAMPLES ===\n")

# ========================================
# MATCH STATEMENTS (Python 3.10+)
# ========================================

print("1. BASIC MATCH STATEMENT EXAMPLES")
print("-" * 40)


def basic_match_example(value):
    """Demonstrate basic match statement"""
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Unknown number"


# Test basic match
for i in range(1, 5):
    result = basic_match_example(i)
    print(f"Match {i}: {result}")

print()

print("2. MATCH WITH PATTERNS")
print("-" * 40)


def pattern_match_example(data):
    """Demonstrate pattern matching"""
    match data:
        case [x, y, z]:
            return f"List with 3 elements: {x}, {y}, {z}"
        case [x, y]:
            return f"List with 2 elements: {x}, {y}"
        case [x]:
            return f"List with 1 element: {x}"
        case []:
            return "Empty list"
        case _:
            return f"Other data: {data}"


# Test pattern matching
test_cases = [[1, 2, 3], [1, 2], [1], [], "hello"]
for case in test_cases:
    result = pattern_match_example(case)
    print(f"Pattern match {case}: {result}")

print()

print("3. MATCH WITH GUARDS")
print("-" * 40)


def match_with_guards(value):
    """Demonstrate match with guards (conditions)"""
    match value:
        case x if x < 0:
            return f"{x} is negative"
        case x if x == 0:
            return f"{x} is zero"
        case x if x > 0 and x < 10:
            return f"{x} is a small positive number"
        case x if x >= 10:
            return f"{x} is a large positive number"
        case _:
            return "Unknown"


# Test guards
test_numbers = [-5, 0, 5, 15]
for num in test_numbers:
    result = match_with_guards(num)
    print(f"Guard match {num}: {result}")

print()

print("4. MATCH WITH CLASS PATTERNS")
print("-" * 40)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def match_class_pattern(point):
    """Demonstrate matching with class patterns"""
    match point:
        case Point(x=0, y=0):
            return "Origin point"
        case Point(x=0, y=y):
            return f"Point on Y-axis at y={y}"
        case Point(x=x, y=0):
            return f"Point on X-axis at x={x}"
        case Point(x=x, y=y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"


# Test class patterns
points = [Point(0, 0), Point(0, 5), Point(3, 0), Point(2, 3)]
for point in points:
    result = match_class_pattern(point)
    print(f"Class pattern match: {result}")

print()

# ========================================
# LOOPS
# ========================================

print("5. FOR LOOPS")
print("-" * 40)

print("5.1 Basic for loop with range:")
for i in range(5):
    print(f"  Iteration {i}")

print("\n5.2 For loop with list:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"  I like {fruit}")

print("\n5.3 For loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\n5.4 For loop with dictionary:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"  {key}: {value}")

print()

print("6. WHILE LOOPS")
print("-" * 40)

print("6.1 Basic while loop:")
count = 0
while count < 3:
    print(f"  Count is {count}")
    count += 1

print("\n6.2 While loop with break:")
number = 0
while True:
    if number >= 5:
        break
    print(f"  Number: {number}")
    number += 1

print("\n6.3 While loop with continue:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip 3
    print(f"  Processing {i}")

print()

print("7. NESTED LOOPS")
print("-" * 40)

print("7.1 Nested for loops (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")
    print()  # Empty line after each row

print("7.2 Nested loops with break:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"  Breaking at ({i}, {j})")
            break
        print(f"  ({i}, {j})")

print()

print("8. LOOP CONTROL STATEMENTS")
print("-" * 40)

print("8.1 Break statement:")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")

print("\n8.2 Continue statement:")
for i in range(5):
    if i == 2:
        print(f"  Skipping {i}")
        continue
    print(f"  Processing {i}")

print("\n8.3 Pass statement:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    else:
        print(f"  Not {i}")

print()

print("9. LIST COMPREHENSIONS")
print("-" * 40)

print("9.1 Basic list comprehension:")
squares = [x**2 for x in range(5)]
print(f"  Squares: {squares}")

print("\n9.2 List comprehension with condition:")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"  Even squares: {even_squares}")

print("\n9.3 Nested list comprehension:")
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"  Matrix: {matrix}")

print()

print("10. PRACTICAL EXAMPLES")
print("-" * 40)

print("10.1 Finding prime numbers:")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [num for num in range(2, 20) if is_prime(num)]
print(f"  Prime numbers up to 20: {primes}")

print("\n10.2 Word counter:")
text = "hello world hello python world"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"  Word count: {word_count}")

print("\n10.3 Interactive menu with match:")


def interactive_menu():
    while True:
        print("\n  Choose an option:")
        print("  1. Say hello")
        print("  2. Count to 3")
        print("  3. Exit")

        choice = input("  Enter your choice (1-3): ")

        match choice:
            case "1":
                print("  Hello, World!")
            case "2":
                for i in range(1, 4):
                    print(f"  {i}")
            case "3":
                print("  Goodbye!")
                break
            case _:
                print("  Invalid choice. Please try again.")


# Uncomment the line below to test the interactive menu
# interactive_menu()

print("\n=== END OF EXAMPLES ===")
