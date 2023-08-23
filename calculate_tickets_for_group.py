STANDARD_PRICE = 15
CHILD_PRICE = 10


def calc_ticket_price_total(standard, child, voucher):
    total = standard * STANDARD_PRICE + child * CHILD_PRICE
    if voucher:
        total -= voucher * total

    return total


print(calc_ticket_price_total(4, 2, None))
print(calc_ticket_price_total(6, 5, 0.2))
