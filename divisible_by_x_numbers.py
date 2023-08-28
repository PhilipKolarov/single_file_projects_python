def divisible_by_x_numbers(num, *args):
    divisible_div_array = []
    for n in args:
        if num % n == 0:
            divisible_div_array.append(n)

    length_array = len(divisible_div_array)
    if length_array == len(args):
        return f'YES! {num} is divisible by all numbers.'
    elif length_array == 0:
        return 'No divisible numbers received.'
    else:
        connector = ', '
        return f'{num} is divisible by {connector.join([str(x) for x in divisible_div_array])}.'


print(divisible_by_x_numbers(24, 2, 3, 4, 8))
print(divisible_by_x_numbers(33, 11, 3, 7, 9, 1, 14, 33))
print(divisible_by_x_numbers(13, 2, 7, 26))
