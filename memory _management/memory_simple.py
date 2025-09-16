"""
Problem:
1. Show difference between mutable (list) and immutable (tuple).
2. Show shallow vs deep copy using nested lists.
"""

import copy

def mutable_vs_immutable():
    print("Mutable vs Immutable:")

    # Mutable (list)
    a = [1, 2, 3]
    b = a
    b.append(4)
    print("Original list after modifying b:", a)

    # Immutable (tuple)
    x = (1, 2, 3)
    y = x
    y = y + (4,)
    print("Original tuple:", x)
    print("New tuple after change:", y)

def shallow_vs_deep():
    print("\nShallow vs Deep Copy:")

    original = [[1, 2], [3, 4]]

    shallow_copy = copy.copy(original)
    deep_copy = copy.deepcopy(original)

    shallow_copy[0][0] = 99
    print("Original after shallow copy change:", original)
    print("Deep copy remains unchanged:", deep_copy)

if __name__ == "__main__":
    mutable_vs_immutable()
    shallow_vs_deep()
