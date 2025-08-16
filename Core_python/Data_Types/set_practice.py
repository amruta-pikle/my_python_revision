"""
Practice Problem: Sets


    Write a function to:
   - Find the union, intersection,symmetric difference and difference of the sets.
   - Check if one set is a subset of the other.
   - Remove duplicates from a list using set.
"""

def set_operations():
    set1 = {1,100,44,50,35}
    set2 = { 35,1,67,88,1000}

    print(f"Set1 is {set1}\n"
          f"Set2 is {set2}")

    set_union= set1 | set2
    set_intersection = set1 & set2
    set_difference = set1 - set2
    symmetric_difference = set1 ^ set2

    print(f"Union of sets is : {set_union}\n"
          f"Intersection of sets is : {set_intersection}\n"
          f"Difference of set is : {set_difference}\n"
          f"Symmetric difference is : {symmetric_difference}")

#set_operations()

def check_subset():
    set1 = {1, 100, 44, 50, 35}
    set2 = {1, 35,44}

    print(f"Set1 is {set1}\n"
          f"Set2 is {set2}")

    print(f"Is set2 subset of set1 ? : {set2.issubset(set1)}")

#check_subset()

def remove_duplicate_using_list():
    set1 = {1, 100, 44, 50, 35,1,44,50}

    print(f"Set1 is {set1}")

    print(f"List after removing duplicates from set : {list(set1)}")

remove_duplicate_using_list()