from abc import abstractmethod
from importlib import import_module
from garden.base import Garden
from garden.weather import Weather
from .messages import Template


class BaseHandler:
    def __init__(self, args: dict) -> None:
        path = 'handlers.'
        level = 'command'
        while level := args.get(level):
            path += '_' + level
        BaseHandler._args = args
        import_module(path).Handler()

    @abstractmethod
    def perform(self):
        pass

    @classmethod
    def get_current_garden(cls):
        if hasattr(cls, 'current_garden'):
            return cls.current_garden
        try:
            with open('.currentgarden', 'r') as stream:
                cls.current_garden = stream.readline()
                return cls.current_garden
        except FileNotFoundError:
            raise FileNotFoundError(
                Template.NO_ACTIVE_GARDEN.value) from None
