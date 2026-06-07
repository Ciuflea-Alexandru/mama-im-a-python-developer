# calculate the distance between two points 

import math

def calculate_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points: (x1, y1) and (x2, y2).
    Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    x1, y1 = point1
    x2, y2 = point2
    
    # math.pow(x, y) returns x raised to the power of y
    # math.sqrt(x) returns the square root of x
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distance

# Define two coordinates
coord_a = (0, 0)
coord_b = (3, 4)

# Calculate result
dist = calculate_distance(coord_a, coord_b)

print(f"The distance between {coord_a} and {coord_b} is: {dist}")