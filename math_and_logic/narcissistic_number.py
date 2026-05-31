# Find out if a number is the sum of its own digits each raised to the power of the number of digits

def narcissist_number(narcissist):
    lst = str(narcissist)
    d = len(lst)
    r = 0
    for n in lst:
        r += int(n) ** d

    return r == narcissist

narcissist = 153
print(narcissist_number(narcissist))