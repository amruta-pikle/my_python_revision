"""
Practice problems for Python map(), filter(), and reduce() functions.

Tasks:
1. Use map() to triple all numbers in a list.
2. Use filter() to get all strings from a list that have length greater than 5.
3. Use reduce() to find the maximum number in a list of integers.
"""
from functools import reduce

# 1. Use map() to triple all numbers in a list.
print("1. Use map() to triple all numbers in a list.")

nums = [1,2,3,-9,0]
print(f"numbers are : {nums}")

tripled_nums = list(map(lambda x : x**3, nums))

print(f"Tripled numbers are : {tripled_nums}")
print()

# 2. Use filter() to get all strings from a list that have length greater than 5.
print("2. Use filter() to get all strings from a list that have length greater than 5.")

string_list = ["word","w", "djdjffddkjg","fddddfdfff"]

new_list = list(filter(lambda x: len(x)>5,string_list))

print(f"strings with length more than 5 are : {new_list}")
print()

# 3. Use reduce() to find the maximum number in a list of integers.
print("3. Use reduce() to find the maximum number in a list of integers.")

num = [-1,-10,-100,-75]
print(f"integers are : {num}")

max_num = reduce(lambda x,y : max(x,y), num)

print(f"maximum is : {max_num}")