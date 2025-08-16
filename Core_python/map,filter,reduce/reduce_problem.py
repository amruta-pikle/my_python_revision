"""
Problem: reduce()

Task:
Given a list of integers, use reduce() to:
1. Find the product of all numbers in the list.
2. Find the maximum element in the list using reduce() (without using max()).
"""

from functools import reduce

numbers = [2, 3, 5, 7, 11]
print(F"numbers are : {numbers}")
print()
# 1. Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
print()

# 2. Maximum element (without using max())
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum element:", maximum)

