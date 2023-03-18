from argyaml import BaseHandler
from database.session import make_session
from handlers.messages import Template
from sqlalchemy.orm import Session


class GardenHandler(BaseHandler.meta()):
    def __init__(self):
        super(GardenHandler, self).__init__()

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
