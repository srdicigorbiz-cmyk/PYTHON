# TODO: Import the Shape class from shape.py
# Use format: from shape import Shape
from shape import Shape

class Rectangle(Shape):
    # TODO: Implement the Rectangle class that inherits from Shape
    
    def __init__(self, length, width):
        # TODO: Initialize the Rectangle with length and width parameters
        # TODO: Store length and width as instance attributes
        self.length = length
        self.width = width
    
    def area(self):
        # TODO: Override the area method to calculate the rectangle's area
        # TODO: Use the formula: length * width
        return self.length * self.width
    
    def perimeter(self):
        # TODO: Override the perimeter method to calculate the rectangle's perimeter
        # TODO: Use the formula: 2 * (length + width)
        return 2*(self.length+self.width)