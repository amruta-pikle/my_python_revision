"""
Problem:
Write a function that extracts all digits from a given string using regex.

Example:

text = "My phone number is 9876543210."

# Output:
['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

"""
import re

text = "My phone number is 9876543210."

print(f"Text is: {text}")

digits_found= re.findall(r'\d',text)
print(f"digits are: {digits_found}")