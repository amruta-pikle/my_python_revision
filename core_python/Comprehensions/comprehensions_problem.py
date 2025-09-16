"""
Problem: Comprehensions in Python

Task:
1. Generate a list of squares of numbers from 1 to 10 using list comprehension.
2. Create a set of all even numbers from 1 to 20 using set comprehension.
3. Create a dictionary where the key is a number and the value is its cube using dict comprehension.
"""

def list_of_squares(n):
    print(f"Numbers are : {n}")
    sq_nums = [ x**2 for x in n]
    print(f"squared numbers are : {sq_nums}")
    print()


def set_of_evens(n):
    print(f"Numbers are : {n}")
    set_of_even = {x for x in n if x%2==0}
    print(f"Set of even numbers are : {set_of_even}")
    print()

def dict_of_cubes(n):
    print(f"List of numbers are : {n}")
    cube_of_nums = {x:x**3 for x in n}
    print(f"Dictionary is : {cube_of_nums}")

list_of_squares([1,2,3,4,5,6,7,8,9,10])
set_of_evens([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
dict_of_cubes([1,2,3,4,5,6,7,8,9,10])