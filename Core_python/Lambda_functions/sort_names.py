"""
Problem:
Given a list of names, sort them by length of name using a lambda function.

Example:


names = ['Amy', 'John', 'Elizabeth', 'Tom']

# Output:
['Amy', 'Tom', 'John', 'Elizabeth']

"""
names = ['Tom', 'John', 'Elizabeth', 'Amy']

sorted_names=sorted(names, key= lambda name: len(name))

print(f"sorted_names: {sorted_names}")
