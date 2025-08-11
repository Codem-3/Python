# ============================================
# PYTHON DATA STRUCTURES TUTORIAL
# ============================================
# This file covers Lists, Tuples, Sets, and Dictionaries
# with comprehensive examples and iteration methods

print("=" * 60)
print("PYTHON DATA STRUCTURES TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: LISTS
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: LISTS")
print("=" * 60)

print("\n1.1 Creating Lists")
print("-" * 30)
# Different ways to create lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
list_from_range = list(range(5))
list_from_string = list("Python")

print(f"Empty list: {empty_list}")
print(f"Numbers list: {numbers}")
print(f"Fruits list: {fruits}")
print(f"Mixed list: {mixed}")
print(f"List from range: {list_from_range}")
print(f"List from string: {list_from_string}")

print("\n1.2 List Indexing and Slicing")
print("-" * 30)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f"Original list: {numbers}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Second to last: {numbers[-2]}")
print(f"Slice [2:5]: {numbers[2:5]}")
print(f"Slice [:3]: {numbers[:3]}")
print(f"Slice [7:]: {numbers[7:]}")
print(f"Slice [::2]: {numbers[::2]}")  # Every second element
print(f"Slice [::-1]: {numbers[::-1]}")  # Reverse

print("\n1.3 List Methods")
print("-" * 30)
fruits = ["apple", "banana"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "grape")
print(f"After insert at index 1: {fruits}")

fruits.extend(["mango", "kiwi"])
print(f"After extend: {fruits}")

# Removing elements
removed_fruit = fruits.pop()
print(f"Popped element: {removed_fruit}")
print(f"After pop: {fruits}")

fruits.remove("banana")
print(f"After remove 'banana': {fruits}")

# Other methods
fruits.sort()
print(f"After sort: {fruits}")

fruits.reverse()
print(f"After reverse: {fruits}")

count = fruits.count("apple")
print(f"Count of 'apple': {count}")

index = fruits.index("grape")
print(f"Index of 'grape': {index}")

print("\n1.4 List Comprehensions")
print("-" * 30)
# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(f"Traditional squares: {squares}")

# List comprehension
squares_comp = [i**2 for i in range(1, 6)]
print(f"List comprehension squares: {squares_comp}")

# With condition
even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i + j for j in range(3)] for i in range(3)]
print(f"3x3 matrix: {matrix}")

print("\n1.5 List Iteration Methods")
print("-" * 30)
colors = ["red", "green", "blue", "yellow"]

print("1. Direct iteration:")
for color in colors:
    print(f"  Color: {color}")

print("\n2. With index using enumerate:")
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

print("\n3. With range:")
for i in range(len(colors)):
    print(f"  Index {i}: {colors[i]}")

print("\n4. While loop:")
i = 0
while i < len(colors):
    print(f"  Index {i}: {colors[i]}")
    i += 1

print("\n5. List comprehension with iteration:")
color_lengths = [len(color) for color in colors]
print(f"Color lengths: {color_lengths}")

# ============================================
# SECTION 2: TUPLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: TUPLES")
print("=" * 60)

print("\n2.1 Creating Tuples")
print("-" * 30)
# Different ways to create tuples
empty_tuple = ()
single_element = (42,)  # Note the comma
coordinates = (10, 20)
rgb_color = (255, 128, 0)
person = ("John", 30, "New York")
tuple_from_list = tuple([1, 2, 3])

print(f"Empty tuple: {empty_tuple}")
print(f"Single element: {single_element}")
print(f"Coordinates: {coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Person info: {person}")
print(f"Tuple from list: {tuple_from_list}")

print("\n2.2 Tuple Properties")
print("-" * 30)
coordinates = (10, 20, 30)
print(f"Tuple: {coordinates}")
print(f"Type: {type(coordinates)}")
print(f"Length: {len(coordinates)}")
print(f"First element: {coordinates[0]}")
print(f"Last element: {coordinates[-1]}")
print(f"Slice [1:]: {coordinates[1:]}")

# Tuples are immutable
try:
    coordinates[0] = 100
except TypeError as e:
    print(f"Error: {e}")

