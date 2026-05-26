# TODO: Import the Shape class from shape.py
# TODO: If you using math don't forget to import math
# Use format: from shape import Shape
from shape import Shape
import math

class Triangle(Shape):
    # TODO: Implement the Triangle class that inherits from Shape
    
    def __init__(self, a, b, c):
        # TODO: Initialize the Triangle with three sides a, b, and c
        # TODO: Store a, b, and c as instance attributes
        self.a=a
        self.b=b
        self.c=c
    
    def area(self):
        # TODO: Override the area method to calculate the triangle's area
        # TODO: Use Heron's formula: sqrt(s * (s-a) * (s-b) * (s-c)), Don't forget to add import math
        # TODO: where s = (a + b + c) / 2 (semi-perimeter)
        s= (self.a + self.b + self.c) / 2 
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
    
    def perimeter(self):
        # TODO: Override the perimeter method to calculate the triangle's perimeter
        # TODO: Use the formula: a + b + c (sum of all sides)
        return self.a+self.b+self.c