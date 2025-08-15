# ============================================
# PYTHON PROCEDURAL PROGRAMMING TUTORIAL
# ============================================
# This file covers procedural programming concepts in Python
# with examples, best practices, and real-world applications

print("=" * 60)
print("PYTHON PROCEDURAL PROGRAMMING TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO PROCEDURAL PROGRAMMING
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO PROCEDURAL PROGRAMMING")
print("=" * 60)

print("\n1.1 What is Procedural Programming?")
print("-" * 30)
print(
    """
Procedural programming is a programming paradigm that:
- Organizes code into procedures (functions)
- Focuses on step-by-step execution
- Uses functions to break down complex tasks
- Emphasizes code reusability and modularity

Key concepts:
1. Functions: Reusable blocks of code
2. Variables: Data storage
3. Control structures: Decision making and loops
4. Scope: Variable visibility and lifetime
5. Parameters: Function inputs
6. Return values: Function outputs

Advantages:
- Simple and straightforward
- Easy to understand and debug
- Good for small to medium programs
- Efficient execution

Disadvantages:
- Can become complex with large programs
- Limited code reusability compared to OOP
- Harder to maintain as program grows
"""
)

print("\n1.2 Procedural vs Other Paradigms")
print("-" * 30)
print(
    """
Programming Paradigms:

1. Procedural Programming:
   - Focus: Functions and procedures
   - Data: Global or local variables
   - Structure: Linear execution flow

2. Object-Oriented Programming (OOP):
   - Focus: Objects and classes
   - Data: Object attributes
   - Structure: Object interactions

3. Functional Programming:
   - Focus: Pure functions
   - Data: Immutable data
   - Structure: Function composition

4. Event-Driven Programming:
   - Focus: Event handlers
   - Data: Event data
   - Structure: Event loops
"""
)

# ============================================
# SECTION 2: FUNCTIONS FUNDAMENTALS
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: FUNCTIONS FUNDAMENTALS")
print("=" * 60)

print("\n2.1 Function Definition and Calling")
print("-" * 30)


# Basic function definition
def greet():
    """Simple function that prints a greeting"""
    print("Hello, World!")


# Function with parameters
def greet_person(name):
    """Function that greets a specific person"""
    print(f"Hello, {name}!")


# Function with multiple parameters
def greet_with_title(name, title="Mr."):
    """Function with default parameter"""
    print(f"Hello, {title} {name}!")


# Function with return value
def add_numbers(a, b):
    """Function that returns the sum of two numbers"""
    return a + b


# Function with multiple return values
def get_name_and_age():
    """Function that returns multiple values"""
    return "John Doe", 30


# Test function calls
print("Testing basic functions:")
greet()
greet_person("Alice")
greet_with_title("Bob")
greet_with_title("Dr. Smith", "Dr.")

result = add_numbers(5, 3)
print(f"Sum: {result}")

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

print("\n2.2 Function Parameters")
print("-" * 30)


# Positional parameters
def describe_person(name, age, city):
    """Function with positional parameters"""
    print(f"{name} is {age} years old and lives in {city}")


# Keyword arguments
describe_person("Alice", 25, "New York")
describe_person(name="Bob", age=30, city="Boston")
describe_person("Charlie", city="Chicago", age=35)


# Default parameters
def create_profile(name, age=18, city="Unknown", occupation="Student"):
    """Function with default parameters"""
    print(f"Profile: {name}, {age}, {city}, {occupation}")


create_profile("David")
create_profile("Eve", 25)
create_profile("Frank", 40, "Los Angeles", "Engineer")


# Variable number of arguments
def sum_all(*args):
    """Function that accepts variable number of arguments"""
    return sum(args)


def print_info(**kwargs):
    """Function that accepts variable number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print(f"Sum of 1, 2, 3, 4: {sum_all(1, 2, 3, 4)}")
print_info(name="Alice", age=25, city="New York", occupation="Developer")

print("\n2.3 Function Types")
print("-" * 30)


# Pure functions (no side effects)
def square(x):
    """Pure function - same input always gives same output"""
    return x**2


# Function with side effects
def append_to_list(lst, item):
    """Function with side effects - modifies input"""
    lst.append(item)
    return lst


# Higher-order function
def apply_operation(func, x, y):
    """Function that takes another function as parameter"""
    return func(x, y)


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"


# Test function types
print("Testing function types:")
print(f"Square of 5: {square(5)}")
print(f"Square of 5 again: {square(5)}")  # Same result

my_list = [1, 2, 3]
print(f"Original list: {my_list}")
append_to_list(my_list, 4)
print(f"Modified list: {my_list}")

print(f"Apply multiply: {apply_operation(multiply, 6, 7)}")
print(f"Apply divide: {apply_operation(divide, 20, 4)}")

# ============================================
# SECTION 3: SCOPE AND VARIABLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: SCOPE AND VARIABLES")
print("=" * 60)

print("\n3.1 Variable Scope")
print("-" * 30)

# Global variable
global_var = "I'm a global variable"


def test_scope():
    """Function to demonstrate variable scope"""
    local_var = "I'm a local variable"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")


def modify_global():
    """Function that modifies global variable"""
    global global_var
    global_var = "I'm a modified global variable"
    print(f"Modified global: {global_var}")


def create_local():
    """Function that creates a local variable with same name"""
    global_var = "I'm a local variable with same name"
    print(f"Local variable: {global_var}")


# Test scope
print("Testing variable scope:")
print(f"Outside function - Global: {global_var}")
test_scope()
create_local()
print(f"After create_local - Global: {global_var}")
modify_global()
print(f"After modify_global - Global: {global_var}")

print("\n3.2 LEGB Rule")
print("-" * 30)
print(
    """
LEGB Rule (Local -> Enclosing -> Global -> Built-in):

1. Local (L): Variables defined inside the function
2. Enclosing (E): Variables in the enclosing function (nested functions)
3. Global (G): Variables defined at module level
4. Built-in (B): Python's built-in names
"""
)

# Example of LEGB rule
x = "global x"


def outer_function():
    x = "enclosing x"

    def inner_function():
        x = "local x"
        print(f"Inner function: {x}")

    inner_function()
    print(f"Outer function: {x}")


outer_function()
print(f"Global scope: {x}")

print("\n3.3 Nonlocal Keyword")
print("-" * 30)


def counter_function():
    """Function demonstrating nonlocal keyword"""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def get_count():
        return count

    return increment, get_count


# Test nonlocal
increment, get_count = counter_function()
print(f"Initial count: {get_count()}")
print(f"After increment: {increment()}")
print(f"After increment: {increment()}")
print(f"Final count: {get_count()}")

# ============================================
# SECTION 4: MODULES AND PACKAGES
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: MODULES AND PACKAGES")
print("=" * 60)

print("\n4.1 Creating and Using Modules")
print("-" * 30)

# Create a simple module (this would be in a separate file)
# math_utils.py
"""
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

PI = 3.14159
"""


# Simulating module import
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b if b != 0 else "Error: Division by zero"

    PI = 3.14159


# Using the module
print("Using math_utils module:")
print(f"Add: {MathUtils.add(10, 5)}")
print(f"Subtract: {MathUtils.subtract(10, 5)}")
print(f"Multiply: {MathUtils.multiply(10, 5)}")
print(f"Divide: {MathUtils.divide(10, 5)}")
print(f"PI: {MathUtils.PI}")

print("\n4.2 Import Statements")
print("-" * 30)
print(
    """
Different ways to import modules:

1. import module_name
   - Import entire module
   - Access with module_name.function_name

2. from module_name import function_name
   - Import specific function
   - Use function directly

3. from module_name import *
   - Import all functions (not recommended)
   - Can cause namespace pollution

4. import module_name as alias
   - Import with alias
   - Useful for long module names

5. from module_name import function_name as alias
   - Import specific function with alias
"""
)

# Example imports (using built-in modules)
import math
from random import randint
import datetime as dt
from os import path

print("Using imported modules:")
print(f"Math sqrt: {math.sqrt(16)}")
print(f"Random number: {randint(1, 10)}")
print(f"Current time: {dt.datetime.now()}")
print(f"Path exists: {path.exists('python_procedural_programming.py')}")

# ============================================
# SECTION 5: ERROR HANDLING IN FUNCTIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: ERROR HANDLING IN FUNCTIONS")
print("=" * 60)

print("\n5.1 Function-Level Error Handling")
print("-" * 30)


def safe_divide(a, b):
    """Function with error handling"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid data types"


def validate_age(age):
    """Function with input validation"""
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True


def process_data(data):
    """Function with comprehensive error handling"""
    try:
        if not data:
            raise ValueError("Data cannot be empty")

        result = []
        for item in data:
            try:
                processed = int(item) * 2
                result.append(processed)
            except (ValueError, TypeError):
                print(f"Warning: Skipping invalid item: {item}")
                continue

        return result

    except Exception as e:
        print(f"Error processing data: {e}")
        return []


# Test error handling
print("Testing error handling:")
print(f"Safe divide 10/2: {safe_divide(10, 2)}")
print(f"Safe divide 10/0: {safe_divide(10, 0)}")
print(f"Safe divide '10'/2: {safe_divide('10', 2)}")

try:
    validate_age(25)
    print("Age validation: Valid")
except ValueError as e:
    print(f"Age validation error: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Age validation error: {e}")

data = [1, 2, "three", 4, "five", 6]
result = process_data(data)
print(f"Processed data: {result}")

# ============================================
# SECTION 6: FUNCTIONAL PROGRAMMING CONCEPTS
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: FUNCTIONAL PROGRAMMING CONCEPTS")
print("=" * 60)

print("\n6.1 Lambda Functions")
print("-" * 30)

# Lambda function (anonymous function)
square_lambda = lambda x: x**2
add_lambda = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print("Testing lambda functions:")
print(f"Square lambda: {square_lambda(5)}")
print(f"Add lambda: {add_lambda(3, 4)}")
print(f"Is even lambda: {is_even(6)}")

# Lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_all = sum(numbers)

print(f"Numbers: {numbers}")
print(f"Squared: {squared}")
print(f"Evens: {evens}")
print(f"Sum: {sum_all}")

print("\n6.2 Map, Filter, Reduce")
print("-" * 30)

from functools import reduce


# Map function
def double(x):
    return x * 2


def square(x):
    return x**2


# Filter function
def is_positive(x):
    return x > 0


def is_even_number(x):
    return x % 2 == 0


# Reduce function
def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


# Test functional programming functions
numbers = [-2, -1, 0, 1, 2, 3, 4, 5]

print("Testing functional programming:")
print(f"Original numbers: {numbers}")

# Map
doubled = list(map(double, numbers))
squared = list(map(square, numbers))
print(f"Doubled: {doubled}")
print(f"Squared: {squared}")

# Filter
positives = list(filter(is_positive, numbers))
evens = list(filter(is_even_number, numbers))
print(f"Positives: {positives}")
print(f"Evens: {evens}")

# Reduce
product = reduce(multiply, positives)
sum_positives = reduce(add, positives)
print(f"Product of positives: {product}")
print(f"Sum of positives: {sum_positives}")

# Combined operations
result = reduce(add, map(square, filter(is_positive, numbers)))
print(f"Sum of squares of positives: {result}")

# ============================================
# SECTION 7: REAL-WORLD APPLICATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: REAL-WORLD APPLICATIONS")
print("=" * 60)

print("\n7.1 Calculator Module")
print("-" * 30)


class Calculator:
    """Simple calculator using procedural programming"""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        return a**b

    @staticmethod
    def calculate(operation, a, b):
        """Main calculation function"""
        operations = {
            "+": Calculator.add,
            "-": Calculator.subtract,
            "*": Calculator.multiply,
            "/": Calculator.divide,
            "**": Calculator.power,
        }

        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")

        return operations[operation](a, b)


# Test calculator
print("Testing calculator:")
try:
    print(f"5 + 3 = {Calculator.calculate('+', 5, 3)}")
    print(f"10 - 4 = {Calculator.calculate('-', 10, 4)}")
    print(f"6 * 7 = {Calculator.calculate('*', 6, 7)}")
    print(f"20 / 5 = {Calculator.calculate('/', 20, 5)}")
    print(f"2 ** 8 = {Calculator.calculate('**', 2, 8)}")
except ValueError as e:
    print(f"Calculator error: {e}")

print("\n7.2 Data Processing Pipeline")
print("-" * 30)


def load_data(filename):
    """Load data from file"""
    # Simulate loading data
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_data(data, condition):
    """Filter data based on condition"""
    return list(filter(condition, data))


def transform_data(data, transformation):
    """Transform data using transformation function"""
    return list(map(transformation, data))


def aggregate_data(data, aggregation_func):
    """Aggregate data using aggregation function"""
    return aggregation_func(data)


def save_results(results, filename):
    """Save results to file"""
    print(f"Saving results to {filename}: {results}")


# Data processing pipeline
def process_data_pipeline():
    """Complete data processing pipeline"""
    # Load data
    data = load_data("input.txt")
    print(f"Loaded data: {data}")

    # Filter even numbers
    even_data = filter_data(data, lambda x: x % 2 == 0)
    print(f"Even numbers: {even_data}")

    # Transform (square the numbers)
    squared_data = transform_data(even_data, lambda x: x**2)
    print(f"Squared data: {squared_data}")

    # Aggregate (sum)
    total = aggregate_data(squared_data, sum)
    print(f"Total: {total}")

    # Save results
    save_results(total, "output.txt")

    return total


# Test data processing pipeline
result = process_data_pipeline()
print(f"Pipeline result: {result}")

print("\n7.3 Configuration Manager")
print("-" * 30)


class ConfigManager:
    """Configuration manager using procedural programming"""

    def __init__(self):
        self.config = {}

    def set_config(self, key, value):
        """Set configuration value"""
        self.config[key] = value

    def get_config(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)

    def load_from_dict(self, config_dict):
        """Load configuration from dictionary"""
        self.config.update(config_dict)

    def save_to_dict(self):
        """Save configuration to dictionary"""
        return self.config.copy()

    def validate_config(self):
        """Validate configuration"""
        required_keys = ["database_url", "port", "debug"]
        missing_keys = [key for key in required_keys if key not in self.config]

        if missing_keys:
            raise ValueError(f"Missing required configuration: {missing_keys}")

        return True


# Test configuration manager
config = ConfigManager()
config.set_config("database_url", "localhost:5432")
config.set_config("port", 8080)
config.set_config("debug", True)
config.set_config("timeout", 30)

print("Configuration manager test:")
print(f"Database URL: {config.get_config('database_url')}")
print(f"Port: {config.get_config('port')}")
print(f"Debug: {config.get_config('debug')}")
print(f"Timeout: {config.get_config('timeout', 60)}")

try:
    config.validate_config()
    print("Configuration is valid")
except ValueError as e:
    print(f"Configuration error: {e}")

# ============================================
# SECTION 8: BEST PRACTICES
# ============================================
print("\n" + "=" * 60)
print("SECTION 8: BEST PRACTICES")
print("=" * 60)

print("\n8.1 Function Design Principles")
print("-" * 30)
print(
    """
1. Single Responsibility Principle:
   - Each function should do one thing well
   - Keep functions focused and concise

2. Function Naming:
   - Use descriptive names
   - Use verbs for actions
   - Be consistent with naming conventions

3. Function Length:
   - Keep functions short (under 20 lines)
   - Break complex functions into smaller ones
   - Aim for readability

4. Parameter Design:
   - Use meaningful parameter names
   - Provide default values when appropriate
   - Limit the number of parameters

5. Return Values:
   - Be consistent with return types
   - Return meaningful values
   - Handle edge cases properly
"""
)

print("\n8.2 Code Organization")
print("-" * 30)
print(
    """
1. Module Structure:
   - Group related functions together
   - Use clear module names
   - Include docstrings and comments

2. Import Organization:
   - Group imports logically
   - Avoid wildcard imports
   - Use absolute imports

3. Error Handling:
   - Handle exceptions at appropriate levels
   - Provide meaningful error messages
   - Use custom exceptions when needed

4. Documentation:
   - Write clear docstrings
   - Include examples in docstrings
   - Keep comments up to date
"""
)

print("\n8.3 Performance Considerations")
print("-" * 30)
print(
    """
1. Function Calls:
   - Minimize function call overhead
   - Use local variables when possible
   - Avoid unnecessary computations

2. Memory Management:
   - Be aware of variable scope
   - Clean up resources properly
   - Avoid memory leaks

3. Algorithm Efficiency:
   - Choose appropriate algorithms
   - Consider time and space complexity
   - Profile code when needed
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

1. PROCEDURAL PROGRAMMING CONCEPTS
   - Functions as building blocks
   - Step-by-step execution
   - Code organization and modularity
   - Advantages and limitations

2. FUNCTION FUNDAMENTALS
   - Function definition and calling
   - Parameters and return values
   - Different function types
   - Lambda functions

3. SCOPE AND VARIABLES
   - Variable scope (LEGB rule)
   - Global and local variables
   - Nonlocal keyword
   - Variable lifetime

4. MODULES AND PACKAGES
   - Creating and using modules
   - Import statements
   - Module organization
   - Package structure

5. ERROR HANDLING
   - Function-level error handling
   - Exception handling in functions
   - Input validation
   - Error propagation

6. FUNCTIONAL PROGRAMMING CONCEPTS
   - Lambda functions
   - Map, filter, reduce
   - Pure functions
   - Higher-order functions

7. REAL-WORLD APPLICATIONS
   - Calculator module
   - Data processing pipeline
   - Configuration manager
   - Practical examples

8. BEST PRACTICES
   - Function design principles
   - Code organization
   - Performance considerations
   - Documentation standards

🚀 KEY TAKEAWAYS:
- Functions are the building blocks of procedural programming
- Proper scope management is crucial
- Error handling makes code robust
- Modular design improves maintainability
- Functional programming concepts enhance code quality
- Best practices lead to better code

To run this tutorial: python python_procedural_programming.py
"""
)

print("\nHappy coding with Python procedural programming! 🐍⚙️")
print("Remember: Good functions make great programs!")
