from abc import ABC, abstractmethod


#Cторонний сервис
class ThirdPartyWeatherService:
    def GetTemperatureFahrenheit(self, city: str) -> float:
        # Имитация данных из внешнего API
        data = {
            "Москва": 68.0,
            "Самара": 59.0,
            "Ульяновск": 75.2
        }
        return data.get(city, 65.0)


#Интерфейс нашего приложения
class IWeatherProvider(ABC):
    @abstractmethod
    def GetTemperatureCelsius(self, city: str) -> float:
        pass


#Адаптер
class WeatherAdapter(IWeatherProvider):
    def __init__(self, third_party_service: ThirdPartyWeatherService):
        self._service = third_party_service

    def GetTemperatureCelsius(self, city: str) -> float:
        fahrenheit = self._service.GetTemperatureFahrenheit(city)
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius


# 4. Главная функция (для одного города)
def main():
    #Создаём адаптер
    adapter = WeatherAdapter(ThirdPartyWeatherService())

    #Получаем температуру для одного города
    city = "Самара"
    temp = adapter.GetTemperatureCelsius(city)

    print(f"Температура в {city}: {temp}°C")


if __name__ == "__main__":
    main()