print("\n2.3 Tuple Methods")
print("-" * 30)
numbers = (1, 2, 2, 3, 2, 4, 5)
print(f"Tuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

print("\n2.4 Tuple Unpacking")
print("-" * 30)
# Basic unpacking
x, y = (10, 20)
print(f"Unpacked: x={x}, y={y}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# Swapping variables
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

print("\n2.5 Tuple Iteration")
print("-" * 30)
coordinates = [(1, 2), (3, 4), (5, 6)]

print("1. Direct iteration:")
for coord in coordinates:
    print(f"  Coordinate: {coord}")

print("\n2. Unpacking in loop:")
for x, y in coordinates:
    print(f"  x={x}, y={y}")

print("\n3. With enumerate:")
for i, (x, y) in enumerate(coordinates):
    print(f"  Point {i}: ({x}, {y})")

# ============================================
# SECTION 3: SETS
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: SETS")
print("=" * 60)

print("\n3.1 Creating Sets")
print("-" * 30)
# Different ways to create sets
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "orange"}
set_from_list = set([1, 2, 2, 3, 3, 4])  # Duplicates removed
set_from_string = set("hello")  # Unique characters

print(f"Empty set: {empty_set}")
print(f"Numbers set: {numbers_set}")
print(f"Fruits set: {fruits_set}")
print(f"Set from list (duplicates removed): {set_from_list}")
print(f"Set from string: {set_from_string}")

print("\n3.2 Set Properties")
print("-" * 30)
numbers = {1, 2, 3, 4, 5}
print(f"Set: {numbers}")
print(f"Type: {type(numbers)}")
print(f"Length: {len(numbers)}")
print(f"Contains 3: {3 in numbers}")
print(f"Contains 10: {10 in numbers}")

# Sets are mutable but elements must be immutable
numbers.add(6)
print(f"After adding 6: {numbers}")

numbers.remove(1)
print(f"After removing 1: {numbers}")

print("\n3.3 Set Operations")
print("-" * 30)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union
union = set1 | set2
print(f"Union (|): {union}")

# Intersection
intersection = set1 & set2
print(f"Intersection (&): {intersection}")

# Difference
difference = set1 - set2
print(f"Difference (-): {difference}")

# Symmetric difference
symmetric_diff = set1 ^ set2
print(f"Symmetric difference (^): {symmetric_diff}")

print("\n3.4 Set Methods")
print("-" * 30)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Adding elements
set1.add(4)
print(f"After add(4): {set1}")

set1.update([5, 6, 7])
print(f"After update([5, 6, 7]): {set1}")

# Removing elements
set1.discard(1)  # No error if element doesn't exist
print(f"After discard(1): {set1}")

set1.remove(2)  # Raises error if element doesn't exist
print(f"After remove(2): {set1}")

popped = set1.pop()
print(f"Popped element: {popped}")
print(f"After pop: {set1}")

set1.clear()
print(f"After clear: {set1}")

print("\n3.5 Set Iteration")
print("-" * 30)
fruits = {"apple", "banana", "orange", "grape"}

print("1. Direct iteration:")
for fruit in fruits:
    print(f"  Fruit: {fruit}")

print("\n2. With enumerate:")
for i, fruit in enumerate(fruits):
    print(f"  Fruit {i}: {fruit}")

print("\n3. Set comprehension:")
fruit_lengths = {len(fruit) for fruit in fruits}
print(f"Fruit lengths: {fruit_lengths}")

# ============================================
# SECTION 4: DICTIONARIES
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: DICTIONARIES")
print("=" * 60)

print("\n4.1 Creating Dictionaries")
print("-" * 30)
# Different ways to create dictionaries
empty_dict = {}
person = {"name": "John", "age": 30, "city": "New York"}
scores = dict(Alice=85, Bob=92, Charlie=78)
dict_from_list = dict([("a", 1), ("b", 2), ("c", 3)])
dict_from_keys = dict.fromkeys(["a", "b", "c"], 0)

print(f"Empty dict: {empty_dict}")
print(f"Person dict: {person}")
print(f"Scores dict: {scores}")
print(f"Dict from list: {dict_from_list}")
print(f"Dict from keys: {dict_from_keys}")

print("\n4.2 Dictionary Access and Modification")
print("-" * 30)
person = {"name": "Alice", "age": 25, "city": "Boston"}

print(f"Original dict: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country', 'Unknown')}")  # Default value

# Adding/updating
person["email"] = "alice@email.com"
print(f"After adding email: {person}")

person.update({"age": 26, "phone": "123-456-7890"})
print(f"After update: {person}")

# Removing
removed_age = person.pop("age")
print(f"Removed age: {removed_age}")
print(f"After pop: {person}")

del person["phone"]
print(f"After del: {person}")

print("\n4.3 Dictionary Methods")
print("-" * 30)
person = {"name": "Bob", "age": 30, "city": "Chicago"}

print(f"Dictionary: {person}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Copying
person_copy = person.copy()
print(f"Copy: {person_copy}")

# Clearing
person_copy.clear()
print(f"After clear: {person_copy}")

print("\n4.4 Dictionary Comprehensions")
print("-" * 30)
# Traditional way
squares = {}
for i in range(1, 6):
    squares[i] = i**2
print(f"Traditional squares: {squares}")

# Dictionary comprehension
squares_comp = {i: i**2 for i in range(1, 6)}
print(f"Dict comprehension squares: {squares_comp}")

# With condition
even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print(f"Even squares: {even_squares}")

# From existing dictionary
person = {"name": "Alice", "age": 25, "city": "Boston"}
uppercase_values = {
    k: v.upper() if isinstance(v, str) else v for k, v in person.items()
}
print(f"Uppercase string values: {uppercase_values}")

print("\n4.5 Dictionary Iteration")
print("-" * 30)
person = {"name": "Charlie", "age": 35, "city": "Denver", "occupation": "Engineer"}

print("1. Iterate over keys:")
for key in person:
    print(f"  Key: {key}")

print("\n2. Iterate over keys explicitly:")
for key in person.keys():
    print(f"  Key: {key}")

print("\n3. Iterate over values:")
for value in person.values():
    print(f"  Value: {value}")

print("\n4. Iterate over items:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\n5. With enumerate:")
for i, (key, value) in enumerate(person.items()):
    print(f"  Item {i}: {key} = {value}")

print("\n6. Dictionary comprehension with iteration:")
value_lengths = {k: len(str(v)) for k, v in person.items()}
print(f"Value lengths: {value_lengths}")

# ============================================
# SECTION 5: NESTED DATA STRUCTURES
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: NESTED DATA STRUCTURES")
print("=" * 60)

print("\n5.1 Lists of Lists (2D Lists)")
print("-" * 30)
# Creating a 3x3 matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

print(f"Element at [1][2]: {matrix[1][2]}")

# List comprehension for matrix operations
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transpose:")
for row in transpose:
    print(f"  {row}")

print("\n5.2 Lists of Dictionaries")
print("-" * 30)
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"},
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

# Filtering
a_students = [s for s in students if s["grade"] == "A"]
print(f"A students: {a_students}")

print("\n5.3 Dictionaries with Lists")
print("-" * 30)
class_info = {
    "name": "Python Programming",
    "students": ["Alice", "Bob", "Charlie"],
    "grades": [85, 92, 78],
    "schedule": ["Mon", "Wed", "Fri"],
}

print(f"Class: {class_info['name']}")
print(f"Students: {class_info['students']}")

# Zip to combine lists
student_grades = list(zip(class_info["students"], class_info["grades"]))
print(f"Student grades: {student_grades}")

print("\n5.4 Sets of Tuples")
print("-" * 30)
coordinates_set = {(1, 2), (3, 4), (5, 6), (1, 2)}  # Duplicate removed
print(f"Coordinates set: {coordinates_set}")

# Iterating over set of tuples
for x, y in coordinates_set:
    print(f"  Point: ({x}, {y})")

# ============================================
# SECTION 6: PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: PRACTICAL EXAMPLES")
print("=" * 60)

print("\n6.1 Student Grade Management")
print("-" * 30)
# Using multiple data structures
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [90, 88, 95]},
    {"name": "Charlie", "grades": [75, 82, 80]},
]

