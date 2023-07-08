def erase_every_second_character(input_string):
    output_string = ''

    for i in range(len(input_string)):
        if i % 2 == 0:
            output_string += input_string[i]
        else:
            pass

    return output_string


result = erase_every_second_character(input())
print(result)
