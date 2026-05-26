from shapefactory import ShapeFactory
from shape import Shape
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
import sys

# Test case executor
test_case = input()

factory = ShapeFactory()

if test_case == "circle_area":
    circle = factory.create_shape("circle", 5)
    print(f"{circle.area():.2f}")

elif test_case == "rectangle_perimeter":
    rectangle = factory.create_shape("rectangle", 4, 6)
    print(f"{rectangle.perimeter()}")

elif test_case == "triangle_perimeter":
    triangle = factory.create_shape("triangle", 3, 4, 5)
    print(f"{triangle.perimeter()}")

elif test_case == "invalid_shape":
    try:
        factory.create_shape("hexagon", 6)
        print("No exception raised")
    except ValueError as e:
        print(str(e))

elif test_case == "case_insensitive":
    circle = factory.create_shape("CiRcLe", 3)
    print(f"{circle.area():.2f}")

elif test_case == "shape_inheritance":
    shapes = [
        factory.create_shape("circle", 2),
        factory.create_shape("rectangle", 2, 3),
        factory.create_shape("triangle", 3, 4, 5)
    ]
    all_shapes = all(isinstance(shape, Shape) for shape in shapes)
    print(all_shapes)

elif test_case == "zero_radius_circle":
    circle = factory.create_shape("circle", 0)
    print(f"{circle.area():.2f} {circle.perimeter():.2f}")

elif test_case == "negative_dimensions":
    rectangle = factory.create_shape("rectangle", -2, -3)
    print(f"{rectangle.area()}")

elif test_case == "large_values":
    circle = factory.create_shape("circle", 1000000)
    print(f"{circle.area():.2e}")

elif test_case == "polymorphism_test":
    shapes = [
        factory.create_shape("circle", 2),
        factory.create_shape("rectangle", 3, 4),
        factory.create_shape("triangle", 3, 4, 5)
    ]
    area_sum = sum(shape.area() for shape in shapes)
    perimeter_sum = sum(shape.perimeter() for shape in shapes)
    print(f"Area sum: {area_sum:.2f}, Perimeter sum: {perimeter_sum:.2f}")

elif test_case == "triangle_area":
    triangle = factory.create_shape("triangle", 3, 4, 5)
    print(f"{triangle.area():.2f}")

elif test_case == "method_override":
    circle = factory.create_shape("circle", 2)
    rectangle = factory.create_shape("rectangle", 3, 4)
    triangle = factory.create_shape("triangle", 3, 4, 5)
    
    # Get method objects to compare implementations
    circle_area = Circle.area
    rectangle_area = Rectangle.area
    triangle_area = Triangle.area
    
    circle_perimeter = Circle.perimeter
    rectangle_perimeter = Rectangle.perimeter
    triangle_perimeter = Triangle.perimeter
    
    # Check if all implementations are unique
    unique_areas = len({circle_area, rectangle_area, triangle_area}) == 3
    unique_perimeters = len({circle_perimeter, rectangle_perimeter, triangle_perimeter}) == 3
    
    if unique_areas and unique_perimeters:
        print("All shapes correctly override methods")
    else:
        print("Some shapes share method implementations")