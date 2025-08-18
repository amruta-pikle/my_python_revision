"""
Problem: map(), filter(), and reduce() in Python

Task:
1. Use map() to convert a list of strings to uppercase.
2. Use filter() to get only negative numbers from a list of integers.
3. Use reduce() to calculate the product of all numbers in a list.
"""

from functools import reduce

def convert_to_uppercase(words):
    print(f"Words are : {words}")
    uppercase_strings = "".join(list(map(lambda x : x.upper(),words)))
    print(f"Upper case words are : {uppercase_strings}\n")

def filter_negative(numbers):
    print(f"Numbers are : {numbers}")
    negative_numbers = list(filter(lambda  x:  x<0,numbers))
    print(f"Negative numbers are : {negative_numbers}\n")


def product_of_list(numbers):
    print(f"Numbers are : {numbers}")
    prod_of_nums = reduce(lambda x,y:x*y, numbers)
    print(f"product of numbers is : {prod_of_nums}")


convert_to_uppercase("this is an example")
filter_negative([45,-8,99,0,-11,987,-0.01])
product_of_list([45,-8,99,-11,987])