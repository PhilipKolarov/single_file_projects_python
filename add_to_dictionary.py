def add_to_my_dict(my_list):
    for x in range(len(my_list)):
        elements = my_list[x].split(' - ')
        key = elements[0]
        value = elements[1]
        my_dict[key] = value


my_dict = {}
input_string = input()
input_list = input_string.split('|')

add_to_my_dict(input_list)
print(my_dict)
