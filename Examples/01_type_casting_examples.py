# Type Casting Examples in Python
# This file demonstrates various type casting techniques

print("=== TYPE CASTING EXAMPLES ===\n")

# 1. String to Integer
print("1. String to Integer:")
string_number = "42"
integer_number = int(string_number)
print(f"Original: '{string_number}' (type: {type(string_number)})")
print(f"After int(): {integer_number} (type: {type(integer_number)})")
print()

# 2. String to Float
print("2. String to Float:")
string_decimal = "3.14"
float_number = float(string_decimal)
print(f"Original: '{string_decimal}' (type: {type(string_decimal)})")
print(f"After float(): {float_number} (type: {type(float_number)})")
print()

# 3. Integer to String
print("3. Integer to String:")
number = 100
string_result = str(number)
print(f"Original: {number} (type: {type(number)})")
print(f"After str(): '{string_result}' (type: {type(string_result)})")
print()

# 4. Float to Integer (truncation)
print("4. Float to Integer (truncation):")
decimal_num = 3.99
truncated = int(decimal_num)
print(f"Original: {decimal_num} (type: {type(decimal_num)})")
print(f"After int(): {truncated} (type: {type(truncated)})")
print()

# 5. Boolean conversion examples
print("5. Boolean conversion examples:")
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(''): {bool('')}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([]): {bool([])}")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")
print()

# 6. List to String
print("6. List to String:")
my_list = [1, 2, 3, 4, 5]
list_string = str(my_list)
print(f"Original: {my_list} (type: {type(my_list)})")
print(f"After str(): '{list_string}' (type: {type(list_string)})")
print()

# 7. String to List (character by character)
print("7. String to List (character by character):")
text = "Python"
char_list = list(text)
print(f"Original: '{text}' (type: {type(text)})")
print(f"After list(): {char_list} (type: {type(char_list)})")
print()

# 8. Tuple conversion
print("8. Tuple conversion:")
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"Original list: {my_list} (type: {type(my_list)})")
print(f"After tuple(): {my_tuple} (type: {type(my_tuple)})")
print()

# 9. Set conversion
print("9. Set conversion:")
my_list = [1, 2, 2, 3, 3, 4]
my_set = set(my_list)
print(f"Original list: {my_list} (type: {type(my_list)})")
print(f"After set(): {my_set} (type: {type(my_set)})")
print()

# 10. Complex number conversion
print("10. Complex number conversion:")
real_part = 3
imaginary_part = 4
complex_num = complex(real_part, imaginary_part)
print(f"Real part: {real_part}, Imaginary part: {imaginary_part}")
print(f"After complex(): {complex_num} (type: {type(complex_num)})")
print()

# 11. Error handling examples
print("11. Error handling examples:")
print("Trying to convert invalid strings:")

try:
    invalid_int = int("abc")
except ValueError as e:
    print(f"Error converting 'abc' to int: {e}")

try:
    invalid_float = float("not a number")
except ValueError as e:
    print(f"Error converting 'not a number' to float: {e}")

print()

# 12. Practical example: Calculator with type casting
print("12. Practical example: Calculator with type casting")
print("Enter two numbers to add them together:")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
    print(f"Result type: {type(result)}")

except ValueError:
    print("Error: Please enter valid numbers!")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n=== END OF EXAMPLES ===")
