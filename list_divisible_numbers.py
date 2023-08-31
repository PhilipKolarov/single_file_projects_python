def list_divisible_numbers(num):
    prime_numbers_array = []
    num_half = num // 2
    for x in range(2, num_half + 1):
        if num % x == 0:
            prime_numbers_array.append(str(x))

    prime_numbers_array_as_string = ', '.join(prime_numbers_array)
    return prime_numbers_array_as_string


print(list_divisible_numbers(20))
print(list_divisible_numbers(45))
print(list_divisible_numbers(720))
