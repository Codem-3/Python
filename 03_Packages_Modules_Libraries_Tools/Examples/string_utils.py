"""
String Utilities Module
======================

A collection of useful string manipulation functions.
"""

import re
from typing import List, Dict, Any


def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
    """
    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a string.

    Args:
        text: The string to count vowels in

    Returns:
        The number of vowels

    Examples:
        >>> count_vowels("hello world")
        3
        >>> count_vowels("bcdfg")
        0
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        text: The string to check

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


def format_phone_number(phone: str) -> str:
    """
    Format a phone number into a standard format.

    Args:
        phone: The phone number string

    Returns:
        Formatted phone number

    Examples:
        >>> format_phone_number("1234567890")
        '(123) 456-7890'
        >>> format_phone_number("123-456-7890")
        '(123) 456-7890'
    """
    # Remove all non-digit characters
    digits = re.sub(r"[^\d]", "", phone)

    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == "1":
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        raise ValueError("Invalid phone number format")


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        text: The string to capitalize

    Returns:
        String with capitalized words

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming")
        'Python Programming'
    """
    return " ".join(word.capitalize() for word in text.split())


def remove_duplicates(text: str) -> str:
    """
    Remove duplicate characters from a string while preserving order.

    Args:
        text: The string to remove duplicates from

    Returns:
        String with duplicates removed

    Examples:
        >>> remove_duplicates("hello")
        'helo'
        >>> remove_duplicates("programming")
        'progamin'
    """
    seen = set()
    result = []

    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)


def count_words(text: str) -> int:
    """
    Count the number of words in a string.

    Args:
        text: The string to count words in

    Returns:
        The number of words

    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("")
        0
    """
    if not text.strip():
        return 0
    return len(text.split())


def find_longest_word(text: str) -> str:
    """
    Find the longest word in a string.

    Args:
        text: The string to search in

    Returns:
        The longest word

    Examples:
        >>> find_longest_word("hello world programming")
        'programming'
    """
    if not text.strip():
        return ""

    words = text.split()
    return max(words, key=len)


def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams.

    Args:
        str1: First string
        str2: Second string

    Returns:
        True if strings are anagrams, False otherwise

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    """
    # Remove spaces and convert to lowercase
    str1_clean = re.sub(r"\s", "", str1.lower())
    str2_clean = re.sub(r"\s", "", str2.lower())

    return sorted(str1_clean) == sorted(str2_clean)


def extract_numbers(text: str) -> List[int]:
    """
    Extract all numbers from a string.

    Args:
        text: The string to extract numbers from

    Returns:
        List of numbers found in the string

    Examples:
        >>> extract_numbers("I have 5 apples and 3 oranges")
        [5, 3]
        >>> extract_numbers("No numbers here")
        []
    """
    numbers = re.findall(r"\d+", text)
    return [int(num) for num in numbers]


def validate_email(email: str) -> bool:
    """
    Validate an email address format.

    Args:
        email: The email address to validate

    Returns:
        True if valid email format, False otherwise

    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.

    Args:
        text: The text to truncate
        max_length: Maximum length of the result
        suffix: Suffix to add if text is truncated

    Returns:
        Truncated text

    Examples:
        >>> truncate_text("This is a very long text", 10)
        'This is a...'
        >>> truncate_text("Short text", 20)
        'Short text'
    """
    if len(text) <= max_length:
        return text

    return text[: max_length - len(suffix)] + suffix


def word_frequency(text: str) -> Dict[str, int]:
    """
    Count the frequency of each word in a text.

    Args:
        text: The text to analyze

    Returns:
        Dictionary with words as keys and frequencies as values

    Examples:
        >>> word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    words = text.lower().split()
    frequency = {}

    for word in words:
        # Remove punctuation
        word = re.sub(r"[^\w]", "", word)
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


if __name__ == "__main__":
    # Test the functions
    print("Testing string utilities...")

    # Test reverse_string
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""

    # Test count_vowels
    assert count_vowels("hello world") == 3
    assert count_vowels("bcdfg") == 0

    # Test is_palindrome
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

    # Test format_phone_number
    assert format_phone_number("1234567890") == "(123) 456-7890"

    print("All tests passed!")
