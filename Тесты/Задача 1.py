import unittest


def add(a, b):
    """Сложение"""
    return a + b


def subtract(a, b):
    """Вычитание"""
    return a - b


def multiply(a, b):
    """Умножение"""
    return a * b


def divide(a, b):
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b




"""В отдельном файле test_calculator.py не получилось запустить тесты"""
class TestCalculator(unittest.TestCase):

#Сложение
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 5), 15)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 7), 7)


#Вычитание
    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)

#Умножение
    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_float(self):
        self.assertEqual(multiply(2.5, 2), 5.0)

#Деление
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
        with self.assertRaises(ValueError):
            divide(0, 0)
        with self.assertRaises(ValueError):
            divide(-5, 0)

    def test_divide_float(self):
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(1, 3), 1 / 3)



if __name__ == "__main__":
    # Запускаем все тесты
    unittest.main()