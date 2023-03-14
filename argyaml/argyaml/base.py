from argparse import ArgumentParser
from importlib import import_module
from pydoc import locate
from yaml import YAMLError, safe_load


class BaseHandler():
    """
    Root parser and handler of arguments.
    """

    def __init__(self,
                 name='Default',
                 args: list[str] | None = None,
                 config_path: str | None = None,
                 handlers_dir='handlers') -> None:
        self.__name = name
        self.__handlers_dir = handlers_dir
        self.__register_name()
        config = self._load_config(config_path)
        default = config.pop('default', {})
        self.__default_group = default.get('group', {})
        self.__default_command = default.get('command', {})
        self.__default_argument = default.get('argument', {})
        self._args = self.__parse(config, args)

    @classmethod
    def meta(cls, name='Default'):
        if (not hasattr(BaseHandler, '_meta')) or (name not in cls._meta):
            raise ValueError(f"BaseHandler with name '{name}' is not defined (${cls._meta.get(name)})")
        args = cls._meta[name]._args

        class CustomHandler:
            @property
            def args(self):
                return args
        return CustomHandler

    def __register_name(self) -> None:
        if not hasattr(BaseHandler, '_meta'):
            BaseHandler._meta: dict[str, BaseHandler] = {}
        if self.__name in BaseHandler._meta:
            raise ValueError(
                f"BaseHandler with name '{self.__name}' is already defined")
        BaseHandler._meta[self.__name] = self

    @staticmethod
    def _load_config(config_path: str | None) -> dict:
        if config_path is None:
            config_path = 'cli-config.yml'
        with open(config_path, 'r', encoding='UTF-8') as stream:
            try:
                config = safe_load(stream)
                if config is None:
                    raise TypeError(f"Config '{config_path}' cannot be empty")
                if not isinstance(config, dict):
                    raise TypeError(
                        f"Invalid config '{config_path}': " +
                        f"{dict} expected, but {type(config)} found")
                return config
            except YAMLError as error:
                print(error)
                exit(1)

    def __parse(self, config: dict, args: list[str] | None) -> dict:
        group = config.pop('group', {})
        rules = config.pop('next', [])
        parser = ArgumentParser(**config)
        self.__next(parser, rules, group)
        namespace = parser.parse_args(args)
        return vars(namespace)

    def __next(self,
               parser: ArgumentParser,
               rules: list[dict],
               group: dict[str, str],
               dest: str | None = None) -> None:
        subparsers = None
        for rule in rules:
            if 'command' in rule:
                if subparsers is None:
                    if dest is None:
                        dest = self.__default_group.get('command', 'command')
                    subparsers = parser.add_subparsers(dest=dest, **group)
                command = rule.pop('command')
                new_next = rule.pop('next', None)
                new_group = rule.pop('group', {})
                new_parser = subparsers.add_parser(
                    command, **self.__default_command, **rule)
                if new_next is not None:
                    self.__next(new_parser, new_next, new_group)
            elif 'argument' in rule:
                argument = rule.pop('argument')
                if 'type' in rule:
                    rule['type'] = locate(rule.pop('type', 'bool'))
                parser.add_argument(
                    *argument, **self.__default_argument, **rule)
            else:
                raise ValueError(f"Invalid rule: {rule}")

    def __get_path(self, handlers_dir: str) -> str:
        path = handlers_dir + '.'
        level = 'command'
        while level := self._args.get(level):
            path += '_' + level
        return path

    def run(self):
        """
        Run the handler.
        """
        path = self.__get_path(self.__handlers_dir)
        import_module(path).Handler()

    @property
    def args(self) -> dict:
        """
        Get the arguments.
        """
        return self._args
