def divisible_by_two_numbers(num, first_div, second_div):
    divisible_div_array = []
    if num % first_div == 0:
        divisible_div_array.append(first_div)
    if num % second_div == 0:
        divisible_div_array.append(second_div)

    length_array = len(divisible_div_array)
    if length_array == 2:
        return f'YES! {num} is divisible by both numbers.'
    elif length_array == 1:
        return f'{num} is divisible by {divisible_div_array[0]}.'
    else:
        return 'No divisible numbers received.'


print(divisible_by_two_numbers(6, 3, 2))
print(divisible_by_two_numbers(8, 4, 6))
print(divisible_by_two_numbers(19, 5, 9))
