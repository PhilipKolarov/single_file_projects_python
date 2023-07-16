def tracker(num, operation, new_num):
    if operation == 'add':
        num += new_num
    elif operation == 'subtract':
        num -= new_num
    elif operation == 'multiply':
        num *= new_num
    elif operation == 'divide':
        num /= new_num
    elif operation == 'power':
        num **= new_num
    return num


my_number = 0
my_number = tracker(my_number, 'add', 6)
my_number = tracker(my_number, 'subtract', 5)
my_number = tracker(my_number, 'multiply', 10)
my_number = tracker(my_number, 'multiply', 6)
my_number = tracker(my_number, 'divide', 12)
my_number = tracker(my_number, 'power', 2)
print(my_number)

i = 1
i = tracker(i, 'divide', 2)
i = tracker(i, 'add', 4)
i = tracker(i, 'divide', 1.5)
i = tracker(i, 'power', 4)
i = tracker(i, 'subtract', 80)
print(i)
