my_list = [1, 2.5, (3+2j), False, 'str', None, (3, 4, 5), [6, 7], {8, 9},
           {10 : 'десять', 11: 'одинадцать'}]
for i, item in enumerate(my_list, 1):
    print(f'{i}) {item} - {type(item)}')
