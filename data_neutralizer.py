def neutralize_data(x, data_type, dictionary):
    new_dictionary = {}

    if data_type == 'key':
        for key in dictionary:
            if key != x:
                new_dictionary[key] = dictionary[key]

    elif data_type == 'value':
        for key, value in dictionary.items():
            if value != x:
                new_dictionary[key] = value

    return new_dictionary


my_dict = {'instrument 1': 'guitar', 'instrument 2': 'piano', 'instrument 3': 'ukulele', 'style': 'indie pop'}
my_new_dict = neutralize_data('style', 'key', my_dict)
my_second_new_dict = neutralize_data('ukulele', 'value', my_new_dict)
print(my_second_new_dict)
