# Returns the square of a number using only the functions

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num - 1)

number = 6
print(square(number))