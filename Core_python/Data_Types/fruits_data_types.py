"""
Problem:
---------
Given a list of fruits with duplicates:
1. Remove duplicates.
2. Store the result in a tuple sorted alphabetically.
3. Create a dictionary where the key is the fruit name and the value is the length of the name.

Author: Amruta Pikle
"""

# Original fruit list
fruit_list = ["apple", "banana", "apple", "cherry", "banana", "date"]
print(f"Original fruit list: {fruit_list}")

# Step 1 & 2: Remove duplicates, sort alphabetically, store in a tuple
sorted_unique_fruits = tuple(sorted(set(fruit_list)))
print(f"Sorted unique fruits tuple: {sorted_unique_fruits}")

# Step 3: Create dictionary mapping fruit -> length of name
fruit_dict = {fruit: len(fruit) for fruit in sorted_unique_fruits}
print(f"Fruit dictionary: {fruit_dict}")
