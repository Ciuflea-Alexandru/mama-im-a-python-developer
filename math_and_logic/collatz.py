# Calculates the stopping time sequence to reach 1 using the The collatz conjecture (also known as the 3n + 1 problem)

def collatz_sequence(n):
    """Generates the Collatz sequence for a given number n."""
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example usage:
number = 12
result = collatz_sequence(number)

print(f"Collatz sequence for {number}:")
print(result)
print(f"Total steps to reach 1: {len(result) - 1}")