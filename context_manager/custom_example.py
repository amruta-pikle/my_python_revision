"""
    Write a custom context manager that prints "enter" and "exit".
"""

# __exit__ SUPPRESSES the exception (return True)

# class MyContext:
#     def __enter__(self):
#         print("Entering context")
#         return "Resource ready"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting context")
#
#         if exc_type:
#             print(f"Exception type : {exc_type.__name__}")
#             print(f"Exception value: {exc_val}")
#         return True
#
# print("Before with block")
#
# with MyContext() as resource:
#     print(resource)
#     raise ValueError("Something went wrong")
#
# print("After eith block")




# __exit__ DOES NOT suppress the exception (return False)

# class MyContext:
#     def __enter__(self):
#         print("Entering context")
#         return "Resource ready"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting context")
#
#         if exc_type:
#             print(f"Exception type : {exc_type.__name__}")
#             print(f"Exception value : {exc_val}")
#         return False
#
#
# print("Before with block")
# print()
#
# with MyContext() as resource:
#     print(resource)
#     raise ValueError("Something went wrong")
#
# print()
# print("After with block")




# No exception at all

class MyContext:
    def __enter__(self):
        print("Entering context")
        return "Resource ready"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        print("exc_type: ", exc_type)
        return True

with MyContext() as resource:
    print(resource)

