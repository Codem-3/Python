# ============================================
# PYTHON MAP & FILTER TUTORIAL
# ============================================
# This file covers Python's map() and filter() functions
# with examples, advanced techniques, and real-world applications

print("=" * 60)
print("PYTHON MAP & FILTER TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO MAP & FILTER
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO MAP & FILTER")
print("=" * 60)

print("\n1.1 What are Map and Filter?")
print("-" * 30)
print(
    """
Map and Filter are built-in Python functions that work with iterables:

MAP FUNCTION:
- Applies a function to every item in an iterable
- Returns a map object (iterator) with transformed values
- Syntax: map(function, iterable)
- Used for: Data transformation, applying operations to collections

FILTER FUNCTION:
- Filters items from an iterable based on a condition
- Returns a filter object (iterator) with filtered values
- Syntax: filter(function, iterable)
- Used for: Data filtering, conditional selection

Key characteristics:
- Both return iterators (not lists)
- Both are lazy (evaluate only when needed)
- Both work with any iterable (lists, tuples, strings, etc.)
- Both are functional programming concepts
"""
)

print("\n1.2 Why Use Map and Filter?")
print("-" * 30)
print(
    """
Advantages:
1. Functional Programming: Write cleaner, more readable code
2. Performance: Lazy evaluation saves memory
3. Readability: Intent is clear and concise
4. Chainability: Can be combined with other functions
5. Immutability: Don't modify original data

Common use cases:
- Data processing and transformation
- List comprehensions alternative
- Functional programming patterns
- Data filtering and validation
- Mathematical operations on collections
"""
)

# ============================================
# SECTION 2: MAP FUNCTION BASICS
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: MAP FUNCTION BASICS")
print("=" * 60)

print("\n2.1 Basic Map Usage")
print("-" * 30)


# Basic map with a simple function
def square(x):
    return x**2


numbers = [1, 2, 3, 4, 5]
squared_map = map(square, numbers)
squared_list = list(squared_map)

print("Basic map example:")
print(f"Original numbers: {numbers}")
print(f"Map object: {squared_map}")
print(f"Squared numbers: {squared_list}")


# Map with multiple iterables
def add_numbers(a, b):
    return a + b


list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sum_map = map(add_numbers, list1, list2)
sum_list = list(sum_map)

print(f"\nMap with multiple iterables:")
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Sum: {sum_list}")

print("\n2.2 Map with Built-in Functions")
print("-" * 30)

# Map with built-in functions
numbers = [1, 2, 3, 4, 5]
strings = ["hello", "world", "python", "programming"]

# Convert to string
str_numbers = list(map(str, numbers))
print(f"Numbers to strings: {str_numbers}")

# Get lengths
lengths = list(map(len, strings))
print(f"String lengths: {lengths}")

# Convert to uppercase
uppercase = list(map(str.upper, strings))
print(f"Uppercase strings: {uppercase}")

# Convert to float
float_numbers = list(map(float, numbers))
print(f"Float numbers: {float_numbers}")

print("\n2.3 Map with Lambda Functions")
print("-" * 30)

# Lambda functions with map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square numbers
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Double numbers
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Add 10 to each number
plus_ten = list(map(lambda x: x + 10, numbers))
print(f"Plus ten: {plus_ten}")

# Convert to string with prefix
with_prefix = list(map(lambda x: f"Number_{x}", numbers))
print(f"With prefix: {with_prefix}")

# ============================================
# SECTION 3: FILTER FUNCTION BASICS
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: FILTER FUNCTION BASICS")
print("=" * 60)

print("\n3.1 Basic Filter Usage")
print("-" * 30)


# Basic filter with a simple function
def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_filter = filter(is_even, numbers)
even_list = list(even_filter)

print("Basic filter example:")
print(f"Original numbers: {numbers}")
print(f"Filter object: {even_filter}")
print(f"Even numbers: {even_list}")


# Filter with multiple conditions
def is_positive_and_even(x):
    return x > 0 and x % 2 == 0


positive_even = list(filter(is_positive_and_even, numbers))
print(f"Positive and even: {positive_even}")

print("\n3.2 Filter with Built-in Functions")
print("-" * 30)

# Filter with built-in functions
mixed_list = [0, 1, False, True, "", "hello", [], [1, 2], None]

# Filter truthy values
truthy = list(filter(bool, mixed_list))
print(f"Truthy values: {truthy}")

# Filter non-empty strings
strings = ["", "hello", "", "world", "", "python"]
non_empty = list(filter(None, strings))  # None is equivalent to bool
print(f"Non-empty strings: {non_empty}")

# Filter non-zero numbers
numbers = [0, 1, 2, 0, 3, 0, 4, 5]
non_zero = list(filter(lambda x: x != 0, numbers))
print(f"Non-zero numbers: {non_zero}")

print("\n3.3 Filter with Lambda Functions")
print("-" * 30)

# Lambda functions with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odds}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

# Filter numbers divisible by 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(f"Divisible by 3: {divisible_by_3}")

# ============================================
# SECTION 4: ADVANCED MAP & FILTER TECHNIQUES
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: ADVANCED MAP & FILTER TECHNIQUES")
print("=" * 60)

print("\n4.1 Combining Map and Filter")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter then map
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Even numbers squared: {even_squares}")

# Map then filter
squares_greater_than_20 = list(filter(lambda x: x > 20, map(lambda x: x**2, numbers)))
print(f"Squares greater than 20: {squares_greater_than_20}")

# Complex combination
complex_result = list(
    map(
        lambda x: x * 2,  # Double the result
        filter(
            lambda x: x > 5,  # Filter numbers > 5
            map(
                lambda x: x**2,  # Square the numbers
                filter(lambda x: x % 2 == 0, numbers),  # Filter even numbers
            ),
        ),
    )
)
print(f"Complex combination: {complex_result}")

print("\n4.2 Map and Filter with Multiple Iterables")
print("-" * 30)

# Map with multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Boston", "Chicago"]

# Create person descriptions
descriptions = list(
    map(
        lambda name, age, city: f"{name} is {age} years old and lives in {city}",
        names,
        ages,
        cities,
    )
)
print(f"Person descriptions: {descriptions}")

# Filter based on multiple conditions
people_data = [
    ("Alice", 25, "New York"),
    ("Bob", 30, "Boston"),
    ("Charlie", 35, "Chicago"),
    ("David", 22, "Los Angeles"),
    ("Eve", 28, "San Francisco"),
]

# Filter people over 25
over_25 = list(filter(lambda person: person[1] > 25, people_data))
print(f"People over 25: {over_25}")

# Map and filter combination with complex data
young_people_names = list(
    map(
        lambda person: person[0],  # Extract name
        filter(lambda person: person[1] < 30, people_data),  # Filter young people
    )
)
print(f"Young people names: {young_people_names}")

print("\n4.3 Map and Filter with Custom Classes")
print("-" * 30)


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"{self.name} (Grade: {self.grade}, Age: {self.age})"


students = [
    Student("Alice", 85, 18),
    Student("Bob", 92, 19),
    Student("Charlie", 78, 20),
    Student("David", 95, 18),
    Student("Eve", 88, 19),
]

# Filter high-performing students
high_performers = list(filter(lambda s: s.grade >= 90, students))
print("High performers:")
for student in high_performers:
    print(f"  {student}")

# Map to get student names
names = list(map(lambda s: s.name, students))
print(f"Student names: {names}")

# Filter and map combination
young_high_performers = list(
    map(lambda s: s.name, filter(lambda s: s.grade >= 90 and s.age < 20, students))
)
print(f"Young high performers: {young_high_performers}")

# ============================================
# SECTION 5: REAL-WORLD APPLICATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: REAL-WORLD APPLICATIONS")
print("=" * 60)

print("\n5.1 Data Processing Pipeline")
print("-" * 30)

# Simulate data from a CSV file
raw_data = [
    "alice,25,new york,85000",
    "bob,30,boston,92000",
    "charlie,35,chicago,78000",
    "david,22,los angeles,65000",
    "eve,28,san francisco,88000",
]


def parse_employee_data(line):
    """Parse employee data from CSV line"""
    name, age, city, salary = line.split(",")
    return {
        "name": name.title(),
        "age": int(age),
        "city": city.title(),
        "salary": int(salary),
    }


def is_high_earner(employee):
    """Check if employee is a high earner"""
    return employee["salary"] > 80000


def format_employee_info(employee):
    """Format employee information"""
    return f"{employee['name']} earns ${employee['salary']:,} in {employee['city']}"


# Data processing pipeline
print("Data processing pipeline:")
print(f"Raw data: {raw_data}")

# Parse data
employees = list(map(parse_employee_data, raw_data))
print(f"Parsed employees: {employees}")

# Filter high earners
high_earners = list(filter(is_high_earner, employees))
print(f"High earners: {high_earners}")

# Format information
formatted_info = list(map(format_employee_info, high_earners))
print("Formatted high earner info:")
for info in formatted_info:
    print(f"  {info}")

print("\n5.2 Text Processing")
print("-" * 30)

# Text processing example
text_lines = [
    "  hello world  ",
    "  python programming  ",
    "  functional programming  ",
    "  data science  ",
    "  machine learning  ",
]


def clean_text(text):
    """Clean and normalize text"""
    return text.strip().lower()


def has_keyword(text, keyword):
    """Check if text contains keyword"""
    return keyword in text


def capitalize_words(text):
    """Capitalize each word"""
    return " ".join(word.capitalize() for word in text.split())


# Text processing pipeline
print("Text processing pipeline:")
print(f"Original lines: {text_lines}")

# Clean text
cleaned_lines = list(map(clean_text, text_lines))
print(f"Cleaned lines: {cleaned_lines}")

# Filter lines with 'programming'
programming_lines = list(
    filter(lambda text: has_keyword(text, "programming"), cleaned_lines)
)
print(f"Lines with 'programming': {programming_lines}")

# Capitalize words
capitalized = list(map(capitalize_words, programming_lines))
print(f"Capitalized: {capitalized}")

print("\n5.3 Mathematical Operations")
print("-" * 30)

# Mathematical operations with map and filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate squares of even numbers
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Squares of even numbers: {even_squares}")

# Calculate sum of squares of even numbers
sum_even_squares = sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Sum of squares of even numbers: {sum_even_squares}")


# Find prime numbers (simple implementation)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = list(filter(is_prime, range(1, 50)))
print(f"Prime numbers up to 50: {primes}")


# Calculate factorial using map
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


factorials = list(map(factorial, range(1, 8)))
print(f"Factorials 1-7: {factorials}")

print("\n5.4 Configuration Management")
print("-" * 30)

# Configuration processing
config_lines = [
    "DEBUG=true",
    "PORT=8080",
    "DATABASE_URL=localhost:5432",
    "SECRET_KEY=abc123",
    "LOG_LEVEL=INFO",
    "CACHE_ENABLED=false",
]


def parse_config_line(line):
    """Parse configuration line"""
    key, value = line.split("=", 1)
    return key.strip(), value.strip()


def is_boolean_config(item):
    """Check if config item is boolean"""
    key, value = item
    return value.lower() in ["true", "false"]


def convert_boolean(item):
    """Convert string boolean to actual boolean"""
    key, value = item
    return key, value.lower() == "true"


# Configuration processing pipeline
print("Configuration processing:")
config_items = list(map(parse_config_line, config_lines))
print(f"Parsed config: {config_items}")

boolean_configs = list(filter(is_boolean_config, config_items))
print(f"Boolean configs: {boolean_configs}")

converted_booleans = list(map(convert_boolean, boolean_configs))
print(f"Converted booleans: {converted_booleans}")

# ============================================
# SECTION 6: PERFORMANCE AND OPTIMIZATION
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: PERFORMANCE AND OPTIMIZATION")
print("=" * 60)

print("\n6.1 Performance Comparison")
print("-" * 30)

import time


def measure_time(func, iterations=1000):
    """Measure execution time of a function"""
    start_time = time.time()
    for _ in range(iterations):
        func()
    end_time = time.time()
    return (end_time - start_time) / iterations


# Test data
numbers = list(range(1000))


# Map performance tests
def test_map_performance():
    return list(map(lambda x: x**2, numbers))


def test_list_comprehension():
    return [x**2 for x in numbers]


def test_for_loop():
    result = []
    for x in numbers:
        result.append(x**2)
    return result


# Filter performance tests
def test_filter_performance():
    return list(filter(lambda x: x % 2 == 0, numbers))


def test_list_comprehension_filter():
    return [x for x in numbers if x % 2 == 0]


def test_for_loop_filter():
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result


print("Performance comparison (seconds per operation):")
print("Map operations:")
print(f"  Map function: {measure_time(test_map_performance):.6f}")
print(f"  List comprehension: {measure_time(test_list_comprehension):.6f}")
print(f"  For loop: {measure_time(test_for_loop):.6f}")

print("\nFilter operations:")
print(f"  Filter function: {measure_time(test_filter_performance):.6f}")
print(f"  List comprehension: {measure_time(test_list_comprehension_filter):.6f}")
print(f"  For loop: {measure_time(test_for_loop_filter):.6f}")

print("\n6.2 Memory Efficiency")
print("-" * 30)
print(
    """
Memory Efficiency Analysis:

1. Map and Filter are lazy:
   - They don't create lists immediately
   - Memory is used only when iterating
   - Good for large datasets

2. List comprehensions:
   - Create lists immediately
   - Use more memory upfront
   - Faster for small datasets

3. For loops:
   - Manual memory management
   - Most memory efficient for simple operations
   - More verbose code

Best practices:
- Use map/filter for large datasets
- Use list comprehensions for small datasets
- Use for loops for complex operations
"""
)

print("\n6.3 Optimization Tips")
print("-" * 30)
print(
    """
1. Use appropriate method:
   - map/filter for functional programming
   - list comprehensions for simple operations
   - for loops for complex logic

2. Avoid unnecessary conversions:
   - Don't convert to list if you only need to iterate
   - Use map/filter objects directly when possible

3. Chain operations efficiently:
   - Combine map and filter in one pass when possible
   - Use generator expressions for large datasets

4. Profile your code:
   - Measure performance for your specific use case
   - Choose method based on requirements
"""
)

# ============================================
# SECTION 7: COMMON PATTERNS AND IDIOMS
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: COMMON PATTERNS AND IDIOMS")
print("=" * 60)

print("\n7.1 Common Map Patterns")
print("-" * 30)

# Type conversion pattern
strings = ["1", "2", "3", "4", "5"]
numbers = list(map(int, strings))
print(f"String to int conversion: {numbers}")


# Function application pattern
def apply_discount(price, discount_rate=0.1):
    return price * (1 - discount_rate)


prices = [100, 200, 300, 400, 500]
discounted_prices = list(map(lambda p: apply_discount(p, 0.2), prices))
print(f"Discounted prices: {discounted_prices}")

# Data transformation pattern
names = ["alice", "bob", "charlie"]
formatted_names = list(map(lambda name: f"Hello, {name.title()}!", names))
print(f"Formatted names: {formatted_names}")

print("\n7.2 Common Filter Patterns")
print("-" * 30)


# Data validation pattern
def is_valid_email(email):
    return "@" in email and "." in email


emails = ["alice@example.com", "invalid-email", "bob@test.org", "no-at-sign"]
valid_emails = list(filter(is_valid_email, emails))
print(f"Valid emails: {valid_emails}")

# Range filtering pattern
ages = [18, 25, 30, 35, 40, 45, 50]
adult_ages = list(filter(lambda age: 18 <= age <= 65, ages))
print(f"Adult ages: {adult_ages}")

# Type filtering pattern
mixed_data = [1, "hello", 2.5, "world", 3, True, "python"]
strings_only = list(filter(lambda x: isinstance(x, str), mixed_data))
print(f"Strings only: {strings_only}")

print("\n7.3 Combined Patterns")
print("-" * 30)

# Transform and filter pattern
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Even squares: {even_squares}")

# Filter and transform pattern
words = ["hello", "world", "python", "programming", "data", "science"]
long_words = list(map(str.upper, filter(lambda w: len(w) > 5, words)))
print(f"Long words in uppercase: {long_words}")

# Multiple transformations
data = ["  alice  ", "  bob  ", "  charlie  "]
processed = list(
    map(str.title, map(str.strip, filter(lambda s: len(s.strip()) > 0, data)))
)
print(f"Processed data: {processed}")

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    """
🎯 WHAT YOU'VE LEARNED:

1. MAP FUNCTION BASICS
   - Basic usage with custom functions
   - Built-in function integration
   - Lambda function applications
   - Multiple iterable support

2. FILTER FUNCTION BASICS
   - Conditional filtering
   - Built-in function usage
   - Lambda function filtering
   - Complex condition handling

3. ADVANCED TECHNIQUES
   - Combining map and filter
   - Multiple iterable operations
   - Custom class integration
   - Complex data transformations

4. REAL-WORLD APPLICATIONS
   - Data processing pipelines
   - Text processing
   - Mathematical operations
   - Configuration management

5. PERFORMANCE ANALYSIS
   - Time complexity comparison
   - Memory efficiency analysis
   - Optimization strategies
   - Best practices

6. COMMON PATTERNS
   - Type conversion patterns
   - Data validation patterns
   - Transformation patterns
   - Combined operation patterns

🚀 KEY TAKEAWAYS:
- Map transforms data, filter selects data
- Both return iterators (lazy evaluation)
- Lambda functions make them powerful
- Can be combined for complex operations
- Choose based on performance needs
- Use for functional programming patterns

To run this tutorial: python python_map_filter.py
"""
)

print("\nHappy coding with Python Map & Filter! 🐍🗺️🔍")
print("Remember: Map transforms, Filter selects!")
