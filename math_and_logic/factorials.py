# Return the factorial of a number

def factorial(num):
    if not isinstance(num, int) or num < 0:
        return None
    if num == 0:
        return 1

    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result

number = 5
print(factorial(number))