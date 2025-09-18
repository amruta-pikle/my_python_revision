"""
mutable_vs_immutable.py

Problem Statement:
------------------
Demonstrate the difference between mutable and immutable objects in Python.

Requirements:
1. Show how modifying a mutable object (list) inside a function
   affects the original object.
2. Show how modifying an immutable object (string or tuple) inside a function
   does not affect the original object.
"""


def modify_list(my_list: list):
    """Append an element to a list (mutable)."""
    my_list.append(100)
    print("Inside function (list modified):", my_list)


def modify_string(my_str):
    """Try to modify a string (immutable)."""
    my_str = my_str + "world"
    print("Inside function (string modified):", my_str)



if __name__ == "__main__":
    # Demo usage

    #Mutable example (list)

    nums = [1,2,3,4]
    print("Bfore function call (list):", nums)
    modify_list(nums)
    print("After function call (list):", nums)

    print("\n---\n")

    # Immutable example (string)

    text = "hello"
    print("Before function call (string):", text)
    modify_string(text)
    print("After function call (string):", text)