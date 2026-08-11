def flatten_list(nested):
    """
    Recursively flattens a nested list structure of arbitrary depth.
    """
    flat = []
    for item in nested:
        if isinstance(item, list):
            # Recursively flatten the sub-list and extend our result list
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# Example Usage
if __name__ == "__main__":
    nested_structure = [1, [2, [3, 4], 5], [6, 7], 8]
    
    result = flatten_list(nested_structure)
    print(f"Original nested list: {nested_structure}")
    print(f"Flattened list:       {result}")