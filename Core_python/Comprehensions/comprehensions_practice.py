"""
Practice problems for Python Comprehensions.

Tasks:
1. Create a list of squares of all odd numbers between 1 and 50 using a list comprehension.
2. From a given list of words, generate a set of words that start and end with the same letter.
3. Convert a dictionary of items with their prices to a dictionary with items having prices increased by 10% using a dict comprehension.
"""

# 1. Create a list of squares of all odd numbers between 1 and 50 using a list comprehension
print("1. Create a list of squares of all odd numbers between 1 and 50 using a list comprehension.")
odd_nums = [x**2 for x in range(1,51,2)]
print(f"odd numbers : {odd_nums}")
print()

# 2. From a given list of words, generate a set of words that start and end with the same letter.
print("2. From a given list of words, generate a set of words that start and end with the same letter.")
words =["amruta","zack","Est","William","kk"]
print(f"Words are : {words}")
new_words = [x for x in words if x[0]==x[-1]]

print(f"New list : {new_words}")
print()

#3. Convert a dictionary of items with their prices to a dictionary with items having prices increased by 10% using a dict comprehension.
print("3. Convert a dictionary of items with their prices to a dictionary with items having prices increased by 10% using a dict comprehension.")

item_dict ={
    "pen" : 10,
    "paper" : 120,
    "botle" : 540
}

print(f"items and their prices : {item_dict}")

updated_price = {key: value + ((10/100)*value) for key,value in item_dict.items()}

print(f"Items with their 10% updated price : {updated_price}")