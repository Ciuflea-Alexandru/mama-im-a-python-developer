# Swap items in a list

def swap_items(arr: list, index1: int, index2: int) -> list:
    n = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = n
    return arr

numbers = [10, 20, 30, 40]
index1 = 1
index2 = 2

list = swap_items(numbers, index1, index2)
print(list)