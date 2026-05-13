# Return a tuple with the sum of two fractions

from fractions import Fraction

def add_fractions(numerator1, denominator1, numerator2, denominator2):
    f1 = Fraction(numerator1, denominator1)
    f2 = Fraction(numerator2, denominator2)
    r = f1 + f2
    return r.numerator, r.denominator

numerator1 = 1
denominator1 = 2
numerator2 = 1
denominator2 = 3

result = add_fractions(numerator1, denominator1, numerator2, denominator2)
print(result)