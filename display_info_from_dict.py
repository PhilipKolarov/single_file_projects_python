def letter_counter(subject, letter):
    counter = 0
    if isinstance(subject, str):
        for i in range(len(subject)):
            if subject[i] == letter:
                counter += 1
        return counter
    else:
        return 0


def info_retriever(dictionary, *args):
    command = args[0]

    if command == 'display':
        result = ''
        for key, value in dictionary.items():
            current_string = f'{key} - {value} \n'
            result += current_string
        result += '----------'
        return result

    elif command == 'letter_count':
        current_letter = args[1]
        current_letter_count = 0
        for value in dictionary.values():
            current_letter_count += letter_counter(value, current_letter)
        result = f'The letter "{current_letter}" appears {current_letter_count} time(s) amongst all values.'
        return result


my_dict = {'A': 'first letter', 'B': 'second letter', 'Z': 'last letter'}
print(info_retriever(my_dict, 'display'))
print(info_retriever(my_dict, 'letter_count', 'l'))
