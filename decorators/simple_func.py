"""
    Write a decorator that prints "Function started" and "Function ended" around a function call
"""
from functools import wraps


def dec_fun(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print("function started")
        fun(*args, **kwargs)
        print("function ended")
    return wrapper

@dec_fun
def hello():
    """this prints hello"""
    print("hello")

hello()
