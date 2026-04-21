'''Задача №1'''
class Shape:
    def __init__(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        square = self.width * self.height
        return square

    def info(self):
        return f'Площадь = {self.area()}, цвет = {self.color}'

rectagle = Rectangle('blue', 20, 10)
print(rectagle.info())





'''Задача №2'''
class Animal:
    def __init__(self, species = 'неизвестно'):
        self.species = species


class Pet(Animal):
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name, species = 'собака')
        self.breed = breed

    def describe(self):
        return f' Вид: {self.species}, имя: {self.name}, порода: {self.breed}'


dog = Dog('Бобик', 'Немецкая овчарка')
print(dog.describe())



'''Задача №3'''
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print('Недостаточно средств')
        else:
            self.balance -= amount
            print(f"Списано {amount}. Баланс: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, owner, balance, min_balance):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if  self.balance - amount >= self.min_balance:
            super().withdraw(amount)

        else:
            print('Недостаточно средств')

person = SavingsAccount('Иван',1000,100)
person.withdraw(20)
