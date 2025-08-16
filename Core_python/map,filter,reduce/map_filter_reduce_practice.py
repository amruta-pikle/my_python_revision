"""
map_filter_reduce_practice.py
Practice problems for Python map(), filter(), and reduce() functions.

Problems:
1. Use map() to double all numbers in a list.
2. Use filter() to get all numbers divisible by 3 from a list.
3. Use reduce() to calculate the product of all numbers in a list.
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
print(f"Numbers are : {numbers}")
print()

# 1. Use map() to double all numbers in a list.

doubled = list(map(lambda x : x *2 , numbers))
print("Doubled numbers:", doubled)
print()

# 2. Use filter() to get all numbers divisible by 5 from a list.
num_divisible_by_five = list(filter(lambda x: x%5==0,numbers))
print(f"Numbers divisible by 5: {num_divisible_by_five}")
print()

# 3. Use reduce() to calculate the product of all numbers in a list.
product = reduce(lambda x,y : x*y, numbers)
print("Product of all numbers:", product) 


