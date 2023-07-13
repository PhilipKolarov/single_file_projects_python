def longest_word_checker(text):
    text_as_array = text.split(' ')
    longest_word = ''
    longest_word_length = 0

    for word in text_as_array:
        if word.isalpha() and len(word) > longest_word_length:
            longest_word = word
            longest_word_length = len(word)

    result = [longest_word, longest_word_length]
    return result


input_text = input()
longest_word_info = longest_word_checker(input_text)
print(f'The longest word in this text is {longest_word_info[0]}, which contains {longest_word_info[1]} letters.')
