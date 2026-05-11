# Return the valid numbers in a list

def count_valid(numbers, lower, upper):
    r = 0
    for n in numbers:
        if abs(n) in range(lower, upper + 1):
            r = r + 1
    return r

numbers = [-2, 5, -20, 30, -56]
lower = 1
upper = 30
result = count_valid(numbers, lower, upper)

print(result)