"""
uppercase_decorator.py

This file contains a very simple beginner-level custom decorator
that converts the return value of a function into uppercase.
"""

from functools import wraps


def make_uppercase(func):
    """
    Decorator to convert string output of a function into uppercase.

    Example:
        >>> @make_uppercase
        ... def greet(name):
        ...     return f"Hello, {name}"
        >>> greet("Amruta")
        'HELLO, AMRUTA'
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@make_uppercase
def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet("Amruta"))
    print(greet.__name__)  # will show "wrapper" without wraps
    print(greet.__doc__)  # will lose original docstring

