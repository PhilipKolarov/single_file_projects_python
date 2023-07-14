input_string = input()
input_as_array = input_string.split('|')
sum_of_ints = 0
int_count = 0

for el in input_as_array:
    if el.isnumeric():
        sum_of_ints += int(el)
        int_count += 1
    else:
        pass

print(f"The sum of the integers in your input is {sum_of_ints}.")
print(f"The amount of integers in your input is {int_count}.")
