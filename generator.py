from dotenv import load_dotenv
from yaml import safe_load
import os


def generate(base: str, arguments: dict):
    subcommand = False
    for argument in arguments:
        if 'command' in argument:
            subcommand = True
            child = argument.get('arguments', {})
            yield from generate(base + '_' + argument['command'], child)
    if not subcommand:
        yield base


def main():
    load_dotenv()
    with open(os.environ['CLI_CONFIG'], 'r') as stream:
        config = safe_load(stream)
    with open(f'handlers/_example.py', 'r') as stream:
        example = stream.readlines()
    for file in generate('', config):
        try:
            with open(f'handlers/{file}.py', 'x') as stream:
                stream.writelines(example)
        except FileExistsError as error:
            pass


if __name__ == '__main__':
    main()
