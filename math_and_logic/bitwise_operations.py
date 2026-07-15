def swap_integers(a, b):
    """Swaps two integers using the XOR bitwise operator without a temporary variable."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def is_power_of_two(n):
    """Checks if a number is a power of two using bitwise AND."""
    # Powers of two in binary have exactly one '1' bit (e.g., 4 is 100, 3 is 011)
    # n & (n - 1) will be 0 only if n is a power of two
    return n > 0 and (n & (n - 1)) == 0

def count_set_bits(n):
    """Counts the number of 1s in the binary representation of a number."""
    count = 0
    while n > 0:
        # Clears the least significant set bit
        n &= (n - 1)
        count += 1
    return count

# Example Usage
if __name__ == "__main__":
    x, y = 10, 20
    print(f"Before swap: x={x}, y={y}")
    x, y = swap_integers(x, y)
    print(f"After swap: x={x}, y={y}")
    
    print(f"Is 16 a power of two? {is_power_of_two(16)}")
    print(f"Number of 1s in binary of 11 (1011): {count_set_bits(11)}")