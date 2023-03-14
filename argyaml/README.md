# Argyaml
Argyaml is a small module for creating _powerful_ and _scalable_ __CLI applications__ based on a _simple_ and _user-friendly_ yaml __configuration file__.

### Motivation
Argyaml is built over the [argparse](https://docs.python.org/3/library/argparse.html) module, which is a part of python standard library starting python 3.2. While it works well for tiny projects that need to quickly access a few arguments and provide automatically generated help and usage messages for user, it gets very complicated and painful when it comes to large projects or your application grows in complexity.

## Example
Imagine that you have several commands, each containing its own sub-commands that have their own set of arguments:
```
add city <name>
add building --city CITY_NAME

remove city <name> [--force]
remove building --id ID

list cities
list buildings --city CITY_NAME
```

A minimal implementation using __argparser__ would be the following:
```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add')
parser_remove = subparsers.add_parser('remove')
parser_list = subparsers.add_parser('list')

subparsers_add = parser_add.add_subparsers()
subparsers_remove = parser_remove.add_subparsers()
subparsers_list = parser_list.add_subparsers()

# 'add' sub-commands
parser_add_city = subparsers_add.add_parser('city')
parser_add_city.add_argument('name', type=str)

parser_add_building = subparsers_add.add_parser('building')
parser_add_building.add_argument('--city', type=str, dest='city_name')

# 'remove' sub-commands
parser_remove_city = subparsers_remove.add_parser('city')
parser_remove_city.add_argument('name', type=str)
parser_remove_city.add_argument('--force', action='store_true')

parser_remove_building = subparsers_remove.add_parser('building')
parser_remove_building.add_argument('--id', type=int)

# 'list' sub-commands
parser_list_cities = subparsers_list.add_parser('cities')

parser_list_buildings = subparsers_list.add_parser('buildings')
parser_list_buildings.add_argument('--city', type=str, dest='city_name')

# parse the arguments and transform to dict
parser.parse_args()
vars(parser.parse_args())
```

Lots of boilerplate code that is not easy to read.  Here is an equivanet using __argyaml__:

```yaml
# cli-config.yaml
next:
  - command: add
    next:
      - command: city
        next:
          - argument: ['name']
            type: str
      - command: building
        next:
          - argument: ['--city']
            dest: 'city_name'
            required: true
            type: str

  - command: remove
    next:
      - command: city
        next:
          - argument: ['name']
            type: str
          - argument: ['--force']
            action: store_true
      - command: building
        next:
          - argument: ['--id']
            required: true
            type: int

  - command: list
    next:
      - command: cities
      - command: buildings
        next:
          - argument: ['--city']
            dest: 'city_name'
            required: true
            type: str
```
```python
from argyaml import BaseHandler

base = BaseHandler()
base.args
```