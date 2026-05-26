# TODO: Import the Shape class from shape.py
# Use format: from shape import Shape
from shape import Shape

class Circle(Shape):
    # TODO: Implement the Circle class that inherits from Shape
    
    def __init__(self, radius):
        # TODO: Initialize the Circle with a radius parameter
        # TODO: Store the radius as an instance attribute
        self.radius = radius
    
    def area(self):
        # TODO: Override the area method to calculate the circle's area
        # TODO: Use the formula: π * radius^2
        # TODO: Use 3.14159 for π
        return 3.14159 * self.radius**2
    
    def perimeter(self):
        # TODO: Override the perimeter method to calculate the circle's perimeter
        # TODO: Use the formula: 2 * π * radius
        # TODO: Use 3.14159 for π
        return 2*3.14159*self.radius