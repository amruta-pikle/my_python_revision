"""
custom_range_iterator.py

This file contains an example of a custom iterator that mimics Python's built-in range().
"""


class CustomRange:
    """
    An iterator that generates numbers from start to end with a given step.

    Example:
        >>> for i in CustomRange(1, 5, 1):
        ...     print(i)
        1
        2
        3
        4
    """

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += self.step
        return current


if __name__ == "__main__":
    for num in CustomRange(1, 5):
        print(num)
