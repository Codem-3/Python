# ============================================
# PYTHON STRING REVERSAL TUTORIAL
# ============================================
# This file covers different methods to reverse strings in Python
# with examples, performance analysis, and real-world applications

print("=" * 60)
print("PYTHON STRING REVERSAL TUTORIAL")
print("=" * 60)

# ============================================
# SECTION 1: INTRODUCTION TO STRING REVERSAL
# ============================================
print("\n" + "=" * 60)
print("SECTION 1: INTRODUCTION TO STRING REVERSAL")
print("=" * 60)

print("\n1.1 What is String Reversal?")
print("-" * 30)
print(
    """
String reversal is the process of changing the order of characters in a string
so that the last character becomes the first, the second-to-last becomes the second, and so on.

Examples:
- "hello" -> "olleh"
- "python" -> "nohtyp"
- "racecar" -> "racecar" (palindrome)
- "12345" -> "54321"

Common use cases:
- Palindrome checking
- Data encryption/decryption
- Text processing
- Algorithm problems
- String manipulation
"""
)

print("\n1.2 Why Learn String Reversal?")
print("-" * 30)
print(
    """
1. Interview Questions: Common in coding interviews
2. Algorithm Problems: Foundation for more complex algorithms
3. Text Processing: Useful in data analysis and NLP
4. Security: Basic encryption techniques
5. Problem Solving: Improves logical thinking
6. Python Skills: Understanding string manipulation
"""
)

# ============================================
# SECTION 2: BASIC STRING REVERSAL METHODS
# ============================================
print("\n" + "=" * 60)
print("SECTION 2: BASIC STRING REVERSAL METHODS")
print("=" * 60)

print("\n2.1 Using String Slicing")
print("-" * 30)


def reverse_string_slicing(text):
    """
    Reverse string using slicing
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return text[::-1]


# Test slicing method
test_strings = ["hello", "python", "racecar", "12345", ""]
print("String reversal using slicing:")
for text in test_strings:
    reversed_text = reverse_string_slicing(text)
    print(f"'{text}' -> '{reversed_text}'")

print("\n2.2 Using reversed() Function")
print("-" * 30)


def reverse_string_reversed(text):
    """
    Reverse string using reversed() function
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return "".join(reversed(text))


# Test reversed() method
print("String reversal using reversed() function:")
for text in test_strings:
    reversed_text = reverse_string_reversed(text)
    print(f"'{text}' -> '{reversed_text}'")

print("\n2.3 Using Loop Method")
print("-" * 30)


def reverse_string_loop(text):
    """
    Reverse string using a loop
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


# Test loop method
print("String reversal using loop:")
for text in test_strings:
    reversed_text = reverse_string_loop(text)
    print(f"'{text}' -> '{reversed_text}'")

print("\n2.4 Using List Method")
print("-" * 30)


def reverse_string_list(text):
    """
    Reverse string using list conversion
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    char_list = list(text)
    char_list.reverse()
    return "".join(char_list)


# Test list method
print("String reversal using list:")
for text in test_strings:
    reversed_text = reverse_string_list(text)
    print(f"'{text}' -> '{reversed_text}'")

# ============================================
# SECTION 3: ADVANCED REVERSAL TECHNIQUES
# ============================================
print("\n" + "=" * 60)
print("SECTION 3: ADVANCED REVERSAL TECHNIQUES")
print("=" * 60)

print("\n3.1 Recursive String Reversal")
print("-" * 30)


def reverse_string_recursive(text):
    """
    Reverse string using recursion
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if len(text) <= 1:
        return text
    return text[-1] + reverse_string_recursive(text[:-1])


# Test recursive method
print("String reversal using recursion:")
for text in test_strings:
    reversed_text = reverse_string_recursive(text)
    print(f"'{text}' -> '{reversed_text}'")

print("\n3.2 Two-Pointer Technique")
print("-" * 30)


def reverse_string_two_pointer(text):
    """
    Reverse string using two-pointer technique
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    char_list = list(text)
    left, right = 0, len(char_list) - 1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    return "".join(char_list)


