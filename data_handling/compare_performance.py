# compare the performance of two different ways to create a list using a for loop versus a list comprehension

import timeit

# Define the code snippets to test
code_loop = """
result = []
for i in range(1000):
    result.append(i * 2)
"""

code_list_comp = """
result = [i * 2 for i in range(1000)]
"""

# number=10000 tells timeit to run the code 10,000 times to get an accurate average
time_loop = timeit.timeit(stmt=code_loop, number=10000)
time_comp = timeit.timeit(stmt=code_list_comp, number=10000)

print(f"Loop execution time: {time_loop:.4f} seconds")
print(f"List comprehension execution time: {time_comp:.4f} seconds")

# Calculating the difference
if time_comp < time_loop:
    print(f"List comprehension is {time_loop / time_comp:.2f}x faster!")