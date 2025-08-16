"""
Practice problems for Python Lambda Functions.

Tasks:
1. Write a lambda function to check if a string is a palindrome.
2. Use a lambda function to sort a list of tuples based on the second element.
3. Combine two lambda functions: one that doubles a number and another that adds 5 to it, to process a list of numbers.
"""

# 1.lambda function to check if a string is a palindrome.
print("1. Write a lambda function to check if a string is a palindrome.")

check_palindrome = lambda s: "True" if s == s[::-1] else "False"
print(f"Is 'ata' a palindrome? : {check_palindrome("ata")}")
print(f"Is 'sam' a palindrome? : {check_palindrome("sam")}")
print(f"Is 'ababa' a palindrome? : {check_palindrome("ababa")}")
print()

# 2. Use a lambda function to sort a list of tuples based on the second element.
print("2. Use a lambda function to sort a list of tuples based on the second element.")

tuples_list = [(1, 5), (2, 2), (3, 8), (4, 1)]
print(f"tuple list : {tuples_list}")

sorted_tuple = sorted(tuples_list,key = lambda x : x[1])

print(f"sorted tuple : {sorted_tuple}")
print()

# 3. Combine two lambda functions: one that doubles a number and another that adds 5 to it, to process a list of numbers.
print("3. Combine two lambda functions: one that doubles a number and another that adds 5 to it, to process a list of numbers.")

numbers = [1, 2, 3, 4, 5]
print(f"number list : {numbers}")

# doubling a number

double_num = lambda x : x*2

# adding five

add_five = lambda x : x+5

new_list = list(map(lambda x : add_five(double_num(x)), numbers))

print(f'new list : {new_list}')

print()