# Calculate averages
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    student["average"] = round(avg_grade, 2)

print("Student averages:")
for student in students:
    print(f"  {student['name']}: {student['average']}")

# Find top student
top_student = max(students, key=lambda s: s["average"])
print(f"Top student: {top_student['name']} with {top_student['average']}")

print("\n6.2 Word Frequency Counter")
print("-" * 30)
text = "the quick brown fox jumps over the lazy dog"
words = text.split()

# Count word frequencies
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")

# Most common word
most_common = max(word_count, key=word_count.get)
print(f"Most common word: '{most_common}'")

print("\n6.3 Shopping Cart System")
print("-" * 30)
# Product catalog
products = {
    "apple": {"price": 0.50, "stock": 100},
    "banana": {"price": 0.30, "stock": 150},
    "orange": {"price": 0.75, "stock": 80},
}

# Shopping cart
cart = {"apple": 5, "banana": 3, "orange": 2}

# Calculate total
total = sum(products[item]["price"] * quantity for item, quantity in cart.items())
print(f"Cart total: ${total:.2f}")

# Check stock
for item, quantity in cart.items():
    if quantity > products[item]["stock"]:
        print(f"Warning: Not enough {item} in stock")

print("\n6.4 Data Analysis Example")
print("-" * 30)
# Sample data
temperatures = [22, 25, 18, 30, 28, 20, 24, 26, 29, 27]

