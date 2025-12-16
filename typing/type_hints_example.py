# Add type hints to a function that takes a list of integers and returns their sum.
from typing import List, Optional, Dict, Tuple, Set


# def calculate_sum(nums: List[int]) -> int:
#     return sum(nums)
#
#
# print(calculate_sum([3, 4, 5, 6, 7]))


# Use Optional in a function parameter.

# def print_example(s: Optional[str]):
#     print(s)
#
# print_example("amruta")
# print_example(None)


# Write a function using List, Dict, Set and Tuple from typing.

def typing_example():
    dict_example: Dict[int, str] = {1: "amruta", 2: "pikle"}
    list_example: List[int] = [2,3,4,56]
    tuple_example: Tuple[str, ...]= ("amruta", "pikle")
    set_example: Set[int] = {1,2,3,4,5}

    print(f"Dict example: {dict_example} \n"
          f"List example : {list_example} \n"
          f"Tuple example : {tuple_example} \n"
          f"Set example : {set_example}")


typing_example()