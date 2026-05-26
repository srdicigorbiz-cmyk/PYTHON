class Temperature:
    def __init__(self, celsius):
        # Store the temperature, but use the setter for validation
        self.celsius = celsius
    
    # TODO: Create a property decorator for celsius that returns self._celsius
    @property
    def celsius(self):
        return self._celsius
    
    # TODO: Create a celsius.setter that validates the temperature is above absolute zero (-273.15°C)
    # TODO: If value < -273.15, raise ValueError with message "Temperature cannot be below absolute zero (-273.15°C)"
    # TODO: Otherwise, set self._celsius to the value
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        else:
            self._celsius = value

    # TODO: Create a property decorator for fahrenheit that converts Celsius to Fahrenheit
    # TODO: Use the formula: F = C × 9/5 + 32
    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    # TODO: Create a fahrenheit.setter that converts Fahrenheit to Celsius
    # TODO: Use the formula: C = (F - 32) × 5/9
    # TODO: Set self.celsius to this converted value (this will use your celsius setter for validation)
    @fahrenheit.setter
    def fahrenheit(self,value):
        celsius_ertek = (value - 32) * 5/9
        self.celsius = celsius_ertek