from random import sample

'''Задание:
Часть кода уже написана
Создайте класс Magic
Создайте атрибут класса ingredients со значением sample(magic_ing, 3). 
Таким образом создастся список из трёх рандомных ингредиентов для коктейля.
Создайте экземпляр my_cocktail от класса Magic (не забудьте скобки).
С помощью цикла и getattr(), выведите на экран три ингредиента, которые находятся в атрибуте ingredients, 
используя экземпляр. Если не получится, можете вывести без цикла, но с помощью getattr() для тренировки. 
Не забывайте кавычки в имени атрибута.
Нажмите кнопку "Запустить код", таким образом вы увидите ингредиенты, 
которые Машенька приготовила для вашего коктейля.'''

class Magic:

    magic_ing = [
    'лунный свет',
    'звёздная пыль',
    'крыло феи',
    'капля радуги',
    'шепот ветра',
    'кристалл единорога',
    'эссенция мечты',
    'роса с заколдованного леса'
]

    ingredients = sample(magic_ing, 3)

my_cocktail = Magic()

for i in range(3):
    ingredients_list = getattr(my_cocktail, "ingredients")
    print(f"Ингредиент {i + 1}: {ingredients_list[i]}")





'''Задание 1) Есть класс Person с атрибутами name и age. 
Используйте getattr, чтобы получить значение name, 
а также попробуйте получить несуществующий атрибут email с значением по умолчанию "не указан". '''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

ivan = Person('Иван', 20)

name_ivan = getattr(ivan, 'name')
email_ivan = getattr(ivan, 'email','не указан')

print(name_ivan)
print(email_ivan)




'''Задание 2) Напишите функцию print_attrs(obj, attr_names), 
которая принимает объект и список строк — имён атрибутов — и печатает их значения. 
Если атрибута нет, выводите "—".'''

class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

def print_attrs(obj, attr_names):
    for attr_name in attr_names:
        value = getattr(obj,attr_name,'-')
        print(f'{attr_name} = {value}')

person = Person('John',25)
print_attrs(person,['name','age','email','number'])
