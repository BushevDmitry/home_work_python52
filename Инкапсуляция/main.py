'''Задача №1'''
class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.__password = password

    def get_password(self):
        return self.__password


person = User("Иван", "ivan@mail.ru", "qwerty")
print(person.name)
print(person._email)

print(person.__password) #Выведет ошибку
print(person.get_password())
print(person._User__password)

'''Так как атрибут __password является приватным,
для обращения к его значению необходимо создать отдельный метод get_password,
либо через имя класса, используя _User__password'''





'''Задача №2'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance


    def get_balance(self):
        return self.__balance


    def withdraw(self, amount, value):
        if amount < 0:
            print('Введите положительное число')
            return False
        elif amount > self.__balance:
            print('Вы превысили сумму снятия')
            return False
        else:
            self.__balance -= amount
            print(f'Вы сняли {amount} рублей')
            return self.__balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Вы пополнили счёт на {amount} рублей')
            return self.__balance
        else:
            print('Сумма должна быть положительной')
            return False

user = BankAccount(1000)
user.deposit(500)
print(user.get_balance())

user.withdraw(100)
print(user.get_balance())





'''Задача 3'''
class BankAccount:
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        if not new_owner or not new_owner.strip():
            raise ValueError('Вы ввели пустую строку')
        self.__owner = new_owner



user = BankAccount(100,'Иван')
print(f'Изначальное имя пользователя - {user.owner}')


try:
    user.owner = ' '
except ValueError:
    print('Вы ввели пустую строку')


user.owner = 'Степан'
print(f'Меняем имя пользователя на - {user.owner}')





'''Задача 4'''

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
        if self.__celsius < -273.15:
            raise ValueError('Температура не может быть ниже -273.15 градусов')

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Температура не может быть ниже -273.15 градусов')
        self.__celsius = value


    @property
    def fahrenheit(self):
        return self.__celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius_value = (value - 32) * 5 / 9
        if celsius_value < -273.15:
            raise ValueError('Температура не может быть ниже -273.15 градусов')
        self.__celsius = celsius_value

temp = Temperature(20)

try:
    temp.celsius = float(input('Введите значение температуры по фаренгейту: '))
except ValueError:
    print('Температура не может быть ниже -273.15 градусов по цельсию')

print(f'Текущее значение температуры по цельсию = {temp.celsius}' '\n')


try:
    temp.fahrenheit = float(input('Введите значение температуры по фаренгейту: '))
except ValueError:
    print('Температура не может быть ниже -273.15 градусов по цельсию')

print(f'Текущее значение температуры по цельсию = {temp.celsius}, что = {temp.fahrenheit} по фаренгейту ')





'''Задача 5'''
class Order:

    def __init__(self):
        self.__items = []
        self.__status = 'new'


    def pay(self):
        if self.__status == 'new':
            self.__status = 'paid'

    def ship(self):
        if self.__status == 'paid':
            self.__status = 'shipped'

    def get_summary(self):
        return self.__items.copy()

    def add_item(self, item):
        if self.__status == "new":
            self.__items.append(item)


    @property
    def status(self):
        return self.__status



user = Order()
print(f"Статус: {user.status}")

user.add_item('Апельсины')
user.add_item('Яблоки')
print(f"Товары: {user.get_summary()}")


user.pay()
print(f"Статус: {user.status}")

user.add_item('бананы') #Пытаюсь добавить товар после оплаты
print(f"Товары: {user.get_summary()}")

user.ship()
print(f"Статус: {user.status}")







