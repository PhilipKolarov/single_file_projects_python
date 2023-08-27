def length_check(min, max, text):
    text_as_array = text.split(' ')
    if len(text_as_array) < min:
        diff = min - len(text_as_array)
        return f'The text is {diff} words too short.'
    elif len(text_as_array) > max:
        diff = len(text_as_array) - max
        return f'The text is {diff} words too long.'
    else:
        return 'The text is within range!'


text_to_be_checked = 'My name is Philip Kolarov and I am a python developer. I have been programming for two years now.'
min_length = 20
max_length = 50
print(length_check(min_length, max_length, text_to_be_checked))
