"""
data_types_practice.py
Practice problems for Python data types: list, tuple, dict, and set.

Problems:
1. Create a list of 10 numbers and find the sum of even numbers.
2. Create a tuple of 5 strings and print only those with length > 3.
3. Create a dictionary with names as keys and ages as values, then find the oldest person.
4. Create a set of numbers from 1 to 20 and find all numbers that are divisible by both 2 and 5.
"""

# 1. Create a list of 10 numbers and find the sum of even numbers.

num_list = [77,6,26,99,45,1,46,75,8,55]
print(f"Number list is : {num_list}")

result = 0
for num in num_list:
    if num%2==0:
        result += num

print(f"Sum of even numbers : {result}")
print()


# 2. Create a tuple of 5 strings and print only those with length > 3.
strings_tuple = ("abc", "abababa", "a","defghim", "opyytrssn")
print(f"The tuple is : {strings_tuple}")

print(f"Words with length greater than 3 are:")
for word in strings_tuple:
    if len(word) > 3:
        print(word)

print()


# 3. Create a dictionary with names as keys and ages as values, then find the oldest person.
people_dict = {"rex" : 3, "maria" : 77, "sam" : 45, "xenith" : 22}
print(f"Person name and their age : {people_dict}")

oldest_person = max(people_dict, key=people_dict.get)

print(f"Oldest person is : {oldest_person} and the age is : {people_dict[oldest_person]}")
print()


# 4. Create a set of numbers from 1 to 20 and find all numbers that are divisible by both 2 and 5.
num_set=set()

for num in range(1,21):
    num_set.add(num)
print(f"number set is : {num_set}")

print(f"numbers that are deivisble by 2 and 5 are:")

for num in num_set:
    if num%2==0 and num%5==0:
        print(num)

