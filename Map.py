# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 11/25/2021
# Name: Ethan Behl
# Description: Text-based RPG Map
# Imports, game quits if imports are imported incorrectly
try:
    import sys
except ModuleNotFoundError:
    print("Error, a module was imported incorrectly in Map.")
    print("Game ended.")
    sys.exit()


# All map classes
class MapTile:
    def __init__(self, description_1, description_2, ):
        self.description_1 = description_1
        self.description_2 = description_2


class SearchLocation:
    def __init__(self, description_1, description_2, pickup_1, pickup_2):
        self.description_1 = description_1
        self.description_2 = description_2
        self.pickup_1 = pickup_1
        self.pickup_2 = pickup_2


class EnemyTile:
    def __init__(self, description_1, description_2, pickup_1, pickup_2, fight):
        self.description_1 = description_1
        self.description_2 = description_2
        self.pickup_1 = pickup_1
        self.pickup_2 = pickup_2
        self.fight = fight


class ConnectTile:
    def __init__(self, description_1, description_2, pickup_1, locked_1, locked_2):
        self.description_1 = description_1
        self.description_2 = description_2
        self.pickup_1 = pickup_1
        self.locked_1 = locked_1
        self.locked_2 = locked_2


class FinalTile:
    def __init__(self, fight, end_fight):
        self.fight = fight
        self.end_fight = end_fight


# Text for the various rooms
allyway = MapTile("""
It's 2:35 in the morning.
You, a police officer, pull up your car to an allyway near a nightclub.
After recieving a distress call from the nearby nightclub,
the station hit you up with the task of investigating the call.
You get out of the car and stare at the neon sign illuminating the ally.
"Moon Dark club"
You stare down at your badge.
""", """
There is a door to the back of the club.
[1] Enter the door""")
lounge = SearchLocation("""
You enter the club,finding yourself in a dimly lit lounge.
After closing the door, you have a look around.
Comfy black couches and small lamps litter the room. It is quiet.
You hear a scream coming from the front entrance.
""", """
LOUNGE
Items of interest:

[1] Drawer
[2] Cabinet

Available rooms:

[3] Hallway to Client Rooms and Dance Floor
[4] Front entrance
""", "You find some pistol ammo!", "Nothing but magazines.")
front_entrance = SearchLocation("""
You walk into the front entrance.
The room has collapsed. There is nothing to find here.
The doors outside are bent, unable to open due to the collapse.
If you can find another way around,
you might be able to explore the rest of this room.
There is a streak of blood leading to the Garage.""", """
FRONT ENTRANCE
Available rooms:
[1] Garage
[2] Lounge""", None, None)
Hall = ConnectTile("""
You are now in a hallway leading to two client rooms.
Beside these rooms is the door to the main dance floor.
Loud, blaring dubstep can be heard from behind the door.
Looking around the room, there is a few chairs and a table in a similar format to the lounge.""", """
HALL
Items of interest:
[1] Table

Available rooms:
[2] Client Room 1
[3] Client Room 2
[4] Dance Floor
[5] Lounge
""", "You find some pistol ammo!", "The door to Client Room 1 is locked.", """
The door to the Dance Floor is locked.""")
client_room_1 = SearchLocation("""
This room is inverted when compared to client room 2.
There is a couch, but it is torn up and covered with blood.
""", """
CLIENT ROOM 1
Items of interest:
[1] Couch 

Available rooms:
[2] Hall""", "You find a grenade within the cushions.", None)
client_room_2 = SearchLocation("""
You now stand in a small room, shadded in low red light.
A nice, comfy and wide couch is found infront of you.
""", """
CLIENT ROOM 2
Items of interest:
[1] Couch 

Available rooms:
[2] Hall""", "There is nothing in this couch but change and dust.", None)
Garage = EnemyTile("""
There is a long streak of blood that trails towards the back of the garage.
Expensive-looking cars line the left of the garage.""", """
GARAGE
Items of interest:
[1] Counter
[2] Tool Storage Cart

Available rooms:
[3] Front Entrance
[4] Locker Room 1""", "You find some pistol ammo.", "You found a health kit", """
Knealt down in front of you is a ragged person,
knawing on the corpse of another.
It slowly turns around, teeth bare and snarling.""")
Locker_1 = SearchLocation("""
Dead bodies are lined across the floor. 
One of them looks like it twitches.""", """
LOCKER ROOM 1
Items of interest:
[1] Locker (102)
[2] Locker (104)

Available rooms:
[3] Locker Room 2
[4] Garage""", "The locker is empty.", "You found some pistol ammo!")
Locker_2 = EnemyTile("""
Similar to locker room 1, multiple dead bodies lie mutilated.""", """
LOCKER ROOM 2
Items of interest:
[1] Locker (203)

Available rooms:
[2] Locker Room 1""", "You find a key.", None, """
The corpses begin to rise from the floor.""")
Dance_Floor = EnemyTile("""
Dozens of bodies lie around, dead.
Whatever happened must have been during a rave.
You can barly hear.
To the side of the dance floor is a bar, broken glass all around.
There is a door to storage.""", """
DANCE FLOOR
Items of interest:
[1] Bar

Available rooms:
[2] Hall
[3] Storage""", "Nothing but drinks and broken glass.", None, None)
Storage = FinalTile("""
The room is completely silent.
You look towards the ground, noticing streams of bloody mass
moving deeper into the room.
The streams of blood are from the bodies in the dance floor.
The mass begins forming into a vile figure infront of you.
A large zombie formed of the victim's flesh bares it's teeth.""", """
The monsterous zombie begins to disintegrate.
Flesh falls off from the zombie to the floor.
Your radio is now no longer blocked. Did the zombies interfere somehow?
You call for help to the station.
Your getting out of here.
""")


def map_room_list():
    """prints map room dictionary neatly"""
    for room in map_rooms:
        print(f"{room}: ")
        for description in map_rooms[room]:
            print(f"{description} - {map_rooms[room][description]}")


def view_map():
    """prints the map the player sees"""
    print("""
 ____________________________________Client Rooms______________________
|              |1    Locker Rooms   2| 1  | 2  |                       |
|              |_________    ________|    |    |         Dance         |
|              |                     | |__| |__|         Floor         |
|              |                     |   Hall                          |
|    Garage    |        Front        |  _______|_______                |
|              |        Lobby        |         |       |_  ____________|
|              |                     |                  |    Storage   |
|              |                     |      Lounge      |______________|
|                                                        ______________ Car
|___________________Front Entrance______________________|    Allyway
""")
