# Garden Manager
Garden Manager is an advanced tool for __modeling__, __storing__, and __managing__ __virtual gardens__ using command-line interface built with [argyaml](https://github.com/qaip/argyaml).

### Features
- Creating multiple gardens.
- Creating multiple garden beds of a fixed capacity within a selected garden.
- Seeding garden beds with plants of different types.
- Viewing the list of available gardens.
- Viewing full information about garden beds and growing plants.
- Navigating between gardens.
- Watering garden beds (regular and intensive).
- Harvesting from individual beds or the entire garden.


## Installation
Before stepping forward, make sure you have [poetry](https://python-poetry.org) and [docker compose](https://docs.docker.com/compose/install) installed.

Clone repository:
```bash
git clone https://github.com/qaip/garden.git
cd garden
```


Run the database:
```bash
docker-compose up
```

Create an alias for running the application in a convenient way (optional):
```bash
alias garden='poetry run garden'
```

## Usage

### Getting started
Being built with argyaml, Garden Manager has complete validation and help information about all available commands and arguments.
```bash
garden --help
# usage: garden [-h] {create,delete,use,new,seed,list,water,harvest} ...
# 
# options:
#   -h, --help            show this help message and exit
# 
# commands:
#   {create,delete,use,new,seed,list,water,harvest}
#     create              create a new garden
#     delete              delete a garden
#     use                 select a garden to work with
#     new                 create a new garden object
#     seed                seed a garden bed with plants
#     list                list available gardens or garden objects
#     water               water a garden bed
#     harvest             harvest from a garden bed
```

Type `--help` after any command to see detailed information and available options.
```bash
garden create --help
# usage: garden create [-h] [--use] name
# 
# positional arguments:
#   name        the name of garden
# 
# options:
#   -h, --help  show this help message and exit
#   --use       automatically switch to the new garden after creation
```


### Creating a garden
```bash
garden create carlos
# Created garden 'carlos'
```
Specify `--use` flag to automatically switch to the newly created garden:
```bash
garden create antonio --use
# Created garden 'antonio'
# Now using garden 'antonio'
```


### Listing available gardens
```bash
garden list
#   carlos
# * antonio
```


### Switching to another garden
```bash
garden use carlos
# Now using garden 'carlos'
```


### Deleting a garden
```bash
garden delete antonio
# Deleted garden 'antonio'
```
In case the garden is not empty and has some beds and plants in it, specify `--force` flag to confirm deletion:
```bash
garden delete antonio --force
# Deleted garden 'antonio' with all its contents
```


### Adding garden beds
```bash
garden new bed --size 30
# Created garden bed of size 30
```

```bash
garden new bed -s 20
# Created garden bed of size 20
```



### Seeding garden beds
```bash
garden seed --bed 1 --name carrot --count 14
# Seeded garden bed 1 with 14 carrots
```

```bash
garden seed -b 1 -n cabbage -c 5
# Seeded garden bed 1 with 5 cabbages
```


### Watering garden beds
```bash
garden water --bed 1
# Watered garden bed 1 (+10)
```
Use `--intensive` flag for intensive watering to make plants grow faster:
```bash
garden water --bed 1 --intensive
# Watered garden bed 1 (+20)
```


### Listing garden beds
```bash
garden list bed
#  Id    Size    Life Factor    Seeds    Spouts    Small Plants    Adult Plants
# ----  ------  -------------  -------  --------  --------------  --------------
#  1      30         100          0        19           2               0
#  2      30         100          6        7            0               24
#  3      30         100         22        4            0               0
```
Use `--details` flag to print all information about beds in details:
```bash
garden list bed --details
# Bed: 1 | size: 30 | seeded: 19 | life factor: 100
#  Id   Name      Stage
# ----  -------  -------
#  15   carrot     50
#  16   carrot     50
#  13   cabbage    30
#  17   carrot     50
# 
# Bed: 2 | size: 30 | seeded: 30 | life factor: 100
#  Id   Name     Stage
# ----  ------  -------
#  21   beet     90
#  79   tomato   20
#  80   tomato   20
#  91   beet     70
# 
# Bed: 3 | size: 30 | seeded: 26 | life factor: 100
#  Id   Name      Stage
# ----  -------  -------
#  97   garlic     30
#  14   beet        0
#  73   potato     40
#  74   potato     40
#  75   potato     40
```


### Harvesting
Harvest from a specific garden bed:
```bash
garden harvest --bed 1
# Harvested 4 carrots, 5 cabbages from garden bed 1
```
Harvest from the entire garden:
```bash
garden harvest --all
# Harvested 4 carrots, 5 cabbages, 1 beet from the whole garden
```
Harvest regardless of plant stage (by default only adult plants are harvested):
```bash
garden harvest --bed 1
# Harvested 6 carrots, 6 cabbages from garden bed 1
```
```bash
garden harvest --force
# Harvested 6 carrots, 7 cabbages, 3 beets, 4 potatoes from the whole garden
```



## Contributing
Feel free to open pull requests, any contribution is appreciated!


## License
This project is licensed under the [MIT License](https://github.com/qaip/garden/blob/LICENSE).
