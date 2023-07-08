def erase_every_second_character(input_string):
    output_string = ''

    for i in range(len(input_string)):
        if i % 2 == 0:
            output_string += input_string[i]
        else:
            pass

    return output_string


first_result = erase_every_second_character('HOi-!') #Hi!
print(first_result)


def erase_every_third_character(input_string):
    output_string = ''

    for i in range(len(input_string)):
        if (i + 1) % 3 != 0:
            output_string += input_string[i]
        else:
            pass

    return output_string


second_result = erase_every_third_character('Go8odBby{e!') #Goodbye!
print(second_result)
