# handle conversions from a base-10 integer to any base (up to 36, using digits 0-9 and letters A-Z) and vice-versa

import string

def decimal_to_base(n, base):
    """Converts a decimal integer to a string representation in the given base."""
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36")
    if n == 0:
        return "0"
    
    digits = string.digits + string.ascii_uppercase
    result = ""
    
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

def base_to_decimal(s, base):
    """Converts a string representation of a number in a given base to decimal."""
    if not 2 <= base <= 36:
        raise ValueError("Base must be between 2 and 36")
    
    # int() has a built-in base parameter, but this is the manual logic:
    digits = string.digits + string.ascii_uppercase
    n = 0
    for char in s.upper():
        n = n * base + digits.index(char)
    return n

# Example Usage
if __name__ == "__main__":
    number = 255
    target_base = 16
    
    converted = decimal_to_base(number, target_base)
    print(f"Decimal {number} in base {target_base} is: {converted}")
    
    reverted = base_to_decimal(converted, target_base)
    print(f"Base {target_base} '{converted}' back to decimal is: {reverted}")