"""
Problem: Lambda Functions

Task:
Write a program that uses a lambda function to:
1. Square each number in a list.
2. Check if a given string is a palindrome (returns True/False).
"""

# 1. Square each number in a list.
list1 = [4,0,-1,5]
print(f"List is : {list1}")
print()
square_num = list(map(lambda x : x**2, list1))
print(f"list of sqaure numbers : {square_num}")
print()

s = "abababa"
check_palindrome = lambda x: True if s==s[::-1] else False

print(f"Is {s} a palindrome?: {check_palindrome(s)}")