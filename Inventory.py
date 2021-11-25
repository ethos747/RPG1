# Course: CS 30
# Period: 3
# Date created: 10/19/2021
# Date last modified: 11/25/2021
# Name: Ethan Behl
# Description: Text-based RPG Inventory
try:
    import random
    import sys
    import Player
except ModuleNotFoundError:
    print("Error, a module was imported incorrectly on Inventory.")
    print("Game ended.")
    sys.exit()
dmg = 0


#Weapon classes
class Knife:
    def knife_attack():
        global dmg
        hit_chance = random.randint(0, 10)
        if hit_chance <= 4:
            print("\nKNIFE MISSED")
            print("You dealt: 0 DAMAGE")
            dmg = 0
        elif hit_chance >= 5:
            print("\nKNIFE HIT")
            print("You dealt: 4 DAMAGE")
            dmg = 4


class Pistol:
    def pistol_attack():
        global dmg
        hit_chance = random.randint(0, 10)
        if hit_chance <= 4:
            print("\nPISTOL MISSED")
            print("You dealt: 0 DAMAGE")
            dmg = 0
        elif hit_chance >= 5:
            print("\nPISTOL HIT")
            print("You dealt: 6 DAMAGE")
            dmg = 6


class Grenade_Weapon:
    def Grenade_Weapon_attack():
        global dmg
        dmg = 15
        print("The grenade explodes, disintegrating the enemy.")


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
        print("Damage:5")
    elif inv_input == "1":
        print("Combat knife usable in a variety of situations.")
        print("Hit chance: 50%")
        print("Damage:4")
    elif inv_input == "3":
        print("You can use this to increase health by 20%.")
        print("Kits remaining:" + str(Player.health_kits))
        if Player.health_kits >= 1:
            health_input = input("""
Use a kit?
[1] Yes
[2] No""")
            if health_input == "1":
                Player.health += 20
                Player.health_kits -= 1
                print("Health: " + str(Player.health) + "%")
            else:
                print("You did not us a health kit")
        else:
            print("You have no health kits left.")
    elif Player.Key == True:
        if inv_input == "4":
            print("Master Key that unlocks Client Rooms and the Dance Floor")
    elif Player.Grenade == 1:
        if inv_input == "5":
            print("A frag grenade able to take out almost any foe.")
            print("Hit chance: 100%")
            print("Damage:15")
    else:
        print ("Please choose an available option")
