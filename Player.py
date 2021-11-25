# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 11/25/2021
# Name: Ethan Behl
# Description: Text-based RPG Character Selection
# Controls player movement, location and interaction
try:
    import Map
    import Combat
    import Inventory
    import sys
except ModuleNotFoundError:
    print("Error, a module was imported incorrectly on Player.")
    print("Game ended.")
    sys.exit()

# Variables that help control events
current_room = "allyway"
health = 100
pistol_ammo = 10
health_kits = 1
Garage_search = 1
Garage_fight = 1
lounge_search = 1
Garage_clear_search = 1
Locker_1_search = 1
Hall_search = 1
Locker_2_fight = 1
Key = False
Dance_Floor_fight = 1
Grenade = 0
Locker_2_search = 1
client_room_1_search = 1


def searched():
    """Search text"""
    print("You have already searched this. There is nothing left.")


def locked_unlocked():
    """Locked text"""
    print("The door is locked.")
    print("You unlock the door using the LOCKER KEY.")


def explore():
    """Controls the player movement and interaction"""
    global current_room
    global health
    global pistol_ammo
    global lounge_search
    global Garage_search
    global Locker_1_search
    global Garage_fight
    global Hall_search
    global Locker_2_fight
    global Garage_clear_search
    global health_kits
    global Key
    global Dance_Floor_fight
    global Grenade
    global Locker_2_search
    global client_room_1_search
    if current_room == "allyway":
        room_in = input(Map.allyway.description_2)
        if room_in == "1":
            print(Map.lounge.description_1)
            current_room = "Lounge"
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Lounge":
        room_in = input(Map.lounge.description_2)
        if room_in == "1":
            if lounge_search == 1:
                print(Map.lounge.pickup_1)
                pistol_ammo += 2
                lounge_search -= 1
            elif lounge_search == 0:
                searched()
        elif room_in == "2":
            print(Map.lounge.pickup_2)
        elif room_in == "3":
            current_room = "Hall"
            print(Map.Hall.description_1)
        elif room_in == "4":
            print(Map.front_entrance.description_1)
            current_room = "Front Entrance"
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Front Entrance":
        room_in = input(Map.front_entrance.description_2)
        if room_in == "1":
            current_room = "Garage"
            print(Map.Garage.description_1)
        elif room_in == "2":
            current_room = "Lounge"
            print(Map.lounge.description_1)
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Hall":
        room_in = input(Map.Hall.description_2)
        if room_in == "1":
            if Hall_search == 1:
                print(Map.Hall.pickup_1)
                pistol_ammo += 2
                Hall_search -= 1
            elif Hall_search == 0:
                searched()
        elif room_in == "2":
            if Key == True:
                current_room = "Client Room 1"
                print(Map.client_room_1.description_1)
            else:
                print(Map.Hall.locked_1)
        elif room_in == "3":
            current_room = "Client Room 2"
            print(Map.client_room_2.description_1)
        elif room_in == "4":
            if Key == True:
                current_room = "Dance Floor"
                print(Map.Dance_Floor.description_1)
            else:
                print(Map.Hall.locked_2)
        elif room_in == "5":
            current_room = "Lounge"
            print(Map.lounge.description_1)
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Client Room 2":
        room_in = input(Map.client_room_2.description_2)
        if room_in == "1":
            print(Map.client_room_2.pickup_1)
        elif room_in == "2":
            current_room = "Hall"
            print(Map.Hall.description_1)
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Client Room 1":
        room_in = input(Map.client_room_1.description_2)
        if room_in == "1":
            if client_room_1_search == 1:
                print(Map.client_room_1.pickup_1)
                Grenade += 1
                client_room_1_search -= 1
                Inventory.Items.append("Grenade")
            else:
                print("The couch is empty.")
        elif room_in == "2":
            current_room = "Hall"
            print(Map.Hall.description_1)
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Garage":
        if Garage_fight == 1:
            Garage_fight -= 1
            print(Map.Garage.fight)
            Combat.player_combat()
        else:
            room_in = input(Map.Garage.description_2)
            if room_in == "1":
                if Garage_search == 1:
                    print(Map.Garage.pickup_1)
                    pistol_ammo += 2
                    Garage_search -= 1
                elif Garage_search == 0:
                    searched()
            elif room_in == "2":
                if Garage_clear_search == 1:
                    print(Map.Garage.pickup_2)
                    health_kits += 1
                    Garage_clear_search -= 1
                elif Garage_clear_search == 0:
                    searched()
            elif room_in == "3":
                current_room = "Front Entrance"
                print(Map.front_entrance.description_1)
            elif room_in == "4":
                current_room = "Locker Room 1"
                print(Map.Locker_1.description_1)
            else:
                print ("\nPlease choose an available option")
    elif current_room == "Locker Room 1":
        room_in = input(Map.Locker_1.description_2)
        if room_in == "1":
            print(Map.Locker_1.pickup_1)
        elif room_in == "2":
            if Locker_1_search == 1:
                print(Map.Locker_1.pickup_2)
                pistol_ammo += 2
                Locker_1_search -= 1
            elif Locker_1_search == 0:
                searched()
        elif room_in == "3":
            current_room = "Locker Room 2"
            print(Map.Locker_2.description_1)
        elif room_in == "4":
            current_room = "Garage"
            print(Map.Garage.description_1)
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Locker Room 2":
        if Locker_2_fight == 1:
            Locker_2_fight -= 1
            print(Map.Locker_2.fight)
            Combat.player_combat()
        room_in = input(Map.Locker_2.description_2)
        if room_in == "1":
            if Locker_2_search == 1:
                print(Map.Locker_2.pickup_1)
                Inventory.Items.append("Key")
                Key = True
                Locker_2_search -= 1
            else:
                print("It is now empty")
        elif room_in == "2":
            current_room = "Locker Room 1"
            print(Map.Locker_1.description_1)
        else:
            print ("\nPlease choose an available option")
    elif current_room == "Dance Floor":
        if Dance_Floor_fight == 1:
            Dance_Floor_fight -= 1
            print(Map.Dance_Floor.fight)
            Combat.player_combat()
        room_in = input(Map.Dance_Floor.description_2)
        if room_in == "1":
            print(Map.Dance_Floor.pickup_1)
        elif room_in == "2":
            current_room = "Hall"
            print(Map.Hall.description_1)
        elif room_in == "3":
            current_room = "Storage"
            print(Map.Storage.fight)
            Combat.player_combat()
            print(Map.Storage.end_fight)
            print("YOU SURVIVED")
            print("Game ended.")
            sys.exit()
        else:
            print ("\nPlease choose an available option")
