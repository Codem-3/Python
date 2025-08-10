# ============================================
# PYTHON BASICS TUTORIAL
# ============================================
# This file contains Python basics with examples and explanations
# Run each section to see the output and understand the concepts

print("=" * 50)
print("PYTHON BASICS TUTORIAL")
print("=" * 50)

# ============================================
# 1. VARIABLES AND DATA TYPES
# ============================================
print("\n1. VARIABLES AND DATA TYPES")
print("-" * 30)

# String data type - for text
name = "Alice"
print(f"String variable 'name': {name}")
print(f"Type of 'name': {type(name)}")
print(f"Length of name: {len(name)}")

# Integer data type - for whole numbers
age = 25
print(f"\nInteger variable 'age': {age}")
print(f"Type of 'age': {type(age)}")

# Float data type - for decimal numbers
height = 5.8
print(f"\nFloat variable 'height': {height}")
print(f"Type of 'height': {type(height)}")

# Boolean data type - True or False
is_student = True
print(f"\nBoolean variable 'is_student': {is_student}")
print(f"Type of 'is_student': {type(is_student)}")

# List data type - ordered, changeable collection
fruits = ["apple", "banana", "orange"]
print(f"\nList variable 'fruits': {fruits}")
print(f"Type of 'fruits': {type(fruits)}")
print(f"First fruit: {fruits[0]}")
print(f"Number of fruits: {len(fruits)}")

# Dictionary data type - key-value pairs
person = {"name": "Bob", "age": 30, "city": "New York"}
print(f"\nDictionary variable 'person': {person}")
print(f"Type of 'person': {type(person)}")
print(f"Person's name: {person['name']}")

# ============================================
# 2. VARIABLE NAMING RULES
# ============================================
print("\n\n2. VARIABLE NAMING RULES")
print("-" * 30)

# Valid variable names
first_name = "John"  # Use underscore for spaces
age2 = 25  # Can include numbers (but not at start)
userName = "admin"  # Camel case
PI = 3.14159  # Constants in uppercase

print("Valid variable names:")
print(f"first_name = {first_name}")
print(f"age2 = {age2}")
print(f"userName = {userName}")
print(f"PI = {PI}")

# Invalid variable names (commented out to avoid errors)
# 2name = "invalid"     # Can't start with number
# my-name = "invalid"   # Can't use hyphens
# class = "invalid"     # Can't use reserved words

# ============================================
# 3. BASIC OPERATIONS
# ============================================
print("\n\n3. BASIC OPERATIONS")
print("-" * 30)

# Arithmetic operations
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Modulus (remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# String operations
first = "Hello"
second = "World"
print(
    f"\nString concatenation: '{first}' + ' ' + '{second}' = '{first + ' ' + second}'"
)
print(f"String repetition: '{first}' * 3 = '{first * 3}'")

# ============================================
# 4. TYPE CONVERSION
# ============================================
print("\n\n4. TYPE CONVERSION")
print("-" * 30)

# Converting between types
number_string = "42"
number_int = int(number_string)
print(f"String '{number_string}' converted to int: {number_int}")

float_string = "3.14"
float_number = float(float_string)
print(f"String '{float_string}' converted to float: {float_number}")

number = 123
string_number = str(number)
print(f"Int {number} converted to string: '{string_number}'")

# ============================================
# 5. CONDITIONAL STATEMENTS (IF-ELSE)
# ============================================
print("\n\n5. CONDITIONAL STATEMENTS")
print("-" * 30)

# Simple if-else
score = 85
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators
x = 5
y = 10
print(f"\nComparison operators with x={x}, y={y}:")
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x < y: {x < y}")  # Less than
print(f"x > y: {x > y}")  # Greater than
print(f"x <= y: {x <= y}")  # Less than or equal to
print(f"x >= y: {x >= y}")  # Greater than or equal to

# ============================================
# 6. LOOPS
# ============================================
print("\n\n6. LOOPS")
print("-" * 30)

# For loop with range
print("For loop with range(5):")
for i in range(5):
    print(f"  Iteration {i}")

# For loop with list
print("\nFor loop with list:")
colors = ["red", "green", "blue"]
for color in colors:
    print(f"  Color: {color}")

# While loop
print("\nWhile loop:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1

# ============================================
# 7. FUNCTIONS
# ============================================
print("\n\n7. FUNCTIONS")
print("-" * 30)


# Simple function
def greet(name):
    return f"Hello, {name}!"


# Function with multiple parameters
def add_numbers(a, b):
    return a + b


# Function with default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"


# Calling functions
print(greet("Alice"))
print(f"Sum of 5 and 3: {add_numbers(5, 3)}")
print(greet_with_title("Bob"))
print(greet_with_title("Bob", "Dr."))

# ============================================
# 8. COMMON ERRORS AND SOLUTIONS
# ============================================
print("\n\n8. COMMON ERRORS AND SOLUTIONS")
print("-" * 30)

# NameError - trying to use undefined variable
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError caught: {e}")

# TypeError - wrong data type operation
try:
    result = "5" + 3
except TypeError as e:
    print(f"TypeError caught: {e}")

# IndexError - accessing list index that doesn't exist
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError caught: {e}")

# ============================================
# 9. PRACTICAL EXAMPLES
# ============================================
print("\n\n9. PRACTICAL EXAMPLES")
print("-" * 30)


# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")


# Example 2: Simple calculator
def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"


print(f"10 + 5 = {calculator('add', 10, 5)}")
print(f"10 - 5 = {calculator('subtract', 10, 5)}")
print(f"10 * 5 = {calculator('multiply', 10, 5)}")
print(f"10 / 5 = {calculator('divide', 10, 5)}")

# ============================================
# 10. BEST PRACTICES
# ============================================
print("\n\n10. BEST PRACTICES")
print("-" * 30)

# Use descriptive variable names
user_age = 25  # Good
ua = 25  # Bad

# Use comments to explain complex logic
# Calculate the area of a circle
radius = 5
area = 3.14159 * radius**2


# Use consistent indentation (4 spaces)
def example_function():
    print("This is properly indented")
    if True:
        print("This too")


# ============================================
# SUMMARY
# ============================================
print("\n\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(
    """
What you've learned:
1. Variables and data types (str, int, float, bool, list, dict)
2. Variable naming rules
3. Basic arithmetic and string operations
4. Type conversion
5. Conditional statements (if-elif-else)
6. Loops (for and while)
7. Functions definition and calling
8. Common errors and how to handle them
9. Practical examples
10. Python best practices

To run this file: python python_basics_tutorial.py
"""
)

print("\nHappy coding! 🐍")
