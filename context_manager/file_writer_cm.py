"""
file_writer_cm.py

Beginner example of a custom context manager using the `with` keyword.
Opens a file for writing and ensures it is closed automatically.
"""


class FileWriter:
    """
    Context manager to open a file for writing and close it safely.

    Example:
        >>> with FileWriter("example.txt") as f:
        ...     f.write("Hello, World!")
    """

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False  # Propagate exceptions if any


if __name__ == "__main__":
    with FileWriter("test.txt") as f:
        f.write("Hello from context manager!")
