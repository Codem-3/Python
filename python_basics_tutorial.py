# ============================================
# PYTHON BASICS TUTORIAL - COMPLETE GUIDE
# ============================================
# This file contains Python basics with examples and explanations
# Run each section to see the output and understand the concepts

print("=" * 60)
print("PYTHON BASICS TUTORIAL - COMPLETE GUIDE")
print("=" * 60)

# ============================================
# SECTION 1: VARIABLES AND DATA TYPES
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: VARIABLES AND DATA TYPES")
print("=" * 60)

print("\n1.1 String Data Type")
print("-" * 30)
# String data type - for text
name = "Alice"
print(f"String variable 'name': {name}")
print(f"Type of 'name': {type(name)}")
print(f"Length of name: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")

print("\n1.2 Integer Data Type")
print("-" * 30)
# Integer data type - for whole numbers
age = 25
print(f"Integer variable 'age': {age}")
print(f"Type of 'age': {type(age)}")
print(f"Binary representation: {bin(age)}")
print(f"Hexadecimal representation: {hex(age)}")

print("\n1.3 Float Data Type")
print("-" * 30)
# Float data type - for decimal numbers
height = 5.8
pi = 3.14159
print(f"Float variable 'height': {height}")
print(f"Type of 'height': {type(height)}")
print(f"Pi value: {pi}")
print(f"Rounded to 2 decimal places: {round(pi, 2)}")

print("\n1.4 Boolean Data Type")
print("-" * 30)
# Boolean data type - True or False
is_student = True
is_working = False
print(f"Boolean variable 'is_student': {is_student}")
print(f"Type of 'is_student': {type(is_student)}")
print(f"Boolean variable 'is_working': {is_working}")

print("\n1.5 List Data Type")
print("-" * 30)
# List data type - ordered, changeable collection
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(f"List variable 'fruits': {fruits}")
print(f"Type of 'fruits': {type(fruits)}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Number of fruits: {len(fruits)}")
print(f"Mixed list: {mixed}")

print("\n1.6 Dictionary Data Type")
print("-" * 30)
# Dictionary data type - key-value pairs
person = {"name": "Bob", "age": 30, "city": "New York"}
print(f"Dictionary variable 'person': {person}")
print(f"Type of 'person': {type(person)}")
print(f"Person's name: {person['name']}")
print(f"All keys: {list(person.keys())}")
print(f"All values: {list(person.values())}")

print("\n1.7 Tuple Data Type")
print("-" * 30)
# Tuple data type - ordered, immutable collection
coordinates = (10, 20)
rgb_color = (255, 128, 0)
print(f"Tuple variable 'coordinates': {coordinates}")
print(f"Type of 'coordinates': {type(coordinates)}")
print(f"X coordinate: {coordinates[0]}")
print(f"RGB color: {rgb_color}")

# ============================================
# SECTION 2: VARIABLE NAMING AND ASSIGNMENT
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: VARIABLE NAMING AND ASSIGNMENT")
print("=" * 60)

print("\n2.1 Valid Variable Names")
print("-" * 30)
# Valid variable names
first_name = "John"  # Use underscore for spaces
age2 = 25  # Can include numbers (but not at start)
userName = "admin"  # Camel case
PI = 3.14159  # Constants in uppercase
_private_var = "hidden"  # Private variable (convention)

print("Valid variable names:")
print(f"first_name = {first_name}")
print(f"age2 = {age2}")
print(f"userName = {userName}")
print(f"PI = {PI}")
print(f"_private_var = {_private_var}")

print("\n2.2 Multiple Assignment")
print("-" * 30)
# Multiple assignment
x, y, z = 1, 2, 3
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Unpacking lists
numbers = [10, 20, 30]
a, b, c = numbers
print(f"Unpacking list: a={a}, b={b}, c={c}")

# Swapping variables
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# ============================================
# SECTION 3: ARITHMETIC OPERATORS
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: ARITHMETIC OPERATORS")
print("=" * 60)

