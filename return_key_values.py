def return_key_values(name, **kwargs):
    output_string = f'{name}:'

    if kwargs:
        for key, value in kwargs.items():
            output_string += f'\n{key} - {value}'

    output_string += '\n ---------- '
    return output_string


print(return_key_values('My Dictionary', A='apple', B='bannana', C='cranberry'))
