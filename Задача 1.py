from abc import ABC, abstractmethod

#Абстрактный наблюдатель (Observer)
class Observer(ABC):
    @abstractmethod
    def update(self, station: WeatherStation):
        pass


#Конкретные наблюдатели (Observers)

class CurrentConditionDisplay(Observer):
    def update(self, station: 'WeatherStation'):
        print("Текущие условия:")
        print(f"Температура: {station.temperature}°C")
        print(f"Влажность:   {station.humidity}%")
        print(f"Давление:    {station.pressure} гПа\n")


class StatisticsDisplay(Observer):
    def __init__(self):
        self._count = 0

    def update(self, station: 'WeatherStation'):
        self._count += 1
        print("Статистика обновлений:")
        print(f"Количество обновлений: {self._count}")
        print(f"Текущая температура:   {station.temperature}°C\n")


class ForecastDisplay(Observer):
    def update(self, station: 'WeatherStation'):
        trend = "потепление" if station.temperature > 20 else "похолодание"
        print("Прогноз:")
        print(f"  Тенденция: {trend}")
        print(f"  Ожидаемая влажность: ~{station.humidity}%\n")


#Субъект(Subject) — погодная станция
class WeatherStation:
    def __init__(self):
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
        self._observers = []

    # Подписать наблюдателя
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    # Отписать наблюдателя (возможность отписки)
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    # Уведомить всех наблюдателей
    def notify(self):
        for observer in self._observers:
            observer.update(self)

    # Изменение данных погоды
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()  # Автоматически обновляем всех подписчиков


if __name__ == "__main__":
    station = WeatherStation()

    current_display = CurrentConditionDisplay()
    stats_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()

    # Подписываем наблюдателей
    station.attach(current_display)
    station.attach(stats_display)
    station.attach(forecast_display)

    print("Первое обновление")
    station.set_measurements(23.5, 65.0, 1013.2)

    print("Второе обновление")
    station.set_measurements(19.0, 75.0, 1008.5)

    # Демонстрация отписки
    print("Отписываем")
    station.detach(stats_display)

    print("Третье обновление")
    station.set_measurements(21.0, 70.0, 1010.0)
