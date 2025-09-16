"""
Given a list of numbers, create:

A list of squares using list comprehension

A set of squares (to remove duplicates)

A dictionary where key is number and value is its square

Example:

nums = [1, 2, 2, 3]

# Output:
List: [1, 4, 4, 9]
Set: {1, 4, 9}
Dict: {1: 1, 2: 4, 3: 9}

"""

nums = [1, 2, 2, 3]

list_of_sqaures = [x ** 2 for x in nums]

print(f"List: {list_of_sqaures}")

unique_list_of_sqaures = {x ** 2 for x in nums}

print(f"Set: {unique_list_of_sqaures} ")

dict_of_nums = {x: x * 2 for x in nums}

print(f"Dict: {dict_of_nums}")