# Test two-pointer method
print("String reversal using two-pointer technique:")
for text in test_strings:
    reversed_text = reverse_string_two_pointer(text)
    print(f"'{text}' -> '{reversed_text}'")

print("\n3.3 Stack-Based Reversal")
print("-" * 30)


def reverse_string_stack(text):
    """
    Reverse string using stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    for char in text:
        stack.append(char)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    return reversed_text


# Test stack method
print("String reversal using stack:")
for text in test_strings:
    reversed_text = reverse_string_stack(text)
    print(f"'{text}' -> '{reversed_text}'")

# ============================================
# SECTION 4: SPECIALIZED REVERSAL SCENARIOS
# ============================================
print("\n" + "=" * 60)
print("SECTION 4: SPECIALIZED REVERSAL SCENARIOS")
print("=" * 60)

print("\n4.1 Reverse Words in a String")
print("-" * 30)


def reverse_words(text):
    """
    Reverse the order of words in a string
    Example: "hello world" -> "world hello"
    """
    words = text.split()
    return " ".join(words[::-1])


def reverse_words_keep_order(text):
    """
    Reverse each word but keep word order
    Example: "hello world" -> "olleh dlrow"
    """
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


# Test word reversal
test_sentences = [
    "hello world",
    "python programming is fun",
    "racecar is a palindrome",
    "123 456 789",
]

print("Reversing word order:")
for sentence in test_sentences:
    reversed_sentence = reverse_words(sentence)
    print(f"'{sentence}' -> '{reversed_sentence}'")

print("\nReversing each word:")
for sentence in test_sentences:
    reversed_sentence = reverse_words_keep_order(sentence)
    print(f"'{sentence}' -> '{reversed_sentence}'")

print("\n4.2 Reverse Only Letters (Keep Numbers and Symbols)")
print("-" * 30)


def reverse_only_letters(text):
    """
    Reverse only letters, keep numbers and symbols in place
    Example: "a1b2c" -> "c1b2a"
    """
    letters = [char for char in text if char.isalpha()]
    letters.reverse()

    result = []
    letter_index = 0

    for char in text:
        if char.isalpha():
            result.append(letters[letter_index])
            letter_index += 1
        else:
            result.append(char)

    return "".join(result)


# Test letter-only reversal
test_mixed = ["a1b2c", "test123!", "hello@world#", "abc123def"]
print("Reversing only letters:")
for text in test_mixed:
    reversed_text = reverse_only_letters(text)
    print(f"'{text}' -> '{reversed_text}'")

print("\n4.3 Reverse String with Special Characters")
print("-" * 30)


def reverse_with_special_chars(text):
    """
    Reverse string while preserving special character positions
    Example: "a@b#c" -> "c@b#a"
    """
    char_list = list(text)
    left, right = 0, len(char_list) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not char_list[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from right
        while left < right and not char_list[right].isalnum():
            right -= 1

        # Swap alphanumeric characters
        if left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1

    return "".join(char_list)


# Test special character reversal
test_special = ["a@b#c", "hello@world!", "test#123$", "a!b@c#d"]
print("Reversing with special characters:")
for text in test_special:
    reversed_text = reverse_with_special_chars(text)
    print(f"'{text}' -> '{reversed_text}'")

# ============================================
# SECTION 5: PALINDROME DETECTION
# ============================================
print("\n" + "=" * 60)
print("SECTION 5: PALINDROME DETECTION")
print("=" * 60)

print("\n5.1 Basic Palindrome Check")
print("-" * 30)


def is_palindrome(text):
    """
    Check if a string is a palindrome
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return text == text[::-1]


