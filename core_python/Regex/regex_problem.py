"""
Problem: Regex Pattern Matching

Task:
Write a regex that extracts all words from a string that start with the letter "a" (case-insensitive).
"""

import re

def words_starting_with_a(text):
    """
    Extracts all words starting with 'a' or 'A' from the given text.
    """
    pattern = r'\b[aA]\w*'  # fill regex here
    return re.findall(pattern, text)


# Test case
print(words_starting_with_a("Apples are awesome and bananas are tasty"))

