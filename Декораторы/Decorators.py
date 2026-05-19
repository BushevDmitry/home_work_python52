'''Задача 1'''

import functools

# def hello(func):
#     def whrapper():
#         print('Привет!')
#         func()
#         print('Пока!')
#     return whrapper
#
# @hello
# def friend():
#     print('Друг!')
#
# friend()





'''Задача 2'''
# def log_name(func):
#     def whrapper(*args):
#         return f'Функция {func.__name__} принимает следующие значения: {args}'
#     return whrapper
#
# @log_name
# def name(*args):
#     return args
#
# print(name('Иван','Степан', 'Ярослав'))





'''Задача 3'''

# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# import time
# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         print(f'Время выполнения кода = {end-start:.6f} секунд')
#         return result
#     return wrapper
#
#
# @timer
# def binar_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (right + left) // 2
#
#         if arr[mid] == target:
#             return mid
#
#         elif arr[mid] < target:
#             left = mid + 1
#
#         elif arr[mid] > target:
#             right = mid - 1
#
#     return -1
#
#
# binar_search(arr, 10)





'''Задача 4'''

# def count_calls(func):
#     func.call_count = 0
#
#     def wrapper():
#         func.call_count += 1
#         return f'Функция {func.__name__} была вызвана {func.call_count} раз'
#     return wrapper
#
# @count_calls
# def greet():
#     return f"Привет!"





'''Задача 5'''
#
# from functools import wraps
#
#
# def cache(func):
#     cached_results = {}
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = (args, tuple(sorted(kwargs.items()))) # Создаём ключ из позиционных и именованных аргументов
#
#         if key in cached_results:
#             return cached_results[key]
#         else:
#             result = func(*args, **kwargs)
#             cached_results[key] = result
#             return result
#
#     return wrapper
#
#
# @cache
# def calc(x, y):
#     print(f"Вычисляем: {x} * {y} = {x * y}")
#     return x * y
#
# calc(2, 3)
# calc(3, 2)





'''Задача №6'''

# current_role = 'admin'
#
# def require_role(role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if current_role == role:
#                 return func(*args, **kwargs)
#             else:
#                 print(f"Доступ запрещен. Требуется роль: {role}, текущая роль: {current_role}")
#         return wrapper
#     return decorator
#
#
# @require_role("admin")
# def delete_user(user_id):
#     print(f"Пользователь {user_id} удален")
#
# delete_user("Сергей")





'''Задача 7'''

# def retry(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for attempt in range(n):
#                 try:
#                     result = func(*args, **kwargs)
#                     print(f"Успех на попытке {attempt + 1}!")
#                     return result
#                 except Exception as e:
#                     print(f"Ошибка на попытке {attempt + 1}: {e}")
#                     if attempt == n - 1:  # если это последняя попытка
#                         raise e
#         return wrapper
#     return decorator
#
# @retry(n=3)
# def add():
#     a = float(input("Введите первое число: "))
#     b = float(input("Введите второе число: "))
#     return a + b
#
# print(add())





'''Задача 8'''

# def validate_types(expected_a_type, expected_b_type):
#     def decorator(func):
#         def wrapper(a, b):
#             if not isinstance(a, expected_a_type):
#                 raise TypeError(
#                     f"Аргумент 'a' должен быть типа {expected_a_type.__name__}, "
#                     f"но получено {type(a).__name__}"
#                 )
#
#             if not isinstance(b, expected_b_type):
#                 raise TypeError(
#                     f"Аргумент 'b' должен быть типа {expected_b_type.__name__}, "
#                     f"но получено {type(b).__name__}"
#                 )
#
#             return func(a, b)
#
#         return wrapper
#
#     return decorator
#
# @validate_types(int, int)
# def add(a, b):
#     return a + b
#
# add(1,'a')