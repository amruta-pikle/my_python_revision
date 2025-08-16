"""
Problem: Exception Handling

Task:
1. Write a program that opens a text file and reads its content.
2. Use try, except, else, and finally blocks to handle:
   - FileNotFoundError (if the file does not exist).
   - PermissionError (if the file cannot be opened due to access restrictions).
3. If no exception occurs, print the file content.
4. Ensure that in the finally block, you display the message: "Execution completed".
"""

def read_file(filename):
    try:
        # try opening and reading file
        with open(filename,"r") as f:
            content = f.read()
    except FileNotFoundError:
        # handle missing file
        print(f"File not found")
    except PermissionError:
        # handle no access issue
        print("permission issue")
    else:
        # runs only if no exception occurs
        print(F"file content is : {content}")
    finally:
        # always executes
        print("Execution completed")


if __name__ == "__main__":
    # test the function with different filenames
    read_file("sample_with_read_permission.txt")
    read_file("sample_without_read__permissin.txt")
