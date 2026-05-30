# Demonstrate the arithmetic, logical checks and the use of math constants

import math

class ShapeCalculator:
    #A class to perform calculations for basic 2D shapes.
    
    def __init__(self, name):
        self.name = name

    def calculate_circle_area(self, radius):
        # Logic: Ensure the input is a valid physical dimension
        if radius < 0:
            return "Error: Radius cannot be negative."
        
        # Math: Area = π * r^2
        area = math.pi * (radius ** 2)
        return round(area, 2)

    def is_equilateral(self, a, b, c):
        # Logic: Verify if a triangle is equilateral
        if a <= 0 or b <= 0 or c <= 0:
            return "Invalid dimensions"
        
        return a == b == c

calc = ShapeCalculator("GeoCalc")

circle_area = calc.calculate_circle_area(5)
print(f"Area of circle: {circle_area}")

is_equal = calc.is_equilateral(10, 10, 10)
print(f"Is triangle equilateral? {is_equal}")