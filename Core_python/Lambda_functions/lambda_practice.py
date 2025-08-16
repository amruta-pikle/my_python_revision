"""
lambda_practice.py
Practice problems for Python lambda functions.

Problems:
1. Write a lambda function to check if a number is even or odd.
2. Write a lambda function to find the square of a number.
3. Write a lambda function that takes two arguments and returns the maximum.
"""

# 1. Write a lambda function to check if a number is even or odd.
is_even = lambda x: "Even" if x % 2 == 0 else 'Odd'
print(f"10 is : {is_even(10)}")
print(f"23 is : {is_even(23)}")
print()

# 2. Write a lambda function to find the square of a number.
square_of_number = lambda x : x**2
print(f"Sqaure of 99 : {square_of_number(99)}")
print()

# 3. Write a lambda function that takes two arguments and returns the maximum.
maximum = lambda a,b : a if a>b else b
print(f"maximum between -9 and 10 : {maximum(-9,10)}")
print(f"maximum between -10 and -100 : {maximum(-10,-100)}")
