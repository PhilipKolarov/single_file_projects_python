def metric_convertor(input_string):
    feet_as_str, inches_as_str = input_string.split(' ')
    feet = int(feet_as_str[:-1])
    inches = int(inches_as_str[:-1])
    total_inches = feet * 12 + inches

    total_centimeters = total_inches * 2.54
    total_meters = total_centimeters / 100

    return round(total_meters, 2)

value = input()
print(metric_convertor(value))