# Basic statistics
avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)

print(f"Temperature data: {temperatures}")
print(f"Average: {avg_temp:.1f}°C")
print(f"Maximum: {max_temp}°C")
print(f"Minimum: {min_temp}°C")

# Temperature ranges
temp_ranges = {
    "Cold": [t for t in temperatures if t < 20],
    "Mild": [t for t in temperatures if 20 <= t < 25],
    "Warm": [t for t in temperatures if t >= 25],
}

print("Temperature ranges:")
for range_name, temps in temp_ranges.items():
    print(f"  {range_name}: {temps} ({len(temps)} days)")

# ============================================
# SECTION 7: PERFORMANCE AND BEST PRACTICES
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: PERFORMANCE AND BEST PRACTICES")
print("=" * 60)

print("\n7.1 When to Use Each Data Structure")
print("-" * 30)
print(
    """
LISTS:
- Use when you need ordered, changeable collection
- Good for: sequences, stacks, queues
- Examples: to-do lists, scores, coordinates

TUPLES:
- Use when you need ordered, immutable collection
- Good for: coordinates, database records, function returns
- Examples: (x, y) coordinates, (name, age, city)

SETS:
- Use when you need unique, unordered collection
- Good for: removing duplicates, membership testing
- Examples: unique tags, visited nodes, unique words

DICTIONARIES:
- Use when you need key-value pairs
- Good for: lookups, configurations, data records
- Examples: user profiles, settings, word counts
"""
)

print("\n7.2 Performance Tips")
print("-" * 30)
print(
    """
1. Lists:
   - append() and pop() are O(1)
   - insert() and remove() are O(n)
   - Use list comprehensions for better performance

2. Sets:
   - add(), remove(), in are O(1) average
   - Great for membership testing
   - Use for removing duplicates

3. Dictionaries:
   - get(), set(), in are O(1) average
   - Keys must be immutable
   - Use .get() with default values

4. Tuples:
   - Immutable, so very fast
   - Use for data that shouldn't change
   - Good for function returns
"""
)

print("\n7.3 Common Patterns")
print("-" * 30)
print("1. Dictionary as switch/case:")


def get_day_name(day_num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    return days.get(day_num, "Invalid day")


print(f"Day 3: {get_day_name(3)}")
print(f"Day 9: {get_day_name(9)}")

print("\n2. Set for unique values:")
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(f"Original: {numbers}")
print(f"Unique: {unique_numbers}")

print("\n3. List comprehension for filtering:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {even_numbers}")

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    """
🎯 WHAT YOU'VE LEARNED:

1. LISTS
   - Ordered, mutable sequences
   - Indexing, slicing, methods
   - List comprehensions
   - Multiple iteration methods

2. TUPLES
   - Ordered, immutable sequences
   - Tuple unpacking
   - Use for fixed data

3. SETS
   - Unordered, unique collections
   - Set operations (union, intersection, etc.)
   - Fast membership testing

4. DICTIONARIES
   - Key-value pairs
   - Dictionary comprehensions
   - Multiple iteration methods

5. NESTED STRUCTURES
   - Combining different data structures
   - Real-world applications

6. PRACTICAL EXAMPLES
   - Grade management
   - Word frequency counting
   - Shopping cart system
   - Data analysis

7. BEST PRACTICES
   - When to use each structure
   - Performance considerations
   - Common patterns

To run this tutorial: python python_data_structures.py
"""
)

print("\nHappy coding with Python data structures! 🐍📊")
print("Remember: Choose the right tool for the job!")
