# Write a function which returns a list of all prime numbers up to the given input number

def allPrimesUpTo(num):
    prime = [2]
    for n in range(3, num):
        limit = n ** 0.5
        is_prime = True
        for factor in prime:
            if n % factor == 0:
                is_prime = False
                break
            if factor > limit:
                break
        if is_prime:
            prime.append(n)
    return prime

number = 100
print(allPrimesUpTo(number))