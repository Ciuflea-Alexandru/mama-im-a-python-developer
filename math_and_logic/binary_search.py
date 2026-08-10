def binary_search(arr, target):
    """
    Searches for a target value in a sorted array using binary search.
    Returns the index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23
    
    result = binary_search(sorted_numbers, target_val)
    print(f"Array: {sorted_numbers}")
    print(f"Target {target_val} found at index: {result}")