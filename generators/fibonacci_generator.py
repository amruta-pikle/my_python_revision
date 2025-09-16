"""
fibonacci_generator.py

This file contains a generator function to yield Fibonacci numbers up to a given limit.
"""

def fibonacci(limit):
    """
    Generator that yields Fibonacci numbers up to `limit`.

    Example:
        >>> list(fibonacci(10))
        [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for num in fibonacci(20):
        print(num)
