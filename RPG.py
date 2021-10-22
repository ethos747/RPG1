# Course: CS 30
# Period: 3
# Date created: 9/15/2021
# Date last modified: 10/20/2021
# Name: Ethan Behl
# Description: Text-based RPG main code area
# imports
import sys
import Map
import Character_selection
import Text
import Inventory

# Other file operations
Text.text_intro()
Character_selection.char_select_menu()
# Starting stats
health = 80
pistol_ammo = 75
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
        # Explore option that lists rooms in various ways
        Map.map_room_list()
        Map.view_array()
        Map.view_map()
    elif menuu == "3":
        # Inventory operations
        Inventory.inventory_input()
    elif menuu == "4":
        # Shows current statis of the player health and ammo-wise
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
