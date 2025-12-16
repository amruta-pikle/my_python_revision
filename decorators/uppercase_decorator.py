"""
Write a decorator that converts a function’s return value to uppercase.
Medium

"""

from functools import wraps


def make_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@make_uppercase
def upper_fun(s):
    return s


if __name__ == "__main__":
    while True:
        s = input("enter a word")
        if s == "exit" or not s:
            break

        print(f"upper case of {s} is : {upper_fun(s)}")


















