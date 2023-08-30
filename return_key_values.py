def return_key_values(name, **kwargs):
    output_string = f'{name}:'

    if kwargs:
        for key, value in kwargs.items():
            output_string += f'\n{key} - {value}'

    output_string += '\n ---------- '
    return output_string


print(return_key_values('My Dictionary', A='apple', B='banana', C='cranberry'))
print(return_key_values('Temple of Doom', director='Steven Spielberg', producer='George Lucas', music='John Williams'))
print(return_key_values('Football Results', manchester_united=9, liverpool=5, chelsea=3, arsenal=2))
