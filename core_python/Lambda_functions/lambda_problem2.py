"""
Problem: Using Lambda Functions

Task:
1. Write a lambda function to check if a number is even.
2. Write a lambda function to return the maximum of two numbers.
3. Write a lambda function to reverse a string.
"""

# Lambda function to check if num is even or not

is_even = lambda x : "Even" if x%2==0 else "Odd"


# Lambda function to return max of two numbers

max_of_two = lambda x,y : x if x>y else y

reverse_string = lambda x : x[::-1]

print(f"is -10 even? : {is_even(-10)}\n")
print(f"Is -100 greater or -101 ? : {max_of_two(-100,-101)}\n")
print(f"Reverse of 'This is an example' is : {reverse_string('This is an example')}")