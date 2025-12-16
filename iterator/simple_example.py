"""
    Create a custom iterator class for a range-like object.
"""


class CustomRange:
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


for num in CustomRange(1,5):
        print(num)
