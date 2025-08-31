"""
Python Modules and Imports Tutorial
===================================

This tutorial covers:
1. What are modules and why use them
2. Different ways to import modules
3. Creating your own modules
4. Module search path and sys.path
5. Best practices for imports
6. Common import patterns
7. Module reloading and caching
"""

import sys
import os
import math
import random
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import json
import pickle

# 1. WHAT ARE MODULES?
print("=" * 50)
print("1. WHAT ARE MODULES?")
print("=" * 50)

"""
A module is a Python file containing functions, classes, variables, and other code.
Modules help organize code by grouping related functionality together.
"""

# 2. DIFFERENT WAYS TO IMPORT MODULES
print("\n" + "=" * 50)
print("2. DIFFERENT WAYS TO IMPORT MODULES")
print("=" * 50)

# Method 1: Import entire module
print("\n--- Method 1: Import entire module ---")
print(f"Math module functions: {dir(math)[:10]}...")  # Show first 10 items
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")

# Method 2: Import specific items
print("\n--- Method 2: Import specific items ---")
from math import sqrt, pi, factorial

print(f"Square root of 25: {sqrt(25)}")
print(f"Pi value: {pi}")
print(f"Factorial of 5: {factorial(5)}")

# Method 3: Import with alias
print("\n--- Method 3: Import with alias ---")
import random as rnd

print(f"Random number: {rnd.randint(1, 100)}")
print(f"Random choice from list: {rnd.choice(['apple', 'banana', 'cherry'])}")

# Method 4: Import specific items with alias
print("\n--- Method 4: Import specific items with alias ---")
from datetime import datetime as dt

print(f"Current time: {dt.now()}")

# Method 5: Import all items (not recommended)
print("\n--- Method 5: Import all items (not recommended) ---")
# from math import *  # This would import all math functions
# print(f"Square root: {sqrt(16)}")  # Would work but not recommended

# 3. MODULE SEARCH PATH
print("\n" + "=" * 50)
print("3. MODULE SEARCH PATH")
print("=" * 50)