print("\n3.1 Basic Arithmetic Operators")
print("-" * 30)
a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Modulus (remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print("\n3.2 Assignment Operators")
print("-" * 30)
x = 10
print(f"Initial value: x = {x}")

x += 5  # Same as x = x + 5
print(f"After x += 5: x = {x}")

x -= 3  # Same as x = x - 3
print(f"After x -= 3: x = {x}")

x *= 2  # Same as x = x * 2
print(f"After x *= 2: x = {x}")

x /= 4  # Same as x = x / 4
print(f"After x /= 4: x = {x}")

x //= 2  # Same as x = x // 2
print(f"After x //= 2: x = {x}")

x %= 3  # Same as x = x % 3
print(f"After x %= 3: x = {x}")

x **= 2  # Same as x = x ** 2
print(f"After x **= 2: x = {x}")

print("\n3.3 Math Functions")
print("-" * 30)
import math

number = 16.7
print(f"Number: {number}")
print(f"Absolute value: {abs(-number)}")
print(f"Square root: {math.sqrt(number)}")
print(f"Ceiling (round up): {math.ceil(number)}")
print(f"Floor (round down): {math.floor(number)}")
print(f"Rounded: {round(number)}")
print(f"Rounded to 1 decimal: {round(number, 1)}")
print(f"Power of 2: {math.pow(number, 2)}")
print(f"Natural logarithm: {math.log(number)}")
print(f"Sine of 30 degrees: {math.sin(math.radians(30))}")

# ============================================
# SECTION 4: LOGICAL OPERATORS
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: LOGICAL OPERATORS")
print("=" * 60)

print("\n4.1 Comparison Operators")
print("-" * 30)
x = 5
y = 10
z = 5

print(f"x = {x}, y = {y}, z = {z}")
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x < y: {x < y}")  # Less than
print(f"x > y: {x > y}")  # Greater than
print(f"x <= y: {x <= y}")  # Less than or equal to
print(f"x >= y: {x >= y}")  # Greater than or equal to
print(f"x == z: {x == z}")  # Equal to

print("\n4.2 Logical Operators")
print("-" * 30)
a = True
b = False
c = True

print(f"a = {a}, b = {b}, c = {c}")
print(f"a and b: {a and b}")  # Logical AND
print(f"a or b: {a or b}")  # Logical OR
print(f"not a: {not a}")  # Logical NOT
print(f"a and c: {a and c}")  # Both True
print(f"b or c: {b or c}")  # One True
print(f"not b: {not b}")  # NOT False = True

print("\n4.3 Complex Logical Expressions")
print("-" * 30)
age = 25
has_license = True
has_car = False

print(f"Age: {age}, Has License: {has_license}, Has Car: {has_car}")

# Can drive if age >= 18 AND has license
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

# Can get insurance if (age >= 25 OR has_license) AND has_car
can_get_insurance = (age >= 25 or has_license) and has_car
print(f"Can get insurance: {can_get_insurance}")

# Is teenager if age >= 13 AND age <= 19
is_teenager = 13 <= age <= 19
print(f"Is teenager: {is_teenager}")

print("\n4.4 Truthiness and Falsiness")
print("-" * 30)
# In Python, these are considered False:
falsy_values = [False, 0, 0.0, "", [], (), {}, None]

print("Falsy values in Python:")
for value in falsy_values:
    print(f"  {value} is {bool(value)}")

# Everything else is considered True
truthy_values = [True, 1, 3.14, "hello", [1, 2], (1, 2), {"key": "value"}]

print("\nTruthy values in Python:")
for value in truthy_values:
    print(f"  {value} is {bool(value)}")

# ============================================
# SECTION 5: STRING OPERATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: STRING OPERATIONS")
print("=" * 60)

print("\n5.1 String Concatenation and Repetition")
print("-" * 30)
first = "Hello"
second = "World"
print(f"String concatenation: '{first}' + ' ' + '{second}' = '{first + ' ' + second}'")
print(f"String repetition: '{first}' * 3 = '{first * 3}'")

print("\n5.2 String Methods")
print("-" * 30)
text = "  Python Programming  "
print(f"Original text: '{text}'")
print(f"Length: {len(text)}")
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")
print(f"Title case: '{text.title()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Strip whitespace: '{text.strip()}'")
print(f"Replace 'Python' with 'Java': '{text.replace('Python', 'Java')}'")
print(f"Split by space: {text.split()}")
print(f"Count 'm': {text.count('m')}")
print(f"Find 'gram': {text.find('gram')}")

print("\n5.3 String Formatting")
print("-" * 30)
name = "Alice"
age = 25
height = 5.6

# f-string (recommended)
print(f"Name: {name}, Age: {age}, Height: {height}")

# .format() method
print("Name: {}, Age: {}, Height: {}".format(name, age, height))

# % operator (old style)
print("Name: %s, Age: %d, Height: %.1f" % (name, age, height))

# ============================================
# SECTION 6: TYPE CONVERSION
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: TYPE CONVERSION")
print("=" * 60)

print("\n6.1 Converting Between Types")
print("-" * 30)
# String to numbers
number_string = "42"
number_int = int(number_string)
print(f"String '{number_string}' converted to int: {number_int}")

float_string = "3.14"
float_number = float(float_string)
print(f"String '{float_string}' converted to float: {float_number}")

# Numbers to string
number = 123
string_number = str(number)
print(f"Int {number} converted to string: '{string_number}'")

# Boolean conversion
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

print("\n6.2 List and Tuple Conversion")
print("-" * 30)
# String to list
text = "hello"
char_list = list(text)
print(f"String '{text}' to list: {char_list}")

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"List {my_list} to tuple: {my_tuple}")

