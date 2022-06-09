my_list = [8, 8, 7, 6, 5, 5, 4, 3, 3]
user_number = int(input('Введте число, обозначающее рейтинг: '))
i = 0
for a in my_list:
    if user_number <= a:
        i += 1

    elif user_number > a:
        break

my_list.insert(i, int(user_number))
print(my_list)