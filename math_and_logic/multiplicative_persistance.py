# Find out how many times you have to multiply the digits of a number until you reach a single digit number

def multiplicative_persistence(n):
    steps = 0
    
    while n >= 10:
        product = 1
        current_number = n
        
        # Mathematically extract digits and multiply them
        while current_number > 0:
            digit = current_number % 10
            product *= digit
            current_number = current_number // 10
            
        n = product
        steps += 1
        
    return steps

print(multiplicative_persistence(999))