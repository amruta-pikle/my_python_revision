"""
Write a function that takes a list of fruits and returns:

A list of unique fruits

The number of total fruits

The number of unique fruits

Example:

python
Copy
Edit
fruits = ['apple', 'banana', 'apple', 'orange', 'banana']

# Output:
Unique fruits list: ['apple', 'banana', 'orange']
Total fruits: 5
Unique fruits: 3
"""

fruits = ['apple', 'banana', 'apple', 'orange', 'banana']


def count_unique_items(fruits):
    print(f"Unique_fruits: {set(fruits)}")
    print(f"total number of fruits: {len(fruits)}")
    print(f"number of unique fruits: {len(set(fruits))}")


count_unique_items(fruits)
