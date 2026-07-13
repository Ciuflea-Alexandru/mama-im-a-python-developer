# split the list into halves, sort them recursively, and then merge the sorted halves back together

def merge_sort(arr):
    """Sorts a list using the Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr

    # Find the middle point and divide the array
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """Helper function to merge two sorted lists."""
    sorted_list = []
    i = j = 0

    # Compare elements and build the sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements (if any)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original list: {data}")
    print(f"Sorted list:   {merge_sort(data)}")