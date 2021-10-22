# Course: CS 30
# Period: 3
# Date created: 10/19/2021
# Date last modified: 10/20/2021
# Name: Ethan Behl
# Description: Text-based RPG Inventory


def nLists(lists):
    """Attatches numbers to each item for a list"""
    for item in lists:
        print(f"[{lists.index(item) + 1}] {item}")


# List of inventory items
Items = ["Knife", "9mm pistol", "First aid kit"]


def inventory_input():
    """Allows the player to select items in the inventoryt"""
    print("Available Items:")
    nLists(Items)
    inv_input = str(input("Which do you inspect?"))
    if inv_input == "2":
        print("Standard issue 9mm pistol.")
        print("Hit chance:90%")
    elif inv_input == "1":
        print("Combat knife usable in a variety of situations.")
        print("Hit chance: 50%")
    elif inv_input == "3":
        print("You can use this to heal 20% health.")
    else:
        print ("Please choose an available option")
