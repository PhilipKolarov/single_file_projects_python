def info_retriever(dictionary, *args):
    if args[0] == 'display':
        result = ''
        for key, value in dictionary.items():
            current_string = f'{key} - {value} \n'
            result += current_string
        result += '----------'
        return result
    elif args[0] == 'letter_count':
        pass


my_dict = {'A': 'first letter', 'B': 'second letter', 'Z': 'last letter'}
print(info_retriever(my_dict, 'display'))
