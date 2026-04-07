from random import sample

'''Задание №1'''

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





'''Задание №2 '''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

ivan = Person('Иван', 20)

name_ivan = getattr(ivan, 'name')
email_ivan = getattr(ivan, 'email','не указан')

print(name_ivan)
print(email_ivan)




'''Задание №3'''

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
