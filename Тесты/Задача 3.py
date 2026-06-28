
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Ошибка: сумма не может быть отрицательной")
            return
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount < 0:
            print("Ошибка: сумма не может быть отрицательной")
            return
        if amount > self.balance:
            print("Ошибка: недостаточно средств")
            return
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance



import unittest


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Создаём счёт перед каждым тестом"""
        self.account = BankAccount(100)

    def test_initial_balance(self):
        """Проверка начального баланса"""
        acc = BankAccount()
        self.assertEqual(acc.get_balance(), 0)

        acc2 = BankAccount(500)
        self.assertEqual(acc2.get_balance(), 500)

    def test_deposit(self):
        """Проверка пополнения"""
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

        self.account.deposit(0)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        """Проверка снятия"""
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

        self.account.withdraw(70)  # снимаем всё
        self.assertEqual(self.account.get_balance(), 0)

    def test_withdraw_too_much(self):
        """Попытка снять больше, чем есть"""
        self.account.withdraw(200)  # должно вывести ошибку
        self.assertEqual(self.account.get_balance(), 100)  # баланс не изменился

    def test_negative_amounts(self):
        """Отрицательные суммы"""
        self.account.deposit(-50)  # должно вывести ошибку
        self.assertEqual(self.account.get_balance(), 100)

        self.account.withdraw(-30)  # должно вывести ошибку
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()