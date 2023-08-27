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


first_text_to_be_checked = 'My name is Philip Kolarov and I am a python developer. I have been programming for two years now.'
first_min_length = 20
first_max_length = 50
print(length_check(first_min_length, first_max_length, first_text_to_be_checked))

second_text_to_be_checked = 'His royal highness will see you now.'
second_min_length = 5
second_max_length = 10
print(length_check(second_min_length, second_max_length, second_text_to_be_checked))

third_text_to_be_checked = 'It is a huge honor to be here. I would like to thank every single one of you for showing up.'
third_min_length = 10
third_max_length = 15
print(length_check(third_min_length, third_max_length, third_text_to_be_checked))
