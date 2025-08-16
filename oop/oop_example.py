"""
oop_example.py
A simple demonstration of Object-Oriented Programming in Python.
Includes classes, objects, inheritance, __init__, and __str__ methods.
"""


# Base Class
class Company:
    """Represents a company with a name and city."""

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"Company name : {self.name}\nCompany City : {self.city}"


# Derived Class
class Employee(Company):
    """Represents an employee who works in a company."""

    def __init__(self, emp_id, emp_name, company_name, company_city):
        super().__init__(company_name, company_city)  # using super() to pass the company variables
        self.emp_id = emp_id
        self.emp_name = emp_name

    def __str__(self):
        return (
            f"Employee id : {self.emp_id}\n"
            f"Employee name : {self.emp_name}\n"
            f"{super().__str__()}"
        )


if __name__ == "__main__":
    # Object creation of Company and Employee Classes
    company = Company("ost", "Bengalore")
    employee = Employee(123, "Amruta", "Ost", "Bangalore")

    # Print the Company and Employee details
    print("Company details:")
    print(company)
    print()
    print("Employee details:")
    print(employee)
