"""
    Create a decorator that counts how many times a function is called.
"""
from functools import wraps

def count(fun):
    count_fun = 0

    @wraps(fun)
    def wrapper(*args, **kwargs):
        nonlocal count_fun
        count_fun += 1
        return fun(*args, **kwargs)

    wrapper.call_count  = lambda : count_fun
    return wrapper

@count
def hello_fun():
    return "hello"

for _ in range(4):
    print(hello_fun())

print(f"hello_fun() is called {hello_fun.call_count()} times")
