'''Задача №1'''
from logging import Logger
from pydoc import describe

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '...'

class  Dog(Animal):
    def speak(self):
        return 'Гав'

class Cat(Animal):
    def speak(self):
        return 'Мяу'

animal = Animal('Животное')
dog = Dog('Бобик')
cat= Cat('Муся')

print(animal.speak())
print(dog.speak())
print(cat.speak())




'''Задача №2'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def info(self):
        return f'{self.name}, {self.age} лет, {self.university}'

ivan = Student('Иван', 20, 'МГУ')
print(ivan.info())



'''Задача №3'''
import datetime
class Logger:
    def log(self, message):
        print(message)

class TimestampLogger(Logger):
    def log(self, message):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        timestamped_message = f"[{current_time}] {message}"
        super().log(timestamped_message)

logger = TimestampLogger()
logger.log("- время на данный момент")





'''Задача №4'''
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f'Brand:{self.brand}, максимальная скорость = {self.speed}'

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def describe(self):
        car_describe = super().describe()
        return f'{car_describe}, тип топлива- {self.fuel_type}'

class ElectricCar(Vehicle):
    def __init__(self, brand, speed, fuel_type, battery_capacity):
        super().__init__(brand, speed, fuel_type)
        self.battery_capacity = battery_capacity

    def describe(self):
        electric_car = super.describe()
        return f'{electric_car}, {self.battery_capacity}'




'''Задача №5'''
class Shape:

    def area(self):
        pass

    @staticmethod
    def sum(*shapes):
        total = 0
        for shape in shapes:
            total += shape.area()
        return total



class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width




class Triangle(Shape):

    def __init__(self, h, sup_triangle):
        self.h = h
        self.sup_triangle = sup_triangle

    def area(self):
        return (0.5 * self.h) * self.sup_triangle




class Circle(Shape):
    def __init__(self, r):
        self.pi = 3.14
        self.r = r

    def area(self):
        return self.pi * self.r**2





rectangle = Rectangle(4, 5)
print(rectangle.area())

triangle = Triangle(2, 3)
print(triangle.area())

circle = Circle(4)
print(circle.area())



shape = Shape()
print(shape.sum(rectangle, triangle, circle))
