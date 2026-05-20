# Given a list and a specific element of that elemnt find the index of the element

def find_index(lst, number):
    r = []
    for n in lst:
        # Check if the item is a number or a list
        if isinstance(n, list):
            # Recursively call the function to flatten the inner list
            r.extend(find_index(n, number))
        else:
            if n == number:
                r.append(1)
            else:
                r.append(0)
    return r

lst = [[0, 2, [1, [2]]], 2]
number = 2
print(find_index(lst, number))
