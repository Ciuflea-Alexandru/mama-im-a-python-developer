#  Recursively searches for a target value in a nested list structure.

def recursive_search(data, target):
    for element in data:
        # Check if the current element matches the target
        if element == target:
            return True
        
        # If the element is a list, recurse into it
        elif isinstance(element, list):
            if recursive_search(element, target):
                return True
                
    return False

if __name__ == "__main__":
    nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
    
    search_value = 4
    result = recursive_search(nested_list, search_value)
    
    print(f"Is {search_value} in the list? {result}")
    print(f"Is 10 in the list? {recursive_search(nested_list, 10)}")