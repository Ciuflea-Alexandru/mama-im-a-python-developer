# apply a transformation to an entire image-like grid of data without using a single nested loop

import numpy as np

# 1. Create a 3x3 grid (e.g., representing brightness levels in a tiny image)
grid = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 2. Broadcasting: Adding a 1D array to a 2D array
# NumPy automatically 'broadcasts' the row across the entire matrix.
# We are adding 5 to the first column, 10 to the second, and 15 to the third.
offsets = np.array([5, 10, 15])
transformed_grid = grid + offsets

print("Original Grid:")
print(grid)
print("\nTransformed (Broadcasted) Grid:")
print(transformed_grid)

# 3. Vectorized Logical Masking (Spatial Processing)
# Let's "clip" values: set any value > 60 to exactly 60.
# In pure Python, this would be multiple nested loops and 'if' statements.
transformed_grid[transformed_grid > 60] = 60

print("\nClipped Grid:")
print(transformed_grid)