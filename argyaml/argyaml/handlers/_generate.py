from argyaml import BaseHandler
from yaml import safe_load
import os


class Handler(BaseHandler.meta('Default')):
    def __init__(self):
        print('Hello from default generate')
        config_path = self.args.get('config', None)
        if not config_path:
            config_path = 'cli-config.yml'
        config = BaseHandler._load_config(config_path)
        rules = config.get('next', [])
        handler_name = self.args.get('name', None)
        handler_meta = f".meta('{handler_name}')" if handler_name else ''
        handlers_dir = self.args.get('dir', 'handlers')
        for file in self.__get_handlers('', rules):
            if not file:
                continue
            try:
                if not os.path.exists(handlers_dir):
                    os.makedirs(handlers_dir)
                flag = 'w' if self.args.get('force', False) else 'x'
                with open(f'{handlers_dir}/{file}.py',
                          flag, encoding='UTF-8') as stream:
                    stream.writelines(
                        f"class Handler(BaseHandler{handler_meta}):\n"
                        f"    def __init__(self):\n"
                        f"        pass\n")
            except FileExistsError:
                pass

    def __get_handlers(self, base: str, rules: list):
        subcommand = False
        for rule in rules:
            if 'command' in rule:
                subcommand = True
                subrules = rule.get('next', [])
                yield from self.__get_handlers(
                    base + '_' + rule['command'], subrules)
        if not subcommand:
            yield base
