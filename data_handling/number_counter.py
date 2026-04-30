#Given a string count the even and odd numbers from it

def count_numbers(which, numbers):
    if which != 'even' and which != 'odd':
        return -1
    
    result = 0
    for num in numbers:
        if which == 'even' and num % 2 == 0:
            result += 1
        if which == 'odd' and num % 2 != 0:
            result += 1
    return result

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

even_count = count_numbers('even', numbers)
print(f"Even numbers: {even_count}")

odd_count = count_numbers('odd', numbers)
print(f"Odd numbers: {odd_count}")