def is_palindrome_loop(text):
    """
    Check palindrome using loop
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


# Test palindrome detection
palindrome_tests = [
    "racecar",
    "level",
    "deed",
    "hello",
    "python",
    "a",
    "",
    "12321",
    "madam",
    "noon",
]

print("Palindrome detection:")
for text in palindrome_tests:
    is_pal = is_palindrome(text)
    print(f"'{text}' -> {'Palindrome' if is_pal else 'Not Palindrome'}")

print("\n5.2 Case-Insensitive Palindrome")
print("-" * 30)


def is_palindrome_case_insensitive(text):
    """
    Check palindrome ignoring case
    """
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


# Test case-insensitive palindrome
case_tests = [
    "Racecar",
    "A man a plan a canal Panama",
    "Madam, I'm Adam",
    "Hello World",
    "No 'x' in Nixon",
]

print("Case-insensitive palindrome detection:")
for text in case_tests:
    is_pal = is_palindrome_case_insensitive(text)
    print(f"'{text}' -> {'Palindrome' if is_pal else 'Not Palindrome'}")

print("\n5.3 Longest Palindromic Substring")
print("-" * 30)


def longest_palindrome_substring(text):
    """
    Find the longest palindromic substring
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if not text:
        return ""

    start, max_length = 0, 1

    def expand_around_center(left, right):
        nonlocal start, max_length
        while left >= 0 and right < len(text) and text[left] == text[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    for i in range(len(text)):
        # Check odd length palindromes
        expand_around_center(i, i)
        # Check even length palindromes
        expand_around_center(i, i + 1)

    return text[start : start + max_length]


# Test longest palindromic substring
longest_palindrome_tests = ["babad", "cbbd", "racecar", "hello", "abacdfgdcaba"]

print("Longest palindromic substring:")
for text in longest_palindrome_tests:
    longest_pal = longest_palindrome_substring(text)
    print(f"'{text}' -> '{longest_pal}'")

# ============================================
# SECTION 6: PERFORMANCE ANALYSIS
# ============================================
print("\n" + "=" * 60)
print("SECTION 6: PERFORMANCE ANALYSIS")
print("=" * 60)

print("\n6.1 Time Complexity Comparison")
print("-" * 30)

import time
import random
import string


def generate_random_string(length):
    """Generate a random string of given length"""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def measure_time(func, text, iterations=1000):
    """Measure execution time of a function"""
    start_time = time.time()
    for _ in range(iterations):
        func(text)
    end_time = time.time()
    return (end_time - start_time) / iterations


# Test different string lengths
string_lengths = [10, 100, 1000, 10000]
methods = [
    ("Slicing", reverse_string_slicing),
    ("Reversed", reverse_string_reversed),
    ("Loop", reverse_string_loop),
    ("List", reverse_string_list),
    ("Recursive", reverse_string_recursive),
    ("Two-Pointer", reverse_string_two_pointer),
    ("Stack", reverse_string_stack),
]

print("Performance comparison (seconds per operation):")
print(
    f"{'Length':<8} {'Slicing':<10} {'Reversed':<10} {'Loop':<10} {'List':<10} {'Two-Pointer':<12} {'Stack':<10}"
)
print("-" * 80)

for length in string_lengths:
    test_string = generate_random_string(length)
    times = []

    for name, method in methods:
        if (
            length <= 1000 or name != "Recursive"
        ):  # Skip recursive for very long strings
            time_taken = measure_time(
                method, test_string, 100 if length > 1000 else 1000
            )
            times.append(f"{time_taken:.8f}")
        else:
            times.append("N/A")

    print(
        f"{length:<8} {times[0]:<10} {times[1]:<10} {times[2]:<10} {times[3]:<10} {times[4]:<12} {times[5]:<10}"
    )

print("\n6.2 Memory Usage Analysis")
print("-" * 30)
print(
    """
Memory Usage Analysis:

1. Slicing Method: O(n) - Creates a new string
2. Reversed Method: O(n) - Creates a new string
3. Loop Method: O(n) - Creates a new string
4. List Method: O(n) - Creates a list and new string
5. Recursive Method: O(n) - Uses recursion stack
6. Two-Pointer Method: O(n) - Creates a list and new string
7. Stack Method: O(n) - Uses stack and creates new string

All methods have O(n) space complexity, but:
- Slicing is most memory efficient for strings
- Recursive method uses additional stack space
- List and two-pointer methods use extra list space
"""
)

# ============================================
# SECTION 7: REAL-WORLD APPLICATIONS
# ============================================
print("\n" + "=" * 60)
print("SECTION 7: REAL-WORLD APPLICATIONS")
print("=" * 60)

print("\n7.1 Text Encryption/Decryption")
print("-" * 30)


def simple_encrypt(text, key):
    """Simple encryption using string reversal"""
    reversed_text = text[::-1]
    encrypted = ""
    for char in reversed_text:
        if char.isalpha():
            # Shift character by key
            shifted = chr((ord(char.lower()) - ord("a") + key) % 26 + ord("a"))
            encrypted += shifted.upper() if char.isupper() else shifted
        else:
            encrypted += char
    return encrypted


def simple_decrypt(encrypted_text, key):
    """Simple decryption using string reversal"""
    decrypted = ""
    for char in encrypted_text:
        if char.isalpha():
            # Reverse shift
            shifted = chr((ord(char.lower()) - ord("a") - key) % 26 + ord("a"))
            decrypted += shifted.upper() if char.isupper() else shifted
        else:
            decrypted += char
    return decrypted[::-1]


# Test encryption/decryption
original_text = "Hello, World! 123"
key = 3
encrypted = simple_encrypt(original_text, key)
decrypted = simple_decrypt(encrypted, key)

print("Simple encryption/decryption:")
print(f"Original: '{original_text}'")
print(f"Encrypted: '{encrypted}'")
print(f"Decrypted: '{decrypted}'")

print("\n7.2 Data Validation")
print("-" * 30)


def validate_reverse_operation(original, reversed_text):
    """Validate if reversal operation is correct"""
    expected = original[::-1]
    is_correct = reversed_text == expected
    return is_correct, expected


def validate_palindrome_input(text):
    """Validate if input is a valid palindrome candidate"""
    if not isinstance(text, str):
        return False, "Input must be a string"

    if len(text) == 0:
        return True, "Empty string is a palindrome"

    # Check if contains only alphanumeric characters
    alphanumeric = "".join(char.lower() for char in text if char.isalnum())
    if len(alphanumeric) == 0:
        return False, "No alphanumeric characters found"

    return True, "Valid input"


# Test validation
validation_tests = [
    ("hello", "olleh"),
    ("python", "nohtyp"),
    ("racecar", "racecar"),
    ("test", "tset"),
    ("", ""),
]

print("Validation tests:")
for original, reversed_text in validation_tests:
    is_valid, expected = validate_reverse_operation(original, reversed_text)
    status = "✓" if is_valid else "✗"
    print(f"{status} '{original}' -> '{reversed_text}' (Expected: '{expected}')")

print("\n7.3 String Processing Pipeline")
print("-" * 30)


class StringProcessor:
    """String processing pipeline with reversal operations"""

    def __init__(self):
        self.operations = []

    def add_operation(self, operation_name, operation_func):
        """Add an operation to the pipeline"""
        self.operations.append((operation_name, operation_func))

    def process(self, text):
        """Process text through all operations"""
        result = text
        for name, func in self.operations:
            result = func(result)
            print(f"After {name}: '{result}'")
        return result


# Create processing pipeline
processor = StringProcessor()
processor.add_operation("Reverse", lambda x: x[::-1])
processor.add_operation("Uppercase", lambda x: x.upper())
processor.add_operation("Remove spaces", lambda x: x.replace(" ", ""))

# Test pipeline
test_text = "hello world"
print("String processing pipeline:")
final_result = processor.process(test_text)
print(f"Final result: '{final_result}'")

# ============================================
# SECTION 8: BEST PRACTICES AND TIPS
# ============================================
print("\n" + "=" * 60)
print("SECTION 8: BEST PRACTICES AND TIPS")
print("=" * 60)

print("\n8.1 Choosing the Right Method")
print("-" * 30)
print(
    """
When to use each method:

1. String Slicing (text[::-1]):
   - ✅ Most readable and Pythonic
   - ✅ Fastest for most cases
   - ✅ Works with any string
   - ❌ Creates a new string

2. reversed() Function:
   - ✅ Memory efficient for large strings
   - ✅ Works with iterables
   - ✅ Good for one-time iteration
   - ❌ Slightly more verbose

3. Loop Method:
   - ✅ Easy to understand
   - ✅ Good for learning
   - ✅ Can be modified for special cases
   - ❌ Slower than slicing

4. Recursive Method:
   - ✅ Elegant for small strings
   - ✅ Good for learning recursion
   - ❌ Stack overflow for large strings
   - ❌ Slower than iterative methods

5. Two-Pointer Technique:
   - ✅ In-place modification possible
   - ✅ Good for special cases
   - ✅ Efficient for certain scenarios
   - ❌ More complex implementation
"""
)

print("\n8.2 Common Mistakes to Avoid")
print("-" * 30)
print(
    """
1. Modifying strings in place:
   - Strings are immutable in Python
   - Always create new strings

2. Forgetting edge cases:
   - Empty strings
   - Single character strings
   - Strings with special characters

3. Ignoring performance:
   - Use slicing for simple cases
   - Consider memory usage for large strings

4. Not handling Unicode:
   - Some methods may not work with Unicode
   - Test with different character sets

5. Overcomplicating simple tasks:
   - Use slicing for basic reversal
   - Only use complex methods when needed
"""
)

print("\n8.3 Optimization Tips")
print("-" * 30)
print(
    """
1. Use slicing for simple reversal:
   text[::-1] is the most efficient

2. Avoid unnecessary conversions:
   Don't convert to list unless needed

3. Use appropriate data structures:
   - Stack for complex operations
   - Two-pointer for in-place operations

4. Consider memory usage:
   - Use generators for large strings
   - Avoid recursion for very long strings

5. Profile your code:
   - Measure performance for your use case
   - Choose method based on requirements
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

1. BASIC REVERSAL METHODS
   - String slicing: text[::-1]
   - reversed() function: ''.join(reversed(text))
   - Loop method: character by character
   - List method: convert to list and reverse

2. ADVANCED TECHNIQUES
   - Recursive reversal
   - Two-pointer technique
   - Stack-based reversal
   - Specialized scenarios

3. SPECIALIZED SCENARIOS
   - Word reversal in sentences
   - Letter-only reversal
   - Handling special characters
   - Case-insensitive operations

4. PALINDROME DETECTION
   - Basic palindrome checking
   - Case-insensitive palindromes
   - Longest palindromic substring
   - Palindrome validation

5. PERFORMANCE ANALYSIS
   - Time complexity comparison
   - Memory usage analysis
   - Method selection guidelines
   - Optimization tips

6. REAL-WORLD APPLICATIONS
   - Text encryption/decryption
   - Data validation
   - String processing pipelines
   - Practical use cases

7. BEST PRACTICES
   - Method selection criteria
   - Common mistakes to avoid
   - Optimization techniques
   - Code quality guidelines

🚀 KEY TAKEAWAYS:
- String slicing is the most Pythonic and efficient method
- Choose the right method based on your specific needs
- Consider performance for large strings
- Handle edge cases and special characters
- Use palindromes for validation and testing
- Apply string reversal in real-world scenarios

To run this tutorial: python python_string_reversal.py
"""
)

print("\nHappy coding with Python string reversal! 🐍🔄")
print("Remember: The right method makes all the difference!")
