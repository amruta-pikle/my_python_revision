"""
exception_handling_example.py
Demonstrates Python exception handling using try, except, else, and finally.
Covers ZeroDivisionError and ValueError scenarios.
"""

if __name__ == "__main__":
    # This example demonstrates handling division and input errors
    try:
        # Get numerator and denominator from user
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))

        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Please enter a valid integer!")

    else:
        print(f"Result is: {result}")

    finally:
        print("Execution completed, whether there was an error or not.")
