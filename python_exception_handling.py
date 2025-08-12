# ============================================
# PYTHON EXCEPTION HANDLING TUTORIAL
# ============================================
# This file covers comprehensive exception handling in Python
# with examples, best practices, and real-world scenarios

print("=" * 60)
print("PYTHON EXCEPTION HANDLING TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO EXCEPTIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO EXCEPTIONS")
print("=" * 60)

print("\n1.1 What are Exceptions?")
print("-" * 30)
print("""
Exceptions are events that occur during the execution of a program
that disrupt the normal flow of the program's instructions.

When an exception occurs:
1. Python creates an exception object
2. The normal flow is interrupted
3. Python looks for exception handlers
4. If no handler is found, the program crashes

Common causes:
- Division by zero
- Accessing non-existent list index
- Converting invalid string to number
- Opening non-existent file
- Network connection errors
""")

print("\n1.2 Exception Hierarchy")
print("-" * 30)
print("""
BaseException (root of all exceptions)
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    ├── SyntaxError
    ├── TypeError
    ├── ValueError
    └── Warning
""")

# ============================================
# SECTION 2: BASIC EXCEPTION HANDLING
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: BASIC EXCEPTION HANDLING")
print("=" * 60)

print("\n2.1 Try-Except Block")
print("-" * 30)
# Basic try-except
try:
    result = 10 / 0
    print("This will never execute")
except ZeroDivisionError:
    print("Error: Division by zero!")

# Catching specific exceptions
try:
    number = int("abc")
except ValueError:
    print("Error: Cannot convert 'abc' to integer")

# Catching multiple exceptions
try:
    numbers = [1, 2, 3]
    print(numbers[10])
    result = 10 / 0
except (IndexError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

print("\n2.2 Try-Except-Else Block")
print("-" * 30)
try:
    number = int("42")
    print(f"Successfully converted: {number}")
except ValueError:
    print("Could not convert to integer")
else:
    print("No exception occurred - this is the else block")

print("\n2.3 Try-Except-Finally Block")
print("-" * 30)
try:
    file = open("nonexistent.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always executes, regardless of exceptions")

# ============================================
# SECTION 3: COMMON EXCEPTIONS AND EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: COMMON EXCEPTIONS AND EXAMPLES")
print("=" * 60)

print("\n3.1 ZeroDivisionError")
print("-" * 30)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

print("\n3.2 ValueError")
print("-" * 30)
try:
    age = int("twenty-five")
except ValueError as e:
    print(f"ValueError: {e}")

print("\n3.3 TypeError")
print("-" * 30)
try:
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

print("\n3.4 IndexError")
print("-" * 30)
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"IndexError: {e}")

print("\n3.5 KeyError")
print("-" * 30)
try:
    person = {"name": "John", "age": 30}
    print(person["city"])
except KeyError as e:
    print(f"KeyError: {e}")

print("\n3.6 NameError")
print("-" * 30)
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

print("\n3.7 AttributeError")
print("-" * 30)
try:
    text = "hello"
    text.append("world")
except AttributeError as e:
    print(f"AttributeError: {e}")

print("\n3.8 FileNotFoundError")
print("-" * 30)
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# ============================================
# SECTION 4: ADVANCED EXCEPTION HANDLING
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: ADVANCED EXCEPTION HANDLING")
print("=" * 60)

print("\n4.1 Multiple Except Clauses")
print("-" * 30)
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid data types!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test the function
print(f"10 / 2 = {divide_numbers(10, 2)}")
print(f"10 / 0 = {divide_numbers(10, 0)}")
print(f"'10' / 2 = {divide_numbers('10', 2)}")

print("\n4.2 Exception Chaining")
print("-" * 30)
try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid calculation") from e
except ValueError as e:
    print(f"Caught: {e}")
    print(f"Original exception: {e.__cause__}")

print("\n4.3 Custom Exceptions")
print("-" * 30)
class AgeError(Exception):
    """Custom exception for age-related errors"""
    pass

class InvalidAgeError(AgeError):
    """Raised when age is invalid"""
    pass

class TooYoungError(AgeError):
    """Raised when person is too young"""
    pass

def verify_age(age):
    if not isinstance(age, int):
        raise InvalidAgeError("Age must be an integer")
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age < 18:
        raise TooYoungError("Must be at least 18 years old")
    return True

# Test custom exceptions
try:
    verify_age(15)
except TooYoungError as e:
    print(f"TooYoungError: {e}")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")

