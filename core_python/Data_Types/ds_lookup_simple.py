"""
Problem:
Create a list, set, dict, and tuple with numbers from 1 to 100.
Check if the number 50 exists in each structure and print the result.
"""

def check_lookup():
    numbers = list(range(1, 101))
    numbers_set = set(numbers)
    numbers_dict = {i: None for i in numbers}
    numbers_tuple = tuple(numbers)

    target = 50

    print("Is 50 in list?", target in numbers)
    print("Is 50 in set?", target in numbers_set)
    print("Is 50 in dict?", target in numbers_dict)
    print("Is 50 in tuple?", target in numbers_tuple)

if __name__ == "__main__":
    check_lookup()
