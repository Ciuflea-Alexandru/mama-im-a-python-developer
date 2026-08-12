def max_subarray(nums):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.
    """
    if not nums:
        return 0
        
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        # Decide whether to add the current number to the existing subarray 
        # or start a new subarray from the current number
        max_current = max(nums[i], max_current + nums[i])
        
        # Update the global maximum if the current subarray sum is larger
        if max_current > max_global:
            max_global = max_current
            
    return max_global

if __name__ == "__main__":
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(numbers)
    print(f"Array: {numbers}")
    print(f"Maximum contiguous subarray sum: {result}")