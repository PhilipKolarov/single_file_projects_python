input_string = input()
input_as_array = input_string.split('|')
sum_of_ints = 0

for el in input_as_array:
    if el.isnumeric():
        sum_of_ints += int(el)
    else:
        pass

print(f'Total: {sum_of_ints}')
