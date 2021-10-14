# Course: CS 30
# Period: 3
# Date created: 9/15/2021
# Date last modified: 10/14/2021
# Name: Ethan Behl
# Description: Text-based RPG
# imports the system function allowing the "quit" option.
import sys

# Introduction to the game,menu and what to input
print("Welcome! To perform an action, select the number between the brackets.")
print("This is a challenging game. Retry If you need.")
# Begins the game that is followed by flavour text
input(str("Continue [any key]"))
print("""It's 2:35 in the morning.
You, a police officer, pull up your car to an allyway near a nightclub.
After recieving a distress call from the near nightclub,
the station hit you up with the task of investigating the call.
You get out of the car and stare at the bright neon sign illuminating the ally.
"Moon Dark club"
You stare down at your badge.
""")
# Dictionary of the available characters
character_select = {
    "Officer Ornell": {"description": "Nick name:'Lucky'",
                       "bonus": """Increased chance to find items
when searching"""},
    "Deputy Bernard": {"description": "Big boy Bernard will mess you up",
                       "bonus": "Takes less damage from all sources"}}


def char_select_menu():
    """Allows the player to select their character using the dictionary"""
    for people in character_select:
        print(f"{people}: ")
        for item in character_select[people]:
                print(f"{item} - {character_select[people][item]}")
    # Input for the player to choose their character with apropriate text
    character_input = str(input("""Who are you?
[1] Officer Ornell
[2] Deputy Bernard"""))
    if character_input == "1":
        print("You are playing as Officer Ornell")
        character_select.pop("Deputy Bernard")
    elif character_input == "2":
        print("You are playing as Deputy Bernard")
        character_select.pop("Officer Ornell")
    else:
        char_select_menu()


# Enables the character menu
char_select_menu()


# Organization of lists
def nLists(lists):
    """Attatches numbers to each item for a list"""
    for item in lists:
        print(f"[{lists.index(item)+1}] {item}")


# Starting inventory and stats
Items = ["First aid kit"]
Weapons = ["9mm Pistol", "Knife"]
health = 80
pistol_ammo = 75
kits = 1
# List of possible map tiles
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
# The list of things a player can do;
menu_list = ("""[1] Interact
[2] Explore
[3] Inventory
[4] Status
[5] Quit""")
# Loops the menu
while True:
    menuu = str(input(menu_list))
    # Various options based on the response
    if menuu == "1":
        # Interact options menu for the current room example
        room_1 = ("Light Switch [1]", "Closet[2]")
        room_1_in = str(input(room_1))
        if room_1_in == "1":
            print("You flick on the light switch but the bulb is broken!")
        elif room_1_in == "2":
            print("You found nothing")
        else:
            print ("Please choose an available option")
    elif menuu == "2":
        # Explore option that lists all available rooms neatly
        for room in map_rooms:
            print(f"{room}: ")
            for description in map_rooms[room]:
                    print(f"{description} - {map_rooms[room][description]}")
    elif menuu == "3":
        # Inventory inspect options
        inv_input = str(input("""What do you want to look at?
[1] Items
[2] Weapons"""))
        # Item section display
        if inv_input == "1":
            print("Available Items:")
            nLists(Items)
            # Item section selection
            inv_input_items = str(input("Which do you inspect?"))
            # Health kit selection, with and additional option to use it
            if inv_input_items == "1":
                print("You can use this to heal 20% health.")
                print("You have " + str(kits) + " remaining")
                if kits == 0:
                    print("You did not use a first aid kit.")
                else:
                    kit_input = input("""Would you like to use it?
[1] Yes
[2] No""")
                # Adjusts to number of health kits and increases health if used
                    if kit_input == "1":
                        kits -= 1
                        health += 20
                        print("You used a first aid kit and healed to:")
                        print(str(health) + "%")
                    else:
                        print("You did not use the first aid kit")
        # Weapon slection list
        if inv_input == "2":
            print("Available Weapons")
            nLists(Weapons)
            inv_input_weapons = str(input("Which do you view?"))
            # Shows weapon and description out of combat, "view" only
            if inv_input_weapons == "1":
                print("Combat knife usable in a variety of situations.")
                print("Hit chance: 50%")
            elif inv_input_weapons == "1":
                print("Standard issue 9mm pistol.")
                print("Hit chance:90%")
            else:
                print ("Please choose an available option")
        else:
            print ("Please choose an available option")
    # Shows current statis of the player health and ammo-wise
    elif menuu == "4":
        print("Current Health:" + str(health) + "%")
        print("Pistol Ammo:" + str(pistol_ammo) + "%")
    # Exits the game
    elif menuu == "5":
        # Option for player to quit
        quit_input = str(input("""Are you sure?
[1] Yes
[2] No"""))
        if quit_input == "1":
            print("Game ended.")
            sys.exit()
        else:
            print("You did not quit.")
    # Message for if the player choses a non-available option
    else:
        print ("Please choose an available option")