print("\n4.4 Context Managers and Exceptions")
print("-" * 30)
class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name
        print(f"Connecting to {database_name}...")
    
    def __enter__(self):
        print("Connection established")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Connection closed")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress the exception

# Using context manager
try:
    with DatabaseConnection("my_database") as db:
        print("Performing database operations...")
        raise ValueError("Database operation failed")
except ValueError as e:
    print(f"Caught: {e}")

# ============================================
# SECTION 5: REAL-WORLD EXAMPLES
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: REAL-WORLD EXAMPLES")
print("=" * 60)

print("\n5.1 File Processing with Error Handling")
print("-" * 30)
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return []
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file '{filename}'")
        return []
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return []

# Test file processing
result = process_file("nonexistent.txt")
print(f"Result: {result}")

print("\n5.2 Network Request with Retry Logic")
print("-" * 30)
import time
import random

def make_network_request(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            # Simulate network request
            if random.random() < 0.7:  # 70% chance of success
                print(f"Successfully connected to {url}")
                return "Data received"
            else:
                raise ConnectionError("Network timeout")
        except ConnectionError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {2 ** attempt} seconds...")
                time.sleep(2 ** attempt)
            else:
                print("Max retries reached")
                raise

# Test network request
try:
    result = make_network_request("https://api.example.com")
    print(f"Result: {result}")
except ConnectionError as e:
    print(f"Final error: {e}")

print("\n5.3 Data Validation with Multiple Checks")
print("-" * 30)
class ValidationError(Exception):
    pass

def validate_user_data(data):
    errors = []
    
    # Check required fields
    required_fields = ['name', 'email', 'age']
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    # Validate email format
    if 'email' in data and '@' not in data['email']:
        errors.append("Invalid email format")
    
    # Validate age
    if 'age' in data:
        try:
            age = int(data['age'])
            if age < 0 or age > 120:
                errors.append("Age must be between 0 and 120")
        except ValueError:
            errors.append("Age must be a number")
    
    if errors:
        raise ValidationError(f"Validation failed: {'; '.join(errors)}")
    
    return True

# Test validation
test_cases = [
    {"name": "John", "email": "john@example.com", "age": "25"},
    {"name": "Jane", "email": "invalid-email", "age": "30"},
    {"name": "Bob", "age": "150"},
    {"name": "Alice", "email": "alice@example.com", "age": "abc"}
]

for i, data in enumerate(test_cases, 1):
    try:
        validate_user_data(data)
        print(f"Case {i}: Valid data")
    except ValidationError as e:
        print(f"Case {i}: {e}")

print("\n5.4 Calculator with Comprehensive Error Handling")
print("-" * 30)
class CalculatorError(Exception):
    pass

def calculator(operation, a, b):
    try:
        # Validate inputs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise CalculatorError("Both operands must be numbers")
        
        # Perform operation
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                raise CalculatorError("Division by zero is not allowed")
            return a / b
        elif operation == "power":
            if a == 0 and b < 0:
                raise CalculatorError("Zero to negative power is undefined")
            return a ** b
        else:
            raise CalculatorError(f"Unknown operation: {operation}")
    
    except CalculatorError:
        raise
    except Exception as e:
        raise CalculatorError(f"Unexpected error: {e}")

# Test calculator
test_operations = [
    ("add", 10, 5),
    ("subtract", 10, 5),
    ("multiply", 10, 5),
    ("divide", 10, 0),
    ("power", 2, 3),
    ("unknown", 10, 5),
    ("add", "10", 5)
]

for operation, a, b in test_operations:
    try:
        result = calculator(operation, a, b)
        print(f"{a} {operation} {b} = {result}")
    except CalculatorError as e:
        print(f"Calculator error: {e}")

# ============================================
# SECTION 6: BEST PRACTICES
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: BEST PRACTICES")
print("=" * 60)

print("\n6.1 Exception Handling Guidelines")
print("-" * 30)
print("""
1. BE SPECIFIC: Catch specific exceptions, not generic ones
   Good: except ValueError:
   Bad:  except Exception:

2. DON'T SUPPRESS EXCEPTIONS: Always handle or log them
   Good: except ValueError as e: print(f"Error: {e}")
   Bad:  except: pass

3. USE FINALLY FOR CLEANUP: Always clean up resources
   Good: finally: file.close()
   Bad:  No cleanup

4. RAISE MEANINGFUL EXCEPTIONS: Provide clear error messages
   Good: raise ValueError("Age must be positive")
   Bad:  raise ValueError("Invalid input")

5. DOCUMENT EXCEPTIONS: Let users know what exceptions to expect
   Good: """This function may raise ValueError if input is invalid"""
   Bad:  No documentation
""")

print("\n6.2 Common Anti-Patterns")
print("-" * 30)
print("""
ANTI-PATTERN 1: Bare except clause
try:
    risky_operation()
except:  # Catches ALL exceptions, including SystemExit
    print("Something went wrong")

ANTI-PATTERN 2: Catching and ignoring
try:
    risky_operation()
except Exception:
    pass  # Silent failure

ANTI-PATTERN 3: Exception handling in wrong place
def process_data(data):
    try:
        return data * 2
    except TypeError:
        return None  # Should validate input first

ANTI-PATTERN 4: Overly broad exception handling
try:
    result = complex_operation()
except Exception as e:
    print(f"Error: {e}")  # Too generic
""")

print("\n6.3 Good Exception Handling Patterns")
print("-" * 30)
print("""
PATTERN 1: EAFP (Easier to Ask for Forgiveness than Permission)
try:
    value = my_dict[key]
except KeyError:
    value = default_value

PATTERN 2: LBYL (Look Before You Leap)
if key in my_dict:
    value = my_dict[key]
else:
    value = default_value

PATTERN 3: Resource management with context managers
with open('file.txt') as f:
    data = f.read()

PATTERN 4: Custom exceptions for domain-specific errors
class InsufficientFundsError(Exception):
    pass

PATTERN 5: Exception chaining for debugging
try:
    process_data()
except ValueError as e:
    raise ProcessingError("Failed to process data") from e
""")

print("\n6.4 Logging Exceptions")
print("-" * 30)
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_with_logging(data):
    try:
        result = int(data)
        logging.info(f"Successfully processed: {result}")
        return result
    except ValueError as e:
        logging.error(f"Failed to process '{data}': {e}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error processing '{data}': {e}")
        raise

# Test logging
try:
    process_with_logging("42")
    process_with_logging("abc")
except Exception:
    pass  # Exception already logged

# ============================================
# SECTION 7: DEBUGGING AND TESTING
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: DEBUGGING AND TESTING")
print("=" * 60)

print("\n7.1 Using Assertions")
print("-" * 30)
def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    assert isinstance(a, (int, float)), "First argument must be a number"
    assert isinstance(b, (int, float)), "Second argument must be a number"
    return a / b

# Test assertions
try:
    result = divide(10, 2)
    print(f"10 / 2 = {result}")
except AssertionError as e:
    print(f"Assertion failed: {e}")

try:
    result = divide(10, 0)
except AssertionError as e:
    print(f"Assertion failed: {e}")

print("\n7.2 Exception Testing")
print("-" * 30)
import unittest

class TestCalculator(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            10 / 0
    
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            "hello" + 5
    
    def test_custom_exception(self):
        with self.assertRaises(ValueError):
            int("abc")

# Run tests
if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)

print("\n7.3 Debugging with Traceback")
print("-" * 30)
import traceback

def debug_function():
    try:
        # Simulate an error
        result = 10 / 0
    except Exception as e:
        print(f"Exception: {e}")
        print("Traceback:")
        traceback.print_exc()

debug_function()

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
🎯 WHAT YOU'VE LEARNED:

1. EXCEPTION BASICS
   - What exceptions are and why they occur
   - Python's exception hierarchy
   - Basic try-except blocks

2. COMMON EXCEPTIONS
   - ZeroDivisionError, ValueError, TypeError
   - IndexError, KeyError, NameError
   - AttributeError, FileNotFoundError

3. ADVANCED HANDLING
   - Multiple except clauses
   - Exception chaining
   - Custom exceptions
   - Context managers

4. REAL-WORLD APPLICATIONS
   - File processing with error handling
   - Network requests with retry logic
   - Data validation
   - Calculator with comprehensive error handling

5. BEST PRACTICES
   - Specific exception handling
   - Proper resource cleanup
   - Meaningful error messages
   - Logging exceptions

6. DEBUGGING AND TESTING
   - Using assertions
   - Exception testing
   - Traceback debugging

KEY TAKEAWAYS:
- Always handle exceptions appropriately
- Use specific exception types
- Clean up resources in finally blocks
- Log exceptions for debugging
- Write custom exceptions for domain-specific errors
- Test exception handling thoroughly

To run this tutorial: python python_exception_handling.py
""")

print("\nHappy coding with robust exception handling! 🐍🛡️")
print("Remember: Good error handling makes your code more reliable!") 