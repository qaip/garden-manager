from .weather import Weather
from .plant import Plant, Vegetable, Weed


class GardenBed:
    __plants: list[Plant]
    __life_factor: int
    __size: int

    def weed(self):
        self.__plants = [
            plant for plant in self.__plants if not isinstance(plant, Weed)]

    def water(self):
        self.__life_factor += 10

    def harvest(self):
        fruits: list[Vegetable.Fruit] = []
        for plant in self.__plants:
            if isinstance(plant, Vegetable):
                fruits += plant.get_fruits()
        return fruits

    def seed(self, name: str, count: int):
        self.__plants += [Vegetable(name) for i in range(count)]

    def clear(self):
        self.__plants.clear()


class Garden:
    beds: list[GardenBed]
    weather: Weather