# Tuple to list
my_tuple2 = (4, 5, 6)
my_list2 = list(my_tuple2)
print(f"Tuple {my_tuple2} to list: {my_list2}")

# ============================================
# SECTION 7: CONDITIONAL STATEMENTS
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: CONDITIONAL STATEMENTS")
print("=" * 60)

print("\n7.1 Simple If-Else")
print("-" * 30)
score = 85
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("\n7.2 Nested If Statements")
print("-" * 30)
age = 25
income = 50000

if age >= 18:
    print("You are an adult")
    if income >= 50000:
        print("You have a good income")
    else:
        print("You need to work on your income")
else:
    print("You are a minor")

print("\n7.3 Conditional Expressions (Ternary Operator)")
print("-" * 30)
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Traditional way
if age >= 18:
    status = "adult"
else:
    status = "minor"

# ============================================
# SECTION 8: LOOPS
# ============================================
print("\n" + "=" * 60)
print("SECTION 8: LOOPS")
print("=" * 60)

print("\n8.1 For Loop with Range")
print("-" * 30)
print("For loop with range(5):")
for i in range(5):
    print(f"  Iteration {i}")

print("\nFor loop with range(1, 6):")
for i in range(1, 6):
    print(f"  Number: {i}")

print("\nFor loop with range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  Even number: {i}")

print("\n8.2 For Loop with Lists")
print("-" * 30)
colors = ["red", "green", "blue"]
print("For loop with list:")
for color in colors:
    print(f"  Color: {color}")

print("\nFor loop with enumerate:")
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

print("\n8.3 While Loop")
print("-" * 30)
count = 0
print("While loop:")
while count < 3:
    print(f"  Count: {count}")
    count += 1

print("\n8.4 Loop Control")
print("-" * 30)
print("Break example:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}")

print("\nContinue example:")
for i in range(5):
    if i == 2:
        continue
    print(f"  {i}")

# ============================================
# SECTION 9: FUNCTIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 9: FUNCTIONS")
print("=" * 60)

print("\n9.1 Simple Function")
print("-" * 30)


def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))

print("\n9.2 Function with Multiple Parameters")
print("-" * 30)


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b, c):
    return a * b * c


print(f"Sum of 5 and 3: {add_numbers(5, 3)}")
print(f"Product of 2, 3, 4: {multiply_numbers(2, 3, 4)}")

print("\n9.3 Function with Default Parameters")
print("-" * 30)


def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"


print(greet_with_title("Bob"))
print(greet_with_title("Bob", "Dr."))

print("\n9.4 Function with Variable Arguments")
print("-" * 30)


def sum_all(*args):
    return sum(args)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


print(f"Sum of 1, 2, 3, 4: {sum_all(1, 2, 3, 4)}")
print("Person info:")
print_info(name="John", age=30, city="New York")

# ============================================
# SECTION 10: ERROR HANDLING
# ============================================
print("\n" + "=" * 60)
print("SECTION 10: ERROR HANDLING")
print("=" * 60)

print("\n10.1 Common Errors and Solutions")
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

# ValueError - invalid value for conversion
try:
    int("abc")
except ValueError as e:
    print(f"ValueError caught: {e}")

# ZeroDivisionError - division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")

