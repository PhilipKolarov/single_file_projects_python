def calculate_change(price, given_money):
    if price > given_money:
        diff = price - given_money
        return f'You require {diff:.2f} more to pay the necessary price!'
    else:
        change = given_money - price
        return f'{change:.2f}'


print(calculate_change(56.45, 60))
print(calculate_change(12.99, 100))
print(calculate_change(124.99, 90))
