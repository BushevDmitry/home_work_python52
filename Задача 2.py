from abc import ABC, abstractmethod


# Абстрактный наблюдатель
class Observer(ABC):
    @abstractmethod
    def update(self, stock):
        pass


# Абстрактный субъект
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Конкретная реализация субъекта — акция (биржевой тикер)
class Stock(Subject):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self.observers = []

    def attach(self, observer):

        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):

        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):

        for observer in self.observers:
            observer.update(self)

    # При присваивании новой цены сразу рассылаем уведомления
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price
        self.notify()


# Сообщает о новой цене
class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, stock):
        print(f"[Инвестор {self.name}] Новая цена акции {stock.symbol}: ${stock.price:.2f}")


# Принимает решение о покупке/продаже
class TradingBot(Observer):
    def __init__(self, bot_id, buy_threshold, sell_threshold):
        self.bot_id = bot_id
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def update(self, stock):
        action = None
        reason = ""

        if stock.price <= self.buy_threshold:
            action = "ПОКУПКА"
            reason = f"цена ({stock.price}) <= порога покупки ({self.buy_threshold})"
        elif stock.price >= self.sell_threshold:
            action = "ПРОДАЖА"
            reason = f"цена ({stock.price}) >= порога продажи ({self.sell_threshold})"

        if action:
            print(f"[TradingBot {self.bot_id}] Решение: {action} акции {stock.symbol}. Причина: {reason}")


if __name__ == "__main__":
    # Создаём акцию
    apple = Stock("AAPL", 150.0)

    # Создаём наблюдателей
    investor1 = Investor("Алексей")
    investor2 = Investor("Мария")
    bot1 = TradingBot("Bot-001", buy_threshold=145.0, sell_threshold=160.0)
    bot2 = TradingBot("Bot-002", buy_threshold=140.0, sell_threshold=155.0)

    # Подписываем всех
    apple.attach(investor1)
    apple.attach(investor2)
    apple.attach(bot1)
    apple.attach(bot2)

    print("Цена изменилась до 148.0")
    apple.price = 148.0

    print("\nЦена упала до 142.0 (ниже порога покупки)")
    apple.price = 142.0

    print("\nЦена выросла до 162.0 (выше порога продажи)")
    apple.price = 162.0

    print("\nМария отписывается от уведомлений")
    apple.detach(investor2)

    print("\nЕщё одно изменение цены до 155.0")
    apple.price = 155.0
