# Returns the square of a number using only the functions

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num - 1)

number = 3
print(square(number))

# Return multiple numbers and their squares in a list of tuples

def square_items_with_tuples(lst: list[int]) -> list[tuple[int, int]]:
    result = []
    for n in lst:
        result.append((n, n * n))
    
    return result

list = [1, 2, 3]
print(square_items_with_tuples(list))