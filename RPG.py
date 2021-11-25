# Course: CS 30
# Period: 3
# Date created: 9/15/2021
# Date last modified: 11/25/2021
# Name: Ethan Behl
# Description: Text-based RPG main code area
# imports, game quits if imports are imported incorrectly
try:
    import sys
    import Map
    import Character_selection
    import Inventory
    import Player
    import Combat
except ModuleNotFoundError:
    print("Error, a module was imported incorrectly on RPG.")
    print("Game ended.")
    sys.exit()
print("""
N O T  A L O N E


A mini survival-horror by Ethan Behl""")
# Other file operations
print(Map.allyway.description_1)
Character_selection.char_select_menu()

# The list of things a player can do;
menu_list = ("""
[1] Explore
[2] Inventory
[3] Status
[4] Map
[5] Quit""")
# Loops the menu
while True:
    menuu = str(input("\n" + menu_list + "\n"))
    # Various options based on the response
    if menuu == "1":
        # Explore option that lists rooms in various ways
        Player.explore()
    elif menuu == "2":
        # Inventory operations
        Inventory.inventory_input()
    elif menuu == "3":
        # Shows current statis of the player health and ammo-wise
        print("Current Health:" + str(Player.health) + "%")
        print("Pistol Ammo:" + str(Player.pistol_ammo))
    # Exits the game
    elif menuu == "4":
        Map.view_map()
        print("Current room:" + Player.current_room)
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
