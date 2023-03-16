from argyaml import BaseHandler
from database.session import make_session
from handlers.messages import Template
from sqlalchemy.orm import Session


class GardenHandler(BaseHandler.meta()):
    def __init__(self):
        super(GardenHandler, self).__init__()

    __current_garden: str | None = None
    __session: Session | None = None

    @property
    def db(self):
        if not self.__session:
            self.__session = make_session()
        return self.__session

    @property
    def current_garden(self):
        if not self.__current_garden:
            try:
                with open('.currentgarden', 'r', encoding='UTF-8') as stream:
                    self.__current_garden = stream.readline()
            except FileNotFoundError:
                raise FileNotFoundError(
                    Template.NO_ACTIVE_GARDEN.value) from None
        return self.__current_garden
    

    def __del__(self):
        if self.__session:
            self.__session.close()
