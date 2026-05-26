class Rectangle:
    def __init__(self, width, height):
        # TODO: Initialize private attributes _width and _height with default values
        # NOTE: Set initial values to 0 before using the property setters
        self._width = 0
        self._height = 0
        
        # TODO: Use property setters to set width and height (for validation)
        # This ensures validation happens during initialization
        self.width = width
        self.height = height
    
    # TODO: Implement width property getter
    @property
    def width(self):
        # TODO: Return the private _width attribute
        return self._width
    
    # TODO: Implement width property setter
    @width.setter
    def width(self, value):
        # TODO: Validate that value is positive
        # Check: if value <= 0, raise ValueError with message "Width must be positive"
        # Otherwise, set self._width = value
        if value <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = value
    
    # TODO: Implement height property getter
    @property
    def height(self):
        # TODO: Return the private _height attribute
        return self._height
    
    # TODO: Implement height property setter
    @height.setter
    def height(self, value):
        # TODO: Validate that value is positive (greater than 0)
        # TODO: If value is not positive, raise ValueError with message "Height must be positive"
        # TODO: If value is valid, set the _height attribute
        if value <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = value
    
    # TODO: Implement read-only area property
    @property
    def area(self):
        # TODO: Calculate and return the area (width * height)
        return self.width * self.height
    
    # TODO: Implement read-only perimeter property
    @property
    def perimeter(self):
        # TODO: Calculate and return the perimeter (2 * (width + height))
        return (2 * (self.width + self.height))
    
    # TODO: Implement dimensions property getter
    @property
    def dimensions(self):
        # TODO: Return width and height as a tuple (width, height)
        return (self.width, self.height)
    
    # TODO: Implement dimensions property setter
    @dimensions.setter
    def dimensions(self, dimensions):
        # TODO: Unpack the tuple using: width, height = dimensions
        # TODO: Then use the width and height setters: self.width = width, self.height = height
        # This ensures validation happens
        width, height = dimensions
        self.width = width
        self.height = height

    
    # TODO: Implement dimensions property deleter
    @dimensions.deleter
    def dimensions(self):
        # TODO: Reset both width and height to 1
        # TODO: Use the property setters to ensure validation
        self.width = 1
        self.height = 1