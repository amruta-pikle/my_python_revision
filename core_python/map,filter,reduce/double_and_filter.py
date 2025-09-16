"""

Given a list of numbers, do the following:

Use map() to double each number

Use filter() to keep only numbers greater than 5

Example:


nums = [1, 2, 3, 4]

# Doubled: [2, 4, 6, 8]
# Filtered: [6, 8]

"""

nums = [1, 2, 3, 4]

print(nums)

doubled = list(map(lambda x: x*2,nums))
print(doubled)

reduced = list(filter(lambda x : x>5,doubled))
print(reduced)