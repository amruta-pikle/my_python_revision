"""
comprehensions_practice.py
Practice problems for Python comprehensions: list, set, and dictionary.

Problems:
1. Create a list of squares of all odd numbers between 1 and 30 that are divisible by 3 using list comprehension.
2. Create a set of all unique characters (ignoring spaces and punctuation) from a given sentence using set comprehension.
3. Create a dictionary mapping each word in a given list to its reversed version, but only include words longer than 4 characters using dict comprehension.
"""


# 1. Create a list of squares of all odd numbers between 1 and 30 that are divisible by 3 using list comprehension.
num_list = [x**2 for x in range(1,31,2) if x%3==0]
print(f"List is : {num_list}")
print()

# 2.Create a set of all unique characters (ignoring spaces and punctuation) from a given sentence using set comprehension.
sentence = "Hello, world! Python is fun."
print(f"sentence is : {sentence}")

unique_char = {char.lower() for char in sentence if char.isalpha()}
print(f"Unique characters are : {unique_char}")
print()

# 3. Create a dictionary mapping each word in a given list to its reversed version, but only include words longer than 4 characters using dict comprehension.
sentence = "Hello, world! Python is fun."
print(f"sentence is : {sentence}")

reversed_word = {x:x[::-1] for x in sentence.split() if len(x) > 4 }
print(f"Reversed word dictionary is : {reversed_word}")