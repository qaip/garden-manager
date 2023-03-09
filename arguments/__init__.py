from argparse import ArgumentParser, Namespace
from dotenv import load_dotenv
from yaml import safe_load
from pydoc import locate
import os


args: Namespace = None  # type: ignore


def parse(parser: ArgumentParser, rules: list, dest='command') -> None:
    subparsers = None
    for argument in rules:
        if 'command' in argument:
            if not subparsers:
                subparsers = parser.add_subparsers(
                    title='commands', dest=dest, required=argument.get('required', False))
            parser = subparsers.add_parser(
                argument['command'], help=argument.get('help', ''), allow_abbrev=False)
            if 'arguments' in argument:
                parse(parser, argument['arguments'], argument['command'])
        else:
            option = argument.pop('option')
            if 'type' in argument:
                argument['type'] = locate(argument.pop('type', 'bool'))
            parser.add_argument(*option,    **argument)  # type: ignore


def __init__() -> None:
    parser = ArgumentParser(
        description='Manage your virtual garden using CLI', prog='garden', allow_abbrev=False)
    with open(os.environ['CLI_CONFIG'], 'r') as stream:
        parse(parser, safe_load(stream))
    global args
    args = parser.parse_args()


if args == None:
    load_dotenv()
    __init__()

__all__ = ['args']
