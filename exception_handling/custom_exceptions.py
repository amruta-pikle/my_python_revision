"""
Problem:
Create a custom exception `NegativeNumberError`.
Write a function that checks if a number is positive.
If the number is negative, raise the exception.
Otherwise, print "Number is valid".
"""

class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Number cannot be negative")
    else:
        return num

if __name__ == "__main__":
    try:
        check_number(0.000)
        check_number(-0.0000133)
    except NegativeNumberError as e:
        print("Error",e)

