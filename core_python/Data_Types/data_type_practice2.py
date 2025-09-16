"""

Tasks:
1. Given a list of integers, remove duplicates without changing the order and return a new list.
2. You have a dictionary where keys are student names and values are lists of scores.
   Write a function to return a new dictionary with each student's average score.
3. Merge two sets and return a sorted list of elements that are present in either set but not in both.
4. Given a tuple of integers, return a new tuple where each element is squared if it is even, else unchanged.

"""

# 1. Given a list of integers, remove duplicates without changing the order and return a new list.
print("1. Given a list of integers, remove duplicates without changing the order and return a new list.")
num = [1, 99, 3, 4, 1, 7, 99, 100]
seen = []

for n in num:
    if n not in seen:
        seen.append(n)

print(f"New list: {seen}")
print()
# Better approaches

# Using dict.fromkeys()
new_list = list(dict.fromkeys(num))

# Using set + list comprehension trick
seen = set()
new_list = [x for x in num if not (x in seen or seen.add(x))]

# 2. You have a dictionary where keys are student names and values are lists of scores.
#    Write a function to return a new dictionary with each student's average score.
print("# 2. You have a dictionary where keys are student names and values are lists of scores..Write a function to return a new dictionary with each student's average score.")
students_scores = {
    "Alice": [85, 92, 78],
    "Bob": [70, 88, 90, 75],
    "Charlie": [95, 100],
    "Diana": [60, 65, 70, 75]
}

def students_avg_score(students_scores):
    return {key: sum(values) / len(values) for key, values in students_scores.items()}


print(f"Students with their average numbers : {students_avg_score(students_scores)}")
print()

# 3. Merge two sets and return a sorted list of elements that are present in either set but not in both.
print("# 3. Merge two sets and return a sorted list of elements that are present in either set but not in both.")
set1 = {1,4,99,76}
set2  = {99,1,99,34}
print(f"set1 : {set1}")
print(f"set2 : {set2}")
print()
#new_set = set1 ^ set2
new_set = set1.symmetric_difference(set2)
print(f"Union of set1 and set2 : {new_set}")
print()

# 4. Given a tuple of integers, return a new tuple where each element is squared if it is even, else unchanged.
print("# 4. Given a tuple of integers, return a new tuple where each element is squared if it is even, else unchanged.")
num_tuple = (1,3,4,88,55,78)
print(f"original tuple : {num_tuple}")

new_tuple = tuple(x**2 if x%2==0 else x for x in num_tuple)

print(f"New tuple : {new_tuple}")