print("\n10.2 Try-Except with Else and Finally")
print("-" * 30)
try:
    number = int("42")
    print(f"Successfully converted: {number}")
except ValueError:
    print("Could not convert to integer")
else:
    print("No exception occurred")
finally:
    print("This always executes")

# ============================================
# SECTION 11: PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 11: PRACTICAL EXAMPLES")
print("=" * 60)

print("\n11.1 Temperature Converter")
print("-" * 30)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F = {temp_c2}°C")

print("\n11.2 Simple Calculator")
print("-" * 30)


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

print("\n11.3 Number Guessing Game Logic")
print("-" * 30)
import random


def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("I'm thinking of a number between 1 and 10.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return

        except ValueError:
            print("Please enter a valid number!")

    print(f"Game over! The number was {secret_number}")


# Uncomment to play the game
# number_guessing_game()

print("\n11.4 Grade Calculator")
print("-" * 30)


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_gpa(grades):
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    total_points = sum(grade_points[grade] for grade in grades)
    return total_points / len(grades)


scores = [85, 92, 78, 96, 88]
grades = [calculate_grade(score) for score in scores]
gpa = calculate_gpa(grades)

print(f"Scores: {scores}")
print(f"Grades: {grades}")
print(f"GPA: {gpa:.2f}")

# ============================================
# SECTION 12: BEST PRACTICES
# ============================================
print("\n" + "=" * 60)
print("SECTION 12: BEST PRACTICES")
print("=" * 60)

print("\n12.1 Variable Naming")
print("-" * 30)
# Use descriptive variable names
user_age = 25  # Good
ua = 25  # Bad

# Use snake_case for variables and functions
first_name = "John"  # Good
firstName = "John"  # Bad

# Use UPPERCASE for constants
PI = 3.14159  # Good
pi = 3.14159  # Bad

print("Good naming examples:")
print(f"user_age = {user_age}")
print(f"first_name = {first_name}")
print(f"PI = {PI}")

print("\n12.2 Code Organization")
print("-" * 30)
# Use comments to explain complex logic
# Calculate the area of a circle
radius = 5
area = math.pi * radius**2
print(f"Circle area with radius {radius}: {area:.2f}")


# Use consistent indentation (4 spaces)
def example_function():
    print("This is properly indented")
    if True:
        print("This too")


print("\n12.3 String Formatting Best Practices")
print("-" * 30)
name = "Alice"
age = 25

# Use f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# Avoid concatenation for multiple variables
# Bad: "Name: " + name + ", Age: " + str(age)
# Good: f"Name: {name}, Age: {age}"

# ============================================
# SUMMARY AND NEXT STEPS
# ============================================
print("\n" + "=" * 60)
print("SUMMARY AND NEXT STEPS")
print("=" * 60)

print(
    """
🎯 WHAT YOU'VE LEARNED:

1.  Variables and Data Types
    - String, Integer, Float, Boolean, List, Dictionary, Tuple
    - Type checking and conversion

2.  Variable Naming and Assignment
    - Naming conventions and rules
    - Multiple assignment and unpacking

3.  Arithmetic Operators
    - Basic operations (+, -, *, /, //, %, **)
    - Assignment operators (+=, -=, *=, etc.)
    - Math functions (abs, sqrt, ceil, floor, etc.)

4.  Logical Operators
    - Comparison operators (==, !=, <, >, <=, >=)
    - Logical operators (and, or, not)
    - Truthiness and falsiness

5.  String Operations
    - Concatenation and repetition
    - String methods (upper, lower, strip, split, etc.)
    - String formatting (f-strings, .format(), %)

6.  Type Conversion
    - Converting between different data types
    - Safe conversion practices

7.  Conditional Statements
    - if, elif, else statements
    - Nested conditions
    - Ternary operators

8.  Loops
    - for loops with range and iterables
    - while loops
    - Loop control (break, continue)

9.  Functions
    - Function definition and calling
    - Parameters and return values
    - Default and variable arguments

10. Error Handling
    - Common Python errors
    - try-except blocks
    - Best practices for error handling

11. Practical Examples
    - Real-world applications
    - Problem-solving approaches

12. Best Practices
    - Code organization and style
    - Python conventions (PEP 8)

To run this tutorial: python python_basics_tutorial.py
"""
)

print("\nHappy coding! 🐍✨")
print("Remember: Practice makes perfect!")
