"""
Problem:
---------
Given a list of integers:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Tasks:
1. Create a list comprehension for squares of even numbers.
2. Create a set comprehension for cubes of numbers divisible by 3.
3. Create a dict comprehension where the key is the number and the value is "even" or "odd".

Author: Amruta Pikle
"""

# List of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Task 1 : Create a list comprehension for squares of even numbers.
square_of_even_numbers = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Square of even numbers : {square_of_even_numbers}")

# Task 2 : Create a set comprehension for cubes of numbers divisible by 3.
cubes_divisible_by_three = {x ** 3 for x in numbers if x % 3 == 0}
print(f"Cube of numbers divisible by 3 : {sorted(cubes_divisible_by_three)}")

# Task 3 : create a dict comprehension where the key is the number and the value is "even" or "odd"
even_odd_dict = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(f"number dictionary : {even_odd_dict}")
