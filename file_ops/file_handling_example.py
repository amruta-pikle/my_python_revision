"""
file_handling_example.py
Demonstrates Python file handling with open, read, and write modes.
"""

import  os

project_root = os.path.dirname(os.path.abspath(__file__))
print(f"project root : {project_root}")

file_path = os.path.join(project_root,"sample.txt")
print(f"file path : {file_path}")

# Writing to a file
with open(file_path, "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This is a write operation")


# Reading from a file
with open(file_path, "r") as file:
    content = file.read()
    print("File Content:")
    print(content)