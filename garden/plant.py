from abc import ABC, abstractmethod
from enum import Enum


class Plant(ABC):
    @abstractmethod
    def __init__(self, name: str) -> None:
        self.register_name(name, self.__class__.__name__)
        self.__name = name
        self.__stage = 0

    @classmethod
    def register_name(cls, name: str, type: str) -> None:
        if not hasattr(cls, 'types'):
            cls.types: dict[str, str] = {}
        defined_type = cls.types.get(name)
        if defined_type is None:
            cls.types[name] = type
        elif defined_type != type:
            raise ValueError(
                f"Plant '{name}' is already defined as '{defined_type}'")

    class Stage(Enum):
        SEED = 0
        SPROUT = 40
        SMALL_PLANT = 60
        ADULT_PLANT = 80

    @property
    def name(self):
        return self.__name

    @property
    def stage(self):
        if (self.__stage >= Plant.Stage.ADULT_PLANT.value):
            return Plant.Stage.ADULT_PLANT
        elif (self.__stage >= Plant.Stage.SMALL_PLANT.value):
            return Plant.Stage.SMALL_PLANT
        elif (self.__stage >= Plant.Stage.SPROUT.value):
            return Plant.Stage.SPROUT
        else:
            return Plant.Stage.SEED

    def grow(self):
        self.__stage += 10


class Vegetable(Plant):
    class Fruit:
        def __init__(self, name: str) -> None:
            self.__name = name

    __fruits: list[Fruit] = []

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def grow(self):
        super().grow()
        # if self.stage == Plant.Stage.ADULT_PLANT:
        # self.__fruits += 1

    @property
    def number_of_fruits(self):
        return len(self.__fruits)

    def get_fruits(self):
        fruits = self.__fruits.copy()
        self.__fruits.clear()
        return fruits


class Weed(Plant):
    def __init__(self, name: str) -> None:
        super().__init__(name)
