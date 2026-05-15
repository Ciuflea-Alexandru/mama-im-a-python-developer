# Find the second smallest number in a list

def find_second_smallest(lst):
    f = float('inf')
    s = float('inf')
    if len(lst) < 2:
        return None
    else:
        for n in lst:
            if n < f:
                s = f
                f = n
            elif f < n < s:
                s = n
    return s

list = [4, 5, 6, 3]
print(find_second_smallest(list))