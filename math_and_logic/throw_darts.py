# Simulate throwing darts at a squareboard that contains a inscribed circle

import random

def estimate_pi(num_points):
    """
    Uses the Monte Carlo method to estimate pi.
    Logic: 
    - A circle with radius r=1 has an area of pi * r^2 = pi.
    - A square enclosing this circle has a side length of 2, area = 4.
    - The ratio of the area of the circle to the square is pi/4.
    """
    points_inside_circle = 0
    
    for _ in range(num_points):
        # Generate random x and y coordinates between -1 and 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Mathematical logic: Distance from origin is sqrt(x^2 + y^2)
        # If distance <= 1, the point is inside the circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
            
    # Pi/4 = points_inside / total_points
    return 4 * (points_inside_circle / num_points)

# Run the simulation
n = 100000
pi_estimate = estimate_pi(n)

print(f"Estimated value of pi using {n} points: {pi_estimate}")