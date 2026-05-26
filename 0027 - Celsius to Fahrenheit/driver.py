# TODO: Import the Temperature class from the temperature module
from temperature import Temperature
# Test the class:
# TODO: Create a temperature instance at 25°C
temp = Temperature(40)  # Replace with actual Temperature instance

# TODO: Print both Celsius and Fahrenheit values
# TODO: Use the format: "25.0°C is 77.0°F"
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")
# TODO: Set the temperature to 98.6°F
temp.fahrenheit=500
# TODO: Print both values again to confirm the conversion works
# TODO: Use the same format as before
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")
