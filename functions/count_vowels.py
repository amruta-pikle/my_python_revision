"""
     write a function count_vowels(sentence) returning a dictionary.
"""

def count_vowels(s: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    print(f"Count of vowels in {s} is : {count}")


if __name__ == "__main__":

    while True:
        s = input("enter the word or sentence")
        if s == "exit" or not s:
            break
        else:
            print(f"the input is : {s}")
            count_vowels(s)

    print("Done!")

