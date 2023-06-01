from enum import Enum
from argyaml import BaseHandler
from database.session import make_session
from handlers.messages import Template
from sqlalchemy.orm import Session
from typing import Any


class GardenHandler():
    def __init__(self, server=False):
        # super(GardenHandler, self).__init__()
        self.__default = BaseHandler.meta()
        self.args: dict[str, Any] = self.__default.args()
        self.__server = server
        try:
            print('existing response?!', self.response)
        except:
            pass
        self.response = []

    def print(self, *kargs):
        if self.__server:
            self.response.append(kargs)
        else:
            print(*kargs)

    __current_garden: int | None = None
    __session: Session | None = None

    @property
    def db(self):
        if not self.__session:
            self.__session = make_session()
        return self.__session

    @property
    def safe_current_garden_id(self):
        if not self.__current_garden:
            try:
                with open('.currentgarden', 'r', encoding='UTF-8') as stream:
                    id_str = stream.read()
                    try:
                        self.__current_garden = int(id_str)
                    except ValueError:
                        self.__current_garden = None
            except FileNotFoundError:
                self.__current_garden = None
        return self.__current_garden

    @property
    def current_garden_id(self):
        if not self.safe_current_garden_id:
            print(Template.NO_ACTIVE_GARDEN.value)
            exit(1)
        return self.safe_current_garden_id

    def __del__(self):
        if self.__session:
            self.__session.close()

    class PlantStage(Enum):
        SEED = 0
        SPROUT = 40
        SMALL_PLANT = 60
        ADULT_PLANT = 80

    @classmethod
    def get_plant_stage(cls, stage: int) -> PlantStage:
        if (stage >= cls.PlantStage.ADULT_PLANT.value):
            return cls.PlantStage.ADULT_PLANT
        if (stage >= cls.PlantStage.SMALL_PLANT.value):
            return cls.PlantStage.SMALL_PLANT
        if (stage >= cls.PlantStage.SPROUT.value):
            return cls.PlantStage.SPROUT
        return cls.PlantStage.SEED
