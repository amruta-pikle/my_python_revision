"""
copy_demo.py

Problem Statement:
------------------
Demonstrate the difference between shallow and deep copy in Python.

Requirements:
1. Create a nested list (list of lists).
2. Perform a shallow copy and show that changes to inner lists
   reflect in both copies.
3. Perform a deep copy and show that changes do not affect the original.
"""

import copy


def shallow_copy_demo():
    """Show how shallow copy behaves with nested lists."""
    original = [[1,2],[3,4]]
    shallow = copy.copy(original)

    print("Original:", original)
    print("Shallow:", shallow)

    shallow[0][0] = 99
    print("\nAfter modifying shallow copy (inner list):")
    print("Original:", original)
    print("Shallow:", shallow)
def deep_copy_demo():
    """Show how deep copy behaves with nested lists."""

    original = [[1,2],[3,4]]
    deep = copy.deepcopy(original)

    print("\nOriginal:", original)
    print("Deep:", deep)

    # Modify inner list
    deep[0][0] = 99
    print("\nAfter modifying deep copy (inner list):")
    print("Original:", original)
    print("Deep:", deep)

if __name__ == "__main__":
    # Demo usage
    print("=== Shallow Copy Demo ===")
    shallow_copy_demo()

    print("\n=== Deep Copy Demo ===")
    deep_copy_demo()
