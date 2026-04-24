'''Задача 1'''
# def split_bill(total, people):
#     try:
#         return total/people
#     except ZeroDivisionError:
#         print('Нельзя делить на 0 друзей!')
#     except TypeError:
#         print('Нужно ввести число, а не строку')
#
# print(split_bill(100,2))




'''Задача 2'''
# def check_age():
#     while True:
#         try:
#             age = int(input('Введите возраст: '))
#             print(f'Ваш возраст {age}')
#             break
#         except ValueError:
#             print('Вы ввели некорректное значение')
#
# check_age()




'''Задача 3'''
# def read_config(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             return file.read()
#     except FileNotFoundError:
#         return 'Конфиг не найден, используем настройки по умолчанию'
#     finally:
#         print('Попытка чтения завершена')
#
# file = read_config('file.txt')
# print(file)



'''Задача 4'''
# class WeakPasswordError(Exception):
#     pass
#
# def check_password(pwd):
#     if len(pwd) < 8:
#         raise WeakPasswordError('Слишком короткий пароль')
#     elif not any(char.isdigit() for char in pwd):
#         raise WeakPasswordError('Пароль должен содержать цифры')
#
#     return pwd
#
# try:
#     name = check_password(input('Введите пароль: '))
#     print(f'Успешно! Ваш пароль: {name}')
# except WeakPasswordError as e:
#     print(f'Ошибка: {e}')




'''Задача 5'''

# dict1 = {
#         'фрукты':['апельсины', 'яблоки', 'ананасы'],
#          'молочные продукты':['мясо', 'творог', 'молоко'],
#          'овощи':['огурцы', 'лук', 'помидоры'],
#          'снэки':'чипсы'
#          }
#
# def get_value(data, key, index):
#     try:
#         shop_list = data[key]
#
#         if type(shop_list) != list:
#             raise TypeError(f'Ключ {key} не является списком')
#
#         return shop_list[index]
#     except KeyError:
#         print(f"Ошибка: ключ '{key}' отсутствует в словаре")
#
#     except IndexError:
#         print(f"Ошибка: индекс {index} выходит за пределы списка")
#
#     except TypeError as e:
#         print(f"Ошибка типа: {e}")
#
# print(get_value(dict1, 'фрукты',10))
# print(get_value(dict1, 'qwerty',1))
# print(get_value(dict1, 'снэки',0))

