from rectangle import Rectangle

# Test case handler
test_case = input()

# Basic functionality test
if test_case == "default_test":
    rect = Rectangle(5, 3)
    print(f"Width: {rect.width}, Height: {rect.height}")
    print(f"Area: {rect.area}, Perimeter: {rect.perimeter}")
    
    # Test the dimensions property
    print(f"Dimensions: {rect.dimensions}")
    rect.dimensions = (10, 8)
    print(f"New area: {rect.area}")
    
    # Test validation
    try:
        rect.width = -2
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Test deleter
    del rect.dimensions
    print(f"After reset: {rect.dimensions}")

# Test with zero values
elif test_case == "zero_values":
    try:
        rect = Rectangle(0, 5)
    except ValueError as e:
        print(f"Error creating rectangle: {e}")
    
    try:
        rect = Rectangle(5, 0)
    except ValueError as e:
        print(f"Error creating rectangle: {e}")

# Test with negative values
elif test_case == "negative_values":
    rect = Rectangle(5, 3)
    original_dimensions = rect.dimensions
    
    try:
        rect.dimensions = (5, -3)
    except ValueError as e:
        print(f"Error setting dimensions: {e}")
    
    print(f"Dimensions after failed update: {rect.dimensions}")
    print(f"Original dimensions preserved: {rect.dimensions == original_dimensions}")

# Test with large values
elif test_case == "large_values":
    rect = Rectangle(1000000, 2000000)
    print(f"Large rectangle area: {rect.area}")
    print(f"Large rectangle perimeter: {rect.perimeter}")

# Test with floating point values
elif test_case == "float_values":
    rect = Rectangle(3.5, 2.75)
    print(f"Dimensions: {rect.dimensions}")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")
    
    rect.dimensions = (1.1, 2.2)
    print(f"New area with float dimensions: {rect.area}")

# Test with type errors
elif test_case == "type_errors":
    try:
        rect = Rectangle("5", 3)
    except Exception as e:
        print(f"Type error during creation: {type(e).__name__}: {e}")
    
    rect = Rectangle(5, 3)
    try:
        rect.dimensions = 10  # Not a tuple
    except Exception as e:
        print(f"Type error setting dimensions: {type(e).__name__}: {e}")

# Test multiple property operations
elif test_case == "property_operations":
    rect = Rectangle(5, 10)
    print(f"Initial - Width: {rect.width}, Height: {rect.height}, Area: {rect.area}")
    
    rect.width = 8
    print(f"After width change - Width: {rect.width}, Area: {rect.area}")
    
    rect.height = 6
    print(f"After height change - Height: {rect.height}, Area: {rect.area}")
    
    rect.dimensions = (12, 9)
    print(f"After dimensions change - Dimensions: {rect.dimensions}, Area: {rect.area}")
    
    del rect.dimensions
    print(f"After reset - Dimensions: {rect.dimensions}, Area: {rect.area}")

# Test property validation edge cases
elif test_case == "validation_edge_cases":
    rect = Rectangle(5, 3)
    
    try:
        rect.width = 0
    except ValueError as e:
        print(f"Zero width error: {e}")
    
    # Very small positive value should be accepted
    rect.height = 0.0001
    print(f"Small height accepted: {rect.height}")
    print(f"Area with small height: {rect.area}")

# Test multiple rectangles
elif test_case == "multiple_rectangles":
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(10, 2)
    rect3 = Rectangle(4, 4)
    
    print(f"Rectangle 1 - Area: {rect1.area}, Perimeter: {rect1.perimeter}")
    print(f"Rectangle 2 - Area: {rect2.area}, Perimeter: {rect2.perimeter}")
    print(f"Rectangle 3 - Area: {rect3.area}, Perimeter: {rect3.perimeter}")
    
    # Modify each rectangle
    rect1.width = 7
    rect2.height = 5
    rect3.dimensions = (6, 6)
    
    print(f"After modifications:")
    print(f"Rectangle 1 - Dimensions: {rect1.dimensions}")
    print(f"Rectangle 2 - Dimensions: {rect2.dimensions}")
    print(f"Rectangle 3 - Dimensions: {rect3.dimensions}")

# Test performance with many operations
elif test_case == "performance_test":
    rect = Rectangle(5, 5)
    
    # Perform many property operations
    for i in range(1000):
        rect.width = i % 10 + 1  # Values 1-10
        rect.height = i % 5 + 1  # Values 1-5
        area = rect.area  # Access computed property
        perimeter = rect.perimeter  # Access computed property
        dims = rect.dimensions  # Access property getter
    
    print(f"Final state after 1000 operations:")
    print(f"Width: {rect.width}, Height: {rect.height}")
    print(f"Area: {rect.area}, Perimeter: {rect.perimeter}")