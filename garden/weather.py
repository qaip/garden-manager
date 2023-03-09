from abc import ABC, abstractmethod


class Weather(ABC):
    @abstractmethod
    def __init__(self, temperature: int, humidity: int, wind: int) -> None:
        '''
        Construct a new Weather object.

        :param temperature: The air temperature in [°C]
        :param humidity: The humidity level in [%]
        :param wind: The wind speed in [m/s]
        :return: 
        '''
        self._humidity = humidity
        self._temperature = temperature
        self._wind = wind

    def humidity(self):
        return self._humidity

    def temperature(self):
        return self._temperature

    def wind(self):
        return self._wind


class Rainy(Weather):
    def __init__(self, temperature: int, wind: int, intensity: int) -> None:
        super().__init__(temperature=temperature, humidity=100, wind=wind)
        self._intensity = intensity

    def intensity(self):
        return self._intensity


class Sunny(Weather):
    def __init__(self, temperature: int, humidity: int, wind: int) -> None:
        super().__init__(temperature, humidity, wind)


class Drought(Sunny):
    def __init__(self, temperature: int) -> None:
        if (temperature < 0):
            raise ValueError('The temperature of drought cannot be negative')
        super().__init__(temperature=temperature, humidity=100, wind=0)
