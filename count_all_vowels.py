def vowel_counter(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    extracted_vowels = {}
    index = 0

    while text != '':
        if index >= len(text):
            break

        ch = text[index]
        if ch in vowels:
            if ch in extracted_vowels.keys():
                extracted_vowels[ch] += 1
            else:
                extracted_vowels[ch] = 1
        else:
            pass

        index += 1

    return extracted_vowels


for key, value in vowel_counter('Bohemian Rhapsody').items():
    print(f'{key} - {value}')
