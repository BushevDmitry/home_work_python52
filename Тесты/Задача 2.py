
def count_vowels(text):
    """Считает гласные буквы (русские и английские)"""
    vowels = 'aeiouyаеёиоуыэюяAEIOUYАЕЁИОУЫЭЮЯ'
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count


def is_palindrome(text):
    """Проверяет, является ли строка палиндромом"""
    # Убираем пробелы и приводим к нижнему регистру
    text = text.replace(" ", "").lower()
    return text == text[::-1]  # Сравниваем с перевёрнутой версией


def reverse_string(text):
    """Переворачивает строку"""
    return text[::-1]



import unittest


class TestStringFunctions(unittest.TestCase):

    # Тест подсчёта гласных
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)  # e, o
        self.assertEqual(count_vowels("привет"), 2)  # и, е
        self.assertEqual(count_vowels("AEIOU"), 5)  # все гласные
        self.assertEqual(count_vowels(""), 0)  # пустая строка
        self.assertEqual(count_vowels("bcdfg"), 0)  # нет гласных
        self.assertEqual(count_vowels("123"), 0)  # только цифры
        self.assertEqual(count_vowels("Hello мир"), 3)  # смешанный текст

    # Тест палиндрома
    def test_palindrome(self):
        self.assertTrue(is_palindrome("топот"))  # простой палиндром
        self.assertTrue(is_palindrome("Madam"))  # разный регистр
        self.assertTrue(is_palindrome("а роза упала на лапу азора"))  # с пробелами
        self.assertTrue(is_palindrome(""))  # пустая строка
        self.assertTrue(is_palindrome("12321"))  # цифры
        self.assertFalse(is_palindrome("hello"))  # не палиндром
        self.assertFalse(is_palindrome("привет"))  # не палиндром

    # Тест реверса
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("мир"), "рим")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string("Hello world"), "dlrow olleH")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()