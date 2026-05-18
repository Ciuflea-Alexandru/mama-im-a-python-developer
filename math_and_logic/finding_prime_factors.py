# Find the prime factors of a number

def find_prime_factors(num):
    r = []
    n = 2
    while num > 1:
        if num % n == 0:
            r.append(n)
            num //= n
        else:
            n += 1
    return r

num = 630
print(find_prime_factors(num))
