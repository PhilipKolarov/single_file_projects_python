def add_to_my_dict(my_list):
    for x in range(len(my_list)):
        elements = my_list[x].split(' - ')
        k = elements[0]
        v = elements[1]
        my_dict[k] = v


my_dict = {}
input_string = input()
input_list = input_string.split('|')

add_to_my_dict(input_list)
for key, value in my_dict.items():
    print(f"{key} - {value}")
