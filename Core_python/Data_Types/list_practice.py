"""
Practice Problem: Lists

   - Write a function to:
   - Find the sum of all even numbers.
   - Find the maximum and minimum values.
   - Reverse the list without using the built-in reverse() function.
"""

def list_prac(list1 : list):
    print(f"The list is : {list1}")
    print()

    sum_of_even_numbers = sum([num for num in list1 if num%2==0])
    print(f"Sum of even numbers : {sum_of_even_numbers}")
    print()

    max_num = max([num for num in list1])
    min_num = min([num for num in list1])
    print(f"Max number is : {max_num}\n"
          F"Min number is : {min_num}")
    print()
    list1.reverse()
    print(f"reversed list is : {list1}")


list_prac([1,2,3,4,5,6,7,8])
