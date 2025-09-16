"""
Problem: map()

Task:
Given a list of temperatures in Celsius, use map() to:
1. Convert each temperature into Fahrenheit.
   Formula: F = (C * 9/5) + 32
2. Return the new list of Fahrenheit values.
"""

celsius_temps = [0, 20, 37, 100, -10]
print(f"Temp in celsius : {celsius_temps}")

fah_tem= list(map(lambda x : (x*(9/5))+32, celsius_temps))
print(f"new list of Fahrenheit values. : {fah_tem}")
