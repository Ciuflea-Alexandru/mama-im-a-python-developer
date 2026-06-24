# implement recursion with memoization (to optimize performance) and iteration (which is more memory-efficient)

# Using a dictionary to store calculated values (Memoization)
memo = {}

def fib_recursive(n):
    """Calculates Fibonacci using recursion with memoization."""
    if n <= 0: return 0
    if n == 1: return 1
    if n in memo: return memo[n]
    
    memo[n] = fib_recursive(n - 1) + fib_recursive(n - 2)
    return memo[n]

def fib_iterative(n):
    """Calculates Fibonacci using iteration (O(n) time, O(1) space)."""
    if n <= 0: return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Testing the functions
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} (recursive): {fib_recursive(n)}")
    print(f"Fibonacci number at position {n} (iterative): {fib_iterative(n)}")