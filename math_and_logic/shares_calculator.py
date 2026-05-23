# Calculate home many fractional sheres you bought

def share_calculators(current_shares, investment, old_price, new_price):
    # 1. Removed the * 100 so you get actual share counts
    fractional_shares = investment / new_price
    
    # 2. Used a clear variable name for the new total
    total_shares = current_shares + fractional_shares
    
    # 3. Calculated Total Money Spent / Total Shares
    total_money_spent = (current_shares * old_price) + investment
    avg_price = total_money_spent / total_shares
    
    # 4. Added the percentage calculation
    percentage_new = (fractional_shares / total_shares) * 100

    return fractional_shares, total_shares, avg_price, percentage_new

current_shares = 2.5
investment = 700.00
old_price = 1800.00
new_price = 1200.00

new_shares, total_sh, average, pct = share_calculators(current_shares, investment, old_price, new_price)

print(f"New Shares Bought: {new_shares:.4f}")
print(f"New Total Shares: {total_sh:.4f}")
print(f"New Average Buy Price: €{average:.2f}")
print(f"New Shares Portfolio Weight: {pct:.2f}%")