print("Python searches for modules in these locations:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# 4. CREATING YOUR OWN MODULES
print("\n" + "=" * 50)
print("4. CREATING YOUR OWN MODULES")
print("=" * 50)


# Let's create a simple module structure
def create_sample_module():
    """Create a sample module file for demonstration"""
    module_content = '''"""
Sample module: math_utils.py
Contains mathematical utility functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def power(base, exponent):
    """Raise base to the power of exponent"""
    return base ** exponent

def is_even(number):
    """Check if number is even"""
    return number % 2 == 0

def is_prime(number):
    """Check if number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Module-level variables
PI = 3.14159
E = 2.71828

# Module-level function that runs when imported
def _init_module():
    print("Math utils module loaded!")

# This runs when the module is imported
if __name__ == "__main__":
    _init_module()
'''

    with open("03_Packages_Modules_Libraries_Tools/Examples/math_utils.py", "w") as f:
        f.write(module_content)

    print("Created sample module: math_utils.py")


create_sample_module()

# Now let's import and use our custom module
print("\n--- Using our custom module ---")
try:
    import sys

    sys.path.append("03_Packages_Modules_Libraries_Tools/Examples")

    import math_utils

    print(f"Addition: {math_utils.add(5, 3)}")
    print(f"Multiplication: {math_utils.multiply(4, 7)}")
    print(f"Power: {math_utils.power(2, 8)}")
    print(f"Is 7 even? {math_utils.is_even(7)}")
    print(f"Is 17 prime? {math_utils.is_prime(17)}")
    print(f"Module constants: PI={math_utils.PI}, E={math_utils.E}")

    # Import specific functions
    from math_utils import add, is_prime

    print(f"Direct import - add(10, 20): {add(10, 20)}")
    print(f"Direct import - is_prime(23): {is_prime(23)}")

except ImportError as e:
    print(f"Import error: {e}")

# 5. MODULE RELOADING
print("\n" + "=" * 50)
print("5. MODULE RELOADING")
print("=" * 50)

"""
Python caches imported modules. If you modify a module file,
you need to reload it to see changes.
"""

import importlib

# Example of reloading a module
print("Module reloading example:")
print("1. Import module")
print("2. Modify module file")
print("3. Use importlib.reload(module_name) to reload")

# 6. COMMON IMPORT PATTERNS
print("\n" + "=" * 50)
print("6. COMMON IMPORT PATTERNS")
print("=" * 50)

# Pattern 1: Standard library imports first
import os
import sys
import json
import pickle

# Pattern 2: Third-party imports
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# Pattern 3: Local imports
# from . import my_module
# from .my_module import my_function

# Pattern 4: Conditional imports
print("\n--- Conditional imports ---")
try:
    import numpy as np

    print("NumPy is available")
    print(f"NumPy version: {np.__version__}")
except ImportError:
    print("NumPy is not installed")

# 7. BEST PRACTICES
print("\n" + "=" * 50)
print("7. BEST PRACTICES")
print("=" * 50)

print(
    """
Best Practices for Python Imports:

1. Import Order:
   - Standard library imports
   - Third-party imports  
   - Local application imports
   - Separate each group with a blank line

2. Import Style:
   - Use absolute imports when possible
   - Avoid 'from module import *'
   - Use aliases for long module names
   - Import only what you need

3. Module Organization:
   - Keep modules focused on a single responsibility
   - Use descriptive module names
   - Include docstrings in modules
   - Use __all__ to control what gets imported with *

4. Performance:
   - Imports are cached, so import at module level
   - Use conditional imports for optional dependencies
   - Avoid circular imports
"""
)

# 8. ADVANCED IMPORT FEATURES
print("\n" + "=" * 50)
print("8. ADVANCED IMPORT FEATURES")
print("=" * 50)


# Using __all__ to control exports
def create_advanced_module():
    """Create a module with __all__ defined"""
    module_content = '''"""
Advanced module with __all__ defined
"""

def public_function():
    """This function is in __all__"""
    return "I'm public!"

def _private_function():
    """This function is not in __all__"""
    return "I'm private!"

def another_public_function():
    """This function is in __all__"""
    return "I'm also public!"

# Define what gets imported with 'from module import *'
__all__ = ['public_function', 'another_public_function']

# Module-level variable
PUBLIC_CONSTANT = 42
_PRIVATE_CONSTANT = 100
'''

    with open(
        "03_Packages_Modules_Libraries_Tools/Examples/advanced_module.py", "w"
    ) as f:
        f.write(module_content)

    print("Created advanced module with __all__ defined")


create_advanced_module()

# Demonstrate __all__ usage
print("\n--- __all__ demonstration ---")
try:
    from advanced_module import *

    print(f"public_function(): {public_function()}")
    print(f"another_public_function(): {another_public_function()}")
    print(f"PUBLIC_CONSTANT: {PUBLIC_CONSTANT}")

    # This would raise an error:
    # print(_private_function())  # Not in __all__

except ImportError as e:
    print(f"Import error: {e}")

# 9. PRACTICAL EXAMPLES
print("\n" + "=" * 50)
print("9. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Working with JSON
print("\n--- JSON Module Example ---")
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
}

# Serialize to JSON string
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# Deserialize from JSON string
parsed_data = json.loads(json_string)
print(f"\nParsed data type: {type(parsed_data)}")
print(f"Name: {parsed_data['name']}")

# Example 2: Working with collections
print("\n--- Collections Module Example ---")
from collections import defaultdict, Counter

# DefaultDict example
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    word_count[word] += 1
print(f"Word count: {dict(word_count)}")

# Counter example
word_counter = Counter(words)
print(f"Most common words: {word_counter.most_common(2)}")

# Example 3: Working with datetime
print("\n--- DateTime Module Example ---")
now = datetime.now()
print(f"Current time: {now}")
print(f"Formatted time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Add 5 days
future_date = now + timedelta(days=5)
print(f"Date in 5 days: {future_date.strftime('%Y-%m-%d')}")

# 10. COMMON PITFALLS AND SOLUTIONS
print("\n" + "=" * 50)
print("10. COMMON PITFALLS AND SOLUTIONS")
print("=" * 50)

print(
    """
Common Import Pitfalls:

1. Circular Imports:
   - Problem: Module A imports Module B, which imports Module A
   - Solution: Restructure code or use lazy imports

2. Import Errors:
   - Problem: Module not found in sys.path
   - Solution: Check PYTHONPATH or add to sys.path

3. Name Conflicts:
   - Problem: Imported name conflicts with local variable
   - Solution: Use aliases or be more specific with imports

4. Performance Issues:
   - Problem: Importing heavy modules unnecessarily
   - Solution: Use conditional imports or lazy loading

5. Version Conflicts:
   - Problem: Multiple versions of same module
   - Solution: Use virtual environments
"""
)

# 11. EXERCISES
print("\n" + "=" * 50)
print("11. EXERCISES")
print("=" * 50)

print(
    """
Exercises to practice:

1. Create a module with utility functions for string manipulation
2. Create a module that imports and uses multiple standard library modules
3. Practice different import styles with your own modules
4. Create a module with __all__ defined and test its behavior
5. Handle import errors gracefully in your code
6. Create a module that demonstrates conditional imports
"""
)

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MODULE TUTORIAL COMPLETED!")
    print("=" * 50)
    print("Check the Examples folder for sample modules created during this tutorial.")
