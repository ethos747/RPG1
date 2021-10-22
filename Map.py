# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 10/20/2021
# Name: Ethan Behl
# Description: Text-based RPG Map
# Imports
from tabulate import tabulate

# Descriptions of possible room types
map_rooms = {
    "Start": {"description": "Moon Dark Club entrance",
              "abbreviation": "S",
              "actions": "Interact with door"},
    "Search Location": {"description": """no enemies,
up to 3 searchable items/objects""",
                        "abbreviation": "SL",
                        "actions": "Interact with doors, optional searching"},
    "Enemy tile": {"description": """Up to three enemies,
up to 2 searchable items/objects""",
                   "abbreviation": "ET",
                   "actions": """Fight zombies, interact with doors,
optional searching"""},
    "Enemy tile(advanced)": {"description": """Up to 3 enemies(different types),
up to 3 searchable items/objects""",
                             "abbreviation": "ET(A)",
                             "action": """may pick up items or move
to another location"""},
    "Search Location(advanced)": {"description": """no enemies, pick up more
valuable items""",
                                  "abbreviation": "SL(A)",
                                  "actions": """Interact with doors, optional
searching"""}}
# Room type array
array_map = [
    [" ", " ", " ", "SL", "SL"],
    ["SL", "SL", "SL", "SL", "ET(A)", "SL"],
    [" ", "SL", " ", "SL", "ET"],
    ["ET(A)", "ET", "SL", "SL", "S"]
]


def map_room_list():
    """prints map room dictionary neatly"""
    for room in map_rooms:
        print(f"{room}: ")
        for description in map_rooms[room]:
            print(f"{description} - {map_rooms[room][description]}")


def view_array():
    """prints room types in an organized array"""
    print(tabulate(array_map, tablefmt='plain'))


def view_map():
    """prints the map the player sees"""
    print("""
                            First Floor
 ______________________Entrance____ _Client Rooms________________________
|              |1    Locker Rooms   2| 1  | 2  |                        S|
|              |_________    ________|    |    |         Dance         |t|
|              |                     | |__| |__|         Floor         |a|
|              |                     |  ________                       |i|
|    Garage    |        Front        |         |__________________  ___|r|
|              |       Entance       |         |       |_  ____________|s|
|              |                     |                  |    Storage    |
|              |                     |      Lounge      |_______________|
|                                                        _______________Car
|_______________________________________________________|    Allyway
""")
