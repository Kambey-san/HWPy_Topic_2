while True:
    month_number = input('Введите номер месяца: ')
    if month_number.isdigit() and 0 < int(month_number) <= 12:
        season_list = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_dict = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Сезон(список): {season_list[int(month_number) // 3]}')
        print(f'Сезон(словарь): {season_list[int(month_number) // 3]}')
        break






