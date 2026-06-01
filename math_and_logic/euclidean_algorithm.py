# find the greatest common divisor of two numbers

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

num1, num2 = 48, 18
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")