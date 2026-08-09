def two_sum(nums, target):
    """
    Finds the indices of two numbers in the list that add up to the target.
    Returns a list containing the two indices.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example Usage
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target_val = 9
    
    result = two_sum(numbers, target_val)
    print(f"Numbers: {numbers}")
    print(f"Target: {target_val}")
    print(f"Indices: {result}")