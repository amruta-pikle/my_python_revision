"""
Problem:
Create a base class `Shape` with a method `area()`.
Inherit classes `Rectangle` and `Circle` from Shape.
Demonstrate polymorphism by storing different shape objects in a list
and printing their areas.
"""

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):
        print(f"Area of rectangle is : {self.height * self.width}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of circle is : {3.14 * self.radius ** 2}")



if __name__ == "__main__":
    # Create a list of shapes and print areas
    r = Rectangle(2,3)
    c = Circle(1.5)
    shapes = [r,c]

    for figure in shapes:
        figure.area()


