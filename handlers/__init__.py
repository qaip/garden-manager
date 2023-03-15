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
