def letter_counter(ch, text):
    text_length = len(text)
    ch_counter = 0

    for i in range(text_length):
        current_ch = text[i]
        if ch == current_ch:
            ch_counter += 1

    return ch_counter


letter_search = input()
input_string = input()
print(letter_counter(letter_search, input_string))
