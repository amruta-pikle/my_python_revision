"""
Problem: Working with Python Data Types

Task:
1. Create a list of integers and find the second largest number.
2. Convert the list to a tuple and retrieve the last 3 elements.
3. Store the elements in a dictionary where the key is the index and the value is the element.
4. Convert the dictionary values into a set and display the unique elements.
"""

nums = [1, 99, -1, 3, 100, 66]

def find_second_largest(numbers):
    print(f"Number list is : {numbers}")
    numbers.sort()
    print(f"Second largest number is : {numbers[-2]}")
    print()


def last_three_elements_as_tuple(numbers):
    print(f"Number list is : {numbers}")
    num_tup = tuple(numbers)
    print(f"List after converting to tuple : {num_tup}")
    last_three_elements = num_tup[-3::]
    print(f"Last three elements of a tuple : {last_three_elements}")
    print()


def create_index_dict(numbers):
    print(f"Number list is : {numbers}")
    num_dict = {}

    for index,num in enumerate(numbers):
        num_dict[index] = num

    print(f"Dictionary where the key is the index and the value is the element : {num_dict}")
    print()


def convert_dict_values_to_set():
    num_dict = {0: 100, 1: 99, 2: -1, 3: 3, 4: 100, 5: -1}
    print(f"Num dict is : {num_dict}")
    unique_values = set(num_dict.values())
    print(f"Unique values coverted to set are : {unique_values}")


find_second_largest(nums)
last_three_elements_as_tuple(nums)
create_index_dict(nums)
convert_dict_values_to_set()