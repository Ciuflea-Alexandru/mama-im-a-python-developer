# perform precise financial calculations

from decimal import Decimal, getcontext, ROUND_HALF_UP

# 1. Set the global precision (optional, default is 28 places)
getcontext().prec = 6

# 2. Use strings to initialize Decimals to avoid float precision errors
# Never initialize with a float: Decimal(0.1) creates an inaccurate value
price = Decimal('19.99')
quantity = Decimal('3')
tax_rate = Decimal('0.075')

# 3. Perform calculations
subtotal = price * quantity
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

# 4. Rounding to two decimal places (standard for currency)
# ROUND_HALF_UP ensures .5 rounds away from zero (standard commercial rounding)
final_total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax_amount.quantize(Decimal('0.01'))}")
print(f"Final Total (Rounded): ${final_total}")

# 5. Comparing the difference
print("-" * 20)
print(f"Float math error (0.1 + 0.2): {0.1 + 0.2}")
print(f"Decimal math (0.1 + 0.2): {Decimal('0.1') + Decimal('0.2')}")