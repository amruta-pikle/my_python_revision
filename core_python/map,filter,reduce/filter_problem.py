"""
Problem: filter()

Task:
Given a list of integers, use filter() to:
1. Get all numbers that are prime.
2. Return the list of prime numbers.
"""

numbers = [2, 3, 4, 5, 10, 11, 13, 15, 17, 20, 23]
print(f"numbers are : {numbers}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_num = list(filter(is_prime,numbers))
print(f"Prime numbera are : {prime_num}")