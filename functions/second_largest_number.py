"""
    Write a function second_largest(nums) without sorting.
"""


def find_second_largest_num(nums: list):
    if len(nums) < 2:
        print("There is no second largest")
        return

    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and num > second:
            second = num

    print(f"Second largest number is : {second}")


if __name__ == "__main__":
    while True:
        input_nums = input("Provide the numbers")
        if input_nums == "exit" or not input_nums:
            break

        print(f"input provided is : {input_nums}")
        array_nums = list(map(int, input_nums.split()))
        find_second_largest_num(array_nums)

    print("Done!!")
